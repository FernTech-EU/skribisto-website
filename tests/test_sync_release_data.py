# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Cyril Jacquet
"""Tests for the release-data sync.

The point of the script is that the download page cannot claim something that is
not published, so these tests are mostly about the negative cases: a release with
no assets, an entry written ahead of its release, and a failed fetch.
"""

import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("sync", ROOT / "scripts" / "sync_release_data.py")
sync = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sync)


def release(tag, published, assets=(), draft=False, prerelease=False):
    return {
        "tag_name": tag,
        "published_at": published,
        "draft": draft,
        "prerelease": prerelease,
        "html_url": f"https://github.com/jacquetc/skribisto/releases/tag/{tag}",
        "assets": [
            {"name": n, "size": s, "browser_download_url": f"https://example.invalid/{n}"}
            for n, s in assets
        ],
    }


NEWS = """Version: 3.0.0
Date: 2026-07-19
Type: stable
Description:
- "Rewritten in Rust"
- "New project format"
---
Version: 2.0.7
Date: 2026-02-21
Type: stable
Description:
- "Bug fixes"
"""


class TestAssetClassification(unittest.TestCase):
    def test_each_package_lands_on_its_platform(self):
        self.assertEqual(sync.classify("Skribisto-setup.exe")[0], "windows")
        self.assertEqual(sync.classify("Skribisto-portable.zip")[0], "windows")
        self.assertEqual(sync.classify("skribisto.flatpak")[0], "linux")
        self.assertEqual(sync.classify("Skribisto.dmg")[0], "macos")

    def test_the_installer_rule_wins_over_the_zip_rule(self):
        # Both files are Windows, but they must not carry the same label.
        self.assertNotEqual(
            sync.classify("Skribisto-setup.exe")[1],
            sync.classify("Skribisto-portable.zip")[1],
        )

    def test_a_linux_tarball_is_a_download(self):
        # rc1 shipped a tarball rather than the Flatpak bundle the pipeline was written
        # for, and an unmatched asset is silently dropped from the page.
        kind = sync.classify("skribisto-v3.0.0-rc1-linux-x86_64.tar.gz")
        self.assertIsNotNone(kind)
        self.assertEqual(kind[0], "linux")

    def test_a_windows_portable_zip_is_not_read_as_a_linux_archive(self):
        self.assertEqual(sync.classify("Skribisto-portable.zip")[0], "windows")

    def test_a_checksum_file_is_not_a_download(self):
        self.assertIsNone(sync.classify("SHA256SUMS.txt"))

    def test_an_unknown_file_is_not_a_download(self):
        self.assertIsNone(sync.classify("release_notes.md"))


class TestStage(unittest.TestCase):
    def test_the_tag_names_the_stage(self):
        for tag, expected in (
            ("v3.0.0-alpha2", "alpha"),
            ("v3.0.0-beta1", "beta"),
            ("v3.0.0-rc1", "rc"),
            ("v3.0.0", ""),
        ):
            self.assertEqual(sync.stage_of(release(tag, "2026-08-31T00:00:00Z")), expected)

    def test_an_unrecognised_prerelease_still_says_so(self):
        r = release("v3.0.0.pre", "2026-08-31T00:00:00Z", prerelease=True)
        self.assertEqual(sync.stage_of(r), "prerelease")


class TestChecksums(unittest.TestCase):
    def test_parses_sha256sum_output(self):
        digest = "a" * 64
        parsed = sync.parse_checksums(f"{digest}  skribisto.flatpak\n{'b' * 64} *Setup.exe\n")
        self.assertEqual(parsed["skribisto.flatpak"], digest)
        self.assertEqual(parsed["Setup.exe"], "b" * 64)

    def test_ignores_lines_that_are_not_digests(self):
        self.assertEqual(sync.parse_checksums("not a checksum line\n"), {})


