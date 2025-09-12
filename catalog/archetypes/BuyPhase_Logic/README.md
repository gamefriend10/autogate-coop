OnEnterBuyPhaseTrigger():
  `GV_CurrentGameState` = Preset_GameState.buy
  // For every active player besides the AI Enemy, Refresh shop
  `active_players_minus_enemy_ai_at_slot_5` = PlayerGroup_GetActivePlayers()
  PlayerGroup_RemovePlayer(`active_players_minus_enemy_ai_at_slot_5`, 5)
  PlayerGroup_ForEachPlayerInGroup(`active_players_minus_enemy_ai_at_slot_5`):
    TechTree_SetUpgradeLevel(PlayerGroup_GetCurrentPlayer, GameStateIsBattleStateDummyUpgrade, 0) // Allows rdy up
    TODO: add 1 max lum
    TODO: reset everyone's lum
    `GV_PlayerToRefreshFor` = PlayerGroup_GetCurrentPlayer()
    RefreshForPlayer(`GV_PlayerToRefreshFor`)

OnExitBuyPhaseTrigger():
  TODO: do end of buy phase effects
