`GV_NumActivePlayers`

Inits to PlayerGroup_CountPlayers(PlayerGroup_GetActivePlayers())

--------------------

`GV_ObjectiveList`

Inits to Objectives_List_Create("Objectives")

--------------------

`GV_ReadyUpObjective`

Inits to Objectives_Objective_Create("Number of Players Ready:", "0")

--------------------

InitReadyUpObjective_Trigger

Objectives_List_AddObjective(`GV_ObjectiveList`, `GV_ReadyUpObjective`)
Objectives_Panel_AddList(`GV_ObjectiveList`)
UpdateReadyUpObjective_Trigger()

--------------------

UpdateReadyUpObjective_Trigger

Objectives_Objective_SetDetails(`GV_ReadyUpObjective`, "`GV_NumPlayersReady` / `GV_NumActivePlayers`")