class TestReleaseSelection(unittest.TestCase):
    def test_drafts_are_never_chosen(self):
        releases = [
            release("v9.9.9", "2026-08-01T00:00:00Z", draft=True),
            release("v3.0.0-alpha2", "2026-07-15T00:00:00Z"),
        ]
        self.assertEqual(sync.pick_latest(releases)["tag_name"], "v3.0.0-alpha2")

    def test_no_published_release_is_an_error(self):
        with self.assertRaises(sync.SyncError):
            sync.pick_latest([release("v1", "2026-01-01T00:00:00Z", draft=True)])

    def test_a_hyphenated_tag_is_a_prerelease_even_when_github_says_otherwise(self):
        # The alpha releases are flagged stable on GitHub; the tag is the fact.
        self.assertTrue(sync.is_prerelease(release("v3.0.0-alpha2", "2026-07-15T00:00:00Z")))
        self.assertFalse(sync.is_prerelease(release("v3.0.0", "2026-07-19T00:00:00Z")))

    def test_publication_date_does_not_decide_which_release_is_newest(self):
        # Real data from this repository: v1.9.43 (the retired QWidgets codebase)
        # was published two hours AFTER v2.0.7 on the same day. Sorting by
        # published_at picks the older line's tag as the current release.
        releases = [
            release("v2.0.7", "2026-02-21T14:43:04Z"),
            release("v1.9.43", "2026-02-21T16:49:25Z"),
        ]
        self.assertEqual(sync.pick_latest(releases)["tag_name"], "v2.0.7")

    def test_a_release_outranks_its_own_release_candidate(self):
        releases = [
            release("v3.1.0-rc1", "2026-10-01T00:00:00Z"),
            release("v3.1.0", "2026-10-05T00:00:00Z"),
        ]
        self.assertEqual(sync.pick_latest(releases)["tag_name"], "v3.1.0")
        # ...and still does when the candidate is republished afterwards.
        releases[0]["published_at"] = "2026-10-09T00:00:00Z"
        self.assertEqual(sync.pick_latest(releases)["tag_name"], "v3.1.0")

    def test_version_key_follows_semver_precedence(self):
        k = sync.version_key
        self.assertLess(k("v3.0.0-alpha1"), k("v3.0.0-alpha2"))
        self.assertLess(k("v3.0.0-alpha2"), k("v3.0.0-beta1"))
        self.assertLess(k("v3.0.0-rc1"), k("v3.0.0"))
        self.assertLess(k("v3.0.0"), k("v3.0.1"))
        self.assertLess(k("v3.0.9"), k("v3.1.0"))
        # Numeric pre-release identifiers compare numerically, not as text.
        self.assertLess(k("v3.0.0-rc.2"), k("v3.0.0-rc.10"))
        # Build metadata is ignored by precedence.
        self.assertEqual(k("v3.0.1"), k("v3.0.1+5c62c8cac"))


class TestStableSelection(unittest.TestCase):
    """`pick_latest_stable` feeds the application's update check.

    The download page may legitimately headline a release candidate; the update
    notice may never do so, because a reader on the stable line cannot act on it.
    """

    def test_a_release_candidate_is_never_the_stable_release(self):
        releases = [
            release("v3.1.0-rc2", "2026-10-01T00:00:00Z"),
            release("v3.0.1", "2026-09-03T00:00:00Z"),
        ]
        # This is the live failure: GitHub flags every tag in this repository
        # `prerelease: false`, so /releases/latest would serve the rc.
        self.assertEqual(sync.pick_latest(releases)["tag_name"], "v3.1.0-rc2")
        self.assertEqual(sync.pick_latest_stable(releases)["tag_name"], "v3.0.1")

    def test_drafts_are_excluded_from_the_stable_pick_too(self):
        releases = [
            release("v4.0.0", "2026-11-01T00:00:00Z", draft=True),
            release("v3.0.1", "2026-09-03T00:00:00Z"),
        ]
        self.assertEqual(sync.pick_latest_stable(releases)["tag_name"], "v3.0.1")

    def test_no_final_release_yields_no_feed_rather_than_an_empty_one(self):
        releases = [release("v3.0.0-alpha1", "2026-07-11T00:00:00Z")]
        self.assertIsNone(sync.pick_latest_stable(releases))


class TestUpdatesFeed(unittest.TestCase):
    def test_the_feed_names_the_version_and_both_languages(self):
        feed = json.loads(
            sync.build_updates_feed(release("v3.0.1", "2026-09-03T13:42:53Z"))
        )
        self.assertEqual(feed["feed"], sync.FEED_SCHEMA)
        self.assertEqual(feed["version"], "3.0.1")
        self.assertEqual(feed["tag"], "v3.0.1")
        self.assertEqual(feed["date"], "2026-09-03")
        self.assertEqual(feed["download"]["en"], "https://www.skribisto.eu/download/")
        self.assertEqual(feed["download"]["fr"], "https://www.skribisto.eu/fr/download/")
        self.assertEqual(feed["notes"]["en"], "https://www.skribisto.eu/news/")
        self.assertEqual(feed["notes"]["fr"], "https://www.skribisto.eu/fr/news/")

    def test_the_feed_carries_nothing_about_the_client(self):
        # The feed is fetched by every installation with the check enabled. It
        # must stay a statement about the release and nothing else.
        feed = json.loads(
            sync.build_updates_feed(release("v3.0.1", "2026-09-03T13:42:53Z"))
        )
        self.assertEqual(
            set(feed), {"feed", "version", "tag", "date", "notes", "download"}
        )

    def test_the_feed_is_small_enough_to_be_free_to_fetch(self):
        body = sync.build_updates_feed(release("v3.0.1", "2026-09-03T13:42:53Z"))
        self.assertLess(
            len(body.encode("utf-8")),
            1024,
            "the whole point of not polling the GitHub API is that this is tiny",
        )


