import QcaComparator.Solution
import QcaComparator.AssertAxioms

/-!
# Permitted axioms

The build fails if either solution theorem depends on anything beyond
`propext`, `Classical.choice` and `Quot.sound` (in particular `sorryAx`, or
`Lean.ofReduceBool`, which `native_decide` introduces). The count fixes the list.
-/

/-- info: 2 theorems use only propext, Classical.choice, Quot.sound -/
#guard_msgs in
#assert_standard_axioms QcaComparator.tn_bound QcaComparator.delta_le_four_T
