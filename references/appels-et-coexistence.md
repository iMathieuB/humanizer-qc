# Appels, sortie lisible par un script et coexistence

Lis ce fichier avant toute réponse en mode pipeline, et chaque fois que `passages=`, un fichier bilingue ou une autre passe de révision entre en jeu.

## 1. Paramètres d'appel

Un skill ou un script de publication appelle humanizer avec une ligne de paramètres, dans cet ordre, chaque paramètre facultatif :

```
humanizer mode=pipeline type=article lang=fr fichier=<chemin> sortie=<chemin> original=<chemin> passages=<plages> auteur=texte-auteur exceptions=quote
```

- `fichier` : le fichier à réviser, un seul par appel. Pour une paire FR et EN (article ou page publiés dans les deux langues), l'appelant fait un appel par fichier, et chaque appel rend sa propre sortie complète (STATUT, Version finale, Changements, Vérification).
- `sortie` : le fichier où écrire la version finale; par défaut, `fichier` lui-même (révision en place). Les cas d'evals passent `sortie=sortie.md` pour garder `avant.md` intact.
- `original` : une copie de l'état avant la passe, pour `--compare`. Si elle est absente et que `sortie` est `fichier`, crée-la dans un dossier temporaire, jamais à côté du fichier publié. Si `sortie` diffère de `fichier`, `fichier` sert d'original.
- `passages` : limite la passe à une partie du texte, en plages de lignes de `fichier` (`passages=40-58,112-120`) ou en intertitres exacts entre guillemets (`passages="Ce qui change"`, la section jusqu'au titre suivant de même niveau). Sert quand seule la prose ajoutée ou retouchée doit repasser (révision d'une page déjà publiée, passages touchés après une autre passe). Hors des passages, le texte reste au caractère près. Le script tourne quand même sur le fichier entier avec `--compare` : la règle des paragraphes et la comparaison des nombres portent sur le fichier entier, ce qui revient à exiger le même nombre de paragraphes dans chaque passage puisque le reste est inchangé. Une erreur située hors des passages ne se corrige pas : note « Hors passages : L<ligne> <constat> » dans Changements et passe la ligne en `--ignore-line`. Un appelant peut aussi fournir un fichier extrait qui ne contient que les passages; alors `--compare` et la règle des paragraphes portent sur l'extrait, et l'appelant remet l'extrait en place.
- `auteur` : absent par défaut (voix calibrée sur l'échantillon fourni et sur `voix-auteur.md` s'il existe); `tiers` déclare le texte d'un client, d'un participant ou d'un autre auteur : mode `audit` par défaut, sans profil de voix; `texte-auteur` déclare un texte écrit, dicté ou approuvé par l'auteur : mode `audit` par défaut et, si une correction est demandée, seules les règles dures 1, 7 et 8 s'appliquent (SKILL.md, Étape 0).
- `exceptions` : liste séparée par des virgules (`footer-dash,quote`); `footer-dash` est implicite avec `type=article`, `timecode-dash` avec `type=chronique`.

Fichier qui mélange les deux langues (traité par partie) : le script n'accepte qu'un `--lang`. Extrais chaque partie, et la partie correspondante de l'original, dans un dossier temporaire, lance le script sur chacune avec sa langue, puis remets les parties en place dans l'ordre d'origine. La section Vérification donne une sortie par partie, chacune précédée de sa langue.

## 2. Format lisible par un script

Ces règles valent pour les modes interactif et pipeline, pour qu'un script puisse découper la réponse même quand le texte contient des intertitres `###` (H3, questions de FAQ).

- Chaque titre de section commence par `### humanizer : `.
- Le texte du Brouillon et de la Version finale se place entre deux lignes délimitrices uniques, seules sur leur ligne : `<<<HUMANIZER_BROUILLON` et `HUMANIZER_BROUILLON>>>`, `<<<HUMANIZER_VERSION_FINALE` et `HUMANIZER_VERSION_FINALE>>>`.
- La sortie du script se place dans une clôture `text`.
- Les puces de Changements ont une seule forme dans les deux modes : `§<n> <Pnn> : « <extrait avant> » devient « <extrait après> »`. Regroupe les changements semblables en une puce : au plus 12 puces de changements, plus les puces Conflit, Hors passages, Exception, Registre et Vérification.

Gabarit du mode pipeline, à reproduire tel quel :

````
STATUT: <pass|exception|fail|non-verifie>

### humanizer : Version finale
<<<HUMANIZER_VERSION_FINALE
<texte final>
HUMANIZER_VERSION_FINALE>>>

