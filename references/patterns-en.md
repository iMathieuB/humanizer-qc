# English patterns (humanizer 3.0.0)

Use this file for English text. The pass edits toward the author's voice: it removes generic AI tics and keeps every fact, number and link; it is not a tool for evading AI detectors. Read the index first, then only the sections you need (grep `^### Pnn`). IDs are shared with patterns-fr.md: a pattern marked for both languages has the same ID, level and sources in both files.

Metadata line of each pattern. Level, the strength of the best source, in lowercase French as in the script output: `mesure` (study or quantitative measurement), `guide` (editorial or institutional guide, Wikipedia included), `blogue` (vendor or practitioner post), `maison` (house rule: a formula flagged by the skill's own evaluation, or a rejection documented in the author's voice profile; for that author's voice it outranks the three others). Origin: `2.8` (text inherited from humanizer 2.8.0 by Siqi Chen, kept as is), `recherche` (3.0 research) or `maison`. Types: type keys of SKILL.md, `all` for the five. Script: the check in scripts/verif_humanizer.py that reports the pattern, or `reading`. One tic alone proves nothing: look for clusters.

## Index

| ID | Pattern | Level | Types | Script check |
|---|---|---|---|---|
| P01 | Undue emphasis on significance, legacy and broader trends | guide | article, page_web | reading |
| P02 | Undue emphasis on notability and media coverage | guide | article, page_web | reading |
| P03 | Superficial analyses with -ing endings | mesure | article, page_web, formation | reading |
| P04 | Promotional and advertisement-like language | guide | article, page_web, publicite | reading |
| P05 | Vague attributions and weasel words | guide | article, page_web | reading |
| P06 | Outline-like "Challenges and future prospects" sections | guide | article, page_web, formation | reading |
| P07 | Overused AI vocabulary | mesure | all | kill_list/vocabulaire |
| P08 | Copula avoidance | guide | article, page_web, publicite | reading |
| P09 | Negative parallelisms and tailing negations | mesure | all | not_x_but_y |
| P10 | Rule of three overuse | mesure | article, page_web, publicite | triad |
| P11 | Elegant variation (synonym cycling) | guide | article, formation | reading |
| P12 | False ranges | guide | article, page_web | reading |
| P13 | Passive voice and subjectless fragments | guide | page_web, formation | reading |
| P14 | Em dashes and en dashes | mesure | all | dash |
| P15 | Overuse of boldface | mesure | article, page_web, formation | bold_density |
| P16 | Inline-header vertical lists | mesure | article, page_web, formation | inline_header_list |
| P17 | Title case in headings | guide | article, page_web, formation | title_case |
| P18 | Emojis | mesure | page_web, publicite, formation | emoji, kill_list/ponctuation |
| P19 | Curly quotation marks | guide | article, page_web | curly_quotes |
| P20 | Collaborative communication artifacts | guide | all | reading |
| P21 | Knowledge-cutoff disclaimers and speculative gap-filling | guide | article, page_web | reading |
| P22 | Sycophantic or servile tone | guide | publicite, chronique | reading |
| P23 | Filler phrases | guide | all | kill_list/formules |
| P24 | Excessive hedging | guide | article, formation | hedging_stack |
| P25 | Generic positive conclusions | guide | article, page_web, chronique | kill_list/clotures |
| P26 | Hyphenated word pair overuse | guide | article, page_web | reading |
| P27 | Persuasive authority tropes | guide | article, chronique | reading |
| P28 | Signposting and announcements | guide | article, chronique, formation | reading |
| P29 | Fragmented headers | guide | article, page_web, formation | reading |
| P30 | Diff-anchored writing | guide | formation | reading |
| P31 | Manufactured punchlines and staccato drama | blogue | article, publicite, chronique | staccato |
| P32 | Aphorism formulas | guide | article, publicite, chronique | reading |
| P33 | Conversational rhetorical openers | guide | publicite, chronique | reading |
| P34 | Vague link | guide | article, page_web | reading |
| P35 | Template section headings | guide | article, page_web | reading |
| P36 | Inverted parallelism "Y rather than X" | guide | all | reading |
| P37 | Corrective disclaimers about sources | guide | article, formation | reading |
| P38 | GPT-6 era vocabulary and uniform sentence length | guide | article, page_web, publicite | reading |
| P39 | Cluster of measured style words | mesure | all | reading |
| P40 | Nominalizations | mesure | all | reading |
| P41 | Missing downtoners | mesure | article, formation | reading |
| P42 | Generation leftovers (placeholders, prompts, tracking) | guide | all | kill_list/structure |
| P43 | Small tables and empty headings | guide | article, page_web, formation | reading |
| P44 | Section-ending summary | guide | article, chronique, formation | reading |
| P45 | Repetitive content | mesure | article, page_web | reading |
| P46 | Interchangeable "In today's world" opening | blogue | article, page_web, publicite, chronique | kill_list/ouvertures |
| P67 | Mechanical filler hesitations | blogue | chronique | reading |
| P68 | Too many clauses for one breath | guide | chronique | long_sentence |
| P69 | Relentlessly upbeat tone and praise of the subject | blogue | publicite, chronique | reading |
| P70 | Generic call to action | blogue | publicite, chronique | reading |
| P71 | Mad-lib headline | blogue | page_web, publicite | reading |
| P72 | Interchangeable slogan fragments and stacked imperatives | blogue | publicite | exclamation |
| P73 | Hollow aspirational formula | blogue | page_web, publicite | reading |
| P74 | Implausible quiz distractors | mesure | formation | reading |
| P81 | Sentence too long on the page | maison | all | long_sentence |
| P82 | Commas that separate nothing | maison | all | comma_load |
| P83 | Sentence with no finite verb | maison | article, page_web, formation, general | reading |

## Voice and soul

The hard rules of SKILL.md win over this section: never add an opinion, a first person, a tangent or a fact absent from the source, and never copy dashes from a sample.

Breath (hard rule 10): a removed sentence leaves no hole, so reconnect the sentences around it (because, so, but). Never write a filler sentence to fill a gap: cut it, or reuse a fact already in the text. Outside a spoken script, no run of short juxtaposed sentences and no paragraph reduced to a fragment: keep the author's variation of sentence length. A trimmed tell is still a tell ("has become a crucial issue" minus "crucial"): replace the sentence with the first fact of the text, or cut it.

### Voice Calibration (Optional)

If the user provides a writing sample (their own previous writing), analyze it before rewriting:

1. **Read the sample first.** Note:
   - Sentence length patterns (short and punchy? Long and flowing? Mixed?)
   - Word choice level (casual? academic? somewhere between?)
   - How they start paragraphs (jump right in? Set context first?)
   - Punctuation habits (lots of dashes? Parenthetical asides? Semicolons?)
   - Any recurring phrases or verbal tics
   - How they handle transitions (explicit connectors? Just start the next point?)

2. **Match their voice in the rewrite.** Don't just remove AI patterns: replace them with patterns from the sample. If they write short sentences, don't produce long ones. If they use "stuff" and "things," don't upgrade to "elements" and "components."

3. **When no sample is provided,** fall back to the default behavior (natural, varied, opinionated voice from the PERSONALITY AND SOUL section below).

#### How to provide a sample
- Inline: "Humanize this text. Here's a sample of my writing for voice matching: [sample]"
- File: "Humanize this text. Use my writing style from [file path] as a reference."

### PERSONALITY AND SOUL

Avoiding AI patterns is only half the job. Sterile, voiceless writing is just as obvious as slop. Good writing has a human behind it.

**Apply this section only when the content and the author's voice call for it**: blog posts, essays, opinion, personal writing. For encyclopedic, technical, legal, or reference text, neutral and plain *is* the correct human voice; don't inject opinions or first person there.

#### Signs of soulless writing (even if technically "clean"):
- Every sentence is the same length and structure
- No opinions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- No first-person perspective when appropriate
- No humor, no edge, no personality
- Reads like a Wikipedia article or press release

#### How to add voice:

**Have opinions.** Don't just report facts; react to them. "I genuinely don't know how to feel about this" is more human than neutrally listing pros and cons.

**Vary your rhythm.** Short punchy sentences. Then longer ones that take their time getting where they're going. Mix it up.

**Let some mess in.** Perfect structure feels algorithmic. Tangents, asides, and half-formed thoughts are human.

#### Before (clean but soulless):
> The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical. The implications remain unclear.

#### After (has a pulse):
> I genuinely don't know how to feel about this one. 3 million lines of code, generated while the humans presumably slept. Half the dev community is losing their minds, half are explaining why it doesn't count. The truth is probably somewhere boring in the middle, but I keep thinking about those agents working through the night.

If references/voix-auteur.md exists (an optional voice profile written by the user), use it together with the sample.

## Patterns from 2.8 (P01 to P33)

**Content patterns**

### P01. Undue emphasis on significance, legacy, and broader trends

Level: guide · Origin: 2.8 · Types: article, page_web · Script: reading

**Words to watch:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted

**Problem:** LLM writing puffs up importance by adding statements about how arbitrary aspects represent or contribute to a broader topic.

**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance.

**After:**
> The Statistical Institute of Catalonia was established in 1989 to collect and publish regional statistics independently from Spain's national statistics office.

**False positive.** An analysis that demonstrates an event's reach with precise facts is fine.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P02. Undue emphasis on notability and media coverage

Level: guide · Origin: 2.8 · Types: article, page_web · Script: reading

**Words to watch:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence

**Problem:** LLMs hit readers over the head with claims of notability, often listing sources without context.

**Before:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.

**After:**
> In a 2024 New York Times interview, she argued that AI regulation should focus on outcomes rather than methods.

**False positive.** A press page or media kit, where the coverage list is the content, is fine.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative

### P03. Superficial analyses with -ing endings

Level: mesure · Origin: 2.8 · Types: article, page_web, formation · Script: reading

**Words to watch:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...

**Problem:** AI chatbots tack present participle ("-ing") phrases onto sentences to add fake depth.

**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.

**After:**
> The temple uses blue, green, and gold colors. The architect said these were chosen to reference local bluebonnets and the Gulf coast.

**False positive.** A participle clause that describes a real, simultaneous action ("She left, slamming the door") is normal English.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://arxiv.org/html/2410.16107

### P04. Promotional and advertisement-like language

Level: guide · Origin: 2.8 · Types: article, page_web, publicite · Script: reading

**Words to watch:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning

**Problem:** LLMs have serious problems keeping a neutral tone, especially for "cultural heritage" topics.

**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.

**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia, known for its weekly market and 18th-century church.

**False positive.** An ad or a service page is allowed to sell; the problem is generic praise, not commercial intent.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P05. Vague attributions and weasel words

Level: guide · Origin: 2.8 · Types: article, page_web · Script: reading

**Words to watch:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few cited)

