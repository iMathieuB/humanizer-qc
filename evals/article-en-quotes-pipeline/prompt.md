---
tags: [humanizer, article, en, pipeline]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Voici la section anglaise de l'article sur le temps passé aux soumissions. Passe-la dans le humanizer.

humanizer-qc mode=pipeline type=article lang=en fichier=avant.md sortie=sortie.md original=avant.md

Input files: avant.md
