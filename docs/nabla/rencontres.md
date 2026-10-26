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
- **Herbes** : Yungoos 40 % (4) · Taillow 20 % (5) · Zigzagoon 20 % (4-5) · Marill 20 % (3-5) — *changé : +Yungoos, +Zigzagoon, −Poochyena, −Wingull, −Wurmple*
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
- **Herbes** : Trapinch 30 % (23-24) · Sandile 20 % (23) · Hippopotas 15 % (21-24) · Sandshrew 15 % (21) · Silicobra 10 % (24) · Bramblin 5 % (23-25) · Cacnea 5 % (23-25) — *changé : +Bramblin, +Hippopotas, +Sandile, +Silicobra, −Baltoy*
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
- **Herbes** : Numel 30 % (18-19) · Charcadet 20 % (18) · Larvesta 20 % (18) · Growlithe-Hisui 15 % (18-19) · Slugma 10 % (16-19) · Torkoal 5 % (16-19) — *changé : +Charcadet, +Growlithe-Hisui, +Larvesta, −Grimer, −Koffing, −Machop*

### Jagged Pass
- **Herbes** : Ponyta 20 % (25) · Carkol 20 % (25) · Vullaby 15 % (25) · Magmar 15 % (23-26) · Kangaskhan 10 % (23) · Spinda 10 % (23) · Marowak-Alola 10 % (26) — *changé : +Carkol, +Kangaskhan, +Magmar, +Marowak-Alola, +Ponyta, +Spinda, +Vullaby, −Machop, −Numel, −Spoink*

### Meteor Falls 1F 1R
- **Herbes** : Minior 30 % (19-21) · Elgyem 20 % (20) · Bagon 20 % (16-18) · Glimmet 20 % (16-21) · Solrock 10 % (22-23) — *changé : +Bagon, +Elgyem, +Glimmet, +Minior, −Zubat*
- **Surf** : Tatsugiri-Curly 60 % (6-43) · Tatsugiri-Droopy 30 % (37-43) · Tatsugiri-Stretchy 10 % (6-43) — *changé : +Tatsugiri-Curly, +Tatsugiri-Droopy, +Tatsugiri-Stretchy, −Solrock, −Zubat*
- **Canne** : Magikarp 70 % (6-12) · Goldeen 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (12-37) → en jeu : Seaking (selon le niveau) · Barboach 20 % (12-37) → en jeu : Whiscash (selon le niveau)
- **Méga Canne** : Barboach 100 % (24-55) → en jeu : Whiscash (selon le niveau)

### Meteor Falls 1F 1R (nuit)
- **Herbes** : Minior 30 % (19-21) · Elgyem 20 % (20) · Bagon 20 % (16-18) · Glimmet 20 % (16-21) · Lunatone 10 % (22-23) — *changé : +Bagon, +Elgyem, +Glimmet, +Lunatone, +Minior, −Solrock, −Zubat*
- **Surf** : Tatsugiri-Curly 60 % (6-43) · Tatsugiri-Droopy 30 % (37-43) · Tatsugiri-Stretchy 10 % (6-43) — *changé : +Tatsugiri-Curly, +Tatsugiri-Droopy, +Tatsugiri-Stretchy, −Solrock, −Zubat*

### Route 112
- **Herbes** : Eevee 30 % (18) · Numel 25 % (18-19) · Pawmi 15 % (16-19) → en jeu : Pawmo (selon le niveau) · Bouffalant 15 % (16-19) · Mudbray 15 % (16-19) — *changé : +Bouffalant, +Eevee, +Mudbray, +Pawmi, −Marill*

### Route 113
- **Herbes** : Capsakid 30 % (18) · Houndour 20 % (18) · Darumaka 20 % (16) · Sunflora 15 % (16-19) · Skarmory 15 % (19) — *changé : +Capsakid, +Darumaka, +Houndour, +Sunflora, −Slugma, −Spinda*

### Route 114
- **Herbes** : Swablu 30 % (19-20) · Gligar 20 % (19) · Zangoose 15 % (18-19) · Bombirdier 15 % (18-21) · Jangmo-O 10 % (19) · Mankey 10 % (18-20) — *changé : +Bombirdier, +Gligar, +Jangmo-O, +Mankey, +Zangoose, −Lombre, −Lotad, −Nuzleaf, −Seviper*
- **Surf** : Marill 99 % (6-43) → en jeu : Azumarill (selon le niveau) · Goldeen 1 % (25-37) → en jeu : Seaking (selon le niveau)
- **Éclate-Roc** : Geodude 100 % (6-23)
- **Canne** : Magikarp 70 % (6-12) · Goldeen 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (12-37) → en jeu : Seaking (selon le niveau) · Barboach 20 % (12-37) → en jeu : Whiscash (selon le niveau)
- **Méga Canne** : Barboach 100 % (24-55) → en jeu : Whiscash (selon le niveau)