### humanizer : Changements
- §<n> <Pnn> : « <extrait avant> » devient « <extrait après> »
- §<n> retiré : <paragraphe fait uniquement de tics, retiré ou fondu dans le voisin>
- Conflit : <règle> contre <élément protégé ou décision de l'auteur>, élément gardé (L<ligne>)
- Hors passages : L<ligne> <constat>
- Exception : <exception déclarée gardée>
- Registre : « <formulation rejetée> » remplacée par « <remplacement> »

### humanizer : Vérification
```text
<dernière sortie texte de verif_humanizer.py, telle quelle, ou « script non exécuté : <raison> »>
```
````

## 3. STATUT du mode pipeline

Écris la ligne STATUT en première ligne de la réponse, exactement sous la forme `STATUT: <valeur>`, avec l'une de ces quatre valeurs :

- `pass` : la dernière exécution du script rend le code 0 sans `--ignore-line`.
- `exception` : le code 0 n'est obtenu qu'avec `--ignore-line`, et chaque ligne ignorée porte seulement des conflits documentés avec des éléments protégés (ou des lignes hors `passages=`), chacun listé dans Changements.
- `fail` : le code 1 reste après trois tours, avec au moins une erreur sans justification. N'écris pas le fichier : l'original reste en place, et la version finale figure entre ses délimiteurs pour examen.
- `non-verifie` : le script rend 2 après une correction de l'appel, ou Python manque. Fais le balayage manuel de l'Étape 5, écris le fichier, et dis dans la section Vérification pourquoi le script n'a pas tourné.

Règles du mode pipeline :

- Rien avant la ligne STATUT ni après la section Vérification : aucun préambule, aucun commentaire, aucune question.
- Si `fichier=` est fourni et que le STATUT n'est pas `fail`, écris la version finale dans `sortie` (par défaut `fichier`) et remplace le bloc délimité par la seule ligne `Écrite dans <sortie>.`.
- Un appel traite un seul fichier (section 1).
- Aucune question à l'appelant : un type manquant donne `general` et « type non fourni » dans Changements.
- L'appelant lit la ligne STATUT et n'injecte rien sur `fail`.

## 4. Vérification : cas particuliers

- **Code 2 et STATUT `non-verifie`** : le code 2 signale un appel invalide (option, langue, type ou fichier). Corrige l'appel une fois et relance. S'il rend encore 2, ou si Python n'est pas disponible, balaie à la main les deux tirets (cadratin et demi-cadratin) et les retours forcés, écris « script non exécuté : <raison> » dans la section Vérification, et rends `STATUT: non-verifie`.
- **Erreurs hors `passages=`** : ne les corrige pas. Note « Hors passages : L<ligne> <constat> » dans Changements et relance avec `--ignore-line <ligne>` (répétable). Le STATUT devient `exception` si le code 0 n'est obtenu qu'ainsi.
- **Fichier extrait** : quand l'appelant fournit un extrait qui ne contient que les passages, lance `--compare` sur l'extrait et sur la partie correspondante de l'original; la règle des paragraphes porte sur l'extrait. Ne remets pas l'extrait en place : l'appelant s'en charge.
- **Fichier bilingue** : un lancement par partie, chacun avec son `--lang` et sa partie d'original (section 1); une sortie par partie dans Vérification.

## 5. Avec une passe de révision de fond

Une passe de révision de fond (structure, ton, clarté, force de vente), faite par un autre skill ou par l'auteur, coexiste avec humanizer selon ces règles.

- Elle vient avant; humanizer passe en dernier. Tout changement de texte après la passe, quelle qu'en soit l'origine, relance humanizer sur les passages touchés (`passages=`), puis verif_humanizer.py.
- Si l'auteur ou cette passe tient un registre de formulations rejetées, n'en réintroduis aucune, et entre deux reformulations choisis celle qui n'en touche aucune famille. Si ce registre vient avec un script de contrôle, lance-le aussi sur la version finale.
- Toute phrase ajoutée plus tard, même à la demande de l'auteur, passe par humanizer avant de lui être montrée.
- Ne défais jamais une décision prise pendant cette passe : régime des titres, répétitions défendues, première phrase-réponse des H2, CTA repris d'un texte précédent.
- Une dictée de l'auteur et les textes qu'il fournit restent à la lettre; la passe porte sur ce que l'assistant a composé ou réécrit.
- En conflit avec le registre, une dictée ou un élément protégé, ceux-ci gagnent et le conflit va dans Changements.
- Une formulation que l'auteur rejette pendant la passe se signale dans la puce « Registre » de Changements, pour qu'il l'ajoute à son registre ou à `voix-auteur.md`.
