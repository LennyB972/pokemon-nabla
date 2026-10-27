@ The Emerald Forest (story of the user): at the top of Mt. Pyre, after Team Aqua took the Red Orb, Wally tells
@ the player that Team Magma went to the Emerald Forest to find a Pokémon that travels through time (Celebi),
@ to get back the Orb they are missing. Wally waits at the edge of the forest; Magma grunts in the forest; in
@ the sanctuary, the player and Wally battle Maxie and Tabitha together; Celebi chooses Wally, who heals the
@ player's team and battles them. Until then, a Magma guard keeps the Magma Hideout closed in Jagged Pass.
@ Who is shown on each map is set when entering it (temporary flags), from FLAG_NABLA_EMERALD_FOREST_*.

@ Mt. Pyre summit

@ Called from MtPyre_Summit_OnTransition
Nabla_MtPyre_Summit_EventScript_HideWally::
	setflag FLAG_TEMP_11
	return

@ Called at the end of the summit scene
Nabla_MtPyre_Summit_EventScript_WallyArrives::
	delay 30
	msgbox Nabla_Text_WallyWaitForMe, MSGBOX_DEFAULT
	closemessage
	clearflag FLAG_TEMP_11
	addobject LOCALID_MT_PYRE_SUMMIT_NABLA_WALLY
	applymovement LOCALID_MT_PYRE_SUMMIT_NABLA_WALLY, Nabla_MtPyre_Summit_Movement_WallyComesUp
	waitmovement 0
	applymovement OBJ_EVENT_ID_PLAYER, Common_Movement_WalkInPlaceFasterDown
	waitmovement 0
	msgbox Nabla_Text_WallyMagmaWentToTheForest, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_MT_PYRE_SUMMIT_NABLA_WALLY, Nabla_MtPyre_Summit_Movement_WallyLeaves
	waitmovement 0
	removeobject LOCALID_MT_PYRE_SUMMIT_NABLA_WALLY
	setflag FLAG_NABLA_EMERALD_FOREST_CALL
	return

Nabla_MtPyre_Summit_Movement_WallyComesUp:
	walk_fast_up
	walk_fast_up
	walk_fast_up
	walk_fast_up
	walk_fast_up
	walk_fast_up
	step_end

Nabla_MtPyre_Summit_Movement_WallyLeaves:
	walk_fast_down
	walk_fast_down
	walk_fast_down
	walk_fast_down
	walk_fast_down
	walk_fast_down
	step_end

@ Jagged Pass: the Magma Hideout stays closed while Maxie is in the forest

@ Called from JaggedPass_OnTransition
Nabla_JaggedPass_EventScript_SetUpGuard::
	setflag FLAG_TEMP_11
	goto_if_unset FLAG_NABLA_EMERALD_FOREST_CALL, Common_EventScript_NopReturn
	goto_if_set FLAG_NABLA_EMERALD_FOREST_DONE, Common_EventScript_NopReturn
	clearflag FLAG_TEMP_11
	return

Nabla_JaggedPass_EventScript_Guard::
	msgbox Nabla_Text_JaggedPassGuard, MSGBOX_NPC
	end

@ Edge of the forest: Wally waits at the entrance of the woods

Nabla_EmeraldForest_Entrance_EventScript_SetUp::
	setflag FLAG_TEMP_11
	goto_if_unset FLAG_NABLA_EMERALD_FOREST_CALL, Common_EventScript_NopReturn
	goto_if_set FLAG_NABLA_EMERALD_FOREST_WALLY_MET, Common_EventScript_NopReturn
	clearflag FLAG_TEMP_11
	setvar VAR_TEMP_1, 1
	return

Nabla_EmeraldForest_Entrance_EventScript_WallyNoticesPlayer::
	lockall
	applymovement LOCALID_EMERALD_FOREST_ENTRANCE_WALLY, Common_Movement_ExclamationMark
	waitmovement 0
	goto Nabla_EmeraldForest_Entrance_EventScript_WallyGoesAhead

