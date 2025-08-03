# GetNearestStagingPositionForPlayerX()

Note: for optimization, not iterating over all points, and just grabbing the first that is <3 units away

Returns: "staging_position_X" to be used in player blackboard in GlobalVar: `GV_ClosestStagingPosition`

If (
  Vector_GetDistance(triggeringUnit, PlayerX_StagingPosition1 < 3
) {
  Set `GV_ClosestStagingPosition` = "staging_position_0"
  General_SkipRemainingActions
}

repeat for all 9...

# AddStagingCoreToPlayerBlackboard(String `GV_ClosestStagingPosition`)

1. switch(`GV_ClosestStagingPosition`)
  1. case "staging_position_1": set playerBlackboard `staging_core_at_staging_position_1` to triggeringUnit
  2. repeat for "staging_position_2-8" `staging_core_at_staging_position_2-8`... 
  3. default: set playerBlackboard `staging_core_at_staging_position_0` to triggeringUnit