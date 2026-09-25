# NONCORNER_SIGNALING_ONE_STEP — preregistered execution

**Verdict: `NONCORNER_SIGNALING_CONSTRUCTED`.**

Execution of the preregistered contract
[`NONCORNER_SIGNALING_GATE.md`](../theory/NONCORNER_SIGNALING_GATE.md),
§10 steps 0–5, in order. The contract was not modified. No commit, no push,
no promotion of `state/CURRENT_STATE.md`.

## 1. Preflight

| Item | Result |
| --- | --- |
| `HEAD` | `a1396d45a70be8f8bc6b34a014c2ff83a0911750` |
| Baseline match | `BASELINE_MATCH` |
| Tracked contamination before execution | none (`git status --porcelain -uno` empty) |
| Untracked files present | four; **not touched** (two debate `.log`, one audit `.md`, `scripts/__pycache__/`) |
| Files read in full before calculating | the contract, `ALICE_LOCAL_PREPARATION_WITNESS.md`, `verify_signaling_witness.py`, `verify_directional_saturation.py` |
| Code modified before step 0 | none |

## 2. Step 0 — binding support certification

**`STEP_0_PASS`.**

Certified exactly and algebraically from the frozen symbol, by extracting the
Laurent support of `walk2()` entry by entry and comparing with the blocks of
`exact_blocks()`. Both give the same set, and it is the preregistered one.

**Scope of that agreement (repair MR1).** These two extractions are **not**
independent: both run the same `laurent(...) * prod(Z)` / `Poly` /
`power - 1` pipeline, merely aggregated differently, so a fault in `laurent()`
would defeat both alike. The entry-by-entry pass certifies the per-entry
*attribution* claimed in contract §3, not the pipeline itself. Genuine
independence was supplied by the independent review, which re-transcribed
(5.15) onto the torus from scratch and reproduced the same 14 displacements.

`supp K_1`, the 14 displacements:

```
(+1,+1,+1) (+1,-1,+1) (-1,+1,+1) (-1,-1,+1)      from W_11 = c1 c2 z3
(+1,+1,-1) (+1,-1,-1) (-1,+1,-1) (-1,-1,-1)      from W_22 = c1 c2 z3^-1
(+1,+1, 0) (+1,-1, 0) (-1,+1, 0) (-1,-1, 0)      from W_12, W_21
(+1, 0, 0) (-1, 0, 0)                            from W_12, W_21
```

Per-entry attribution matches §3 exactly, no stored block is zero, and every
entry is exact. The support is symmetric under `y -> -y`, so the
displacement/reachable-site convention is immaterial.

**Domain derived from the certified support, not assumed.** Of the 14
reachable sites, (D1) `||y||_2 > 1` removes `(+-1,0,0)` and (D3) non-vertex
removes the eight corners, leaving

```
admissible = { (1,1,0), (1,-1,0), (-1,1,0), (-1,-1,0) }
```

exactly the four preregistered points. Recorded exclusions, each an exact
zero rather than a search: the eight edges with a zero in coordinate 1 or 2
— `(+-1,0,+-1)` and `(0,+-1,+-1)` — have `K_1(0,y) = 0`; the axis sites
`(+-1,0,0)` are micro-accessible but satisfy `||y||_2 = 1`, null-separated
from the encoding event.

## 3. Exhaustive table

Frozen preparation reused unchanged: `chi(0) = -3 down/4`,
`||P chi||^2 = 9/16`, `||Q chi||^2 = 7/16`, `||chi|| = 1`. No symmetry was
assumed; all four sites were evaluated independently.

