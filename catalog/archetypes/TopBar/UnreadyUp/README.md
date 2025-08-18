# UnreadyUp

Requirements: GameStateIsBattleStateDummyUpgrade is not researched

## UnreadyUp_Trigger

Set triggering player's blackboard `ready` to false
Subtract 1 from `GV_NumPlayersReady`
UpdateReadyUpObjective_Trigger()
TechTree_SetAbilityAllowed(triggering player, ReadyUp, add)
TechTree_SetAbilityAllowed(triggering player, UnreadyUp, remove)