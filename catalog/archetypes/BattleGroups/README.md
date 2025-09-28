# Battle Groups

## When adding to/removing from the battle group arrays, 
1. update the length var of all affected battleGroup arrays (its own tier AND up)
  1. BOTH the array_size of the var itself AND 
  2. the var keeping track of the length e.g. LengthOfTier2AndBelowBattleGroups
2. add/remove the battleGroup's ShopCore to/from GeneralShopCoreSpawn 
3. add/remove the battleGroup's ShopCore to/from SetVarsForCoreSpawnUnits

## When adding a triple
1. copy the battle group + rename all the files
2. rename the base core's name
3. double the units spawned in the SetVarsFor trigger
4. add/remove the battleGroup's HandCore to/from SetVarsForCoreSpawnUnits