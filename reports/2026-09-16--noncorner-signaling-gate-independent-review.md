# Independent review: NONCORNER_SIGNALING_ONE_STEP preregistered execution

Date: 2026-09-16. **Verdict: PASS. Mandatory repairs: three, all textual;
none affects the verdict, the domain, or any computed quantity.**

This is a separate agent's independent adversarial review of the execution of
the preregistered contract
[`NONCORNER_SIGNALING_GATE.md`](../theory/NONCORNER_SIGNALING_GATE.md), not
external human review, multi-member consensus, or ratification. The reviewer
started cold, read `PROJECT_INSTRUCTIONS.md` and `state/CURRENT_STATE.md`
first, and treated every claim of
[`2026-09-16--noncorner-signaling-gate.md`](2026-09-16--noncorner-signaling-gate.md)
as something to be attacked rather than accepted. Neither `exact_blocks()`
nor the new `verify_noncorner_gate()` was used as authority for any
algebraic conclusion below: the symbol was re-transcribed from `walk2()`,
re-expressed on the torus, and every Laurent support, state, arm, `M(y)`,
probability and trace distance was rebuilt from scratch with independent
SymPy code. The earlier
[Alice-local preparation review](2026-09-16--alice-local-preparation-independent-review.md)
PASS was not used as authority either.

No reviewed input, canonical state, frozen theory file, script, debate log or
untracked artefact was edited. This report is the only file created. No
commit, no push, no promotion of `state/CURRENT_STATE.md`. All Python was run
as throwaway heredocs with `PYTHONDONTWRITEBYTECODE=1`; `scripts/__pycache__/`
retains its pre-existing mtime (`2026-09-16 14:22:09`, earlier than both the
script modification and the report) and was written by neither the execution
nor this review.

Baseline: `research/b-infinity-post-s4-gate`,
`HEAD = a1396d45a70be8f8bc6b34a014c2ff83a0911750`. Tracked working-tree
delta: `scripts/verify_directional_saturation.py` only.

| Reviewed input | SHA256 |
|---|---|
| `PROJECT_INSTRUCTIONS.md` | `e9a0a2724920cb97378e32e7b96190af64a5d57bb72bb4b15890f5f59ee6d77b` |
| `state/CURRENT_STATE.md` | `6419790a9db4e1ff4914ffb639fe40f029bb81cf92838e70714ea596f1124dfa` |
| `theory/NONCORNER_SIGNALING_GATE.md` | `6eeef53b58353835029d2027b625d1e1b51d20bd73b2bc4d7b636163b31cc8d7` |
| `theory/ALICE_LOCAL_PREPARATION_WITNESS.md` | `66475c218c33d56ba1a41912a7d101ce17c0550b1f93a35e2cb6e8d078a21024` |
| `theory/COUPLING_MAP_SIGNALING_WITNESS.md` | `9493cfa7135645acbc9dd8c10718cf33467632514fdd821d561c3257adaa6ae2` |
| `scripts/verify_directional_saturation.py` (working tree) | `1d1894730f83ea24808bb5e939492fe2144fdd97cdcf87961a0978da35ae4596` |
| `scripts/verify_directional_saturation.py` (at `HEAD`) | `37a769814d8e273a27568b2ff9a996a86580033c4cc7225e4a1f00cd208816de` |
| `scripts/verify_signaling_witness.py` | `4953009ebf838b98e0dd095e4cbeefdde1bc65a83ee716e96d1ce3eb9ee58d17` |
| `reports/2026-09-16--noncorner-signaling-gate.md` | `b49ca70767eba2a628d82e75eb1e68acbccc61ce549e69cc5db535b9e651f94d` |
| `reports/2026-09-16--alice-local-preparation.md` | `00f160f6a1c563297dc033ed45c565d17e363759a08922248763c888a4d3bd9e` |
| `reports/2026-09-16--alice-local-preparation-independent-review.md` | `af8e162ddc4da8250d37a5792dec9a624a51a5834960d9bb7d22475a07802206` |

---

## 1. Step 0 — independent certification of `supp K_1` — PASS

The symbol was re-transcribed from `walk2()` and rewritten directly on the
real torus, with `z_k = exp(i p_k)`, `c_k = (z_k + z_k^-1)/2`,
`s_k = (z_k - z_k^-1)/(2i)`, **without ever calling `laurent()`,
`exact_blocks()` or the new function**:

