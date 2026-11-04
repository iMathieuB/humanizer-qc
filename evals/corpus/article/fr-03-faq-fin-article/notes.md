# Notes : article, fr, paire 3

Source : jeu d'exemples fictifs de la version 3.0, Article de blogue SEO, GEO et AEO, Paire 3 (FR) : FAQ et fin d'article. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Majuscules superflues dans les titres : « Questions Fréquentes » (https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative).
- Abus du gras : gras retiré des adjectifs « indispensable » et « fondamentale », gardé sur les chiffres (« 3 semaines », « 45 $ », « 3 000 courriels », « 0,015 $ »), élément protégé de type-article.md (https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://www.pangram.com/fr/signs-of-ai-writing).
- Tiret cadratin : dans la réponse sur la mise en place, remplacé par un deux-points (https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative).
- Typographie non conforme à l'OQLF : dollar à gauche, point décimal, espace avant « ? » et « ! » (https://vitrinelinguistique.oqlf.gouv.qc.ca/22039/la-typographie/espacement/espacement-avant-et-apres-les-signes-de-ponctuation-et-les-symboles; https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/).
- Recommandation finale de consulter un spécialiste introduite par « il est important de » (https://ar5iv.labs.arxiv.org/html/2306.05871).
- Section « Conclusion » et clôture « En conclusion » qui résume ce qui précède (https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://www.blogdumoderateur.com/detecter-texte-ia-chatgpt-outils-methodes/; https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr).
- Adjectifs gonflés : « indispensable », « fondamentale » (https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/; https://www.blogdumoderateur.com/tiret-cadratin-mort-vive-tiret-cadratin/).
- Clôture de service : « J'espère que cet article vous aidera » (https://ar5iv.labs.arxiv.org/html/2306.05871).

## Structures conservées

La FAQ visible, ses trois questions et leurs réponses directes. La fin d'article garde un intertitre, renommé « Délai, coût et accès », et son paragraphe reprend les seuls faits de la conclusion, sans « En conclusion » ni clôture de service.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 6, apres.md en compte 6.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang fr --type article --compare avant.md
```
