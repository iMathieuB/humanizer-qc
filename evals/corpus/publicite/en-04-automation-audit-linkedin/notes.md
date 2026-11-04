# Notes : publicite, en, paire 4

Source : jeu d'exemples fictifs de la version 3.0, Publicité LinkedIn ou Meta, Paire 4 (EN) : Automation audit for manufacturers, LinkedIn single image. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Opening "In today's fast-paced world", removed; the ad opens on the 10 hours, inside the first 150 characters: https://cbriansmith.substack.com/p/leash-the-robot-and-keep-your-emails
- Empty promotional formula "unlock your team's full potential", removed: https://www.eesel.ai/blog/ai-ad-copy-generator
- Marketing verbs "offers" and "features" instead of a plain verb, replaced by "takes", "costs", "gives you": https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Style vocabulary "comprehensive" (Kobak list) and "leverage" (GPT-6 list), replaced by "using": https://arxiv.org/html/2406.07016 and https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- "It's not X, it's Y" ("It's not just an audit. It's a transformation."), removed: https://arxiv.org/html/2510.15061 and https://storeytime.beehiiv.com/p/anti-ai-copywriting-prompts
- Interchangeable benefits in a rule of three ("Save time. Work smarter. Scale faster."), removed: https://superdesign.dev/blog/fix-generic-ai-landing-page and https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Em dash, removed with the clause it introduced: https://arxiv.org/html/2603.27006
- Mad-lib headline "The AI-powered [X] for modern [Y]", replaced by a headline that states duration and price: https://superdesign.dev/blog/fix-generic-ai-landing-page

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : étiquettes de champ (texte d'introduction ou principal, titre, bouton), bouton d'appel à l'action prédéfini et son impératif, puces de faits sans émoji, longueurs recommandées par la plateforme.

## Remarques de la source

Longueurs de l'Après : first paragraph, 69 characters (150 before truncation); headline, 51 characters out of 70. Check: 15 quotes at 40 minutes is 600 minutes, or 10 hours.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 6, apres.md en compte 4.

Exemption : paragraph_count.

La réécriture de référence retire des paragraphes entiers de remplissage (slogans, survol, clôture), ce que la règle dure 5 du skill interdit. Les tests du corpus ignorent la seule comparaison du nombre de paragraphes pour cette paire; chiffres, gras et liens restent comparés. Ce n'est pas un modèle de la règle dure 5 : un cas d'evals bâti sur elle exige le compte de avant.md.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang en --type publicite --compare avant.md
```
