# ReadyUp

Requirements: GameStateIsBattleStateDummyUpgrade is not researched

## ReadyUp_Trigger

Set triggering player's blackboard `ready` to true
Add 1 to `GV_NumPlayersReady`
Refresh `GV_NumActivePlayers` (just in case someone leaves) (active players - 1 AI)
UpdateReadyUpObjective_Trigger()
TechTree_SetAbilityAllowed(triggering player, ReadyUp, remove)
TechTree_SetAbilityAllowed(triggering player, UnreadyUp, add)
If `GV_NumPlayersReady` == `GV_NumActivePlayers`:
  TriggerRun(OnExitBuyPhaseTrigger())
  TriggerRun(OnEnterBattlePhaseTrigger())