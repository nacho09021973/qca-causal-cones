# Thirring: approximate recovery of the microscopic code at growing times

2026-11-09. Author Claude (Opus 5.5). The user chose the option
"Contrato aproximado" offered from `state/ROADMAP_2026-11-09.md`; the Lean
alternative of that roadmap is not executed under this contract.
Initial evidence status: `OPEN`. This file is written and committed before
any derivation or code for the question below.

## 1. Known (with sources)

- Rule U=FJ, W=[[nu T, -i mu],[-i mu, nu T^{-1}]], J=prod_x exp(i chi
  n_R(x) n_L(x)); `sources/1804.08508v1.pdf` p.3, Eq.(1), as already used in
  `reports/2026-11-08--thirring-exact-recovery.md` Sec. 2.
- Code: M=1, two fermions A=(R|0>,L|1>), B=(R|1>,L|0>) at positions {0,1},
  opposite Gamma sectors, isometry B on logical inputs 00,01,10,11; free
  output frame B_T=F^T B. mu=3/5, nu=4/5, chi=pi/2 (z=i), infinite line.
- T=1: UB=FBD, D=diag(1,z,z,1), exact entangling gate (same report, Sec. 2).
- For every integer T>=2 there is no matrix V with U^T B=B_T V
  (report Secs. 3-4, commit 0828861, clarified dbfd6d8; one sealed opus
  review, "se sostiene"; PRELIMINARY, not promoted).
- Lower bound p_01(T) >= |z-1|^2 mu^4 nu^{8T-6}/(1+nu^{2T-1})^2 (report
  Sec. 5). It tends to zero, so it does not decide approximate recovery.
- Exact rational p_01(T) at T=2,3,4,6,8,12 lies between 0.16 and 0.57 (report
  Sec. 6 table). These are samples; they decide no limit and are not
  evidence for this contract's verdict.

## 2. Frozen question

Same rule, code, parameters, output frame and infinite line as Sec. 1. No
auxiliaries, controls on F or J, measurement, postselection, change of
code, mass, coupling, profile or geometry. Define

  K_T = B_T^dagger U^T B,   E_T = (I - B_T B_T^dagger) U^T B,
  ell_T = ||E_T||^2   (operator norm; = maximal leakage over code inputs).

Since B_T is an isometry, U^T B - B_T V = E_T + B_T(K_T - V) with
orthogonal ranges, so

  max(||E_T||, ||K_T - V||) <= ||U^T B - B_T V||
                            <= (||E_T||^2 + ||K_T - V||^2)^{1/2}.

**Question.** Does there exist a sequence T_n -> infinity, phases theta_n
and a fixed 4x4 unitary V that is entangling, such that

  ||U^{T_n} B - e^{i theta_n} B_{T_n} V|| -> 0 ?

Equivalently: ell_{T_n} -> 0 and K_{T_n} - e^{i theta_n} V -> 0.

"Entangling" (logical order A,B): V is not of the form e^{i a}(u tensor w)
nor e^{i a}(u tensor w) SWAP. Small leakage alone, or entanglement of one
output state, does not count.

## 3. Admitted routes (bounded analytic attempt)

Order of work, from the roadmap; none of these is a result yet.

R1. Re-read the exact proof and identify which information is lost as the
    ray weights nu^{2T-1} go to zero.

R2. Two-particle scattering structure. Read the Thirring two-particle
    solution in `sources/1711.03920v1.pdf` (bound states, scattering) and,
    if needed, `biblioteca/entropy-27-00198.pdf`, citing page numbers. Whether
    that solution covers this encoding, these parameters and this sector is
    `[UNVERIFIED]` until read. Candidate criteria to derive, not assumed:
    (a) if some code vector has nonzero weight on a two-particle bound state
        of U, that weight cannot appear in K_T at large T, giving
        liminf ell_T > 0;
    (b) if the limit Omega B = lim_T F^{-T} U^T B exists in norm on the code
        (no bound-state weight), then ell_T -> ||(I - BB^dagger) Omega B||^2
        and K_T -> B^dagger Omega B, which decides the question directly.
    Each step (existence of the limit, the weak-convergence argument,
    applicability of the published solution) must be proved or cited, not
    assumed from scattering-theory analogy.

R3. A uniform or asymptotic lower bound on p_01(T), or a spectral
    expression of K_T with controlled errors.

R4. Computation only to check a concrete derived identity (e.g. a
    predicted limit of K_T or of p_01). Before running: a permanent
    verifier in `scripts/`, committed with its frozen list of times and
    tolerance rules. Exact arithmetic where the quantity is certified. A
    longer table of times is not a substitute for the argument and must not
    feed a verdict.

## 4. Verdicts

- `APPROXIMATE_RECOVERY_EXCLUDED`: proof that liminf_{T->inf} ell_T > 0
  (or liminf p_01(T) > 0), or another proved obstruction to every
  subsequence in the sense of Sec. 2. Closes this route for this code only;
  not a no-go for the Thirring QCA, other codes or other resources.
- `LEAKAGE_VANISHES_GATE_NOT_ENTANGLING`: ell_{T_n} -> 0 proved along some
  subsequence, but every limit point of K_{T_n} modulo phase is
  non-entangling.
- `APPROXIMATE_ENTANGLING_GATE_ALONG_SUBSEQUENCE`: explicit T_n, explicit
  bounds on ell_{T_n} and ||K_{T_n} - e^{i theta_n} V|| tending to zero, and
  an entangling limit V. This is a gate resource, not composable
  universality, preparation/readout or compatibility with the relativistic
  regime.
- `OPEN_AFTER_BOUNDED_ANALYTIC_ATTEMPT`: R1-R3 attempted, no proof or
  construction. Record and stop.

## 5. Stop rules and what abandons the line

- No exact-recovery search (closed for T>=2). No parameter, code or
  architecture change inside this contract. Results valid for general
  0<mu,nu<1, z != 1 may be stated as such, but no parameter is selected.
- No time sweeps beyond R4's frozen list; no fitted tolerances.
- Abandon this line (approximate recovery with this code and rule) if:
  the result is `APPROXIMATE_RECOVERY_EXCLUDED` or
  `LEAKAGE_VANISHES_GATE_NOT_ENTANGLING`; or if every route in R2-R3
  requires an unproved asymptotic assumption (e.g. existence of the limit
  Omega B), in which case the verdict is OPEN, not a conditional claim.
- No composition of gates, other codes or Lean work opened by this contract.

## 6. Status discipline

Author result PRELIMINARY. No external review (`revision-ciega`,
`sanedrin`) or promotion without separate explicit user authorization.
Report: `reports/2026-11-09--thirring-approximate-recovery.md`, citing this
contract's commit.
