// Note: `IV_REUSABLE_PerformEndOfBuyPhase_StagingCore` is reused across all PerformEndOfBuyPhase's
// Note: every PerformEndOfBuyPhase should have a condition in it to check for its type
BuyPhase_PerformEndOfBuyPhase():
  PlayerGroup_ForEachPlayerInGroup(PlayerGroup_GetActivePlayers()):
    set `IV_PlayerToGetStagingCoresFor` = PlayerGroup_GetCurrentPlayer()
    `OV_PlayerStagingCoresAsUnitGroup` = GetAllStagingCoresForPlayer(`IV_PlayerToGetStagingCoresFor`)
    UnitGroup_ForEachUnitInGroup(`OV_PlayerStagingCoresAsUnitGroup`):
      set `IV_REUSABLE_PerformEndOfBuyPhase_StagingCore` = UnitGroup_GetCurrentUnit()
      LoveLetter_PerformEndOfBuyPhase(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`)
      LoveLetterTriple_PerformEndOfBuyPhase(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`)