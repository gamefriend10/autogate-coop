// "Dog Soldiers": Convert all SCOUTs in a Staging Battle Group into Exos (can be used on allies).
// Note: assumes topbar checks for Ability_GetTriggeringAbility == DogSoldiers
PerformRykerHeroPowerActive():
  UnitGroup_ForEachUnitInGroup(
    Blackboard_GetValue_UnitGroup(
      Blackboard_GetBlackboardOfEntity(Ability_GetTargetUnitOfTriggeringAbility()),
      `units`
    )
  ):
    If(Unit_GetType(UnitGroup_GetCurrentUnit()) == Scout_Uncommandable):
      Unit_CreateUnit(
        1,
        Gunner_Autogate,
        Unit_GetOwningPlayer(Ability_GetTargetUnitOfTriggeringAbility()),
        Actor_GetPosition(Ability_GetTargetUnitOfTriggeringAbility()),
        true
      )
      Unit_SetVeterancyTier(
        Unit_GetLastCreatedUnit,
        Unit_GetVeterancyTier(UnitGroup_GetCurrentUnit)
        General_DoDoNot.do_not
      )
      UnitGroup_AddUnit(
        Blackboard_GetValue_UnitGroup(
          Blackboard_GetBlackboardOfEntity(Ability_GetTargetUnitOfTriggeringAbility()),
          `units`
        )
      )
      Unit_Remove(UnitGroup_GetCurrentUnit())

  