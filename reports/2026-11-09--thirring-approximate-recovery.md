# Microscopic Thirring code: no approximate recovery at growing times

2026-11-09. Author Claude (Opus 5.5). **PRELIMINARY: author proof plus exact
author checks; one sealed cross-family review (Grok), no promotion, not
formalized in Lean.**

[Sealed Grok review](reviews/2026-11-09-thirring-approximate-recovery-grok/informe_grok.md)
of this text at ad01e20 (grok-4.7, revision-ciega, herramientas 97292a9):
«se sostiene», no objections; steps 1-6 rederived by hand; script inspected,
not executed. One round; its report is kept unedited.

Contract [THIRRING_APPROXIMATE_RECOVERY_GATE.md](../theory/THIRRING_APPROXIMATE_RECOVERY_GATE.md),
frozen at `61a8215` before any derivation. Verifier committed before its first
run at `dd4e547`; that run failed two checks (wrong expectations, Sec. 5), was
retained and corrected at `f5c0d16`.

## 1. Result

Same M=1 code B, rule U=FJ, mu=3/5, nu=4/5, z=i, infinite line, output frame
B_T=F^T B, K_T=B_T^dagger U^T B, E_T=(I-B_T B_T^dagger)U^T B (contract Sec. 2).

**Theorem.** There is a constant c>0 such that, for the logical input 00,

  liminf_{T->infinity} ||E_T|00>||^2 >= c > 0.

Hence ell_T=||E_T||^2 does not tend to zero along any subsequence, and no
sequence T_n -> infinity, phases theta_n and matrix V (unitary or not,
entangling or not) satisfy ||U^{T_n}B - e^{i theta_n}B_{T_n}V|| -> 0.

Verdict: `APPROXIMATE_RECOVERY_EXCLUDED` (contract Sec. 4). The proof shows
c>0 but gives no numerical value for it.

Scope: this code, rule and frozen parameters only. It is not a no-go for the
Thirring QCA, for other codes, auxiliaries, measurements or architectures.
The exact first-step gate D (T=1) is unchanged.

## 2. Mechanism: a two-particle bound state overlapping the code

The line of argument changed after reading the source; the contract's R2(a)
assumed localized bound states of U, which is not the structure here. In
`sources/1711.03920v1.pdf`, U_2=W_2 V_2(chi) (p.2, Eq.(2); same order as
U=FJ, phase first; same W and chi convention, p.1) commutes with the diagonal
translation and decomposes into fibers U(p) over the half total momentum p
(p.2, Eq.(3) and below). Bound states form one band, one eigenvector per
fiber (p.3, Lemma 2; p.4, Eq.(14) and Proposition 1). They travel in the
centre of mass; they are not normalizable eigenvectors of U on the lattice.
The argument is therefore made fiber by fiber.

Fiber convention: w=x1+x2, y=x1-x2 (w and y of equal parity),
psi_p(y)=sum_w exp(ipw) psi(w,y), p in (-pi/2,pi/2], with
||psi||^2=(1/pi) integral ||psi_p||^2 dp. U and F act fiberwise as U(p) and
W_2(p); U(p)-W_2(p)=W_2(p)(J(p)-I) has rank 2 (y=0, opposite components).

**Step 1 (explicit eigenvector).** At p0=pi/4 one has exp(2i p0)=i=z, the
exceptional case of Eq.(14), p.4. Its "+" vector, with basis order
(up up, up down, down up, down down),

  f(1)=(-i e^{i p0},0,0,0),  f(0)=(0, mu/nu, -mu/nu, 0),
  f(-1)=(i e^{i p0},0,0,0),  f(y)=0 for |y|>=2,

satisfies U(p0) f = i f. Verified exactly as the lattice identity
U[exp(-i p0 w) f(y)] = i exp(-i p0 w) f(y) at every target with w in {0,1};
diagonal translation covariance extends it to all w (verifier check 1).
f is antisymmetric (check 2), ||f||^2=25/8.

**Step 2 (isolation).** W(q) has det 1 and trace 2 nu cos q, so eigenvalues
exp(+-i omega(q)), cos omega=nu cos q, omega in [0,pi]. The spectrum of
W_2(p) is the closure of {exp(-i(s omega(p+k)+r omega(p-k)))}, s,r=+-, k real
(multiplication operator). Equality with i requires a+-b to be congruent to
+-pi/2 (a=omega(p+k), b=omega(p-k)); in all four cases this gives
cos^2 a = sin^2 b, i.e.
nu^2(cos^2(p+k)+cos^2(p-k)) = nu^2(1+cos2p cos2k) = 1. At p0, cos 2p0=0,
so this would require nu^2=1; false. By compactness in k, i lies at positive
distance from sigma(W_2(p0)), which equals sigma_ess(U(p0)) (rank-2
perturbation, Weyl). So i is an isolated eigenvalue of U(p0) with finite
multiplicity. Check 3 verifies the algebraic identities; the case analysis
is written here.