\[
W=\begin{pmatrix} c_1c_2z_3 & -c_1s_2+is_1\\ c_1s_2+is_1 & c_1c_2z_3^{-1}\end{pmatrix}.
\]

Independent checks on that transcription, with `conj` implemented on the
torus as `i -> -i`, `z_k -> 1/z_k`:

- `W^dagger W - I = 0` exactly, `det W - 1 = 0` exactly;
- `W^dagger = adj(W)` exactly, so `S = adj(W)` as the report asserts;
- `tr W / 2 = c_1c_2c_3`, i.e. CJWW (5.16).

Independent Laurent extraction (my own `Poly` on `W_{ij} z_1z_2z_3`, own
monomial bookkeeping) gives the per-entry supports

```
W_11 : (+-1,+-1,+1), each coefficient 1/4
W_22 : (+-1,+-1,-1), each coefficient 1/4
W_12 : (1,1,0)=i/4  (1,-1,0)=-i/4  (-1,1,0)=i/4  (-1,-1,0)=-i/4  (1,0,0)=1/2  (-1,0,0)=-1/2
W_21 : (1,1,0)=-i/4 (1,-1,0)=i/4   (-1,1,0)=-i/4 (-1,-1,0)=i/4   (1,0,0)=1/2  (-1,0,0)=-1/2
```

Consequences, all verified exactly:

- `|supp K_1| = 14`, and the set is exactly
  `{(+-1,+-1,+-1)} U {(+-1,+-1,0)} U {(+-1,0,0)}`;
- the per-entry attribution is **exactly** the one declared in contract §3:
  `W_11` carries the four vertices with third coordinate `+1`, `W_22` those
  with `-1`, and `W_12`, `W_21` carry `edges U axes` and nothing else;
- the support **is** symmetric under `d -> -d`, so the
  displacement/reachable-site convention does not change the domain. (It
  does change the individual blocks — `K_{(1,1,0)} != K_{(-1,-1,0)}` — but
  the report scopes the immateriality claim to the support, correctly.)
- every stored block is nonzero, and no entry contains `sp.Float`.

My blocks were then compared entrywise with `exact_blocks()`: identical keys,
identical matrices. The repo's `laurent()` pathway is therefore also correct,
but that is a conclusion of this review, not an input to it.

**Was the domain DERIVED or assumed?** Derived. In the new code the chain is
`blocks -> reachable = {-d} -> filter by (D1) and (D3) -> admissible`, and
only *afterwards* is `admissible == edges` asserted. (D2) is not a separate
filter because `reachable` is by construction `{y : K_1(0,y) = K_{-y} != 0}`.
Reproducing the same filtering with my own blocks:

```
reachable            : 14 sites
(D1) ||y||_2 > 1     : removes (+-1,0,0)        [||y||_2 = 1 exactly]
(D3) < 3 nonzero     : removes the 8 vertices
derived admissible   : {(1,1,0), (1,-1,0), (-1,1,0), (-1,-1,0)}
```

This equals the preregistered four points. Independently confirmed exact
zeros, i.e. exclusion by criterion and not by search:
`K_1(0,y) = 0` for all eight of `(+-1,0,+-1)`, `(0,+-1,+-1)`, and also for
`(0,+-1,0)`, `(0,0,+-1)`, `(2,0,0)` and `(2,2,0)`.

**The binding stop rule of §10 step 0 was genuinely honoured.** The
certification is a real derivation compared against a hard-coded target set,
not a rubber stamp; had the support differed, the first `require` would have
raised before any `M(y)` was formed, because `blocks` is computed before
`prepared` and every arm.

`c_IR = 1`, which underwrites (D1), was also re-derived rather than inherited:
entrywise series expansion gives
`W = I + i(p_1 sigma_1 - p_2 sigma_2 + p_3 sigma_3) + O(|p|^2)` exactly, whose
generator has eigenvalues `+-|p|`; and `omega = arccos(c_1c_2c_3)` has
`omega/|p| -> 1` along `(1,1,1)`, `(1,1,0)` and `e_1`. So `||y||_2 > 1` is the
correct strict test and `sqrt(2) > 1` holds at all four sites.

## 2. From-scratch reconstruction of `chi`, `a`, `r`, `M` — PASS

Two mutually independent reconstructions were run and cross-checked.

