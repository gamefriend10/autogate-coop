OnEnterBuyPhaseTrigger():
  `GV_CurrentGameState` = Preset_GameState.buy
  // For every active player besides the AI Enemy, Refresh shop
  `active_players_minus_enemy_ai_at_slot_5` = PlayerGroup_GetActivePlayers()
  PlayerGroup_RemovePlayer(`active_players_minus_enemy_ai_at_slot_5`, 5)
  PlayerGroup_ForEachPlayerInGroup(`active_players_minus_enemy_ai_at_slot_5`):
    TechTree_SetUpgradeLevel(PlayerGroup_GetCurrentPlayer, GameStateIsBattleStateDummyUpgrade, 0) // Allows top bar

    `GV_PlayerToUnreadyUp` = PlayerGroup_GetCurrentPlayer()
    UnreadyUp_Trigger(`GV_PlayerToUnreadyUp`)
    
    `IV_PlayerToResetLumFor` = PlayerGroup_GetCurrentPlayer()
    ResetPlayerLumToTheirMax(`IV_PlayerToResetLumFor`)

    `GV_PlayerToRefreshFor` = PlayerGroup_GetCurrentPlayer()
    RefreshForPlayer(`GV_PlayerToRefreshFor`)

OnExitBuyPhaseTrigger():
  BuyPhase_PerformEndOfBuyPhase()
