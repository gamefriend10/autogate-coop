GeneralShopCoreSpawn(
  `GV_PlayerToSpawnShopCoreFor`,
  `ShopPositionToSpawnAt`,
  `BattleGroupToSpawnTag`,
  `ShopPositionKeyToSaveToBlackboard`
):

LONG if-then-else that determines which ShopCore BattleGroup to spawn

TODO: switch this over to switch case

If(`BattleGroupToSpawnTag` == hogdog_snowtag):
  `GV_ShopCoreToSpawn` = HogDog_ShopCore
If ... etc
ShopCore_Spawn(`GV_ShopCoreToSpawn`, `GV_PlayerToSpawnShopCoreFor`, `ShopPositionToSpawnAt`, `ShopPositionKeyToSaveToBlackboard`)

---

GeneralSpawnUnitsOnShopCoreSpawn

Trigger: On ShopCore being birthed

Set `ShopPositionToSpawnAt` to triggering ShopCore
If (triggering unit, shop core) has tag = E.g. HogDog (Entity_HasAllTags)
  Then run E.g. HogDogSpawn trigger
If (triggering unit, shop core) has tag... etc
