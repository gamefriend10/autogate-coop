// When placed, add 2 Dog Pack Beta's to hand.
// Note: 2nd won't be added if no room
DogPackTriple_PerformWhenXIsPlaced():
  Set `IV_AddBattleGroupToHand_HandCoreType` = DogPack_HandCore
  Set `IV_AddBattleGroupToHand_Player` = Unit_GetOwningPlayer(Unit_GetTriggeringUnit())
  AddBattleGroupToHand(`IV_AddBattleGroupToHand_HandCoreType`, `IV_AddBattleGroupToHand_Player`)
  AddBattleGroupToHand(`IV_AddBattleGroupToHand_HandCoreType`, `IV_AddBattleGroupToHand_Player`)