**Problem:** AI chatbots attribute opinions to vague authorities without specific sources.

**Before:**
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.

**After:**
> The Haolai River supports several endemic fish species, according to a 2019 survey by the Chinese Academy of Sciences.

**False positive.** A common-sense generalization in a signed opinion piece does not need an authority.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P06. Outline-like "Challenges and future prospects" sections

Level: guide · Origin: 2.8 · Types: article, page_web, formation · Script: reading

**Words to watch:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

**Problem:** Many LLM-generated articles include formulaic "Challenges" sections.

**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.

**After:**
> Traffic congestion increased after 2015 when three new IT parks opened. The municipal corporation began a stormwater drainage project in 2022 to address recurring floods.

**False positive.** A "Risks" section required by the format (bid, case study) stays if it is concrete.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

**Language and grammar patterns**

### P07. Overused "AI vocabulary" words

Level: mesure · Origin: 2.8 · Types: all · Script: kill_list/vocabulaire

**High-frequency AI words:** Actually, additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

**Problem:** These words appear far more frequently in post-2023 text. They often co-occur.

**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.

**After:**
> Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south.

**False positive.** A listed word used alone and in its literal sense (a landscaper's "landscape") is not a tell.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://arxiv.org/html/2406.07016; https://arxiv.org/html/2412.11385; https://arxiv.org/abs/2509.09596

### P08. Avoidance of "is"/"are" (copula avoidance)

Level: guide · Origin: 2.8 · Types: article, page_web, publicite · Script: reading

**Words to watch:** serves as/stands as/marks/represents [a], boasts/features/offers [a]

**Problem:** LLMs substitute elaborate constructions for simple copulas.

**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.

**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.

**False positive.** "Features" in a product sheet that lists real functions is normal usage.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P09. Negative parallelisms and tailing negations

Level: mesure · Origin: 2.8 · Types: all · Script: not_x_but_y

**Problem:** Constructions like "Not only...but..." or "It's not just about..., it's..." are overused. So are clipped tailing-negation fragments such as "no guessing" or "no wasted motion" tacked onto the end of a sentence instead of written as a real clause.

**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.

**After:**
> The heavy beat adds to the aggressive tone.

**Before (tailing negation):**
> The options come from the selected item, no guessing.

**After:**
> The options come from the selected item without forcing the user to guess.

**False positive.** Correcting a misconception the reader really holds ("it's not an extra fee, it's included in the plan") stays useful.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://arxiv.org/html/2510.15061

### P10. Rule of three overuse

Level: mesure · Origin: 2.8 · Types: article, page_web, publicite · Script: triad

**Problem:** LLMs force ideas into groups of three to appear comprehensive.

**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.

**After:**
> The event includes talks and panels. There's also time for informal networking between sessions.

**False positive.** A list of three real, distinct items, such as the three steps of a procedure, is normal.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://www.pangram.com/signs-of-ai-writing

### P11. Elegant variation (synonym cycling)

Level: guide · Origin: 2.8 · Types: article, formation · Script: reading

**Problem:** AI has repetition-penalty code causing excessive synonym substitution.

**Before:**
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.

**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.

**False positive.** Writers trained to avoid repetition, many non-native speakers among them, do it too; flag it only in a cluster.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P12. False ranges

Level: guide · Origin: 2.8 · Types: article, page_web · Script: reading

**Problem:** LLMs use "from X to Y" constructions where X and Y aren't on a meaningful scale.

**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.

**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.

**False positive.** A real, measurable range ("from 5 to 50 employees") is correct.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P13. Passive voice and subjectless fragments

Level: guide · Origin: 2.8 · Types: page_web, formation · Script: reading

**Problem:** LLMs often hide the actor or drop the subject entirely with lines like "No configuration file needed" or "The results are preserved automatically." Rewrite these when active voice makes the sentence clearer and more direct.

**Before:**
> No configuration file needed. The results are preserved automatically.

**After:**
> You do not need a configuration file. The system preserves the results automatically.

**False positive.** The passive is right when the actor is unknown or irrelevant; fragments are normal in a short ad or an interface.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

**Style patterns**

### P14. Em dashes (and en dashes): cut them

Level: mesure · Origin: 2.8 · Types: all · Script: dash

**Rule:** The final rewrite contains no em dashes (U+2014) or en dashes (U+2013). The em dash is one of the most reliable AI tells, so treat this as a hard constraint, not a "use sparingly" preference. Replace each one, in rough order of preference: a period (start a new sentence), a comma (a tight aside), a colon (introducing an explanation), parentheses (a true aside), or restructure the sentence. Also catch spaced em dashes (an em dash with a space on each side) and double hyphens (` -- `) used the same way.

**Before:**
> The term is primarily promoted by Dutch institutions—not by the people themselves. You don't say "Netherlands, Europe" as an address—yet this mislabeling continues—even in official documents.

**After:**
> The term is primarily promoted by Dutch institutions, not by the people themselves. You don't say "Netherlands, Europe" as an address, yet this mislabeling continues in official documents.

**Before:**
> The new policy — announced without warning — affects thousands of workers. The changes -- long overdue according to critics -- will take effect immediately.

**After:**
> The new policy, announced without warning, affects thousands of workers. The changes, long overdue according to critics, will take effect immediately.

Before returning the final rewrite, scan it for U+2014 and U+2013. Any hit means the draft isn't done.

**False positive.** Alone, a dash proves nothing about authorship; hard rule 1 of this skill still bans it from every output.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://arxiv.org/html/2603.27006

### P15. Overuse of boldface

Level: mesure · Origin: 2.8 · Types: article, page_web, formation · Script: bold_density

**Problem:** AI chatbots emphasize phrases in boldface mechanically.

**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.

**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.

**False positive.** An AEO article that bolds two or three key figures respects its format.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style; https://www.pangram.com/signs-of-ai-writing

### P16. Inline-header vertical lists

Level: mesure · Origin: 2.8 · Types: article, page_web, formation · Script: inline_header_list

**Problem:** AI outputs lists where items start with bolded headers followed by colons.

**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.

**After:**
> The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.

**False positive.** Training material or a spec sheet where each bullet is a distinct step or field keeps its list.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style; https://www.pangram.com/signs-of-ai-writing

### P17. Title case in headings

Level: guide · Origin: 2.8 · Types: article, page_web, formation · Script: title_case

**Problem:** AI chatbots capitalize all main words in headings.

**Before:**
> ## Strategic Negotiations And Global Partnerships

**After:**
> ## Strategic negotiations and global partnerships

**False positive.** A house style guide that imposes headline case in English (AP, Chicago) wins.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style

### P18. Emojis

Level: mesure · Origin: 2.8 · Types: page_web, publicite, formation · Script: emoji, kill_list/ponctuation

**Problem:** AI chatbots often decorate headings or bullet points with emojis.

**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting

**After:**
> The product launches in Q3. User research showed a preference for simplicity. Next step: schedule a follow-up meeting.

**False positive.** An ad or a social post where the brand already uses one emoji consistently is fine.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style; https://www.pangram.com/signs-of-ai-writing

### P19. Curly quotation marks

Level: guide · Origin: 2.8 · Types: article, page_web · Script: curly_quotes

**Problem:** ChatGPT uses curly quotes (“...”) instead of straight quotes ("...").

**Before:**
> He said “the project is on track” but others disagreed.

**After:**
> He said "the project is on track" but others disagreed.

**False positive.** Most editors and CMSes curl quotes by default, and per the Style subpage, Gemini and Claude generally do not use them.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style

**Communication patterns**

### P20. Collaborative communication artifacts

Level: guide · Origin: 2.8 · Types: all · Script: reading

**Words to watch:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., Want me to...?, Want me to give examples?, Should I continue?, let me know, here is a...

**Problem:** Text meant as chatbot correspondence gets pasted as content.

**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

**False positive.** A real email addressed to someone can offer help; the tell is chatbot phrasing in published text.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P21. Knowledge-cutoff disclaimers and speculative gap-filling

Level: guide · Origin: 2.8 · Types: article, page_web · Script: reading

**Words to watch:** as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information, not publicly available, maintains a low profile, keeps personal details private, prefers to stay out of the spotlight, likely [grew up/studied/began], it is believed that

**Problem:** Two related tells. (a) Older models leave hard knowledge-cutoff disclaimers in the text. (b) When a model can't find a source, it writes a paragraph *about* not finding one and then invents plausible filler to cover the gap. For a private person the guess almost always lands on the same stock phrases ("maintains a low profile," "keeps personal details private"), none of it sourced. Say what isn't known, or cut the sentence; don't dress a guess up as fact.

**Before (cutoff disclaimer):**
> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.

**After:**
> The company was founded in 1994, according to its registration documents.

**Before (speculative gap-fill):**
> Information about her early life is not publicly available, suggesting she maintains a low profile and keeps personal details private. She likely grew up in a middle-class household, which shaped her later interest in education reform.

**After:**
> Her early life is not documented in the available sources. (Or omit the section.)

**False positive.** An honest, dated note on the limits of a source ("2024 data") is good practice.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P22. Sycophantic/servile tone

Level: guide · Origin: 2.8 · Types: publicite, chronique · Script: reading

**Problem:** Overly positive, people-pleasing language.

**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.

**After:**
> The economic factors you mentioned are relevant here.

**False positive.** A public reply to a specific comment can thank the person once, without flattery.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

**Filler and hedging**

### P23. Filler phrases

Level: guide · Origin: 2.8 · Types: all · Script: kill_list/formules

**Before → After:**
- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "At this point in time" → "Now"
- "In the event that you need help" → "If you need help"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"

**False positive.** Wikipedia lists isolated "in order to" and "the fact that" among phrasings more frequent in human text; flag only accumulation.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P24. Excessive hedging

Level: guide · Origin: 2.8 · Types: article, formation · Script: hedging_stack

**Problem:** Over-qualifying statements.

**Before:**
> It could potentially possibly be argued that the policy might have some effect on outcomes.

**After:**
> The policy may affect outcomes.

**False positive.** Wikipedia lists isolated "perhaps" or "tends to" among human phrasings; one justified nuance stays.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P25. Generic positive conclusions

Level: guide · Origin: 2.8 · Types: article, page_web, chronique · Script: kill_list/clotures

**Problem:** Vague upbeat endings.

**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.

**After:**
> The company plans to open two more locations next year.

**False positive.** A conclusion that announces a specific decision or project is fine.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P26. Hyphenated word pair overuse

Level: guide · Origin: 2.8 · Types: article, page_web · Script: reading

**Words to watch:** third-party, cross-functional, client-facing, data-driven, decision-making, well-known, high-quality, real-time, long-term, end-to-end

**Problem:** AI hyphenates these uniformly, including in predicate position (`the report is high-quality`). Humans hyphenate inconsistently, typically only when the compound is attributive (`a high-quality report`) and often dropping the hyphen otherwise (`the report is high quality`). Keep attributive-position hyphens; drop them when the compound follows the noun.

**Before:**
> The cross-functional team delivered a high-quality, data-driven report. The team is cross-functional, the report is high-quality, and the methodology is data-driven.

**After:**
> The cross-functional team delivered a high-quality, data-driven report. The team is cross functional, the report is high quality, and the methodology is data driven.

**False positive.** Dictionary compounds ("well-being", "self-employed") keep their hyphen in every position.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P27. Persuasive authority tropes

Level: guide · Origin: 2.8 · Types: article, chronique · Script: reading

**Phrases to watch:** The real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter

**Problem:** LLMs use these phrases to pretend they are cutting through noise to some deeper truth, when the sentence that follows usually just restates an ordinary point with extra ceremony.

**Before:**
> The real question is whether teams can adapt. At its core, what really matters is organizational readiness.

**After:**
> The question is whether teams can adapt. That mostly depends on whether the organization is ready to change its habits.

**False positive.** A real reframing of the question in a debate or an analysis can keep "the question is".

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P28. Signposting and announcements

Level: guide · Origin: 2.8 · Types: article, chronique, formation · Script: reading

**Phrases to watch:** Let's dive in, let's explore, let's break this down, here's what you need to know, now let's look at, without further ado

**Problem:** LLMs announce what they are about to do instead of doing it. This meta-commentary slows the writing down and gives it a tutorial-script feel.

**Before:**
> Let's dive into how caching works in Next.js. Here's what you need to know.

**After:**
> Next.js caches data at multiple layers, including request memoization, the data cache, and the router cache.

**False positive.** Learning objectives announced at the start of a training module are expected structure.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://styleguide.dynatrace.com/docs/best-practices/remove-ai-writing-patterns-from-content; https://www.opus.pro/blog/chatgpt-prompts-video-scripts-2026; https://simonwillison.net/2024/Sep/29/notebooklm-audio-overview/

### P29. Fragmented headers

Level: guide · Origin: 2.8 · Types: article, page_web, formation · Script: reading

**Signs to watch:** A heading followed by a one-line paragraph that simply restates the heading before the real content begins.

**Problem:** LLMs often add a generic sentence after a heading as a rhetorical warm-up. It usually adds nothing and makes the prose feel padded.

**Before:**
> ## Performance
>
> Speed matters.
>
> When users hit a slow page, they leave.

**After:**
> ## Performance
>
> When users hit a slow page, they leave.

**False positive.** A question H2 followed by a short, direct answer is the intended AEO structure, not a warm-up.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style

### P30. Diff-anchored writing

Level: guide · Origin: 2.8 · Types: formation · Script: reading

**Problem:** Documentation or comments written as if narrating a change rather than describing the thing as it is. Unless the document is inherently version-scoped (changelogs, release notes, migration guides), it should read coherently without knowing what changed in the last commit.

**Before:**
> This function was added to replace the previous approach of iterating through all items, which caused O(n²) performance.

**After:**
> This function uses a hash map for O(1) lookups, avoiding the O(n²) cost of naive iteration.

**False positive.** Release notes, changelogs and migration guides are meant to talk about the change.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P31. Manufactured punchlines and staccato drama

Level: blogue · Origin: 2.8 · Types: article, publicite, chronique · Script: staccato

**Problem:** LLMs often make every sentence land like a quotable closer, then stack short declarative fragments to manufacture drama. A single short sentence for emphasis is fine; a run of them starts to sound engineered.

**Before:**
> Then AlphaEvolve arrived. It had no preference for symmetry. No aesthetic prior. No nostalgia for human taste. The old rules were gone.

**After:**
> AlphaEvolve changed the search because it did not favor symmetry or human-looking designs. That made some of the older assumptions less useful.

**False positive.** One short sentence to land a point, or the deliberately choppy rhythm of a spoken script, stays human.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://superdesign.dev/blog/fix-generic-ai-landing-page

### P32. Aphorism formulas

Level: guide · Origin: 2.8 · Types: article, publicite, chronique · Script: reading

**Words to watch:** X is the Y of Z, X becomes a trap, X is not a tool but a mirror, the language of, the currency of, the architecture of

**Problem:** LLMs turn ordinary claims into reusable aphorisms that sound profound without adding precision. Replace the formula with the concrete claim it is gesturing at.

**Before:**
> Symmetry is the language of trust. Efficiency becomes a trap when teams forget the human layer.

**After:**
> Symmetric layouts often feel more predictable to users. Teams can over-optimize workflows and miss how people actually use them.

**False positive.** A metaphor the author already uses in their own work is not a generic formula.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P33. Conversational rhetorical openers

Level: guide · Origin: 2.8 · Types: publicite, chronique · Script: reading

**Phrases to watch:** Honestly?, Look, Here's the thing, The thing is, Let's be honest, Real talk, when used as standalone hooks or fake-candid pauses before an ordinary point.

**Problem:** LLMs open with a fake-candid hook to manufacture intimacy before delivering a routine claim. The tell is the theatrical pause-and-reveal: a one-word question or aside, then the "real" answer. A person being honest usually just says the thing.

**Before:**
> Is it worth the price? Honestly? It depends on how often you'll use it.

**After:**
> Whether it's worth the price depends on how often you'll use it.

**False positive.** "Honestly" or "look" mid-sentence is ordinary casual English; the tell is the standalone theatrical opener.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

## Patterns added in 3.0 (P34 and up)

**Content patterns**

### P37. Corrective disclaimers about sources

Level: guide · Origin: recherche · Types: article, formation · Script: reading

**Cue.** Watch for warnings about how to use a source: "should be treated as X rather than Y", "does not establish", "should not be confused with". Wikipedia dates this sign to mid-2026.

**Fix.** Cut the warning, or replace it with what the source actually says (only facts already in the text), with its limit in one clause.

**Before**
> This survey of 312 firms in Ontario should be treated as indicative rather than conclusive, and it does not establish causation.

**After**
> The survey covered 312 firms in Ontario.

**False positive.** A precise methodological limit that helps the reader (sample size, period covered) stays.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P73. Hollow aspirational formula

Level: blogue · Origin: recherche · Types: page_web, publicite · Script: reading

**Cue.** Watch for "Unlock your full potential", "Imagine a future where" and "what really matters", which read as a slogan instead of a message.

**Fix.** Replace the promise with the concrete result that is already in the text.

**Before**
> Imagine a future where your team unlocks its full potential and stops retyping purchase orders by hand.

**After**
> Your team stops retyping purchase orders by hand.

**False positive.** A measured, dated projection ("in six months, the software sends your reminders") is not hollow.

**Sources.** https://www.eesel.ai/blog/ai-ad-copy-generator; https://www.eesel.ai/fr/blog/generateur-de-texte-publicitaire-ia; https://arxiv.org/html/2512.03373v1

### P74. Implausible quiz distractors

Level: mesure · Origin: recherche · Types: formation · Script: reading

**Cue.** In multiple-choice questions, watch for wrong answers that nobody would pick ("5 minutes", "1 million minutes").

**Fix.** Flag the implausible distractor (audit or "Ce qui sonne encore IA") and suggest, in a note, an option built from a real learner mistake, such as the figure from before the change or a forgotten step. Do not change the question or the answers: stems and correct answers are protected (`type-formation.md`).

**Before**
> How many hours a month does the template save? a) 15 hours b) 5 minutes c) 1 million minutes

