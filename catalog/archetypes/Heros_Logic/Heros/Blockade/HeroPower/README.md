// "I Am Your Shield": Passing a Battle Group permanently applies a shield to its units
// that nullifies the first damage taken each Battle Phase.
// Note: applies to triggering unit
PerformBlockadeHeroPowerPassive():
  Actor_ApplyBuff(IAmYourShield_BuffListener)