# BunkerRush_ShopCore_Spawn

prereqs:
1. `ShopPositionToSpawnAt` is set
2. `ShopPositionKeyToSaveToBlackboard` is set

1. spawn shopCore
2. set player's blackboard `ShopPositionKeyToSaveToBlackboard` to this created shopCore
3. set lastCreatedUnit (this shopCore)'s blackboard `shop_position_key` to `ShopPositionKeyToSaveToBlackboard`

# BunkerRush_Spawn

1. spawn sentry posts
2. add to local var `units_spawned`
3. spawn servos
4. add to local var `units_spawned`
5. add `units_spawned` to triggering shopCore's blackboard `units`
6. add `units_spawned` to global var `UnitsToOrderToBattle`