**After**
> Question unchanged. Note: b) and c) are implausible; suggestion for the author: a distractor drawn from the time measured before the template.

**False positive.** A very easy warm-up question, placed on purpose at the start of a module, can have obvious distractors.

**Sources.** https://arxiv.org/html/2404.02124; https://elearningindustry.com/why-pedagogy-should-drive-ai-course-generation-not-the-other-way-around

**Language and grammar patterns**

### P34. Vague link

Level: guide · Origin: recherche · Types: article, page_web · Script: reading

**Cue.** Watch for "associated with", "in connection with", "connected to" or "linked to" where the exact relationship is known. Wikipedia lists this among the most common signs as of October 2026.

**Fix.** State the precise relationship (who founded, funded, caused or replaced what), only when the text already gives it; otherwise keep or flag the vague link.

**Before**
> The firm is associated with several automation projects in the region: it built and still maintains three of them.

**After**
> The firm built and still maintains three automation projects in the region.

**False positive.** When the relationship is genuinely uncertain or multiple, "associated with" is honest.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P36. Inverted parallelism "Y rather than X"

Level: guide · Origin: recherche · Types: all · Script: reading

**Cue.** Watch for "Y rather than X", "not simply" and "less like an X and more like a Y", which correct an idea nobody put forward. Graphite reports that Claude Opus 5 uses "less like a _ and more like" about 105 times more often than humans.