**Step 3 (positive bound-state weight).** Choose a circle Gamma around i in the
resolvent set of U(p0). U(p) depends norm-continuously on p (banded in y,
trigonometric in p), so Gamma stays in the resolvent set for p in an interval
I around p0. The Riesz projection P(p) is norm-continuous there and has
constant finite rank; its range consists of eigenvectors of U(p). The code
fiber vector b_p of input 00 has ||b_p||=1 and is continuous in p. At p0,

  <b_{p0}, P(p0) b_{p0}> >= |<f, b_{p0}>|^2/||f||^2 = 2/(25/8) = 16/25

(<f,b_{p0}> = -i sqrt2, check 4). By continuity the integrand is positive on
I, so with P_I the direct integral of P(p) over I,

  c := ||P_I B|00>||^2 = (1/pi) integral_I <b_p, P(p) b_p> dp > 0.

**Step 4 (that weight never returns to the free frame).** P_I commutes with
U. Split B|00> = P_I B|00> + (I-P_I)B|00>. For each code column b_j,

  <F^T b_j, U^T P_I B|00>> = (1/pi) integral_I <W_2(p)^T b_{j,p}, U(p)^T P(p) b_p> dp.

On ran P(p), U(p)^T is a finite sum of lambda_i(p)^T P_i(p), |lambda_i|=1.
For p in I (taken small around pi/4), every branch
k -> s omega(p+k)+r omega(p-k) is real-analytic (|nu cos|<1) and
non-constant (omega_{++}(p,0)=2omega(p) != pi=omega_{++}(p,pi/2) as p != pi/2;
omega_{+-}(p,0)=0 != omega_{+-}(p,pi/2) as sin p != 0; the others are
negatives). Hence W_2(p) has purely absolutely continuous spectrum and, by
Riemann-Lebesgue on the spectral measure, each <W_2(p)^T b, P_i(p)v> -> 0.
The integrand is bounded by ||b_{j,p}|| ||b_p||, which is integrable, so
dominated convergence gives B_T^dagger U^T P_I B|00> -> 0 (finite rank). Then

  ||K_T|00>|| <= ||(I-P_I)B|00>|| + o(1) = sqrt(1-c) + o(1),

and since ||U^T B|00>||=1 with orthogonal decomposition,

  ||E_T|00>||^2 = 1 - ||K_T|00>||^2 >= c - o(1).

## 3. Relation to the earlier results

- Exact recovery for T>=2 was excluded via input 01 and edge rays
  (0828861). This result needs neither: it gives a time-independent lower
  bound for input 00 from the bound-state band.
- The same fiber computation gives nonzero overlaps <f,b_{p0}> for inputs 01
  (3sqrt2/4) and 10 (-3i sqrt2/4), the on-site pairs, so by the same Steps
  3-4 they also leak persistently. Input 11 has zero overlap with this f; its
  status is not determined here (the "-" vector of Eq.(14) at p=-pi/4 was not
  checked).
- No relation is claimed between c and the sampled values p_01(T) of the
  previous report.

## 4. What the verifier certifies and what it does not

[Script](../scripts/verify_thirring_approximate_recovery.py),
[record](2026-11-09--thirring-approximate-recovery.txt),
[JSON](2026-11-09--thirring-approximate-recovery.json): **16/16 exact checks**
(SymPy 1.14.0, Q(i,sqrt2), no floating point, no time evolution).
Certified: the eigenvector identity of Step 1, antisymmetry, the algebraic
identities of Step 2, the overlaps and the fiber weight 16/25.
Not certified (written proof only): the case analysis of Step 2, the Riesz
continuity of Step 3, absolute continuity and Riemann-Lebesgue of Step 4, and
the fiber decomposition itself. Eq.(14) was taken from the source and checked
independently on the lattice; the remaining statements of the source (Lemma
2, Proposition 1) are not used.

## 5. Failed first run

The run at `dd4e547` gave 14/16: I had predicted zero overlap for inputs 01
and 10, overlooking that they are on-site opposite-component pairs and meet
f(0). The computed values were exact and are not used in Steps 1-4. Record
kept as `2026-11-09--thirring-approximate-recovery-failed-run-1.{txt,json}`;
expectations corrected and labelled in the script at `f5c0d16`.

## 6. Closure under the contract

`APPROXIMATE_RECOVERY_EXCLUDED`. Per contract Sec. 5 this abandons approximate
recovery with this code and rule. Not opened: other codes or resources, gate
composition, Lean formalization, external review, promotion.
Waiting longer does not bring this code back into the free frame, even
approximately.
