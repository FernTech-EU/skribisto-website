+++
title = "Get involved"
description = "Translation, documentation, code, and telling me what is broken."
weight = 8
aliases = ["/index.php/contribute/"]
+++

## Translate it

This is the most useful thing anyone can do right now, and it needs no build system and no Rust.

The interface is translated with [Fluent](https://projectfluent.org). Each language is a directory of four plain text files:

```
crates/teksilo_ui/locales/en-US/{main,tooltips,tags,templates}.ftl
crates/teksilo_ui/locales/fr-FR/{main,tooltips,tags,templates}.ftl
```

Copy the `en-US` directory to your locale code, translate the values on the right of each `=`, open a pull request. Nothing else changes: no `.ts` files, no `lupdate`, no Transifex account. Anything you do not translate falls back to English at runtime, so a partial translation is genuinely useful and can be finished later.

The help topics inside the application are translated the same way, in the same files, so improving them is the same kind of pull request.

## Write help

The help is never finished. A topic that explains the wrong thing, or does not exist, is worth as much to fix as a bug: it lives in the application's own source, alongside the strings above.

## Write code

Skribisto is Rust, edition 2024. The [README](https://github.com/jacquetc/skribisto/blob/dev/README.md#build-it-test-it) explains the workspace and how to build it, and [CONTRIBUTING.md](https://github.com/jacquetc/skribisto/blob/dev/CONTRIBUTING.md) explains the rest. Contributions are accepted under a [CLA](https://github.com/jacquetc/skribisto/blob/dev/CLA.md): you keep your copyright, and your work is guaranteed to stay available under the GPL.

Issues tagged [good first issue](https://github.com/jacquetc/skribisto/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) are the gentle end.

## Use it and complain

Genuinely: a bug report from someone writing a real book is worth more than a feature request from someone imagining one. [Issues](https://github.com/jacquetc/skribisto/issues), or [Discord](https://discord.gg/5BSkvQmyVH).

## Or help pay for the server

[There is a button](@/support.md), and nothing behind it is locked.
