// End of Buy Phase: Convert 5 Exos into an Exo5.
// Note: also handles sdfvanguard triple
SDFVanguard_PerformEndOfBuyPhase(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`):
  Set `count` = 0
  Set `exos` = UnitGroup_GetNewUnitGroup()
  Set `total_exp` = 0
  UnitGroup_ForEachUnitInGroup(
    Blackboard_GetValue_UnitGroup(
      Blackboard_GetBlackboardOfEntity(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`),
      `units`
    )
  ):
    If(Unit_GetType(UnitGroup_GetCurrentUnit()) == Gunner_Autogate):
      `count` += 1
      UnitGroup_AddUnit(`exos`, UnitGroup_GetCurrentUnit())
      `total_exp` += Unit_GetVeterancyTier(UnitGroup_GetCurrentUnit)
    If(`count` == 5):
      General_Break

  If(`count` == 5):
    Unit_CreateUnit(
      1,
      Exo5,
      Unit_GetOwningPlayer(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`),
      Actor_GetPosition(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`),
      true
    )
    Unit_SetVeterancyTier(
      Unit_GetLastCreatedUnit,
      `total_exp` / 5
      General_DoDoNot.do_not
    )
    UnitGroup_AddUnit(
      Blackboard_GetValue_UnitGroup(
        Blackboard_GetBlackboardOfEntity(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`),
        `units`
      )
    )
    UnitGroup_ForEachUnitInGroup(`exos`):
      Unit_Remove(UnitGroup_GetCurrentUnit())