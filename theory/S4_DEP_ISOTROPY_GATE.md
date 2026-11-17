# S4 family: isotropy in the sense of D'Ariano-Erba-Perinotti

2026-11-17. Author: Claude Code (Claude Opus 5.5). Initial status
**OPEN / NOT EXECUTED**. User «si a ambas preguntas» (2026-11-17)
authorized drafting; user «autorizao congelar» (2026-11-17) authorizes
freezing by this commit. Execution needs a separate user authorization. One contract; no review,
promotion or publication follows from it.

## Known, question, abandonment

Known (read in this session, with source):
- Family: `theory/S4_STRICT_CONE_COUNTEREXAMPLE.md` (last change `1dae941`,
  SHA256 prefix `bc15165e1acb4268`), Secs. 2-5. On C^2_sigma ⊗ C^2_tau,
  0<a<1, b = sqrt(1-a^2): T_x = b tau_x + a tau_z, T_y = b tau_y + a tau_z,
  T_z = -b tau_x + a tau_z; Gamma_i = sigma_i ⊗ T_i; P_i^± = (I ± Gamma_i)/2;
  W_theta = I ⊗ exp(-i theta tau_z). Fourier coefficients
  A_{h_s} = W_theta P_x^{s_x} P_y^{s_y} P_z^{s_z} on the eight BCC
  displacements h_s = (s_x,s_y,s_z)/sqrt3, no on-site coefficient. The
  counterexample point is theta = pi/4, with c_0 = a/sqrt3 and
  C_infty^strict = C_micro (reviewed; `CURRENT_STATE.md` Sec. 4.1).
- Sec. 4 of that file: R_l = sigma_l ⊗ I commute with W_theta and give
  R_l A(k) R_l^dagger = A(l k) for the binary rotations l of the BCC
  tetrahedral generators. The independent review
  (`reports/2026-09-15--s4-independent-review.md`, lines 23-28) states that
  the coordinate half-turns act transitively on the four parity +1 sign
  triples, and that full cubic symmetry is not assumed.
- D'Ariano, Erba, Perinotti, arXiv:1708.00826v2 (read 2026-11-17, logged
  in `investigaciones/2026-11-17-c0-causal-body-prior-art/comprobacion.md`):
  Definition 1 (isotropic QW): a group L of Cayley-graph automorphisms
  acting as permutations lambda of S_+, transitive on each S_+^n, with a
  projective unitary representation U on C^s such that
  A_lambda(h) = U_l A_h U_l^dagger for all l in L, h in S_+; plus
  homogeneity condition (2): [U_l, A_h] ≠ 0 for all h in S_+ and l in L
  with l(h) ≠ h. They also assume A_h ≠ 0 for all h in S_+ ∪ S_-.
  Their classification (s = 2) gives, for d = 3, only the two Weyl walks.
- D'Ariano, arXiv:1701.06309v1, Sec. 3.8: the s ≥ 3 isotropic problem is
  unsolved; only block-form s = 4 solutions are given.

Question: does the frozen s=4 family at theta = pi/4 satisfy Definition 1
of 1708.00826 with S_+ the four parity +1 BCC generators, L the Klein
group of coordinate half-turns and U_l = sigma_l ⊗ I, including condition
(2), and for which a in (0,1)?

Abandonment of the line (the possible note "s=2 rigidity does not extend
to s=4"): if condition (2) or covariance fails for every a in (0,1) at
theta = pi/4 with this L and U, the family is not isotropic in this sense
and the note has no candidate; stop, record the failure, do not search for
another family under this contract. If it fails only on a finite set of a,
the candidate survives on the complement, stated with the exceptions.

## Fixed objects (no change after freezing)

- Family, conventions and theta = pi/4 as above; a symbolic in (0,1).
- S_+ = {h_s : s_x s_y s_z = +1}, S_- = -S_+ (generating set of the BCC
  Cayley graph of Z^3 as in 1306.1934 / 1708.00826).
- L = {id, l_x, l_y, l_z}, l_x(s_x,s_y,s_z) = (s_x,-s_y,-s_z), cyclically.
  U_l = I, sigma_x ⊗ I, sigma_y ⊗ I, sigma_z ⊗ I.
- No alternative L, U, generating set or basis change is admitted under
  this contract. A failure with this choice is reported as such; it is not
  a proof that no other isotropy group works.

## Tasks (exact SymPy; one permanent verifier, committed before running)

- C1. A_h ≠ 0 for all eight h, for every a in (0,1).
- C2. Covariance: U_l A_h U_l^dagger = A_{l(h)} for all l in L and all
  eight h (exact matrix identity, symbolic a).
- C3. Transitivity: L acts transitively on S_+ and on S_-; no nontrivial
  l fixes any h.
- C4. Condition (2): [U_l, A_h] ≠ 0 for the 3 x 8 pairs with l ≠ id.
  For each pair compute the commutator exactly; report the set of a in
  (0,1) where it vanishes (expected to be decided by exact polynomial
  factorization in a and b with b^2 = 1 - a^2).
- C5. U is a projective representation of L (U_l U_m = phase x U_{lm}).
Verifier: `scripts/verify_s4_dep_isotropy.py`, standalone, rebuilding the
family from the definitions above; no reviewed verifier is modified
(`cert_Aa_s4_counterexample.py` and `review_Aa_s4_exact.py` read-only).
Add its two exact command forms to `.claude/settings.json`.

## Verdicts

- `DEP_ISOTROPIC_IN_DECLARED_L`: C1-C5 hold for every a in (0,1).
- `DEP_ISOTROPIC_EXCEPT_FINITE_SET`: C1-C3, C5 hold for all a; C4 fails
  exactly on a stated finite set of a.
- `NOT_DEP_ISOTROPIC_IN_DECLARED_L`: C2 or C3 fails, or C4 fails for every
  a in (0,1).
Author results PRELIMINARY until an independent review.

## Not claimed under any verdict

Novelty of the family or of the statement; that no published s=4
isotropic walk with variable speed exists (prior-art search is separate
and incomplete); full cubic isotropy; Lorentz covariance; anything about
massive sectors, other theta, other groups L or other generating sets;
that D'Ariano-Erba-Perinotti's other assumptions (e.g. the quasi-isometric
embedding discussion of 1306.1934) are met beyond Definition 1 and
condition (2). NOVELTY = OPEN.
