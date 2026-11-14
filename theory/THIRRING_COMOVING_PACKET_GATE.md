# Thirring co-moving packet gate

2026-11-14. Author: Claude Code (Claude Opus 5.5). Initial status **OPEN**.
Freeze this document (commit) before any execution.

## Authorization and budget

`state/CURRENT_STATE.md` (promotion entry of 2026-11-14, `58a8bd4`) left no
contract open and no work authorized. This contract follows a new explicit
user instruction, 2026-11-14: «si redacta el contrato y luego congelas».
That instruction authorizes **drafting and freezing only**. Execution,
independent review and promotion each need a separate user authorization.
One contract; mandatory balance on closure; no further contract follows
automatically. Q1-B, Q2-A, Q3-A and Q4-A apply unchanged (as in
`theory/THIRRING_FLAVOUR_PACKET_GATE.md`).

## Known, question, abandonment

Known (read this session):
- `reports/2026-11-14--thirring-flavour-packet.md` Secs. 4-5: for the two
  declared opposite-moving flavour packets, T_+ = (a_r + z a_l)/(a_l + z a_r),
  T_- = (a_r - z a_l)/(z a_r - a_l), z = e^{-i chi}, a(K) = sqrt(1 + K^2) + K,
  and the logical block al = (T_+ + T_-)/2, be = (T_+ - T_-)/2 on
  {|AB>, |BA>}, identity on |AA>, |BB>. Promoted in that frozen scope only
  (`58a8bd4`), verdict `FLAVOUR_PACKET_EXCHANGE_GATE_IN_DECLARED_CODE`.