**(a) Position space.** Implementing the convention from first principles —
`K_t(x,z) = (W^t)_{x-z}`, states evolve by `S = W^dagger`, hence
`(S psi)_b = sum_d K_d^dagger psi_{b+d}` — and applying it twice to
`|0,down>` gives a state on **38 sites** with `||chi||^2 = 1`,
`chi(0) = -3 down/4`, support in `[-2,2]^3`.

**(b) Laurent generating vector.** Independently,
`chi_hat(z) = adj(W)^2 (0,1)^T`, which I verified equals the
Cayley-Hamilton form of the frozen witness,

\[
\hat\chi=\binom{-2fb}{2fa-1}
=\binom{2c_1c_2c_3(c_1s_2-is_1)}{c_1^2c_2^2(1+z_3^2)-1},\qquad f=c_1c_2c_3 .
\]

Coefficient extraction from (b) reproduces (a) site by site. Splitting
`P chi = -3 down/4` at the origin and `Q chi` elsewhere gives
`||P chi||^2 = 9/16`, `||Q chi||^2 = 7/16`, both nonzero, so the encoding is a
relative and not a global phase.

One further `S` step applied separately to `P chi` and to `Q chi` gives, with
`a(y) = (S P chi)_y`, `r(y) = (S Q chi)_y`, `M = a r^dagger + r a^dagger`:

| `y` | `K_1(0,y)` | `a(y)` | `r(y)` | `M(y)` | `Tr M` | `v_0` | `v_1` | `p_0` | `p_1` | `p_1-p_0` |
|---|---|---|---|---|---|---|---|---|---|---|
| `(1,1,0)` | `[[0,-i/4],[i/4,0]]` | `(3i/16) up` | `(-i/32) up` | `diag(-3/256,0)` | `-3/256` | `5i/32` | `-7i/32` | `25/1024` | `49/1024` | `+3/128` |
| `(1,-1,0)` | `[[0,i/4],[-i/4,0]]` | `(-3i/16) up` | `(i/32) up` | `diag(-3/256,0)` | `-3/256` | `-5i/32` | `7i/32` | `25/1024` | `49/1024` | `+3/128` |
| `(-1,1,0)` | `[[0,-i/4],[i/4,0]]` | `(3i/16) up` | `(-i/32) up` | `diag(-3/256,0)` | `-3/256` | `5i/32` | `-7i/32` | `25/1024` | `49/1024` | `+3/128` |
| `(-1,-1,0)` | `[[0,i/4],[-i/4,0]]` | `(-3i/16) up` | `(i/32) up` | `diag(-3/256,0)` | `-3/256` | `-5i/32` | `7i/32` | `25/1024` | `49/1024` | `+3/128` |
| `(1,1,1)` | `diag(0,1/4)` | `-3 down/16` | `-down/32` | `diag(0,3/256)` | `+3/256` | `-7 down/32` | `5 down/32` | `49/1024` | `25/1024` | `-3/128` |

Every entry of the report's §3 table is reproduced exactly, including the
per-site `K_1(0,y)` blocks — note that `K_1(0,y) = K_{-y}`, so `(1,1,0)` and
`(-1,1,0)` legitimately share a block while `(1,1,0)` and `(-1,-1,0)` do not.
`Delta p_B = 2|Tr M| = 3/128` at each of the four sites, and
`p_0 - p_1 = 2 Tr M` holds with the correct sign in every row.

**The "exchanged probabilities" claim is correct.** At the vertex
`(p_0,p_1) = (49/1024, 25/1024)`; at all four edge sites
`(p_0,p_1) = (25/1024, 49/1024)`. Same magnitude `3/128`, opposite sign: at
the vertex the encoding lowers Bob's occupation, at these sites it raises it.

No convention error was found. The independently reconstructed `evolve`
direction, the `blocks[-y]`-applied-as-`.H` keying, and the `S = adj(W)`
identity all check out, and the two reconstruction routes agree.

## 3. The `x3` parity selection rule — PROVED, not merely spot-checked

The report's mechanism is correct and admits a two-line algebraic proof,
which I supply (the executed check verifies it only by enumerating populated
sites; that is sound for this protocol but is not the proof the report
asserts).

Read off the `z_3` exponents of `S = adj(W)`:

```
S_11 = W_22 : z3 exponent -1   (odd)      S_12 = -W_12 : exponent 0 (even)
S_22 = W_11 : z3 exponent +1   (odd)      S_21 = -W_21 : exponent 0 (even)
```

