+++
title = "Obtenir Skribisto 3"
description = "Ce qui est publié aujourd’hui, ce qui ne l’est pas, et comment être là quand ce sera le cas."
template = "download.html"
weight = 2
+++

## Il n’y a encore rien à installer

Cette version ne comporte aucun paquet, et aucune version antérieure non plus. La chaîne de publication est écrite et produit un paquet Flatpak, un installeur Windows, une archive portable et une image disque macOS, mais elle ne peut pas aller à son terme tant que **Teksilo**, la bibliothèque graphique sur laquelle Skribisto 3 est bâti, n’est pas publiée. D’ici là, compiler depuis les sources n’est pas non plus à la portée de tout le monde.

Cette page est engendrée à partir de l’API des versions de GitHub. Dès qu’une version portera des fichiers, ils apparaîtront ci-dessus, avec leur taille et leur empreinte, et cette section disparaîtra.

**Pour le savoir à ce moment-là** : suivez [le dépôt](https://github.com/jacquetc/skribisto) sur GitHub, où les nouvelles versions vous seront notifiées, ou rejoignez [le Discord](https://discord.gg/5BSkvQmyVH), où cela sera dit en premier.

## Ce qui sera publié

| Plateforme | Paquet | Remarques |
|---|---|---|
| Linux | paquet Flatpak | la manière prise en charge sous Linux |
| Windows | installeur NSIS, plus une archive portable | l’installeur est celui qui est pris en charge |
| macOS | `.dmg` universel | non signé pour l’instant : Gatekeeper protestera |

Un rapport de bogue est surtout utile s’il provient d’une version reproductible, c’est-à-dire en pratique le Flatpak sous Linux et l’installeur sous Windows.

## Ce que vous pouvez installer aujourd’hui

Une seule chose, et elle est ancienne : **Skribisto 1.9.41** sur Flathub, datant de 2022. Ce n’est ni la version 3 ni la version 2, elle n’est plus développée, et ce n’est pas l’application décrite sur ce site.

```
flatpak install flathub eu.skribisto.skribisto
```

Skribisto 2.0.7 fut la dernière version de l’implémentation en C++ et Qt. Le lien de son installeur Windows ne répond plus. La version 3 est une réécriture complète en Rust, avec un nouveau format de projet, et c’est là que tout se passe désormais. Vos projets 2.x [s’y ouvrent](@/coming-from-skribisto-2.md).

## Ce que « alpha » veut dire ici

Le format de projet est arrêté, il est documenté, et il met à niveau les anciens projets à l’ouverture. L’application autour n’a pas encore connu de version stable. Quand vous pourrez la faire tourner, gardez des sauvegardes de ce que vous ne pouvez pas vous permettre de perdre. Skribisto fait les siennes, et toute sauvegarde s’ouvre en lecture seule, mais un manuscrit mérite bretelles et ceinture.
