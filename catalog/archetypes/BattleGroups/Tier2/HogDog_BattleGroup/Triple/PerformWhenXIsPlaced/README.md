// When placed, add 2 SCOUTs to all adjacent (diagonal included) Battle Groups.
HogDogTriple_PerformWhenXIsPlaced():
  set `IV_Staging_GetAdjacentStagingCores_Core` = Unit_GetTriggeringUnit()
  `OV_Staging_GetAdjacentStagingCores_Cores` = Staging_GetAdjacentStagingCores(`IV_Staging_GetAdjacentStagingCores_Core`)

  UnitGroup_ForEachUnitInGroup(`OV_Staging_GetAdjacentStagingCores_Cores`):
    Unit_CreateUnit(
      2,
      Scout_Uncommandable,
      Unit_GetOwningPlayer(UnitGroup_GetCurrentUnit()),
      Actor_GetPosition(UnitGroup_GetCurrentUnit()),
      true
    )
    UnitGroup_AddUnits(
      Blackboard_GetValue_UnitGroup(
        Blackboard_GetBlackboardOfEntity(UnitGroup_GetCurrentUnit()),
        `units`
      ),
      UnitGroup_GetLastCreatedUnits()
    )