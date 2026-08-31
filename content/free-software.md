+++
title = "Free software, and it stays that way"
description = "Skribisto is GPLv3. Here is exactly what that guarantees you, and what it does not."
weight = 4
+++

Skribisto is free software under the [GNU General Public License v3.0](https://github.com/jacquetc/skribisto/blob/dev/LICENSE). You can use it for anything, read all of it, change it, and pass it on.

That is the licence. What follows is the commitment, which is a different thing, and the one that actually matters when you are deciding whether to put three years of work into an application.

## Four things that do not move

<ul class="promises">
  <li><strong>Everything you need to write a book is GPLv3, permanently.</strong> Creating, editing, opening, saving and exporting a manuscript, in every format Skribisto supports, is free-software work and stays there.</li>
  <li><strong>Your project stays readable.</strong> The <code>.skrib</code> bundle format is open and documented, and a project remains readable, editable and exportable by free software, whatever else ever touches it.</li>
  <li><strong>Nothing is taken back.</strong> No feature that has shipped will ever be removed and put somewhere you have to pay to reach.</li>
  <li><strong>No key, no server, no permission.</strong> Skribisto will never require a licence key, an activation step, or a network connection to open or edit your own work.</li>
</ul>

## What your project actually is

You write in a rich-text editor, and it is stored as text. A `.skrib` project is a zip archive, or an exploded folder if you prefer, containing:

- your prose as [Djot](https://djot.net) files, one per scene, in plain UTF-8 text. Djot is close enough to Markdown that you can read a scene at a glance;
- a readable index of the structure beside them, in plain text as well;
- your images under `assets/`, named by the hash of their own bytes.

Point a text editor at it. Point `git` at the folder form and get real diffs of your novel. Nothing in there needs Skribisto to be understood, which is the whole point: an application should not be able to hold your book hostage, including this one.

## No account, no telemetry

Skribisto has no account system, sends no usage data, and needs no network connection to do its work. It reaches the network for exactly one thing, when you ask it to: downloading a spelling dictionary.

## Contributing, and the CLA

Contributions are welcome, and are accepted under a [Contributor License Agreement](https://github.com/jacquetc/skribisto/blob/dev/CLA.md) rather than a bare sign-off. You keep the copyright to your work, and in return your contribution is guaranteed to remain available under the GPL. [How to contribute](@/get-involved.md).

## Trademark

Skribisto™ is a trademark of FernTech, and the GPL grants no trademark rights. Fork the code freely, which is what the licence is for, but a fork distributed to others needs its own name and its own branding, the way Iceweasel did with Firefox. Saying "built on Skribisto", or writing about it, needs no permission at all. Anything else: <trademarks@ferntech.eu>.
