StagingCoreBirthTrigger

Trigger: stagingCore is birthed (expected to be from the HandCore constructing into the StagingCore)

// Wait for 0.1 seconds, because this trigger seems to run in parallel with OnHandCoreAbilityUsed and `HandCoreUnitsToMove` could be empty or the prev value
// set stagingCore's `units` (tracked by blackboard) to `HandCoreUnitsToMove` (tracked by player's blackboard)
// move stagingCore's `units` (tracked by blackboard) to Actor's current position

// Copy buffs from HandCoreBuffDummyToCopy (tracked by player's blackboard)
`buff_dummy` = Blackboard_GetValue_Unit(
  Blackboard_GetBlackboardOfPlayer(),
  "HandCoreBuffDummyToCopy"
)
Actor_CopyBuffsFromActor(
  Unit_GetTriggeringUnit(),
  `buff_dummy`
)
Unit_Remove(`buff_dummy`)

(
  `GV_ClosestStagingPosition`,
  `OV_GetNearestStagingPositionForTriggeringPlayer_Row`,
  `OV_GetNearestStagingPositionForTriggeringPlayer_Col`
)
  = GetNearestStagingPositionForTriggeringPlayer()

// AddStagingCoreToPlayerBlackboard(`GV_ClosestStagingPosition`)

// Set position coords of core to that position in its blackboard
Blackboard_SetValue_Integer(
  Blackboard_GetBlackboardOfEntity(Unit_GetTriggeringUnit()),
  "row",
  `OV_GetNearestStagingPositionForTriggeringPlayer_Row`
)
Blackboard_SetValue_Integer(
  Blackboard_GetBlackboardOfEntity(Unit_GetTriggeringUnit()),
  "col",
  `OV_GetNearestStagingPositionForTriggeringPlayer_Col`
)

Trigger_Run(Triple_PickAndAddRandomNextTierBattleGroupToHand)

Trigger_Run(PerformWhenXIsPlaced)

--------------------

StagingCoreAbilityUsedTrigger

Trigger: stagingCore uses an ability

// if ability is Sell OR SellFor2 OR SellFor4
  // delete stagingCore's `units` (tracked by blackboard)