**Fix.** Say what the thing is, without the invented contrast. Keep the comparison only if the reader really believes X.

**Before**
> The audit works less like a checklist and more like a conversation: a two-hour interview about how your team handles each request, focusing on habits rather than tools.

**After**
> The audit is a two-hour interview about how your team handles each request.

**False positive.** A real choice between two options the reader is weighing ("rent rather than buy") is correct.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://graphite.io/five-percent/research/ai-tells

### P38. GPT-6 era vocabulary and uniform sentence length

Level: guide · Origin: recherche · Types: article, page_web, publicite · Script: reading

**Cue.** Watch for challenge, clearer, dependable, echoed, foster, leverage, quietly, steady, and for sentences that all fall between 8 and 20 words. Overused words shift with the era and the model: delve dropped in 2025, and Grok overuses causal, empirical and correlate.

**Fix.** Replace the word with the precise term of the trade, and vary sentence length to fit what each idea needs.

**Before**
> Our steady process quietly removes friction: we set up the rule on Monday, and by Friday your team stops copying invoices by hand.

**After**
> We set up the rule on Monday. By Friday, your team stops copying invoices by hand.

**False positive.** The source of this word list is a product review of middling reliability; never flag one of these words alone.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P39. Cluster of measured style words

Level: mesure · Origin: recherche · Types: all · Script: reading