Nabla_EmeraldForest_Entrance_EventScript_Wally::
	lockall
	faceplayer
	goto Nabla_EmeraldForest_Entrance_EventScript_WallyGoesAhead

Nabla_EmeraldForest_Entrance_EventScript_WallyGoesAhead::
	setvar VAR_TEMP_1, 0
	msgbox Nabla_Text_WallyForestEntrance, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_EMERALD_FOREST_ENTRANCE_WALLY, Nabla_EmeraldForest_Entrance_Movement_WallyGoesAhead
	waitmovement 0
	removeobject LOCALID_EMERALD_FOREST_ENTRANCE_WALLY
	setflag FLAG_NABLA_EMERALD_FOREST_WALLY_MET
	releaseall
	end

Nabla_EmeraldForest_Entrance_Movement_WallyGoesAhead:
	face_down
	walk_fast_down
	walk_fast_down
	walk_fast_down
	walk_fast_down
	step_end

@ The forest: Magma grunts

Nabla_EmeraldForest_EventScript_SetUp::
	setflag FLAG_TEMP_11
	goto_if_unset FLAG_NABLA_EMERALD_FOREST_CALL, Common_EventScript_NopReturn
	goto_if_set FLAG_NABLA_EMERALD_FOREST_DONE, Common_EventScript_NopReturn
	clearflag FLAG_TEMP_11
	return

Nabla_EmeraldForest_EventScript_Grunt1::
	trainerbattle_single TRAINER_NABLA_GRUNT_EMERALD_FOREST_1, Nabla_Text_ForestGrunt1Intro, Nabla_Text_ForestGrunt1Defeat
	msgbox Nabla_Text_ForestGrunt1PostBattle, MSGBOX_AUTOCLOSE
	end

Nabla_EmeraldForest_EventScript_Grunt2::
	trainerbattle_single TRAINER_NABLA_GRUNT_EMERALD_FOREST_2, Nabla_Text_ForestGrunt2Intro, Nabla_Text_ForestGrunt2Defeat
	msgbox Nabla_Text_ForestGrunt2PostBattle, MSGBOX_AUTOCLOSE
	end

Nabla_EmeraldForest_EventScript_Grunt3::
	trainerbattle_single TRAINER_NABLA_GRUNT_EMERALD_FOREST_3, Nabla_Text_ForestGrunt3Intro, Nabla_Text_ForestGrunt3Defeat
	msgbox Nabla_Text_ForestGrunt3PostBattle, MSGBOX_AUTOCLOSE
	end

@ The sanctuary: Maxie and Tabitha, then Celebi and Wally

Nabla_EmeraldForest_Sanctuary_EventScript_SetUp::
	setflag FLAG_TEMP_11  @ Wally
	setflag FLAG_TEMP_12  @ Maxie and Tabitha
	setflag FLAG_TEMP_13  @ Celebi
	goto_if_unset FLAG_NABLA_EMERALD_FOREST_WALLY_MET, Common_EventScript_NopReturn
	goto_if_set FLAG_NABLA_EMERALD_FOREST_DONE, Common_EventScript_NopReturn
	clearflag FLAG_TEMP_11
	goto_if_defeated TRAINER_NABLA_MAXIE_EMERALD_FOREST, Nabla_EmeraldForest_Sanctuary_EventScript_ShowCelebi
	clearflag FLAG_TEMP_12
	setvar VAR_TEMP_1, 1
	return

@ After the player lost to Wally
Nabla_EmeraldForest_Sanctuary_EventScript_ShowCelebi::
	clearflag FLAG_TEMP_13
	return

