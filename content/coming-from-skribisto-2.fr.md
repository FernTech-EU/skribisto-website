+++
title = "Vous venez de Skribisto 2 ou de Plume Creator"
description = "Vos anciens projets s’ouvrent. L’application autour d’eux n’a plus la même tête. Voici ce qui change."
weight = 5
+++

Skribisto 3 n’est pas Skribisto 2 repeint : c’est une réécriture : nouveau langage, nouvelle interface, nouveau format de projet. Ce qui a été délibérément préservé, c’est votre travail.

## Vos projets s’ouvrent

Un **projet Skribisto 2**, l’ancien fichier `.skrib` en SQLite, est reconnu à l’ouverture et mis à niveau au chargement vers le nouveau format. Le fichier d’origine n’est pas modifié : vous obtenez un nouveau projet à côté. Ouvrez-le et continuez d’écrire.

Un **projet Plume Creator** arrive par *Projet ▸ Importer depuis ▸ Plume Creator*, quelle que soit la version du format de Plume, et est converti vers un `.skrib` à jour. Là non plus, rien n’est réécrit dans l’original.

Vous pouvez aussi importer un livre qui n’a jamais vécu dans l’un ou l’autre : les fichiers Markdown, texte brut, DOCX et ODT entrent par *Projet ▸ Importer depuis ▸ Documents*, qui vous montre chaque ligne qu’il compte créer, et ce qu’il a dû deviner, avant que rien ne soit écrit.

<figure class="shot">
  <img src="/img/launcher.png" alt="Le lanceur, avec les projets récents et les exemples fournis." width="984" height="708" loading="lazy">
</figure>

## Ce qui est franchement mieux

- **Votre manuscrit est redevenu du texte brut.** Pas une base de données : des fichiers Djot et des manifestes lisibles, dans un zip ou dans un dossier que vous pouvez garder dans git.
- **La structure est explicite.** Une ligne est un chapitre ou une scène parce que vous l’avez dit, pas à cause de sa place dans l’arbre, et réorganiser l’arbre ne peut donc pas changer le livre.
- **Le texte et le synopsis ne font qu’un**, partout : dans l’éditeur, dans le tableau de liège, et sous forme de flux que l’on lit d’un bout à l’autre.
- **Commentaires, notes de bas de page, images, étiquettes, point de vue, mentions** : rien de tout cela n’existait dans la lignée 2.x.
- **L’export est un véritable compilateur** : neuf formats, un aperçu en direct, et un aller-retour éditorial qui ramène un DOCX ou un ODT de chez votre relecteur avec ses commentaires intacts.
- **Des sauvegardes réellement lisibles**, avec un historique des versions et une chronologie du projet construits à partir d’elles.

## Ce qui n’y est pas

Être honnête sur une réécriture importe davantage que d’en être enthousiaste.

- **Les langues.** Skribisto 2 était traduit dans plus de dix langues. La version 3 en a deux : l’anglais et le français. Le système de traduction est plus simple qu’avant : de simples fichiers texte, aucune chaîne d’outils. C’est donc la contribution la plus facile du projet, et celle dont j’ai le plus besoin. [Comment traduire](@/get-involved.md).
- **Les greffons.** Les anciennes interfaces de greffons ont disparu ; ce qu’elles apportaient est désormais intégré.
- **Les habitudes.** L’interface est vraiment différente. Le [manuel](https://manual.skribisto.eu/manual/) est le chemin le plus court, et la [FAQ](https://manual.skribisto.eu/faq/) couvre les questions qui reviennent.

## S’il manque quelque chose dont vous dépendiez

Dites-le. Une fonction qui comptait pour un vrai manuscrit vaut plus qu’une fonction qui sonnait bien dans un plan : [le suivi des tickets](https://github.com/jacquetc/skribisto/issues) ou [le Discord](https://discord.gg/5BSkvQmyVH).