- Same report Sec. 4 item 1: T_- is written through g_+(q1), g_-(q2') for
  general momenta; the contact argument uses only the four waves sharing one
  free eigenvalue. Nothing in that formula refers to the direction of motion.
- `theory/THIRRING_LOW_ENERGY_PACKET_GATE.md` (frozen construction): Fourier
  convention under which positive-band positive q moves toward negative x;
  envelope h, delta = mu^(3/2), L = ceil(mu^(-2)).
- `theory/THIRRING_FLAVOUR_PACKET_GATE.md` Known list (read in its own
  session, to be re-read at execution): sources/1711.03920v1.pdf p.3,
  Lemma 1 (four degenerate two-particle solutions) and Eq. (12).

Hand algebra of this session (author, PRELIMINARY, no machine check; it is a
hypothesis for the verifier, not a premise): with r = a_r/a_l,
al = z(r^2 - 1)/(z^2 r^2 - 1), be = r(z^2 - 1)/(z^2 r^2 - 1); the six-vertex
parameter Delta = (1 + al^2 - be^2)/(2 al) = (z^2 + 1)/(2z) = cos chi, independent
of r; 1 + al^2 - be^2 = 0 iff z^2 = -1, so chi = pi/2 is the free-fermion
point.

Not sources: the pasted AI evaluation of 2026-11-14 (its symbolic
Yang-Baxter check and its reading of a "Lemma 7, Sec. 8" of a 2025 Entropy
paper). That paper is not in `sources/` and `biblioteca/` is absent in this
checkout: [UNVERIFIED].

Question (main): in the limit mu -> 0, does the autonomous overtaking of two
flavour packets moving in the **same** direction act on the declared flavour
code as a fixed unitary logical gate with vanishing leakage, and is that gate
the same family V(r) as in the opposite-moving case, with r the ratio of the
two packets' a(K)?

Question (algebraic, part A): do the family V(r) and its permuted form
satisfy the Yang-Baxter / braid relations exactly, and in which form?

Abandonment of the three-crossing route built on one family V(r) (this code
and rule): a positive asymptotic leakage for the co-moving pair, or a
limiting co-moving gate that is not V(r') for the declared r' (including a
diagonal gate). Neither is a Thirring no-go. Separately recorded, not decided
by this contract: if the logical gates are free-fermionic in the matchgate
sense, gate-only universality is excluded by prior art still to be read.

## Frozen construction

Rule and parameters as contract 2: infinite line, two fermions, U = F J,
chi = pi/2, nu = sqrt(1 - mu^2), 0 < mu < 1/10, limit mu -> 0. Fourier
convention, normalized positive-band v_q^+, W, labels R, L and Gamma =
sigma_z (-1)^x, Pi_A = (1 + Gamma)/2, Pi_B = (1 - Gamma)/2, all exactly as in
the flavour-packet gate. No ancillas, intermediate measurement, postselection,
external control or parameter change. Ideal preparation and readout.

Packets (envelope h, delta = mu^(3/2), L = ceil(mu^(-2))), both on the
positive band with positive momentum centre, hence both moving toward
negative x:
- fast packet phi_f: momentum centre +3mu (K_f = 3), envelope
  delta^(-1/2) h((q - 3mu)/delta), translated to x = +L by e^{iqL};
- slow packet phi_s: momentum centre +mu (K_s = 1), envelope
  delta^(-1/2) h((q - mu)/delta), translated to x = -L by e^{-iqL}.

The fast packet starts behind the slow one. Time T = 20L (even). Free
limiting group velocities K/sqrt(1 + K^2): v_f = 3/sqrt10, v_s = 1/sqrt2,
v_f - v_s > 0.24, so at T the limiting centres have exchanged order with
final gap at least 2L. These values are inherited choices plus the one
time needed for overtaking; they are not optimized and no other centre,
position or time is admissible. Execution verifies the direction sign, the
velocities and the gap; a mismatch is a construction failure, not
permission to redefine after results.

Logical qubit of each packet: |0> = A, |1> = B. Columns
B_mu|f_f f_s> = (sqrt2 Pi_{f_f} phi_f) wedge (sqrt2 Pi_{f_s} phi_s), fast
packet first in the creation order. Labels follow packet identity
(momentum), not position. Admission checks (not assumptions):
||Pi_f phi||^2 = 1/2, columns orthonormal, B_mu an isometry. Output frame
B_out = F^T B_mu (comparison frame, not an applied inverse evolution).

## Low-energy admission under U^2

As in the flavour-packet gate, for K = 1 and K = 3: U^2 keeps each packet's
flavour, both Gamma-components carry e^{-2i omega(q)} with one group velocity,
omega(mu K)/mu -> sqrt(1 + K^2) on the support. Not an interacting QFT limit.

## Observables and success

K_mu = B_out^* U^T B_mu, E_mu = (I - B_out B_out^*) U^T B_mu, operator norms
uniform over logical inputs.

- C1: ||E_mu|| -> 0.
- C2: a fixed unitary V_co and phases alpha_mu with
  ||K_mu - e^{i alpha_mu} V_co|| -> 0.
- C3: V_co given exactly, compared with the family
  V(r) = 1 (+) [[al(r), be(r)], [be(r), al(r)]] (+) 1 at
  r_co = a(3)/a(1) = (sqrt10 + 3)/(sqrt2 + 1), up to one global phase.
  Whether r_co or 1/r_co, and which sector carries which phase, must be
  derived from the antisymmetrization and the creation order, not chosen
  after comparison.

Hypothesis H_co (OPEN, not a premise): V_co = V(r_co) in that sense, i.e.
al = i (r_co^2 - 1)/(r_co^2 + 1), be = 2 r_co/(1 + r_co^2) at chi = pi/2.

Part A (exact algebra, symbolic in r, x, y and z, excluding zero
denominators, and specialised to z = -i):
- A1: al, be as functions of r follow from T_+ and T_-.
- A2: Delta = cos chi, independent of r; free-fermion iff z^2 = -1.
- A3: R form, V_12(x) V_13(xy) V_23(y) = V_23(y) V_13(xy) V_12(x) on
  (C^2)^(x3), all eight dimensions, not only by a symmetry reduction.
- A4: braid form with Rcheck = P V (P the qubit swap):
  Rcheck_12(x) Rcheck_23(xy) Rcheck_12(y) =
  Rcheck_23(y) Rcheck_12(xy) Rcheck_23(x). Report which of A3, A4 holds.
- A5 (diagnostic, decides nothing): the matchgate determinant condition for
  V and for V composed with the fermionic swap, exact values.
Part A is unrelated to packets: it does not certify that physical
three-packet scattering factorizes, nor which tensor structure (graded or
ungraded) the fermionic packets require. Both stay OPEN.

## Method

Exact analytic packet/scattering analysis first, reusing the contract-2
and flavour-packet bridges and stating every place the co-moving geometry
changes them: time T = 20L instead of 4L, smaller relative velocity, both
momenta of one sign, distance of the supports (2mu apart, width mu^(3/2))
from the degenerate configurations of Lemma 1 and from q_f = q_s. A
plane-wave phase without the bridge decides nothing. No finite scan or fit
decides an asymptotic claim. Any computation: permanent verifier in
`scripts/` committed before execution, failed runs retained, exact command
entries added to `.claude/settings.json`. Reviewed verifiers are reused
read-only, never modified. Written analytic steps are listed separately from
machine checks.

## Verdicts

- `COMOVING_PACKET_GATE_SAME_FAMILY`: C1-C3 proved with V_co = V(r_co).
- `COMOVING_PACKET_GATE_OTHER_MATRIX`: C1-C2 proved, V_co exact and not
  V(r_co) (route abandoned as stated).
- `COMOVING_PACKET_GATE_DIAGONAL`: C1-C2 proved, V_co diagonal in the
  flavour basis (route abandoned).
- `NO_COMOVING_PACKET_GATE`: C1 or C2 disproved (route abandoned).
- `OPEN_AFTER_BOUNDED_EXACT_ATTEMPT`: otherwise; record the open obligation.

Part A is reported separately as `PASS` / `FAIL` per item, exact. All
author PRELIMINARY pending independent review (separate permission).

## Not claimed by any verdict

Factorization of three-packet scattering; universality (flavour number
conserved, Hamming weight preserved on raw qubits; possible free-fermion
structure at chi = pi/2); composability with controlled error; a
relativistic interacting QFT limit; Thirring no-go; any other packet,
coupling or time. NOVELTY = OPEN: six-vertex / XXZ R-matrices, the
Yang-Baxter equation and free-fermion simulability are prior art.

## Execution bound

One working session, one construction, no parameter or packet search. Stop
on a proved verdict or when a required estimate cannot be closed. After
closure: balance in `state/CURRENT_STATE.md`; coexistence stays OPEN unless
actually proved; no promotion or merge authorized by this charter.

## Before freezing

No packet evolution, scattering evaluation or numerical experiment has been
performed for this construction. The only algebra done is the hand algebra
listed under Known, which is unchecked and is re-derived by Part A.