**Cue.** Watch for a pile-up of across, additionally, comprehensive, crucial, enhancing, insights, notably, particularly and within, and of the evaluative adjectives commendable, innovative, meticulous and notable. A text that uses one of these terms is much more likely to use others.

**Fix.** Remove the superfluous linking adverbs, and replace each evaluative adjective with the fact that would justify it.

**Before**
> Additionally, this comprehensive guide offers meticulous insights, notably across quotes, invoices and follow-ups, with the time each one takes.

**After**
> This guide covers quotes, invoices and follow-ups, with the time each one takes.

**False positive.** These words are ordinary one at a time; a single "notably" or "within" signals nothing.

**Sources.** https://arxiv.org/html/2406.07016; https://arxiv.org/html/2403.07183; https://arxiv.org/abs/2509.09596

### P40. Nominalizations

Level: mesure · Origin: recherche · Types: all · Script: reading

**Cue.** Watch for sentences built on action nouns ("the implementation of", "the optimization of") and short on conjugated verbs. Models use 1.5 to 2 times more nominalizations than humans in English, and ChatGPT overuses nouns and underuses verbs and pronouns in French speeches.

**Fix.** Replace the action noun with a conjugated verb and a subject who acts.

**Before**
> The implementation of an automation enables the optimization of the management of our clients' requests.

**After**
> An automation improves how we manage our clients' requests.

**False positive.** Labels, form fields and section titles are normally noun phrases.

**Sources.** https://arxiv.org/html/2410.16107; https://arxiv.org/abs/2411.18382v1; https://www.letemps.ch/articles/chatgpt-a-son-propre-style-mais-pour-combien-de-temps; https://www.slate.fr/tech-internet/intelligence-artificielle-ia-chatbot-chatgpt-texte-litterature-internet-ecriture

### P41. Missing downtoners

Level: mesure · Origin: recherche · Types: article, formation · Script: reading

**Cue.** Watch for a text where no claim is softened by slightly, somewhat or partly, and where subject that-clauses abound. Eleven models, across eight genres, underuse these downtoners even when asked for a human style.

**Fix.** Add a downtoner only when the source already says the fact is partial, without sprinkling them everywhere; never invent the nuance.

**Before**
> The new rule eliminates manual sorting, although about one message in ten still needs a person.

**After**
> The new rule removes most of the manual sorting; about one message in ten still needs a person.

**False positive.** A truly absolute, verified claim needs no softening; do not create doubt to imitate a human.

**Sources.** https://arxiv.org/html/2604.14111

**Structure patterns**

### P35. Template section headings

Level: guide · Origin: recherche · Types: article, page_web · Script: reading

**Cue.** Watch for stock headings such as "Awards and recognition" and the "X and Y" form ("History and Background", "Challenges and Legacy").

**Fix.** Give the heading the real content of its section, one heading for one heading. Do not merge the section: flag it in audit or in "Ce qui sonne encore IA"; never merge sections or convert a table without the author's agreement.

**Before**
> ## Background And Development

**After**
> ## How the tool was built

**False positive.** A service page can keep an "Awards and recognition" section if it lists real, dated awards.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing

### P43. Small tables and empty headings

Level: guide · Origin: recherche · Types: article, page_web, formation · Script: reading

**Cue.** Watch for two- or three-row tables that would be clearer as one sentence, and for headings that contain only other headings and no text. French Wikipedia also notes content laid out in tables and short, incongruous tables.

**Fix.** Flag it in audit or in "Ce qui sonne encore IA"; never merge sections or convert a table into prose without the author's agreement. Flag an empty heading too; never add a sentence under it.

**Before**
> | Option | Price |
> |---|---|
> | Basic | $49 a month |

**After**
> Table kept as is. Bullet in "Ce qui sonne encore IA": one-row table, a sentence would do; convert only with the author's agreement.

**False positive.** A table that compares several options on several criteria is useful, and AEO protects comparison tables.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing/Style; https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://fr.wikipedia.org/wiki/Aide:Identifier_une_source_g%C3%A9n%C3%A9r%C3%A9e_par_IA

### P44. Section-ending summary

Level: guide · Origin: recherche · Types: article, chronique, formation · Script: reading

