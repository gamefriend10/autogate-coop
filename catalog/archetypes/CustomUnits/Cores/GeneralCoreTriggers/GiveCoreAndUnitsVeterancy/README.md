GiveCoreAndUnitsVeterancy(
  Unit `IV_GiveCoreAndUnitsVeterancy_Core`,
  Value `IV_GiveCoreAndUnitsVeterancy_NumXP`
):
  Unit_AdjustVeterancyXP(
    `IV_GiveCoreAndUnitsVeterancy_Core`,
    `IV_GiveCoreAndUnitsVeterancy_NumXP`,
    General_DoDoNot.do_not
  )
  
  // For every unit in `units`
  UnitGroup_ForEachUnitInGroup(
    Blackboard_GetValue_UnitGroup(
      Blackboard_GetBlackboardOfEntity(`IV_GiveCoreAndUnitsVeterancy_Core`),
      `units`
    )
  ):
    Unit_AdjustVeterancyXP(
      UnitGroup_GetCurrentUnit(),
      `IV_GiveCoreAndUnitsVeterancy_NumXP`,
      General_DoDoNot.do_not
    )