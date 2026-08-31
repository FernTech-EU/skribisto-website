+++
title = "Un logiciel libre, et qui le reste"
description = "Skribisto est en GPLv3. Voici exactement ce que cela vous garantit, et ce que cela ne garantit pas."
weight = 4
+++

Skribisto est un logiciel libre sous [licence GNU General Public License v3.0](https://github.com/jacquetc/skribisto/blob/dev/LICENSE). Vous pouvez l’utiliser pour n’importe quoi, en lire tout le code, le modifier et le transmettre.

Voilà pour la licence. Ce qui suit est l’engagement, ce qui n’est pas la même chose, et c’est celui-ci qui compte vraiment au moment de décider si vous allez confier trois ans de travail à une application.

## Quatre choses qui ne bougeront pas

<ul class="promises">
  <li><strong>Tout ce qu’il faut pour écrire un livre est en GPLv3, définitivement.</strong> Créer, modifier, ouvrir, enregistrer et exporter un manuscrit, dans tous les formats pris en charge : c’est du logiciel libre et cela le reste.</li>
  <li><strong>Votre projet reste lisible.</strong> Le format <code>.skrib</code> est ouvert et documenté, et un projet reste lisible, modifiable et exportable par un logiciel libre, quoi qu’il lui arrive par ailleurs.</li>
  <li><strong>Rien n’est repris.</strong> Aucune fonction déjà livrée ne sera retirée pour être placée derrière un paiement.</li>
  <li><strong>Ni clé, ni serveur, ni permission.</strong> Skribisto n’exigera jamais une clé de licence, une activation ou une connexion réseau pour ouvrir ou modifier votre propre travail.</li>
</ul>

## Ce qu’est réellement votre projet

Vous écrivez dans un éditeur de texte enrichi, et c’est enregistré en texte. Un projet `.skrib` est une archive zip, ou si vous préférez un dossier déplié, qui contient :

- votre prose en fichiers [Djot](https://djot.net), un par scène, en texte UTF-8. Djot est assez proche de Markdown pour qu’une scène se lise d’un coup d’œil ;
- à côté d’eux, un index lisible de la structure, en texte lui aussi ;
- vos images sous `assets/`, nommées d’après l’empreinte de leurs propres octets.

Ouvrez-le avec un éditeur de texte. Pointez `git` sur sa forme dépliée et obtenez de vraies différences sur votre roman. Rien là-dedans n’a besoin de Skribisto pour être compris, et c’est tout l’enjeu : un logiciel ne devrait pas pouvoir retenir votre livre en otage, celui-ci compris.

## Pas de compte, pas de télémétrie

Skribisto n’a pas de système de comptes, n’envoie aucune donnée d’usage et n’a besoin d’aucune connexion réseau pour travailler. Il ne contacte le réseau que pour une seule chose, et seulement si vous le demandez : télécharger un dictionnaire orthographique.

## Contribuer, et le CLA

Les contributions sont bienvenues et acceptées sous un [accord de licence de contributeur](https://github.com/jacquetc/skribisto/blob/dev/CLA.md) plutôt qu’un simple « signed-off-by ». Vous gardez le droit d’auteur sur votre travail, et en retour votre contribution restera disponible sous GPL. [Comment contribuer](@/get-involved.md).

## Marque

Skribisto™ est une marque de FernTech, et la GPL n’accorde aucun droit sur les marques. Dupliquez le code librement, c’est à cela que sert la licence, mais une version dérivée distribuée à d’autres doit porter son propre nom et sa propre identité, comme Iceweasel l’a fait vis-à-vis de Firefox. Dire « bâti sur Skribisto », ou écrire à son sujet, ne demande aucune autorisation. Pour le reste : <trademarks@ferntech.eu>.