**Cue.** Watch for paragraphs or sections that end by restating their central idea ("In short, ...", "In summary, ...", "Bottom line, ..."). Wikipedia lists this reflex among the historical indicators.

**Fix.** Delete the summary sentence; the section ends on its last useful fact.

**Before**
> It takes 25 minutes to build a quote by hand and 8 with the template. In short, timing your quotes reveals your savings.

**After**
> It takes 25 minutes to build a quote by hand and 8 with the template.

**False positive.** A training module can end with a recap announced as such; that is a teaching structure.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://mcpservers.org/ko/agent-skills/samber/humaniseur-fr

### P45. Repetitive content

Level: mesure · Origin: recherche · Types: article, page_web · Script: reading

**Cue.** Watch for the same idea restated in other words across several paragraphs or sections, or an outline that repeats the same items elsewhere. Repetitive content is 47% more likely to be generated, and it is one of the only cues readers use correctly.

**Fix.** Keep the best wording where it does its job and cut the repeats.

**Before**
> Automation saves time. Thanks to it, your team gains hours. This time saving changes everything.

**After**
> Automation saves your team hours.

**False positive.** The FAQ of an AEO article repeats the body on purpose so that each answer stands alone; that repetition is defensible.

**Sources.** https://pmc.ncbi.nlm.nih.gov/articles/PMC10089155/; https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative

### P71. Mad-lib headline

Level: blogue · Origin: recherche · Types: page_web, publicite · Script: reading

**Cue.** Watch for interchangeable headlines of the "The AI-powered [X] for modern [Y]" kind.

**Fix.** Write a headline that says what the offer delivers, to whom, and how fast or at what price, using only facts already on the page.

**Before**
> The AI-powered solution for modern SMBs
> The service sorts your email before 8 a.m. Setup takes one week.

**After**
> Your email sorted before 8 a.m., set up in one week
> The service sorts your email before 8 a.m. Setup takes one week.

**False positive.** An established, recognized short brand headline does not need rewriting.

**Sources.** https://superdesign.dev/blog/fix-generic-ai-landing-page

**Style patterns**

### P72. Interchangeable slogan fragments and stacked imperatives

Level: blogue · Origin: recherche · Types: publicite · Script: exclamation

**Cue.** Watch for strings of fragments that are true of any product ("Save time. Work smarter. Scale faster.") and stacked imperatives with exclamation marks ("Book now. Don't wait!"), including the "Get..." variants that ad generators produce.

**Fix.** Replace the string with the reader's measured gain only when that figure is already in the text; otherwise cut the string and keep one imperative. Leave the imperative to the call-to-action button alone; a protected CTA is reported as a Conflit, never replaced.

**Before**
> Ten fewer hours of data entry a month. Save time. Work smarter. Grow faster. Don't wait!

**After**
> Ten fewer hours of data entry a month.

**False positive.** One clear imperative in the copy, or the platform's preset button, is expected in an ad.

**Sources.** https://superdesign.dev/blog/fix-generic-ai-landing-page; https://arxiv.org/html/2601.04925v1; https://developers.facebook.com/docs/marketing-api/creative/generative-ai-features

**Communication patterns**

### P42. Generation leftovers (placeholders, prompts, tracking)

Level: guide · Origin: recherche · Types: all · Script: kill_list/structure

**Cue.** Watch for fill-in templates ("[Your Name]", "[Company name]", "2025-XX-XX"), instructions addressed to the model ("Expand all sections"), "as an AI", and the utm_source=chatgpt.com parameter in links.

**Fix.** Delete the gap or flag it in Changements; never fill it with an invented value. Remove the instruction and clean up the link address.

**Before**
> Thank you for your trust, [Client name]. See you on 2026-XX-XX. Be more detailed and precise.

**After**
> Thank you for your trust.

In Changements: appointment date missing (2026-XX-XX), to be supplied by the author.

**False positive.** A template delivered on purpose as a template, with its fields to fill announced, is not a leftover.

**Sources.** https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing; https://fr.wikipedia.org/wiki/Aide:Identifier_l%27usage_d%27une_IA_g%C3%A9n%C3%A9rative; https://next.ink/article/71730/comment-tenter-didentifier-textes-emanant-dintelligences-artificielles-generatives; https://www.boston.com/news/technology/2025/05/14/professors-using-chatgpt-some-students-arent-happy/

**Filler and hedging**

### P46. Interchangeable "In today's world" opening

Level: blogue · Origin: recherche · Types: article, page_web, publicite, chronique · Script: kill_list/ouvertures

**Cue.** Watch for interchangeable openings about the times: "In today's fast-paced world", "In a world where", "In the ever-evolving digital landscape".

**Fix.** Open with the fact, the figure or the reader's specific situation.

**Before**
> In a world where technology evolves at a breakneck pace, email management has become a crucial challenge for small businesses.

**After**
> Email management has become a challenge for small businesses.

**False positive.** An opening that gives dated context specific to the topic is not interchangeable.

**Sources.** https://www.blogdumoderateur.com/detecter-texte-ia-chatgpt-outils-methodes/; https://www.blogdumoderateur.com/chatgpt-mots-utilises-chatbot/; https://digitad.ca/comment-savoir-texte-genere-par-chatgpt/; https://styleguide.dynatrace.com/docs/best-practices/remove-ai-writing-patterns-from-content; https://textcortex.com/fr/post/%C3%A9diter-contenu-ia; https://seranking.com/fr/blog/bon-prompt-chatgpt/

**Spoken-script patterns**

### P67. Mechanical filler hesitations

Level: blogue · Origin: recherche · Types: chronique · Script: reading

**Cue.** Watch for "um", "you know" or "uh" sown at regular intervals through a written script.

**Fix.** Remove them from the text; the host will hesitate naturally on camera.

**Before**
> So, um... you know, these follow-ups, uh, they take time.

**After**
> These follow-ups take time.

**False positive.** A faithful transcript of a real conversation keeps its hesitations.

**Sources.** https://simonwillison.net/2024/Sep/29/notebooklm-audio-overview/

### P68. Too many clauses for one breath

Level: guide · Origin: recherche · Types: chronique · Script: long_sentence

**Cue.** In text meant to be spoken, watch for sentences with several clauses in "which", "that" or "because", and for present participles or past progressives that stretch the story.

**Fix.** Split into sentences of one idea each, in the present tense, that can be said in one breath.

**Before**
> The company, which employed 22 people and which received requests that nobody sorted because everything landed in the same inbox, was losing hours.

**After**
> The company has 22 employees. Every request lands in the same inbox. The requests stay unsorted. The company loses hours.

**False positive.** A long sentence that sounds natural in the author's voice, checked aloud, can stay.

**Sources.** https://www.npr.org/sections/npr-training/2025/05/31/g-s1-66074/would-you-say-it-that-way-tips-on-writing-for-your-voice; https://pedagogie.ac-toulouse.fr/emi/node/1198

### P69. Relentlessly upbeat tone and praise of the subject

Level: blogue · Origin: recherche · Types: publicite, chronique · Script: reading

**Cue.** Watch for constant enthusiasm and praise of the subject: "absolutely fascinating", "simply remarkable", "one of the most inspiring projects we've ever seen".

