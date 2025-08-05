# Staging

Staging is laid out as a 3x3 grid with positions as follows:

|      | col0 | col1 | col2 |
|------|------|------|------|
|row2  |  20  |  21  |  22  |
|row1  |  10  |  11  |  12  |
|row0  |  00  |  01  |  02  |

The player blackboard keys should be just the indexes concatted as above e.g. exactly `00` for bottom left.

## GetNearestStagingPositionForPlayerX()

Note: for optimization, not iterating over all points, and just grabbing the first that is <3 units away

Returns: "[row][col]" to be used in player blackboard in GlobalVar: `GV_ClosestStagingPosition`

If (
  Vector_GetDistance(triggeringUnit, PlayerX_StagingPosition00 < 3
) {
  Set `GV_ClosestStagingPosition` = "00"
  General_SkipRemainingActions
}

repeat for all 9...

## AddStagingCoreToPlayerBlackboard(String `GV_ClosestStagingPosition`)

Blackboard_SetValue_Unit(TriggeringPlayer, `GV_ClosestStagingPosition`, TriggeringUnit)