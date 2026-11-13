NablaAreaZero_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaAreaZero_OnTransition
	.byte 0

NablaAreaZero_OnTransition:
	call Nabla_AreaZero_EventScript_SetUp
	end