so `S` has **odd** `z_3` parity on the diagonal and **even** off the
diagonal. Hence, for any state whose `up` component has all-odd `x_3` and
whose `down` component has all-even `x_3`:

```
(S psi)_up   = S_11 psi_up + S_12 psi_down :  odd+odd = even,  even+even = even
(S psi)_down = S_21 psi_up + S_22 psi_down :  even+odd = odd,  odd+even  = odd
```

so one step exchanges the two parity classes, exactly as claimed. The
hypothesis holds for `chi`, directly from the generating vector: the `up`
entry `2c_1c_2c_3(c_1s_2 - is_1)` carries `c_3`, hence `z_3` exponents
`{-1,+1}` (odd); the `down` entry `c_1^2c_2^2(1+z_3^2)-1` carries exponents
`{0,2}` (even). Confirmed symbolically, and confirmed on all 38 populated
sites. After one more step the exponents are `{-2,0,2}` for `up` and
`{-1,1,3}` for `down`, as the rule requires.

**Does it genuinely explain collinearity?** Yes, and the argument needs one
step the report leaves implicit, which I checked: the rule holds *separately*
for `P chi` (origin, `down`, `x_3 = 0` — even, compliant) and therefore for
`Q chi = chi - P chi`. Applying `S` to each arm separately then forces both
`S P chi` and `S Q chi` to be purely `up` on even `x_3`. The four admissible
sites have `x_3 = 0`, so `a(y)` and `r(y)` are both proportional to `up`:
collinear. Verified on every populated site of both arms.

Collinearity gives `M = 2 Re(a_1 conj(r_1)) |up><up|`, hence diagonal and of
rank at most one. **It does not by itself give rank exactly one, nor
`Tr M != 0`**: a collinear pair with purely imaginary ratio has `M = 0`
identically, which is precisely the blind case the contract warned of. Here
`a_1/r_1 = -6`, real, so `Re(a_1 conj(r_1)) = -3/512 != 0`. That is a computed
fact, not a corollary of the parity rule. See MR3.

At the vertex, `x_3 = +-1` is odd, so only the `down` channel arrives — also
confirmed. One parity rule does account for both channel geometries.

## 4. (P1), (P2), (P3) verified without the new helper — PASS

**(P1).** `M(y) = diag(-3/256, 0) != 0` at each of the four sites, from my own
arms. `M` is Hermitian. Exact rationals, no `sp.Float`.

**(P2).** Both effects were checked independently, as operators:

| `E` | `E^2 = E` | `E = E^dagger` | `0 <= E <= I` | even (`[E, diag(1,-1,-1,1)] = 0`) | `||E||` | `delta = |Tr E(rho_1-rho_0)|` |
|---|---|---|---|---|---|---|
| `diag(0,1,1,1)` | yes | yes | yes | yes | 1 | `3/128` |
| `diag(0,1,0,0)` | yes | yes | yes | yes | 1 | `3/128` |

**No factor-of-two error.** I computed the trace distance itself rather than
accepting the bound: `rho_1 - rho_0 = diag(-3/128, 3/128, 0, 0)`, so
`||rho_1-rho_0||_1 = 3/64` and `D = (1/2)||rho_1-rho_0||_1 = 3/128`. The
supremum `max_{0<=E<=I} Tr(E(rho_1-rho_0))` equals the sum of positive
eigenvalues, `3/128`, which equals `D`. The bound `D >= delta = 3/128` is
therefore correct **and saturated** at these sites. As a control, `E_up` gives
`delta = 0` at the vertex `(1,1,1)`, where the distinguishing channel is
`down` — the effect is genuinely channel-selective, as the report says.

**(P3).** At each of the four sites: `||y||_2^2 = 2 > 1`, `||y||_inf = 1`,
exactly two nonzero coordinates, `K_1(0,y) != 0` with the block exhibited.

**Is `M` the COMPLETE invariant, or only a sufficient witness?** Complete.
Proved here symbolically for *generic* complex two-vectors `a, r`, with no
reference to this protocol, using
`rho_b = (1 - ||v_b||^2)|vac><vac| + v_b v_b^dagger`, `v_b = (-1)^b a + r`:

```
(rho_0 - rho_1) one-particle block  =  v_0 v_0^dag - v_1 v_1^dag  =  2M     (identically)
(rho_0 - rho_1) vacuum slot         =  -Tr(2M)                              (identically)
all rows/columns touching the vacant and doubly-occupied slots vanish
```