| `y` | `K_1(0,y)` | `a(y)` | `r(y)` | `M(y)` | `Tr M(y)` | `Delta p_B(y)` | `M(y)=0` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(1,1,0)` | `[[0,-i/4],[i/4,0]]` | `(3i/16) up` | `(-i/32) up` | `diag(-3/256, 0)` | `-3/256` | `3/128` | **false** |
| `(1,-1,0)` | `[[0,i/4],[-i/4,0]]` | `(-3i/16) up` | `(i/32) up` | `diag(-3/256, 0)` | `-3/256` | `3/128` | **false** |
| `(-1,1,0)` | `[[0,-i/4],[i/4,0]]` | `(3i/16) up` | `(-i/32) up` | `diag(-3/256, 0)` | `-3/256` | `3/128` | **false** |
| `(-1,-1,0)` | `[[0,i/4],[-i/4,0]]` | `(-3i/16) up` | `(i/32) up` | `diag(-3/256, 0)` | `-3/256` | `3/128` | **false** |

`rho_B^(0) != rho_B^(1)` was also checked **directly** from the reduced
states, not only through `M`. At every admissible site

```
p_0 = 25/1024 ,   p_1 = 49/1024 ,   p_1 - p_0 = +3/128 .
```

These are exactly the frozen vertex's probabilities **exchanged**: at
`(1,1,1)`, `p_0 = 49/1024` and `p_1 = 25/1024`. The magnitude of the effect
is identical, `3/128`, and its sign is opposite — at the vertex encoding
lowers Bob's occupation, at these sites it raises it. The state difference
was verified to equal `2M` on the one-particle block with
`-Tr(2M)` in the vacuum slot, confirming on the computed objects that `M` is
the complete invariant.

## 4. Mechanism

**A `z3` parity selection rule, certified exactly.** In the prepared state at
`T = 2` the internal components are segregated by the parity of `x3`: the
`up` component occupies odd `x3`, the `down` component even `x3`. One further
step exchanges the two, because the diagonal symbol entries carry `z3`
exponent `+-1` while the off-diagonal entries carry exponent `0`. Hence at
`T = 3` the `up` component lives on even `x3` and `down` on odd `x3`.

The four admissible sites have `x3 = 0`. **Only the `up` channel can arrive
there**, and both arms do: `a(y)` and `r(y)` are purely `up`, with the same
magnitudes `3/16` and `1/32` as the frozen vertex arms. The vertex has
`x3 = +-1`, so there only the `down` channel arrives. One parity rule
accounts for both geometries.

The sign difference is a **separate, computed fact** and is *not* explained by
the parity rule (repair MR2): parity fixes which internal channel carries the
interference, and says nothing about the relative phase of `a` and `r`. What
was computed is the ratio `a_up / r_up = -6` at these sites against `+6` at
the vertex. At the vertex `a` and `r` are both negative reals and add in
`v_0`; here `a = +-3i/16` and `r = -+i/32` have opposite phase, so they
subtract in `v_0` and add in `v_1`:

```
v_0 = a + r = +- 5i/32 ,    v_1 = -a + r = -+ 7i/32 .
```

**Explicit local effect (P2).** Both of the following are even local
projections of norm one on Bob's two-mode Fock space, and both give the same
exact response:

```
E_novac = diag(0,1,1,1)   ->  delta = |Tr E (rho_1 - rho_0)| = 3/128
E_up    = diag(0,1,0,0)   ->  delta = 3/128
```

so `D(rho_B^(0), rho_B^(1)) >= 3/128 > 0` at each of the four sites. `E_up`
identifies the distinguishing component explicitly: it is **Bob's spin-up
occupation**, where at the vertex it was spin-down. No optimization of `E`
was performed or is claimed.

**Where the contract's structural note was half right.** §10 step 4
anticipated that `a(y)` would be spin-flipped at these sites — **certified,
correct**. It further suggested that part of `M(y)` might then sit
off-diagonal, where the occupation witness is blind. **That does not occur
here**, but the reason must be stated carefully (repair MR3). The parity rule
forces `r(y)` into the `up` channel too, so `a` and `r` are collinear; that
gives `M(y)` rank **at most** one and no more. Collinearity alone does not
exclude the blind case: for `r = lambda a` with `lambda` purely imaginary,
`M = 2 Re(lambda) a a^dagger = 0` exactly. What excludes it here is the
computed value `Re(a_up conj(r_up)) = -3/512 != 0`, equivalently the real
ratio `a_up / r_up = -6`. So the occupation witness is not blind at these
sites **as a matter of arithmetic, not of structure**. The contract's
requirement that a null occupation response never be read as state equality
did not bind in this execution; it was not thereby unnecessary, since nothing
before the calculation excluded the blind case.

## 5. Verdict

**`NONCORNER_SIGNALING_CONSTRUCTED`**, satisfied at **all four** admissible
sites rather than at one:

- **(P1)** `M(y) != 0` exactly at each, with `M(y) = diag(-3/256, 0)`.
- **(P2)** explicit even local projections `E_novac` and `E_up` with exact
  `delta = 3/128 > 0`.
- **(P3)** admissibility recertified at each site: `||y||_2 = sqrt(2) > 1`,
  `||y||_inf = 1`, `K_1(0,y) != 0`, two nonzero coordinates.

Answering the gate's physical question: **the locally-prepared signalling
mechanism is not exclusive to the corner.** Within the frozen protocol at
`Delta T = 1`, it is present at every admissible non-vertex site, with the
same magnitude as at the vertex.

## 6. Claim ceiling

Binding, per §9 of the contract.

- **The `l_inf`/`l_2` gap is not thereby shown irrelevant.** Admissibility
  *is* that gap: every admissible site satisfies `||y||_inf <= 1 < ||y||_2`.
  What is refuted is **vertex-exclusivity**, not dependence on the mismatch
  between the microscopic and emergent balls.
- This adds finite witnesses. It establishes **no** optimality, minimality,
  optimal measurement, minimal preparation time, scaling, asymptotics,
  channel capacity, experimental feasibility, or any claim about our
  universe.
- It does **not** enlarge or amend the frozen vertex witness, whose bytes and
  scope are unchanged.
- Every admissible site lies inside the exact microscopic causal support.
  **No microcausality violation of the model is claimed or implied.**
- `Delta T = 1` throughout. Nothing here speaks to `Delta T = 2`, which the
  contract declares a separate successor gate.
- The other seven vertices were **not** examined; `(1,1,1)` was recomputed
  only as a consistency check against the frozen witness, and reproduced.
- Nothing reopens the optimal-D gate, the axial gate,
  `GATE_COMPLETITUD_AXIAL_N3`, or the experimental question.

## 7. Validation

All executed from the repository root, all exit status zero:

```text
python3 scripts/verify_directional_saturation.py --noncorner-gate-only   20/20 exact checks
python3 scripts/verify_directional_saturation.py                         27/27 checks
python3 scripts/verify_directional_saturation.py --local-preparation-only 21/21 exact checks
python3 scripts/verify_signaling_witness.py                              17/17 exact checks
git diff --check                                                         clean
```

Implementation isolation: one file modified, `scripts/verify_directional_saturation.py`,
with **168 insertions and 0 deletions** — one added function
`verify_noncorner_gate()` plus one `elif` branch in the CLI dispatch. No
pre-existing function body was altered, the default `main()` path is
unchanged and still passes 27/27, and no new script was created. Frozen
witnesses, `verify_signaling_witness.py` and the contract are untouched.
Exact arithmetic throughout: no floating point, tolerance, sampling, search
or optimization anywhere in the new path.

## 8. Independent review

**Verdict: PASS.** Three mandatory repairs, all textual, none changing any
computed quantity or the verdict; all three are applied above and marked
`MR1`, `MR2`, `MR3`. See
[the review](2026-09-16--noncorner-signaling-gate-independent-review.md).
This is one separate agent's independent review, not external human review,
consensus, or ratification.

The reviewer re-transcribed (5.15) onto the torus from scratch, without using
`exact_blocks()`, `laurent()` or the new function as authority, and
independently reproduced: the 14 displacements and their per-entry
attribution; `chi` by two routes (position-space convolution and Laurent
coefficients of `adj(W)^2 (0,1)^T`), 38 sites, `chi(0) = -3 down/4`; every
entry of the §3 table; the exchanged vertex probabilities; and `c_IR = 1`,
which underwrites (D1). It confirmed that **the binding stop rule was
honoured** — the domain is computed from the certified support and only then
compared with the four sites — and it proved the `x3` parity rule
algebraically rather than by enumeration. It found **no overclaim** in §6.

**Strengthening supplied by the review.** The exact trace distance is
`||rho_1 - rho_0||_1 = 3/64`, so `D = 3/128`: the effect bound is not merely
satisfied but **saturated**, and the exhibited projection is optimal *for
this pair of states*. Confirmed here independently. This is a statement about
two computed reduced states, **not** protocol optimality, optimal
preparation, or optimality over sites or interventions; the ceiling of §6 is
unchanged. The reviewer also verified that `E_up` gives `delta = 0` at the
vertex, confirming the channel selectivity of the parity rule.

**Evidence gaps in the certificate, recorded rather than concealed.** The
reviewer verified independently that each of these holds; they are gaps in
what `verify_noncorner_gate()` *checks*, not defects in the result:

1. Bob's vacancy at the encoding event is not certified at the four sites. It
   holds — every `x1` exponent of `chi` is even, so `chi(y) = 0` at all four
   and at the vertex — and the frozen witness treats it as a named control.
2. The certificate does not check `||out_b|| = 1`, `Tr rho_B = 1` or
   positivity, although both sibling verifiers do and the effect bound
   presupposes states. All three hold.
3. The parity rule is executed as an enumeration over populated sites rather
   than as the algebraic argument the report states, and is not checked on
   the two arms separately — which is the step collinearity actually needs.
4. The completeness check pairs `states` with `results` positionally rather
   than by `y`: correct as written, order-fragile.
5. `E_up = diag(0,1,0,0)` is the projector onto "exactly one particle, spin
   up", not the number operator `n_up = diag(0,1,0,1)`. They agree in
   expectation here only because the two-particle block vanishes.
6. By-product, observed and correctly **not** claimed as a certified protocol
   symmetry: `a(y)` depends only on `sgn(y_2)`, and all four `M(y)` coincide.

## 9. Status

Result frozen at this report only, with the independent review of §8 and its
three repairs applied. **Promotion of `state/CURRENT_STATE.md` has not been
requested and is not performed here.** The certificate's recorded gaps
(§8.1–§8.4) should be closed before it is cited as standalone authority;
closing them changes the reviewed script and would require re-review of that
file.
