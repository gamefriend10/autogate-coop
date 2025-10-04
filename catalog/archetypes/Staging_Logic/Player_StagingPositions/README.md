// Note: for optimization, not iterating over all points, and just grabbing the first that is <3 units awayString
// Returns:
//  String `GV_ClosestStagingPosition` `row`+`col` e.g.  "00"
//  Integer `OV_GetNearestStagingPositionForTriggeringPlayer_Row`
//  Integer `OV_GetNearestStagingPositionForTriggeringPlayer_Col`
GetNearestStagingPositionForTriggeringPlayer():
  `player_number_as_string` = String_Concat(
    "Player",
    String_ToString(Unit_GetOwningPlayer(Unit_GetTriggeringUnit()))
  )
  `triggering_unit_pos` = Actor_GetPosition(Unit_GetTriggeringUnit())
  `row` = 0
  `col` = 0

  General_ForEachInteger(`row`, 0, 2):
    General_ForEachInteger(`col`, 0, 2):
      `rowcol` = String_Concat(
        `row`,
        `col`
      )
      // `placed_name_of_position` e.g. Player1_StagingPosition00
      `placed_name_of_position` = String_Concat(
        `player_number_as_string`,
        "_StagingPosition",
        `rowcol`
      )
      If (
        Vector_GetDistance(
          `triggering_unit_pos`,
          Actor_GetPosition(Point_GetPointFromPlacedName(`placed_name_of_position`))
        ) < `GV_AcceptableDistanceFromPosition`
      ) {
        `GV_ClosestStagingPosition` = `rowcol`
        `OV_GetNearestStagingPositionForTriggeringPlayer_Row` = `row`
        `OV_GetNearestStagingPositionForTriggeringPlayer_Col` = `col`
        General_SkipRemainingActions()
      }
