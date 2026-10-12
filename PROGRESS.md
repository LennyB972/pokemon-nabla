# PROGRESS — Pokémon Nabla

## État actuel

- **Base** : pokeemerald-expansion **1.17.2** (master, commit non tagué, `git describe` = `expansion/1.17.1-11-g87cc74b5ec`).
- **Build** : ✅ `make` passe sur macOS (devkitARM). ROM utilisée à 79,7 % (26,7 Mo / 32 Mo), EWRAM 86 %, IWRAM 87 %.
- **Jeu** : aucune modification pour l'instant (expansion par défaut).
- **Étape en cours** : 0.1 terminée (documents). Prochaine : 0.2 — distribution et crédits (attend la ROM de base).

## Journal

### Session 1 — 2026-10-12
- Lecture de VISION.md, build vérifié, exploration des configs `include/config/`.
- Créé : `CLAUDE.md` (règles permanentes), `ROADMAP.md` (correspondance VISION ↔ expansion + phases), `PROGRESS.md`.
- Constats :
  - Déjà actifs par défaut : mécaniques Gen 9, Dex Gen 1-9 complet, Méga activée (mais Anneau Méga jamais donné), course en intérieur, poison sans dégâts hors combat, jour/nuit (DNS), dernière Ball utilisée, option texte « Instant ».
  - Réglables en config : Gelure (`B_USE_FROSTBITE`), doubles sauvages, level caps, CT réutilisables, Multi Exp moderne, IV/EV, followers, name box.
  - Évolutions par échange : alternatives par objet déjà présentes (Fil de Liaison…), sauf Carabing/Escargaume.
  - À coder : Nuzlocke, Choix à l'aveugle, CS sans slot, menu de début de partie.
  - Ressources libres : 381 flags `FLAG_UNUSED_*`, 29 vars `VAR_UNUSED_*`.
- Note technique : le shell de Claude doit exporter `DEVKITPRO`/`DEVKITARM` avant `make` (voir CLAUDE.md).
- Retours sur la roadmap intégrés : Nuzlocke retiré, 2 difficultés, phase 6 « Monde étendu » (nouvelles zones + ajouts narratifs) créée, post-game devient la phase 7, événement Latios/Méga-Bracelet façon ROSA en 3.4, crédits RHH en 0.2.

## Décisions prises

| Date | Décision |
|---|---|
| 2026-10-12 | Docs de projet en français, code et commits en anglais. |
| 2026-10-12 | Nouveaux textes regroupés dans `data/text/nabla/` (scripts) et un fichier dédié (C). |
| 2026-10-12 | **Nuzlocke retiré** du projet. |
| 2026-10-12 | **2 difficultés** : Normal / Difficile, choisies en début de partie. |
| 2026-10-12 | **Level caps activables** en début de partie ; valeurs définies à la main par l'utilisateur. |
| 2026-10-12 | **CS → objets clés** obtenus aux mêmes moments de l'histoire, sans Pokémon qui connaît l'attaque. |
| 2026-10-12 | **Vraie horloge (RTC)** pour le jour/nuit. |
| 2026-10-12 | **Intro RHH retirée** ; crédit RHH dans le README, les notes de version et le générique de fin. |
| 2026-10-12 | **Méga-Bracelet** donné comme dans ROSA : événement Latios après le 6ᵉ badge, Île du Sud, combat en duo avec Steven. |

## Questions ouvertes

1. **ROM de base** : une ROM Émeraude US propre (SHA1 `f3ae088181bf583e55daf962a92bb46f4f1d07b7`), à ranger hors du repo. Bloque l'étape 0.2.
2. **Nouvelles zones** : uniquement en post-game, ou aussi des zones facultatives pendant l'aventure ?
3. **Dessin des maps** : l'utilisateur dessine dans Porymap (recommandé), ou Claude génère les maps en recombinant des maps existantes ?
4. **Level caps** : valeurs à fournir avant l'étape 2.2 (sinon valeurs provisoires).
