`GV_NumActivePlayers`

Inits to PlayerGroup_CountPlayers(PlayerGroup_GetActivePlayers() - 1 AI)

--------------------

`GV_ReadyUp_ObjectiveList`

Inits to Objectives_List_Create("Players Ready")

--------------------

`GV_ReadyUp_Objective`

Inits to Objectives_Objective_Create("Number of Players Ready:", "0")

--------------------

InitReadyUpObjective_Trigger

Objectives_List_AddObjective(`GV_ReadyUp_ObjectiveList`, `GV_ReadyUp_Objective`)
Objectives_Panel_AddList(`GV_ReadyUp_ObjectiveList`)
UpdateReadyUpObjective_Trigger()

--------------------

UpdateReadyUpObjective_Trigger

Objectives_Objective_SetDetails(`GV_ReadyUp_Objective`, "`GV_NumPlayersReady` / `GV_NumActivePlayers`")