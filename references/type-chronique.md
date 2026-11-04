# Type : Script de chronique vidéo parlée (chronique et reel)

Script de tournage d'une vidéo parlée : chronique longue (par exemple 9 à 11 minutes) ou reel (110 à 220 mots dits); publications qui l'accompagnent : `publicite`; article compagnon : `article`. Script : `--type chronique`. Indices de structure : codes temporels, lignes ▶ ou « accroche ». Mode en conversation : `interactif`. En pipeline : un skill de publication vidéo (section 7). Du fichier de langue, lis l'index et les patrons de la section 5 seulement.

## 1. Éléments protégés

1. Les plages de minutage (0:00, tiret demi-cadratin, 0:30) et la cible de durée : protégées par la requête. Exception déclarée `timecode-dash` (section 9).
2. Les lignes ▶ (réalisation) et la liste « À ne pas dire à l'écran » : non dites, leur prose ne se réécrit pas. Seule retouche : un tiret y devient virgule ou point (le script le signale en `warning`).
3. L'accroche incrustée et le titre entre guillemets : l'auteur choisit et réécrit l'accroche à la main; le titre se recopie ailleurs.
4. Les indications phonétiques entre crochets : elles évitent au lecteur de trébucher.
5. La chaîne chiffrée figée avant le tournage, « environ » compris : référence de tout le reste.
6. Les répétitions voulues et le verbe unique de l'épisode : celui de la grille, repris tel quel dans toute la vidéo; aucun synonyme, aucun verbe qui ne couvre qu'une partie du geste (si le geste est « traiter » un courriel, ni « lire » ni « gérer »).
7. Le vouvoiement (ou le tutoiement choisi par la série) et le « je » qui fait le geste au présent : règle de la série.
8. La consigne de l'aimant et son mot déclencheur (« Écrivez MOTCLÉ en commentaire »).
9. Les mentions d'honnêteté : « basé sur un cas réel », taux « estimé », projection annoncée, réserve après la démonstration.
10. Les noms exacts des outils, marque et version.
11. Les drapeaux [NEEDS SOURCE] : aucune statistique inventée.
12. Le script final, la dictée ou tout texte approuvé par l'auteur (`auteur=texte-auteur`) : mode `audit` par défaut; en correction demandée, règles dures 1, 7 et 8 seulement. La première version de l'assistant reçoit la passe complète, formulations rejetées du profil de voix comprises.

## 2. Structures légitimes à ne pas signaler

- Phrases courtes, une idée par phrase (neutralise P31 sous le seuil de staccato).
- Répétition d'un mot clé plutôt qu'un synonyme : ne varie jamais pour varier.
- Vouvoiement et questions à l'auditoire, sans ton artificiel (neutralise P61).
- Présent et passé composé; phrase qui paraîtrait enfantine à l'écrit mais sonne naturelle à l'oreille.
- Chiffre arrondi ou « environ » prévu par la chaîne figée (forme dite seulement, jamais la valeur).
- Attente commentée pendant une démonstration, réserve placée après (neutralise P69).
- Le « là » et les marqueurs québécois que l'auteur dit : n'en ajoute pas, n'en retire pas d'une transcription (neutralise P67).
- Structure de reel prévue par le gabarit de la série (démonstration, objection retournée, erreur racontée, décorticage, chiffre qui recadre), même répétée (neutralise P59).

## 3. Tics propres au type