### Route 114 (nuit)
- **Herbes** : Swablu 30 % (19-20) · Gligar 20 % (19) · Seviper 15 % (18-19) · Bombirdier 15 % (18-21) · Jangmo-O 10 % (19) · Mankey 10 % (18-20) — *changé : +Bombirdier, +Gligar, +Jangmo-O, +Mankey, −Lombre, −Lotad, −Nuzleaf*

### Route 115
- **Herbes** : Cottonee 30 % (27-29) · Shinx 20 % (27) → en jeu : Luxio · Clauncher 15 % (28) · Inkay 15 % (29) · Slowpoke 10 % (29) · Greavard 10 % (28-30) → en jeu : Houndstone (selon le niveau) — *changé : +Clauncher, +Cottonee, +Greavard, +Inkay, +Shinx, +Slowpoke, −Jigglypuff, −Swablu, −Swellow, −Taillow, −Wingull*
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-37) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-37)
- **Méga Canne** : Wailmer 100 % (24-55) → en jeu : Wailord (selon le niveau)

## 4e → 5e badge

### Mirage Tower 1F
- **Herbes** : Yamask 20 % (24) · Baltoy 20 % (24) · Bronzor 20 % (23) · Golett 20 % (23) · Honedge 20 % (25-27) — *changé : +Baltoy, +Bronzor, +Golett, +Honedge, +Yamask, −Sandshrew, −Trapinch*

### Mirage Tower 2F
- **Herbes** : Yamask 20 % (24) · Baltoy 20 % (24) · Bronzor 20 % (23) · Golett 20 % (23) · Honedge 20 % (25-27) — *changé : +Baltoy, +Bronzor, +Golett, +Honedge, +Yamask, −Sandshrew, −Trapinch*

### Mirage Tower 3F
- **Herbes** : Yamask 20 % (24) · Baltoy 20 % (24) · Bronzor 20 % (23) · Golett 20 % (23) · Honedge 20 % (25-27) — *changé : +Baltoy, +Bronzor, +Golett, +Honedge, +Yamask, −Sandshrew, −Trapinch*

### Mirage Tower 4F
- **Herbes** : Yamask 20 % (24) · Baltoy 20 % (24) · Bronzor 20 % (23) · Golett 20 % (23) · Honedge 20 % (25-27) — *changé : +Baltoy, +Bronzor, +Golett, +Honedge, +Yamask, −Sandshrew, −Trapinch*

## 5e → 6e badge

### Abandoned Ship Hidden Floor Corridors
- **Surf** : Dhelmise 60 % (6-43) · Gholdengo 40 % (6-43) — *changé : +Dhelmise, +Gholdengo, −Tentacool, −Tentacruel*
- **Canne** : Corsola-Galar 70 % (6-12) · Dhelmise 30 % (6-12) — *changé : +Corsola-Galar, +Dhelmise, −Magikarp, −Tentacool*
- **Super Canne** : Corsola-Galar 80 % (12-37) · Dhelmise 20 % (12-37) — *changé : +Corsola-Galar, +Dhelmise, −Magikarp, −Tentacool*
- **Méga Canne** : Corsola-Galar 60 % (24-43) → en jeu : Cursola (selon le niveau) · Dhelmise 40 % (36-43) — *changé : +Corsola-Galar, +Dhelmise, −Tentacool, −Tentacruel*

### Abandoned Ship Rooms B1F
- **Surf** : Dhelmise 60 % (6-43) · Gholdengo 40 % (6-43) — *changé : +Dhelmise, +Gholdengo, −Tentacool, −Tentacruel*
- **Canne** : Corsola-Galar 70 % (6-12) · Dhelmise 30 % (6-12) — *changé : +Corsola-Galar, +Dhelmise, −Magikarp, −Tentacool*
- **Super Canne** : Corsola-Galar 80 % (12-37) · Dhelmise 20 % (12-37) — *changé : +Corsola-Galar, +Dhelmise, −Magikarp, −Tentacool*
- **Méga Canne** : Corsola-Galar 60 % (24-43) → en jeu : Cursola (selon le niveau) · Dhelmise 40 % (36-43) — *changé : +Corsola-Galar, +Dhelmise, −Tentacool, −Tentacruel*

### New Mauville Entrance
- **Herbes** : Magneton 25 % (30-32) · Electivire 25 % (30-32) · Tadbulb 15 % (27-29) · Rotom 15 % (27-29) · Toxtricity-Amped 10 % (31) · Toxtricity-Low-Key 10 % (31) — *changé : +Electivire, +Magneton, +Rotom, +Tadbulb, +Toxtricity-Amped, +Toxtricity-Low-Key, −Magnemite, −Voltorb*

