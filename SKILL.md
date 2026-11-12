---
name: humanizer-qc
metadata:
  version: "3.1.0"
description: >-
  Passe d'édition qui retire les tics d'écriture IA d'un texte et le ramène vers la voix de son auteur, en français du Québec et en anglais. Utilise ce skill dès qu'on dit « humanise », « passe humanizer », « ça sonne IA », « rends ça naturel », « enlève les tics d'IA », « relis pour le ton », « humanize this » ou « sounds like AI », et sans ces mots chaque fois qu'un texte rédigé ou réécrit par l'assistant va être publié ou envoyé : article de blogue SEO/GEO/AEO, page web de service, publicité LinkedIn ou Meta, script vidéo parlé, matériel de formation. Trois modes : interactif, pipeline (appel par un autre skill ou un script), audit (évaluer sans réécrire). Protège chiffres, sources, liens, FAQ, CTA et minutage; vérifie le résultat avec un script. Passe en dernier, après toute révision de fond. Jamais un outil pour rendre un texte indétectable.
license: MIT
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
---

# Humanizer : retirer les tics d'IA, garder la voix de l'auteur

Dernier relecteur avant publication : retire les tics d'écriture IA documentés et ramène le texte vers la voix de son auteur, sans toucher au fond. Dans le doute, garde la phrase de l'auteur.

## Étape 0 : langue, type, mode, auteur

- **Langue** : celle du texte; `lang=` gagne. Fichier FR et EN : par partie.
- **Type** : `type=` gagne; sinon le contexte (appelant, chemin), puis les indices en tête des `type-*.md`. Courriel, offre, lettre, préparation de rencontre : `general`, sans fichier de type.
- **Mode** : `mode=` gagne; appel par un skill ou script : `pipeline`; évaluer sans corriger, ou texte d'un tiers (client, participant) : `audit`; sinon `interactif`.
- **Une question au plus** : en interactif, type ambigu : une AskUserQuestion (cinq types, autres manques). Pipeline : aucune, `general`, « type non fourni » dans Changements. Audit : hypothèse en tête.
- **Auteur** : calibre-toi sur l'échantillon fourni (« Voice calibration », « Voix et souffle »); sans échantillon, voix claire au registre du type. Profil de voix facultatif `references/voix-auteur.md` (registre, rythme, rejets) : lis-le s'il existe. Texte d'un tiers (`auteur=tiers`) : audit, sans profil.
- **Texte de l'auteur** (dictée, script final, « c'est mon texte », `auteur=texte-auteur`) : `audit` par défaut; correction demandée : règles 1, 7 et 8 seulement, le reste en « encore IA ».

## Étape 1 : charger seulement ce qu'il faut

| Situation | Fichier à lire |
|---|---|
| Texte en français | `references/patterns-fr.md` |
| Texte en anglais | `references/patterns-en.md` |
| Type connu | `references/type-<clé>.md` (un seul) |
| Profil de voix présent | `references/voix-auteur.md` |
| Mode audit, ou question sur les détecteurs | `references/detecteurs.md` |
| Mode pipeline, `passages=`, fichier bilingue, autre passe de révision | `references/appels-et-coexistence.md` |

D'un fichier de langue, lis l'index puis seulement les sections `^### Pnn` des patrons signalés, prioritaires du type ou soupçonnés. Plafond : 30 Ko par appel, hors SKILL.md, `detecteurs.md`, `appels-et-coexistence.md`.

## Étape 2 : éléments protégés

Liste complète au fichier de type. Partout : (1) chiffres, dates, unités; (2) sources, citations, liens; (3) noms propres, outils, termes techniques; (4) code, front matter, HTML, tableaux; (5) dictées et textes de l'auteur, témoignages, CTA, mentions légales, au caractère près. Protégé avec un tic : tel quel, « Conflit » dans Changements. Seule retouche, sauf exceptions nommées au fichier de type : un tiret dans `title`, `meta_description` ou une ligne ▶ devient virgule, deux-points ou point.

## Étape 3 : repérer par grappes

Un signe isolé ne prouve rien : agis sur deux signes croisés par paragraphe, un patron récurrent, ou une règle dure enfreinte. Les formulations rejetées du profil de voix comptent même isolées sur un brouillon de l'assistant. Relis d'abord « Ce qu'il ne faut pas signaler » (langue) et « Structures légitimes à ne pas signaler » (type).

## Étape 4 : règles dures de réécriture

