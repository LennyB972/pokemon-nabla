NablaKalosSanctuary_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaKalosSanctuary_OnTransition
	.byte 0

NablaKalosSanctuary_OnTransition:
	call Nabla_KalosSanctuary_EventScript_SetUp
	end
