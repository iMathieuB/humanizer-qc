---
tags: [humanizer, article, fr, pipeline]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Passe la FAQ et la fin de l'article dans le humanizer avant la publication sur le blogue.

humanizer mode=pipeline type=article lang=fr fichier=avant.md sortie=sortie.md original=avant.md

Input files: avant.md