class TestReleaseData(unittest.TestCase):
    def test_a_release_with_no_assets_yields_no_asset_rows(self):
        data = sync.build_release_data([release("v3.0.0-alpha2", "2026-07-15T17:39:43Z")], {})
        self.assertIn('version = "3.0.0-alpha2"', data)
        self.assertIn('published_at = "2026-07-15"', data)
        self.assertIn("prerelease = true", data)
        self.assertIn('stage = "alpha"', data)
        self.assertNotIn("[[assets]]", data)

    def test_assets_carry_their_checksum(self):
        digest = "c" * 64
        data = sync.build_release_data(
            [
                release(
                    "v3.0.0",
                    "2026-07-19T00:00:00Z",
                    assets=[("skribisto.flatpak", 42), ("SHA256SUMS.txt", 100)],
                )
            ],
            {"skribisto.flatpak": digest},
        )
        self.assertIn("[[assets]]", data)
        self.assertIn(f'sha256 = "{digest}"', data)
        self.assertIn('checksums_url = "https://example.invalid/SHA256SUMS.txt"', data)
        # The checksum file itself is not offered as a platform download.
        self.assertEqual(data.count("[[assets]]"), 1)

    def test_a_size_is_formatted_for_the_page(self):
        data = sync.build_release_data(
            [release("v3.0.0-rc1", "2026-08-31T00:00:00Z", assets=[("skribisto-linux.tar.gz", 45658335)])],
            {},
        )
        self.assertIn('size_mb = "43.5"', data)

    def test_downloads_are_ordered_by_platform_not_by_upload_time(self):
        data = sync.build_release_data(
            [
                release(
                    "v3.0.0-rc1",
                    "2026-08-31T00:00:00Z",
                    assets=[
                        ("Skribisto-portable.zip", 1),
                        ("Skribisto-setup.exe", 2),
                        ("skribisto-v3.0.0-rc1-linux-x86_64.tar.gz", 3),
                    ],
                )
            ],
            {},
        )
        names = re.findall(r'name = "([^"]+)"', data)
        self.assertEqual(
            names,
            [
                "skribisto-v3.0.0-rc1-linux-x86_64.tar.gz",
                "Skribisto-setup.exe",
                "Skribisto-portable.zip",
            ],
        )

    def test_quotes_in_a_name_cannot_break_the_toml(self):
        self.assertEqual(sync.toml_string('a"b'), '"a\\"b"')


class TestNewsData(unittest.TestCase):
    def test_parses_every_entry_and_its_bullets(self):
        entries = sync.parse_news(NEWS)
        self.assertEqual([e["version"] for e in entries], ["3.0.0", "2.0.7"])
        self.assertEqual(entries[0]["items"][0], "Rewritten in Rust")
        self.assertEqual(len(entries[0]["items"]), 2)

    def test_an_entry_without_a_published_tag_is_marked_unreleased(self):
        data = sync.build_news_data(NEWS, [release("v2.0.7", "2026-02-21T00:00:00Z")])
        first, second = data.split("[[entries]]")[1:3]
        self.assertIn('version = "3.0.0"', first)
        self.assertIn("released = false", first)
        self.assertIn('version = "2.0.7"', second)
        self.assertIn("released = true", second)


class TestFileWriting(unittest.TestCase):
    def test_write_if_changed_reports_no_change(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "release.toml"
            self.assertTrue(sync.write_if_changed(path, "a"))
            self.assertFalse(sync.write_if_changed(path, "a"))
            self.assertTrue(sync.write_if_changed(path, "b"))

    def test_a_failed_run_leaves_the_existing_data_untouched(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "data"
            out.mkdir()
            (out / "release.toml").write_text("previous good data", encoding="utf-8")
            code = sync.main(
                ["--out", str(out), "--releases-json", str(Path(tmp) / "missing.json"),
                 "--news-yml", str(Path(tmp) / "missing.yml")]
            )
            self.assertEqual(code, 1)
            self.assertEqual((out / "release.toml").read_text(encoding="utf-8"), "previous good data")

    def test_an_offline_run_writes_both_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            (tmp / "releases.json").write_text(
                json.dumps([release("v3.0.0-alpha2", "2026-07-15T17:39:43Z")]), encoding="utf-8"
            )
            (tmp / "NEWS.yml").write_text(NEWS, encoding="utf-8")
            out = tmp / "data"
            code = sync.main(
                ["--out", str(out), "--releases-json", str(tmp / "releases.json"),
                 "--news-yml", str(tmp / "NEWS.yml")]
            )
            self.assertEqual(code, 0)
            self.assertIn('tag = "v3.0.0-alpha2"', (out / "release.toml").read_text(encoding="utf-8"))
            self.assertIn('version = "3.0.0"', (out / "news.toml").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