so `rho_0 = rho_1 <=> M = 0`, both directions, with no inequality anywhere.
The structural premise is also sound independently of any superselection
argument: the global state has exactly one particle, so Bob's two-particle
block vanishes and the vacuum/one-particle cross terms vanish because the
complementary environment states (`|vac_env>` versus a one-particle
`|phi_env>`) are orthogonal. Fermion parity is consistent with this but is
not needed to obtain the form. The report's §3 claim that this was confirmed
on the computed objects is correct; the code checks the `rho_0 - rho_1`
orientation, which is the one that gives `+2M`.

## 5. Isolation and regression audit — PASS

`git diff` against `HEAD = a1396d4`: **one file, 168 insertions, 0
deletions**, `git diff --check` clean. AST audit:

- `ast.parse` of the working file, with the single `FunctionDef`
  `verify_noncorner_gate` removed and the single
  `elif sys.argv[1:] == ['--noncorner-gate-only']: sys.exit(verify_noncorner_gate())`
  branch spliced out of the `__main__` guard, **round-trips to an AST dump
  byte-identical to `HEAD`**
  (`sha256 = 3fcacca951796c4c2846e8de6b1c2bb875c882d654bd1e828ae0d7959d463cdb`
  for both);
- pre-existing named top-level definitions altered: **none**;
- named top-level definitions added: **`verify_noncorner_gate` only**;
- all 26 module-level non-`def` statements (imports, `ROOT`, `SOURCE`,
  `SOURCE_SHA256`, `P1/P2/P3`, `PAULI`, `Z`, `CHECKS`, `F1`, `F2`, `B1`,
  `B2`, `CORNERS`, ...) identical, guard excepted;
- all 27 anonymous `@check`-decorated registration bodies identical and in
  the same order, so the default suite's registry is untouched;
- the new helper imports are inside the function body, so no import cycle
  executes on ordinary import or on the default path.

Frozen files, byte-compared against `HEAD`: all **IDENTICAL** —
`theory/COUPLING_MAP_SIGNALING_WITNESS.md`,
`theory/ALICE_LOCAL_PREPARATION_WITNESS.md`,
`theory/NONCORNER_SIGNALING_GATE.md`, `scripts/verify_signaling_witness.py`,
`state/CURRENT_STATE.md`. `git status --porcelain -uno` shows only the one
modified script. The contract is committed at `1b9a0bc` (freeze,
18:24:36) and `a1396d4` (stop-rule tightening, 18:38:28), both **before** the
working-tree script mtime — the preregistration genuinely precedes the
execution.

Verifiers, all re-run by this reviewer from the repository root with
`PYTHONDONTWRITEBYTECODE=1`, all exit status zero:

```text
python3 scripts/verify_directional_saturation.py --noncorner-gate-only    20/20 exact checks
python3 scripts/verify_directional_saturation.py                          27/27 checks
python3 scripts/verify_directional_saturation.py --local-preparation-only  21/21 exact checks
python3 scripts/verify_signaling_witness.py                               17/17 exact checks
```

The counts match the report exactly, and the `--noncorner-gate-only` per-site
printout matches my independently derived table row for row. The default
suite's two `SUPPORTED` numerical diagnostics retain that classification and
are not part of this gate, exactly as contract §7 demands.

## 6. Claim ceiling — ADEQUATE

The report's §6 ceiling is correct and, on the specific point flagged for
attack, unusually well drawn. The bullet

> Admissibility *is* that gap: every admissible site satisfies
> `||y||_inf <= 1 < ||y||_2`. What is refuted is **vertex-exclusivity**, not
> dependence on the mismatch between the microscopic and emergent balls.

is exactly right: `||y||_inf = 1` and `||y||_2 = sqrt(2)` at all four sites,
so the `l_inf`/`l_2` mismatch is the very reason these sites are in the
domain. Nothing in the execution weakens that dependence, and the report does
not claim otherwise. The remaining bullets (no optimality, minimality,
scaling, capacity, feasibility, no claim about our universe; no microcausality
violation; `Delta T = 1` only; the frozen vertex witness unamended; the other
seven vertices not examined; nothing reopened) are each accurate against what
was actually computed. The verdict statement in §5 carries its scope
explicitly ("Within the frozen protocol at `Delta T = 1`").

