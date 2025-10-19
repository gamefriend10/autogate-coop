# Heros_Logic

## Adding a hero

1. copy/paste an old hero
2. add to SpawnHeros()
3. add to ShopTopBarCaster
4. add to AutoGateFaction

// Condition: Entity_HasAllTags(attribute_topbar)
// Trigger: Unit_OnAbilityUsed()
SpawnHeros():
  Set `player` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())

  Switch(`player`):
    Case 1: Set `pos` = Actor_GetPosition(
      Point_GetPointFromPlacedName(Player1_HeroSpawnPoint)
    )
    Case 2: Set `pos` = Actor_GetPosition(
      Point_GetPointFromPlacedName(Player2_HeroSpawnPoint)
    )
    Case 3: Set `pos` = Actor_GetPosition(
      Point_GetPointFromPlacedName(Player3_HeroSpawnPoint)
    )
    Case 4: Set `pos` = Actor_GetPosition(
      Point_GetPointFromPlacedName(Player4_HeroSpawnPoint)
    )

  Switch(Ability_GetTriggeringAbility):
    Case SpawnRykerHero:
      CreateUnit(1, RykerHeroUnit_Autogate, `player`, `pos`)
    Case SpawnBlockadeHero:
      CreateUnit(1, BlockadeUnit_Uncommandable, `player`, `pos`)

  UnitGroup_AddUnit(`GV_Heros_UnitGroup`)

  TechTree_SetUpgradeLevel(`player`, HeroSelectedDummyUpgrade, 1) // Blocks hero select