+++
title = "Participer"
description = "Traduction, documentation, code, et me dire ce qui ne marche pas."
weight = 8
+++

## Traduire

C’est aujourd’hui la contribution la plus utile, et elle ne demande ni chaîne de compilation ni Rust.

L’interface est traduite avec [Fluent](https://projectfluent.org). Chaque langue est un dossier de quatre fichiers texte :

```
crates/teksilo_ui/locales/en-US/{main,tooltips,tags,templates}.ftl
crates/teksilo_ui/locales/fr-FR/{main,tooltips,tags,templates}.ftl
```

Copiez le dossier `en-US` sous le code de votre langue, traduisez les valeurs à droite de chaque `=`, ouvrez une pull request. Rien d’autre ne change : pas de fichiers `.ts`, pas de `lupdate`, pas de compte Transifex. Ce que vous ne traduisez pas retombe sur l’anglais à l’exécution : une traduction partielle est donc réellement utile et peut être terminée plus tard.

Le [manuel et la FAQ](https://github.com/jacquetc/skribisto-help-website) se traduisent séparément et existent déjà en quatre langues.

## Écrire de la documentation

Le manuel n’est jamais fini. Pages manquantes, passages obscurs, captures d’écran périmées : tout cela mérite d’être corrigé, dans [le dépôt dédié](https://github.com/jacquetc/skribisto-help-website).

## Écrire du code

Skribisto est en Rust, édition 2024. Le [README](https://github.com/jacquetc/skribisto/blob/dev/README.md#build-it-test-it) décrit l’espace de travail et la compilation, et [CONTRIBUTING.md](https://github.com/jacquetc/skribisto/blob/dev/CONTRIBUTING.md) le reste. Les contributions sont acceptées sous un [CLA](https://github.com/jacquetc/skribisto/blob/dev/CLA.md) : vous gardez votre droit d’auteur, et votre travail restera disponible sous GPL.

Les tickets marqués [good first issue](https://github.com/jacquetc/skribisto/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) sont l’entrée en douceur.

## L’utiliser et râler

Très sérieusement : un rapport de bogue venant de quelqu’un qui écrit un vrai livre vaut plus qu’une demande de fonction venant de quelqu’un qui en imagine un. [Les tickets](https://github.com/jacquetc/skribisto/issues), ou [Discord](https://discord.gg/5BSkvQmyVH).

## Ou aider à payer le serveur

[Il y a un bouton](@/support.md), et rien n’est verrouillé derrière.
