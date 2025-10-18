// When placed, Gain 1 Veterancy Level.
LancerArmstrong_PerformWhenXIsPlaced():
  Set `IV_GiveCoreUnitsVeterancy_Core` = Unit_GetTriggeringUnit()
  Set `IV_GiveCoreUnitsVeterancy_NumXP` = 100
  GiveCoreUnitsVeterancy(`IV_GiveCoreUnitsVeterancy_Core`, `IV_GiveCoreUnitsVeterancy_NumXP`)