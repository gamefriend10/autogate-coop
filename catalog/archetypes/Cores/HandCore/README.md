# HandCoreBuildTrigger

Trigger: HandCore uses an ability (expected to be building the StagingCore)

Note: if you build 2 in less than 0.1s, then only the 2nd units will move... maybe Ability_GetTargetUnitOfTriggeringAbility will give us access to the stagingCore being built

1. set `HandCoreUnitsToMove` (tracked by player's blackboard)
2. RemoveHandCoreFromHandPositionInPlayerBlackboard()
3. rm HandCore
