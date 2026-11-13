NablaPowerPlant_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaPowerPlant_OnTransition
	.byte 0

NablaPowerPlant_OnTransition:
	call Nabla_PowerPlant_EventScript_SetUp
	end
