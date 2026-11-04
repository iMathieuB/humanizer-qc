# Détecteurs, lecteurs humains et garde-fous

Position du humanizer face aux détecteurs, et artefacts de surcorrection interdits. Sources : la recherche compilée pour la version 3.0 (détecteurs, perception des lecteurs, surcorrection), citée point par point.

## 1. La position

Le humanizer est une passe de révision vers la voix de l'auteur : il retire les tics génériques et rapproche le texte de la façon dont son auteur écrit et parle. Il ne vise aucun score de détecteur, parce que ces scores varient de 0,0 % à 100,0 % de faux positifs selon l'outil sur les mêmes textes humains (https://arxiv.org/html/2608.26710) et que des experts repèrent encore le texte « humanisé » même quand on l'a réécrit contre une liste d'indices (https://arxiv.org/html/2501.15654). Pour une entreprise qui vend son expertise, la confiance est l'actif : croire qu'un message marketing a été écrit par l'IA réduit le bouche-à-oreille positif et la fidélité (https://www.newswise.com/articles/the-ai-authorship-effect-understanding-authenticity-moral-disgust-and-consumer-responses-to-ai-generated-marketing-communications), et être découvert après avoir caché son usage de l'IA provoque la plus forte baisse de confiance (https://news.arizona.edu/employee-news/being-honest-about-using-ai-work-makes-people-trust-you-less-research-finds). Un texte précis dans la vraie voix de l'auteur sert mieux l'entreprise qu'un texte trafiqué pour tromper une machine.

## 2. Comment fonctionnent les détecteurs en 2026

**Perplexité et rafales.** La méthode d'origine mesure la probabilité qu'un modèle choisisse exactement les mêmes mots (perplexité) et la variation de cette probabilité dans le document (rafales) (https://gptzero.me/news/perplexity-and-burstiness-what-is-it/, https://support.gptzero.me/hc/en-us/articles/15130070230551-How-do-I-interpret-burstiness-or-perplexity). Les modèles sont en moyenne plus répétitifs et ont une perplexité plus basse que les humains (https://arxiv.org/html/2405.07940).

**Classificateurs entraînés.** Les principaux éditeurs disent avoir dépassé cette méthode :

- GPTZero dit avoir abandonné la perplexité et les rafales à l'automne 2023 pour un classificateur profond phrase par phrase (https://gptzero.me/technology), et affirme un taux de faux positifs d'au plus 1 % (même source).
- Pangram dit reposer sur des négatifs difficiles et l'apprentissage actif, où les tics visibles ne sont qu'un signal parmi des centaines de milliers (https://www.pangram.com/blog/how-does-pangram-work), et déclare 0,0041 % de faux positifs pour Pangram 4 (https://www.pangram.com/blog/is-pangram-accurate).
- Turnitin analyse seulement la prose en format long, exclut les listes (https://www.turnitin.ca/products/features/ai-writing-detection) et déclare moins de 1 % de faux positifs au niveau du document, environ 4 % au niveau de la phrase (https://www.turnitin.ca/blog/ai-writing-detection-update-from-turnitins-chief-product-officer).
- Copyleaks donne selon ses propres pages de 0,03 % à 0,66 % de faux positifs (https://copyleaks.com/ai-detector/testing-methodology).

Ces chiffres viennent des éditeurs, et plusieurs déconseillent de sanctionner sur un score seul (https://gptzero.me/faq, https://originality.ai/ai-checker).

## 3. Les faux positifs

Le humanizer ne traite aucun de ces traits comme un défaut à corriger.

- **Registre formel et soigné.** Écrire de façon soignée et formelle sans IA expose à des signalements erronés (https://www.mtroyal.ca/AI/ai-detection-advisory.htm).
- **Rédacteurs non natifs et vocabulaire simple.** 61,22 % de faux positifs en moyenne sur 91 essais TOEFL humains (https://arxiv.org/html/2304.02819v3); un texte traduit automatiquement fait chuter l'exactitude de 20 % (https://edintegrity.biomedcentral.com/articles/10.1007/s40979-023-00146-z).
- **Texte très révisé.** Le score monte avec l'ampleur de la révision professionnelle (https://arxiv.org/html/2608.26710), et un polissage minimal donne de 10 % à 75 % de détection selon l'outil (https://arxiv.org/html/2502.15666).
- **Textes courts.** Sous 300 mots, Turnitin reconnaît un taux de faux positifs trop élevé (https://www.turnitin.ca/blog/new-research-turnitin-s-ai-detector-shows-no-statistically-significant-bias-against-english-language-learners); sous 50 mots, GPTZero, Originality.ai et Pangram perdent en exactitude (https://www.chicagobooth.edu/review/do-ai-detectors-work-well-enough-trust).
- **Listes, gabarits et prose technique.** Les recettes atteignent 33,4 % de faux positifs pour un seuil global de 5 % (https://arxiv.org/html/2405.07940); GPTZero nomme l'écriture technique concise, les gabarits et les réponses courtes parmi ses groupes à risque (https://gptzero.me/news/why-writing-flagged-ai). Turnitin ne détecte pas les scripts de façon fiable (https://www.turnitin.ca/products/features/ai-writing-detection).
- **Textes publics mémorisés.** La Constitution américaine et la Bible ont été classées IA par certains outils (https://arstechnica.com/information-technology/2023/07/why-ai-detectors-think-the-us-constitution-was-written-by-ai/, https://decrypt.co/286121/ai-detectors-fail-reliability-risks).

Au Québec, la majorité des plagiats par IA allégués à l'épreuve uniforme de français se sont révélés des faux positifs (https://www.sciencepresse.qc.ca/actualites-scientifiques/2026/07/09/detecteurs-ia-credibilite-defaillante).

## 4. Ce que les lecteurs humains utilisent vraiment

Les lecteurs non entraînés font le hasard : 49,9 % de bonnes réponses (https://arxiv.org/html/2107.00061). Des lecteurs qui utilisent souvent les LLM pour écrire atteignent toutefois 92,7 % de vrais positifs, même face à du texte paraphrasé ou « humanisé » (https://arxiv.org/html/2501.15654).

**Indices qui tiennent :**

- la répétition, 47 % plus susceptible d'être générée, et le contenu absurde (https://pmc.ncbi.nlm.nih.gov/articles/PMC10089155/);
- le vocabulaire typique de l'IA (vibrant, crucial, significantly), cité dans 53,1 % des explications d'experts, devant la structure formulaïque (35,9 %) (https://arxiv.org/html/2501.15654);
- l'absence de surprise, d'humour et d'originalité, les citations trop lisses et la conclusion nette qui résume tout (même source).

**Heuristiques fausses :**

- les fautes : les textes fautifs étaient jugés IA alors qu'ils étaient 15 % moins susceptibles d'être générés (https://pmc.ncbi.nlm.nih.gov/articles/PMC10089155/);
- les mots longs ou rares, pris pour de l'IA alors que la plupart de ces textes étaient humains (même source);
- le ton neutre, attribué à tort à l'IA (https://arxiv.org/html/2501.15654);
- le « je », les contractions et les sujets familiaux, associés à tort à l'humain (https://arxiv.org/abs/2206.07271).

Conséquence : retire la répétition, le vocabulaire gonflé et la structure formulaïque; ne plaque jamais de familiarité, car des textes IA optimisés selon ces heuristiques ont été jugés plus humains que de vrais textes humains (https://pmc.ncbi.nlm.nih.gov/articles/PMC10089155/).

## 5. Artefacts de surcorrection interdits

Ne produis jamais ces artefacts, typiques des outils de contournement.

- **Fautes insérées.** Des outils ajoutent des coquilles (https://arxiv.org/html/2501.03437). C'est inutile : un texte avec fautes ajoutées est revenu à 99 % IA (https://ai-in-real-life.beehiiv.com/p/do-typos-fool-ai-detectors).
- **Synonymes rares ou déplacés.** Le remplacement par dictionnaire emploie des mots hors contexte (https://arxiv.org/html/2501.03437); les humains choisissent plus souvent le mot simple, « used » plutôt que « utilized » (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).
- **Collocations cassées.** « big data » devient « enormous information » (https://arxiv.org/html/2402.03370); ces « expressions torturées » sont documentées (https://arxiv.org/abs/2107.06751). Garde intacts les termes techniques et les expressions figées.
- **Sens aplati ou déplacé.** Les humaniseurs audités dégradent le texte, et ceux fondés sur des LLM ajoutent ou retirent des phrases (https://arxiv.org/html/2501.03437). Ne retire aucun chiffre ni aucune nuance; n'ajoute rien d'absent de la source.
- **Familiarité théâtrale.** L'ajout de pronoms personnels absents de la source est un artefact connu, et les meilleurs outils reprennent le niveau et le ton de l'original (https://arxiv.org/html/2501.03437). Pas d'interjections plaquées, pas de « je » inventé.
- **Phrases hachées et bricolage typographique.** Ni découpage en phrases d'une seule proposition (https://arxiv.org/html/2501.03437), ni espaces retirées ou caractères Unicode non standard (https://www.pangram.com/blog/humanizers-aug-25).

## 6. Ce que le humanizer ne poursuit pas

- Un score « humain » sur un détecteur, quel qu'il soit.
- Le mot « indétectable », dans le texte comme dans la promesse.
- La suppression d'une liste, d'un tableau, d'un gabarit ou d'un registre formel quand le type de contenu les demande.
- L'ajout de fautes, de familiarité ou de mots rares pour « faire humain ».
- L'effacement de toute trace d'assistance par IA : la transparence relève de l'auteur, pas de l'outil.

## 7. Gabarit du mode audit

```
**Langue :** <fr|en> · **Type :** <clé> · **Mode :** audit · **Mots :** <n> · **Tics :** <n> haute, <n> moyenne, <n> basse

| # | Position | Gravité | Patron | Extrait | Source |
|---|---|---|---|---|---|
| 1 | §<n> (L<ligne>) | <haute|moyenne|basse> | <Pnn> <nom du patron> | « <extrait de 12 mots au plus> » | <URL ou « observation maison »> |

**Grappes :** <paragraphes où les tics se concentrent, une ligne>
**Protégés, non comptés :** <éléments protégés repérés qui ressemblent à des tics>
**Vérification :** verif_humanizer.py, code <0|1|2> (<n> erreurs, <n> avertissements), ou « script non exécuté : <raison> »
```

Ni réécriture, ni remplacement, ni fichier modifié. Tri par position. Source : la meilleure du patron. Hypothèse de type ou de langue : une ligne au-dessus du tableau. Rien repéré : « Aucun tic repéré. » à la place du tableau. Texte écrit ou approuvé par l'auteur (`auteur=texte-auteur`) ou texte d'un tiers (`auteur=tiers`) : c'est le mode par défaut, et les formulations rejetées du profil de voix (`voix-auteur.md`) s'y signalent sans se corriger.
