# Rencontres des Pokémon sauvages

Généré par `python3 dev_scripts/nabla/list_encounters.py` : ne pas modifier à la main (pour changer des rencontres, écrire les changements dans le chat ou dans une fiche à part).

- Pour chaque espèce : sa part des rencontres de la zone (emplacements additionnés) et ses niveaux. « → en jeu » : les Pokémon sauvages évoluent selon leur niveau (échange, objet, bonheur… à partir du niveau 40).
- Emplacements d'une zone d'herbes : 20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1 % ; Surf et Éclate-Roc : 60, 30, 5, 4, 1 % ; Canne : 70, 30 % ; Super Canne : 60, 20, 20 % ; Méga Canne : 40, 40, 15, 4, 1 %.
- « Nuit » : table utilisée la nuit (sinon la même table jour et nuit).
- Changements depuis Émeraude : espèces ajoutées (+) et retirées (−) dans chaque zone.
- Le Safari a ses propres tables par région : `docs/nabla/safari.md`. Barpau : cases spéciales de la Route 119, niveaux 20-25.

## Avant le 1er badge

### Petalburg City
- **Surf** : Marill 100 % (6-43) → en jeu : Azumarill (selon le niveau)
- **Canne** : Magikarp 70 % (5-11) · Goldeen 30 % (5-11)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (12-37) → en jeu : Seaking (selon le niveau) · Corphish 20 % (12-37) → en jeu : Crawdaunt (selon le niveau)
- **Méga Canne** : Corphish 100 % (24-55) → en jeu : Crawdaunt (selon le niveau)

### Petalburg Woods
- **Herbes** : Venipede 30 % (5-6) · Wurmple 25 % (5-6) · Shroomish 15 % (5-6) · Silcoon 10 % (5) · Cascoon 10 % (5) · Taillow 5 % (5-6) · Slakoth 5 % (5-6) — *changé : +Venipede, −Poochyena*

### Route 101
- **Herbes** : Zigzagoon 45 % (2-3) · Wurmple 45 % (2-3) · Rockruff 5 % (3) · Rockruff-Own-Tempo 5 % (3) — *changé : +Rockruff, +Rockruff-Own-Tempo, −Poochyena*

### Route 101 (nuit)
- **Herbes** : Poochyena 45 % (2-3) · Wurmple 45 % (2-3) · Rockruff 5 % (3) · Rockruff-Own-Tempo 5 % (3) — *changé : +Rockruff, +Rockruff-Own-Tempo, −Zigzagoon*

### Route 102
- **Herbes** : Zigzagoon 30 % (3-4) · Dewpider 30 % (3-4) · Ralts 10 % (3) · Lotad 10 % (4) · Seedot 10 % (3) · Surskit 10 % (3-4) — *changé : +Dewpider, +Surskit, −Poochyena, −Wurmple*
- **Surf** : Marill 99 % (6-43) → en jeu : Azumarill (selon le niveau) · Goldeen 1 % (25-37) → en jeu : Seaking (selon le niveau)
- **Canne** : Magikarp 70 % (5-11) · Goldeen 30 % (5-11)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (12-37) → en jeu : Seaking (selon le niveau) · Corphish 20 % (12-37) → en jeu : Crawdaunt (selon le niveau)
- **Méga Canne** : Corphish 100 % (24-55) → en jeu : Crawdaunt (selon le niveau)

### Route 102 (nuit)
- **Herbes** : Poochyena 30 % (3-4) · Dewpider 30 % (3-4) · Ralts 10 % (3) · Lotad 10 % (4) · Seedot 10 % (3) · Surskit 10 % (3-4) — *changé : +Dewpider, +Surskit, −Wurmple, −Zigzagoon*

### Route 103
- **Herbes** : Pidgey 20 % (2) · Wingull 20 % (3) · Fletchling 20 % (3-4) · Starly 20 % (2-3) · Rookidee 20 % (2-4) — *changé : +Fletchling, +Pidgey, +Rookidee, +Starly, −Poochyena, −Zigzagoon*
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Magikarp 70 % (5-11) · Tentacool 30 % (5-11)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-37) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-37)
- **Méga Canne** : Wailmer 60 % (30-55) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (36-43)

### Route 104
- **Herbes** : Skwovet 40 % (4) · Taillow 20 % (5) · Zigzagoon 20 % (4-5) · Marill 20 % (3-5) — *changé : +Skwovet, +Zigzagoon, −Poochyena, −Wingull, −Wurmple*
- **Surf** : Wingull 95 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Magikarp 100 % (5-11)
- **Super Canne** : Magikarp 100 % (12-37) → en jeu : Gyarados (selon le niveau)
- **Méga Canne** : Magikarp 100 % (24-55) → en jeu : Gyarados

### Route 104 (nuit)
- **Herbes** : Rattata-Alola 40 % (4) · Taillow 20 % (5) · Zigzagoon-Galar 20 % (4-5) · Marill 20 % (3-5) — *changé : +Rattata-Alola, +Zigzagoon-Galar, −Poochyena, −Wingull, −Wurmple*

### Route 116
- **Herbes** : Fidough 28 % (6-9) · Whismur 20 % (6) · Nincada 20 % (6-7) · Taillow 20 % (6-9) · Abra 10 % (7) · Skitty 2 % (7-9) — *changé : +Fidough, −Poochyena*

