# Thirring co-moving packet gate: results

2026-11-14. Author: Claude Code (Claude Opus 5.5). **PRELIMINARY: written
proof plus author checks; one sealed cross-family review (Astra) with
repairs applied, re-review PASS; no promotion.**

**Re-review (2026-11-14).** Astra `gpt-6-astra`, sealed, one bounded
round on `583868e`:
[unaltered re-review](reviews/2026-11-14-thirring-comoving-packet-astra-rereview/informe_astra.md).
PASS: R1 and R2 resolved, clarifications reproduced faithfully, no new
error, no mandatory repair. Physical simulability and the other questions
delimited below remain OPEN.

**Review (2026-11-14).** Astra `gpt-6-astra`, sealed revision-ciega, one
round, herramientas `2a7342b`, on `e81a719`:
[unaltered review](reviews/2026-11-14-thirring-comoving-packet-astra/informe_astra.md).
REPAIR_REQUIRED; blocks 1-3 (bridge geometry, eigenfunctions and
degeneracies, r_co and values) PASS; no flaw found that invalidates the
declared gate. Repairs applied (each checked by the author; user «si»):

- R1: the "iff" statements of A2 and A5 omitted r = 1 (where V = P,
  alpha = 0, beta = 1 and P V = I). Restated in Sec. 2.
- R2: two checks (`C-beta>0`, `C-concurrence(V|AB>)>0`) evaluate exact
  expressions numerically (`sp.N(..., 30) > 0`). The count is qualified
  as 50 exact + 2 numerical positivity checks; exact argument added in
  Sec. 6. Verifier bytes unchanged.

Clarifications recorded: the factor five bounds the time parameter, not
necessarily the final tail constant; Lemma 1 also assumes p != n pi/2, and
here p, k in mu[2 - m, 2 + m], mu[1 - m, 1 + m] keep distances proportional
to mu from every degeneracy (also in the mixed sector), with scaled
denominators >= sqrt2; r_co is fixed by the incoming geometry together
with the declared order; in position order the gate is P V up to a sign
common to all four basis states. The original text is in git at `e81a719`.

Contract [THIRRING_COMOVING_PACKET_GATE.md](../theory/THIRRING_COMOVING_PACKET_GATE.md),
frozen at `dca5ebc` before execution; drafting and freezing authorized with
«si redacta el contrato y luego congelas», execution with «autorizado»
(both 2026-11-14). Verifier `scripts/verify_thirring_comoving_packet.py`,
committed before running at `2685635`. It imports read-only the contract-2
verifier (SHA256 `a1900674…f4d517`) and the flavour-packet verifier
(SHA256 `7e66c30a…af6cd`), both unchanged.

Runs: one, in `~/.venvs/qca-causal-cones` (sympy 1.14.0), 52/52 passed (50 exact,
2 numerical positivity checks; see Sec. 6),
about 112 s ([output](2026-11-14--thirring-comoving-packet.txt),
[record](2026-11-14--thirring-comoving-packet.json)). No failed run.

## 1. Verdict

`COMOVING_PACKET_GATE_SAME_FAMILY` (author, PRELIMINARY). For the declared
fast (K = 3) and slow (K = 1) flavour packets, both moving toward negative
x, as mu -> 0, in the basis (AA, AB, BA, BB) with the fast packet first:

    V_co = V(r_co) = 1 (+) [[ alpha, beta ], [ beta, alpha ]] (+) 1,
    r_co  = a(3)/a(1) = (sqrt10 + 3)/(sqrt2 + 1) = 3 sqrt2 + 2 sqrt5 - sqrt10 - 3 ~ 2.5525,
    beta  = 2 r_co/(1 + r_co^2) = (3 + 2 sqrt5)/11 ~ 0.6793,
    alpha = i (r_co^2 - 1)/(r_co^2 + 1) = i sqrt(92 - 12 sqrt5)/11 ~ 0.7339 i,

with leakage ||E_mu|| -> 0 and no extra global phase. C1 and C2 hold; C3:
V_co is the family V(r) at r = r_co, with r_co (not 1/r_co) fixed by the
creation order (Sec. 4). Concurrence of V_co|AB> is 2|alpha beta| ~ 0.997.
(The closed form of alpha follows from |alpha|^2 = 1 - beta^2 and
Im alpha > 0; the verifier certifies the r-form.)

The verdict rests on the contract-2 packet/scattering bridge (re-reviewed
PASS 2026-11-14) and its flavour-gate (+,-) adaptation (Grok PASS),
adapted here in writing to the co-moving geometry (Sec. 3). The adaptation
is not reviewed. The verdict is no stronger than it.

## 2. Part A (exact, verifier A1-A5)

- A1: alpha(r) = z(r^2 - 1)/(z^2 r^2 - 1), beta(r) = r(z^2 - 1)/(z^2 r^2 - 1)
  with r = a1/a2 reproduce (T_+ +- T_-)/2. PASS.
