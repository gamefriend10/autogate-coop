# GeneralShopCoreSpawn

LONG if-then-else that checks determines which ShopCore BattleGroup to spawn

prereqs:
1. ShopPositionToSpawnAt is set
2. BattleGroupToSpawnTag is set

# GeneralUnitsForCoreSpawn

LONG if-then-else for every BG in the game.

prereqs:
1. ShopPositionToSpawnAt is set

1. If (triggering unit) has tag = E.g. HogDog (Entity_HasAllTags) TODO CHANGE THE INBATTLE var check to some tag check
    1. Then run E.g. HogDogSpawn trigger
    2. Break
2. If (triggering unit) has tag... etc