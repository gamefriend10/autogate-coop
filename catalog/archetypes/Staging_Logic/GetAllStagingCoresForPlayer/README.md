// Returns `OV_PlayerStagingCoresAsUnitGroup`
GetAllStagingCoresForPlayer(`IV_PlayerToGetStagingCoresFor`):
  row = 0
  col = 0
  General_ForEachInteger(row, 0, 2):
    General_ForEachInteger(col, 0, 2):
      UnitGroup_AddUnit(
        `OV_PlayerStagingCoresAsUnitGroup`,
        player `IV_PlayerToGetStagingCoresFor` 's blackboard[[row][col]] stagingCore
      )
  <!-- UnitGroup_ForEachUnitInGroup(`OV_PlayerStagingCoresAsUnitGroup`):
    print(Unit_GetPlacedName(UnitGroup_GetCurrentUnit)) -->
