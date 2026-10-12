# PROGRESS — Pokémon Nabla

## État actuel

- **Base** : pokeemerald-expansion **1.17.2** (master, commit non tagué, `git describe` = `expansion/1.17.1-11-g87cc74b5ec`).
- **Build** : ✅ `make` passe sur macOS (devkitARM). ROM utilisée à 79,7 % (26,7 Mo / 32 Mo), EWRAM 86 %, IWRAM 87 %.
- **Jeu** : expansion par défaut, sans l'intro RHH.
- **Étape en cours** : 0.2 terminée (patch BPS, README, crédits, intro retirée), en attente de ton test. Prochaine : 1.1 — combat moderne.

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

### Session 2 — 2026-10-12
- Étape 0.2 :
  - ROM de base vérifiée (SHA1 Émeraude US correct), rangée dans `../rom/`.
  - Flips compilé depuis les sources officielles (Alcaro/Flips) dans `../tools/flips`.
  - `make_bps.sh` : build release → patch `build/pokemon_nabla.bps` (16,8 Mo) → ré-application et comparaison SHA1 ✅.
  - `README.md` remplacé : présentation de Nabla, comment jouer, crédits RHH (pokeemerald-expansion 1.17.2) + pret.
  - `EXPANSION_INTRO` = FALSE ; code de l'intro absent de la ROM (vérifié dans les symboles).
  - **À tester par toi** : appliquer le patch sur la ROM propre, le jeu démarre sur l'écran de copyright puis l'intro Game Freak, sans la scène RHH.

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
| 2026-10-12 | **Nouvelles zones** : quelques zones facultatives pendant l'aventure + des zones nouvelles en post-game. Maps dessinées par l'utilisateur (Porymap) **et** par Claude. |
| 2026-10-12 | En-tête de ROM inchangé (titre `POKEMON EMER`, code `BPEE`) : les émulateurs s'en servent pour détecter la sauvegarde et l'horloge. |
| 2026-10-12 | README public en anglais (le jeu est en anglais d'abord). |
| 2026-10-12 | **Méga-Bracelet** donné comme dans ROSA : événement Latios après le **5ᵉ badge**, Île du Sud, combat en duo avec Steven. |

## Questions ouvertes

1. **Level caps** : valeurs à fournir avant l'étape 2.2 (sinon valeurs provisoires).