### New Mauville Inside
- **Herbes** : Magneton 25 % (30-32) · Electivire 25 % (30-32) · Tadbulb 15 % (27-32) · Rotom 15 % (27-32) · Toxtricity-Amped 10 % (31) · Toxtricity-Low-Key 10 % (31) — *changé : +Electivire, +Rotom, +Tadbulb, +Toxtricity-Amped, +Toxtricity-Low-Key, −Electrode, −Magnemite, −Voltorb*

### Route 105
- **Surf** : Seadra 60 % (6-43) → en jeu : Kingdra (selon le niveau) · Lanturn 40 % (12-37) — *changé : +Lanturn, +Seadra, −Pelipper, −Tentacool, −Wingull*
- **Canne** : Seadra 70 % (6-12) · Lanturn 30 % (6-12) — *changé : +Lanturn, +Seadra, −Magikarp, −Tentacool*
- **Super Canne** : Seadra 60 % (12-37) · Lanturn 40 % (12-37) — *changé : +Lanturn, +Seadra, −Magikarp, −Tentacool, −Wailmer*
- **Méga Canne** : Seadra 60 % (24-55) → en jeu : Kingdra (selon le niveau) · Lanturn 40 % (36-43) — *changé : +Lanturn, +Seadra, −Wailmer*

### Route 107
- **Surf** : Frillish 60 % (6-43) → en jeu : Jellicent (selon le niveau) · Octillery 40 % (12-37) — *changé : +Frillish, +Octillery, −Pelipper, −Tentacool, −Wingull*
- **Canne** : Frillish 70 % (6-12) · Octillery 30 % (6-12) — *changé : +Frillish, +Octillery, −Magikarp, −Tentacool*
- **Super Canne** : Frillish 60 % (12-37) · Octillery 40 % (12-37) — *changé : +Frillish, +Octillery, −Magikarp, −Tentacool, −Wailmer*
- **Méga Canne** : Frillish 60 % (24-55) → en jeu : Jellicent (selon le niveau) · Octillery 40 % (36-43) — *changé : +Frillish, +Octillery, −Wailmer*

### Route 108
- **Surf** : Alomomola 60 % (6-43) · Dondozo 40 % (12-37) — *changé : +Alomomola, +Dondozo, −Pelipper, −Tentacool, −Wingull*
- **Canne** : Alomomola 70 % (6-12) · Dondozo 30 % (6-12) — *changé : +Alomomola, +Dondozo, −Magikarp, −Tentacool*
- **Super Canne** : Alomomola 60 % (12-37) · Dondozo 40 % (12-37) — *changé : +Alomomola, +Dondozo, −Magikarp, −Tentacool, −Wailmer*
- **Méga Canne** : Alomomola 60 % (24-55) · Dondozo 40 % (36-43) — *changé : +Alomomola, +Dondozo, −Wailmer*

### Route 118
- **Herbes** : Fomantis 20 % (30) · Yanma 20 % (30) · Spoink 15 % (31-32) → en jeu : Grumpig (selon le niveau) · Kecleon 15 % (31-32) · Scyther 15 % (32-34) · Nymble 15 % (31-32) → en jeu : Lokix — *changé : +Fomantis, +Nymble, +Scyther, +Spoink, +Yanma, −Electrike, −Linoone, −Manectric, −Wingull, −Zigzagoon*
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Clobbopus 100 % (6-12) — *changé : +Clobbopus, −Magikarp, −Tentacool*
- **Super Canne** : Clobbopus 100 % (12-37) — *changé : +Clobbopus, −Carvanha, −Magikarp, −Tentacool*
- **Méga Canne** : Clobbopus 100 % (24-55) → en jeu : Grapploct (selon le niveau) — *changé : +Clobbopus, −Carvanha, −Sharpedo*

### Route 119
- **Herbes** : Liepard 30 % (31-34) · Tropius 25 % (31-34) · Arboliva 20 % (31-34) · Obstagoon 15 % (30-32) · Ariados 10 % (31-34) — *changé : +Arboliva, +Ariados, +Liepard, +Obstagoon, −Kecleon, −Linoone, −Oddish, −Zigzagoon*
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-37) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (31-37)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-37) → en jeu : Tentacruel (selon le niveau) · Carvanha 20 % (12-37) → en jeu : Sharpedo (selon le niveau)
- **Méga Canne** : Carvanha 100 % (24-55) → en jeu : Sharpedo (selon le niveau)

