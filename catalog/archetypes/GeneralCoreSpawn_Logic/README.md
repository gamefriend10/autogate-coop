// LONG if-then-else that determines which ShopCore BattleGroup to spawn
GeneralShopCoreSpawn(
  `GV_PlayerToSpawnShopCoreFor`,
  `ShopPositionToSpawnAt`,
  `BattleGroupToSpawnTag`,
  `ShopPositionKeyToSaveToBlackboard`
):
  // TODO: switch this over to switch case
  If(`BattleGroupToSpawnTag` == hogdog_snowtag):
    `GV_ShopCoreToSpawn` = HogDog_ShopCore
  If ... etc
  ShopCore_Spawn(`GV_ShopCoreToSpawn`, `GV_PlayerToSpawnShopCoreFor`, `ShopPositionToSpawnAt`, `ShopPositionKeyToSaveToBlackboard`)

--------------------

// Note: just regular handcores
// Returns: UnitData `OV_DetermineHandCoreFromTag_HandCoreType`
DetermineHandCoreFromTag(
  SnowTag `IV_DetermineHandCoreFromTag_Tag`
):
  Switch(`IV_DetermineHandCoreFromTag_Tag`):
    case lancerarmstrong_snowtag:
      Set `OV_DetermineHandCoreFromTag_HandCoreType` = LancerArmstrong_HandCore
    case dogpack_snowtag:
      Set `OV_DetermineHandCoreFromTag_HandCoreType` = DogPack_HandCore
    case dogpackbeta_snowtag:
      Set `OV_DetermineHandCoreFromTag_HandCoreType` = DogPackBeta_HandCore
    case bunkerrush_snowtag:
      Set `OV_DetermineHandCoreFromTag_HandCoreType` = BunkerRush_HandCore
    case loveletter_snowtag:
      Set `OV_DetermineHandCoreFromTag_HandCoreType` = LoveLetter_HandCore
    case bedtech_snowtag:
      Set `OV_DetermineHandCoreFromTag_HandCoreType` = BedTech_HandCore
    case blockhead_snowtag:
      Set `OV_DetermineHandCoreFromTag_HandCoreType` = Blockhead_HandCore
    case sdfvanguard_snowtag:
      Set `OV_DetermineHandCoreFromTag_HandCoreType` = SDFVanguard_HandCore