## 1er → 2e badge

### Dewford Town
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Qwilfish-Hisui 70 % (5-11) · Basculin 30 % (5-11) — *changé : +Basculin, +Qwilfish-Hisui, −Magikarp, −Tentacool*
- **Super Canne** : Qwilfish-Hisui 80 % (12-37) · Basculin 20 % (12-37) — *changé : +Basculin, +Qwilfish-Hisui, −Magikarp, −Tentacool, −Wailmer*
- **Méga Canne** : Qwilfish-Hisui 60 % (24-55) → en jeu : Overqwil (selon le niveau) · Basculin 40 % (36-43) — *changé : +Basculin, +Qwilfish-Hisui, −Wailmer*

### Granite Cave 1F
- **Herbes** : Aron 30 % (7) · Sableye 20 % (8) · Rolycoly 20 % (8-9) · Woobat 15 % (8-11) · Roggenrola 15 % (6-9) — *changé : +Aron, +Roggenrola, +Rolycoly, +Sableye, +Woobat, −Abra, −Geodude, −Makuhita, −Zubat*

### Granite Cave B1F
- **Herbes** : Aron 30 % (9) · Sableye 20 % (11) · Rolycoly 20 % (11-12) · Woobat 15 % (9-11) · Roggenrola 15 % (9-12) — *changé : +Roggenrola, +Rolycoly, +Woobat, −Abra, −Makuhita, −Zubat*

### Granite Cave B2F
- **Herbes** : Aron 30 % (11) · Sableye 20 % (12) · Rolycoly 20 % (12-13) · Woobat 15 % (11) · Roggenrola 15 % (11-13) — *changé : +Roggenrola, +Rolycoly, +Woobat, −Abra, −Zubat*
- **Éclate-Roc** : Geodude 70 % (6-23) · Nosepass 30 % (12-23)

### Granite Cave Stevens Room
- **Herbes** : Aron 30 % (7) · Sableye 20 % (8) · Rolycoly 20 % (8-9) · Woobat 15 % (8-11) · Roggenrola 15 % (6-8) — *changé : +Roggenrola, +Rolycoly, +Sableye, +Woobat, −Abra, −Makuhita, −Zubat*

### Route 106
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Feebas 70 % (5-11) · Magikarp 30 % (5-11) — *changé : +Feebas, −Tentacool*
- **Super Canne** : Feebas 60 % (12-37) · Magikarp 40 % (12-37) → en jeu : Gyarados (selon le niveau) — *changé : +Feebas, −Tentacool, −Wailmer*
- **Méga Canne** : Feebas 60 % (24-55) → en jeu : Milotic (selon le niveau) · Magikarp 40 % (36-43) → en jeu : Gyarados — *changé : +Feebas, +Magikarp, −Wailmer*

### Rusturf Tunnel
- **Herbes** : Axew 20 % (6) · Gible 20 % (7) · Larvitar 20 % (6) · Beldum 20 % (7) · Deino 20 % (5-8) — *changé : +Axew, +Beldum, +Deino, +Gible, +Larvitar, −Whismur*

## 2e → 3e badge

### Route 109
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Dratini 100 % (6-11) — *changé : +Dratini, −Magikarp, −Tentacool*
- **Super Canne** : Dratini 100 % (12-37) → en jeu : Dragonair (selon le niveau) — *changé : +Dratini, −Magikarp, −Tentacool, −Wailmer*
- **Méga Canne** : Dratini 100 % (24-55) → en jeu : Dragonair, Dragonite (selon le niveau) — *changé : +Dratini, −Wailmer*

### Route 110
- **Herbes** : Electrike 20 % (14) · Zorua 20 % (14) · Gulpin 15 % (14-15) · Zorua-Hisui 15 % (15) · Minun 10 % (15) · Plusle 10 % (15) · Oddish 10 % (14-15) — *changé : +Zorua, +Zorua-Hisui, −Poochyena, −Wingull*
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Magikarp 70 % (6-11) · Tentacool 30 % (6-11)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-37) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-37)
- **Méga Canne** : Wailmer 100 % (24-55) → en jeu : Wailord (selon le niveau)

### Route 111
- **Herbes** : Sandshrew 35 % (21-24) → en jeu : Sandslash (selon le niveau) · Trapinch 35 % (21-24) · Baltoy 24 % (21-24) · Cacnea 6 % (23-25)
- **Surf** : Marill 99 % (6-43) → en jeu : Azumarill (selon le niveau) · Goldeen 1 % (25-37) → en jeu : Seaking (selon le niveau)
- **Éclate-Roc** : Nacli 100 % (6-23) — *changé : +Nacli, −Geodude*
- **Canne** : Barboach 100 % (6-11) — *changé : +Barboach, −Goldeen, −Magikarp*
- **Super Canne** : Barboach 100 % (12-37) → en jeu : Whiscash (selon le niveau) — *changé : −Goldeen, −Magikarp*
- **Méga Canne** : Barboach 100 % (24-55) → en jeu : Whiscash (selon le niveau)

