+++
title = "Skribisto"
sort_by = "none"
template = "index.html"

[extra]
tagline = "un logiciel d’écriture pour les textes longs"
hero_title = "Écrivez le livre. La mise en forme viendra après."
hero_lede = "Un projet contient tout : votre livre, ou plusieurs, les chapitres et les scènes en dessous, et les notes et la documentation à côté. Chaque texte porte son propre résumé, et tout est enregistré dans des fichiers texte que vous pouvez ouvrir avec n’importe quoi."
hero_shot_alt = "Le classeur à gauche, le texte d’une scène et son synopsis côte à côte dans l’éditeur."
export_shot_alt = "La fenêtre d’export, avec un aperçu en direct du manuscrit compilé."
cta_note = "Logiciel libre, GPLv3 · Linux, Windows et macOS · version en cours :"

cards_title = "Trois choses à savoir avant de commencer"
cards_lede = "Ce sont elles qui distinguent Skribisto d’un dossier de documents, et d’un logiciel de plan qui range votre livre dans les cases de quelqu’un d’autre."




cards = [
  { title = "Il s’adapte à votre façon d’écrire", body = "Un projet peut contenir plusieurs livres, et un livre autant de chapitres que vous voulez, avec des scènes en dessous ou sans. Un chapitre peut être un dossier plein de scènes, ou une simple page que vous écrivez d’un trait, et les deux peuvent coexister dans le même livre. Vous pouvez aussi tenir plusieurs classeurs, pour que le manuscrit, la bible et la documentation ne partagent pas le même arbre." },
  { title = "Un résumé à côté de chaque scène", body = "Chaque texte porte un court récit de ce qui s’y passe, dans un encadré au-dessus de la page ou dans une colonne à côté. Ce sont ces résumés que le tableau de liège affiche sur ses cartes, et vous pouvez les lire tous, un livre entier à la fois, quand vous voulez le plan plutôt que la prose." },
  { title = "Des fichiers encore lisibles dans dix ans", body = "Vous écrivez dans un véritable éditeur de texte enrichi : gras, italique, titres, images. C’est enregistré en Djot, un format texte très proche de Markdown, un fichier par scène, dans un paquet que vous gardez en un seul fichier ou en dossier versionnable. Pas de base de données, et rien qui exige Skribisto pour être lu." },
]

today_title = "Ce qu’il fait aujourd’hui"
today_lede = "Ceci n’est pas une feuille de route, mais l’application telle qu’elle est."
today_link = "Voir cela de plus près"
today = [
  "Des **classeurs** que l’on réorganise sans casser le livre.",
  "Un **résumé** à côté de chaque texte.",
  "Des **vues divisées** et des onglets, avec une typographie par éditeur.",
  "Des **flux** : un chapitre, une partie ou un livre entier d’une traite.",
  "Un **tableau de liège** dont on lit, modifie et réordonne les cartes.",
  "Une **vue d’ensemble** de tout ce qui se trouve sous un dossier.",
  "L’**analyse** de la forme d’un livre, selon ses propres chiffres.",
  "Une planification du **rythme**, avec jalons et jours chômés.",
  "Un **compteur de mots** en direct, et des sessions d’écriture.",
  "Des **commentaires** en marge, avec fils de réponses.",
  "Des **notes de bas de page**, numérotées d’après le manuscrit.",
  "Des **modèles de notes** pour personnages, lieux et documentation.",
  "Des **étiquettes**, le point de vue, et un index des mentions.",
  "Des **images** dans le texte, et une couverture.",
  "Le **remplacement à la frappe**, selon la langue que vous écrivez.",
  "Un mode **sans distraction**, avec ses propres thèmes.",
  "**Rechercher et remplacer** dans tout le projet.",
  "Une **corbeille** et la restauration, avec annulation.",
  "Un **historique des versions**, et une chronologie du projet.",
  "Des **sauvegardes** planifiées, qui s’ouvrent en lecture seule.",
  "L’**import** depuis Plume Creator, Markdown, DOCX et ODT.",
  "L’**export** vers neuf formats, avec aperçu en direct.",
  "La **correction orthographique**, avec dictionnaires téléchargeables.",
  "Des thèmes **clair et sombre**, et une taille de texte réglable.",
  "L’**anglais et le français**, et un arbre d’accessibilité.",
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

coming_title = "Vous venez de Plume Creator ou de Skribisto 2 ?"
coming_body = "Un projet Skribisto 2 est mis à niveau au moment de son ouverture : ouvrez-le et continuez d’écrire. Un projet Plume Creator arrive par Projet ▸ Importer depuis ▸ Plume Creator. Aucun fichier d’origine n’est modifié, et l’interface a suffisamment changé pour mériter cinq minutes de lecture."
coming_link = "Ce qui change, et à quoi s’attendre"
+++

### Sous le capot

Skribisto 3 est écrit en Rust, de bout en bout. L’interface repose sur **Teksilo**, une bibliothèque graphique entièrement en Rust : il n’y a ni Qt, ni QML, ni C++, ni moteur de navigateur dans la compilation. C’est une application de bureau native, et elle démarre comme telle. Le cœur applicatif est engendré à partir d’un seul fichier de modèle par [Qleany](https://github.com/jacquetc/qleany), ce qui explique que toutes les opérations partagent une même pile d’annulation et un même bus d’événements.

L’application expose aussi un véritable arbre d’accessibilité, qu’un lecteur d’écran peut piloter ; NVDA et JAWS sont ceux utilisés pour les tests. Si vous rencontrez une lacune de ce côté, [dites-le](https://github.com/jacquetc/skribisto/issues) : c’est un bogue comme un autre.
