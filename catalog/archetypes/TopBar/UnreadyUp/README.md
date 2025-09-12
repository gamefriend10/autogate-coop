# UnreadyUp

Requirements: GameStateIsBattleStateDummyUpgrade is not researched

UnreadyUp_Trigger(`GV_PlayerToUnreadyUp`):
  If(
    Blackboard_GetValue_Boolean(
      Blackboard_GetBlackboardOfPlayer(`GV_PlayerToUnreadyUp`),
      "ready"
    ) == false
  ):
    SkipRemainingActions()
  
  Blackboard_SetValue_Boolean(
    Blackboard_GetBlackboardOfPlayer(`GV_PlayerToUnreadyUp`),
    "ready",
    false
  )
  Subtract 1 from `GV_NumPlayersReady`
  UpdateReadyUpObjective_Trigger()
  TechTree_SetAbilityAllowed(`GV_PlayerToUnreadyUp`, ReadyUp, add)
  TechTree_SetAbilityAllowed(`GV_PlayerToUnreadyUp`, UnreadyUp, remove)