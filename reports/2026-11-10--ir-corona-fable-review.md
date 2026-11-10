# IR-corona manuscript: adversarial review (one round)

2026-11-10. Reviewer: **Claude Fable 5.2** (`claude-fable-5-2`), via Claude Code,
single session, no delegation, no external transmission, no commit.
Base `cb40b4f13305d383c01d6aae241d77d585eba14e`, branch
`research/tetrahedral-support-rigidity-2026-11-09`, working tree with the
uncommitted changes of the readiness audit.

Reviewed object: `papers/ir-corona/ir-corona.tex`, SHA256
`5274dda038ffe08c8d3d9bad8be58e7576070ee548d1dfd53299390629e5d579`
(matches the "after repairs" hash in `reports/2026-11-10--ir-corona-readiness.md`).

**Numbering.** Theorem numbers are those of the compiled manuscript, where
all environments share one counter: 4.1 upper bound, 4.3 regional rate, 4.4
leading asymptotics, 5.1 ellipse lemma, 5.2 spectral radius, 7.1 tilted
symbol, 7.2 free tail, 7.3 depth sums, 7.4 layers, 7.5 assembly. I derived
them from the source; I did not compile. `formal/README.md` still calls the
rate and the asymptotics "Theorem 4.2" and "Theorem 4.3" (stale numbering).

**Independence.** This is a same-session reading by one Claude model. Under
the repository rules it is not an independent review of any text drafted with
a Claude-family model, and it authorizes nothing. I did not establish who
drafted the manuscript. The readiness report was used for scope only; each of
its statements that I rely on was rechecked and is listed below.

## Verdicts

| Question | Verdict |
| --- | --- |
| **Correctness** of Theorems 3.3, 4.1, 4.3 (rate), 4.4 (leading asymptotics) as stated | **No fatal error found.** The chain to `N^{-13/2} e^{-K_* N}` with the stated coefficient was re-derived by hand and closes. Five steps are too terse to be checked from the text alone (C1–C5, all reparable). The remainder is non-effective (limitation, stated by the manuscript). |
| **Infrared interpretation** | The proofs do **not** presuppose infrared spectral predominance. The wording in several places invites that reading, and the manuscript omits a cancellation that the repository itself records (I1, reparable by disclosure). |
| **Certificates and Lean** | They cover less than two sentences of the manuscript say (L1, L2, reparable). Fresh runs today pass. |
| **Novelty** | **OPEN.** None of the originals I read yields the result as a direct corollary. The rate `K_*` is, however, an evaluation of a formula already printed in CJWW (N1, reparable attribution). Three cited sources were not available locally and were not read. Absence of a located antecedent is not a novelty finding. |

## 1. What was checked, and how

### 1.1 Re-derived by hand in this session

Line numbers refer to `papers/ir-corona/ir-corona.tex`.

- Signal expansion (929–940) from `U_M = I + c_N + i s_N M`; `C(σ3,·) = −C(I,·)`.
- Separation bounds (421–425); Theorem 4.1 arithmetic (779–795, 797–802).
- Admissibility: Lemma 6.1 (854–873) and all constants of Theorem 3.3
  (876–912), including `Z_N`, the floor `sqrt(11/(140π²))`, `m`, `K_e`, `K_d`,
  and the rank-two identity for `Δ_M − Π'Δ_MΠ'`.
- Rate: closed form for `cosh² t_*` (581), `t_* ≈ 0.73575`, `K_* ≈ 0.19052`,
  `q_t ≈ 0.68956`, `q_n ≈ 0.30338` (hand arithmetic, 4–5 digits); uniqueness of
  `v_*` (824–831); `ξ_*·(y−x) ≥ N ξ_*·v_*` (846–848).