- A2: 1 + alpha^2 - beta^2 = (z^2 + 1)(r^2 - 1)/(z^2 r^2 - 1) (rational
  identity, where z^2 r^2 != 1). Hence Delta = (1 + alpha^2 - beta^2)/(2 alpha)
  = (z^2 + 1)/(2z) = cos chi wherever the quotient is defined (alpha != 0,
  i.e. r != 1), independent of r. Pointwise, 1 + alpha^2 - beta^2 = 0 iff
  z^2 = -1 or r = 1; it vanishes for the whole family iff z^2 = -1. PASS
  (R1).
- A3: V_12(x) V_13(xy) V_23(y) = V_23(y) V_13(xy) V_12(x), all 64 entries,
  symbolic in x, y, z, and at z = -i. PASS.
- A4: with Rcheck = P V, Rcheck_12(x) Rcheck_23(xy) Rcheck_12(y) =
  Rcheck_23(y) Rcheck_12(xy) Rcheck_23(x), symbolic and at z = -i. PASS.
- A5 (diagnostic, decides nothing). Matchgate determinants (block {00,11}
  versus block {01,10}) at z = -i: V: 1 vs -1; fSWAP V: -1 vs 1; P V: 1 vs 1
  (equal). In general det A(P V) = 1 and det B(P V) =
  1 - (z^2 + 1)(r^2 - 1)/(z^2 r^2 - 1) (certified identities). So for r != 1
  P V meets the determinant condition iff z^2 = -1, i.e. chi = pi/2 mod pi;
  at r = 1, V = P and P V = I for every chi with defined denominators (R1).
  The declared code has r_co != 1 and chi = pi/2.

Part A is algebra on C^2 tensor C^2 tensor C^2. It does not show that three
physical packets scatter in factorized form, and it does not decide whether
the fermionic packets need a graded tensor structure. Both stay OPEN.

**Reading of A5 (author, [UNVERIFIED] against prior art).** In a
1D line of packets, each crossing acts on the two packets adjacent in
position, and after the crossing they exchange position: in position
order the gate is P V. At chi = pi/2, P V has the form G(A, B) with
A = 1, B = [[beta, alpha], [alpha, beta]], det A = det B. Nearest-neighbour
circuits of such gates are, by the matchgate literature (Valiant; Terhal
and DiVincenzo; Jozsa and Miyake), classically simulable. Not one of those
papers has been read in this session, and the mapping from flavour qubits
to their qubit convention is not checked. If it holds, gate-only
universality from crossings at chi = pi/2 in this code is excluded,
independently of factorization. This is the obligation the contract
recorded as separate; it is not a verdict of this gate.

## 3. Bridge in the co-moving geometry (written)

Notation of contract 2 Sec. 4: c(q1, q2) = phi_f(q1) phi_s(q2), particle 1
the fast packet (carrying e^{iq1 L}, centred at x = +L), particle 2 the slow
one (e^{-iq2 L}, x = -L), y = x1 - x2. Changes with respect to contract 2:

**(i) Eigenfunctions.** The general contact argument of contract 2 Sec. 4(i)
((+,+)) and of the flavour report Sec. 4 item 1 ((+,-)) uses only the four
waves sharing one free eigenvalue and contact antisymmetry; it holds for
any (q1, q2) away from the degeneracies q1 = q2 (and their pi partners,
Lemma 1 of 1711.03920 as recorded in the flavour contract). On the
supports q1/mu in [3 - m, 3 + m], q2/mu in [1 - m, 1 + m], m = sqrt(mu) <
1/sqrt10, these are disjoint (M). Worked examples: E1, E2 certify both
eigenfunctions exactly at the co-moving pair e^{iq1} = (4+3i)/5,
e^{iq2} = (12+5i)/13 (both momenta positive), chi = pi/2 and chi = 0.

**(ii) Which wave is incoming.** On y >= 0 the eigenfunction is
[incoming, q1 on x1] - T [swap, q2 on x1]. Positive-band positive q moves
toward negative x with speed omega'(q), so dy/dt = omega'(q2) - omega'(q1)
for the incoming term. omega'(q)^2 = nu^2 s/(mu^2 + nu^2 s), s = sin^2 q,
is increasing in s (V), so omega'(q1) > omega'(q2) on the supports and
the term with the fast momentum on the larger coordinate is incoming, as
in contract 2. At t = 0 the swap term is centred at y = -2L (wrong side),
as there. In the (+,-) sector, Gamma phi_s moves as phi_s (flavour report
Sec. 4 item 3), so the same holds.

**(iii) Initial error.** Unchanged: O(mu^{3/4}) from the tail bound with
D = L.