### Route 120
- **Herbes** : Absol 30 % (31-34) · Shiftry 20 % (31) · Ludicolo 20 % (31) · Azumarill 15 % (32-34) · Thievul 15 % (31-34) — *changé : +Azumarill, +Ludicolo, +Shiftry, +Thievul, −Kecleon, −Marill, −Mightyena, −Oddish, −Poochyena, −Seedot*
- **Surf** : Marill 99 % (6-43) → en jeu : Azumarill (selon le niveau) · Goldeen 1 % (25-37) → en jeu : Seaking (selon le niveau)
- **Canne** : Magikarp 70 % (6-12) · Goldeen 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-37) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (12-37) → en jeu : Seaking (selon le niveau) · Barboach 20 % (12-37) → en jeu : Whiscash (selon le niveau)
- **Méga Canne** : Barboach 100 % (24-55) → en jeu : Whiscash (selon le niveau)

### Scorched Slab
- *Table ajoutée par Nabla.*
- **Herbes** : Tinkatink 25 % (31-34) → en jeu : Tinkatuff · Mimikyu 20 % (31) · Goomy 20 % (31-34) · Rhyhorn 20 % (31-32) · Paras 15 % (31-34) → en jeu : Parasect

## 6e → 7e badge

### Lilycove City
- **Surf** : Wailord 100 % (6-43) — *changé : +Wailord, −Pelipper, −Tentacool, −Wingull*
- **Canne** : Wailord 100 % (6-12) — *changé : +Wailord, −Magikarp, −Tentacool*
- **Super Canne** : Wailord 100 % (12-36) — *changé : +Wailord, −Magikarp, −Tentacool, −Wailmer*
- **Méga Canne** : Wailord 100 % (30-55) — *changé : +Wailord, −Staryu, −Wailmer*

### Magma Hideout 1F
- **Herbes** : Magmortar 30 % (33-34) · Armarouge 25 % (34-36) · Ceruledge 25 % (35-36) · Salandit 20 % (36-40) → en jeu : Salazzle (selon le niveau) — *changé : +Armarouge, +Ceruledge, +Magmortar, +Salandit, −Geodude, −Graveler, −Torkoal*

### Magma Hideout 2F 1R
- **Herbes** : Magmortar 30 % (33-34) · Armarouge 25 % (34-36) · Ceruledge 25 % (35-36) · Salandit 20 % (36-40) → en jeu : Salazzle (selon le niveau) — *changé : +Armarouge, +Ceruledge, +Magmortar, +Salandit, −Geodude, −Graveler, −Torkoal*

### Magma Hideout 2F 2R
- **Herbes** : Magmortar 30 % (33-34) · Armarouge 25 % (34-36) · Ceruledge 25 % (35-36) · Salandit 20 % (36-40) → en jeu : Salazzle (selon le niveau) — *changé : +Armarouge, +Ceruledge, +Magmortar, +Salandit, −Geodude, −Graveler, −Torkoal*

### Magma Hideout 2F 3R
- **Herbes** : Magmortar 30 % (33-34) · Armarouge 25 % (34-36) · Ceruledge 25 % (35-36) · Salandit 20 % (36-40) → en jeu : Salazzle (selon le niveau) — *changé : +Armarouge, +Ceruledge, +Magmortar, +Salandit, −Geodude, −Graveler, −Torkoal*

### Magma Hideout 3F 1R
- **Herbes** : Magmortar 30 % (33-34) · Armarouge 25 % (34-36) · Ceruledge 25 % (35-36) · Salandit 20 % (36-40) → en jeu : Salazzle (selon le niveau) — *changé : +Armarouge, +Ceruledge, +Magmortar, +Salandit, −Geodude, −Graveler, −Torkoal*

### Magma Hideout 3F 2R
- **Herbes** : Magmortar 30 % (33-34) · Armarouge 25 % (34-36) · Ceruledge 25 % (35-36) · Salandit 20 % (36-40) → en jeu : Salazzle (selon le niveau) — *changé : +Armarouge, +Ceruledge, +Magmortar, +Salandit, −Geodude, −Graveler, −Torkoal*

### Magma Hideout 3F 3R
- **Herbes** : Magmortar 30 % (33-34) · Armarouge 25 % (34-36) · Ceruledge 25 % (35-36) · Salandit 20 % (36-40) → en jeu : Salazzle (selon le niveau) — *changé : +Armarouge, +Ceruledge, +Magmortar, +Salandit, −Geodude, −Graveler, −Torkoal*

### Magma Hideout 4F
- **Herbes** : Magmortar 30 % (33-34) · Armarouge 25 % (34-36) · Ceruledge 25 % (35-36) · Salandit 20 % (36-40) → en jeu : Salazzle (selon le niveau) — *changé : +Armarouge, +Ceruledge, +Magmortar, +Salandit, −Geodude, −Graveler, −Torkoal*

### Mossdeep City
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-36) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (30-36)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 60 % (30-55) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (36-43)

### Mt Pyre 1F
- **Herbes** : Greavard 25 % (28-33) → en jeu : Houndstone (selon le niveau) · Spiritomb 25 % (27-34) · Banette 20 % (30-32) · Sableye 20 % (29-35) · Litwick 10 % (29-35) — *changé : +Banette, +Greavard, +Litwick, +Sableye, +Spiritomb, −Shuppet*

