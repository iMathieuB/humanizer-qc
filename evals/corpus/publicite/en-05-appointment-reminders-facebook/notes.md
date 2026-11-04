# Notes : publicite, en, paire 5

Source : jeu d'exemples fictifs de la version 3.0, Publicité LinkedIn ou Meta, Paire 5 (EN) : Appointment reminders for a clinic, Meta Facebook feed. Texte fictif rédigé pour le humanizer v3; « avant » mauvais exprès.

## Tics corrigés

- Variants that open on "Get" with exclamation marks and emojis, as in Meta's own generated examples ("Get the best patient experience ever!", "Get the best reminders now!"), rewritten as plain statements: https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features
- Comparatives and superlatives used to push persuasion ("best", "faster, smarter, better"), removed: https://arxiv.org/html/2601.04925v1
- Stacked imperatives in the body ("Book now. Grow faster. Don't wait!"), removed; the imperative stays only in the predefined "Book now" button: https://arxiv.org/html/2601.04925v1 and https://www.facebook.com/business/ads-guide/update/image/facebook-marketplace
- Aspirational slogan "Transform your clinic", replaced by the clinic's numbers, which read as direct rather than inspiring: https://arxiv.org/html/2512.03373v1
- Evaluative adjective "innovative" (Liang et al. list), removed: https://arxiv.org/html/2403.07183
- Emoji at the start of each line (📅, 💰, 📈) and mid-sentence (🚀), removed: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Em dash, removed with the triad it introduced: https://arxiv.org/html/2603.27006

## Structures conservées

Structures du type, selon l'introduction de la section dans la source : étiquettes de champ (texte d'introduction ou principal, titre, bouton), bouton d'appel à l'action prédéfini et son impératif, puces de faits sans émoji, longueurs recommandées par la plateforme.

## Remarques de la source

Longueurs de l'Après : primary text, 135 characters (range of 50 to 150); headline, 24 characters out of 27. Check: 2 no-shows at $90 is $180 a day.

## Paragraphes

Règle des paragraphes de scripts/verif_humanizer.py, fonction count_paragraphs (ligne de prose, titre, puce, rangée, ligne de régie, code temporel) : avant.md en compte 7, apres.md en compte 3.

Exemption : paragraph_count.

La réécriture de référence retire des paragraphes entiers de remplissage (slogans, survol, clôture), ce que la règle dure 5 du skill interdit. Les tests du corpus ignorent la seule comparaison du nombre de paragraphes pour cette paire; chiffres, gras et liens restent comparés. Ce n'est pas un modèle de la règle dure 5 : un cas d'evals bâti sur elle exige le compte de avant.md.

## Vérification attendue

```
python3 -I scripts/verif_humanizer.py apres.md --lang en --type publicite --compare avant.md
```
