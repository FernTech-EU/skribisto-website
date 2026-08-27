# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Cyril Jacquet
"""Tests for the release-data sync.

The point of the script is that the download page cannot claim something that is
not published, so these tests are mostly about the negative cases: a release with
no assets, an entry written ahead of its release, and a failed fetch.
"""

import importlib.util
import json
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

    def test_a_checksum_file_is_not_a_download(self):
        self.assertIsNone(sync.classify("SHA256SUMS.txt"))

    def test_an_unknown_file_is_not_a_download(self):
        self.assertIsNone(sync.classify("release_notes.md"))


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


class TestReleaseData(unittest.TestCase):
    def test_a_release_with_no_assets_yields_no_asset_rows(self):
        data = sync.build_release_data([release("v3.0.0-alpha2", "2026-07-15T17:39:43Z")], {})
        self.assertIn('version = "3.0.0-alpha2"', data)
        self.assertIn('published_at = "2026-07-15"', data)
        self.assertIn("prerelease = true", data)
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
