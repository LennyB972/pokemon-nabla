NablaPinwheelForest_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, NablaPinwheelForest_OnTransition
	.byte 0

NablaPinwheelForest_OnTransition:
	call Nabla_PinwheelForest_EventScript_SetUp
	end
