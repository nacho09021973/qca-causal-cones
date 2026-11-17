# S4 family: isotropy in the sense of D'Ariano-Erba-Perinotti — execution

2026-11-17. Author: Claude Code (Claude Opus 5.5). Contract
`theory/S4_DEP_ISOTROPY_GATE.md`, preregistration commit `9188755`.
User «autorizo ejecutar». Branch `research/thirring-isolated-spectator`.
Status: author verdict **`DEP_ISOTROPIC_IN_DECLARED_L`**, PRELIMINARY,
no independent review, no promotion. NOVELTY = OPEN.

## Execution record

- Verifier `scripts/verify_s4_dep_isotropy.py` committed before running
  (`fdae12c`). Run 1 stopped with `NotImplementedError` in `sp.solve`
  after C1-C3 PASS (tooling; no verdict). Output retained:
  `reports/2026-11-17--s4-dep-isotropy-run1.txt`.
- Method fix committed before run 2 (`36fb8fd`): zero sets computed on
  M_h = P_x^{s_x} P_y^{s_y} P_z^{s_z}, since A_h = W M_h with W unitary and
  commuting with every U_l (both checked as sanity), so A_h = 0 iff M_h = 0
  and [U_l, A_h] = W [U_l, M_h]; the arc a^2+b^2=1, 0<a<1, b>0 is
  parametrized by a = (1-t^2)/(1+t^2), b = 2t/(1+t^2), t in (0,1); common
  zeros = real roots in (0,1) of the gcd of the real and imaginary parts of
  the numerators (exact, SymPy real_roots). No expectation changed.
- Run 2: all sanity checks PASS; output
  `reports/2026-11-17--s4-dep-isotropy-run2.txt`. SymPy 1.14.0.

## Results (run 2)

| Task | Result |
| --- | --- |
| C1 A_h ≠ 0, eight h, all a in (0,1) | PASS, no zeros |
| C2 U_l A_h U_l† = A_{l(h)}, 24 identities | PASS |
| C3 L transitive on S_+ and S_-, no fixed generator | PASS |
| C4 [U_l, A_h] ≠ 0, 24 pairs | no pair identically zero; no a in (0,1) where any commutator vanishes |
| C5 U projective representation of L | PASS |

Verdict: `DEP_ISOTROPIC_IN_DECLARED_L`. At theta = pi/4 and every
0 < a < 1, the s=4 family on the eight BCC displacements, with no on-site
coefficient, satisfies Definition 1 of arXiv:1708.00826v2 (isotropy with
respect to S_+ = parity +1 generators, L = Klein group of coordinate
half-turns, U_l = sigma_l ⊗ I) together with their homogeneity condition
(2) as stated there; no other formulation of homogeneity (e.g. the one of
their Ref. [23]) is certified.

C1-C5 certify the declared isotropy only. The spectral expansion of the
family, derived separately (all-parameter analytic proof in
`theory/S4_STRICT_CONE_COUNTEREXAMPLE.md`, exact spot checks on a six-point
a panel in `scripts/cert_Aa_s4_counterexample.py`; status
COUNTEREXAMPLE_VERIFIED, independent review PASS, `CURRENT_STATE.md` Sec. 4.1;
not recomputed here), gives Weyl slopes
c_0 = a/sqrt3 about the quasienergies ±pi/4. With c_strict^iso = 1/sqrt3
(strict exact-support body, same section), this isotropy notion does not
fix that slope when the internal dimension is four. The comparison is with
the strict support body, not with a ballistic front defined by
amplitudes.

## Second reading of C4

By C2, U_l M_h U_l† = M_{l(h)}, so [U_l, M_h] = 0 iff M_{l(h)} = M_h.
Condition (2) is therefore equivalent here to: transition matrices of
distinct generators in one L-orbit are distinct — the reading given by
1708.00826 itself ("two transition matrices associated to different
generators must be distinct"). This is a structural restatement, not an
independent computation; an independent check (another CAS, a person or a
cross-family reviewer) has not been made.

## Repairs after the sealed Astra review (2026-11-17)

Review `reports/reviews/2026-11-17-s4-dep-isotropy-astra/informe_astra.md`
(gpt-6-astra, on `251c163`, archived `ed63258`): REPAIR_REQUIRED limited to
documentation; blocks 1-4 PASS; block 5 OPEN pending the diff between the
two verifier versions; block 6 REPAIR_REQUIRED. User «si, aplica 1-3».

- R1 (erratum, verifier untouched): the verifier docstring lists "P
  projectors" among the sanity checks, but no explicit projector check is
  executed. What is checked is that each Gamma_i is a Hermitian involution;
  that P_i^± are projectors follows. The verifier bytes are not changed
  (reviewed file); the erratum is recorded here and in `scripts/README.md`.
- R2: the diff between the run-1 and run-2 verifier versions,
  `git diff fdae12c 36fb8fd -- scripts/verify_s4_dep_isotropy.py`, is
  archived in `reports/reviews/2026-11-17-s4-dep-isotropy-astra-rereview/`
  for a bounded re-review of block 5.
- R3: the verdict paragraph now separates the certified isotropy from the
  separately computed slope, names the strict support body as the
  comparison, and restricts homogeneity to condition (2) as stated.
- Also noted by the reviewer and not changed: the `"UNDECIDED"` branch is
  unreachable in the run-2 code, so "C4 pairs undecided: none" adds no
  check; `simplify` is used in identity tests (exact, no tolerances).
- The reviewer's trace witnesses for C1/C4 (tr(J_y [J_x, M_h]) =
  s_x s_y a^2, etc.) and its derivation of the slope are AI-written and
  were not checked here; they are not used as evidence.

## Scope and what is not claimed

- Only theta = pi/4, this L, this U and this generating set; the family
  definition of `theory/S4_STRICT_CONE_COUNTEREXAMPLE.md` (`1dae941`).
- Definition 1 and condition (2) only; other assumptions of 1306.1934
  (e.g. its quasi-isometric embedding discussion) are not examined.
  Full cubic isotropy, Lorentz covariance and massive sectors: not claimed.
- Prior art: open and targeted searches and the original checks are in
  `investigaciones/2026-11-17-c0-causal-body-prior-art/comprobacion.md`;
  the statement was not found there, which does not establish absence.
  NOVELTY = OPEN.
- Line criterion of the contract: not triggered (C4 holds for every a).
