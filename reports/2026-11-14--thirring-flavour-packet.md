# Thirring flavour-packet gate: results

2026-11-14. Author: Claude Code (Claude Opus 5.5). **PRELIMINARY: written
proof plus exact author checks; one sealed cross-family review PASS; no
promotion.**

**Review (2026-11-14).** Grok `grok-4.7`, sealed revision-ciega, one round,
herramientas `2a7342b`, on `24b78e9`:
[unaltered review](reviews/2026-11-14-thirring-flavour-packet-grok/informe_grok.md).
PASS on all six blocks, no mandatory repair. Clarifications: (i) F7's
check name `left-inside-4mu(2-m>0)` repeats the expression of
`left-negative`; author reading: both bounds of the left support,
`-2+m < 0` and `-2-m > -4`, reduce to the same inequality `m < 2`, so the
outer bound is checked, only the label is uninformative (verifier bytes not
changed); (ii) the ceiling of the argument remains the contract-2 bridge
(written, repaired, not re-reviewed), as Sec. 1 states. The reviewer
re-derived the (+,-) contact condition, T_-, the degeneracy margin and
x = (sqrt10 - 2)/6. The body below is unchanged.

Contract [THIRRING_FLAVOUR_PACKET_GATE.md](../theory/THIRRING_FLAVOUR_PACKET_GATE.md),
frozen at `d0c59cb` before execution; authorization «AUTORIZO SU EJECUCION»
(2026-11-14). Verifier `scripts/verify_thirring_flavour_packet.py`, committed
before running at `b49bf18`; test point replaced at `8d7e444` after run 2.
Contract-2 verifier imported read-only (SHA256 `a1900674…`, unchanged).

Runs (all retained):
1. System `python3` without SymPy: import error, no checks, no files.
   Rerun in `~/.venvs/qca-causal-cones` with `scripts/requirements.txt`
   (sympy 1.14.0, numpy 1.26.4).
2. 31/32: the (+,-) eigenfunction check failed at the test point
   `z2 = -z1`, which gives `q_l = q_r` (k = -pi/2), where the four waves
   coincide pairwise. Check-construction error; the point is outside the
   packet supports. Replaced by `z2 = conj(z1)`
   ([note](2026-11-14--thirring-flavour-packet-failed-run-2-note.txt),
   [output](2026-11-14--thirring-flavour-packet-failed-run-2.txt)).
3. 32/32 exact ([output](2026-11-14--thirring-flavour-packet.txt)).

## 1. Verdict

`FLAVOUR_PACKET_EXCHANGE_GATE_IN_DECLARED_CODE` (author, PRELIMINARY). In the
flavour basis (AA, AB, BA, BB), as mu -> 0,

    V = 1 (+) [[ i y, x ], [ x, i y ]] (+) 1,
    x = (sqrt10 - 2)/6 ~ 0.1937,   y = sqrt(11/18 + sqrt10/9) ~ 0.9811,

with leakage `||E_mu|| -> 0`. S1 and S2 hold; S3: `|<BA|V|AB>| = x > 0`;
S4: `V|AB> = i y |AB> + x |BA>` has concurrence `2xy ~ 0.380`.

The proof depends on the packet/scattering bridge of contract 2
(written, repaired after an Astra review, **not re-reviewed**), reused for
the (+,+) sector and adapted here for the (+,-) sector (Sec. 4). The
verdict is no stronger than that bridge.

## 2. Code structure (exact; F3)

Let `phi_r`, `phi_l` be the positive-band packets of the contract and
`Gamma = sigma_z (-1)^x`. `Gamma` maps a positive-band component at q to a
negative-band component at q + pi (contract 2, P2), so `phi` and
`Gamma phi` have disjoint momentum supports (F7). Hence
`||Pi_f phi||^2 = 1/2` and the four columns
`(sqrt2 Pi_{f_r} phi_r) wedge (sqrt2 Pi_{f_l} phi_l)` are orthonormal.

With `G = Gamma_1 Gamma_2` and `P = (1 - G)/2`:

- AA and BB have `G = +1`. Since `U(1 - P) = F(1 - P)` exactly (contract 2,
  Sec. 3), `U^T |AA> = F^T |AA> = B_out |AA>` for every mu and T, and
  likewise for BB. No error at all.
- `AB = P(phi_r ^ phi_l) - P(phi_r ^ Gamma phi_l)` and
  `BA = P(phi_r ^ phi_l) + P(phi_r ^ Gamma phi_l)`. The first vector lies
  in band sector (+,+) at total momentum near `q_r + q_l`; the second in
  sector (+,-) (right particle band +, left band - near `q_l + pi`) at
  total momentum shifted by pi. They are orthogonal, each of norm^2 1/2.

This is why the doubler leakage of contract 2 disappears: the band code
loses amplitude into `G` times the code; the flavour code contains it.

## 3. Low-energy admission under U^2 (written)

`Gamma W = -W Gamma` (contract 2, P2) gives
`W (Pi_A phi) = Pi_B (W phi)`: one step swaps the flavour and moves the
packet; two steps restore it, `W^2 Pi_f phi = Pi_f W^2 phi`. Gamma acts on
site, so the position-space trajectory of `Gamma phi` equals that of `phi`;
in momentum space the negative-band component at q + pi carries phase
`e^{+i omega(q+pi)} = -e^{-i omega(q)}`, so under `W^2` both components
carry `e^{-2i omega(q)}` with the same group velocity. On the support
`omega(mu K)/mu -> sqrt(1 + K^2)` (contract 2, P5). This is the admission
decided by the user for Q2-A; it is not an interacting QFT limit.