**(iv) Time T = 20L.** Rational bounds for 0 < mu < 1/10 (V):
omega'^2 >= 87/100 on the fast support, omega'^2 <= 16/25 on the slow
support, so omega'(q1) - omega'(q2) >= 93/100 - 4/5 = 13/100. At t = T the
incoming y-centre is <= 2L - 20L (13/100) = -3L/5 and the outgoing
y-centre >= +3L/5. The wrong-side restriction of either term needs a
one-particle deviation >= 3L/10. In the limit v_f - v_s > 0.24 (V), giving
-2.83L; the rational bound is only what is uniform on 0 < mu < 1/10.

The tail bound of contract 2 (iii) needs the residual phase derivatives
uniform for 0 <= t <= T: t delta^2 |omega''| <= 20 ceil(mu^{-2}) mu^3 C/mu =
O(1), five times the contract-2 constant. With D = 3L/10, delta D ≍
mu^{-1/2}, the wrong-side mass is O(mu^{3/2}) and the norm error O(mu^{3/4}),
as in contract 2.

**(v) Phase variation.** The scaled denominators at chi = pi/2 are
|a_s - i a_f| and |-a_s - i a_f|, both sqrt(a_f^2 + a_s^2) > 0; T_+ and T_-
are smooth in (q1/mu, q2/mu) with gradient O(1/mu); on supports of width
mu^{3/2}: sup |T - T_c| = O(mu^{1/2}). Unchanged.

**(vi) Assembly.** Exactly as in the flavour report Sec. 5 (reused F3/F4,
label-agnostic): AA and BB evolve freely (G = +1, exactly); AB and BA mix
through the two P-sectors with
T_+ -> (a_f + z a_s)/(a_s + z a_f), T_- -> (a_f - z a_s)/(z a_f - a_s),
z = -i, a(K) = sqrt(1 + K^2) + K (contract 2, P6, symbolic in K). Error
O(mu^{1/2}) + O(mu^{3/4}); per-column uniformity gives operator norm
uniformity. Leakage vanishes because every image lies in the span of
B_out up to o(1).

## 4. Why r_co and not 1/r_co

T_+ = T(q1, q2) with q1 the particle first in the creation order and on
the larger coordinate of the incoming wave (ii). Here that is the fast
packet, so r = a1/a2 = a_f/a_s = r_co (verifier checks C). In the
opposite-moving flavour gate the same rule gave r = a(1)/a(-2) =
a(1) a(2), since a(-K) = 1/a(K). In both cases r = e^{theta_1 - theta_2},
theta = asinh K: one family in the rapidity difference, as hypothesis
H_co stated. This choice was fixed by the contract's creation order before
the comparison.

## 5. Low-energy admission under U^2

The flavour report Sec. 3 argument is momentum-general; P5 and P6 of
contract 2 are symbolic in K, so omega(mu K)/mu -> sqrt(1 + K^2) holds on
both supports (K near 1 and 3). Not an interacting QFT limit.

## 6. What the verifier does and does not certify

Passed 52/52: 50 exact (E1-E2, reused F1 and F3/F4, M, V, C except two,
A1-A4, the two A5 identities) and 2 numerical positivity checks,
`C-beta>0` and `C-concurrence(V|AB>)>0`, which evaluate exact expressions
with `sp.N(..., 30)` (R2). Exact argument for both: r_co > 1, so
beta = 2 r_co/(1 + r_co^2) > 0 and Im alpha = (r_co^2 - 1)/(r_co^2 + 1) > 0
(identities certified exactly by `C-beta=2r/(1+r^2)` and
`C-alpha=i(r^2-1)/(r^2+1)`); hence the concurrence 2|alpha beta| > 0.
r_co > 1 because a(3) = sqrt10 + 3 > sqrt2 + 1 = a(1). The A5
determinant values are recorded diagnostics. Not certified: the bridge adaptation of Sec. 3 (written),
the U^2 admission (written), the verdict, physical three-packet
factorization, graded tensor structure, the A5 reading.

## 7. Scope and balance

- Holds for this code, this rule, chi = pi/2, these two packets, T = 20L,
  mu -> 0. No parameter was varied.
- With the opposite-moving result, two-packet crossings of either
  orientation act by one family V(r), r = e^{Delta theta}, which satisfies
  Yang-Baxter (A3) and the braid relation (A4). This removes the specific
  objection that same-direction crossings might use a different matrix.
- It does not establish three-packet factorization, composability or
  universality. Flavour number stays conserved. A5 indicates that, at
  chi = pi/2, crossing gates in position order meet the matchgate
  determinant condition; if the prior-art reading holds, crossings alone
  do not give universality here.
- NOVELTY = OPEN: six-vertex / XXZ R-matrices, Yang-Baxter and matchgate
  simulability are prior art; the two-particle solution is from 1711.03920.
- Balance: this contract is closed; no further contract follows
  automatically. Coexistence stays OPEN.
