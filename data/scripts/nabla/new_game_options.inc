@ Asks the player for the difficulty and level caps, just before leaving the truck.
Nabla_EventScript_ChooseGameOptions::
	msgbox Nabla_Text_DifficultyIntro, MSGBOX_DEFAULT
	message Nabla_Text_ChooseDifficulty
	waitmessage
	dynmultichoice 0, 0, TRUE, 2, 0, DYN_MULTICHOICE_CB_NONE, Nabla_Text_Normal, Nabla_Text_Hard
	goto_if_eq VAR_RESULT, 1, Nabla_EventScript_ChooseHard
	setdifficulty DIFFICULTY_NORMAL
	bufferstring STR_VAR_1, Nabla_Text_Normal
	goto Nabla_EventScript_ChooseLevelCaps

Nabla_EventScript_ChooseHard:
	setdifficulty DIFFICULTY_HARD
	bufferstring STR_VAR_1, Nabla_Text_Hard
Nabla_EventScript_ChooseLevelCaps:
	msgbox Nabla_Text_LevelCapsIntro, MSGBOX_DEFAULT
	msgbox Nabla_Text_EnableLevelCaps, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Nabla_EventScript_NoLevelCaps
	setflag FLAG_NABLA_LEVEL_CAPS
	bufferstring STR_VAR_2, Nabla_Text_On
	goto Nabla_EventScript_ConfirmGameOptions

Nabla_EventScript_NoLevelCaps:
	clearflag FLAG_NABLA_LEVEL_CAPS
	bufferstring STR_VAR_2, Nabla_Text_Off
Nabla_EventScript_ConfirmGameOptions:
	msgbox Nabla_Text_ConfirmGameOptions, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Nabla_EventScript_ChooseGameOptions
	closemessage
	return