- Tilted symbol at `ξ_*` and projector `P` (977–983), from `P = (S − e^{−Φ_*})/(2D_*)`.
- Exact representation (961–968): bookkeeping of `x_*`, `y_*`, `N v_*`, and
  the exact cancellation of the phase `e^{−iNη·v_*}` against `iv_*·η` in `log λ`.
- Depth coordinates and the common `θ_N` on both sides (1034–1043); parity
  `(−1)^{N+u·(y−x)} = (−1)^{j+j'}`; profile identity `F_N = 64 ε_⊥²/N²` (1047–1052).
- Free tail (1057–1085): normalisation `c_r`, sign of the `j_1` term,
  `H_W(û)↓ = (1+i, −1)/√3`.
- Depth sums (1101–1130): Laplace transform, `c_g`, Poisson form, the tails
  `1/720` and `1/48`, `Γ̄ ≈ 49.44`, `ε_+ ≈ 0.04917`, `ε_− ≈ 0.00289`.
- Layer prefactors `16π/√3` and `32/√3` (1171–1175); assembly constant
  `128/(3π²)` and the power `−5 − 1/2 − 1 = −13/2` (1195–1212); `𝒦 ≈ 1.7493`.
- `ℓ_0`, `ℓ_π` for the row `(I,I)`, `(I,P3)` (1364), and
  `C̄_{I,I} ≈ −0.0753`, oscillation bound `1.47·10⁻³` (638).
- Second route for the power (position space): kernel `N^{−3/2}`, two profile
  factors `N^{−7/2}`, two in-plane areas `N` with a Gaussian of the same width
  `√N`, depth sums `O(1)`: `−3/2 − 7 + 2 = −13/2`. Agrees.

### 1.2 Executed in this session (unchanged files)

| Command | Result |
| --- | --- |
| `python3 -B scripts/verify_scaled_ir_gate.py` | 53/53, exit 0 |
| `python3 -B scripts/verify_regional_directional_asymptotics_gate.py` | 18/18, exit 0 |
| `python3 -B scripts/verify_regional_laplace_coefficient_gate.py` | 58/58, exit 0 |
| `python3 -B scripts/verify_directional_saturation.py` | 27/27, exit 0 |
| `cd formal && lake build` | `Build completed successfully (8564 jobs)`, exit 0 |

Python 3.12.3, SymPy 1.14.0, mpmath 1.3.0, NumPy 1.26.4. The Lean build used
the existing `.lake` cache; I did not force a clean rebuild or run
`#print axioms`. `grep` finds no `sorry`/`axiom` in `formal/QcaFormal`.
`git diff --stat 551addabe28b HEAD` is empty for the four scripts and
`formal/QcaFormal*`. `--diagnostics` was not run.

### 1.3 Not verified

- Ellipse-lemma algebra (727–729): not re-derived; relied on the certificate
  line "ellipse product" and on Lean for the inclusion only.
- The sum-of-squares identity (355): spot-checked at two points only.
- `ℓ_0`, `ℓ_π` for the other nine rows of the appendix table; the values of
  `𝓘_0`, `𝓘_1`, `I_b`; all table entries except `(I,I)`.
- "By the same argument" for `⟨r, E a_c⟩ = O(N^{−17/2})` (954–955): power
  counting only.
- The one-step value `3/128` (119–121), the Bialynicki-Birula maximum
  `√(3/2)` (401–402), "Γ fills the ball numerically" (153).
- All finite-`N` diagnostics (1379–1393).
- The published CJWW (Ann. Henri Poincaré 2026) against the arXiv v1 I read.
- BGPP (arXiv:0903.2967), Baryshnikov–Pemantle III (arXiv:0810.4898) and the
  ACSV book or manuscript: not present in `biblioteca/` (checked with `ls`
  and `INDICE.md`). Lines 244–256 of the manuscript are **[UNVERIFIED]** here.
- The repository's C1/C2a/C2b results quoted in I1: read in
  `state/CURRENT_STATE.md`, not re-derived.

## 2. The `N^{-13/2} e^{-K_* N}` term

