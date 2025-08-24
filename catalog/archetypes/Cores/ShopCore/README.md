ShopCore_Spawn(`GV_ShopCoreToSpawn`, `GV_PlayerToSpawnShopCoreFor`, `ShopPositionToSpawnAt`, `ShopPositionKeyToSaveToBlackboard`):

// Creates shop core
Unit_CreateUnit(1, `GV_ShopCoreToSpawn`, `GV_PlayerToSpawnShopCoreFor`, `ShopPositionToSpawnAt`, true)
// Assigns shop core to player's blackboard
Blackboard_SetValue_Unit(
  Blackboard_GetBlackboardOfPlayer(`GV_PlayerToSpawnShopCoreFor`),
  `ShopPositionKeyToSaveToBlackboard`,
  Unit_GetLastCreatedUnit()
)
// Saves shop position to shop core's blackboard
Blackboard_SetValue_String(
  Blackboard_GetBlackboardOfEntity(Unit_GetLastCreatedUnit()),
  "shop_position_key",
  `ShopPositionKeyToSaveToBlackboard`
)

              "type": "Value",
              "value": {
                "type": {
                  "directive": "FunctionType",
                  "type": "Player"
                },
                "value": "1"
              }

---

ShopToHandCoreTransitionTrigger

Trigger: shopCore uses ability (expected to only be Buy, which morphs ShopCore into HandCore)

1. `GV_OpenHandPositionToSpawnAt` = PickFirstOpenHandPositionForPlayer()
1. SetHandCoreBlackboardHandPosition(`GV_OpenHandPositionToSpawnAt`)
1. `GV_HandPositionToSpawnAt` = GetVectorForPlayer1HandPosition(`GV_OpenHandPositionToSpawnAt`)
1. Set position to `GV_HandPositionToSpawnAt`
1. move shopCore's `units` (tracked by blackboard) to Actor's current position
1. Remove this shopCore from the player's blackboard
  1. (the player blackboard key to use should be saved to `shop_position_key` in this core's blackboard)
1. AddHandCoreToOpenHandPositionInPlayerBlackboard(`GV_OpenHandPositionToSpawnAt`)