### Mt Pyre 2F
- **Herbes** : Greavard 25 % (28-33) → en jeu : Houndstone (selon le niveau) · Spiritomb 25 % (27-34) · Banette 20 % (30-32) · Sableye 20 % (29-35) · Litwick 10 % (29-35) — *changé : +Banette, +Greavard, +Litwick, +Sableye, +Spiritomb, −Shuppet*

### Mt Pyre 3F
- **Herbes** : Greavard 25 % (28-33) → en jeu : Houndstone (selon le niveau) · Spiritomb 25 % (27-34) · Banette 20 % (30-32) · Sableye 20 % (29-35) · Litwick 10 % (29-35) — *changé : +Banette, +Greavard, +Litwick, +Sableye, +Spiritomb, −Shuppet*

### Mt Pyre 4F
- **Herbes** : Greavard 25 % (28-33) → en jeu : Houndstone (selon le niveau) · Spiritomb 25 % (27-34) · Banette 20 % (30-32) · Sableye 20 % (29-35) · Litwick 10 % (30-35) — *changé : +Banette, +Greavard, +Litwick, +Sableye, +Spiritomb, −Duskull, −Shuppet*

### Mt Pyre 5F
- **Herbes** : Greavard 25 % (28-33) → en jeu : Houndstone (selon le niveau) · Spiritomb 25 % (27-34) · Banette 20 % (30-32) · Sableye 20 % (29-35) · Litwick 10 % (30-35) — *changé : +Banette, +Greavard, +Litwick, +Sableye, +Spiritomb, −Duskull, −Shuppet*

### Mt Pyre 6F
- **Herbes** : Greavard 25 % (28-33) → en jeu : Houndstone (selon le niveau) · Spiritomb 25 % (27-34) · Banette 20 % (30-32) · Sableye 20 % (29-35) · Litwick 10 % (30-35) — *changé : +Banette, +Greavard, +Litwick, +Sableye, +Spiritomb, −Duskull, −Shuppet*

### Mt Pyre Exterior
- **Herbes** : Braviary 30 % (33-34) · Bombirdier 25 % (33-35) · Drifblim 20 % (35) · Fearow 10 % (33) · Dusclops 10 % (30-34) · Meditite 5 % (32-33) — *changé : +Bombirdier, +Braviary, +Drifblim, +Dusclops, +Fearow, +Meditite, −Shuppet, −Vulpix, −Wingull*

### Mt Pyre Summit
- **Herbes** : Braviary 30 % (33-34) · Bombirdier 25 % (29-35) · Drifblim 20 % (32-36) · Fearow 10 % (30) · Dusclops 10 % (32-34) · Meditite 5 % (34-36) — *changé : +Bombirdier, +Braviary, +Drifblim, +Dusclops, +Fearow, +Meditite, −Chimecho, −Duskull, −Shuppet*

### Route 121
- **Herbes** : Zebstrika 20 % (32) · Rapidash-Galar 20 % (32) · Nidoqueen 15 % (32-34) · Nidoking 15 % (34) · Farigiraf 15 % (32-34) · Wyrdeer 15 % (30-33) — *changé : +Farigiraf, +Nidoking, +Nidoqueen, +Rapidash-Galar, +Wyrdeer, +Zebstrika, −Gloom, −Kecleon, −Mightyena, −Oddish, −Poochyena, −Shuppet, −Wingull*
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-36) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (30-36)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 100 % (24-55) → en jeu : Wailord (selon le niveau)

### Route 122
- **Surf** : Tatsugiri-Curly 60 % (6-43) · Tatsugiri-Droopy 30 % (12-36) · Tatsugiri-Stretchy 10 % (18-36) — *changé : +Tatsugiri-Curly, +Tatsugiri-Droopy, +Tatsugiri-Stretchy, −Pelipper, −Tentacool, −Wingull*
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 60 % (30-55) → en jeu : Wailord (selon le niveau) · Sharpedo 40 % (36-43)

### Route 123
- **Herbes** : Zoroark 25 % (32-34) · Clodsire 25 % (32-34) · Breloom 20 % (32-34) · Noctowl 15 % (32-34) · Tarountula 15 % (30-33) → en jeu : Spidops — *changé : +Breloom, +Clodsire, +Noctowl, +Tarountula, +Zoroark, −Gloom, −Kecleon, −Mightyena, −Oddish, −Poochyena, −Shuppet, −Wingull*
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Wingull 35 % (12-36) → en jeu : Pelipper (selon le niveau) · Pelipper 5 % (30-36)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 100 % (24-55) → en jeu : Wailord (selon le niveau)