Structure, as checked: exact contour shift to `η − iξ_*`; the spectral radius
of the tilted symbol is maximal exactly on `Σ = {0,π}³`; near each point a
Gaussian with Hessian `Q`; the six points with non-trivial plane characters
are suppressed by in-plane Poisson summation; the two remaining points give
`Γ_+ ℓ_0 + Γ_− ℓ_π`; `Γ_−` is bounded by `ε_− < 6·10⁻⁵ Γ̄`, so the sign is
that of `ℓ_0`. I found no step that fails.

**Uniformity in `θ_N`.** `θ_N` enters only through the depths
`δ = (θ_N + j)/√3` and through `S_±(τ; θ)`. The Poisson form in Lemma 7.3
is manifestly continuous and 1-periodic (`S_−` is anti-periodic, `Γ_−` uses
its square). The endpoint `θ_N → 0` makes the first plane a disc of radius
`sqrt(Nθ_N/(2√3))`, which may hold `O(1)` sites; there the `m ≠ 0` Poisson
terms are not small relative to the `m = 0` term of that plane, but they are
small in absolute terms (C2 below), which is what the proof needs. I see no
loss of uniformity.

**Non-vanishing.** Given Lemma 7.3 and the closed forms, the margin
`|ℓ_0|(Γ̄ − ε_+) > ε_−|ℓ_π|` needs `|ℓ_0/ℓ_π| > 6·10⁻⁵`. For the worst row
`(I,I)` the ratio is `(c_*−1)/(c_*+1) ≈ 0.124`. The certificate reports all
sixteen. The inference `δ > 0` for `N > N_*` is valid and non-effective.

### Objections on correctness

**C1 — reparable.** `ir-corona.tex:824–831`. The step
`ξ_*·v − Φ(ξ_*) = I(v_*) + ξ_*·(v − v_*)` uses `I(v_*) = ξ_*·v_* − Φ_*`, that
is, that the supremum in (565) is attained at the critical point. This needs
convexity of `Φ`, which is not stated. It holds: with the Hessian of line 1017,
Cauchy–Schwarz gives
`(Σ tanh ξ_j x_j)² ≤ (Σ sech² ξ_j x_j²)(Σ sinh² ξ_j)` and
`Σ sinh² ξ_j ≤ Π(1 + sinh² ξ_j) − 1 = D²`. One sentence repairs it. Without
it, the closed form in Theorem 4.3(b) is only a lower bound for `I(v_*)`.
Theorem 4.4 is unaffected, since its proof uses `ξ_*·v_* − Φ_*` directly (965).

**C2 — reparable.** `ir-corona.tex:1159–1164`. The in-plane Poisson remainder
is stated as `‖∂³G_0‖_𝓜 |2πm − η_t|^{−3}` with no estimate of the norm and no
statement of its uniformity in the depth. My estimate: the second derivative
of `(δ − |u|²/2R)_+²` jumps by `4δ/R` across a rim of length `2π sqrt(2Rδ)`,
and the interior third derivative is `O(|u|/R²)` on area `O(Rδ)`; both give
`O(δ^{3/2} R^{−1/2})`, hence `‖∂³G_0‖_𝓜 = O(N^{−4} δ^{3/2})`, uniform as
`δ → 0`. After the weighted depth sum this is the claimed relative
`N^{−3/2}`. Also unstated: `r_0` must be smaller than half the shortest dual
vector of `Λ_0`, so that `|2πm − η_t|` is bounded below; and the planes are
translates of `Λ_0`, which only adds phases to the `m ≠ 0` terms. The same
estimate is what gives `O(N^{−4})` in part (d) (1176–1179).

