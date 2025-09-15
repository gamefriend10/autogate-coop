// Note: if you build 2 in less than 0.1s, then only the 2nd units will move... maybe Ability_GetTargetUnitOfTriggeringAbility will give us access to the stagingCore being built
// Trigger: HandCore uses an ability (expected to be building the StagingCore)
HandCoreBuildTrigger():
  set `HandCoreUnitsToMove` (tracked by player's blackboard)

  `IV_RemoveHandCoreFromHandPositionInPlayerBlackboard_HandCore` = Unit_GetTriggeringUnit()
  RemoveHandCoreFromHandPositionInPlayerBlackboard(`IV_RemoveHandCoreFromHandPositionInPlayerBlackboard_HandCore`)
  
  rm HandCore