**Fix.** Remove the praise and let the measured result already in the text make the impression.

**Before**
> This is absolutely fascinating: this project is simply remarkable! In the first year, the reminders brought in $4,800 of overdue invoices.

**After**
> In the first year, the reminders brought in $4,800 of overdue invoices.

**False positive.** One sincere, specific reaction from the host, once, to a result that earns it stays human.

**Sources.** https://www.scientificamerican.com/podcast/episode/how-tools-like-notebooklm-create-ai-generated-podcasts; https://simonwillison.net/2024/Sep/29/notebooklm-audio-overview/

### P70. Generic call to action

Level: blogue · Origin: recherche · Types: publicite, chronique · Script: reading

**Cue.** Watch for "Subscribe for more content!", "Don't forget to like" or "Follow for more tips!" at the end of a script or a post.

**Fix.** Replace it with an action tied to the topic only when that action is already in the text or in the series' rules; otherwise cut it. A protected CTA is reported as a Conflit, never replaced.

**Before**
> Run the same calculation on your own follow-ups this week. And don't forget to subscribe for more content!

**After**
> Run the same calculation on your own follow-ups this week.

**False positive.** A subscribe reminder required by the series' editorial rules, written in the author's voice, stays.

**Sources.** https://www.opus.pro/blog/chatgpt-prompts-video-scripts-2026

## House rules added in 3.1 (P81 to P83)

Rules of this skill on sentence form, added in 3.1.0. They do not come from research, and their examples are made up. Numbers P75 to P80 are not published.

### P81. Sentence too long on the page

Level: maison · Origin: maison · Types: all · Script: long_sentence

**Cue.** A sentence of more than 30 words (25 in an ad) that stacks a condition, an aside and a consequence. For a spoken script, see P68.

**Fix.** One idea per sentence. Cut at a full stop where the idea changes, and keep the logical link in the next sentence. The result is made of complete sentences, never a string of fragments (P83, P31).

**Before**
> When a supplier invoice arrives by email, the system reads it, pulls out the supplier, the date and the amount, checks it against the purchase order, then prepares the accounting entry, which the accounts manager approves before payment.

**After**
> When a supplier invoice arrives by email, the system reads it and pulls out the supplier, the date and the amount. It checks it against the purchase order and prepares the accounting entry. The accounts manager approves it before payment.

**False positive.** A list the reader must see in one block, an approved contract clause (protected), a quotation.

**Sources.** House rule of the skill, 3.1.0

### P82. Commas that separate nothing

Level: maison · Origin: maison · Types: all · Script: comma_load

**Cue.** A comma placed by habit: before "and", "or" or "then" between two short items, after a short opener, around a word that is not an aside. More than three commas in one sentence means the sentence carries too many asides.

**Fix.** Read the sentence without the comma. If the meaning holds, remove it. If the comma frames an aside, give the aside its own sentence or drop its wrapping. Keep the commas of a plain list, the comma after a long opening clause, and the ones grammar requires.

**Before**
> On page 3, you tick the options you chose, then, once you have read the document, you sign, just below.

**After**
> You tick the options you chose on page 3. You sign just below once you have read the document.

**False positive.** A plain list ("the client, the date, the hours and the parts"), the comma inside a number, an address or a date.

**Sources.** House rule of the skill, 3.1.0

### P83. Sentence with no finite verb

Level: maison · Origin: maison · Types: article, page_web, formation, general · Script: reading (the `verbless` check covers French only)

**Cue.** A noun phrase left as a sentence by a cut, or written for effect: "Ten hours a month, no commitment.", "No surprises.", "Instant results." The pass itself often creates it: a removed tell takes the verb with it.

**Fix.** Give the sentence a subject and a finite verb, or attach the fragment to its neighbour. Invent nothing: the verb says what the text already says.

**Before**
> Ten hours of coaching over one month, with no commitment after that.

**After**
> The package covers ten hours of coaching over one month, with no commitment after that.

**False positive.** Headings, labels, bullets, bold run-in labels, "label: value" lines, greetings and sign-offs, a short FAQ answer followed by the full one, a deliberate fragment in a spoken script or an ad.

**Sources.** House rule of the skill, 3.1.0

## False positives: what NOT to flag

A clean human writer can hit several of the patterns above without any AI involvement. Before rewriting, sanity-check that you are not gutting legitimate prose. The following are *not* reliable indicators on their own:

- **Perfect grammar and consistent style.** Many writers are professionals or have been edited. Polish does not equal AI.
- **Mixed casual and formal registers.** This often signals a person in a technical field, a young writer, or someone with neurodivergent prose habits, not a chatbot.
- **"Bland" or "robotic" prose.** AI prose has *specific* tells. Generic dryness without those tells is just dry writing.
- **Formal or academic vocabulary.** AI overuses *specific* fancy words (see §7), not all fancy words. Don't flatten "ostensibly" or "constituent" just because they sound brainy.
- **Letter-style opening or closing on a comment.** Salutations and sign-offs predate ChatGPT by centuries.
- **Common transition words in isolation.** *Additionally*, *moreover*, *consequently* are AI-coded only when piled up. One *however* is not a tell.
- **Curly quotes alone.** macOS, Word, Google Docs, and most CMSes auto-curl by default. Curly quotes only count when stacked with other tells.
- **Em dashes alone.** Many editors and journalists use them often. Em dashes are evidence only when paired with formulaic sales-y rhythm.
- **One short emphatic sentence.** Humans use clipped sentences to land a point. Flag staccato drama only when several short fragments appear in a row and inflate the tone.
- **"Honestly" or "look" mid-sentence.** These are ordinary in casual writing. The tell is the standalone theatrical opener, not the word itself.
- **Unsourced claims.** Most of the web is unsourced. Lack of citations doesn't prove anything.
- **Correct, complex formatting.** Visual editors and templates produce clean output without any AI.

When in doubt, look for **clusters** of tells, not isolated ones. A single em dash means nothing; em dashes plus rule-of-three plus *vibrant tapestry* plus a "Conclusion" section is a confession.

**Added in 3.0 from the research.** Detectors most often misread these human habits as AI. Never treat them as defects, and never "fix" them by inflating vocabulary, which lowers detector scores without making the text more human for a reader.

- **Simple, predictable vocabulary** (non-native writers, writers aiming for clarity): 61.22% false positives on average on 91 human TOEFL essays. https://arxiv.org/html/2304.02819v3
- **Text polished by an editor or a tool**: scores rise with the amount of editing; false positives ran from 0.0% to 100.0% across detectors on the same manuscripts. https://arxiv.org/html/2608.26710
- **Structured, repetitive or templated text** (recipes, technical prose, lists): up to 33.4% false positives on recipes at a 5% overall threshold. https://arxiv.org/html/2405.07940
- **Short text**: Turnitin admits too many false positives under 300 words; GPTZero, Originality.ai and Pangram lose accuracy under 50. https://www.turnitin.ca/blog/new-research-turnitin-s-ai-detector-shows-no-statistically-significant-bias-against-english-language-learners
- **Machine-translated text**: detector accuracy drops by 20% on text written in another language and translated into English, the case of a French-speaking author who translates his own posts. https://edintegrity.biomedcentral.com/articles/10.1007/s40979-023-00146-z
- **Neutral tone, long or rare words, flawless grammar**: non-experts read them as AI, wrongly; humans make more grammatical errors, and flawed texts were 15% less likely to be generated. https://arxiv.org/html/2501.15654; https://pmc.ncbi.nlm.nih.gov/articles/PMC10089155/

