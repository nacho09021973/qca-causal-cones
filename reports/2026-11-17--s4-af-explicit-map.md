# S4 family as a homogeneous Arrighi-Facchini walk — execution

2026-11-17. Author: Claude Code (Claude Opus 5.5). Contract
`theory/S4_AF_EXPLICIT_MAP_GATE.md`, preregistration `fcb6f50`. User
«push y autorizo ejecucion». Branch `research/thirring-isolated-spectator`.
Author verdict: **`AF_EQUIVALENT_VIA_ANSATZ`** under the frozen reading
R1-R3. PRELIMINARY, no independent review. See Sec. 4 before acting on
the abandonment criterion.

## 1. Execution record

Verifier `scripts/verify_s4_af_explicit_map.py`, committed before running
(`db25f3d`). Four runs, all retained:
- run 1 (`db25f3d`): 580 s timeout, no output (symbolic `eigenvects` with
  square roots; buffered prints) — `...-run1.txt`;
- run 2 (`0da360c`, closed-form half-angle eigenvectors on a rational
  parametrization): 30/31, M3 for axis x reported FAIL; a manual
  inspection with `expand_complex` gave a zero residual, i.e. a
  simplification false negative — `...-run2.txt`;
- run 3 (`c8867fb`, `expand_complex` in the zero test): M1-M3 all PASS,
  then timeout in the old M4 (full product of exponentials) — `...-run3.txt`;
- run 4 (`ec7de10`, M4 as the per-factor identity): **33/33 PASS**, exit 0
  — `reports/2026-11-17--s4-af-explicit-map-run4.txt`.
No expectation was changed between runs; each change is recorded in the
verifier docstring. SymPy 1.14.0. Final verifier SHA256 prefix
`67f5b995b89081b3`.

## 2. The map (T1-T3)

T1. In AF coordinates phi = (u, d, u', d') (Eq. (3)-(4)), with
P, P' the unprimed/primed selectors and J' = [P'; 0], J = [0; P], one
homogeneous paired step along axis i has grouped symbol (Eqs. (5)-(6),
(36), reading R1)
  G_i(p) = E_i† W'_i (e^{-ip} J' + e^{ip} J) E_i.
M1: J' = Pi Q', J = Pi Q with Pi = X = sigma_x ⊗ I_4 (block swap) and
Q' + Q = I, so G_i(p) = (E_i† W'_i Pi E_i) · E_i† (e^{-ip} Q' + e^{ip} Q) E_i:
an arbitrary coin times a conditional shift on the rank-4 subspace
E_i† Q' E_i.

T2 (A1). Take an explicit unitary E_i (closed-form eigenvectors of
Gamma_i) with E_i† Q' E_i = I_2 ⊗ P_i^+ (M2) and W'_i = E_i C_i E_i† Pi†.
Then G_i(p) = C_i (I_2 ⊗ F_i(p)), F_i(p) = e^{-ip} P_i^+ + e^{ip} P_i^-
(M3): the paired step does not mix the two sites of a pair; on the psi
lattice each site moves by ∓2 cells along axis i on the eigenspaces of
Gamma_i. Both parity sublattices evolve identically (R2, E7 keeps one).

T3 (A2). With C_y = C_z = I and C_x = W ⊗ I_2, the composed psi-level
symbol is W F_x(2k_x) F_y(2k_y) F_z(2k_z); by M4 (F_i(q) = cos q I -
i sin q Gamma_i) this is the family symbol A(k') with q_i = k'_i/sqrt3 =
2k_i, i.e. the family after the uniform rescaling E8 (AF axis displacement
2 ↔ family displacement 1/sqrt3 per axis) and dropping identical copies
(E7). The AF time label x0+2 per step is a unit choice; A3 (A(k)^2) was
not needed. The ordering of the three factors matches the family's
W F_x F_y F_z.

## 3. Verdict

`AF_EQUIVALENT_VIA_ANSATZ` under R1-R3 and E1-E8: the s=4 family at
theta = pi/4, for every 0<a<1, is exactly a homogeneous AF (3+1) walk with
s = 2, coins W'_y, W'_z equal to the block swap conjugated by the
encodings (trivial coin C = I) and W'_x carrying the family coin W.

## 4. What this does and does not mean (author assessment)

- R3 does not impose AF's zeroth-order condition Eq. (16). M5 (a remark
  check) shows that in AF's phi coordinates the trivial coin gives
  I_4 ⊕ U with U = I, as Eq. (16) requires, but the coin carrying W has
  unprimed block W ≠ I, so Eq. (16) fails for that step. The family is
  therefore realized in AF's **architecture** (operator splitting of
  coined conditional-shift paired steps with encodings), not in AF's
  continuum-limit class, where the walk is the identity on the physical
  field at zeroth order. Since A(0)^4 = W^4 = -I, whether A(k)^4 fits
  that class under E5 and E2 was not examined.
- Under R3 the "AF class" is broad: by T1 it is any product over axes of
  arbitrary coins times conditional shifts on half-dimensional subspaces.
  The family's being in it says that its circuit is of this standard
  operator-split form (as are product walks such as Farrelly-Short's),
  and that the compression mechanism is AF's — already recorded as a
  structural antecedent on 2026-09-15 and 2026-11-02.
- AF does not state isotropy in the sense of 1708.00826, nor an isotropic
  s>2 walk with variable c_0 (2026-11-02 reading; not re-read here).
- The contract's frozen abandonment criterion ("an explicit map verified
  exactly → record as prior art and drop the candidacy") is met as
  written. Given the two points above, whether the restricted claim loses
  its candidacy is a decision for the user; this report does not change
  `CURRENT_STATE.md` Sec. 4.

NOVELTY = OPEN pending that decision.