## 4. Scattering of the two P-sectors (written; F1, F2, F6)

**(+,+) sector.** `P(phi_r ^ phi_l)` is the P-part of the contract-2
column with the A mode at k = 1 and the B mode at k = 2 (the same packets).
Contract 2 Sec. 4 proves
`U^T P(phi_r ^ phi_l) = T_+ F^T P(phi_r ^ phi_l) + o(1)`, with
`T_+ -> (a_r + z a_l)/(a_l + z a_r)`, `z = e^{-i chi}`,
`a(K) = sqrt(1 + K^2) + K` (contract 2, P6), `a_r = sqrt2 + 1`,
`a_l = sqrt5 - 2`. Consistency check: `|T_+ - 1|^2/4` equals contract 2's
limit `l01` exactly (F6).

**(+,-) sector.** The same proof applies with these substitutions:

1. *Exact eigenfunctions.* The contract-2 contact argument (Sec. 4(i)) uses
   only the four waves sharing one free eigenvalue and the contact
   antisymmetry at y = 0; with `(a,b,c,d) = v+_{q1} (x) v-_{q2'}` it gives
   `T_- = (g_+(q1) + z g_-(q2'))/(g_-(q2') + z g_+(q1))`, the source's
   Eq. (12) lower sign. Shifting both momenta by pi and flipping both
   bands keeps the eigenvalue `e^{-i omega(q1)} e^{+i omega(q2')}`. F2
   certifies the eigenfunction exactly at two non-degenerate algebraic
   points. With `g_-(q + pi) = -g_+(q)` (F1) and `q2' = q_l + pi`:
   `T_- = (a_r - z a_l)/(z a_r - a_l)`.
2. *Initial error.* `P` of a (+,-) plane-wave pair is
   `(1/2)[v^{+-} - (-1)^{x1+x2} v^{-+}_{shifted}]`, the incoming part of
   the eigenfunction, exactly as in Sec. 4(iii) of contract 2.
3. *Tails and geometry.* The free motion of `Gamma phi_l` is that of
   `phi_l` up to the on-site unitary Gamma and a sign per step, so every
   position-space tail, separation and velocity bound of contract 2
   transfers unchanged.
4. *Smoothness.* At chi = pi/2, `|T_-| = 1` and the scaled denominator
   `|z a_r - a_l|^2 = a_r^2 + a_l^2 > 0`; `T_-` depends on `q/mu`, so its
   variation over a packet of width `mu^{3/2}` is `O(mu^{1/2})`, as for `T_+`.
5. *Degeneracy.* The (+,-) sector degenerates at `q_l = q_r`; the supports
   stay `3mu` apart with width `mu^{3/2}`, the same separation that
   controls the approach to `k = 0` in the (+,+) sector of contract 2.

Hence `U^T P(phi_r ^ Gamma phi_l) = T_- F^T P(phi_r ^ Gamma phi_l) + o(1)`.

## 5. Logical map (F4, F5, F6)

Combining Secs. 2 and 4, with `F^T` mapping each column to `B_out`:
`U^T |AB> -> al B_out|AB> + be B_out|BA>`, `U^T |BA> -> be B_out|AB> +
al B_out|BA>`, `al = (T_+ + T_-)/2`, `be = (T_+ - T_-)/2`. The block is
unitary because the two sectors are orthogonal and `|T_+-| = 1`. Leakage
vanishes because every image lies in the span of `B_out` up to `o(1)`.

`T_+ - T_- = 2 a1 a2 (z^2 - 1)/((a2 + z a1)(z a1 - a2))`, so the exchange
amplitude vanishes iff `chi in {0, pi}` (F5). At chi = pi/2:
`T_+ = x + i y`, `T_- = -x + i y`, so `al = i y`, `be = x`, and
`|be| = 2 a_r a_l/(a_r^2 + a_l^2) = (sqrt10 - 2)/6` (F6).

## 6. What the verifier does and does not certify

Certified exactly (32/32): F1-F7 as listed in the verifier docstring,
including the (+,-) eigenfunction at two points, the code algebra in a
faithful finite model, the form of V given the bridge limits, the
vanishing condition for `be` and the limiting values. Not certified: the
bridge (contract 2's written proof and its (+,-) adaptation above), the
U^2 admission argument, and the verdict.

## 7. Scope and balance

- Holds for this code, this rule, chi = pi/2, these two packets, mu -> 0.
  The angle depends on the momentum centres; no parameter was varied.
- The gate conserves the flavour number `N_A` (Hamming weight in the
  flavour basis). On raw qubits this family is not universal; each pair of
  packets crosses at most once in 1D, and nothing here composes gates.
- First result of the line with an entangling, non-diagonal, leakage-free
  logical gate on carriers in the low-energy regime under U^2. It is not
  universality, composability or an interacting relativistic QFT limit.
- `NOVELTY = OPEN`: exchange-type gates and conservation obstructions are
  prior art; the Thirring two-particle solution is from 1711.03920.
- Balance: this contract is closed; no further contract follows
  automatically. Coexistence stays OPEN. Independent review needs separate
  permission.
