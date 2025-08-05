# AutoGateInitialization TODO

`autoGateState` = FSM_CreateStateMachine("autoGate")
`buyState` = FSM_CreateStateMachine("buy")
`battleState` = FSM_CreateStateMachine("battle")

FSM_SetInitialSubState(`autoGateState`, `buyState`)
FSM_AddSubState(`autoGateState`, `battleState`)

FSM_AddTransition(`autoGateState`, `buyState`, `battleState`, "go_to_battle")
FSM_AddTransition(`autoGateState`, `battleState`, `buyState`, "go_to_buy")

FSM_SetEnterTrigger(`autoGateState`, OnEnterBattlePhaseTrigger)

FSM_SendSignal(`autoGateState`, "go_to_battle")