- Ouverture qui annonce le programme (« Dans cette vidéo, nous allons voir », "let's dive in"); appel à l'action générique (« abonnez-vous pour plus »). https://www.opus.pro/blog/chatgpt-prompts-video-scripts-2026
- Script correct qui ne sonne comme personne. https://www.kapwing.com/resources/how-to-get-chatgpt-to-write-video-scripts-in-your-tone-of-voice/
- Ton positif uniforme, éloge du sujet, analogies presque justes, hésitations plaquées. https://simonwillison.net/2024/Sep/29/notebooklm-audio-overview/
- Règle de trois en série. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Synonymes variés qui brouillent l'écoute unique. https://www.npr.org/sections/npr-training/2025/05/31/g-s1-66074/would-you-say-it-that-way-tips-on-writing-for-your-voice
- Phrase trop longue pour un souffle; point-virgule ou deux-points dans le texte dit (règle radio transposée). https://mediahelpingmedia.org/quick-guides/writing-a-radio-news-script/
- Style écrit : « qui », « que », « parce que » en chaîne, « car », « en effet », imparfait, passé simple, participe présent. https://pedagogie.ac-toulouse.fr/emi/node/1198
- Préambule (« aujourd'hui je vais vous parler de »), « il faut » au lieu du « je », récapitulatif final, « donc » ou « fait que » partout. Règle maison du skill.
- Formule qui commente au lieu d'informer; phrase sans fonction claire. Règle maison du skill.
- Sens porté par une négation que le lapsus retourne; nombre exact indicible. Règle maison du skill.

## 4. Registre

Oral préparé, expert-conseil qui pose un diagnostic, ton factuel et clinique, vouvoiement partout. Permis : syntaxe orale, répétitions, « je » au présent, « environ ». Exclus : couleur conversationnelle, commentaire du rédacteur, piques, posture de vendeur. Un profil de voix (`voix-auteur.md`) ou un échantillon de l'auteur l'emporte sur ce registre par défaut.

## 5. Patrons prioritaires

(fr) : patterns-fr.md seulement; (en) : patterns-en.md seulement; sinon les deux.

- P54 Tiret cadratin en français (fr); P14 Em dashes (and en dashes): cut them (en)
- P51 Vocabulaire gonflé en français (fr); P07 Overused "AI vocabulary" words (en)
- P49 Restes de conversation et flatterie (fr); P20 Collaborative communication artifacts (en)
- P63 « Non seulement X, mais aussi Y », en chute ou en titre compris (fr); P09 Negative parallelisms and tailing negations (en)
- P61 Style impersonnel et consensuel (fr)
- P40 Nominalisations
- P68 Phrase trop longue pour une respiration
- P53 Annonces et survols en français (fr); P28 Signposting and announcements (en)
- P55 Point-virgule et deux-points en série (fr)
- P50 Connecteurs et formules de liaison lourds (fr); P23 Filler phrases (en)
- P67 Hésitations mécaniques
- P69 Ton enjoué et éloge du sujet
- P70 Appel à l'action générique

## 6. Seuils du script pour ce type

| Seuil | chronique |
|---|---|
| Densité vocabulaire, `warning` au-delà (pour 1 000 mots) | fr 6, en 8 |
| Triades, `warning` au-delà (pour 1 000 mots) | 3 |
| Staccato : phrases consécutives de 3 mots ou moins | 4, `warning` |
| CV minimal des phrases (si 12 phrases ou plus) | 0,40 |
| Phrase longue, mots | 30, `warning` |
| Gras non numérique, `warning` au-delà (pour 1 000 mots) | 2 |
| Listes à intitulé en gras | `warning` |
| Émojis | chaque émoji `warning` |
| `!` : `warning` à partir de | 3 |
| Longueur par section (caractères) | aucun |

Ces seuils sont ceux de verif_humanizer.py; en cas d'écart, le script fait foi.

## 7. Ce que les pipelines attendent

- **Skill de publication vidéo** : ce que l'assistant compose ou réécrit pour la vidéo (script, accroche, texte d'accompagnement) passe par humanizer, puis se montre à l'auteur en citation avant son accord.
- **Passe de révision de fond** : elle passe avant; humanizer en dernier, refait sur les passages touchés après tout changement. Négation porteuse de sens réécrite en affirmation; nombre exact dicible; même verbe pour le même geste dans tout le script et toute la vidéo.
- **Règles de la série** : la dictée de l'auteur s'applique à la lettre. Exemple chiffré en nombres exacts qui se multiplient juste. Les réserves de l'assistant (risques, contre-arguments) vont dans le rapport de livraison, jamais dans le texte dit.

## 8. Liste de contrôle

- [ ] Le texte dit est-il sans tiret?
- [ ] Les plages de minutage, les lignes ▶ et la liste « À ne pas dire à l'écran » sont-elles intactes?
- [ ] Chaque phrase se dit-elle d'un seul souffle à voix haute?
- [ ] La première phrase est-elle déjà le sujet, sans préambule?
- [ ] Le script finit-il sans récapitulatif, avec le même verbe partout pour le geste?
- [ ] Le lecteur est-il vouvoyé (ou tutoyé selon la série), et « je » fait-il le geste au présent?
- [ ] Les chiffres sont-ils ceux de la chaîne figée, et dicibles?
- [ ] Aucune phrase clé ne tient-elle à une négation?
- [ ] La passe n'a-t-elle ajouté aucune hésitation ni marqueur oral?
- [ ] Aucun point-virgule ni deux-points d'annonce dans le texte dit?
- [ ] Les mentions « basé sur un cas réel », « estimé » et les réserves sont-elles conservées?
- [ ] Aucun nom de client ni détail qui rendrait un cas identifiable?
- [ ] Le nombre de mots dits par section varie-t-il de 10 % au plus?
- [ ] Chaque paragraphe tient-il sur une ligne, et leur nombre est-il inchangé?

## 9. Lecture à voix haute et minutage

- **Lecture à voix haute.** Dis chaque phrase comme à la caméra : « le dirait-on comme ça? » Coupe au-delà de 30 mots (`warning`).
- **Unités de souffle.** Une phrase, une idée, un souffle. Coupe aux « qui », « que », « parce que ». Virgule et point seulement dans le texte dit.
- **Répétition voulue.** Garde le même mot : un synonyme fait croire à l'auditeur qu'on parle d'autre chose.
- **Minutage préservé.** Pas plus de 10 % d'écart de mots dits par section (`stats.spoken_words`, sans régie, codes temporels ni crochets).
- **Chiffres en lettres** écrits pour la lecture : garde-les tels quels.
- **`timecode-dash`.** Le tiret entre deux codes temporels est admis (`info`), automatique avec `--type chronique`. Si l'auteur préfère, remplace-le par « à » sans toucher aux temps.

## 10. Exemple court

Exemple fictif (paire `evals/corpus/chronique/fr-01-relances-factures`, segment « Le coût »).

**Avant**
> Il est important de noter que l'entreprise — 22 employés — envoyait 140 relances par mois; chaque relance prenait 6 minutes. Cela représente 14 heures par mois; à 40 $ de l'heure, 560 $ par mois, soit 6 720 $ par année.

**Après**
> Cette entreprise de 22 employés envoyait 140 relances par mois. Une relance prenait 6 minutes. Ça fait 14 heures par mois. À 40 $ de l'heure, c'est 560 $ par mois. Sur une année, 6 720 $.

Corrigés : P50, P54, P55, P68. Chiffres au caractère près, « 22 employés » compris.
