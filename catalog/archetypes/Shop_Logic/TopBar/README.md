# Refresh

triggers when topbar casts ability

1. if triggering ability was tier2
  1. set tier to 2
  2. set tier2 ability to disabled

1. if triggering ability was refresh
  1. set `PlayerToRemoveShopCoreFor` to triggering player
  3. RemoveShopCoresForPlayer(`PlayerToRemoveShopCoreFor`)
  4. SpawnShopForPlayer1