I found **no overclaim of scope or of physical significance** anywhere in the
report. The three defects below are all mechanism-attribution or
methodology-description defects inside otherwise correct sections.

## 7. The contract's §10 step-4 structural note — both halves verified

- **First half — CERTIFIED, and the report is right to say so.** The note
  predicted `a(y)` would be spin-flipped relative to `down` at `(+-1,+-1,0)`
  because the one-step block there comes only from the off-diagonal symbol
  entries. Independently confirmed: `K_{-y}` at those sites is purely
  off-diagonal and purely imaginary, `a(y) = K_{-y}^dagger (-3 down/4)` is
  `+-3i/16 up`, exactly spin-flipped.
- **Second half — correctly reported as NOT occurring.** The note suggested
  part of `M(y)` might then sit off-diagonal where the occupation witness is
  blind. It does not: `r(y)` is forced into the same `up` channel by the same
  parity rule, so `M(y)` is diagonal with `Tr M = -3/256 != 0` and the
  occupation witness is *not* blind. Confirmed independently. The report's
  observation that the "blind case" lock did not bind but was not therefore
  unnecessary is sound: nothing available before the calculation excluded it,
  and I verified that collinearity alone does not.

## 8. What the execution missed

None of the following changes the verdict. All were checked by me and all
pass; they are recorded because they belong in the evidence and are absent
from it.

1. **Bob's vacancy at the encoding event was not recorded at the four new
   sites.** The frozen witness makes this a named control (`chi(1,1,1) = 0`,
   Control 8) and the report inherits that protocol wholesale, yet never says
   whether Bob's site is occupied at `T = 2` at `(+-1,+-1,0)`. It is not:
   every `x_1` exponent of `chi` is even (`c_1^2`, `c_1 s_1` and `c_1^2 c_2^2`
   are all even in `z_1`), so `chi(y) = 0` for every `y` with odd first
   coordinate, which includes all four gate sites and the vertex. The four
   new witnesses therefore do have the vacancy property; this should be
   stated rather than left to inference.
2. **The new certificate never checks that the post-encoding global states
   are normalized, nor that `rho_B^(b)` are legitimate density matrices.**
   `verify_noncorner_gate()` checks `norm_squared(prepared) == 1` but not
   `norm_squared(outputs[b]) == 1`, and never checks `Tr rho = 1` or
   positivity — both sibling verifiers (`--local-preparation-only`,
   `verify_signaling_witness.py`) do. The effect bound `D >= delta`
   presupposes states. I verified independently: `||out_0||^2 = ||out_1||^2 = 1`
   and both `rho_B^(b)` have unit trace and non-negative spectrum at every
   site. The gap is in the certificate, not in the result.
3. **The `z3` parity rule is executed as an enumeration, not as the algebraic
   proof the report asserts.** `z3_parity_rule()` iterates over populated
   sites of `chi` and of the two outputs. That is complete *for this
   protocol*, but the report's stated reason ("because the diagonal symbol
   entries carry `z3` exponent `+-1` while the off-diagonal entries carry
   exponent `0`") is a general algebraic claim that no check in the run
   verifies. Section 3 above supplies the missing proof; it is correct.
   Additionally, the parity rule is never checked on the two *arms*
   separately, which is the step the collinearity conclusion actually needs
   (the code substitutes a direct check that `a[1] = r[1] = 0`, which suffices
   for the result but not for the stated mechanism).
4. **Order-coupled iteration.** The completeness check zips
   `states.items()` with `results.values()`, relying on both dicts having been
   populated in `sorted(admissible)` order. Correct as written, but the
   pairing is positional rather than keyed by `y`; a future edit that
   populates either dict differently would silently compare mismatched sites.
5. **`E_up` is described loosely.** `diag(0,1,0,0)` is the projector onto
   "exactly one particle, spin up", not the spin-up number operator
   `n_up = diag(0,1,0,1)`. They agree in expectation here only because the
   two-particle block is exactly zero. Harmless, but "Bob's spin-up
   occupation" is not literally what the exhibited operator is.
6. **"Candado 3" (§4) is undefined** in the contract, in the report and
   anywhere in the tracked repository. A frozen report should not carry an
   untraceable reference to an external deliberation artefact.
