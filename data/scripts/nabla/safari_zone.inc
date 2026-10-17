@ Nabla's Safari Zone: each visit explores one region (see include/constants/nabla.h).
@ Only Kanto is available for now; unlocking the other regions comes in a later step.
Nabla_EventScript_SafariZoneChooseRegion::
	setvar VAR_NABLA_SAFARI_REGION, NABLA_SAFARI_REGION_KANTO
	bufferstring STR_VAR_1, Nabla_Text_SafariZoneRegionKanto
	return
