// Can Cast: Give 1 Veterancy Level to all Vanguard Battle Groups.
// End of Buy Phase: Gain 2 Ability Charges.
BlockheadTriple_PerformEndOfBuyPhase(`IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`):
  Unit_IssueOrderWithNoTarget(
    `IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`,
    StagingCoreRestoreOneCharge
  )
  Unit_IssueOrderWithNoTarget(
    `IV_REUSABLE_PerformEndOfBuyPhase_StagingCore`,
    StagingCoreRestoreOneCharge
  )
