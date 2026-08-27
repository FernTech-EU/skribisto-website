+++
title = "Skribisto"
sort_by = "none"
template = "index.html"

[extra]
tagline = "un logiciel d’écriture pour les textes longs"
hero_title = "Écrivez le livre. La mise en forme viendra après."
hero_lede = "Skribisto organise un manuscrit selon ce que chaque élément est (livre, partie, chapitre, scène, note), et garde le texte et son synopsis côte à côte. Tout ce que vous écrivez reste dans un texte brut que vous pouvez ouvrir sans lui."
hero_shot_alt = "Le classeur à gauche, le texte d’une scène et son synopsis côte à côte dans l’éditeur."
export_shot_alt = "La fenêtre d’export, avec un aperçu en direct du manuscrit compilé."
cta_note = "Logiciel libre, GPLv3 · Linux, Windows et macOS · version en cours :"

cards_title = "Trois idées sur lesquelles tout repose"
cards_lede = "Ce sont elles qui distinguent Skribisto d’un dossier de documents, et de tous les plans qui rangent votre livre dans des boîtes."




cards = [
  { title = "La structure vient du sens", body = "L’arbre du classeur sert à ranger, et c’est tout ce qu’il fait. Ce qui fait d’une ligne un chapitre ou une scène, c’est le rôle que vous lui donnez, et vous pouvez donc déplacer, indenter, désindenter et regrouper sans réécrire la forme du livre." },
  { title = "Le texte et le synopsis, ensemble", body = "Chaque ligne d’écriture possède son texte et son résumé. C’est pour cela que l’éditeur a deux volets, et que l’on peut lire tous les synopsis d’un livre comme un seul document continu, quand on veut voir le plan plutôt que la prose." },
  { title = "Du texte brut qui vous appartient", body = "Un projet est un paquet .skrib : de la prose en Djot et des manifestes lisibles, sous la forme d’un fichier unique ou d’un dossier que vous pouvez versionner. Pas de base de données, pas de format opaque, rien qui exige Skribisto pour être lu." },
]

today_title = "Ce qu’il fait aujourd’hui"
today_lede = "Ceci n’est pas une feuille de route, mais l’application telle qu’elle est."
today_link = "Voir cela de plus près"
today = [
  "Un classeur entièrement modifiable : créer, renommer, dupliquer, déplacer, indenter, désindenter, convertir",
  "Un éditeur à deux volets, avec volets divisés et onglets",
  "Des flux de manuscrit : lire un chapitre, une partie ou un livre entier comme un seul document",
  "Tableau de liège, vue d’ensemble, sessions d’écriture et compteur de mots en direct",
  "Une planification du rythme avec jalons, jours chômés et objectifs de mots",
  "L’analyse de la forme d’un livre : mots par scène, part de dialogue, longueur des phrases et des paragraphes",
  "Des commentaires ancrés en marge avec fils de réponses, et des notes de bas de page",
  "Modèles de notes, étiquettes de couleur, point de vue et index des mentions",
  "Des images dans le texte, conservées dans chaque export, et une couverture",
  "Le remplacement à la frappe : votre propre lexique et une typographie adaptée à la langue",
  "Un mode sans distraction, avec ses propres thèmes",
  "Rechercher et remplacer dans tout le projet",
  "Corbeille et restauration, avec annulation",
  "Historique des versions et chronologie du projet, lus dans les sauvegardes déjà existantes",
  "Enregistrement automatique, sauvegardes avec rétention et planificateur, ouverture en lecture seule",
  "Import depuis Plume Creator, Markdown, texte brut, DOCX et ODT",
  "Export vers DOCX, ODT, EPUB, PDF, HTML, Markdown, Djot, LaTeX et texte brut",
  "Correction orthographique avec dictionnaires téléchargeables",
  "Thèmes clair et sombre, typographie par éditeur, taille de texte réglable",
  "Une interface en anglais et en français, et un arbre d’accessibilité pour les lecteurs d’écran",
]

promises_title = "Un logiciel libre, et qui le reste"
promises_lede = "Skribisto est sous licence GNU General Public License v3.0. Quatre choses à ce sujet ne bougeront pas."
promises_link = "Lire l’engagement en entier"
promises = [
  "Tout ce qu’il faut pour écrire un livre (créer, modifier, ouvrir, enregistrer et exporter un manuscrit, dans tous les formats pris en charge) est en GPLv3, définitivement.",
  "Votre projet reste lisible. Le format .skrib est ouvert et documenté, et rien ne peut rendre l’un de vos projets illisible par un logiciel libre.",
  "Rien n’est repris. Aucune fonction déjà livrée ne sera retirée du logiciel libre.",
  "Ni clé, ni serveur, ni permission. Skribisto n’exigera jamais une clé de licence, une activation ou une connexion réseau pour ouvrir ou modifier votre propre travail.",
]

coming_title = "Vous venez de Plume Creator ou de Skribisto 2 ?"
coming_body = "Un projet Skribisto 2 est mis à niveau au moment de son ouverture : ouvrez-le et continuez d’écrire. Un projet Plume Creator arrive par Projet ▸ Importer depuis ▸ Plume Creator. Aucun fichier d’origine n’est modifié, et l’interface a suffisamment changé pour mériter cinq minutes de lecture."
coming_link = "Ce qui change, et à quoi s’attendre"
+++

### Sous le capot

Skribisto 3 est écrit en Rust, de bout en bout. L’interface repose sur **Teksilo**, une bibliothèque graphique entièrement en Rust : il n’y a ni Qt, ni QML, ni C++, ni moteur de navigateur dans la compilation. C’est une application de bureau native, et elle démarre comme telle. Le cœur applicatif est engendré à partir d’un seul fichier de modèle par [Qleany](https://github.com/jacquetc/qleany), ce qui explique que toutes les opérations partagent une même pile d’annulation et un même bus d’événements.

L’application expose aussi un véritable arbre d’accessibilité, qu’un lecteur d’écran peut piloter ; NVDA et JAWS sont ceux utilisés pour les tests. Si vous rencontrez une lacune de ce côté, [dites-le](https://github.com/jacquetc/skribisto/issues) : c’est un bogue comme un autre.
