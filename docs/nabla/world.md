# Plan du monde étendu

Idées de nouvelles zones et d'ajouts narratifs, à compléter au fil des idées. Chaque zone sera construite comme une étape à part (phase 6), après validation de sa fiche. Les niveaux (Pokémon, dresseurs) sont calés sur les zones qui entourent chaque nouvelle zone (`docs/nabla/levels.md`). Zones déjà construites : `docs/nabla/zones.md`.

## Pendant l'aventure

### Forêt Émeraude (au sud du Mont Mémoria)
- **Fait** : les cartes (lisière, forêt, sanctuaire) et leurs rencontres, accès par la Route 123 (`docs/nabla/zones.md`), et l'histoire (étape 6.2b, `data/scripts/nabla/emerald_forest.inc`). **Reste** : objets dans les culs-de-sac, équipes à confirmer.
- **Idée** : une forêt au sud du Mont Mémoria, vers les routes 122 et 123.
- **Histoire (utilisateur, 2026-10-27)** : au sommet du Mont Mémoria, Timmy rejoint le joueur : la Team Magma est partie dans la Forêt Émeraude chercher un Pokémon qui voyage dans le temps, pour récupérer l'orbe qui lui manque. On retrouve Timmy à l'entrée de la forêt, on affronte des sbires Magma, puis le chef et son adjoint. Celebi apparaît et reconnaît Timmy comme son dresseur ; Timmy soigne l'équipe du joueur et le défie pour tester son nouveau Pokémon. Ensuite, l'histoire reprend où elle en était.
- **Scénario (résumé, à mieux écrire)** : après l'événement du Mont Mémoria, Timmy (Wally) vient voir le joueur : il a entendu parler d'activités suspectes dans la Forêt Émeraude. On y va, on affronte des ennemis ; à la fin, Timmy obtient Celebi, que le joueur a sauvé. Timmy propose alors un combat, obligatoire.
- **Combat** : `TRAINER_NABLA_WALLY_EMERALD_FOREST` (857), déjà prêt (Magnézone, Altaria, Pyronille, Celebi, Gallame ; niveaux 40-43, avant le 7ᵉ badge).
- **Place** : la carte de la région a des cases libres sous la route 123.
- **Rencontres** (choisies par l'utilisateur, à appliquer quand la zone existera) : Grimalin 20 %, Brocélôme 20 %, Mushana 20 %, Florges 20 %, Magirêve 10 %, Bombydou 10 % (`IMPIDIMP`, `PHANTUMP`, `MUSHARNA`, `FLORGES`, `MISMAGIUS`, `CUTIEFLY`). Niveaux : ceux des Routes 122-123.
- **À définir** : les ennemis (Team Aqua/Magma ? autres ?), l'entrée de la forêt, qui dessine.

### Îles accessibles par Plongée
- **Idée** : des zones sous-marines (Plongée) qui mènent à des îles en plus, hors scénario.
- **Place** : la mer de l'est de Hoenn a de la place sur la carte de la région.
- **À définir** : combien d'îles, sur quelles routes marines, leur contenu.

### Pilier Céleste entre la 8e arène et la Ligue (fait)
- **Fait** : événement de Rayquaza et Deoxys (voir `PROGRESS.md`, scripts dans `data/scripts/nabla/rayquaza_event.inc`). Rencontres du Pilier : lot 8.

### West Beach (faite, v2)
- **Fait** : la plage (`docs/nabla/zones.md`) et ses rencontres (avant le 1er badge).
- **À venir** : objets à obtenir (choisis par l'utilisateur) ; peut-être un événement dans l'histoire pour y attirer le joueur, par exemple un dresseur qui propose un échange contre un Pokémon qu'on ne trouve que sur West Beach.

## Après la Ligue

### Îles mirages des légendaires
- **Idée** : des îles mirages pour capturer les légendaires, avec un système proche de la Flûte Éon de ROSA, sans le vol en 3D (étape 7.4 de la roadmap).
- **À définir** : l'objet ou le moyen d'y aller, les conditions de déblocage, la répartition des légendaires.
