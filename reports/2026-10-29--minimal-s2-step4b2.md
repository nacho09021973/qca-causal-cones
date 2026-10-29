# Minimal s=2 rigidity gate: Step 4b-2, sectors and speeds in the (V4, Pauli) class — 2026-10-29

## Provenance

- **Charter:** [`MINIMAL_S2_RIGIDITY_GATE.md`](../theory/MINIMAL_S2_RIGIDITY_GATE.md),
  preregistration commit `785565c`, Step 4b-2 and Sec. 5.
- **Starting point:** Step 4b-1 ([report](2026-10-29--minimal-s2-step4b1.md), repaired in
  `4646be5`, reviewed in two rounds and promoted in `014753e`). Only `(V4, tetrahedron, Pauli)`
  is nonempty.
- **Authorization:** "si a todo" (2026-10-29), recorded in `CURRENT_STATE` in `4646be5`. Budget
  3 hours of wall time, scope the `(V4, Pauli)` class only. Step 4a (Q-b) is not authorized.
- **Timing:** started 15:52 UTC. Certificate passed at 16:32 UTC (about 40 minutes of the budget).
- **Certificate:** `scripts/verify_minimal_s2_step4b2.py`, SHA-256 `8849e87a0041205f…`. 20/20 exact
  checks, about 240 s, Python 3.12.3, SymPy 1.14.0. It imports no certificate code.
- **Full sweep:** 50/50 verifiers pass ([record](2026-10-29--minimal-s2-step4b2-run_all.tsv)).
- **Evidence level:** see `CURRENT_STATE`. Reviewed by Grok
  ([review and author reading](../debates/2026-10-29--minimal-s2-step4b2-review-grok/verificacion_autor.md));
  repairs G-4B2-01..05 applied to this text, certificate bytes unchanged.

## Result

For the class `(V4, tetrahedron, Pauli)` (family P, `ρ` = inclusion, d=3, `N_3` without on-site
term, `s=2`, all eight `T_h != 0`, Eq. (2) not assumed):

| Question (charter Sec. 5) | Outcome |
| --- | --- |
| Description of the class | Every unitary symbol is `U = α W_σ(q)`, with `α` a unit complex number and `W_σ` one of 48 fixed symbols. The real set is 48 circles |
| Q-a | `DISTINGUISHABILITY_IMPLIED_IN_CLASS`. It holds for every unitary symbol of the class, not only those with a node |
| Sectors | `ADMISSIBLE_SECTORS_EXIST`. Every symbol has exactly four admissible nodes on the Brillouin torus (16 points in `[0, 2π)^3` of `q`) |
| Main | `RIGIDITY_PROVED_FOR_FROZEN_CLASS`: `c_0 = c_strict^iso = 1/sqrt(3)` at every admissible node of every symbol |
| Saturation | `SATURATION_PROVED_FOR_CLASS`: `c_strict^iso = rho_micro = 1/sqrt(3)` for every symbol |

**Consequence.** In the frozen class, unitarity, `V4` covariance and active support imply P17's
Eq. (2) on `S_+` (and the stronger statement on all of `N_3`), and every admissible node has speed
`1/sqrt(3)` (normalized units), equal to `c_strict^iso` and `rho_micro`. This does not say that the
class is P17's class: P17's normalization `Σ_h A_h = I` (a quotient the charter excludes from
transport) is not imposed, and the 48 families are not identified with P17's walks up to its
equivalences.

Combined with Step 4b-1 and stage (a), every class of the two frozen families is now decided:
all classes other than `(V4, Pauli)` are `EMPTY_CLASS`, hence `VACUOUS` for the main question.
This combination is stated here for the record; it is promoted only with both stages reviewed.

## Derivation

Units: `q_j = k_j / sqrt(3)` (the `ε` units of the charter), `c_j = cos q_j`, `s_j = sin q_j`.

**1. Parametrization.** `V4` acts simply transitively on each tetrahedron
`S_+ = {h : h_1 h_2 h_3 = 1}` and `S_− = −S_+`. With `ρ` = inclusion, covariance gives
`T_h = a I + Σ_j h_j b_j σ_j` on `S_+` and `T_h = c I − Σ_j h_j d_j σ_j` on `S_−`, with
`a, c ∈ C`, `b, d ∈ C^3`: 16 real parameters, as in 4b-1. Summing over each tetrahedron,