**C3 — reparable.** `ir-corona.tex:1173–1175`. On Bob's side
`w = h_N M_B r` contains the exact `r`, not `N^{−3/2}R_0`. The `m ≠ 0`
Poisson terms need derivative bounds on the exact `r̃`; "the smoothness of
`R_0`" and the uniform `O(N^{−5/2})` error of Lemma 7.2 do not give them. They
do hold, because `r̃` is band-limited to `|p| ≤ N^{−1}`, so each lattice
derivative costs a factor `N^{−1}`. This should be said.

**C4 — reparable.** `ir-corona.tex:1195–1206`. Two silent steps. (i) The
branch `λ^{−N}(I − P(η))` of the spectral decomposition (990) is dropped
without comment; it is `O(e^{−2NΦ_*})` relative. (ii) The six-point estimate
uses "the Gaussian decay of `S̃_N`" near those points, but Lemma 7.1(d) is
stated at `η_0 = 0` and transported only to `πu` (1025–1026). The other six
follow from the same identities (984–985); say so.

**C5 — reparable.** `ir-corona.tex:954–955`. `⟨r, E a_c⟩ = O(N^{−17/2})`
"by the same argument" is not written. With a profile vanishing to fourth
order the depth transform changes (`s^{−6}` in place of `s^{−4}`); the power
is plausible, the argument is absent.

**C6 — reparable (wording).** `ir-corona.tex:497–499`, abstract `64–66`.
"Acting on anything in the infrared band, an admissible operation leaves only
a vanishing fraction of its output outside" is stronger than Definition 3.1.
`η_op` is a ratio of two operator norms, not a supremum of ratios: for a
band-limited `ψ` with `‖Xψ‖ ≪ N^{−1/2}‖ψ‖`, Lemma 6.1 gives no control of the
fraction. What is proved for the protocol is the ratio for the actual
resource, via `‖a_M φ_N‖ ≥ sqrt((2−√2)m)` (897).

**C7 — limitation.** `ir-corona.tex:1386–1393`, `683–686`, `207–209`.
(a) The diagnostics contain no `N` at which the exact signal is compared with
the leading formula. "Brute" is compared with a Gaussian-kernel reference at
`N ≤ 56`; the semi-analytic evaluation is compared with the leading term at
`N ≥ 10³`. The two links are never tested in a common range, and at `N = 56`
the quoted correction `−100/N` exceeds the leading term. (b) The quoted
ratios of the "`N^{−17/2}` piece" to the "`N^{−13/2}` piece", `15.2`, `9.4`,
`6.4` at `N = 24, 40, 56`, give `ratio × N = 365, 376, 358`: over that range
they scale like `N^{−1}`, not `N^{−2}`. This does not contradict the theorem
(the range is pre-asymptotic: `R = N/4 ≤ 14`), but the diagnostics do not
corroborate the relative order of the two pieces, and the labels should not
suggest that they do. Diagnostics are not used in any proof.

**C8 — limitation.** The `O(N^{−1/2})` remainder and `N_*` are not explicit
(625–629). Stated by the manuscript; I agree with the statement.

## 3. Infrared interpretation

**Check.** No step of Section 7 uses `Π` or `Π'`. The signal is defined
without projection, and lines 469–470 say so. The theorem is therefore a
statement about strictly local operations that satisfy a norm-level
admissibility bound. It does not presuppose, and does not prove, that the
response is carried by infrared modes.

**I1 — reparable (disclosure).** `ir-corona.tex:42` (title), `123–127`,
`133–136`, `269–273`, `1277–1278`, `1302–1304`. The admissibility tolerance is
polynomial (`N^{−1/2}` relative in norm) and the signal is `e^{−K_* N}`. A
component of the encoded state outside `Π'` of polynomial size is therefore
free to carry, or cancel, the whole response; the definition cannot decide
which. The repository records exactly that: `state/CURRENT_STATE.md` Sec. 10.1
states, for `σ_2/I`, that the block with hard projection `Π'` satisfies
`L_pp = Θ(N^{−3})` and is cancelled by the blocks involving `I − Π'`
(C2a/C2b, internal agent reviews; not re-derived here). If that holds, the
infrared block alone overshoots the true signal by a factor growing like
`e^{K_* N}`, and the exponentially small response is the residue of a
cancellation in which the non-infrared component is essential. The
manuscript's only mention of cancellation is a hypothetical (133–136). A
reader of "infrared operational response" and "infrared-controlled" will
assume the opposite. Repair: state the cancellation, with its status and
scope, next to Definition 3.1 or in Section 8.1, and say that "infrared"
qualifies the operations, not the spectral origin of the signal.

