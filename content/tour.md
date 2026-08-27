+++
title = "A tour of Skribisto"
description = "What a book looks like inside Skribisto: how it is structured, how you write it, how you see it, and how it gets out."
weight = 1
+++

## 1. Structure

A project opens on a **binder**: a tree of folders and items down the side. The tree is organisational. It is not the book.

What makes a row part of the book is the **role** you give it — Book, Part, Chapter, Scene, Note, or plain text — and roles compose. A chapter can be a folder holding scenes, or a single flat row if that is how you think; the same project reads either way. Because the structure is carried by the rows and not by the nesting, you can regroup the tree, indent, outdent and reorder without the manuscript changing shape underneath you.

<figure class="shot">
  <img src="/img/binder-and-editor.png" alt="The binder tree on the left, a scene's prose and its synopsis side by side in the editor." width="1440" height="960" loading="lazy">
</figure>

Two more things fall out of that:

- **Promote.** A scene becomes a note, a flat chapter becomes a chapter folder, and the prose comes with it.
- **Streams.** A chapter, a part or a whole book can be read as one continuous document — and so can every synopsis in it, which is the fastest way to see the plan without the prose.

## 2. Write

Every writing row owns two texts: its **prose** and its **synopsis**. The editor shows both, side by side or stacked, and each pane has its own typography — face, size, leading and indent — because a synopsis is not read the way a scene is.

Around that:

- **Distraction-free mode** with its own themes, for when the rest of the interface is in the way.
- **Replace-while-typing**, in two layers: your own lexicon of abbreviations and corrections, and locale-aware smart punctuation — curly quotes, dashes, ellipses, French spacing, guillemets, dialogue dashes. Backspace reverts a replacement instead of fighting you.
- **Spell checking** with dictionaries you download from inside the application, and a per-project word list.
- **Footnotes**, numbered from the manuscript rather than stored, so inserting one in chapter two does not leave chapter nine wrong.
- **Images** in the prose — a map, a face, a photograph of a street — carried inside the project and through every export, plus a cover for the book.
- **Note templates**: character sheet, location, object, beat sheet, faction, research note, or your own saved from any note.

## 3. See

A manuscript is easier to write when you can look at it from further away.

- **Corkboard** — the scenes of a chapter or part as cards you can read and reorder.
- **Overview** — a table of the subtree: title, type, label, tags, own words, total words, open comments.
- **Analysis** — the shape of a book measured against its own numbers, never against a norm: words per scene, dialogue share, sentence and paragraph length, punctuation density.
- **Pace** — a plan with a deadline, milestones and the days you are not writing, against the words you actually wrote.
- **Comments** — anchored in the margin, LibreOffice-style, with threaded replies, a project-wide dock and a per-document one.
- **Tags, point of view and mentions** — colour tags with genre presets, the cast member whose head a scene is in, and an index of every place a tagged character or location is named in the prose.
- **Timeline and version history** — what a scene said last Tuesday, read out of the backups you already have, with a diff.

## 4. Finish

Skribisto is not a word processor, and does not try to be. It compiles the manuscript and hands it to whichever program you finish in.

<figure class="shot">
  <img src="/img/export-preview.png" alt="The export window, with a live preview of the compiled manuscript." width="1440" height="960" loading="lazy">
</figure>

- **Nine formats**: DOCX, ODT, EPUB, PDF, HTML, Markdown, Djot, LaTeX and plain text, with a live preview of what will come out and per-format style presets.
- **The editorial round trip closes.** Send a chapter out as DOCX or ODT, get it back marked up, and the comments come home to the rows they belong to — matched against the prose that is actually stored, not against a line number.
- **Backups** with a retention policy, several destinations and a scheduler; any backup opens read-only, so you can look without risking the live project.
- **Your project, without Skribisto.** The `.skrib` bundle is a zip of Djot prose and readable manifests — or an exploded folder, which is what you want if the manuscript lives in git. A plain Markdown viewer pointed at that folder shows you your book, images included.

<div class="callout">
  <h3>Not in the box</h3>
  <p>There is no cloud sync, no collaborative editing, no account, and no plugin system — the last of these existed in Skribisto 2 and was not rebuilt. The interface is available in English and French only.</p>
</div>
