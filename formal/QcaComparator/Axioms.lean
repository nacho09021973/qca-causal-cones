import QcaComparator.Solution

/-!
# Permitted axioms

The build fails if either solution theorem depends on anything beyond
`propext`, `Classical.choice` and `Quot.sound` (in particular `sorryAx` or
`Lean.ofReduceBool`, which `native_decide` introduces).
-/

/-- info: 'QcaComparator.tn_bound' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms QcaComparator.tn_bound

/--
info: 'QcaComparator.delta_le_four_T' depends on axioms: [propext, Classical.choice, Quot.sound]
-/
#guard_msgs in
#print axioms QcaComparator.delta_le_four_T
