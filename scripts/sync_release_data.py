#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Cyril Jacquet
"""Rebuild `data/release.toml` and `data/news.toml` from published facts.

The download page of a website is the one page that must never be optimistic. The
previous WordPress site advertised features the application did not have; this script
exists so the same thing cannot happen to a version number. Nothing here is written by
hand: the release data comes from the GitHub Releases API (what is actually published,
with the assets that are actually attached), and the news data comes from `NEWS.yml` in
the application repository, with every entry marked `released` only when a matching
published tag exists.

A fetch failure is fatal and leaves the existing data files untouched. A stale download
page is a small problem; a blank or invented one is not.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = "jacquetc/skribisto"
API = f"https://api.github.com/repos/{REPO}/releases?per_page=50"
# NEWS.yml is read from the working branch, not from `master`: `master` still holds the
# 2.x history, and an entry written ahead of its release is rendered as unreleased
# rather than hidden. Point `--news-ref` at `master` once 3.0 has landed there.
NEWS_REF = "dev"
NEWS_RAW = "https://raw.githubusercontent.com/{repo}/{ref}/NEWS.yml"
USER_AGENT = "skribisto-website-sync/1.0"
TIMEOUT = 30

# Filename patterns, most specific first: a portable zip must not be caught by the
# installer rule, and SHA256SUMS.txt is not a platform download at all.
ASSET_RULES: list[tuple[str, str, str]] = [
    (r"-setup\.exe$", "windows", "Windows installer"),
    (r"portable.*\.zip$", "windows", "Windows, portable"),
    (r"\.flatpak$", "linux", "Linux, Flatpak"),
    (r"\.AppImage$", "linux", "Linux, AppImage"),
    (r"linux.*\.tar\.(gz|xz|zst)$", "linux", "Linux, archive"),
    (r"\.dmg$", "macos", "macOS disk image"),
]

# A pre-release says which stage it is in, so the site can call a release candidate a
# release candidate without anyone editing a string. Derived from the tag, which is the
# only part of a release that cannot be wrong about this.
STAGES = ("alpha", "beta", "rc")
CHECKSUM_NAMES = ("SHA256SUMS.txt", "SHA256SUMS", "checksums.txt")


class SyncError(RuntimeError):
    """Anything that must abort the sync without touching the data files."""


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return response.read()
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
        raise SyncError(f"could not fetch {url}: {exc}") from exc


def toml_string(value: str) -> str:
    escaped = (
        value.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\t", "\\t")
    )
    return f'"{escaped}"'


PLATFORM_ORDER = ("linux", "windows", "macos")


def classify(name: str) -> tuple[str, str] | None:
    """Map an asset filename to a (platform, label) pair, or None if it is not a download."""
    for pattern, platform, label in ASSET_RULES:
        if re.search(pattern, name, re.IGNORECASE):
            return platform, label
    return None


def download_order(asset: dict) -> tuple[int, int]:
    """Sort key: platform first, then the rule order, which puts an installer above a zip.

    The API returns assets in upload order, which is whichever CI job finished first. The
    page should not reshuffle itself between releases, and neither should the diff.
    """
    name = asset["name"]
    for index, (pattern, platform, _) in enumerate(ASSET_RULES):
        if re.search(pattern, name, re.IGNORECASE):
            return PLATFORM_ORDER.index(platform), index
    return len(PLATFORM_ORDER), 0


def parse_checksums(text: str) -> dict[str, str]:
    """Parse `sha256sum` output into {filename: digest}."""
    digests: dict[str, str] = {}
    for line in text.splitlines():
        parts = line.split()
        if len(parts) >= 2 and re.fullmatch(r"[0-9a-f]{64}", parts[0], re.IGNORECASE):
            digests[parts[-1].lstrip("*")] = parts[0].lower()
    return digests


def stage_of(release: dict) -> str:
    """`alpha`, `beta`, `rc`, a bare `prerelease`, or empty for a final release."""
    tag = release.get("tag_name", "")
    for stage in STAGES:
        if re.search(rf"-{stage}", tag, re.IGNORECASE):
            return stage
    return "prerelease" if is_prerelease(release) else ""


def is_prerelease(release: dict) -> bool:
    """A tag carrying a hyphen is a pre-release.

    GitHub's own `prerelease` flag is not trustworthy for this repository: the alpha
    releases are flagged stable because they predate the workflow line that sets it.
    The tag is the fact.
    """
    return bool(release.get("prerelease")) or "-" in release.get("tag_name", "")


def pick_latest(releases: list[dict]) -> dict:
    published = [r for r in releases if not r.get("draft")]
    if not published:
        raise SyncError("the repository has no published release")
    published.sort(key=lambda r: r.get("published_at") or "", reverse=True)
    return published[0]


def build_release_data(releases: list[dict], checksums: dict[str, str]) -> str:
    latest = pick_latest(releases)
    tag = latest["tag_name"]
    version = tag.lstrip("v")
    published = (latest.get("published_at") or "")[:10]

    lines = [
        "# SPDX-License-Identifier: MIT",
        "# SPDX-FileCopyrightText: 2026 Cyril Jacquet",
        "#",
        "# Generated by scripts/sync_release_data.py. Do not edit by hand.",
        f"generated_at = {toml_string(datetime.now(timezone.utc).strftime('%Y-%m-%d'))}",
        f"tag = {toml_string(tag)}",
        f"version = {toml_string(version)}",
        f"published_at = {toml_string(published)}",
        f"prerelease = {'true' if is_prerelease(latest) else 'false'}",
        f"stage = {toml_string(stage_of(latest))}",
        f"url = {toml_string(latest.get('html_url', ''))}",
    ]

    checksum_url = ""
    for asset in latest.get("assets", []):
        if asset["name"] in CHECKSUM_NAMES:
            checksum_url = asset["browser_download_url"]
    lines.append(f"checksums_url = {toml_string(checksum_url)}")

    for asset in sorted(latest.get("assets", []), key=download_order):
        kind = classify(asset["name"])
        if kind is None:
            continue
        platform, label = kind
        lines += [
            "",
            "[[assets]]",
            f"platform = {toml_string(platform)}",
            f"label = {toml_string(label)}",
            f"name = {toml_string(asset['name'])}",
            f"url = {toml_string(asset['browser_download_url'])}",
            f"size = {int(asset.get('size', 0))}",
            # Formatted here rather than in the template: Tera has no number formatter,
            # and a page should not be doing arithmetic to print a file size.
            f"size_mb = {toml_string(f"{int(asset.get('size', 0)) / 1048576:.1f}")}",
            f"sha256 = {toml_string(checksums.get(asset['name'], ''))}",
        ]
    return "\n".join(lines) + "\n"


def parse_news(text: str) -> list[dict]:
    """Read NEWS.yml without a YAML dependency.

    The file is a stream of `---`-separated blocks of `Version:`, `Date:`, `Type:` and a
    `Description:` list of quoted bullets. Parsing it by hand keeps this script runnable
    on any machine with a bare Python, which is what CI has before it installs anything.
    """
    entries: list[dict] = []
    current: dict | None = None
    in_description = False
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.strip() == "---":
            if current and current.get("version"):
                entries.append(current)
            current, in_description = None, False
            continue
        match = re.match(r"^(Version|Date|Type):\s*(.*)$", line)
        if match:
            key, value = match.group(1).lower(), match.group(2).strip().strip('"')
            current = current or {"items": []}
            current[key] = value
            in_description = False
            continue
        if re.match(r"^Description:\s*$", line):
            current = current or {"items": []}
            in_description = True
            continue
        if in_description and current is not None:
            item = re.match(r"^\s*-\s*(.*)$", line)
            if item:
                current["items"].append(item.group(1).strip().strip('"'))
    if current and current.get("version"):
        entries.append(current)
    return entries


def build_news_data(news_text: str, releases: list[dict]) -> str:
    published_tags = {r["tag_name"] for r in releases if not r.get("draft")}
    published_versions = {tag.lstrip("v") for tag in published_tags}
    prerelease_versions = {
        r["tag_name"].lstrip("v") for r in releases if not r.get("draft") and is_prerelease(r)
    }

    lines = [
        "# SPDX-License-Identifier: MIT",
        "# SPDX-FileCopyrightText: 2026 Cyril Jacquet",
        "#",
        "# Generated by scripts/sync_release_data.py from NEWS.yml. Do not edit by hand.",
        "# `released` is true only when a matching tag is published on GitHub, so an entry",
        "# written ahead of its release can never render as if it had shipped.",
    ]
    for entry in parse_news(news_text):
        version = entry.get("version", "")
        released = version in published_versions
        lines += [
            "",
            "[[entries]]",
            f"version = {toml_string(version)}",
            f"date = {toml_string(entry.get('date', ''))}",
            f"type = {toml_string(entry.get('type', 'stable'))}",
            f"released = {'true' if released else 'false'}",
            f"prerelease = {'true' if version in prerelease_versions else 'false'}",
            "items = [",
        ]
        lines += [f"  {toml_string(item)}," for item in entry.get("items", [])]
        lines.append("]")
    return "\n".join(lines) + "\n"


def write_if_changed(path: Path, content: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="data", help="directory to write the data files into")
    parser.add_argument("--releases-json", help="read the releases list from this file instead of the API")
    parser.add_argument("--news-yml", help="read NEWS.yml from this file instead of the repository")
    parser.add_argument("--news-ref", default=NEWS_REF, help="branch or tag to read NEWS.yml from")
    args = parser.parse_args(argv)

    try:
        if args.releases_json:
            releases = json.loads(Path(args.releases_json).read_text(encoding="utf-8"))
        else:
            releases = json.loads(fetch(API).decode("utf-8"))
        if not isinstance(releases, list):
            raise SyncError("the releases endpoint did not return a list")

        news_text = (
            Path(args.news_yml).read_text(encoding="utf-8")
            if args.news_yml
            else fetch(NEWS_RAW.format(repo=REPO, ref=args.news_ref)).decode("utf-8")
        )

        checksums: dict[str, str] = {}
        latest = pick_latest(releases)
        for asset in latest.get("assets", []):
            if asset["name"] in CHECKSUM_NAMES and not args.releases_json:
                checksums = parse_checksums(fetch(asset["browser_download_url"]).decode("utf-8"))

        release_toml = build_release_data(releases, checksums)
        news_toml = build_news_data(news_text, releases)
    except SyncError as exc:
        print(f"sync failed, data files left untouched: {exc}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as exc:
        print(f"sync failed, data files left untouched: {exc}", file=sys.stderr)
        return 1

    out = Path(args.out)
    changed = write_if_changed(out / "release.toml", release_toml)
    changed |= write_if_changed(out / "news.toml", news_toml)
    print(f"{'updated' if changed else 'unchanged'}: {out}/release.toml, {out}/news.toml")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
