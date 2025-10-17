// When placed, add 1 Dog Pack Beta to hand.
DogPack_PerformWhenXIsPlaced():
  Set `IV_AddBattleGroupToHand_HandCoreType` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())
  Set `IV_AddBattleGroupToHand_Player` = `IV_PickFirstOpenHandPositionForPlayer_Player`
  AddBattleGroupToHand(`IV_AddBattleGroupToHand_HandCoreType`, `IV_AddBattleGroupToHand_Player`)