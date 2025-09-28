# Hand Core

// Note: if you do this twice in less than 0.1s, then only the 2nd units will move bc `HandCoreUnitsToMove` gets overwritten...
// maybe Ability_GetTargetUnitOfTriggeringAbility will give us access to the stagingCore being built.
// Must be on triggering unit.
PrepHandCoreUnitsForStagingAndRemoveHandCore():
  // set `HandCoreUnitsToMove` (tracked by player's blackboard) to this core's `units`
  Blackboard_SetValue_UnitGroup(
    Blackboard_GetBlackboardOfPlayer(),
    "HandCoreUnitsToMove",
    Blackboard_GetValue_UnitGroup(
      Blackboard_GetBlackboardOfEntity(Unit_GetTriggeringUnit()),
      "units"
    )
  )

  set `IV_RemoveHandCoreFromHandPositionInPlayerBlackboard_HandCore` = Unit_GetTriggeringUnit()
  RemoveHandCoreFromHandPositionInPlayerBlackboard(`IV_RemoveHandCoreFromHandPositionInPlayerBlackboard_HandCore`)
  
  Unit_Remove()

--------------------

OnHandCoreAbilityUsed():
  If(Ability_GetTriggeringAbility == HandCore_PassToPlayer1 ||
    Ability_GetTriggeringAbility == HandCore_PassToPlayer2 ||
    Ability_GetTriggeringAbility == HandCore_PassToPlayer3 ||
    Ability_GetTriggeringAbility == HandCore_PassToPlayer4 ||
  ):
    If(Ability_GetTriggeringAbility == HandCore_PassToPlayer1):
      set `IV_Pass_PassHandCoreToPlayer_Player` = 1
    If(Ability_GetTriggeringAbility == HandCore_PassToPlayer2):
      set `IV_Pass_PassHandCoreToPlayer_Player` = 2
    If(Ability_GetTriggeringAbility == HandCore_PassToPlayer3):
      set `IV_Pass_PassHandCoreToPlayer_Player` = 3
    If(Ability_GetTriggeringAbility == HandCore_PassToPlayer4):
      set `IV_Pass_PassHandCoreToPlayer_Player` = 4
    Pass_PassHandCoreToPlayer(`IV_Pass_PassHandCoreToPlayer_Player`)
    SkipRemainingActions()

  // Default to assuming HandCore_Construct was used.
  // Ability_GetTriggeringAbility can't find a value for construct abilities. I suspect this is bc construct abilities have nested constructions.
  PrepHandCoreUnitsForStagingAndRemoveHandCore()