### Route 117
- **Herbes** : Cyclizar 30 % (15-16) · Blitzle 20 % (15) · Litleo 20 % (15-16) · Illumise 15 % (15) · Volbeat 15 % (15-16) — *changé : +Blitzle, +Cyclizar, +Litleo, −Marill, −Oddish, −Poochyena, −Seedot*
- **Surf** : Marill 99 % (6-43) → en jeu : Azumarill (selon le niveau) · Goldeen 1 % (25-37) → en jeu : Seaking (selon le niveau)
- **Canne** : Magikarp 70 % (6-11) · Goldeen 30 % (6-11)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (12-37) → en jeu : Seaking (selon le niveau) · Corphish 20 % (12-37) → en jeu : Crawdaunt (selon le niveau)
- **Méga Canne** : Corphish 100 % (24-55) → en jeu : Crawdaunt (selon le niveau)

### Slateport City
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Dhelmise 100 % (6-11) — *changé : +Dhelmise, −Magikarp, −Tentacool*
- **Super Canne** : Dhelmise 100 % (12-37) — *changé : +Dhelmise, −Magikarp, −Tentacool, −Wailmer*
- **Méga Canne** : Dhelmise 100 % (24-55) — *changé : +Dhelmise, −Wailmer*

## 3e → 4e badge

### Fiery Path
- **Herbes** : Numel 30 % (18-19) · Koffing 25 % (18-19) · Torkoal 18 % (16-19) · Machop 15 % (18-19) · Slugma 10 % (18) · Grimer 2 % (16)

### Jagged Pass
- **Herbes** : Numel 55 % (23-26) · Machop 25 % (23-26) · Spoink 20 % (23-26)

### Meteor Falls 1F 1R
- **Herbes** : Zubat 80 % (16-23) → en jeu : Golbat (selon le niveau) · Solrock 20 % (16-21)
- **Surf** : Zubat 90 % (6-43) → en jeu : Crobat, Golbat (selon le niveau) · Solrock 10 % (6-43)
- **Canne** : Magikarp 70 % (6-12) · Goldeen 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (12-37) → en jeu : Seaking (selon le niveau) · Barboach 20 % (12-37) → en jeu : Whiscash (selon le niveau)
- **Méga Canne** : Barboach 100 % (24-55) → en jeu : Whiscash (selon le niveau)

### Meteor Falls 1F 1R (nuit)
- **Herbes** : Zubat 80 % (16-23) → en jeu : Golbat (selon le niveau) · Lunatone 20 % (16-21) — *changé : +Lunatone, −Solrock*
- **Surf** : Zubat 90 % (6-43) → en jeu : Crobat, Golbat (selon le niveau) · Lunatone 10 % (6-43) — *changé : +Lunatone, −Solrock*

### New Mauville Entrance
- **Herbes** : Voltorb 50 % (26-30) → en jeu : Electrode (selon le niveau) · Magnemite 50 % (26-30) → en jeu : Magneton (selon le niveau)

### New Mauville Inside
- **Herbes** : Voltorb 49 % (26-30) → en jeu : Electrode (selon le niveau) · Magnemite 49 % (26-30) → en jeu : Magneton (selon le niveau) · Electrode 1 % (30) · Magneton 1 % (30)

### Route 112
- **Herbes** : Numel 75 % (16-19) · Marill 25 % (16-19) → en jeu : Azumarill (selon le niveau)

### Route 113
- **Herbes** : Spinda 70 % (16-19) · Slugma 25 % (16-19) · Skarmory 5 % (19)

### Route 114
- **Herbes** : Swablu 40 % (18-20) · Lotad 30 % (18-19) → en jeu : Lombre · Lombre 20 % (19-21) · Seviper 5 % (20) · Zangoose 4 % (18) · Nuzleaf 1 % (18) — *changé : +Zangoose*
- **Surf** : Marill 99 % (6-43) → en jeu : Azumarill (selon le niveau) · Goldeen 1 % (25-37) → en jeu : Seaking (selon le niveau)
- **Éclate-Roc** : Geodude 100 % (6-23)
- **Canne** : Magikarp 70 % (6-12) · Goldeen 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (12-37) → en jeu : Seaking (selon le niveau) · Barboach 20 % (12-37) → en jeu : Whiscash (selon le niveau)
- **Méga Canne** : Barboach 100 % (24-55) → en jeu : Whiscash (selon le niveau)

### Route 115
- **Herbes** : Taillow 40 % (27-29) → en jeu : Swellow · Swablu 30 % (27-29) · Swellow 10 % (29) · Jigglypuff 10 % (28-29) · Wingull 10 % (28-30) → en jeu : Pelipper
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-37) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-37)
- **Méga Canne** : Wailmer 100 % (24-55) → en jeu : Wailord (selon le niveau)

## 4e → 5e badge

### Mirage Tower 1F
- **Herbes** : Sandshrew 50 % (23-27) → en jeu : Sandslash · Trapinch 50 % (23-27)

### Mirage Tower 2F
- **Herbes** : Sandshrew 50 % (23-27) → en jeu : Sandslash · Trapinch 50 % (23-27)

### Mirage Tower 3F
- **Herbes** : Sandshrew 50 % (23-27) → en jeu : Sandslash · Trapinch 50 % (23-27)

### Mirage Tower 4F
- **Herbes** : Sandshrew 50 % (23-27) → en jeu : Sandslash · Trapinch 50 % (23-27)

## 5e → 6e badge

