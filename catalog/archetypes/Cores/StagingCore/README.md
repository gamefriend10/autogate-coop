# StagingCoreBirthTrigger

Trigger: stagingCore is birthed (expected to be from the HandCore constructing into the StagingCore)

1. Wait for 0.1 seconds, because this trigger seems to run in parallel with HandCoreBuildTrigger and `HandCoreUnitsToMove` could be empty or the prev value
2. set stagingCore's `units` (tracked by blackboard) to `HandCoreUnitsToMove` (tracked by player's blackboard)
3. move stagingCore's `units` (tracked by blackboard) to Actor's current position

# StagingCoreAbilityUsedTrigger

Trigger: stagingCore uses an ability

1. if ability is Sell
  1. delete stagingCore's `units` (tracked by blackboard)
