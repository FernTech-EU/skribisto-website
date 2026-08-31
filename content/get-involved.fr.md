+++
title = "Participer"
description = "Traduction, documentation, code, et me dire ce qui ne marche pas."
weight = 8
+++

## Traduire

C’est aujourd’hui la contribution la plus utile, et traduire ne demande aucune programmation.

Chaque langue est un dossier de cinq fichiers texte, au format [Fluent](https://projectfluent.org) :

```
crates/teksilo_ui/locales/fr-FR/{main,tooltips,tags,templates,story_bible}.ftl
```

Copiez le dossier `en-US` sous le code de votre langue et traduisez le texte à droite de chaque `=`. Ce que vous n’avez pas encore fait retombe sur l’anglais pendant votre travail : une langue à moitié faite est donc réellement utile, et peut être terminée plus tard, ou par quelqu’un d’autre.

**Vous pouvez voir votre travail apparaître au fil des enregistrements.** Une version que vous avez compilée vous-même surveille votre dossier et recharge la langue à chaque fichier écrit : Skribisto reste ouvert à côté de votre éditeur de texte.

```
cargo run -p teksilo_ui -- --translation-dev fr-FR=crates/teksilo_ui/locales/fr-FR
```

Indiquez le dossier, jamais un seul fichier à l’intérieur. Une langue, ce sont ces cinq fichiers pris ensemble, et n’en recharger qu’un viderait les quatre autres, ce qui ressemble exactement à une traduction effacée. L’option refuse un fichier plutôt que de vous le laisser découvrir, et elle n’existe que dans les versions de développement.

Les pages d’aide, plus longues, sont à part : dix pages par langue, écrites en Djot et non en Fluent, sous `crates/teksilo_ui/help/`.

Une langue entièrement nouvelle doit en outre être déclarée à trois endroits du code avant que ses textes ne soient intégrés à l’application. Ce sont trois courtes modifications, détaillées dans le [README](https://github.com/jacquetc/skribisto/blob/dev/README.md#translation), et aucun système de compilation à apprendre.

## Écrire l’aide

L’aide n’est jamais finie. Une rubrique qui explique la mauvaise chose, ou qui n’existe pas du tout, est un défaut comme un autre. Les pages sont rangées à côté des traductions, dans les sources de l’application, et ce sont de simples textes : si vous voyez ce qui manque, vous pouvez l’écrire.

## Écrire du code

Skribisto est en Rust, édition 2024. Le [README](https://github.com/jacquetc/skribisto/blob/dev/README.md#build-it-test-it) décrit l’espace de travail et la compilation, et [CONTRIBUTING.md](https://github.com/jacquetc/skribisto/blob/dev/CONTRIBUTING.md) le reste. Les contributions sont acceptées sous un [CLA](https://github.com/jacquetc/skribisto/blob/dev/CLA.md) : vous gardez votre droit d’auteur, et votre travail restera disponible sous GPL.

Les tickets marqués [good first issue](https://github.com/jacquetc/skribisto/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) sont l’entrée en douceur.

## L’utiliser et râler

Très sérieusement : un rapport de bogue venant de quelqu’un qui écrit un vrai livre passe avant une demande de fonction venant de quelqu’un qui en imagine un. [Les tickets](https://github.com/jacquetc/skribisto/issues), ou [Discord](https://discord.gg/5BSkvQmyVH).

## L’argent

Il n’y a nulle part où l’envoyer, [et voici pourquoi](@/support.md).
