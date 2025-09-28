RemoveShopCoreAtPlayerPosition(
  Player PlayerToRemoveShopCoreFor,
  String BlackboardKeyForShopCoreShopPosition
):

1. Set local var `shop_core_to_remove` to `PlayerToRemoveShopCoreFor`'s blackboard value at `BlackboardKeyForShopCoreShopPosition` e.g. "shop_core_at_shop_position_0"
2. Remove all units in `shop_core_to_remove`'s blackboard `units`
3. Remove `shop_core_to_remove`

---

RemoveShopCoresForPlayer(Player PlayerToRemoveShopCoreFor):

1. Set `BlackboardKeyForShopCoreShopPosition` to `shop_core_at_shop_position_0`
2. RemoveShopCoreAtPlayerPosition(PlayerToRemoveShopCoreFor, BlackboardKeyForShopCoreShopPosition)
3. Repeat for all shop positions...

---

SpawnShop(`GV_PlayerToSpawnShopFor`, `ShopPositions`):
  set `GV_PlayerToSpawnShopCoreFor` = `GV_PlayerToSpawnShopFor`
  set `IV_PickBattleGroupToSpawnForPlayer_Player` = `GV_PlayerToSpawnShopFor`

  // repeat for all shop positions 0-2...
  // TODO: increase # of positions when tiered up
  set `ShopPositionToSpawnAt` = `ShopPositions`[0]

  `BattleGroupToSpawnTag` = PickBattleGroupToSpawnForPlayer(`IV_PickBattleGroupToSpawnForPlayer_Player`)

  set `ShopPositionKeyToSaveToBlackboard` = "shop_core_at_shop_position_0"
  GeneralShopCoreSpawn(
    `GV_PlayerToSpawnShopCoreFor`,
    `ShopPositionToSpawnAt`,
    `BattleGroupToSpawnTag`,
    `ShopPositionKeyToSaveToBlackboard`
  )