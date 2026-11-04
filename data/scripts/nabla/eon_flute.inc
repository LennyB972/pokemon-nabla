@ The Eon Flute, used from the bag (ItemUseOutOfBattle_EonFlute, src/item_use.c): Latios takes the player to a place
@ where legendary Pokémon live, then back to where they were (src/nabla_eon_flute.c)
Nabla_EventScript_EonFlute::
	lockall
	specialvar VAR_RESULT, NablaEonFlute_IsAtDestination
	goto_if_eq VAR_RESULT, TRUE, Nabla_EventScript_EonFluteGoBack
	playmoncry SPECIES_LATIOS, CRY_MODE_NORMAL
	message Nabla_Text_EonFluteWhereTo
	waitmessage
	waitmoncry
	dynmultipush Nabla_Text_FarawayIsland, 0
	dynmultipush Nabla_Text_NavelRock, 1
	dynmultipush Nabla_Text_BirthIsland, 2
	getcaughtmon SPECIES_LUGIA
	call_if_eq VAR_RESULT, TRUE, Nabla_EventScript_EonFluteListBirdIslet
	dynmultipush Nabla_Text_MoonIsland, 4
	dynmultipush Nabla_Text_LibertyIsland, 5
	dynmultipush Nabla_Text_TapuIslands, 6
	getcaughtmon SPECIES_MEW
	call_if_eq VAR_RESULT, TRUE, Nabla_EventScript_EonFluteListCeruleanCave
	getcaughtmon SPECIES_HO_OH
	call_if_eq VAR_RESULT, TRUE, Nabla_EventScript_EonFluteListBurnedTower
	dynmultipush Nabla_Text_ThreeLakes, 9
	dynmultistack 0, 0, FALSE, 6, FALSE, 0, DYN_MULTICHOICE_CB_NONE
	closemessage
	switch VAR_RESULT
	case 0, Nabla_EventScript_EonFluteToFarawayIsland
	case 1, Nabla_EventScript_EonFluteToNavelRock
	case 2, Nabla_EventScript_EonFluteToBirthIsland
	case 3, Nabla_EventScript_EonFluteToBirdIslet
	case 4, Nabla_EventScript_EonFluteToMoonIsland
	case 5, Nabla_EventScript_EonFluteToLibertyIsland
	case 6, Nabla_EventScript_EonFluteToTapuIslands
	case 7, Nabla_EventScript_EonFluteToCeruleanCave
	case 8, Nabla_EventScript_EonFluteToBurnedTower
	case 9, Nabla_EventScript_EonFluteToThreeLakes
	releaseall
	end

Nabla_EventScript_EonFluteToFarawayIsland:
	special NablaEonFlute_SaveReturnPoint
	warp MAP_FARAWAY_ISLAND_ENTRANCE, 13, 38
	waitstate
	releaseall
	end

Nabla_EventScript_EonFluteToNavelRock:
	special NablaEonFlute_SaveReturnPoint
	warp MAP_NAVEL_ROCK_HARBOR, 8, 4
	waitstate
	releaseall
	end

Nabla_EventScript_EonFluteToBirthIsland:
	special NablaEonFlute_SaveReturnPoint
	warp MAP_BIRTH_ISLAND_HARBOR, 8, 4
	waitstate
	releaseall
	end

Nabla_EventScript_EonFluteToBirdIslet:
	special NablaEonFlute_SaveReturnPoint
	warp MAP_NABLA_BIRD_ISLET, 12, 19
	waitstate
	releaseall
	end

Nabla_EventScript_EonFluteToMoonIsland:
	special NablaEonFlute_SaveReturnPoint
	warp MAP_NABLA_MOON_ISLAND, 15, 16
	waitstate
	releaseall
	end

Nabla_EventScript_EonFluteToLibertyIsland:
	special NablaEonFlute_SaveReturnPoint
	warp MAP_NABLA_LIBERTY_ISLAND, 10, 12
	waitstate
	releaseall
	end