**I2 — limitation.** `ir-corona.tex:1025–1029`, `1096–1099`, `1263–1268`.
Visible from the manuscript alone: the leading coefficient is built from
`O(1)` lattice planes at the two rims, weighted `e^{−t_*(θ_N+j)}`; it depends
on `θ_N`, the commensurability of the lattice with the spheres; and one of
the two contributing torus points is `πu`, outside the band `Π'` (it is a
Weyl node, line 346, but not the one the admissibility bands are centred on).
Its weight is at most `6·10⁻⁵` of the other, but it is part of the leading
term. The mechanism is a lattice-scale boundary-layer effect of smooth, wide
profiles. Lines 211–219 describe it accurately; the summary sentences do not.

**I3 — limitation.** `ir-corona.tex:663–669`, `1251–1261`. The power `13/2`
contains `2 + 2` from the quadratic vanishing of `F_N` and `h_N`. "The exact
power 13/2" is a property of this profile family. Profiles with another
vanishing order would change it, and flat (`C^∞`) cut-offs are not covered by
the argument at all. The Methodology remark (689–696) lists what was frozen
but not this dependence.

## 4. Scope of the certificates and of Lean

**L1 — reparable.** `ir-corona.tex:548–549`. "Theorem 4.1 is machine-checked
… for every `N ≥ 2`" is contradicted by the last sentence of the same remark
(557–559) and by `formal/README.md` ("What is not formalized"). Lean proves
`TN_bound` (`formal/QcaFormal/Theorem41.lean:226`, constant 4) and the
abstract inequality `delta_le_four_T` (`:258`) under the hypothesis
`‖v_1 − v_0‖ ≤ 2T`. It does not prove `v_1 − v_0 = P_B S^N P_A (U − I)ψ`,
nor `D_B ≤ 4T_N`, which is part of the displayed statement (543). The
appendix was repaired by the readiness audit; this remark and the repository
`README.md` line "with its Theorem 4.1 formalized in Lean 4" were not.

**L2 — reparable.** `ir-corona.tex:1325–1327`. "Lemma 5.1 [is] formally
verified" holds for the inclusion only. `formal/QcaFormal/Ellipse.lean`
contains `gauge_nonneg`, `gauge_mul_le`, `gauge_anti`,
`norm_le_four_of_gauge`; there is no boundary characterisation. The second
half of the lemma (709–710) feeds the equality case of Lemma 5.2 (742–743)
and, through it, Lemma 7.1(e) (1020–1022), on which Theorem 4.4 depends. That
part rests on the written proof and on the SymPy "ellipse product" checks.
Lemma 5.2 itself is formalized only in its use at `17/8`.

**L3 — limitation.** `scripts/verify_regional_laplace_coefficient_gate.py`.
The 58 checks certify identities, closed forms and enclosures. Three of them
are bookkeeping of a derivation, not the derivation: the power count is a sum
of eight declared rationals (`:283–285`), the prefactor check multiplies the
declared factors (`:279–282`), and the positivity check for `𝓘_0, 𝓘_1` tests
`ρ_* < 3` and `1 < π/2` (`:225–228`). `Γ_±(θ)` is never evaluated; the sign
margin uses the analytic bounds of Lemma 7.3. This agrees with
`scripts/README.md:208–225` and with line 1332 of the manuscript. The abstract
(77–79) reads as if interval arithmetic alone established non-vanishing; it
establishes it given the closed form and the analytic bounds.

