# General infrared rate: second diagnostic, walk-adapted regions

2026-11-12. Claude (claude-opus-5-5). Charter
`theory/GENERAL_IR_RATE_ROUND2_DIAGNOSTIC.md`, script
`scripts/diagnose_general_ir_rate_round2.py` (both `7302105`, committed
before the run). Output `reports/2026-11-12--general-ir-rate-round2.json`
and `-stdout.txt`; single run, exit 0. **Floating-point diagnostic; no
label is a certificate or a verdict.** Not reviewed.

## 1. Table

`s_0`: extent along `n` of the zero set of the rate (at `t = 10^-3`);
`s_0/c_IR - 1 > 0` means ballistic modes faster than `c_IR` along `n`.
Every row now has Bob in the non-ballistic corona (`K_* > 0`) and a Newton
residual `< 3e-10`. "Axis": distance of `xi_*/|xi_*|` from `n`.

| Id | Body | `Z^d` | `s_0/c_IR - 1` | `K_*` | axis | zero dominant | Outcome |
| --- | --- | --- | --- | --- | --- | --- | --- |
| W1 | cube (CJWW 5.15) | yes | `-3e-5` | 0.391 | 0 | yes | all hold |
| W4 | square Weyl | yes | `-2e-5` | 0.195 | 0 | yes | all hold |
| W5 | hexagon (JDW L6d) | no | `1e-7` | 0.255 | 0 | yes | all hold (lattice outside class) |
| Z3 | regular hexagon | no | `1e-7` | 0.255 | 0 | yes | all hold (lattice outside class) |
| Z1 | octagon | yes | `-9e-6` | 0.182 | 0.034 | yes | H3 fails |
| Z2 | octagon (long axes) | yes | `-2e-5` | 0.182 | 0.034 | yes | H3 fails |
| Z5 | octagon, other order | yes | `-9e-6` | 0.242 | 0.069 | yes | H3 fails |
| Z4 | dodecagon | no | `-9e-6` | 0.366 | 0.065 | yes | H3 fails |
| Z6 | rhombic dodecahedron | no | `1.3e-6` | 0.318 | 0 | **no** | H4′ fails |
| W2 | cube, BCC (CJWW 5.12) | no | `0.22` | 0.292 | 0 | no | H4′ fails |
| W3 | cube, BCC (Pavia A+) | no | `0.22` | 0.292 | 0 | no | H4′ fails |
| W6 | tetrahedron (s=4) | no | `1.41` | 0.097 | 0 | no | H4′ fails |
| Z7 | truncated octahedron | yes | `0.071` | 0.517 | 0.16 | no | H3, H4′ fail |
| Z8 | axes + diagonals | no | `0.14` | 0.454 | 0.20 | no | H3, H4′ fail |
| Z9 | great rhombicuboctahedron | no | `0.13` | 0.561 | 0.091 | no | H3, H4′ fail |
| Z10 | hexagonal prism | no | `0.016` | 0.063 | 0.29 | no | H3, H4′ fail |

H2 and H8 hold in all sixteen rows; H5, H6, H10 hold wherever zero is
dominant.

## 2. What the rows show (these sixteen walks only)

1. **Faster ballistic modes along `n` ⇒ zero momentum is not dominant**, in
   all seven rows that have them (W2, W3, W6, Z7–Z10). There the theorem
   does not apply.
2. **No faster modes ⇒ zero momentum dominant** in eight of nine rows. The
   exception is Z6: `s_0` equals `c_IR` to the method's resolution
   (`1.3e-6`, the same size as the finite-`t` curvature, which is
   `-1e-5` in the other rows), yet four non-zero momenta dominate. So the
   absence of fast modes is not sufficient in these rows.
3. **The first round's two faults were real.** With walk-adapted regions
   the hexagonal walks (W5, Z3) satisfy every hypothesis; their lattice is
   outside the declared class only because the proof is written for `Z^d`.
4. **H3 is the next limitation.** When the walk's rate has no symmetry axis
   (product walks Z1, Z2, Z4, Z5), the true dual direction is irrational
   and the layer decomposition of the proof is not available, although
   every other hypothesis holds.
5. **Geometry of the body is not what decides.** Cube walks fall on both
   sides (W1 versus W2, W3); the octagon gives the same outcome for two
   factor orders (Z1, Z5) but different `K_*`.

## 3. Reading for the next question (author's reasoning, not established)

When zero momentum is not dominant, the dominant tilted points are at
non-zero momenta reached by the fast modes. The IR-admissible operations
still have finitely smooth profiles, whose Fourier content at a fixed
non-zero momentum is polynomially, not exponentially, small (manuscript
Layers (d): `O(N^-4)` per layer). The CJWW rate `K_*` is then plausibly
still attained, with a smaller power, by the ultraviolet content of the
encoder and detector; even with `C^infinity` profiles of compact support
the loss would be sub-exponential. If so, a strict gap in the **rate**
between the two kinds of walks is unlikely. The difference would be in
**which momenta carry the leading signal**: zero momentum (infrared) when
H4′ holds, the fast modes' momenta (ultraviolet, through the profiles'
rims) when it fails. This is consistent with the tetrahedral case of
2026-11-10, where the polynomial signal is carried by the admissibility
leakage. It is a conjecture, not a result.

## 4. Limits

Floating point; a dominant point missed by the grid would change the
H4′ column. The fast-mode criterion uses a single small `t`. Rows outside
`Z^d` are outside the class as written. No statement about other walks.