### Abandoned Ship Hidden Floor Corridors
- **Surf** : Tentacool 99 % (6-43) → en jeu : Tentacruel (selon le niveau) · Tentacruel 1 % (37-43)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Tentacool 40 % (12-37) → en jeu : Tentacruel (selon le niveau)
- **Méga Canne** : Tentacool 80 % (30-43) → en jeu : Tentacruel · Tentacruel 20 % (24-43)

### Abandoned Ship Rooms B1F
- **Surf** : Tentacool 99 % (6-43) → en jeu : Tentacruel (selon le niveau) · Tentacruel 1 % (37-43)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Tentacool 40 % (12-37) → en jeu : Tentacruel (selon le niveau)
- **Méga Canne** : Tentacool 80 % (30-43) → en jeu : Tentacruel · Tentacruel 20 % (24-43)

### Route 105
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-37) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-37)
- **Méga Canne** : Wailmer 100 % (24-55) → en jeu : Wailord (selon le niveau)

### Route 107
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Arrokuda 70 % (6-12) · Magikarp 30 % (6-12) — *changé : +Arrokuda, −Tentacool*
- **Super Canne** : Arrokuda 60 % (12-37) → en jeu : Barraskewda (selon le niveau) · Magikarp 40 % (12-37) → en jeu : Gyarados (selon le niveau) — *changé : +Arrokuda, −Tentacool, −Wailmer*
- **Méga Canne** : Arrokuda 60 % (24-55) → en jeu : Barraskewda (selon le niveau) · Magikarp 40 % (36-43) → en jeu : Gyarados — *changé : +Arrokuda, +Magikarp, −Wailmer*

### Route 108
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-37) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-37)
- **Méga Canne** : Wailmer 100 % (24-55) → en jeu : Wailord (selon le niveau)

### Route 118
- **Herbes** : Zigzagoon 30 % (30-32) → en jeu : Linoone · Electrike 30 % (30-32) → en jeu : Manectric · Wingull 19 % (31-34) → en jeu : Pelipper · Linoone 10 % (32) · Manectric 10 % (32) · Kecleon 1 % (31)
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Clobbopus 100 % (6-12) — *changé : +Clobbopus, −Magikarp, −Tentacool*
- **Super Canne** : Clobbopus 100 % (12-37) — *changé : +Clobbopus, −Carvanha, −Magikarp, −Tentacool*
- **Méga Canne** : Clobbopus 100 % (24-55) → en jeu : Grapploct (selon le niveau) — *changé : +Clobbopus, −Carvanha, −Sharpedo*

### Route 119
- **Herbes** : Zigzagoon 30 % (31-34) → en jeu : Linoone · Linoone 30 % (31-34) · Oddish 30 % (30-34) → en jeu : Gloom · Tropius 9 % (31-34) · Kecleon 1 % (31)
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-37) → en jeu : Tentacruel (selon le niveau) · Carvanha 20 % (12-37) → en jeu : Sharpedo (selon le niveau)
- **Méga Canne** : Carvanha 100 % (24-55) → en jeu : Sharpedo (selon le niveau)

### Route 120
- **Herbes** : Mightyena 30 % (31-34) · Oddish 25 % (31-34) → en jeu : Gloom · Poochyena 20 % (31) → en jeu : Mightyena · Marill 15 % (31-34) → en jeu : Azumarill · Absol 8 % (31-34) · Kecleon 1 % (31) · Seedot 1 % (31) → en jeu : Nuzleaf
- **Surf** : Marill 99 % (6-43) → en jeu : Azumarill (selon le niveau) · Goldeen 1 % (25-37) → en jeu : Seaking (selon le niveau)
- **Canne** : Magikarp 70 % (6-12) · Goldeen 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (12-37) → en jeu : Seaking (selon le niveau) · Barboach 20 % (12-37) → en jeu : Whiscash (selon le niveau)
- **Méga Canne** : Barboach 100 % (24-55) → en jeu : Whiscash (selon le niveau)

## 6e → 7e badge

### Lilycove City
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-36) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (30-36)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 85 % (30-55) → en jeu : Wailord (selon le niveau) · Staryu 15 % (30-36)

### Magma Hideout 1F
- **Herbes** : Geodude 55 % (33-36) → en jeu : Graveler · Torkoal 30 % (34-36) · Graveler 15 % (36-40) → en jeu : Golem (selon le niveau)

### Magma Hideout 2F 1R
- **Herbes** : Geodude 55 % (33-36) → en jeu : Graveler · Torkoal 30 % (34-36) · Graveler 15 % (36-40) → en jeu : Golem (selon le niveau)

### Magma Hideout 2F 2R
- **Herbes** : Geodude 55 % (33-36) → en jeu : Graveler · Torkoal 30 % (34-36) · Graveler 15 % (36-40) → en jeu : Golem (selon le niveau)

### Magma Hideout 2F 3R
- **Herbes** : Geodude 55 % (33-36) → en jeu : Graveler · Torkoal 30 % (34-36) · Graveler 15 % (36-40) → en jeu : Golem (selon le niveau)

### Magma Hideout 3F 1R
- **Herbes** : Geodude 55 % (33-36) → en jeu : Graveler · Torkoal 30 % (34-36) · Graveler 15 % (36-40) → en jeu : Golem (selon le niveau)

### Magma Hideout 3F 2R
- **Herbes** : Geodude 55 % (33-36) → en jeu : Graveler · Torkoal 30 % (34-36) · Graveler 15 % (36-40) → en jeu : Golem (selon le niveau)

