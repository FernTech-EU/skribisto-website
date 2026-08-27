+++
title = "Skribisto"
sort_by = "none"
template = "index.html"

[extra]
tagline = "a writing application for long-form work"
hero_title = "Write the book. Format it later."
hero_lede = "Skribisto organises a manuscript by what each piece is — book, part, chapter, scene, note — and keeps its prose and its synopsis side by side. Everything you write stays in plain text you can open without it."
hero_shot_alt = "The binder tree on the left, a scene's prose and its synopsis side by side in the editor."
export_shot_alt = "The export window, with a live preview of the compiled manuscript."
cta_note = "Free software, GPLv3 · Linux, Windows and macOS · current build"

cards_title = "Three ideas the whole application is built on"
cards_lede = "They are what makes Skribisto different from a folder of documents, and from every outliner that files your book in boxes."




cards = [
  { title = "Structure comes from meaning", body = "The binder tree is there to keep things tidy, and that is all it does. What makes a row a chapter or a scene is the role you give it — so you can move things around, indent, outdent and regroup without rewriting the shape of the book." },
  { title = "Prose and synopsis, together", body = "Every writing row owns both its text and a summary of it. That is why the editor has two panes — and why you can read a whole book's synopses as one continuous document when you need to see the plan rather than the prose." },
  { title = "Plain text you own", body = "A project is a .skrib bundle: Djot prose and readable manifests, kept as a single file or as a folder you can put under version control. No database, no proprietary blob, nothing that needs Skribisto to be read." },
]

today_title = "What it does today"
today_lede = "Not a roadmap. This is the application as it stands."
today_link = "See it in more detail"
today = [
  "A binder tree with full editing: create, rename, duplicate, move, indent, outdent, promote",
  "A dual editor pane, with split panes and tabs",
  "Manuscript streams: read a whole chapter, part or book as one document",
  "Corkboard, overview table, writing sessions and live word count",
  "Pace planning with milestones, holidays and word targets",
  "Analysis of a book's shape: words per scene, dialogue share, sentence and paragraph length",
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
  "Everything you need to write a book — creating, editing, opening, saving and exporting a manuscript, in every format Skribisto supports — is GPLv3, permanently.",
  "Your project stays readable. The .skrib bundle format is open and documented, and nothing can make one of your projects unreadable by free software.",
  "Nothing is taken back. No feature that has shipped will ever be moved out of the free application.",
  "No key, no server, no permission. Skribisto will never require a licence key, an activation step or a network connection to open or edit your own work.",
]

coming_title = "Coming from Plume Creator, or from Skribisto 2?"
coming_body = "A Skribisto 2 project is upgraded as it loads — open it and keep writing. A Plume Creator project comes in through Work ▸ Import from ▸ Plume Creator. Neither original file is modified, and the interface has changed enough that it is worth five minutes of reading first."
coming_link = "What changed, and what to expect"
+++

### Under the hood

Skribisto 3 is written in Rust, end to end. The interface is built on **Teksilo**, a pure-Rust GUI toolkit, so there is no Qt, no QML, no C++ and no browser engine in the build — it is a native desktop application that starts like one. The backend is generated from a single model file by [Qleany](https://github.com/jacquetc/qleany), which is why every operation in the application shares one undo stack and one event bus.

It also exposes a real accessibility tree, so a screen reader can drive it; NVDA and JAWS are the two used for testing. If you hit a gap there, [say so](https://github.com/jacquetc/skribisto/issues) — that is a bug like any other.