7. Not a defect, but worth recording as the by-product contract §4 invites:
   `a(y)` depends only on `sgn(y_2)` and all four sites yield an identical
   `M(y)`. The execution correctly did **not** assume any symmetry and
   evaluated all four sites; the coincidence is observed, and **no protocol
   symmetry is certified** by it. The report does not claim one.

## 9. Mandatory repairs

All three are corrections to claims in
`reports/2026-09-16--noncorner-signaling-gate.md`. None alters the verdict,
the domain, `M(y)`, the probabilities, `delta`, or any admissibility fact.

**MR1 — §2: "in two independent ways" is false.** The report states that
`supp K_1` was certified "through the frozen helper `exact_blocks()`, and
through a separate entry-by-entry Laurent extraction from `walk2()`", calling
these two independent ways. They are not independent: the new code executes
`sp.Poly(sp.expand(laurent(symbol[i, j]) * sp.prod(Z)), *Z)` and
`tuple(power - 1 ...)`, which is the *same* expression, the *same*
`laurent()` normalization and the *same* monomial-shift bookkeeping as the
body of `exact_blocks()`. It is one extraction aggregated two ways; a fault
in `laurent()` would defeat both identically. Replace with an accurate
description ("the same exact extraction, re-aggregated per entry to check the
contract's attribution table"), or cite this review's from-scratch
re-transcription, which never calls `laurent()` and does agree, as the
independent certification.

**MR2 — §4: "The sign difference has the same origin" is not established.**
The `z3` parity rule determines which internal channel can reach a site; it
says nothing about the relative phase of `a(y)` and `r(y)` within that
channel. The sign reversal is the exact computed fact `a_1/r_1 = -6` at the
four sites against `a_1/r_1 = +6` at the vertex, and no derivation of it from
the parity rule is given or exists in the report. Under
`PROJECT_INSTRUCTIONS` §4 this is an observed relation, not a mechanism.
Restate it as computed, or supply a proof.

**MR3 — §4: the inference "so `a` and `r` are collinear, `M(y)` is rank one
and diagonal, and `Tr M(y) != 0`" does not follow as written.** Collinearity
yields `M` diagonal of rank **at most** one. Rank exactly one and
`Tr M != 0` require `Re(a_1 conj(r_1)) != 0`; a collinear pair with purely
imaginary ratio gives `M = 0` identically — which is exactly the blind case
the contract's step-4 note raised. The conclusion is true here
(`Re(a_1 conj(r_1)) = -3/512`), but by computation, not by the parity rule.
Separate the two steps.

## 10. Verdict

**PASS**, with the three mandatory textual repairs above.

The preregistered chain
`exact supp K_1 => admissible domain => the four sites => M(y) at each` was
independently re-derived end to end, without using `exact_blocks()`,
`laurent()` or `verify_noncorner_gate()` as authority, in exact arithmetic
with no floating point, no sampling and no tolerance. Every quantity in the
executed report is reproduced exactly:

```
supp K_1 = 14 displacements, attribution as declared, symmetric under y -> -y
admissible = {(+-1,+-1,0)}, DERIVED from the certified support
M(y) = diag(-3/256, 0) != 0,  Tr M = -3/256,  Delta p_B = 3/128
p_0 = 25/1024,  p_1 = 49/1024,  p_1 - p_0 = +3/128  (the vertex values exchanged)
delta = 3/128 for both diag(0,1,1,1) and diag(0,1,0,0);  D = 3/128 exactly
```

The verdict `NONCORNER_SIGNALING_CONSTRUCTED` is correct and is satisfied at
all four admissible sites. The binding stop rule was genuinely honoured. The
implementation isolation is exact — one added function, one added `elif`, an
AST identical to `HEAD` otherwise — and every frozen file is byte-identical
to `HEAD`. The claim ceiling is adequate and contains no overclaim; in
particular the report correctly refuses to convert the result into any
statement about the `l_inf`/`l_2` mismatch, and correctly refuses to promote
`state/CURRENT_STATE.md`.

This is one independent agent review of a precisely delimited exact
construction at `Delta T = 1`. It establishes no optimality, minimality,
scaling, capacity, feasibility, protocol symmetry, or any claim about our
universe; it does not examine the other seven vertices, does not speak to
`Delta T = 2`, does not reopen the optimal-D gate, the axial gate or
`GATE_COMPLETITUD_AXIAL_N3`, and does not itself amend the canonical record
or the frozen witnesses, which retain their existing bytes and scope.
