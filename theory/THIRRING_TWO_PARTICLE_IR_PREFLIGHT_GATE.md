# Thirring two-particle low-energy preflight (coexistence, option (c))

2026-11-09. Author Claude (Opus 5.5). User authorization: «adelante con el
preflight de (c)», after committee brief 002 and the quantifier decision of
2026-11-09 (`reports/2026-11-09--coexistence-quantifiers-options.md`, last
section). **Contract 1 of the 2-contract operational budget** of the Thirring
coexistence line. Initial evidence status: `OPEN`. Frozen and committed
before any verifier or calculation for the observables below.

## 1. Known (with sources)

- Rule U=FJ: one-particle W(q)=[[nu e^{iq}, -i mu],[-i mu, nu e^{-iq}]],
  cos omega(q) = nu cos q; interaction phase e^{i chi} on same-site
  opposite components, applied before F (`sources/1804.08508v1.pdf` pp.3-4,
  Eqs.(1)-(4); `sources/1711.03920v1.pdf` p.1-2, Eq.(2)).
- Two-particle fiber at half-total momentum p, half-relative momentum k:
  free eigenphases omega_sr(p,k) = s omega(p+k) + r omega(p-k)
  (1804.08508 p.4). Four-fold degeneracy: (+,+,k),(+,+,-k),(-,-,pi-k),
  (-,-,k-pi) (p.7-8; 1711.03920 Lemma 1, p.3).
- Scattering solutions, Eq.(18) p.9: each generalized eigenvector contains
  the doubler term v^{--}_{k-pi} (for the + solution) with the same weight as v^{++}_k, and
  transmission T_+ = [g_+(p+k)+e^{-i chi} g_+(p-k)] / [g_+(p-k)+e^{-i chi}
  g_+(p+k)], Eq.(16) p.8; T_- Eq.(17) p.9; g_s(q) = -i(s sin omega(q) +
  nu sin q), p.3. The paper calls this momentum transfer between Brillouin
  regions "Fermion-doubled particles" (abstract, p.1).
- Bound states: proper eigenvector iff T_+=0 or T_-=0 for complex
  k = k_R + i k_I with k_R in {0, ±pi/2, pi}, k_I<0; unique for each
  (chi, p) with e^{i chi} not in {1,-1} (p.10, Eq.(19); 1711.03920 Lemma 2,
  p.3, which also requires p != z pi/2 and e^{i chi} != e^{±2ip}).
  At p=0: point spectrum {e^{-2i omega(k~)}, 1}, with eigenvalue 1 an
  infinite-dimensional eigenspace spanned by the v^{+-}_k, present also at
  chi=0 (1804.08508 p.13; 1711.03920 p.4).
- Neither paper computes the low-energy (small mu, small p) behaviour of the
  bound band, its curvature, or the low-energy weight of the doubler channel
  (both papers read in full in this session; no such section).
- Free one-particle low-energy coefficient: omega^2 = omega0^2 + c_f^2 q^2 +
  O(q^4), omega0 = arcsin mu, c_f^2 = omega0 nu / mu
  (`theory/THREE_VELOCITIES.md` lines 64-66 give F = arcsin(m) sqrt(1-m^2)/m
  for the standard Dirac walk; identification with this W to be checked by
  the verifier, not assumed).
- Gate resource: T=1, D=diag(1,z,z,1) on the M=1 code
  (`reports/2026-11-08--thirring-growing-time.md`). Author derivation before
  freezing: since J acts first and the code inputs 01, 10 are the only
  same-site opposite-component pairs, U B = F J B = F B D for every mu; to be
  certified symbolically in mu (O1).
- Prior art on the coexistence theme, not local: Childs, Gosset, Webb,
  "Universal computation by multiparticle quantum walk", Science 339 (2013)
  791, cited as ref. [42] in 1804.08508 p.2 (designed graphs, not a fixed
  translation-invariant rule) `[UNVERIFIED]` beyond that citation.

## 2. Explored before freezing (declared)

- Reading of 1711.03920 pp.1-8 and 1804.08508 pp.1-16 (this session).
- Committee arithmetic (brief 002): omega0 ≈ 0.644 and c_f^2 ≈ 0.858 at
  mu=3/5; unverified by script.
- The O1 derivation above (one line, by hand).
- A partial hand manipulation of T_+=0 at p=0, chi=pi/2, k=i kappa, stopped
  without a result (a sign condition with k_I<0 was left unresolved). No
  value of any observable below was obtained. No code was run.

## 3. Quantifier order (cuantificadores), as decided 2026-11-09

- **Family F (frozen):** chi = pi/2 fixed (z=i), mu in (0,1),
  nu = sqrt(1-mu^2). Limit: mu -> 0 with continuum scaling of momenta
  (total momentum P = p1+p2 = 2p and relative momenta of order mu) and
  quasienergies of order mu. No other chi, no other family, no point of F
  chosen after seeing results.