1. Zéro tiret cadratin ou demi-cadratin hors exceptions déclarées (`footer-dash`, `timecode-dash`, `quote`) : point, virgule, deux-points, parenthèses, « à » dans une plage.
2. Rien d'ajouté, rien de retiré : aucun exemple, chiffre, nom, source, anecdote ou « je » en plus; aucun fait, attribut du produit (la mention de l'IA comprise), libellé d'étape, nuance ou réserve en moins. Retire l'emballage (adverbe, formule, slogan), garde la charge utile.
3. Aucune faute exprès, familiarité plaquée ou caractère Unicode inhabituel.
4. Aucun synonyme rare pour « faire humain » : le mot courant. Aucun point d'exclamation hors de la chute d'un script parlé.
5. Même structure avant et après : titres, puces, rangées, FAQ, minutage, nombre de paragraphes de prose. Seule exception : un paragraphe fait uniquement de tics (slogan en fragments, transition creuse, consigne au modèle) se retire ou se fond dans son voisin, sans remplissage, et Changements le dit (« §n retiré : slogan sans fait »).
6. Ne coupe jamais la prose : un paragraphe ou une puce par ligne, aucun retour forcé à une colonne fixe. Exceptions : code, tableaux, YAML, JSON.
7. Chiffres et sources intacts; en français, seule la typographie OQLF change (`1 300 $`, `32,50`).
8. Typographie OQLF en français (« », « courriel »); en anglais, guillemets droits, intertitres en casse de phrase.
9. Registre du fichier de type (section 4) ou du profil de voix.
10. Souffle : une phrase retirée ne laisse pas de trou, rattache la précédente et la suivante. Garde la variation de longueur de l'auteur : hors script parlé, pas de suite de phrases courtes juxtaposées. Un tic rogné reste un tic (« un enjeu crucial » moins « crucial ») : remplace la phrase par le premier fait du texte, ou retire-la. Une phrase creuse dans un emplacement protégé (ouverture, « À retenir », chute) se réécrit avec ce que le texte dit déjà, jamais inventée.
11. Un remplacement de registre garde le sens; si aucune formulation ne le garde, garde la phrase et signale-la.
12. Phrase par phrase (P81 à P83) : aucune phrase de plus de 30 mots, aucune virgule sans fonction, un verbe conjugué par phrase hors script parlé; la passe n'en crée pas.

## Étape 5 : vérification par le script

`python3 -I <dossier du skill>/scripts/verif_humanizer.py <fichier> --lang <fr|en> --type <clé> --compare <original>`, plus `--skip-quotes` si `exceptions=quote`, `--allow-footer-dash` si `exceptions=footer-dash` hors `article`. Texte hors fichier : écris-le, avec l'original, en dossier temporaire.

Corrige chaque `error`, relance, trois tours au plus. Erreur sur un protégé ou hors `passages=` : « Conflit : ... » dans Changements, puis relance avec `--ignore-line <ligne>`. Tout `warning` : corrigé ou justifié (écart de paragraphes : règle 5). Code 2 : corrige l'appel une fois; s'il revient ou sans Python, balaie à la main tirets et retours forcés, écris « script non exécuté ». Cas particuliers : `appels-et-coexistence.md` section 4.

## Étape 6 : sortie selon le mode

### Mode interactif

````
**Langue :** <fr|en> · **Type :** <clé> · **Mode :** interactif

### humanizer : Brouillon
<<<HUMANIZER_BROUILLON
<texte réécrit>
HUMANIZER_BROUILLON>>>

### humanizer : Ce qui sonne encore IA
- <puce brève>

### humanizer : Version finale
<<<HUMANIZER_VERSION_FINALE
<texte final>
HUMANIZER_VERSION_FINALE>>>

### humanizer : Changements
- §<n> <Pnn> : « <extrait avant> » devient « <extrait après> »
- Conflit : <règle> contre <élément protégé ou décision de l'auteur>, élément gardé (L<ligne>)
- Exception : <exception déclarée gardée>
- Registre : « <formulation rejetée> » remplacée par « <remplacement> »
- Vérification : verif_humanizer.py, code <0|1|2> (<n> avertissements gardés : <raison>)
````

Trois à six puces « encore IA ». Plus de 800 mots : « Brouillon omis : texte de plus de 800 mots. » remplace le Brouillon. Au plus 12 puces de changements, regroupées; Registre seulement si l'auteur rejette une formulation.

### Mode pipeline

Gabarit, règles et valeurs de STATUT : `appels-et-coexistence.md` sections 2 et 3, à lire avant de répondre. Première ligne `STATUT: <pass|exception|fail|non-verifie>`, puis `### humanizer : Version finale` (bloc délimité, ou « Écrite dans <sortie>. »), `### humanizer : Changements` et `### humanizer : Vérification` (sortie du script en clôture `text`). Rien avant STATUT ni après Vérification.

### Mode audit

Gabarit : `detecteurs.md` section 7. Ni réécriture, ni remplacement, ni fichier modifié; « Aucun tic repéré. » s'il n'y a rien.

## Avec une passe de révision

- Une révision de fond (structure, ton, vente) vient avant; humanizer passe en dernier. Tout changement de texte après la passe relance humanizer sur les passages touchés (`passages=`), puis verif_humanizer.py.
- Ne réintroduis aucune formulation rejetée par l'auteur ou par cette passe.
- Toute phrase ajoutée, même à la demande de l'auteur, passe par humanizer avant de lui être montrée. Le reste : `appels-et-coexistence.md` section 5.

## Ce que le skill ne fait jamais

- Viser un score de détecteur, promettre un texte « indétectable » ou effacer les traces d'usage de l'IA : la transparence relève de l'auteur.
- Ajouter ou modifier un fait, un chiffre, une source, une citation, une clause, un nom.
- Retirer une structure exigée par le type (FAQ, tableau, objectifs, minutage, CTA).
- Publier, envoyer, supprimer, ou écrire hors du fichier fourni (ou `sortie=`) et d'un dossier temporaire.

## Origine

P01 à P33 et la calibration de voix : humanizer 2.8.0 de Siqi Chen, licence MIT (https://github.com/blader/humanizer).