All levels `mesure`. The reader cues that do hold are repetition (P45), absurd or wrong content, and the specific AI vocabulary (P07, P39), not fancy words in general (same two sources).

## Signs of human writing (preserve these)

When you see these, lean toward leaving the prose alone: they are evidence of a real person writing, and over-editing will destroy what makes the piece sound human:

- **Specific, unusual, hard-to-fabricate detail.** A real address. A weird quote. The phrase "the lawyer who used to work upstairs from my dentist." LLMs round off specifics; humans hoard them.
- **Mixed feelings and unresolved tension.** "I think this is mostly good, but it bothers me, and I can't fully explain why." LLMs default to clean takes.
- **Dated, era-bound references.** Slang, memes, or in-jokes that map to a specific year and subculture. Models lag by a year or more.
- **First-person editorial choices the writer can defend.** If the writer can explain *why* they made a particular cut or used a particular word, that's a strong human signal.
- **Variety in sentence length.** Real writing alternates short and long. AI writing tends toward an even, mid-length cadence.
- **Genuine asides, parentheticals, or self-corrections.** "(I keep wanting to say 'almost' here, but it really was certain.)" Models rarely interrupt themselves like this.
- **Edits made before November 30, 2022.** ChatGPT's public launch. Anything older than that is, with very rare exceptions, not AI-written.

**Added in 3.0 from the research** (expert annotators who often write with LLMs, 1 error in 300 articles, `mesure`, https://arxiv.org/html/2501.15654):

- **Many specific factual claims.** The experts' guide finds them in human nonfiction; this backs the first item above.
- **Surprise, humor, originality.** Experts read their absence as AI (23.7% of their explanations).
- **Quotes in someone else's voice.** Generated quotes sound too formal and copy the main text's style; keep a real quote's own wording.
- **An ending that stops on a fact.** The experts' guide notes that AI text ends on a tidy, uplifting summary.

Caution: contractions, first person and casual register prove nothing alone. They fooled an expert in o1-Pro output, and readers wrongly link them to human text. Do not add them to sound human. https://arxiv.org/abs/2206.07271

## Full example

**Before (AI-sounding):**
> Great question! Here is an essay on this topic. I hope this helps!
>
> AI-assisted coding serves as an enduring testament to the transformative potential of large language models, marking a pivotal moment in the evolution of software development. In today's rapidly evolving technological landscape, these groundbreaking tools—nestled at the intersection of research and practice—are reshaping how engineers ideate, iterate, and deliver, underscoring their vital role in modern workflows.
>
> At its core, the value proposition is clear: streamlining processes, enhancing collaboration, and fostering alignment. It's not just about autocomplete; it's about unlocking creativity at scale, ensuring that organizations can remain agile while delivering seamless, intuitive, and powerful experiences to users. The tool serves as a catalyst. The assistant functions as a partner. The system stands as a foundation for innovation.
>
> Industry observers have noted that adoption has accelerated from hobbyist experiments to enterprise-wide rollouts, from solo developers to cross-functional teams. The technology has been featured in The New York Times, Wired, and The Verge. Additionally, the ability to generate documentation, tests, and refactors showcases how AI can contribute to better outcomes, highlighting the intricate interplay between automation and human judgment.
>
> - 💡 **Speed:** Code generation is significantly faster, reducing friction and empowering developers.
> - 🚀 **Quality:** Output quality has been enhanced through improved training, contributing to higher standards.
> - ✅ **Adoption:** Usage continues to grow, reflecting broader industry trends.
>
> While specific details are limited based on available information, it could potentially be argued that these tools might have some positive effect. Despite challenges typical of emerging technologies—including hallucinations, bias, and accountability—the ecosystem continues to thrive. In order to fully realize this potential, teams must align with best practices.
>
> In conclusion, the future looks bright. Exciting times lie ahead as we continue this journey toward excellence. Let me know if you’d like me to expand on any section!

**Draft rewrite:**
> AI coding assistants speed up some tasks. In a 2024 study by Google, developers using Codex completed simple functions 55% faster than a control group, but showed no improvement on debugging or architectural decisions.
>
> The tools are good at boilerplate: config files, test scaffolding, repetitive refactors. They are bad at knowing when they are wrong. I have mass-accepted suggestions that compiled, passed lint, and still did the wrong thing because I stopped paying attention.
>
> Mira, an engineer at a fintech startup I interviewed, said she uses Copilot "like autocomplete for boring code" but reviews every line before committing. Jake, a senior dev at a larger company, disabled it after it kept suggesting patterns from a deprecated internal library.
>
> The productivity claims are hard to verify. GitHub says Copilot users "accept 30% of suggestions," but acceptance is not correctness, and correctness is not value. The 2024 Uplevel study found no statistically significant difference in pull-request throughput between teams with and without AI assistants.
>
> None of this means the tools are useless. It means they are tools. They do not replace judgment, and they do not eliminate the need for tests. If you do not have tests, you cannot tell whether the suggestion is right.

**What makes the below so obviously AI generated?**
- The rhythm is still a bit too tidy (clean contrasts, evenly paced paragraphs).
- The named people and study citations can read like plausible-but-made-up placeholders unless they're real and sourced.
- The closer leans a touch slogan-y ("If you do not have tests...") rather than sounding like a person talking.

**Now make it not obviously AI generated.**
> AI coding assistants can make you faster at the boring parts. Not everything. Definitely not architecture.
>
> They're great at boilerplate: config files, test scaffolding, repetitive refactors. They're also great at sounding right while being wrong. I've accepted suggestions that compiled, passed lint, and still missed the point because I stopped paying attention.
>
> People I talk to tend to land in two camps. Some use it like autocomplete for chores and review every line. Others disable it after it keeps suggesting patterns they don't want. Both feel reasonable.
>
> The productivity metrics are slippery. GitHub can say Copilot users "accept 30% of suggestions," but acceptance isn't correctness, and correctness isn't value. If you don't have tests, you're basically guessing.

**Changes made:** Stripped the chatbot framing, significance inflation, promotional and -ing padding, rule-of-three and synonym cycling, false ranges, copula avoidance, em dashes/emojis/boldface/curly quotes, the formulaic "challenges" section, cutoff and hedging disclaimers, filler and persuasive framing, and the generic upbeat conclusion, then rebuilt the voice with varied rhythm and concrete detail.

## Reference

This skill is based on [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. The patterns documented there come from observations of thousands of instances of AI-generated text on Wikipedia.

Key insight from Wikipedia: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

Patterns P01 to P33, the voice calibration, the false positives, the signs of human writing and the full example come from humanizer 2.8.0 by Siqi Chen (https://github.com/blader/humanizer, MIT License). Several "Before" examples in P01 to P08 quote the Wikipedia page, whose text is available under CC BY-SA 4.0. Version 3.0 adds research compiled in 2026 on the English signs and on what human readers perceive; each pattern cites its own sources.
