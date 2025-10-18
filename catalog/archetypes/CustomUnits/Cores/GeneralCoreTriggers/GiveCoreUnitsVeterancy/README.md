GiveCoreUnitsVeterancy(
  Unit `IV_GiveCoreUnitsVeterancy_Core`,
  Value `IV_GiveCoreUnitsVeterancy_NumXP`
):
  // For every unit in `units`
  UnitGroup_ForEachUnitInGroup(
    Blackboard_GetValue_UnitGroup(
      Blackboard_GetBlackboardOfEntity(`IV_GiveCoreUnitsVeterancy_Core`),
      `units`
    )
  ):
    Unit_AdjustVeterancyXP(
      UnitGroup_GetCurrentUnit(),
      `IV_GiveCoreUnitsVeterancy_NumXP`,
      General_DoDoNot.do_not
    )