Nabla_EmeraldForest_Sanctuary_EventScript_Arrive::
	lockall
	setvar VAR_TEMP_1, 0
	call Nabla_EmeraldForest_Sanctuary_EventScript_WalkUpToWally
	applymovement LOCALID_EMERALD_FOREST_SANCTUARY_WALLY, Common_Movement_FaceRight
	applymovement OBJ_EVENT_ID_PLAYER, Common_Movement_FaceLeft
	waitmovement 0
	msgbox Nabla_Text_WallyThereTheyAre, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_EMERALD_FOREST_SANCTUARY_WALLY, Common_Movement_FaceDown
	applymovement OBJ_EVENT_ID_PLAYER, Common_Movement_FaceDown
	waitmovement 0
	playbgm MUS_ENCOUNTER_MAGMA, FALSE
	applymovement LOCALID_EMERALD_FOREST_SANCTUARY_MAXIE, Common_Movement_FaceUp
	applymovement LOCALID_EMERALD_FOREST_SANCTUARY_TABITHA, Common_Movement_FaceUp
	waitmovement 0
	msgbox Nabla_Text_MaxieForestIntro, MSGBOX_DEFAULT
	applymovement LOCALID_EMERALD_FOREST_SANCTUARY_WALLY, Common_Movement_FaceRight
	waitmovement 0
	msgbox Nabla_Text_WallyLetsBattleTogether, MSGBOX_DEFAULT
	closemessage
Nabla_EmeraldForest_Sanctuary_EventScript_ChoosePartyForMultiBattle:
	special SavePlayerParty
	fadescreenswapbuffers FADE_TO_BLACK
	special ChooseHalfPartyForBattle
	goto_if_ne VAR_RESULT, 0, Nabla_EmeraldForest_Sanctuary_EventScript_MultiBattle
	special LoadPlayerParty
	msgbox Nabla_Text_WallyChooseYourPokemon, MSGBOX_DEFAULT
	closemessage
	goto Nabla_EmeraldForest_Sanctuary_EventScript_ChoosePartyForMultiBattle

Nabla_EmeraldForest_Sanctuary_EventScript_MultiBattle:
	multi_2_vs_2 TRAINER_NABLA_MAXIE_EMERALD_FOREST, Nabla_Text_MaxieForestDefeat, TRAINER_NABLA_TABITHA_EMERALD_FOREST, Nabla_Text_TabithaForestDefeat, PARTNER_WALLY_EMERALD_FOREST
	switch VAR_RESULT
	case 1, Nabla_EmeraldForest_Sanctuary_EventScript_DefeatedMagma
	@ Lost: the scene plays again when the player comes back
	fadescreenswapbuffers FADE_TO_BLACK
	special SetCB2WhiteOut
	waitstate

Nabla_EmeraldForest_Sanctuary_EventScript_DefeatedMagma::
	msgbox Nabla_Text_MaxieThisIsNotOver, MSGBOX_DEFAULT
	closemessage
	playse SE_M_MORNING_SUN
	fadescreenswapbuffers FADE_TO_WHITE
	setobjectxyperm LOCALID_EMERALD_FOREST_SANCTUARY_CELEBI, 12, 6
	clearflag FLAG_TEMP_13
	addobject LOCALID_EMERALD_FOREST_SANCTUARY_CELEBI
	fadescreenswapbuffers FADE_FROM_WHITE
	waitse
	playmoncry SPECIES_CELEBI, CRY_MODE_ENCOUNTER
	waitmoncry
	applymovement LOCALID_EMERALD_FOREST_SANCTUARY_MAXIE, Common_Movement_FaceDown
	applymovement LOCALID_EMERALD_FOREST_SANCTUARY_TABITHA, Common_Movement_FaceDown
	waitmovement 0
	msgbox Nabla_Text_MaxieItsCelebi, MSGBOX_DEFAULT
	closemessage
	applymovement LOCALID_EMERALD_FOREST_SANCTUARY_CELEBI, Nabla_EmeraldForest_Sanctuary_Movement_CelebiGoesToWally
	waitmovement 0
	applymovement LOCALID_EMERALD_FOREST_SANCTUARY_WALLY, Common_Movement_FaceDown
	waitmovement 0
	msgbox Nabla_Text_CelebiLooksAtWally, MSGBOX_DEFAULT
	applymovement LOCALID_EMERALD_FOREST_SANCTUARY_MAXIE, Common_Movement_FaceUp
	waitmovement 0
	msgbox Nabla_Text_MaxieRetreats, MSGBOX_DEFAULT
	closemessage
	fadescreenswapbuffers FADE_TO_BLACK
	removeobject LOCALID_EMERALD_FOREST_SANCTUARY_MAXIE
	removeobject LOCALID_EMERALD_FOREST_SANCTUARY_TABITHA
	fadedefaultbgm
	fadescreenswapbuffers FADE_FROM_BLACK
	msgbox Nabla_Text_WallyCelebiComeWithMe, MSGBOX_DEFAULT
	closemessage
	playmoncry SPECIES_CELEBI, CRY_MODE_NORMAL
	waitmoncry
	msgbox Nabla_Text_CelebiChoseWally, MSGBOX_DEFAULT
	applymovement LOCALID_EMERALD_FOREST_SANCTUARY_WALLY, Common_Movement_FaceRight
	waitmovement 0
	msgbox Nabla_Text_WallyLetsBattle, MSGBOX_DEFAULT
	closemessage
	goto Nabla_EmeraldForest_Sanctuary_EventScript_BattleWally

