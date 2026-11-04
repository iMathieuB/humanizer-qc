---
tags: [humanizer, page_web, fr, pipeline]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Passe humanizer sur le haut de la page du diagnostic d'automatisation.

humanizer mode=pipeline type=page_web lang=fr fichier=avant.md sortie=sortie.md original=avant.md

Input files: avant.md
