+++
title = "Skribisto"
sort_by = "none"
template = "index.html"

[extra]
tagline = "a writing application for long-form work"
hero_title = "Write the book. Format it later."
hero_lede = "One project holds the lot: your book, or several, the chapters and scenes under them, and the notes and research beside them. Every piece of writing carries a summary of itself, and all of it is saved as text files you can open with anything."
hero_shot_alt = "The binder tree on the left, a scene's prose and its synopsis side by side in the editor."
export_shot_alt = "The export window, with a live preview of the compiled manuscript."
cta_note = "Free software, GPLv3 · Linux, Windows and macOS · current build:"

cards_title = "Three things worth knowing before you start"
cards_lede = "They are what makes Skribisto different from a folder of documents, and from an outliner that files your book into somebody else's boxes."




cards = [
  { title = "It fits how you write", body = "One project can hold several books, and a book as many chapters as you like, with scenes under them or without. A chapter can be a folder full of scenes, or a single page you write straight down, and both can live in the same book. You can keep more than one binder too, so the manuscript, the story bible and the research need not share a tree." },
  { title = "A summary beside every scene", body = "Each piece of writing carries a short account of what happens in it, in a box above the page or in a column beside it. Those summaries are what the corkboard puts on its cards, and you can read all of them, a whole book at a time, when you want the plan rather than the prose." },
  { title = "Files you can still open in ten years", body = "You write in a proper rich-text editor: bold, italics, headings, images. It is stored as Djot, a plain-text format much like Markdown, one file per scene, in a bundle you keep as a single file or as a folder under version control. No database, and nothing that needs Skribisto to be read." },
]

today_title = "What it does today"
today_lede = "Not a roadmap. This is the application as it stands."
today_link = "See it in more detail"
today = [
  "As many binders as a project needs, with full editing: create, rename, duplicate, move, indent, outdent, convert",
  "Your prose and its summary together, with split views and tabs",
  "Manuscript streams: read a whole chapter, part or book as one document",
  "A corkboard of summaries, an overview table, writing sessions and a live word count",
  "Pace planning with milestones, holidays and word targets",
  "Analysis of a book's shape: words per scene, how much of it is dialogue, how much sits in footnotes",
  "Anchored margin comments with threaded replies, and footnotes",
  "Note templates, colour tags, point-of-view marking and a mention index",
  "Images in the prose, carried through every export, and a book cover",
  "Replace-while-typing: your own lexicon plus locale-aware smart punctuation",
  "Distraction-free writing, with its own themes",
  "Search and replace across the whole project",
  "Trash and restore, with undo",
  "Version history and a project timeline, read out of the backups you already have",
  "Autosave, backups with retention and a scheduler, and read-only opening of any backup",
  "Import from Plume Creator, Markdown, plain text, DOCX and ODT",
  "Export to DOCX, ODT, EPUB, PDF, HTML, Markdown, Djot, LaTeX and plain text",
  "Spell checking with downloadable dictionaries",
  "Light and dark themes, per-editor typography, adjustable text scale",
  "An English and a French interface, and a screen-reader-driven accessibility tree",
]

promises_title = "Free software, and it stays that way"
promises_lede = "Skribisto is under the GNU General Public License v3.0. Four things about that are not going to move."
promises_link = "Read the whole commitment"
promises = [
  "Everything you need to write a book (creating, editing, opening, saving and exporting a manuscript, in every format Skribisto supports) is GPLv3, permanently.",
  "Your project stays readable. The .skrib bundle format is open and documented, and nothing can make one of your projects unreadable by free software.",
  "Nothing is taken back. No feature that has shipped will ever be moved out of the free application.",
  "No key, no server, no permission. Skribisto will never require a licence key, an activation step or a network connection to open or edit your own work.",
]

coming_title = "Coming from Plume Creator, or from Skribisto 2?"
coming_body = "A Skribisto 2 project is upgraded as it loads: open it and keep writing. A Plume Creator project comes in through Work ▸ Import from ▸ Plume Creator. Neither original file is modified, and the interface has changed enough that it is worth five minutes of reading first."
coming_link = "What changed, and what to expect"
+++

### Under the hood

Skribisto 3 is written in Rust, end to end. The interface is built on **Teksilo**, a pure-Rust GUI toolkit, so there is no Qt, no QML, no C++ and no browser engine in the build. It is a native desktop application that starts like one. The backend is generated from a single model file by [Qleany](https://github.com/jacquetc/qleany), which is why every operation in the application shares one undo stack and one event bus.

It also exposes a real accessibility tree, so a screen reader can drive it; NVDA and JAWS are the two used for testing. If you hit a gap there, [say so](https://github.com/jacquetc/skribisto/issues): that is a bug like any other.