@ Talking to Wally after losing to him
Nabla_EmeraldForest_Sanctuary_EventScript_Wally::
	lockall
	faceplayer
	goto_if_not_defeated TRAINER_NABLA_MAXIE_EMERALD_FOREST, Nabla_EmeraldForest_Sanctuary_EventScript_WallyEnd
	msgbox Nabla_Text_WallyReadyAgain, MSGBOX_DEFAULT
	closemessage
Nabla_EmeraldForest_Sanctuary_EventScript_BattleWally:
	call Common_EventScript_OutOfCenterPartyHeal
	trainerbattle_no_intro TRAINER_NABLA_WALLY_EMERALD_FOREST, Nabla_Text_WallyForestDefeat
	msgbox Nabla_Text_WallyFarewell, MSGBOX_DEFAULT
	closemessage
	fadescreenswapbuffers FADE_TO_BLACK
	removeobject LOCALID_EMERALD_FOREST_SANCTUARY_WALLY
	removeobject LOCALID_EMERALD_FOREST_SANCTUARY_CELEBI
	fadescreenswapbuffers FADE_FROM_BLACK
	setflag FLAG_NABLA_EMERALD_FOREST_DONE
Nabla_EmeraldForest_Sanctuary_EventScript_WallyEnd:
	releaseall
	end

@ From the top of the path, the player walks next to Wally (column 11, row 3)
Nabla_EmeraldForest_Sanctuary_EventScript_WalkUpToWally::
	applymovement OBJ_EVENT_ID_PLAYER, Common_Movement_WalkDown
	waitmovement 0
Nabla_EmeraldForest_Sanctuary_EventScript_WalkToColumn:
	getplayerxy VAR_0x8004, VAR_0x8005
	goto_if_lt VAR_0x8004, 11, Nabla_EmeraldForest_Sanctuary_EventScript_WalkRight
	goto_if_gt VAR_0x8004, 11, Nabla_EmeraldForest_Sanctuary_EventScript_WalkLeft
	applymovement OBJ_EVENT_ID_PLAYER, Common_Movement_WalkDown
	waitmovement 0
	return

Nabla_EmeraldForest_Sanctuary_EventScript_WalkRight:
	applymovement OBJ_EVENT_ID_PLAYER, Common_Movement_WalkRight
	waitmovement 0
	goto Nabla_EmeraldForest_Sanctuary_EventScript_WalkToColumn

Nabla_EmeraldForest_Sanctuary_EventScript_WalkLeft:
	applymovement OBJ_EVENT_ID_PLAYER, Common_Movement_WalkLeft
	waitmovement 0
	goto Nabla_EmeraldForest_Sanctuary_EventScript_WalkToColumn

Nabla_EmeraldForest_Sanctuary_Movement_CelebiGoesToWally:
	walk_up
	walk_up
	walk_left
	walk_left
	face_up
	step_end
