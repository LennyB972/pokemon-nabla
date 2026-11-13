NablaCrownTundra_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaCrownTundra_OnTransition
	.byte 0

NablaCrownTundra_OnTransition:
	call Nabla_CrownTundra_EventScript_SetUp
	end
