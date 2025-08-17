# ReadyUp

TODO: Requirements: `GV_CurrentGameState` = "buyState"

## ReadyUp_Trigger

Set triggering player's blackboard `ready` to true
Add 1 to `GV_NumPlayersReady`
UpdateReadyUpObjective_Trigger()
TechTree_SetAbilityAllowed(triggering player, ReadyUp, remove)
TechTree_SetAbilityAllowed(triggering player, UnreadyUp, add)
TODO: If `GV_NumPlayersReady` == number of active players:
  Set `GV_CurrentGameState` to "battleState"
  TriggerRun(OnEnterBattlePhaseTrigger)