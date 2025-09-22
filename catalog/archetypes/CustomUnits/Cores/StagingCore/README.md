StagingCoreBirthTrigger

Trigger: stagingCore is birthed (expected to be from the HandCore constructing into the StagingCore)

// Wait for 0.1 seconds, because this trigger seems to run in parallel with OnHandCoreAbilityUsed and `HandCoreUnitsToMove` could be empty or the prev value
// set stagingCore's `units` (tracked by blackboard) to `HandCoreUnitsToMove` (tracked by player's blackboard)
// move stagingCore's `units` (tracked by blackboard) to Actor's current position
// `GV_ClosestStagingPosition` = GetNearestStagingPositionForTriggeringPlayer()
// AddStagingCoreToPlayerBlackboard(`GV_ClosestStagingPosition`)

--------------------

StagingCoreAbilityUsedTrigger

Trigger: stagingCore uses an ability

// if ability is Sell OR SellFor2
  // delete stagingCore's `units` (tracked by blackboard)