### Route 124
- **Surf** : Wailmer 60 % (6-43) → en jeu : Wailord (selon le niveau) · Basculegion-M 30 % (12-36) · Basculegion-F 10 % (18-36) — *changé : +Basculegion-F, +Basculegion-M, +Wailmer, −Pelipper, −Tentacool, −Wingull*
- **Canne** : Kingdra 100 % (6-12) — *changé : +Kingdra, −Magikarp, −Tentacool*
- **Super Canne** : Kingdra 100 % (12-36) — *changé : +Kingdra, −Magikarp, −Tentacool, −Wailmer*
- **Méga Canne** : Kingdra 100 % (30-55) — *changé : +Kingdra, −Sharpedo, −Wailmer*

### Route 125
- **Surf** : Wailmer 60 % (6-43) → en jeu : Wailord (selon le niveau) · Basculegion-M 30 % (12-36) · Basculegion-F 10 % (18-36) — *changé : +Basculegion-F, +Basculegion-M, +Wailmer, −Pelipper, −Tentacool, −Wingull*
- **Canne** : Kingdra 100 % (6-12) — *changé : +Kingdra, −Magikarp, −Tentacool*
- **Super Canne** : Kingdra 100 % (12-36) — *changé : +Kingdra, −Magikarp, −Tentacool, −Wailmer*
- **Méga Canne** : Kingdra 100 % (30-55) — *changé : +Kingdra, −Sharpedo, −Wailmer*

### Route 126
- **Surf** : Wailmer 60 % (6-43) → en jeu : Wailord (selon le niveau) · Basculegion-M 30 % (12-36) · Basculegion-F 10 % (18-36) — *changé : +Basculegion-F, +Basculegion-M, +Wailmer, −Pelipper, −Tentacool, −Wingull*
- **Canne** : Kingdra 100 % (6-12) — *changé : +Kingdra, −Magikarp, −Tentacool*
- **Super Canne** : Kingdra 100 % (12-36) — *changé : +Kingdra, −Magikarp, −Tentacool, −Wailmer*
- **Méga Canne** : Kingdra 100 % (30-55) — *changé : +Kingdra, −Sharpedo, −Wailmer*

### Route 127
- **Surf** : Wailmer 60 % (6-43) → en jeu : Wailord (selon le niveau) · Basculegion-M 30 % (12-36) · Basculegion-F 10 % (18-36) — *changé : +Basculegion-F, +Basculegion-M, +Wailmer, −Pelipper, −Tentacool, −Wingull*
- **Canne** : Kingdra 100 % (6-12) — *changé : +Kingdra, −Magikarp, −Tentacool*
- **Super Canne** : Kingdra 100 % (12-36) — *changé : +Kingdra, −Magikarp, −Tentacool, −Wailmer*
- **Méga Canne** : Kingdra 100 % (30-55) — *changé : +Kingdra, −Sharpedo, −Wailmer*

### Route 128
- **Surf** : Wailmer 60 % (6-43) → en jeu : Wailord (selon le niveau) · Basculegion-M 30 % (12-36) · Basculegion-F 10 % (18-36) — *changé : +Basculegion-F, +Basculegion-M, +Wailmer, −Pelipper, −Tentacool, −Wingull*
- **Canne** : Kingdra 100 % (6-12) — *changé : +Kingdra, −Magikarp, −Tentacool*
- **Super Canne** : Kingdra 100 % (12-36) — *changé : +Kingdra, −Luvdisc, −Magikarp, −Wailmer*
- **Méga Canne** : Kingdra 100 % (36-55) — *changé : +Kingdra, −Corsola, −Luvdisc, −Wailmer*

### Shoal Cave Low Tide Entrance Room
- **Herbes** : Seel 20 % (32) · Spheal 20 % (32) → en jeu : Sealeo · Sliggoo 20 % (34) · Toedscool 20 % (36) → en jeu : Toedscruel · Gastrodon-West 10 % (39) · Gastrodon-East 10 % (39) — *changé : +Gastrodon-East, +Gastrodon-West, +Seel, +Sliggoo, +Toedscool, −Golbat, −Zubat*
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Zubat 30 % (6-43) → en jeu : Crobat, Golbat (selon le niveau) · Spheal 10 % (30-43) → en jeu : Sealeo (selon le niveau)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 100 % (24-55) → en jeu : Wailord (selon le niveau)

### Shoal Cave Low Tide Ice Room
- **Herbes** : Frigibax 30 % (32-34) · Swinub 25 % (32) · Vulpix-Alola 15 % (34-39) · Snorunt 15 % (36-39) · Sandshrew-Alola 15 % (34-36) — *changé : +Frigibax, +Sandshrew-Alola, +Swinub, +Vulpix-Alola, −Golbat, −Spheal, −Zubat*

