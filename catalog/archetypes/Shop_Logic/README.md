# SpawnShop

1. Set input/prereq vars for GeneralShopCoreSpawn
2. run GeneralShopCoreSpawn
3. repeat for all shop positions

# RemoveShopCoreAtPlayerPosition(Player PlayerToRemoveShopCoreFor, String BlackboardKeyForShopCoreShopPosition)

1. Set local var `shop_core_to_remove` to `PlayerToRemoveShopCoreFor`'s blackboard value at `BlackboardKeyForShopCoreShopPosition` e.g. "shop_core_at_shop_position_0"
2. Remove all units in `shop_core_to_remove`'s blackboard `units`
3. Remove `shop_core_to_remove`
4. Repeat for all shop positions...

# RemoveShopCoresForPlayer(Player PlayerToRemoveShopCoreFor)

1. Set `BlackboardKeyForShopCoreShopPosition` to `shop_core_at_shop_position_0`
2. RemoveShopCoreAtPlayerPosition(PlayerToRemoveShopCoreFor, BlackboardKeyForShopCoreShopPosition)
3. Repeat for all shop positions...