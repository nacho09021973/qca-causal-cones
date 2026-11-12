# Amendment 4 to the general infrared operational rate charter

2026-11-12. Drafted by Claude (claude-opus-5-5). **Status: APPROVED by the
user 2026-11-12 («si a las tres», answering the proposal to correct the
clause); in force from this commit.** The frozen charter (`aa6c5f6`) and
Amendments 1–3 are not edited.

## Reason

Charter Sec. 2 requires «`B - A` lies outside `B(c_IR)` and inside
`conv F`». The manuscript's regions violate the second half:
`B - A = (1,1,1) + B(1/2)` contains points outside `[-1,1]^3`. The Stage 0
report therefore misstated that K3 lies in the class. No step of Stages 1
or 2 uses the clause; they use `K_* > 0`, the uniqueness of `v_*` and
`K_* < inf`. Found while designing the polyhedra diagnostic
(`GENERAL_IR_RATE_POLYHEDRA_DIAGNOSTIC.md`); not raised by the Grok review.

## Change

The clause «and inside `conv F`» is replaced by «and `v_* in conv F`»,
equivalently `K_* < inf` (`I = +inf` outside `conv F`). If `B - A` misses
`conv F` entirely the signal vanishes identically by strict causality and
the question is empty.

## Effect

K3 lies in the class as amended (`v_* = (1 - 1/(2 sqrt3))(1,1,1)` is inside
the cube). Stages 1 and 2 and their review are unchanged.