**L4 — reparable.** `ir-corona.tex:1477–1487`. The repository reference pins
commit `551addabe28b` on another branch. The certificate and Lean bytes are
unchanged since then (checked), the manuscript is not. The author TODO stands.

**Readiness report, contrasted.** Its statements on Lean coverage, on the
certificate not encoding the remainder lemmas, and on the unchanged bytes are
confirmed. Its statement that "the later spectral decomposition records
leading cancellations" is true of `CURRENT_STATE.md`, not of the manuscript
(I1). It did not notice L1 or L2.

## 5. Prior art: can the result be read off the cited originals?

Read in the original, in this session:

| Source | Passage | What it gives |
| --- | --- | --- |
| CJWW, arXiv:2408.02108v1, `sources/2408.02108v1.pdf` (same SHA256 as `biblioteca/EXPONENTIAL_TAIL_ESTIMATES_FOR_QUANTUM_LATTICE_DYNAMICS.pdf`) | p. 3 | Upper rate only: "one also shows lower bounds, but since these would be state dependent, we do not consider them here." |
| same | p. 10, Lemma 4.1 | `I = ∞` outside `conv F`. Citation at line 811 is correct. |
| same | p. 13, Sec. 5.1 | "only two studies [8, 23] … outside of the propagation region", both giving prefactors, both on the line. Matches lines 255–257. |
| same | pp. 17–18, (5.15)–(5.21) | The walk, `|∇ω| ≤ 1`, and `R̃(ℓ) = 2 arcosh(cosh³(ℓ/2√3))` with the maximum "always attained for `λ = ℓ/√3 (1,1,1)` and `p = 0`, and equivalent points", found numerically. |
| Sunada–Tate, `biblioteca/arXiv-1108.1878.pdf` | p. 4, Thm 1.4, Cor. 1.5 | One dimension; pointwise transition probability in the hidden region with prefactor and rate `H_Q`. |
| Carteret–Richmond–Temme, `biblioteca/arXiv-quant-ph_0506048.pdf` | p. 1 abstract; p. 16, Thm 4 | One dimension, Hadamard walk; amplitudes for `1/√2 + ε < |α| < 1 − ε`. |
| Baryshnikov–Brady–Bressler–Pemantle, `biblioteca/arXiv-0810.5495.pdf` | p. 19, Thm 3.3; pp. 24–25, Thm 4.2 | Two dimensions; asymptotics uniform on compact subsets of the interior of the feasible set. Outside it, Thm 4.2 states `|a_r| ≤ C|r|^{−N}` for every `N`, with no prefactor. |

**N1 — reparable (attribution).** `ir-corona.tex:229–231`, `562–566`,
`575–584`. With `λ = 2ξ`, CJWW's `R = 2Φ` and their rate is twice the
amplitude rate, so `Φ(t,t,t) = arcosh(cosh³ t)` is their (5.21), and
`K_* = ½ Ĩ(√3 − ½)` with `Ĩ` the Legendre transform (5.19) of (5.21). On the
diagonal the radial bound is the directional one. As a check I evaluated
`Ĩ(1.1)` from the manuscript's formulas and got `0.105` by hand, against the
printed `.104` (p. 18); the difference is within my arithmetic and their
rounding. The manuscript credits CJWW for "the contour-shift idea" only. What
it adds to the rate is a proof (ellipse lemma) of what CJWW found
numerically, for every `ξ` and not only radially, and the regional minimiser.
The sentence should say that the diagonal tilt function and hence the value
of `K_*` are in CJWW.

**N2 — direct corollary?** Not from the passages read. The one-dimensional
theorems are pointwise and one-dimensional; BBBP gives no prefactor outside
the feasible set; CJWW give upper rates and exclude lower bounds by design.
None treats a region-summed, profile-weighted response, the selection of two
of eight torus points by plane characters, or a certified non-vanishing
coefficient.

