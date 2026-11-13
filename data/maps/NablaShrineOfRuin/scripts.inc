NablaShrineOfRuin_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaShrineOfRuin_OnTransition
	.byte 0

NablaShrineOfRuin_OnTransition:
	call Nabla_ShrineOfRuin_EventScript_SetUp
	end