### Shoal Cave Low Tide Inner Room
- **Herbes** : Seel 20 % (32) · Spheal 20 % (32) → en jeu : Sealeo · Sliggoo 20 % (34) · Toedscool 20 % (36) → en jeu : Toedscruel · Gastrodon-West 10 % (39) · Gastrodon-East 10 % (39) — *changé : +Gastrodon-East, +Gastrodon-West, +Seel, +Sliggoo, +Toedscool, −Golbat, −Zubat*
- **Surf** : Tentacool 60 % (6-43) → en jeu : Tentacruel (selon le niveau) · Zubat 30 % (6-43) → en jeu : Crobat, Golbat (selon le niveau) · Spheal 10 % (30-43) → en jeu : Sealeo (selon le niveau)
- **Canne** : Magikarp 70 % (6-12) · Tentacool 30 % (6-12)
- **Super Canne** : Magikarp 60 % (12-36) → en jeu : Gyarados (selon le niveau) · Tentacool 20 % (12-36) → en jeu : Tentacruel (selon le niveau) · Wailmer 20 % (12-36)
- **Méga Canne** : Wailmer 100 % (24-55) → en jeu : Wailord (selon le niveau)

### Shoal Cave Low Tide Lower Room
- **Herbes** : Seel 20 % (32) · Spheal 20 % (32) → en jeu : Sealeo · Sliggoo 20 % (34) · Toedscool 20 % (36) → en jeu : Toedscruel · Gastrodon-West 10 % (39) · Gastrodon-East 10 % (39) — *changé : +Gastrodon-East, +Gastrodon-West, +Seel, +Sliggoo, +Toedscool, −Golbat, −Zubat*

### Shoal Cave Low Tide Stairs Room
- **Herbes** : Seel 20 % (32) · Spheal 20 % (32) → en jeu : Sealeo · Sliggoo 20 % (34) · Toedscool 20 % (36) → en jeu : Toedscruel · Gastrodon-West 10 % (39) · Gastrodon-East 10 % (39) — *changé : +Gastrodon-East, +Gastrodon-West, +Seel, +Sliggoo, +Toedscool, −Golbat, −Zubat*

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
- **Herbes** : Minior 30 % (46) · Elgyem 20 % (49) → en jeu : Beheeyem · Bagon 20 % (46-49) → en jeu : Shelgon · Glimmet 20 % (49-55) → en jeu : Glimmora · Solrock 10 % (53-56) — *changé : +Bagon, +Elgyem, +Glimmet, +Minior, −Golbat*
- **Surf** : Tatsugiri-Curly 60 % (42-49) · Tatsugiri-Droopy 30 % (42-49) · Tatsugiri-Stretchy 10 % (7-49) — *changé : +Tatsugiri-Curly, +Tatsugiri-Droopy, +Tatsugiri-Stretchy, −Golbat, −Solrock*
- **Canne** : Magikarp 70 % (7-14) · Goldeen 30 % (7-14)
- **Super Canne** : Magikarp 60 % (14-42) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (14-42) → en jeu : Seaking (selon le niveau) · Barboach 20 % (14-42) → en jeu : Whiscash (selon le niveau)
- **Méga Canne** : Barboach 80 % (35-49) → en jeu : Whiscash · Whiscash 20 % (42-63)

### Meteor Falls 1F 2R (nuit)
- **Herbes** : Minior 30 % (46) · Elgyem 20 % (49) → en jeu : Beheeyem · Bagon 20 % (46-49) → en jeu : Shelgon · Glimmet 20 % (49-55) → en jeu : Glimmora · Lunatone 10 % (53-56) — *changé : +Bagon, +Elgyem, +Glimmet, +Lunatone, +Minior, −Golbat, −Solrock*
- **Surf** : Tatsugiri-Curly 60 % (42-49) · Tatsugiri-Droopy 30 % (42-49) · Tatsugiri-Stretchy 10 % (7-49) — *changé : +Tatsugiri-Curly, +Tatsugiri-Droopy, +Tatsugiri-Stretchy, −Golbat, −Solrock*

### Meteor Falls B1F 1R
- **Herbes** : Minior 30 % (46) · Elgyem 20 % (49) → en jeu : Beheeyem · Bagon 20 % (46-49) → en jeu : Shelgon · Glimmet 20 % (49-55) → en jeu : Glimmora · Solrock 10 % (53-56) — *changé : +Bagon, +Elgyem, +Glimmet, +Minior, −Golbat*
- **Surf** : Tatsugiri-Curly 60 % (42-49) · Tatsugiri-Droopy 30 % (42-49) · Tatsugiri-Stretchy 10 % (7-49) — *changé : +Tatsugiri-Curly, +Tatsugiri-Droopy, +Tatsugiri-Stretchy, −Golbat, −Solrock*
- **Canne** : Magikarp 70 % (7-14) · Goldeen 30 % (7-14)
- **Super Canne** : Magikarp 60 % (14-42) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (14-42) → en jeu : Seaking (selon le niveau) · Barboach 20 % (14-42) → en jeu : Whiscash (selon le niveau)
- **Méga Canne** : Barboach 80 % (35-49) → en jeu : Whiscash · Whiscash 20 % (42-63)