**N3 — what the additional step is.** The pointwise kernel asymptotic at a
complex saddle of an entire periodic symbol with non-degenerate Hessian is
the standard method (the manuscript says as much at 257–260). The
model-specific content is: the identification of the maximisers of the
tilted spectral radius; the two-point selection; the discrete depth sums with
the flat tangential direction; and the sign margin. That is an application of
known technique to a new operational quantity. Whether it is significant is a
judgment for a specialist; I do not make it.

**N4 — limitation of this check.** I did no new literature search. BGPP,
Baryshnikov–Pemantle III and ACSV were not read (Sec. 1.3); the ACSV theory
of non-minimal critical points is the place where a transfer theorem for the
kernel, if one exists, would be. The claim at 269–276 ("to our knowledge …
the first") is supported only as "not located in the sources read by the
author's audit and by this review". `NOVELTY = OPEN`.

## 6. Obligations before a human evaluation

1. Repair C1–C5 in the text (each is one to three sentences) and have the
   repaired Section 7 read by a reviewer of another model family or a person.
2. Decide the wording of I1: disclose the `Θ(N^{−3})` cancellation with its
   status, or confirm with the author that it is to be left out and why. Fix
   the paraphrase C6.
3. Correct L1 and L2 so that the manuscript claims exactly the Lean coverage
   of `formal/README.md`; align the repository `README.md` line.
4. Credit CJWW (5.21) for the diagonal tilt function (N1); compare the
   citations with the published version of CJWW, not only v1.
5. Obtain and read BGPP Thms 2.2–2.3, Baryshnikov–Pemantle III Thm 3.7 and
   ACSV Thms 12.12 and 12.14 in the original, with file and page, or mark
   lines 244–256 as unverified by the author.
6. Either add a diagnostic that compares the exact signal with the leading
   formula in a common range of `N`, as a permanent script, or state plainly
   that no such comparison exists; reword the `N^{−17/2}` remarks (C7).
7. Fix the delivery snapshot: commit of the manuscript, archived release for
   the certificates (L4), and a clean Lean rebuild with `#print axioms`.
8. Items of Sec. 1.3 that the author wants stated as fact need their own
   check.

## 7. Files actually read

In full: `papers/ir-corona/ir-corona.tex`; `reports/2026-11-10--ir-corona-readiness.md`;
`CLAUDE.md`; `PROJECT_INSTRUCTIONS.md`; `state/ROADMAP_2026-11-10.md`;
`formal/README.md`; the uncommitted diffs of `README.md`,
`papers/ir-corona/ir-corona.tex`, `state/CURRENT_STATE.md`,
`state/ROADMAP_2026-11-09.md`.

In part: `state/CURRENT_STATE.md` (header diff, section list, Sec. 10 and
10.1); `~/herramientas/REGLAS.md` (first 80 lines); `scripts/README.md`
(lines 136–235); `scripts/verify_regional_laplace_coefficient_gate.py`
(lines 212–285 and its output); `formal/QcaFormal/Theorem41.lean`
(statements of `TN_bound`, `delta_le_four_T`, region definitions);
`formal/QcaFormal/Ellipse.lean` and `Symbol.lean` (declaration lists);
`biblioteca/INDICE.md` (search hits); the PDF passages of Sec. 5; the header
of `reports/2026-09-17--regional-laplace-coefficient-gate-independent-review.md`.

Not read: `papers/ir-corona/ir-corona.md`; the gate reports of 2026-09-17 and
their reviews; `reports/2026-11-02--ir-corona-prior-art-check.md` (two `grep`
hits only); the other certificate sources.

Text extraction of the PDFs used `pdftotext` into the session scratchpad; no
script was created and nothing else was written to the repository. Tool
commit for the shared rules: `~/herramientas` at `97292a9`.
