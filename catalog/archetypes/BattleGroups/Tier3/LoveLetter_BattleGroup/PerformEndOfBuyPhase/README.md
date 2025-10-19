// End of Buy Phase: If adjacent to (diagonal included)
// at least 2 Vanguard Battle Groups, add 1 Exos to
// this Battle Group.
LoveLetter_PerformEndOfBuyPhase(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`):
  set `IV_Staging_GetAdjacentStagingCores_Core` = `IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`
  `OV_Staging_GetAdjacentStagingCores_Cores` = Staging_GetAdjacentStagingCores(`IV_Staging_GetAdjacentStagingCores_Core`)

  set `IV_General_GetNumberOfUnitsWithTag_Units` = `OV_Staging_GetAdjacentStagingCores_Cores`
  set `IV_General_GetNumberOfUnitsWithTag_Tag` = vanguard_snowtag
  `OV_General_GetNumberOfUnitsWithTag_Num` = General_GetNumberOfUnitsWithTag(
    `IV_General_GetNumberOfUnitsWithTag_Units`,
    `IV_General_GetNumberOfUnitsWithTag_Tag`
  )

  if `OV_General_GetNumberOfUnitsWithTag_Num` >= 2:
    Unit_CreateUnit(
      1,
      Exo,
      Unit_GetOwningPlayer(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`),
      Actor_GetPosition(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`),
      true
    )
    UnitGroup_AddUnits(
      Blackboard_GetValue_UnitGroup(
        Blackboard_GetBlackboardOfEntity(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`),
        `units`
      ),
      UnitGroup_GetLastCreatedUnits()
    )
