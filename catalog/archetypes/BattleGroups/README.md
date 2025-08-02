# Battle Groups

## When adding to/removing from the battle group arrays, 
1. update the length var of all affected battleGroup arrays
  1. BOTH the array_size of the var itself AND 
  2. the var keeping track of the length e.g. LengthOfTier2AndBelowBattleGroupsMinus1
2. add/remove the battleGroup's ShopCore to/from GeneralShopCoreSpawn 
3. add/remove the battleGroup's actual units to/from GeneralSpawnUnitsOnShopCoreSpawn