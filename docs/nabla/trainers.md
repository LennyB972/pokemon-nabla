# Équipes des dresseurs importants

Fiche de travail de l'étape 4.2. C'est l'utilisateur qui compose les équipes ; Claude les intègre au jeu (`src/data/trainers.party`), complète les détails techniques et vérifie.

## Règles

- **Mode Normal** : équipes libres, **niveaux d'origine** conservés (le Pokémon le plus fort est au niveau du level cap du badge). **6 Pokémon à partir de la 6ᵉ arène.**
- **Méga-Évolution à partir de la 6ᵉ arène, dans les deux modes** : un seul Pokémon méga-évolutif par équipe, qui tient sa Méga-Gemme (`Altaria @ Altarianite`).
- **Mode Difficile** : **même composition** qu'en Normal ; seuls les niveaux et/ou les sets changent (capacités, objets, talents, natures, EV/IV, IA avancée, pas d'objets de soin). Claude proposera les sets à partir de tes équipes ; les niveaux seront réglés au calibrage (4.3).

## Comment écrire une équipe

Au **format Pokémon Showdown** (noms anglais), le format du fichier des dresseurs du jeu. Le plus simple : le constructeur d'équipes de Showdown (play.pokemonshowdown.com/teambuilder), puis *Export*, et coller le texte dans la case « Normal » du Champion (ou dans le chat). Pour chaque Pokémon :

```
Altaria @ Altarianite
Ability: Natural Cure
Level: 33
- Dragon Breath
- Aerial Ace
- Dragon Dance
- Earthquake
```

- Le niveau est obligatoire ; le reste est facultatif. Si les IV manquent, Claude reprend ceux des équipes d'origine (plus élevés pour le Pokémon le plus fort) ; Showdown n'écrit pas les IV parfaits.
- La ligne `Items:` de l'équipe d'origine liste les objets de soin que le Champion utilise en combat (Potions…) : à garder, changer ou supprimer en Normal ; aucun en Difficile.
- Si une case reste vide, l'équipe d'origine est gardée.

## Pokémon méga-évolutifs (hors légendaires) pour les arènes 6 à 8

- **Vol (Alizée)** : Aerodactyl, Altaria, Charizard X et Y, Clefable, Dragonite, Gyarados, Hawlucha, Pidgeot, Pinsir, Salamence, Skarmory, Staraptor.
- **Psy (Lévy & Tatia)** : Alakazam, Chimecho, Delphox, Gallade, Gardevoir, Malamar, Medicham, Meowstic, Metagross, Slowbro, Starmie.
- **Eau (Juan)** : Barbaracle, Blastoise, Feraligatr, Golisopod, Greninja, Gyarados, Sharpedo, Slowbro, Starmie, Swampert, Tatsugiri.

