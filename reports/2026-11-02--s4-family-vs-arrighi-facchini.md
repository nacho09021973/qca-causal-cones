# s=4 family against Arrighi–Facchini: targeted prior-art comparison

**Date:** 2026-11-02. **Branch:** `research/schur-stability-audit`.
**Nature:** reading of a primary source against the reviewed s=4 family
(CS Sec. 4.1). No computation, no gate, no external tool: the user
declined `investigacion-gemini` and asked for public primary sources.
Written by Claude Code (Claude Opus 5.5); unreviewed.
**Source:** P. Arrighi, S. Facchini, *Quantum walking in curved spacetime:
(3+1) dimensions, and beyond*, arXiv:1609.00305v2 (QIC 17, 810–824,
2017), `sources/1609.00305v2.pdf`, SHA256 prefix `27cb06e4ba36f6f3`
(full hash in `sources/S4_FAMILY_AUDIT_SOURCES.md`). Read: Secs. I–VII,
PDF pp. 1–7.

**Pre-step check.** Known: the 2026-09-15 audit
(`reports/2026-09-15--s4-family-prior-art-audit.md`, AF16/17) found the
compression mechanism of AF Eq. (27) and left grouping, encoding, full
support, D2 action and irreducibility uncompared. Question: does a
homogeneous specialization of AF's construction give our symbol, and
does AF state or imply `c_0 < c_strict^iso`? Abandonment: if AF contains
the family with the same support and adjustable speed, and the strict
support statement is in AF or immediate from it, the family is recorded
as prior art and dropped as a novelty candidate.

## 1. What AF contains (read in the PDF)

- **Compression of an involution sets the speed.** The effective velocity
  matrix `B_1` is the compression of a traceless Hermitian unitary `B`
  (Eq. (18a)); unitarity and hermiticity give `B_1^2 + B_2^† B_2 = I_2s`
  (Eq. (27), p. 4), so the eigenvalues `d_i` of `B_1` lie in `[-1, 1]`
  and are free (Eqs. (28)–(29), p. 4–5).
- **Continuum cone inside the lattice cone.** Sec. V (p. 6): "The
  constraint that the eigenvalues of `B_1` are ... in `[-1, 1]`
  represents the finite speed of propagation on the lattice", and
  coordinates can be rescaled so that "the physical lightcones are
  inside the 'causal lightcones' of the discrete model".
- **Higher dimensions by operator splitting** along the coordinate axes:
  `U = prod_i U^(i)`, each a paired 1D walk along `x_i` with
  `U^(i) ≈ I - 2 i eps H^(i)` (Sec. IV, p. 5), decoding and re-encoding
  between sub-steps.
- **Setting:** continuum limit `eps -> 0` with coins and encodings
  analytic in `eps` and spacetime-dependent (Eqs. (9)–(10)); the grouped
  field is `C^{4s}`, the limit field `C^{2s}`; zeroth order forces
  `E^(0)† W^(0) X E^(0) = I_2s ⊕ U` (Eq. (16)), i.e. the walk is the
  identity at zeroth order on the physical field.
- **Support:** in the `U(2)` scheme the (2+1) step reads a 4×4 block of
  cells, radius 4 (Sec. VI, p. 7).
- **Not in AF:** any statement on the exact support of `U^n`, on vertex
  coefficients, or on an asymptotic body; any D2 covariance or
  irreducibility statement; Floquet-shifted nodes.

## 2. Comparison with the s=4 family

| Property (CS Sec. 4.1) | s=4 family | AF | Same? |
| --- | --- | --- | --- |
| Speed set by compressing an involution | `P Gamma_i P = a sigma_i P`, `c_0 = a/sqrt3` | `B_1` compression of `B`, `d_i in [-1,1]` | **Yes, mechanism** (already recorded in the 2026-09-15 audit) |
| Product of one-dimensional factors | `exp(-i q_x Gamma_x) exp(-i q_y Gamma_y) exp(-i q_z Gamma_z)` | operator splitting `prod_i U^(i)` | **Yes, structure** |
| Step set | exactly the eight `(±1,±1,±1)/sqrt3`, no on-site term | grouped ±2 shifts with encodings; 4×4 block support in (2+1) | **No** as written; a regrouping identification was not attempted |
| Node | two rank-two clusters at `±pi/4`, `A(0) = W` not a phase | `U ≈ I` at zeroth order on the physical field | **No** |
| Homogeneous fixed-lattice symbol | yes | continuum limit `eps -> 0`, spacetime-dependent coins | Different setting; the homogeneous case is a specialization |
| D2 covariance, irreducibility | `R_i = sigma_i ⊗ I_2`; scalar commutant | not discussed | Not in AF |
| Strict asymptotic body `C_infty^strict = C_micro`, `c_strict^iso = r_in` | certified (vertex coefficients non-nilpotent) | not discussed | **Not in AF** |

Reading: AF does not contain the family as written, and does not state
`c_0 < c_strict^iso`. The literal abandonment condition is not met. AF
does contain the mechanism (adjustable speed by compression), the
product structure, and the statement that the continuum cone may sit
strictly inside the lattice causal cone.

## 3. What the comparison leaves, and a stronger objection found on the way

What is left specific to the family is the conjunction: fixed BCC step
set `N_3` with D2 covariance, irreducible, Floquet-shifted clusters, and
the exact strict-support certificate. That conjunction is what makes it a
counterexample to the strong `B_infty^*` **in the declared class**.

As a phenomenon, however, `c_0 < c_strict^iso` is already realised by
published walks. The promoted table (CS Sec. 11) certifies
`C_infty^strict = C_micro`, hence `c_strict^iso = r_in = sqrt3/2`, for
ADMP L6a (`c_0 = 1/2`; arXiv:1803.01015, 2018) and for JDW L6c, L6d, L6f
(`c_0 = 3/4`; arXiv:1803.01304, 2019). Those papers do not compute
`c_strict^iso`; the inequality for their walks is our computation, but
the walks are theirs. CJWW (arXiv:2408.02108, Sec. 5.3) already separate
the small-momentum Weyl speed from faster finite-momentum propagation
(2026-09-15 audit, Sec. 3).

## 4. Verdict on the candidacy

- AF: **structural antecedent** (mechanism and product structure), not an
  identification; the abandonment condition as stated is not met.
- Remaining claim, if any: a counterexample to strong `B_infty^*` that
  holds in one declared class (BCC, D2, irreducible). Published walks on
  other lattices already show `c_0 < c_strict^iso`, and the mechanism is
  in AF. The residual novelty is therefore class-relative and narrow.
- Recommended record: `NOVELTY = OPEN` → **not pursued as a novelty
  candidate** (user decision). The mathematical result and its review
  are unchanged.
- Not done: a regrouping/encoding search for an exact map between AF's
  homogeneous specialization and the family; a forward-citation search
  of AF, ADMP and JDW.
