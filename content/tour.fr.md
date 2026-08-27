+++
title = "Visite de Skribisto"
description = "À quoi ressemble un livre dans Skribisto : comment il est structuré, comment on l’écrit, comment on le regarde, et comment il en sort."
weight = 1
+++

## 1. La structure

Un projet s’ouvre sur un **classeur** : un arbre de dossiers et d’éléments sur le côté. Cet arbre sert à ranger. Ce n’est pas le livre.

Ce qui fait qu’une ligne appartient au livre, c’est le **rôle** que vous lui donnez (livre, partie, chapitre, scène, note ou simple texte), et ces rôles se composent. Un chapitre peut être un dossier contenant des scènes, ou une simple ligne si c’est ainsi que vous pensez ; le même projet se lit dans les deux cas. Comme la structure est portée par les lignes et non par l’imbrication, vous pouvez regrouper, indenter, désindenter et réordonner sans que le manuscrit change de forme sous vos pieds.

<figure class="shot">
  <img src="/img/binder-and-editor.png" alt="Le classeur à gauche, le texte d’une scène et son synopsis côte à côte dans l’éditeur." width="1440" height="960" loading="lazy">
</figure>

Deux conséquences :

- **La conversion.** Une scène devient une note, un chapitre simple devient un dossier de chapitre, et le texte suit.
- **Les flux.** Un chapitre, une partie ou un livre entier se lisent comme un document continu, et tous ses synopsis aussi, ce qui reste le moyen le plus rapide de voir le plan sans la prose.

## 2. Écrire

Chaque ligne d’écriture possède deux textes : sa **prose** et son **synopsis**. L’éditeur montre les deux, côte à côte ou l’un au-dessus de l’autre, et chaque volet a sa propre typographie (police, corps, interligne, alinéa), parce qu’un synopsis ne se lit pas comme une scène.

Autour de cela :

- **Le mode sans distraction**, avec ses propres thèmes, pour quand le reste de l’interface est de trop.
- **Le remplacement à la frappe**, sur deux couches : votre lexique d’abréviations et de corrections, et une typographie adaptée à la langue : guillemets français, tirets, points de suspension, espaces fines insécables, tirets de dialogue. La touche Retour arrière annule un remplacement au lieu de vous résister.
- **La correction orthographique**, avec des dictionnaires téléchargés depuis l’application et une liste de mots par projet.
- **Les notes de bas de page**, numérotées d’après le manuscrit plutôt que stockées : en insérer une au chapitre deux ne laisse pas le chapitre neuf faux.
- **Des images** dans le texte, qu’il s’agisse d’une carte, d’un visage ou de la photo d’une rue, conservées dans le projet et dans chaque export, plus une couverture.
- **Des modèles de notes** : fiche de personnage, lieu, objet, séquencier, faction, note de documentation, ou les vôtres, enregistrés depuis n’importe quelle note.

## 3. Regarder

Un manuscrit s’écrit mieux quand on peut le regarder d’un peu plus loin.

- **Le tableau de liège.** Les scènes d’un chapitre ou d’une partie sous forme de cartes que l’on lit et réordonne.
- **La vue d’ensemble.** Un tableau du sous-arbre : titre, type, libellé, étiquettes, mots propres, mots au total, commentaires ouverts.
- **L’analyse.** La forme d’un livre mesurée à l’aune de ses propres chiffres, jamais d’une norme : mots par scène, part de dialogue, longueur des phrases et des paragraphes, densité de ponctuation.
- **Le rythme.** Un plan avec échéance, jalons et jours non travaillés, comparé aux mots réellement écrits.
- **Les commentaires.** Ancrés en marge, à la manière de LibreOffice, avec fils de réponses, un panneau pour tout le projet et un pour le document courant.
- **Étiquettes, point de vue et mentions.** Des étiquettes de couleur avec des jeux par genre, le personnage dont la scène épouse le regard, et un index de chaque endroit où un personnage ou un lieu étiqueté est nommé dans le texte.
- **Chronologie et historique des versions.** Ce qu’une scène disait mardi dernier, lu dans les sauvegardes que vous avez déjà, avec les différences.

## 4. Terminer

Skribisto n’est pas un traitement de texte et n’essaie pas de l’être. Il compile le manuscrit et le confie au logiciel dans lequel vous finissez.

<figure class="shot">
  <img src="/img/export-preview.png" alt="La fenêtre d’export, avec un aperçu en direct du manuscrit compilé." width="1440" height="960" loading="lazy">
</figure>

- **Neuf formats** : DOCX, ODT, EPUB, PDF, HTML, Markdown, Djot, LaTeX et texte brut, avec un aperçu en direct de ce qui va sortir et des styles enregistrés par format.
- **L’aller-retour éditorial se referme.** Envoyez un chapitre en DOCX ou en ODT, récupérez-le annoté : les commentaires reviennent sur les lignes auxquelles ils appartiennent, retrouvées d’après le texte réellement enregistré, et non d’après un numéro de ligne.
- **Des sauvegardes** avec politique de rétention, plusieurs destinations et un planificateur ; chaque sauvegarde s’ouvre en lecture seule, pour regarder sans risquer le projet vivant.
- **Votre projet, sans Skribisto.** Le paquet `.skrib` est une archive zip de prose Djot et de manifestes lisibles, ou un dossier déplié, ce qu’il vous faut si le manuscrit vit dans git. Un simple lecteur de Markdown pointé sur ce dossier vous montre votre livre, images comprises.

<div class="callout">
  <h3>Ce qu’il n’y a pas</h3>
  <p>Pas de synchronisation dans le nuage, pas d’édition collaborative, pas de compte, pas de système de greffons ; ce dernier existait dans Skribisto 2 et n’a pas été reconstruit. L’interface n’existe qu’en anglais et en français.</p>
</div>
