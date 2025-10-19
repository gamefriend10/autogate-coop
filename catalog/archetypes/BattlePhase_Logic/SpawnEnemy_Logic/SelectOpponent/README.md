// Condition:
//  Entity_HasAllTags(attribute_topbar) AND
//  (
//    Ability_GetTriggeringAbility == SelectMajorGaltEasy OR
//    Ability_GetTriggeringAbility == SelectMajorGaltHard
//  )
// Trigger: Unit_OnAbilityUsed()
SelectOpponent():
  Switch(Ability_GetTriggeringAbility):
    Case SelectMajorGaltEasy:
      Set `GV_Opponent` = MajorGaltEasy
    Case SelectMajorGaltHard:
      Set `GV_Opponent` = MajorGaltHard

  TechTree_SetUpgradeLevel(1, OpponentSelectedDummyUpgrade, 1) // Blocks opponent select
  TechTree_SetUpgradeLevel(2, OpponentSelectedDummyUpgrade, 1) // Blocks opponent select
  TechTree_SetUpgradeLevel(3, OpponentSelectedDummyUpgrade, 1) // Blocks opponent select
  TechTree_SetUpgradeLevel(4, OpponentSelectedDummyUpgrade, 1) // Blocks opponent select