`U = α C_0 + β S_0 + Σ_j σ_j (γ_j C_j + δ_j S_j)`,

with `C_0 = c_1 c_2 c_3`, `S_0 = s_1 s_2 s_3`, `C_j = c_j s_k s_l`, `S_j = s_j c_k c_l`
(`(j, k, l)` cyclic), and the linear bijection `α = 4(a+c)`, `β = 4i(a−c)`, `γ = −4(b+d)`,
`δ = −4i(b−d)`. The certificate checks this as a Laurent identity.

**2. Unitarity.** Write `U = wI + v·σ`. Then `U^†U = (|w|^2 + v̄·v) I + (2 Re(w̄ v) − 2 Im(v̄_k v_l)) σ`.
- In the identity part, `C_0^2, S_0^2, C_j^2, S_j^2` are the eight multilinear Bernstein
  monomials in `c_j^2`, and `C_0 S_0 = C_j S_j` is odd. So
  `|α| = |β| = |γ_j| = |δ_j| = 1` and `Re(ᾱβ) + Σ_j Re(γ̄_j δ_j) = 0`.
- In the `σ_j` part, six independent functions give
  `Re(ᾱγ_j) = Im(δ̄_k δ_l)`, `Re(β̄δ_j) = Im(γ̄_k γ_l)`, `Re(ᾱδ_j) = 0`, `Re(β̄γ_j) = 0`,
  `Im(γ̄_k δ_l) = 0`, `Im(δ̄_k γ_l) = 0`.

These 27 real equations form the reduced system `R`. The certificate checks that the ideal of the
78 real Laurent unitarity identities (both orders) has the same reduced Groebner basis as `R`. The
hand reduction is therefore exact over C.

**3. Real solutions.** Over the reals:
- `|δ_j| = |α| = 1` and `Re(ᾱδ_j) = 0` give `δ_j = i η_j α`, `η_j = ±1`. Identity checked:
  `|δ_j − iα|^2 |δ_j + iα|^2 = (|δ_j|^2 − |α|^2)^2 + 4 Re(ᾱδ_j)^2`.
- In the same way, `γ_j = i ε_j β`, `ε_j = ±1`.
- Then `γ̄_k δ_l = ε_k η_l β̄ α`, so `Im(β̄α) = 0` and `β = κα`, `κ = ±1` (identity checked).
- The remaining equation is `κ(1 + Σ_j ε_j η_j) = 0`, so exactly one `ε_j η_j` equals `+1`.
  The other equations then hold identically.

This leaves `2 · 3 · 8 = 48` sign choices, each a circle in `α`. The certificate checks all 128
sign choices against the full unitarity system with `α` symbolic on the unit circle: exactly
these 48 pass. The 4b-1 witness `e^{-iq_x σ_x} e^{-iq_y σ_y} e^{-iq_z σ_z}` is the choice
`κ = −1`, `ε = (1, −1, 1)`, `η = (−1, −1, −1)` at `α = 1`. Active support holds throughout:
`a = α(1 − iκ)/8` and `c = α(1 + iκ)/8` are nonzero, so every `T_h` has nonzero trace.

