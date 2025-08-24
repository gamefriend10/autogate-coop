# ShopTopBarAbilityCastedTrigger

triggers when: anyone's topbar casts ability

1. if triggering ability was tier2
  1. set tier to 2 for TODO: triggering player
  2. set tier2 ability to disabled for triggering player

1. if triggering ability was refresh
  1. set `PlayerToRemoveShopCoreFor` to triggering player
  3. RemoveShopCoresForPlayer(`PlayerToRemoveShopCoreFor`)
  4. SpawnShopForPlayer1 TODO: change this to triggering player?

If triggering ability was ReadyUp
  Trigger_Run(ReadyUp_Trigger)

If triggering ability was UnreadyUp
  Trigger_Run(UnreadyUp_Trigger)