### Magma Hideout 3F 3R
- **Herbes** : Geodude 55 % (33-36) → en jeu : Graveler · Torkoal 30 % (34-36) · Graveler 15 % (36-40) → en jeu : Golem (selon le niveau)

### Magma Hideout 4F
- **Herbes** : Geodude 55 % (33-36) → en jeu : Graveler · Torkoal 30 % (34-36) · Graveler 15 % (36-40) → en jeu : Golem (selon le niveau)

### Mossdeep City
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-36) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (30-36)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 60 % (30-55) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (36-43)

### Mt Pyre 1F
- **Herbes** : Shuppet 100 % (27-35)

### Mt Pyre 2F
- **Herbes** : Shuppet 100 % (27-35)

### Mt Pyre 3F
- **Herbes** : Shuppet 100 % (27-35)

### Mt Pyre 4F
- **Herbes** : Shuppet 90 % (27-35) · Duskull 10 % (30-35)

### Mt Pyre 5F
- **Herbes** : Shuppet 90 % (27-35) · Duskull 10 % (30-35)

### Mt Pyre 6F
- **Herbes** : Shuppet 90 % (27-35) · Duskull 10 % (30-35)

### Mt Pyre Exterior
- **Herbes** : Shuppet 60 % (33-35) · Vulpix 20 % (33-35) · Meditite 10 % (30-35) · Wingull 10 % (32-34) → en jeu : Pelipper — *changé : +Meditite*

### Mt Pyre Summit
- **Herbes** : Shuppet 85 % (29-36) · Duskull 13 % (32-36) · Chimecho 2 % (34)

### Route 121
- **Herbes** : Shuppet 30 % (32-34) · Poochyena 20 % (32) → en jeu : Mightyena · Mightyena 20 % (32-34) · Oddish 15 % (32-34) → en jeu : Gloom · Wingull 9 % (32-34) → en jeu : Pelipper · Gloom 5 % (34) · Kecleon 1 % (30)
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-36) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (30-36)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 100 % (24-55) → en jeu : Wailord (selon le niveau)

### Route 122
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-36) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (30-36)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 60 % (30-55) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (36-43)

### Route 123
- **Herbes** : Shuppet 30 % (32-34) · Poochyena 20 % (32) → en jeu : Mightyena · Mightyena 20 % (32-34) · Oddish 15 % (32-34) → en jeu : Gloom · Wingull 9 % (32-34) → en jeu : Pelipper · Gloom 5 % (34) · Kecleon 1 % (30)
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-36) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (30-36)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 100 % (24-55) → en jeu : Wailord (selon le niveau)

### Route 124
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-36) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (30-36)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 60 % (30-55) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (36-43)

### Route 125
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-36) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (30-36)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 60 % (30-55) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (36-43)

### Route 126
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-36) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (30-36)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 60 % (30-55) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (36-43)

### Route 127
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-36) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (30-36)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 60 % (30-55) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (36-43)

### Route 128
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-36) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (30-36)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Luvdisc 20 % (12-36) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 45 % (36-55) → en jeu : Wailord (selon le niveau) · Luvdisc 40 % (36-43) · Corsola 15 % (36-43)

### Shoal Cave Low Tide Entrance Room
- **Herbes** : Spheal 50 % (32-39) → en jeu : Sealeo · Zubat 45 % (32-39) → en jeu : Golbat · Golbat 5 % (39)
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Zubat 30 % (6-43) → en jeu : Crobat, Golbat (selon le niveau) · Spheal 10 % (30-43) → en jeu : Sealeo (selon le niveau)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 100 % (24-55) → en jeu : Wailord (selon le niveau)

### Shoal Cave Low Tide Ice Room
- **Herbes** : Spheal 45 % (32-39) → en jeu : Sealeo · Zubat 40 % (32-36) → en jeu : Golbat · Snorunt 10 % (32-36) · Golbat 5 % (36-39)

### Shoal Cave Low Tide Inner Room
- **Herbes** : Spheal 50 % (32-39) → en jeu : Sealeo · Zubat 45 % (32-39) → en jeu : Golbat · Golbat 5 % (39)
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Zubat 30 % (6-43) → en jeu : Crobat, Golbat (selon le niveau) · Spheal 10 % (30-43) → en jeu : Sealeo (selon le niveau)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 100 % (24-55) → en jeu : Wailord (selon le niveau)

### Shoal Cave Low Tide Lower Room
- **Herbes** : Spheal 50 % (32-39) → en jeu : Sealeo · Zubat 45 % (32-39) → en jeu : Golbat · Golbat 5 % (39)

### Shoal Cave Low Tide Stairs Room
- **Herbes** : Spheal 50 % (32-39) → en jeu : Sealeo · Zubat 45 % (32-39) → en jeu : Golbat · Golbat 5 % (39)

## 7e → 8e badge

### Cave Of Origin 1F
- **Herbes** : Zubat 60 % (38-44) → en jeu : Crobat, Golbat · Sableye 30 % (38-44) · Golbat 10 % (42-46) → en jeu : Crobat

### Cave Of Origin Entrance
- **Herbes** : Zubat 90 % (36-45) → en jeu : Crobat, Golbat · Golbat 10 % (42-46) → en jeu : Crobat

