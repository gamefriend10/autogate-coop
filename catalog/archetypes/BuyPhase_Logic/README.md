OnEnterBuyPhaseTrigger()

// For every active player besides the AI Enemy, Refresh shop
`active_players_minus_enemy_ai_at_slot_5` = PlayerGroup_GetActivePlayers()
PlayerGroup_RemovePlayer(`active_players_minus_enemy_ai_at_slot_5`, 5)
PlayerGroup_ForEachPlayerInGroup(`active_players_minus_enemy_ai_at_slot_5`):
  `GV_PlayerToRefreshFor` = PlayerGroup_GetCurrentPlayer()
  RefreshForPlayer(`GV_PlayerToRefreshFor`)