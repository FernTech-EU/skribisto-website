+++
title = "Get Skribisto 3"
description = "Skribisto 3 is out. There are builds for Linux, for Windows and for macOS."
template = "download.html"
weight = 2

# One table per platform, in the order the page shows them. `key` matches the
# `platform` the sync script gives each file of a release, and a platform with no
# file in the release is left out. `notes` stays on the page under the files;
# `more` folds away under `more_label`.

[[extra.platforms]]
key = "linux"
name = "Linux"
notes = """
On Ubuntu, Debian, Linux Mint and the other distributions built on them, take the package that matches your computer (x86-64 for most of them, ARM64 for an ARM machine) and open it with your software centre, or run `sudo apt install ./` followed by the file name. It needs Ubuntu 24.04 or Debian 13, or newer. A later version installs the same way, and Skribisto tells you when there is one.

Elsewhere, unpack the archive and run it, or take the Flatpak if that is what your distribution expects.
"""
more_label = "Found Skribisto 1.9.41 in your software centre?"
more = """
One warning. If you search for Skribisto in your software centre you could find **1.9.41**, from 2022. That is a different program from a different era, no longer developed, and it is not this.
"""

[[extra.platforms]]
key = "windows"
name = "Windows"
notes = """
Take the installer unless you have a reason not to.
"""

[[extra.platforms]]
key = "macos"
name = "macOS"
notes = """
Open the disk image and drag Skribisto into your Applications folder. It is a universal build: it runs on Apple Silicon and on Intel Macs alike.
"""
more_label = "If macOS refuses to open it"
more = """
macOS will complain the first time you open it, because the file does not yet carry the signature Apple asks for. Let it through from *System Settings ▸ Privacy & Security*, where it appears just after the refusal.
"""
+++

## What you are getting

Everything is in place: the writing, the notes, the story bible, the backups, the exports. This is version 3, released, and ready for a real manuscript.

Keep your usual backups, as you would with anything that holds your book. Skribisto also takes its own, as often as you tell it to, and you can open any of them to read without disturbing the one you are working in.

## If something goes wrong

Tell me. The most useful thing you can say is which of these you were running, on what kind of computer, what you were doing, and what you expected instead. [Where to say it](@/help.md).

## If you used Skribisto 2

Version 3 is not an update, it is a different program with a new file format. Your old projects still open in it, and are brought over as they load, without touching the original. [What else changed](@/coming-from-skribisto-2.md).