### Meteor Falls B1F 1R (nuit)
- **Herbes** : Minior 30 % (46) · Elgyem 20 % (49) → en jeu : Beheeyem · Bagon 20 % (46-49) → en jeu : Shelgon · Glimmet 20 % (49-55) → en jeu : Glimmora · Lunatone 10 % (53-56) — *changé : +Bagon, +Elgyem, +Glimmet, +Lunatone, +Minior, −Golbat, −Solrock*
- **Surf** : Tatsugiri-Curly 60 % (42-49) · Tatsugiri-Droopy 30 % (42-49) · Tatsugiri-Stretchy 10 % (7-49) — *changé : +Tatsugiri-Curly, +Tatsugiri-Droopy, +Tatsugiri-Stretchy, −Golbat, −Solrock*

### Meteor Falls B1F 2R
- **Herbes** : Minior 30 % (42-46) · Elgyem 20 % (49) → en jeu : Beheeyem · Bagon 20 % (49) → en jeu : Shelgon · Glimmet 20 % (35-55) → en jeu : Glimmora · Solrock 10 % (53-56) — *changé : +Elgyem, +Glimmet, +Minior, −Golbat*
- **Surf** : Tatsugiri-Curly 60 % (42-49) · Tatsugiri-Droopy 30 % (42-49) · Tatsugiri-Stretchy 10 % (7-49) — *changé : +Tatsugiri-Curly, +Tatsugiri-Droopy, +Tatsugiri-Stretchy, −Golbat, −Solrock*
- **Canne** : Magikarp 70 % (7-14) · Goldeen 30 % (7-14)
- **Super Canne** : Magikarp 60 % (14-42) → en jeu : Gyarados (selon le niveau) · Goldeen 20 % (14-42) → en jeu : Seaking (selon le niveau) · Barboach 20 % (14-42) → en jeu : Whiscash (selon le niveau)
- **Méga Canne** : Barboach 80 % (35-49) → en jeu : Whiscash · Whiscash 20 % (42-63)

### Meteor Falls B1F 2R (nuit)
- **Herbes** : Minior 30 % (42-46) · Elgyem 20 % (49) → en jeu : Beheeyem · Bagon 20 % (49) → en jeu : Shelgon · Glimmet 20 % (35-55) → en jeu : Glimmora · Lunatone 10 % (53-56) — *changé : +Elgyem, +Glimmet, +Lunatone, +Minior, −Golbat, −Solrock*
- **Surf** : Tatsugiri-Curly 60 % (42-49) · Tatsugiri-Droopy 30 % (42-49) · Tatsugiri-Stretchy 10 % (7-49) — *changé : +Tatsugiri-Curly, +Tatsugiri-Droopy, +Tatsugiri-Stretchy, −Golbat, −Solrock*

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
- **Herbes** : Minior 30 % (33) · Elgyem 20 % (35) · Bagon 20 % (33-35) → en jeu : Shelgon · Glimmet 20 % (35-39) → en jeu : Glimmora · Solrock 10 % (38-40) — *changé : +Bagon, +Elgyem, +Glimmet, +Minior, −Golbat*

### Meteor Falls Stevens Cave (nuit)
- **Herbes** : Minior 30 % (33) · Elgyem 20 % (35) · Bagon 20 % (33-35) → en jeu : Shelgon · Glimmet 20 % (35-39) → en jeu : Glimmora · Lunatone 10 % (38-40) — *changé : +Bagon, +Elgyem, +Glimmet, +Lunatone, +Minior, −Golbat, −Solrock*

### Nabla West Beach
- *Table ajoutée par Nabla.*
- **Herbes** : Wiglett 20 % (5-7) · Dwebble 20 % (5-7) · Pyukumuku 10 % (5-8) · Sandygast 10 % (5-8) · Krabby 10 % (5-8) · Mantyke 10 % (5-8) · Clauncher 10 % (6-8) · Staryu 10 % (6-8)
- **Surf** : Mareanie 60 % (6-43) → en jeu : Toxapex (selon le niveau) · Tentacool 40 % (12-37) → en jeu : Tentacruel (selon le niveau)
- **Canne** : Mareanie 70 % (5-11) · Tentacool 30 % (5-11)
- **Super Canne** : Mareanie 60 % (12-37) · Tentacool 40 % (12-37) → en jeu : Tentacruel (selon le niveau)
- **Méga Canne** : Mareanie 60 % (30-55) → en jeu : Toxapex (selon le niveau) · Tentacool 40 % (36-43) → en jeu : Tentacruel
