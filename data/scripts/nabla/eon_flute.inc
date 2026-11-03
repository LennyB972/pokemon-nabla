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
	dynmultistack 0, 0, FALSE, 6, FALSE, 0, DYN_MULTICHOICE_CB_NONE
	closemessage
	switch VAR_RESULT
	case 0, Nabla_EventScript_EonFluteToFarawayIsland
	case 1, Nabla_EventScript_EonFluteToNavelRock
	case 2, Nabla_EventScript_EonFluteToBirthIsland
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
	lock
	faceplayer
	waitse
	playmoncry SPECIES_JIRACHI, CRY_MODE_ENCOUNTER
	delay 40
	waitmoncry
	setwildbattle SPECIES_JIRACHI, NABLA_POST_GAME_LEGENDARIES_LEVEL
	special BattleSetup_StartLegendaryBattle
	specialvar VAR_RESULT, GetBattleOutcome
	goto_if_eq VAR_RESULT, B_OUTCOME_CAUGHT, Nabla_BirthIsland_EventScript_CaughtJirachi
	setvar VAR_0x8004, SPECIES_JIRACHI
	goto Common_EventScript_LegendaryFlewAway

Nabla_BirthIsland_EventScript_CaughtJirachi:
	setflag FLAG_NABLA_JIRACHI_CAUGHT
	removeobject VAR_LAST_TALKED
	release
	end