Nabla_EventScript_EonFluteToTapuIslands:
	special NablaEonFlute_SaveReturnPoint
	warp MAP_NABLA_TAPU_ISLANDS, 20, 23
	waitstate
	releaseall
	end

@ The mirages to unlock are in the list once the Pokémon they ask for are caught
Nabla_EventScript_EonFluteListBirdIslet:
	dynmultipush Nabla_Text_BirdIslet, 3
	return

Nabla_EventScript_EonFluteListCeruleanCave:
	dynmultipush Nabla_Text_CeruleanCave, 7
	return

Nabla_EventScript_EonFluteListBurnedTower:
	dynmultipush Nabla_Text_BurnedTower, 8
	return

Nabla_EventScript_EonFluteToCeruleanCave:
	special NablaEonFlute_SaveReturnPoint
	warp MAP_NABLA_CERULEAN_CAVE, 12, 23
	waitstate
	releaseall
	end

Nabla_EventScript_EonFluteToBurnedTower:
	special NablaEonFlute_SaveReturnPoint
	warp MAP_NABLA_BURNED_TOWER, 17, 16
	waitstate
	releaseall
	end

Nabla_EventScript_EonFluteToThreeLakes:
	special NablaEonFlute_SaveReturnPoint
	warp MAP_NABLA_THREE_LAKES, 15, 16
	waitstate
	releaseall
	end

Nabla_EventScript_EonFluteGoBack:
	playmoncry SPECIES_LATIOS, CRY_MODE_NORMAL
	msgbox Nabla_Text_EonFluteGoBack, MSGBOX_YESNO
	waitmoncry
	goto_if_eq VAR_RESULT, NO, Nabla_EventScript_EonFluteStay
	closemessage
	special NablaEonFlute_WarpBack
	waitstate
	releaseall
	end

Nabla_EventScript_EonFluteStay:
	releaseall
	end

@ Mossdeep City, Steven's house, after the League (MOM tells the player he's waiting there): Steven is at home
@ until he gives the Eon Flute, also in a game that was already past the League; then he leaves for Meteor Falls
Nabla_StevensHouse_EventScript_SetUp::
	goto_if_unset FLAG_SYS_GAME_CLEAR, Common_EventScript_NopReturn
	checkitem ITEM_EON_FLUTE
	goto_if_eq VAR_RESULT, TRUE, Common_EventScript_NopReturn
	clearflag FLAG_HIDE_MOSSDEEP_CITY_STEVENS_HOUSE_STEVEN
	return

Nabla_StevensHouse_EventScript_EonFlute::
	lock
	faceplayer
	msgbox Nabla_Text_StevenEonFlute, MSGBOX_DEFAULT
	giveitem ITEM_EON_FLUTE
	msgbox Nabla_Text_StevenAboutEonFlute, MSGBOX_DEFAULT
	closemessage
	fadescreen FADE_TO_BLACK
	removeobject LOCALID_STEVENS_HOUSE_STEVEN
	fadescreen FADE_FROM_BLACK
	release
	end

@ Birth Island: Jirachi instead of Deoxys (already caught at Sky Pillar), without the triangle puzzle.
@ It comes back on the next visit until it is caught.
Nabla_BirthIsland_EventScript_SetUp::
	setflag FLAG_HIDE_BIRTH_ISLAND_DEOXYS_TRIANGLE
	setflag FLAG_HIDE_DEOXYS
	setflag FLAG_TEMP_11  @ Jirachi
	goto_if_set FLAG_NABLA_JIRACHI_CAUGHT, Common_EventScript_NopReturn
	clearflag FLAG_TEMP_11
	return

Nabla_BirthIsland_EventScript_Jirachi::
	setvar VAR_0x8004, SPECIES_JIRACHI
	call Nabla_EventScript_MirageLegendary
	setflag FLAG_NABLA_JIRACHI_CAUGHT
	release
	end