### Pacifidlog Town
- **Surf** : Tentacool 60 % (6-45) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (13-38) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (32-38)
- **Canne** : Magikarp 70 % (6-13) · Tentacool 30 % (6-13)
- **Super Canne** : Magikarp 60 % (13-38) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (13-38) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (13-38)
- **Méga Canne** : Wailmer 60 % (32-58) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (38-45)

### Route 129
- **Surf** : Tentacool 60 % (6-45) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (13-38) → en jeu : Pelipper (selon le niveau) · Pelipper 4 % (32-38) · Wailord 1 % (32-38)
- **Canne** : Magikarp 70 % (6-13) · Tentacool 30 % (6-13)
- **Super Canne** : Magikarp 60 % (13-38) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (13-38) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (13-38)
- **Méga Canne** : Wailmer 60 % (32-58) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (38-45)

### Route 130
- **Herbes** : Wynaut 100 % (6-64) → en jeu : Wobbuffet (selon le niveau)
- **Surf** : Tentacool 60 % (6-45) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (13-38) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (32-38)
- **Canne** : Magikarp 70 % (6-13) · Tentacool 30 % (6-13)
- **Super Canne** : Magikarp 60 % (13-38) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (13-38) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (13-38)
- **Méga Canne** : Wailmer 60 % (32-58) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (38-45)

### Route 131
- **Surf** : Tentacool 60 % (6-45) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (13-38) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (32-38)
- **Canne** : Magikarp 70 % (6-13) · Tentacool 30 % (6-13)
- **Super Canne** : Magikarp 60 % (13-38) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (13-38) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (13-38)
- **Méga Canne** : Wailmer 60 % (32-58) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (38-45)

### Route 132
- **Surf** : Tentacool 60 % (6-45) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (13-38) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (32-38)
- **Canne** : Magikarp 70 % (6-13) · Tentacool 30 % (6-13)
- **Super Canne** : Magikarp 60 % (13-38) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (13-38) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (13-38)
- **Méga Canne** : Wailmer 45 % (38-58) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (38-45) · Horsea 15 % (32-38) → en jeu : Seadra

### Route 133
- **Surf** : Tentacool 60 % (6-45) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (13-38) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (32-38)
- **Canne** : Magikarp 70 % (6-13) · Tentacool 30 % (6-13)
- **Super Canne** : Magikarp 60 % (13-38) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (13-38) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (13-38)
- **Méga Canne** : Wailmer 45 % (38-58) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (38-45) · Horsea 15 % (32-38) → en jeu : Seadra

### Route 134
- **Surf** : Tentacool 60 % (6-45) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (13-38) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (32-38)
- **Canne** : Magikarp 70 % (6-13) · Tentacool 30 % (6-13)
- **Super Canne** : Magikarp 60 % (13-38) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (13-38) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (13-38)
- **Méga Canne** : Wailmer 45 % (38-58) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (38-45) · Horsea 15 % (32-38) → en jeu : Seadra

### Seafloor Cavern Entrance
- **Surf** : Tentacool 60 % (6-45) → en jeu : Tentacruel (selon le niveau) · Zubat 35 % (6-45) → en jeu : Crobat, Golbat (selon le niveau) · Golbat 5 % (38-45) → en jeu : Crobat (selon le niveau)
- **Canne** : Magikarp 70 % (6-13) · Tentacool 30 % (6-13)
- **Super Canne** : Magikarp 60 % (13-38) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (13-38) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (13-38)
- **Méga Canne** : Wailmer 100 % (26-58) → en jeu : Wailord (selon le niveau)

### Seafloor Cavern Room 1
- **Herbes** : Zubat 90 % (36-45) → en jeu : Crobat, Golbat · Golbat 10 % (42-46) → en jeu : Crobat

### Seafloor Cavern Room 2
- **Herbes** : Zubat 90 % (36-45) → en jeu : Crobat, Golbat · Golbat 10 % (42-46) → en jeu : Crobat

### Seafloor Cavern Room 3
- **Herbes** : Zubat 90 % (36-45) → en jeu : Crobat, Golbat · Golbat 10 % (42-46) → en jeu : Crobat

### Seafloor Cavern Room 4
- **Herbes** : Zubat 90 % (36-45) → en jeu : Crobat, Golbat · Golbat 10 % (42-46) → en jeu : Crobat

### Seafloor Cavern Room 5
- **Herbes** : Zubat 90 % (36-45) → en jeu : Crobat, Golbat · Golbat 10 % (42-46) → en jeu : Crobat

### Seafloor Cavern Room 6
- **Herbes** : Zubat 90 % (36-45) → en jeu : Crobat, Golbat · Golbat 10 % (42-46) → en jeu : Crobat
- **Surf** : Tentacool 60 % (6-45) → en jeu : Tentacruel (selon le niveau) · Zubat 35 % (6-45) → en jeu : Crobat, Golbat (selon le niveau) · Golbat 5 % (38-45) → en jeu : Crobat (selon le niveau)
- **Canne** : Magikarp 70 % (6-13) · Tentacool 30 % (6-13)
- **Super Canne** : Magikarp 60 % (13-38) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (13-38) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (13-38)
- **Méga Canne** : Wailmer 100 % (26-58) → en jeu : Wailord (selon le niveau)