- **Same points (Q1-B):** coexistence is required at the same points of F.
  Properties to be preserved along the limit:
  (G) the gate D at T=1 holds exactly at every point of F;
  (R) the relativistic properties of Sec. 4 hold in the limit mu -> 0.
- **Sector (Q2-A):** the two-fermion sector of the code's carriers, with the
  interaction active (opposite-component, same-site subspace, the subspace P
  of 1804.08508 Eq.(8)). The low-energy window is the (+,+) branch near
  total quasienergy 2 omega0 and small P.
- **Frames (Q3-A):** only for O1: free frame F B, defined in advance,
  independent of the logical input.
- **Resources (Q4-A):** the rule only. No ancillas, measurement or feed-forward.

## 4. Observables (all exact or symbolic in mu; limits taken analytically)

- **O1.** U B = F B D with D=diag(1,i,i,1) for symbolic mu (exact).
- **O2.** Free branch: omega0(mu), c_f^2(mu) from the exact expansion of
  omega(q)^2; limits omega0/mu and c_f as mu -> 0.
- **O3.** Bound branch in the low-energy window: existence of the solution
  of T_+=0 or T_-=0 near p=0 for small mu; its quasienergy at P=0,
  M_b(mu) (below 2 omega0, measured from the same zero as the (+,+)
  threshold); its expansion omega_b(P)^2 = M_b^2 + c_b^2 P^2 + O(P^4);
  limits M_b/mu and c_b/c_f as mu -> 0. The infinite-dimensional
  eigenvalue-1 space at p=0 (v^{+-}, quasienergy 0) is outside the (+,+)
  window and is reported separately, not used for (R).
- **O4.** Doubler channel: for an incoming (+,+) state at relative momentum
  k = mu K, total momentum P = mu Q, the outgoing weight carried by the
  doubler components (v^{--}_{k-pi}, v^{--}_{pi-k}) of Eq.(18), defined by a
  wave-packet (in/out) analysis stated in the report before evaluation;
  its limit as mu -> 0 at fixed K, Q.

## 5. Verdicts (frozen; OPEN has the same weight)

- `TWO_PARTICLE_IR_REGIME_IN_DECLARED_FAMILY`: O1 holds on all of F; c_f -> 1
  and omega0/mu -> 1; every bound branch in the window has c_b/c_f -> 1 and
  M_b/mu -> a limit in (0, 2]; the doubler weight -> 0. Gate and regime then
  coexist at the same points of F in the sense of Sec. 3. This is **not**
  composable universality, not an interacting relativistic QFT limit, and
  not a statement outside the two-particle sector.
- `IR_BOUND_BRANCH_RELATIVISTIC / DOUBLER_CHANNEL_OPEN`: as above, but O4 not
  decided within the bound of Sec. 6.
- `NO_COMMON_TWO_PARTICLE_IR_CONE_IN_DECLARED_FAMILY`: proved that a bound
  branch exists in the window for all small mu with c_b/c_f not tending to 1.
- `DOUBLER_TRANSFER_PERSISTS_IN_IR`: proved that the doubler weight has a
  nonzero limit as mu -> 0 for some fixed K, Q.
- `GATE_NOT_ALONG_FAMILY`: O1 fails on F (then (G) is lost; the regime
  results are still reported).
- `OPEN_AFTER_BOUNDED_EXACT_ATTEMPT`: none of the above decided within
  Sec. 6. Recorded and stopped, not converted into a pass or fail.

If no bound branch exists in the window for small mu, that is not a
negative: O3 is then reported as "no bound branch", and (R) rests on O2 and O4.

## 6. Method, budget, stop rules

- Exact algebra first: SymPy with mu symbolic, series expansions in mu and
  P, exact limits. Implicit equations (T_±=0) are solved by series in mu
  with stated order, or by exact closed form if available. Floating point
  may appear only in a separately labelled illustration file and never
  feeds a verdict.
- One permanent verifier `scripts/verify_thirring_two_particle_ir.py`,
  committed before its first run; failed runs retained.
- Bound: one working session. No chi scan, no other family, no change of
  sector, code or resources. No many-body or finite-density calculation.
- Stop at the first decided verdict for O3 and O4 or at the bound.

## 7. What abandons what (Q5)

- A demonstrated negative (`NO_COMMON_TWO_PARTICLE_IR_CONE_IN_DECLARED_FAMILY`
  or `DOUBLER_TRANSFER_PERSISTS_IN_IR`) **discards the family F (chi=pi/2)
  and the two-particle sector only**; it does not exclude the Thirring model.
- Operational: this is contract 1 of 2. A positive or partial result does
  not reset the count. After contract 2, mandatory closure and balance; if
  the coexistence objective is not reached, the line stops as OPEN unless
  an exclusion is demonstrated in scope.

## 8. Review and status

Author result PRELIMINARY. Cross-family reviewer named in advance: Grok via
`revision-ciega` (sending requires the user's explicit permission at that
time). Blocking objection: any error in an exact identity, series or limit
on which a verdict rests. No promotion without a separate user decision.
Report: `reports/2026-11-09--thirring-two-particle-ir.md`, citing this
contract's commit.
