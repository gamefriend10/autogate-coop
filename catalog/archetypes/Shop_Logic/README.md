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
  set `num_shop_positions_to_spawn` = Math_Min(
    2 + Blackboard_GetValue_Integer(
      Blackboard_GetBlackboardOfPlayer(`IV_PickBattleGroupToSpawnForPlayer_Player`),
      "shop_tier"
    ),
    7
  )

  General_ForEachInteger(`i`, 0, `num_shop_positions_to_spawn`-1):
    set `ShopPositionToSpawnAt` = `ShopPositions`[`i`]
    `BattleGroupToSpawnTag` = PickBattleGroupToSpawnForPlayer(`IV_PickBattleGroupToSpawnForPlayer_Player`)
    set `ShopPositionKeyToSaveToBlackboard` = String_Concat("shop_core_at_shop_position_", `i`)
    GeneralShopCoreSpawn(
      `GV_PlayerToSpawnShopCoreFor`,
      `ShopPositionToSpawnAt`,
      `BattleGroupToSpawnTag`,
      `ShopPositionKeyToSaveToBlackboard`
    )