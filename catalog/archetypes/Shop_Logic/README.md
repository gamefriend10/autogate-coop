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
  Set `GV_PlayerToSpawnShopCoreFor` = `GV_PlayerToSpawnShopFor`
  Set `IV_DetermineBattleGroupMaxIndex_Tier` = Blackboard_GetValue_Integer(
    Blackboard_GetBlackboardOfPlayer(`GV_PlayerToSpawnShopFor`),
    "shop_tier"
  )
  Set `num_shop_positions_to_spawn` = Math_Min(
    2 + `IV_DetermineBattleGroupMaxIndex_Tier`,
    7
  )
  `GV_DetermineBattleGroupMaxIndex_Index` = DetermineBattleGroupMaxIndex(`IV_DetermineBattleGroupMaxIndex_Tier`)
  General_ForEachInteger(`i`, 0, `num_shop_positions_to_spawn`-1):
    Set `ShopPositionToSpawnAt` = `ShopPositions`[`i`]
    `BattleGroupToSpawnTag` = PickBattleGroupToSpawnForPlayer(`GV_DetermineBattleGroupMaxIndex_Index`)
    set `ShopPositionKeyToSaveToBlackboard` = String_Concat("shop_core_at_shop_position_", `i`)
    GeneralShopCoreSpawn(
      `GV_PlayerToSpawnShopCoreFor`,
      `ShopPositionToSpawnAt`,
      `BattleGroupToSpawnTag`,
      `ShopPositionKeyToSaveToBlackboard`
    )