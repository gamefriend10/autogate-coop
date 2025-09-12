# AutoGateInitialization 

Game_SpawnTopBar(PlayerGroup_GetAllPlayers())
Set camera zoom limit
Set everyone's camera to 100 zoom over 5 secs
InitReadyUpObjective_Trigger()
SpawnHeros()
PlayerGroup_ForEachPlayerInGroup(PlayerGroup_GetActivePlayers()):
  `IV_NumberOfMaxLumToSet` = 3
  `IV_PlayerToSetMaxLumFor` = PlayerGroup_GetCurrentPlayer()
  SetMaxLumForPlayer_Trigger(`IV_NumberOfMaxLumToSet`, `IV_PlayerToSetMaxLumFor`)
OnEnterBuyPhaseTrigger()

# AutoGateInitializationWhenFSMWorks (TODO When state machines work)

Set camera zoom limit
Set everyone's camera to 100 zoom over 5 secs

`autoGateState` = FSM_CreateStateMachine("autoGate")
`buyState` = FSM_CreateStateMachine("buy")
`battleState` = FSM_CreateStateMachine("battle")

FSM_SetInitialSubState(`autoGateState`, `buyState`)
FSM_AddSubState(`autoGateState`, `battleState`)

FSM_AddTransition(`autoGateState`, `buyState`, `battleState`, "go_to_battle")
FSM_AddTransition(`autoGateState`, `battleState`, `buyState`, "go_to_buy")

DISABLED: FSM_SetEnterTrigger(`autoGateState`, OnEnterBattlePhaseTrigger)

DISABLED: FSM_SendSignal(`autoGateState`, "go_to_battle")
