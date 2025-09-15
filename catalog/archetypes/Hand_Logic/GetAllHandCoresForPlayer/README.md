TODO
// Returns `OV_PlayerHandCoresAsUnitGroup`
GetAllHandCoresForPlayer(`IV_GetAllHandCoresForPlayer_Player`):
  row = 0
  col = 0
  General_ForEachInteger(row, 0, 2):
    General_ForEachInteger(col, 0, 2):
      UnitGroup_AddUnit(
        `OV_PlayerHandCoresAsUnitGroup`,
        player `IV_GetAllHandCoresForPlayer_Player` 's blackboard[[row][col]] stagingCore
      )
