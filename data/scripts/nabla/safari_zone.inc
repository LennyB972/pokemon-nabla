@ Nabla's Safari Zone: each visit explores one region (see include/constants/nabla.h and src/nabla_safari_zone.c).
@ Kanto is always open; the other regions are unlocked at the counter, in any order, and the
@ special zones too after the League.
@ Sets VAR_NABLA_SAFARI_REGION to the chosen region and buffers its name in STR_VAR_1,
@ or sets it to NABLA_SAFARI_REGION_NONE if the player cancels.
Nabla_EventScript_SafariZoneChooseRegion::
	message Nabla_Text_SafariZoneWelcome
	goto Nabla_EventScript_SafariZoneRegionMenu

Nabla_EventScript_SafariZoneRegionMenuAgain:
	message Nabla_Text_SafariZoneWhichRegion
Nabla_EventScript_SafariZoneRegionMenu:
	waitmessage
	setvar VAR_0x8004, FALSE
	special NablaSafariZone_PushRegions
	specialvar VAR_RESULT, NablaSafariZone_CountRegionsForSale
	goto_if_eq VAR_RESULT, 0, Nabla_EventScript_SafariZoneShowRegionMenu
	dynmultipush Nabla_Text_SafariZoneUnlockARegion, NABLA_SAFARI_MENU_UNLOCK
Nabla_EventScript_SafariZoneShowRegionMenu:
	dynmultipush gText_Cancel, NABLA_SAFARI_MENU_CANCEL
	dynmultistack 28, 1, FALSE, 6, FALSE, 0, DYN_MULTICHOICE_CB_NONE
	switch VAR_RESULT
	case NABLA_SAFARI_MENU_UNLOCK, Nabla_EventScript_SafariZoneUnlockMenu
	case NABLA_SAFARI_MENU_CANCEL, Nabla_EventScript_SafariZoneCancel
	case MULTI_B_PRESSED, Nabla_EventScript_SafariZoneCancel
	copyvar VAR_NABLA_SAFARI_REGION, VAR_RESULT
	copyvar VAR_0x8005, VAR_RESULT
	special NablaSafariZone_BufferRegionName
	return

Nabla_EventScript_SafariZoneCancel:
	setvar VAR_NABLA_SAFARI_REGION, NABLA_SAFARI_REGION_NONE
	return

@ Stays on the regions left to unlock, so several can be bought in a row. B goes back to the region menu.
Nabla_EventScript_SafariZoneUnlockMenu:
	message Nabla_Text_SafariZoneWhichRegionToUnlock
	waitmessage
	setvar VAR_0x8004, TRUE
	special NablaSafariZone_PushRegions
	dynmultipush gText_Cancel, NABLA_SAFARI_MENU_CANCEL
	dynmultistack 28, 1, FALSE, 6, FALSE, 0, DYN_MULTICHOICE_CB_NONE
	goto_if_eq VAR_RESULT, NABLA_SAFARI_MENU_CANCEL, Nabla_EventScript_SafariZoneRegionMenuAgain
	goto_if_eq VAR_RESULT, MULTI_B_PRESSED, Nabla_EventScript_SafariZoneRegionMenuAgain
	copyvar VAR_0x8005, VAR_RESULT
	special NablaSafariZone_BufferRegionName
	msgbox Nabla_Text_SafariZoneConfirmUnlock, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Nabla_EventScript_SafariZoneUnlockMenu
	specialvar VAR_RESULT, NablaSafariZone_TryBuyRegion
	goto_if_eq VAR_RESULT, FALSE, Nabla_EventScript_SafariZoneNotEnoughMoney
	updatemoneybox
	playse SE_SHOP
	msgbox Nabla_Text_SafariZoneRegionUnlocked, MSGBOX_DEFAULT
	specialvar VAR_RESULT, NablaSafariZone_CountRegionsForSale
	goto_if_eq VAR_RESULT, 0, Nabla_EventScript_SafariZoneRegionMenuAgain
	goto Nabla_EventScript_SafariZoneUnlockMenu

Nabla_EventScript_SafariZoneNotEnoughMoney:
	msgbox Route121_SafariZoneEntrance_Text_NotEnoughMoney, MSGBOX_DEFAULT
	goto Nabla_EventScript_SafariZoneUnlockMenu