(Le Pokémon ou sa Méga-Évolution a le type de l'arène. Le nom de la Méga-Gemme est celui de Showdown : Altarianite, Metagrossite, Swampertite…)

## Roxanne — Mérouville (Roche)

- Niveau maximal : **15** (level cap du badge).
- Objets de soin d'origine : Potion / Potion.

**Équipe d'origine**

```
Geodude
Level: 12
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Tackle
- Defense Curl
- Rock Throw
- Rock Tomb

Geodude
Level: 12
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Tackle
- Defense Curl
- Rock Throw
- Rock Tomb

Nosepass @ Oran Berry
Level: 15
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Block
- Harden
- Tackle
- Rock Tomb
```

**Normal** (à remplir)

```

```

**Difficile** : même composition ; sets proposés par Claude une fois l'équipe Normal fixée.

## Bastien (Brawly) — Myokara (Combat)

- Niveau maximal : **19** (level cap du badge).
- Objets de soin d'origine : Super Potion / Super Potion.

**Équipe d'origine**

```
Machop
Level: 16
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Karate Chop
- Low Kick
- Seismic Toss
- Bulk Up

Meditite
Level: 16
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Focus Punch
- Light Screen
- Reflect
- Bulk Up

Makuhita @ Sitrus Berry
Level: 19
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Arm Thrust
- Vital Throw
- Reversal
- Bulk Up
```

**Normal** (à remplir)

```

```

**Difficile** : même composition ; sets proposés par Claude une fois l'équipe Normal fixée.

## Voltère (Wattson) — Lavandia (Électrik)

- Niveau maximal : **24** (level cap du badge).
- Objets de soin d'origine : Super Potion / Super Potion.

**Équipe d'origine**

```
Voltorb
Level: 20
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Rollout
- Spark
- Self Destruct
- Shock Wave

Electrike
Level: 20
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Shock Wave
- Leer
- Quick Attack
- Howl

Magneton
Level: 22
IVs: 26 HP / 26 Atk / 26 Def / 26 SpA / 26 SpD / 26 Spe
- Supersonic
- Shock Wave
- Thunder Wave
- Sonic Boom

Manectric @ Sitrus Berry
Level: 24
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Quick Attack
- Thunder Wave
- Shock Wave
- Howl
```

**Normal** (à remplir)

```

```

**Difficile** : même composition ; sets proposés par Claude une fois l'équipe Normal fixée.

## Adriane (Flannery) — Vermilava (Feu)

- Niveau maximal : **29** (level cap du badge).
- Objets de soin d'origine : Hyper Potion / Hyper Potion.

**Équipe d'origine**

```
Numel
Level: 24
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Overheat
- Take Down
- Magnitude
- Sunny Day

Slugma
Level: 24
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Overheat
- Smog
- Light Screen
- Sunny Day

Camerupt
Level: 26
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Overheat
- Tackle
- Sunny Day
- Attract

Torkoal @ White Herb
Level: 29
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Overheat
- Sunny Day
- Body Slam
- Attract
```

**Normal** (à remplir)

```

```

**Difficile** : même composition ; sets proposés par Claude une fois l'équipe Normal fixée.

## Norman — Clémenti-Ville (Normal)

- Niveau maximal : **31** (level cap du badge).
- Objets de soin d'origine : Hyper Potion / Hyper Potion.

**Équipe d'origine**

```
Spinda
Level: 27
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Teeter Dance
- Psybeam
- Facade
- Encore

Vigoroth
Level: 27
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Slash
- Facade
- Encore
- Feint Attack

Linoone
Level: 29
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Slash
- Belly Drum
- Facade
- Headbutt

Slaking @ Sitrus Berry
Level: 31
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Counter
- Yawn
- Facade
- Feint Attack
```

**Normal** (à remplir)

```

```

**Difficile** : même composition ; sets proposés par Claude une fois l'équipe Normal fixée.

## Alizée (Winona) — Cimetronelle (Vol)

- Niveau maximal : **33** (level cap du badge) ; **6 Pokémon, une Méga-Évolution**.
- Objets de soin d'origine : Hyper Potion / Hyper Potion.

**Équipe d'origine**

```
Swablu
Level: 29
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Perish Song
- Mirror Move
- Safeguard
- Aerial Ace

Tropius
Level: 29
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Sunny Day
- Aerial Ace
- Solar Beam
- Synthesis

Pelipper
Level: 30
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Water Gun
- Supersonic
- Protect
- Aerial Ace

Skarmory
Level: 31
IVs: 26 HP / 26 Atk / 26 Def / 26 SpA / 26 SpD / 26 Spe
- Sand Attack
- Fury Attack
- Steel Wing
- Aerial Ace

Altaria @ Oran Berry
Level: 33
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Earthquake
- Dragon Breath
- Dragon Dance
- Aerial Ace
```

**Normal** (à remplir)

```

```

**Difficile** : même composition ; sets proposés par Claude une fois l'équipe Normal fixée.

## Lévy & Tatia (Tate & Liza) — Algatia (Psy, combat en duo)

- Niveau maximal : **42** (level cap du badge) ; **6 Pokémon, une Méga-Évolution**.
- Objets de soin d'origine : Hyper Potion / Hyper Potion / Hyper Potion / Hyper Potion.

**Équipe d'origine**

```
Claydol
Level: 41
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Earthquake
- Ancient Power
- Psychic
- Light Screen

Xatu
Level: 41
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Psychic
- Sunny Day
- Confuse Ray
- Calm Mind

Lunatone @ Sitrus Berry
Level: 42
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Light Screen
- Psychic
- Hypnosis
- Calm Mind

Solrock @ Sitrus Berry
Level: 42
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Sunny Day
- Solar Beam
- Psychic
- Flamethrower
```

**Normal** (à remplir)

```

```

**Difficile** : même composition ; sets proposés par Claude une fois l'équipe Normal fixée.

## Juan — Atalanopolis (Eau)

- Niveau maximal : **46** (level cap du badge) ; **6 Pokémon, une Méga-Évolution**.
- Objets de soin d'origine : Hyper Potion / Hyper Potion.

**Équipe d'origine**

```
Luvdisc
Level: 41
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Water Pulse
- Attract
- Sweet Kiss
- Flail

Whiscash
Level: 41
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Rain Dance
- Water Pulse
- Amnesia
- Earthquake

Sealeo
Level: 43
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Encore
- Body Slam
- Aurora Beam
- Water Pulse

Crawdaunt
Level: 43
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Water Pulse
- Crabhammer
- Taunt
- Leer

Kingdra @ Chesto Berry
Level: 46
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Water Pulse
- Double Team
- Ice Beam
- Rest
```

**Normal** (à remplir)

```

```

**Difficile** : même composition ; sets proposés par Claude une fois l'équipe Normal fixée.
