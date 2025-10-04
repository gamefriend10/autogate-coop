// Local Vars:
//  `row`
//  `col`
//  `core_row`
//  `core_col`
// Returns `OV_Staging_GetAdjacentStagingCores_Cores`
Staging_GetAdjacentStagingCores(Unit `IV_Staging_GetAdjacentStagingCores_Core`):
  UnitGroup_Clear(`OV_Staging_GetAdjacentStagingCores_Cores`)
  `core_row` = Blackboard_GetValue_Integer(
    Blackboard_GetBlackboardOfEntity(`IV_Staging_GetAdjacentStagingCores_Core`),
    "row"
  )
  `core_col` = Blackboard_GetValue_Integer(
    Blackboard_GetBlackboardOfEntity(`IV_Staging_GetAdjacentStagingCores_Core`),
    "col"
  )
  `player` = Unit_GetOwningPlayer(`IV_Staging_GetAdjacentStagingCores_Core`)
  General_ForEachInteger(`row`, `core_row`-1, `core_row`+1):
    If(`row` < 0 || `row` > 2):
      General_Continue()
    General_ForEachInteger(`col`, `core_col`-1, `core_col`+1):
      If(`col` < 0 || `col` > 2):
        General_Continue()
      If(`row` == `core_row` && `col` == `core_col`):
        General_Continue()
      UnitGroup_AddUnit(
        `OV_Staging_GetAdjacentStagingCores_Cores`,
        Blackboard_GetValue_Unit( // `player`'s blackboard[[`row`][`col`]] stagingCore
          Blackboard_GetBlackboardOfPlayer(`player`),
          String_Concat(`row`, `col`)
        )
      )
  <!-- print(UnitGroup_CountUnits(`OV_Staging_GetAdjacentStagingCores_Cores`)) -->
  <!-- UnitGroup_ForEachUnitInGroup(`OV_PlayerStagingCoresAsUnitGroup`):
    print(Unit_GetPlacedName(UnitGroup_GetCurrentUnit)) -->
