+++
title = "Obtenir Skribisto 3"
description = "Skribisto 3 est disponible. Il existe des versions pour Linux, pour Windows et pour macOS."
template = "download.html"
weight = 2

# One table per platform, in the order the page shows them. `key` matches the
# `platform` the sync script gives each file of a release, and a platform with no
# file in the release is left out. `notes` stays on the page under the files;
# `more` folds away under `more_label`.

[[extra.platforms]]
key = "linux"
name = "Linux"
notes = """
Sur Ubuntu, Debian, Linux Mint et les distributions qui en dérivent, prenez le paquet qui correspond à votre ordinateur (x86-64 pour la plupart, ARM64 pour une machine ARM) et ouvrez-le avec votre logithèque, ou lancez `sudo apt install ./` suivi du nom du fichier. Il demande Ubuntu 24.04 ou Debian 13, ou plus récent. Une version ultérieure s’installe de la même façon, et Skribisto vous prévient quand il y en a une.

Ailleurs, décompressez l’archive et lancez-la, ou prenez le Flatpak si c’est ce que votre distribution attend.
"""
more_label = "Vous trouvez Skribisto 1.9.41 dans votre logithèque ?"
more = """
Un avertissement. Si vous cherchez Skribisto dans votre logithèque, vous pourriez trouver la **1.9.41**, datant de 2022. C’est un autre programme, d’une autre époque, qui n’est plus développé, et ce n’est pas celui-ci.
"""

[[extra.platforms]]
key = "windows"
name = "Windows"
notes = """
Prenez l’installeur, sauf raison contraire.
"""

[[extra.platforms]]
key = "macos"
name = "macOS"
notes = """
Ouvrez l’image disque et glissez Skribisto dans votre dossier Applications. C’est une version universelle : elle fonctionne aussi bien sur les Mac Apple Silicon que sur les Mac Intel.
"""
more_label = "Si macOS refuse de l’ouvrir"
more = """
macOS protestera à la première ouverture, parce que le fichier ne porte pas encore la signature qu’Apple réclame. Autorisez-le depuis *Réglages Système ▸ Confidentialité et sécurité*, où il apparaît juste après le refus.
"""
+++

## Ce que vous obtenez

Tout est en place : l’écriture, les notes, la bible, les sauvegardes, les exports. C’est la version 3, elle est publiée, et elle est prête pour un vrai manuscrit.

Gardez vos sauvegardes habituelles, comme avec tout ce qui détient votre livre. Skribisto fait aussi les siennes, aussi souvent que vous le lui demandez, et vous pouvez en ouvrir une pour la lire sans déranger celle dans laquelle vous travaillez.

## Si quelque chose ne va pas

Dites-le-moi. Le plus utile est de préciser laquelle de ces versions vous utilisiez, sur quel type d’ordinateur, ce que vous faisiez, et ce que vous attendiez à la place. [Où le dire](@/help.md).

## Si vous veniez de Skribisto 2

La version 3 n’est pas une mise à jour : c’est un autre programme, avec un nouveau format de fichier. Vos anciens projets s’y ouvrent quand même, et sont repris au chargement, sans toucher à l’original. [Ce qui change par ailleurs](@/coming-from-skribisto-2.md).
