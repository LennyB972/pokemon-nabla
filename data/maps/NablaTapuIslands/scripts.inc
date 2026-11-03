NablaTapuIslands_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaTapuIslands_OnTransition
	.byte 0

NablaTapuIslands_OnTransition:
	call Nabla_TapuIslands_EventScript_SetUp
	end
