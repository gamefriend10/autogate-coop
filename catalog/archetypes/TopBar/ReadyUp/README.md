# ReadyUp

Requirements: GameStateIsBattleStateDummyUpgrade is not researched

ReadyUp_Trigger():
  If(
    Blackboard_GetValue_Boolean(
      Blackboard_GetBlackboardOfPlayer(), // defaults to triggering player's
      "ready"
    ) == true
  ):
    SkipRemainingActions()

Set triggering player's blackboard `ready` to true
Add 1 to `GV_NumPlayersReady`
Refresh `GV_NumActivePlayers` (just in case someone leaves)
UpdateReadyUpObjective_Trigger()
TechTree_SetAbilityAllowed(triggering player, ReadyUp, remove)
TechTree_SetAbilityAllowed(triggering player, UnreadyUp, add)
If `GV_NumPlayersReady` == `GV_NumActivePlayers`:
  TriggerRun(OnExitBuyPhaseTrigger())
  General_Wait(2.0)
  TriggerRun(OnEnterBattlePhaseTrigger())