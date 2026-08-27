+++
title = "Getting Skribisto 3"
description = "What is published today, what is not, and how to be there when it is."
template = "download.html"
weight = 2
aliases = ["/index.php/download/"]
+++

## There is nothing to install yet

That release carries no packaged build, and no earlier one does either. The release pipeline is written and produces a Flatpak bundle, a Windows installer, a portable zip and a macOS disk image, but it cannot run to completion until **Teksilo**, the GUI framework Skribisto 3 is built on, is published. Until then, building from source is not open to everyone either.

This page is generated from the GitHub releases API. The moment a release carries files, they appear above, with their sizes and checksums, and this section goes away.

**To know when that happens:** watch [the repository](https://github.com/jacquetc/skribisto) on GitHub, where releases will notify you, or join [the Discord](https://discord.gg/5BSkvQmyVH), where it will be said first.

## What will be published

| Platform | Package | Notes |
|---|---|---|
| Linux | Flatpak bundle | the supported way to run it on Linux |
| Windows | NSIS installer, plus a portable zip | the installer is the supported one |
| macOS | universal `.dmg` | unsigned for now; expect Gatekeeper to object |

Bug reports are most useful from a build that can be reproduced, which in practice means the Flatpak on Linux and the installer on Windows.

## What you can install today

Only one thing, and it is old: **Skribisto 1.9.41** on Flathub, from 2022. It is neither version 3 nor version 2, it is not developed any more, and it is not the application described on this site.

```
flatpak install flathub eu.skribisto.skribisto
```

Skribisto 2.0.7 was the last release of the C++ and Qt implementation. Its Windows installer link no longer resolves. Version 3 is a full rewrite in Rust with a new project format, and it is where everything since has gone. Your 2.x projects [open in it](@/coming-from-skribisto-2.md).

## What "alpha" means here

The project format is settled, it is documented, and it upgrades older projects when it opens them. The application around it has not had a stable release. When you can run it, keep backups of anything you cannot afford to lose. Skribisto takes its own, and any backup opens read-only, but a manuscript deserves belt and braces.
