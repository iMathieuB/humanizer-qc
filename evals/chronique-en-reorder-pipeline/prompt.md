---
tags: [humanizer, chronique, en, pipeline]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Script anglais du reel sur les alertes de réapprovisionnement, à passer avant l'enregistrement.

humanizer-qc mode=pipeline type=chronique lang=en fichier=avant.md sortie=sortie.md original=avant.md

Input files: avant.md