### Seafloor Cavern Room 7
- **Herbes** : Zubat 90 % (36-45) → en jeu : Crobat, Golbat · Golbat 10 % (42-46) → en jeu : Crobat
- **Surf** : Tentacool 60 % (6-45) → en jeu : Tentacruel (selon le niveau) · Zubat 35 % (6-45) → en jeu : Crobat, Golbat (selon le niveau) · Golbat 5 % (38-45) → en jeu : Crobat (selon le niveau)
- **Canne** : Magikarp 70 % (6-13) · Tentacool 30 % (6-13)
- **Super Canne** : Magikarp 60 % (13-38) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (13-38) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (13-38)
- **Méga Canne** : Wailmer 100 % (26-58) → en jeu : Wailord (selon le niveau)

### Seafloor Cavern Room 8
- **Herbes** : Zubat 90 % (36-45) → en jeu : Crobat, Golbat · Golbat 10 % (42-46) → en jeu : Crobat

### Sky Pillar 1F
- **Herbes** : Sableye 30 % (42-44) · Golbat 30 % (44-45) → en jeu : Crobat · Claydol 25 % (46-49) · Banette 15 % (47-49)

### Sky Pillar 3F
- **Herbes** : Sableye 30 % (42-44) · Golbat 30 % (44-45) → en jeu : Crobat · Claydol 25 % (46-49) · Banette 15 % (47-49)

### Sky Pillar 5F
- **Herbes** : Sableye 30 % (42-44) · Golbat 30 % (44-45) → en jeu : Crobat · Claydol 19 % (46-47) · Banette 15 % (47-49) · Altaria 6 % (49-50)

### Sootopolis City
- **Surf** : Magikarp 100 % (6-45) → en jeu : Gyarados (selon le niveau)
- **Canne** : Magikarp 70 % (6-13) · Tentacool 30 % (6-13)
- **Super Canne** : Magikarp 100 % (13-38) → en jeu : Gyarados (selon le niveau)
- **Méga Canne** : Magikarp 80 % (38-45) → en jeu : Gyarados · Gyarados 20 % (6-58)

### Underwater Route 124
- **Surf** : Clamperl 65 % (26-45) → en jeu : Gorebyss, Huntail (selon le niveau) · Chinchou 30 % (26-38) → en jeu : Lanturn (selon le niveau) · Relicanth 5 % (38-45)

### Underwater Route 126
- **Surf** : Clamperl 65 % (26-45) → en jeu : Gorebyss, Huntail (selon le niveau) · Chinchou 30 % (26-38) → en jeu : Lanturn (selon le niveau) · Relicanth 5 % (38-45)

## Route Victoire

### Ever Grande City
- **Surf** : Tentacool 60 % (7-49) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (14-42) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (35-42)
- **Canne** : Magikarp 70 % (7-14) · Tentacool 30 % (7-14)
- **Super Canne** : Magikarp 60 % (14-42) → en jeu : Gyarados (selon le niveau) · Luvdisc 20 % (14-42) · Wailmer 20 % (14-42) → en jeu : Wailord (selon le niveau)
- **Méga Canne** : Wailmer 45 % (42-63) → en jeu : Wailord · Luvdisc 40 % (42-49) · Corsola 15 % (42-49)

### Meteor Falls 1F 2R
- **Herbes** : Golbat 65 % (46-56) → en jeu : Crobat · Solrock 35 % (46-55)
- **Surf** : Golbat 90 % (42-49) → en jeu : Crobat · Solrock 10 % (7-49)
- **Canne** : Magikarp 70 % (7-14) · Goldeen 30 % (7-14)
- **Super Canne** : Magikarp 60 % (14-42) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (14-42) → en jeu : Seaking (selon le niveau) · Barboach 20 % (14-42) → en jeu : Whiscash (selon le niveau)
- **Méga Canne** : Barboach 80 % (35-49) → en jeu : Whiscash · Whiscash 20 % (42-63)

### Meteor Falls 1F 2R (nuit)
- **Herbes** : Golbat 65 % (46-56) → en jeu : Crobat · Lunatone 35 % (46-55) — *changé : +Lunatone, −Solrock*
- **Surf** : Golbat 90 % (42-49) → en jeu : Crobat · Lunatone 10 % (7-49) — *changé : +Lunatone, −Solrock*

### Meteor Falls B1F 1R
- **Herbes** : Golbat 65 % (46-56) → en jeu : Crobat · Solrock 35 % (46-55)
- **Surf** : Golbat 90 % (42-49) → en jeu : Crobat · Solrock 10 % (7-49)
- **Canne** : Magikarp 70 % (7-14) · Goldeen 30 % (7-14)
- **Super Canne** : Magikarp 60 % (14-42) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (14-42) → en jeu : Seaking (selon le niveau) · Barboach 20 % (14-42) → en jeu : Whiscash (selon le niveau)
- **Méga Canne** : Barboach 80 % (35-49) → en jeu : Whiscash · Whiscash 20 % (42-63)

### Meteor Falls B1F 1R (nuit)
- **Herbes** : Golbat 65 % (46-56) → en jeu : Crobat · Lunatone 35 % (46-55) — *changé : +Lunatone, −Solrock*
- **Surf** : Golbat 90 % (42-49) → en jeu : Crobat · Lunatone 10 % (7-49) — *changé : +Lunatone, −Solrock*

