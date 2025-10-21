// Note: `IV_REUSABLE_PerformEndOfBuyPhase_StagingCore` is reused across all PerformEndOfBuyPhase's
// Note: every PerformEndOfBuyPhase should have a condition in it to check for its type
BuyPhase_PerformEndOfBuyPhase():
  PlayerGroup_ForEachPlayerInGroup(PlayerGroup_GetActivePlayers()):
    set `IV_PlayerToGetStagingCoresFor` = PlayerGroup_GetCurrentPlayer()
    `OV_PlayerStagingCoresAsUnitGroup` = GetAllStagingCoresForPlayer(`IV_PlayerToGetStagingCoresFor`)
    UnitGroup_ForEachUnitInGroup(`OV_PlayerStagingCoresAsUnitGroup`):
      set `IV_REUSABLE_PerformEndOfBuyPhase_StagingCore` = UnitGroup_GetCurrentUnit()
      If(Entity_HasAllTags(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`, loveletter_snowtag)):
        LoveLetter_PerformEndOfBuyPhase(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`)
        General_Continue()
      If(Entity_HasAllTags(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`, lovelettertriple_snowtag)):
        LoveLetterTriple_PerformEndOfBuyPhase(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`)
        General_Continue()
      If(Entity_HasAllTags(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`, bedtech_snowtag)):
        BedTech_PerformEndOfBuyPhase(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`)
        General_Continue()
      If(Entity_HasAllTags(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`, bedtechtriple_snowtag)):
        BedTechTriple_PerformEndOfBuyPhase(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`)
        General_Continue()
      If(Entity_HasAllTags(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`, sdfvanguard_snowtag)):
        SDFVanguard_PerformEndOfBuyPhase(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`)
        General_Continue()
      If(Entity_HasAllTags(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`, sdfvanguardtriple_snowtag)):
        SDFVanguard_PerformEndOfBuyPhase(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`) // Reusing the non-triple func
        SDFVanguard_PerformEndOfBuyPhase(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`)
        General_Continue()
      If(Entity_HasAllTags(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`, blockhead_snowtag)):
        Blockhead_PerformEndOfBuyPhase(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`)
        General_Continue()
      If(Entity_HasAllTags(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`, blockheadtriple_snowtag)):
        BlockheadTriple_PerformEndOfBuyPhase(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`)
        General_Continue()