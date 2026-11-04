# Evals du humanizer

Ce dossier mesure si la version 3.0 retire les tics d'écriture IA sans toucher aux chiffres, aux structures protégées ni à la structure du texte (un écart de paragraphes n'est permis que pour un paragraphe fait de tics, déclaré dans Changements). Range les résultats hors du skill.

## Contenu

- `corpus/` : 25 paires avant et après, toutes fictives, rangées par type puis par langue (`corpus/<type>/<lang>-<nn>-<slug>/`), 3 en français et 2 en anglais par type. Chaque dossier contient `avant.md`, `apres.md` et `notes.md` (source, tics corrigés, structures conservées, paragraphes, commande attendue).
- Neuf cas au format skill-creator : `prompt.md` (réglages, puis la demande telle qu'un utilisateur l'écrirait), `case.yaml` (résultat attendu), `place-files.sh`, `files/avant.md` (copie du `avant.md` de la paire), `graders/NN-*.md` (un énoncé par fichier).

| Cas | Type | Langue | Mode | Paire du corpus | Déclencheur |
|---|---|---|---|---|---|
| `article-fr-faq-pipeline` | article | fr | pipeline | `article/fr-03-faq-fin-article` | ligne de paramètres |
| `article-en-quotes-pipeline` | article | en | pipeline | `article/en-04-quote-time` | ligne de paramètres |
| `page-web-fr-diagnostic-pipeline` | page_web | fr | pipeline | `page_web/fr-01-diagnostic-automatisation` | « passe humanizer » et ligne de paramètres |
| `page-web-en-triage-audit` | page_web | en | audit | `page_web/en-04-email-triage` | « est-ce que ça sonne IA? » |
| `publicite-fr-linkedin-interactif` | publicite | fr | interactif | `publicite/fr-01-diagnostic-courriels-linkedin` | « ça sonne IA » |
| `publicite-en-linkedin-interactif` | publicite | en | interactif | `publicite/en-04-automation-audit-linkedin` | « rends ça naturel » |
| `chronique-en-reorder-pipeline` | chronique | en | pipeline | `chronique/en-04-reorder-alerts` | ligne de paramètres |
| `formation-fr-mesure-interactif` | formation | fr | interactif | `formation/fr-01-mesurer-tache` | « enlève les tics d'IA » |
| `formation-en-approval-interactif` | formation | en | interactif | `formation/en-04-approval-workflow` | « relis pour le ton » |

Les cas de réécriture ont sept graders, dans cet ordre : zéro tiret, chiffres conservés, structures protégées, script à code 0, paragraphes conservés (ou écart déclaré), format du mode, tics retirés. Le cas d'audit en a cinq : aucune réécriture, tableau d'audit, tirets localisés, tics repérés, éléments protégés non comptés. Le skill écrit dans `sortie.md` et garde `avant.md` intact, pour que `--compare avant.md` fonctionne.

Plusieurs références humaines retirent un paragraphe vide (« Conclusion », slogan) : leur `notes.md` le signale. Un cas accepte un écart de paragraphes seulement pour un paragraphe fait uniquement de tics, déclaré dans Changements (règle dure 5); le script le signale en avertissement.

## Vérification déterministe

Depuis le dossier du skill :

```
python3 -I -m unittest discover -s scripts/tests -v
```

Les tests unitaires prouvent que chaque constat de `scripts/verif_humanizer.py` se déclenche quand il le doit, et seulement là. Les tests du corpus lancent le script sur chaque `apres.md` avec `--compare avant.md` et sur chaque `avant.md` : un `avant.md` doit produire au moins un constat, un `apres.md` doit sortir avec le code 0. Une paire dont `notes.md` signale un écart de paragraphes échoue à ce test tant qu'elle n'est pas corrigée ou exemptée. Aucun modèle n'est appelé.

## Lancer les cas avec skill-creator

1. Charge le skill skill-creator et demande-lui de faire tourner les cas de `evals/`.
2. Pour chaque cas, lance une exécution avec le skill et une sans, même prompt, `files/avant.md` placé dans le dossier d'exécution.
3. Note chaque grader à partir de la trace et des fichiers produits; le taux de réussite d'un cas est la part des graders réussis.
4. Pour comparer avec la version d'origine, refais la série avec humanizer 2.8.0 (https://github.com/blader/humanizer) installé comme skill de référence.

Avec Claude Code (v2.1.269 ou plus récent), la même série tourne en ligne de commande, depuis le dossier du skill :

```
claude plugin eval . --allow-tools Write,Edit,Bash --scaffold
```

`--scaffold` exécute `place-files.sh`; l'outil fait tourner chaque cas avec et sans le skill et écrit son rapport sous `evals/results/`. Ce sont de vraies exécutions du modèle, facturées : lance-les quand la version est prête, pas à chaque retouche.

## Optimiser la description

Le script `scripts/run_loop.py` de skill-creator teste le déclenchement de la description sur un jeu de requêtes et en propose de meilleures. Lance-le quand le skill est stable. Toute nouvelle description garde les six déclencheurs français (« humanise », « passe humanizer », « ça sonne IA », « rends ça naturel », « enlève les tics d'IA », « relis pour le ton »), les cinq types, les deux langues et la phrase qui dit que le skill n'est jamais un outil pour rendre un texte indétectable, et reste sous 1 000 caractères.

## Ajouter un cas

1. Choisis un nom en minuscules avec traits d'union, de la forme `<type>-<langue>-<sujet>-<mode>` (`page-web` pour le type `page_web`). N'emploie pas `files`, `results`, `mocks` ni `node_modules`.
2. Crée `prompt.md` avec le même bloc de réglages que les autres cas, la demande en français, puis une dernière ligne `Input files: avant.md`. Aucun texte libre dans le bloc de réglages.
3. Crée `case.yaml` (`schema_version: "1.1"` entre guillemets, `name` identique au dossier, `expected_outcome` sous un `|`, `context.scaffold_script: place-files.sh`) et copie `place-files.sh` d'un autre cas, exécutable.
4. Mets le texte à réviser dans `files/avant.md`.
5. Écris un grader par fichier dans `graders/`, numérotés, avec le bloc `type: llm`, `focus: trace`, `weight: 1` en tête. Chaque énoncé nomme des valeurs précises; compte les paragraphes avec `count_paragraphs` du script. Sans énoncé prêt, écris `graders/01-expected-output.md` avec le corps « The result matches this description: » suivi du résultat attendu : un cas sans grader ne se charge pas.

Pour ajouter une paire au corpus : crée `corpus/<type>/<lang>-<nn>-<slug>/` avec `avant.md`, `apres.md` (un paragraphe par ligne, mêmes chiffres, même nombre de paragraphes que `avant.md`, aucun tiret) et `notes.md` sur le modèle des autres. Retire tout nom de client, tout secteur et tout montant réel lié à un client. Une paire de référence qui s'écarte du compte de paragraphes le déclare par la ligne « Exemption : paragraph_count. » dans la section Paragraphes de `notes.md` (les tests ignorent alors cette seule comparaison) et ne sert pas de modèle de la règle dure 5. Lance ensuite les tests du corpus.

## Mise en garde

Le dossier `corpus/` n'est pas un cas. Si l'outil d'evals refuse de charger `evals/` à cause de lui, déplace `corpus/` hors de `evals/` le temps de l'exécution, remets-le ensuite, et note-le dans ton rapport d'évaluation.