### Meteor Falls B1F 2R
- **Herbes** : Golbat 50 % (46-56) → en jeu : Crobat · Bagon 25 % (35-49) → en jeu : Shelgon · Solrock 25 % (49-55)
- **Surf** : Golbat 90 % (42-49) → en jeu : Crobat · Solrock 10 % (7-49)
- **Canne** : Magikarp 70 % (7-14) · Goldeen 30 % (7-14)
- **Super Canne** : Magikarp 60 % (14-42) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (14-42) → en jeu : Seaking (selon le niveau) · Barboach 20 % (14-42) → en jeu : Whiscash (selon le niveau)
- **Méga Canne** : Barboach 80 % (35-49) → en jeu : Whiscash · Whiscash 20 % (42-63)

### Meteor Falls B1F 2R (nuit)
- **Herbes** : Golbat 50 % (46-56) → en jeu : Crobat · Bagon 25 % (35-49) → en jeu : Shelgon · Lunatone 25 % (49-55) — *changé : +Lunatone, −Solrock*
- **Surf** : Golbat 90 % (42-49) → en jeu : Crobat · Lunatone 10 % (7-49) — *changé : +Lunatone, −Solrock*

### Victory Road 1F
- **Herbes** : Golbat 25 % (53-56) → en jeu : Crobat · Hariyama 25 % (53-56) · Lairon 10 % (56) → en jeu : Aggron · Loudred 10 % (56) → en jeu : Exploud · Zubat 10 % (50) → en jeu : Crobat · Makuhita 10 % (50) → en jeu : Hariyama · Aron 5 % (50) → en jeu : Aggron · Whismur 5 % (50) → en jeu : Exploud

### Victory Road B1F
- **Herbes** : Golbat 35 % (53-59) → en jeu : Crobat · Hariyama 35 % (53-59) · Lairon 25 % (56-59) → en jeu : Aggron · Mawile 5 % (53)
- **Éclate-Roc** : Graveler 70 % (42-56) → en jeu : Golem · Geodude 30 % (42-56) → en jeu : Golem

### Victory Road B2F
- **Herbes** : Golbat 35 % (56-62) → en jeu : Crobat · Sableye 35 % (56-62) · Lairon 25 % (56-62) → en jeu : Aggron · Mawile 5 % (59-62)
- **Surf** : Golbat 100 % (35-56) → en jeu : Crobat (selon le niveau)
- **Canne** : Magikarp 70 % (7-14) · Goldeen 30 % (7-14)
- **Super Canne** : Magikarp 60 % (14-42) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (14-42) → en jeu : Seaking (selon le niveau) · Barboach 20 % (14-42) → en jeu : Whiscash (selon le niveau)
- **Méga Canne** : Barboach 80 % (35-49) → en jeu : Whiscash · Whiscash 20 % (42-63)

## Hors aventure (après la Ligue, zones Nabla)

### Altering Cave (table 1)
- **Herbes** : Zubat 100 % (6-16)

### Altering Cave (table 2)
- **Herbes** : Mareep 100 % (3-13)

### Altering Cave (table 3)
- **Herbes** : Pineco 100 % (19-29)

### Altering Cave (table 4)
- **Herbes** : Houndour 100 % (12-22)

### Altering Cave (table 5)
- **Herbes** : Teddiursa 100 % (6-16)

### Altering Cave (table 6)
- **Herbes** : Aipom 100 % (18-28)

### Altering Cave (table 7)
- **Herbes** : Shuckle 100 % (18-28)

### Altering Cave (table 8)
- **Herbes** : Stantler 100 % (18-28)

### Altering Cave (table 9)
- **Herbes** : Smeargle 100 % (18-28)

### Artisan Cave 1F
- **Herbes** : Smeargle 100 % (40-50)

### Artisan Cave B1F
- **Herbes** : Smeargle 100 % (40-50)

### Desert Underpass
- **Herbes** : Ditto 50 % (38-45) · Whismur 34 % (35-38) → en jeu : Loudred · Loudred 16 % (38-44) → en jeu : Exploud (selon le niveau)

### Meteor Falls Stevens Cave
- **Herbes** : Golbat 65 % (33-40) → en jeu : Crobat (selon le niveau) · Solrock 35 % (33-39)

### Meteor Falls Stevens Cave (nuit)
- **Herbes** : Golbat 65 % (33-40) → en jeu : Crobat (selon le niveau) · Lunatone 35 % (33-39) — *changé : +Lunatone, −Solrock*

### Nabla West Beach
- *Table ajoutée par Nabla.*
- **Herbes** : Wiglett 20 % (5-7) · Dwebble 20 % (5-7) · Pyukumuku 10 % (5-8) · Sandygast 10 % (5-8) · Krabby 10 % (5-8) · Mantyke 10 % (5-8) · Clauncher 10 % (6-8) · Staryu 10 % (6-8)
- **Surf** : Mareanie 60 % (6-43) → en jeu : Toxapex (selon le niveau) · Tentacool 40 % (12-37) → en jeu : Tentacruel (selon le niveau)
- **Canne** : Mareanie 70 % (5-11) · Tentacool 30 % (5-11)
- **Super Canne** : Mareanie 60 % (12-37) · Tentacool 40 % (12-37) → en jeu : Tentacruel (selon le niveau)
- **Méga Canne** : Mareanie 60 % (30-55) → en jeu : Toxapex (selon le niveau) · Tentacool 40 % (36-43) → en jeu : Tentacruel
