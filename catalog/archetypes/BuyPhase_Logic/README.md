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

    // Pan cameras to shop
    Switch(PlayerGroup_GetCurrentPlayer):
      Case 1: `pos` = Actor_GetPosition(Point_GetPointFromPlacedName("Player1_ShopCameraPosition"))
      Case 2: `pos` = Actor_GetPosition(Point_GetPointFromPlacedName("Player2_ShopCameraPosition"))
      Case 3: `pos` = Actor_GetPosition(Point_GetPointFromPlacedName("Player3_ShopCameraPosition"))
      Case 4: `pos` = Actor_GetPosition(Point_GetPointFromPlacedName("Player4_ShopCameraPosition"))
    Camera_PanCameraToLocation(
      PlayerGroup_GetCurrentPlayer,
      `pos`,
      0.5
    )

OnExitBuyPhaseTrigger():
  PlayerGroup_ForEachPlayerInGroup(PlayerGroup_GetActivePlayers()):
    TechTree_SetUpgradeLevel(PlayerGroup_GetCurrentPlayer, GameStateIsBattleStateDummyUpgrade, 1) // Stops top bar
  BuyPhase_PerformEndOfBuyPhase()
