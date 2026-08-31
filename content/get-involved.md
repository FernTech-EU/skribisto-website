+++
title = "Get involved"
description = "Translation, documentation, code, and telling me what is broken."
weight = 8
aliases = ["/index.php/contribute/"]
+++

## Translate it

This is the most useful thing anyone can do right now, and the translating itself needs no programming.

Each language is a folder of five plain text files, in [Fluent](https://projectfluent.org) format:

```
crates/teksilo_ui/locales/fr-FR/{main,tooltips,tags,templates,story_bible}.ftl
```

Copy the `en-US` folder to your language code and translate the text to the right of each `=`. Anything you have not got to yet falls back to English while you work, so a half-finished language is genuinely useful, and can be finished later or by somebody else.

**You can watch your work appear as you save it.** A build you have compiled yourself will watch your folder and reload the language every time you write a file, so Skribisto stays open beside your text editor:

```
cargo run -p teksilo_ui -- --translation-dev fr-FR=crates/teksilo_ui/locales/fr-FR
```

Point it at the folder, never at a single file inside it. A language is those five files taken together, and reloading one of them alone would empty the other four, which looks exactly like your translation being deleted. The flag refuses a file rather than let you find that out the hard way, and it is for development builds only.

The longer help pages are separate: ten pages per language, written in plain Djot rather than Fluent, under `crates/teksilo_ui/help/`.

A brand-new language also has to be declared in three places in the source before its strings are built into the application. That is three short edits, spelled out in the [README](https://github.com/jacquetc/skribisto/blob/dev/README.md#translation), and no build system to learn.

## Write help

The help is never finished. A topic that explains the wrong thing, or does not exist at all, is a defect like any other. The pages sit beside the translations, in the application's own source, and they are ordinary text: if you can spot what is missing, you can write it.

## Write code

Skribisto is Rust, edition 2024. The [README](https://github.com/jacquetc/skribisto/blob/dev/README.md#build-it-test-it) explains the workspace and how to build it, and [CONTRIBUTING.md](https://github.com/jacquetc/skribisto/blob/dev/CONTRIBUTING.md) explains the rest. Contributions are accepted under a [CLA](https://github.com/jacquetc/skribisto/blob/dev/CLA.md): you keep your copyright, and your work is guaranteed to stay available under the GPL.

Issues tagged [good first issue](https://github.com/jacquetc/skribisto/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) are the gentle end.

## Use it and complain

Genuinely: a bug report from someone writing a real book beats a feature request from someone imagining one. [Issues](https://github.com/jacquetc/skribisto/issues), or [Discord](https://discord.gg/5BSkvQmyVH).

## Money

There is nowhere to send any, [and this is why](@/support.md).
