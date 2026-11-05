# Journal des modifications : humanizer-qc

Le champ `metadata.version` du frontmatter de SKILL.md, le `__version__` de `scripts/verif_humanizer.py` et la première entrée ci-dessous doivent toujours concorder.

## 3.0.1 (2026-11-05), première version publique

Version dérivée de humanizer 2.8.0 de Siqi Chen (https://github.com/blader/humanizer, licence MIT), refaite pour le français du Québec et l'anglais. Cette édition suit sa propre numérotation : elle ne correspond pas aux versions 3.x publiées depuis dans le dépôt d'origine. Elle est publiée sous le nom humanizer-qc, pour ne pas se confondre avec le skill d'origine une fois installée.

### Repris de la 2.8.0
- Les 33 patrons d'origine (P01 à P33), déplacés dans `references/patterns-en.md`, sourcés et non réécrits. Seuls changements : numérotation `Pnn`, tirets retirés hors des blocs « Before », lignes « False positive » et « Sources » ajoutées.
- « What NOT to flag », « Signs of human writing », « Personality and soul », la calibration de voix et l'exemple complet, conservés dans `patterns-en.md`; les faux positifs et les signes humains sont adaptés en français dans `patterns-fr.md`.
- La règle sur les tirets et le balayage final, devenus la règle dure 1 et l'Étape 5.
- La boucle brouillon, « encore IA », version finale, devenue le mode interactif.

### Ajouté
- Le français du Québec : `references/patterns-fr.md`, patrons communs et propres au français, typographie OQLF, faux positifs en français.
- P34 à P74 : 41 patrons tirés d'une recherche compilée en 2026 (Wikipédia en anglais et en français, études mesurées, guides éditoriaux, billets de praticiens), chacun avec son niveau de preuve (`mesure`, `guide`, `blogue`, `maison`) et ses sources.
- Cinq types de contenu plus `general`, un fichier chacun : `type-article.md`, `type-page-web.md`, `type-publicite.md`, `type-chronique.md`, `type-formation.md` (éléments protégés, structures légitimes, tics du type, registre, patrons prioritaires, seuils du script, liste de contrôle, exemple).
- Trois modes : `interactif`, `pipeline` (sortie lisible par un script, ligne STATUT) et `audit` (tableau sans réécriture).
- `references/detecteurs.md` : position face aux détecteurs, faux positifs documentés, ce que les lecteurs humains perçoivent, artefacts de surcorrection interdits.
- `references/appels-et-coexistence.md` : paramètres d'appel, `passages=`, fichiers bilingues, coexistence avec une passe de révision de fond.
- Onze règles dures de réécriture, dont « rien d'ajouté, rien de retiré » (règle 2), « même structure » (règle 5), « aucun retour forcé » (règle 6) et le souffle (règle 10).
- `scripts/verif_humanizer.py` : vérification déterministe (tirets, liste de formules, triades, staccato, uniformité des phrases, gras, émojis, guillemets, casse des titres, parallélisme négatif, atténuateurs empilés, retours forcés, typographie française, comparaison des chiffres, liens, codes temporels et paragraphes avec l'original), codes de sortie 0, 1 et 2, sortie texte ou JSON.
- `scripts/kill_list.json` : 564 entrées, 175 en français et 389 en anglais, en six catégories (vocabulaire, formules, ouvertures, clôtures, ponctuation, structure).
- `scripts/tests/test_verif.py` : tests unitaires du script, tests du corpus et contrôle des tirets dans tout le dossier.
- `evals/` : 25 paires avant et après fictives dans `corpus/` et neuf cas au format skill-creator.
- Profil de voix facultatif : un fichier `references/voix-auteur.md`, écrit par l'utilisateur, est lu s'il existe.
