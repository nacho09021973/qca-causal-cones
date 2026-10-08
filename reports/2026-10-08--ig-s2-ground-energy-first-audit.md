# IG-S2 — ground-energy prerequisite for the N-type tensor gate

Date: 2026-10-08
Branch: `research/inverse-gravity-design`
Base: `1dd814c56be848852d8d92e50648bd1d4436f1a2`
Status: `OPEN_AFTER_GROUND_ENERGY_AUDIT`

Correction, 2026-10-08: the original version at `801bc0e` overstated the
necessity of separately knowing E_0 and an exact reference wavefunction.
The corrected statements below distinguish absolute-energy subtraction from
ground-state identities that cancel E_0. The five-method preflight
`2026-10-08--ig-s2-five-ground-energy-methods.md` supersedes the earlier
method-selection restriction. No spectral gate has passed.

## A. State reproduced

The live branch is `research/inverse-gravity-design`, synchronized with its
origin. The pre-existing untracked file
`reports/2026-10-08--elastic-atlas-documentary-audit.md` is unrelated and was
not modified.

The canonical state records that IG-S0 is only a state-first preflight, IG-S1
rejects the dressed commuting-parent recipe for a gapless propagating target,
and the earlier qutrit tick has no certified energy vacuum or spectrum. The A/B
state-selection attempt is closed by control limitations. No exact ground state
of a complete N-type Hamiltonian is currently recorded.

The primary PDF is present at `biblioteca/arXiv-0907.1203.pdf`, SHA256
`3b1af85075e346cf00b0b91824554f6f87bf494f6bfb9737c867f2a8c134fa0c`.
The relevant source locations are the compactified constraints and penalties
(pp. 13–14), the N-type definition (pp. 18–20), and the reliability discussion
(pp. 20–22).

Gu–Wen define

\[
H_N(L)=H_U(L)+H_J(L)+H_g(L),
\]

with \(\tilde U\sim\tilde J\sim\tilde g\). The constraint penalties in
\(H_U\) are nonnegative, but the displayed \(H_J\) and \(H_g\) contain
sign-indefinite cosine/sine terms. The paper states that
\([H_U,H_J]\ne0\) and \([H_U,H_g]\ne0\), and explicitly calls the N-type
spin-wave/quantum-freeze calculation uncontrolled and its linear-dispersion
conclusion unreliable (pp. 19–22). These are source statements, not a
finite-volume spectral theorem.

## B. First rigorous proposition

Let \(H_L=H_N(L)\) have ordered eigenvalues
\(E_0(L)\le E_1(L)\le\cdots\). Let \(T_L\) be a normalized two-dimensional
subspace orthogonal to the complete ground eigenspace, and set

\[
r_L=\sup_{\psi\in T_L,\,\|\psi\|=1}\langle\psi,H_L\psi\rangle.
\]

**Proposition (sufficient subtraction certificate).** If
\(E_0(L)\ge b_L\) and \(r_L-b_L\le C/L\), then
\(r_L-E_0(L)\le C/L\).

Proof: \(E_0(L)\ge b_L\) implies
\(r_L-E_0(L)\le r_L-b_L\). The two-dimensional statement is the same inequality
applied to the worst Rayleigh quotient. \(\square\)

This is not a necessity theorem for all variational methods. For a true
ground eigenvector \(\Omega\),
\(\langle A\Omega,(H-E_0)A\Omega\rangle
=\langle\Omega,A^\dagger[H,A]\Omega\rangle\).
This identity cancels E_0 without a numerical lower bound. Existence of
\(\Omega\) in finite dimension is automatic; control of its correlations,
ground-space removal, and two independent tensor probes is not.

Thus an extensive lower-bound error \(O(L^3)\), or an uncontrolled constant
error, cannot certify an \(O(1/L)\) excitation energy by this subtraction
certificate. The error statement does not exclude exact cancellation methods.

## C. Viability analysis

### Local-term bounds

Finite local dimension gives only bounds of the form
\[
H_U\ge0,\qquad H_J\ge-c_JL^3,\qquad H_g\ge-c_gL^3,
\]
and hence an extensive lower bound on \(H_N\). A relative-bound argument
against \(H_U\) would become useful only with an exact or \(O(1/L)\)-accurate
ground-energy formula. Such dominance cannot be inferred in the declared
regime \(\tilde U\sim\tilde J\sim\tilde g\); taking \(\tilde U\gg\tilde J,\tilde g\)
would change the gate.

### Constraint-kernel reference

The nonempty common kernel of the compact constraints proves that \(H_U\) has
zero-energy states. It does not prove that they minimize \(H_N\), because
\(H_J\) and \(H_g\) do not preserve that kernel. An exact certificate would
need, for some \(\Omega_L\),
\[
H_N(L)-e_L\mathbf 1\ge0,\qquad H_N(L)\Omega_L=e_L\Omega_L.
\]
No such inequality or eigenvector is present in the current records.

### Momentum and commutator routes

Translation symmetry can block-diagonalize \(H_N(L)\), but it supplies no
absolute lower bound on the ground energy. A single-mode/double-commutator
ratio requires estimates in a true ground state, but not necessarily its
explicit wavefunction or energy. Substituting the constraint reference or
trace state is an unproved change of ensemble.
Likewise, the verified constraint commutation does not imply a continuous Ward
identity for the full compact N-type Hamiltonian.

## D. Result

`OPEN_AFTER_GROUND_ENERGY_AUDIT`.

No \(O(1/L)\)-accurate subtraction certificate has been supplied. Nor have
the ground-state correlation estimates needed for a commutator route been
supplied. This is a missing proof, not a mathematical obstruction to either
route. It records that the available explicit references belong to
\(H_U\) or to stationary/trace constructions, while \(H_J,H_g\) act at
comparable strength and do not commute with \(H_U\).

No TT subspace, spectral upper bound, gap statement, helicity statement, or
gravitational claim is promoted.

## E. Frozen candidate and single next falsifiable obligation

The candidate is now frozen in
`theory/INVERSE_GRAVITY_NTYPE_GROUND_REFERENCE_GATE.md` as

\[
|\Omega_L\rangle=
\frac{P_S(L)|0_L\rangle}{\|P_S(L)|0_L\rangle\|},
\qquad
P_S(L)=\prod_i\frac13\sum_{m=0}^{2}S(i)^m,
\]

with \(n_G=3\), six qutrits per cell, and the exact Gu–Wen stencils. This is
only a constraint-sector candidate; it is not assumed to minimize \(H_N\).

The historical exact-reference obligation was to prove or refute
\[
\exists e_L:\quad H_N(L)|\Omega_L\rangle=e_L|\Omega_L\rangle,
\quad H_N(L)-e_L\mathbf 1\ge0.
\]

The proof must use the printed compact operators of Gu–Wen (pp. 13–20) and
hold for all declared periodic \(L\ge3\). The candidate has now been refuted
author-side in `2026-10-08--inverse-gravity-ground-reference-refutation.md`
(use its corrected proof). Failure refutes this reference, not N-type.
The former blanket prohibition on other variational methods is withdrawn:
the five-method preflight states their separate admission conditions.

No script was created or run; this report is an analytic logical audit and
produces no retained numerical result.