**4. Q-a, two routes.**
- (i) On the 48 families, `T_{gh} != T_h` for every `g ∈ V4 \ {e}` and `h ∈ N_3`. Since `V4`
  moves every vertex, this implies P17's Eq. (2), `[R_g, T_h] != 0` whenever `g h != h` for
  `h ∈ S_+` (the domain of P17 and of the charter's family P). The check on all of `N_3` is
  stronger than the literal statement.
- (ii) Without the classification (the argument of the Astra review of 4b-1): for each `g ≠ e`
  and each orbit representative `h`, unitarity plus `T_{gh} = T_h` plus `y ||T_h||^2 = 1` has
  unit ideal. By hand (repaired after the Grok review, G-4B2-01):
  - `T_h` has rank one (the shift `2h` has the single pair `(−h, h)`, A8). `T_{gh} = T_h` means
    `T_h` commutes with `R_g`, so `T_h = λ P` with `P` a `σ_g` eigenprojector.
  - The shift `2h` gives `T_{−h}^† T_h = 0` and `T_h T_{−h}^† = 0`, so `T_{−h} = μ(I − P)`.
  - Then `T_{−h}` also commutes with `R_g`, and covariance gives `T_{−gh} = R_g T_{−h} R_g^† = T_{−h}`.
  - The shift `gh − h` has exactly the pairs `(h, gh)` and `(−gh, −h)`:
    `T_h^† T_{gh} + T_{−gh}^† T_{−h} = |λ|^2 P + |μ|^2 (I − P) = 0`, so `λ = 0`, against
    `T_h != 0`.

**5. Nodes.** `U = α W` with `W = (C_0 + κ S_0) I + i Σ_j σ_j (ε_j κ C_j + η_j S_j)`, so `U` is
scalar iff `ε_j κ c_j s_k s_l + η_j s_j c_k c_l = 0` for `j = 1, 2, 3`.
- If all `c_j != 0`, divide by `c_1 c_2 c_3`: `t_j + μ_j t_k t_l = 0` with `t = tan q`,
  `μ_j = κ ε_j η_j`. If some `t_j = 0` then all are. Otherwise `t_j^2 = μ_k μ_l` for every `j`,
  which needs `μ_1 = μ_2 = μ_3`, but the `ε_j η_j` are not all equal.
- If some `c_j = 0`, the equations force all `c_j = 0`.

So the scalar points are `q ∈ {0, π}^3` and `q ∈ {π/2, 3π/2}^3`. The certificate solves the
system exactly for every family and finds these 16 points. Modulo
`Λ^* = π{m : Σ m_j even}` (in `q`), they are four nodes:
`0`, `(π, 0, 0)`, `(π/2)(1, 1, 1)` and `(π/2)(1, 1, −1)`.

At every point, `U = aI` with `|a| = 1`, and `H_j = i ā ∂U/∂k_j` is traceless with
`½ tr(H_j H_l) = δ_jl / 3`. For example, `H_j = −η_j σ_j / sqrt(3)` on `{0, π}^3` and
`H_j = ε_j σ_j / sqrt(3)` on `{π/2, 3π/2}^3`. The linearized band is `±|p|/sqrt(3)`, isotropic and
untilted, so each node is admissible with the full two-band sector and `c_0 = 1/sqrt(3)`.

**6. Strict body.** Every `T_h` has rank one, `T_h^2 = tr(T_h) T_h` and `tr T_h != 0`. The
coefficient of `U^n` at the vertex `n h` is `T_h^n = tr(T_h)^{n−1} T_h != 0`. By the vertex lemma
([`MASSLESS_INRADIUS_RIGIDITY_GATE.md`](../theory/MASSLESS_INRADIUS_RIGIDITY_GATE.md), erratum,
lines 24–29), the strict body equals `C_micro = conv(N_3)`. With the normalized vertices
`h = ε/sqrt(3)` (not the sign vectors `ε` used in Secs. 1–5), `h_infty(q̂) = |q̂|_1 / sqrt(3)`. Its
minimum over unit `q̂` is `1/sqrt(3)`, on the axes (`|q|_1 >= |q|_2`), and
`c_strict^iso = rho_micro = 1/sqrt(3) = c_0`.

## Scope and limits

- **One frozen class.** d=3, `N_3`, `s=2`, no on-site term, proper cube rotations, `V4` with the
  Pauli representation. Not a general QCA law (charter Sec. 5 ceilings).
- **Nothing about** `s > 2`, other supports, on-site terms, masses, interactions or species (A).
- **Q-b** (transport of the Pavia certificate along P17's equivalences) stays open; it is not
  needed here, because every symbol of the class is computed directly.
- **Relation to P17.** Every symbol satisfies P17's Definition 1 and Eq. (2) on `S_+`. The repo does not
  re-derive P17's classification and does not claim to; the computation above is independent of
  it. Whether the 48 families coincide with P17's list up to its equivalences is not checked.
- **Literature.** Charter Sec. 4: before Q-a is described beyond this class, the external search
  for P17 [31] and later work needs separate permission. Not done. **NOVELTY = OPEN.**
- **Not certified by the script:** the passage from `R` to the 48 families beyond the identities
  listed, and the vertex lemma itself (cited).
