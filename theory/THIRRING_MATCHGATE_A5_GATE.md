# Thirring crossing-matchgate gate (A5)

2026-11-14. Author: Claude Code (Claude Opus 5.5). Initial status **OPEN**.
Freeze this document (commit) before any execution.

## Authorization and budget

`state/CURRENT_STATE.md` (promotion entry «Co-moving packet result
promoted — 2026-11-14», `1722dd0`) left no contract open and no work
authorized. User instruction, 2026-11-14: «redacta el contrato de A5 con
matchgates» (drafting). Then (user, 2026-11-14): Q-a and Q-b decided as
below, and «Autorizo congelar y hacer commit … con F explícitamente
asumida, T1–T4 pendientes»; «No autorizo adelantar un PASS ni modificar el
alcance del contrato». Source acquisition for T1 is authorized under Q-b.
Execution of T2-T4, review and promotion each need a separate user
authorization. One contract; mandatory balance on closure; no further
contract follows automatically.

## Known, question, abandonment

Known (read this session, with source):
- `reports/2026-11-14--thirring-comoving-packet.md` (promoted in frozen
  scope, `1722dd0`): two flavour packets crossing in either orientation act
  on the flavour code (fast/first packet first, labels by packet identity)
  by V(r) = 1 (+) [[alpha, beta], [beta, alpha]] (+) 1, r = e^{theta_1 -
  theta_2}; at chi = pi/2, alpha = i (r^2 - 1)/(r^2 + 1),
  beta = 2r/(1 + r^2).
- Same report, A5 (certified identities): det A(P V) = 1 and
  det B(P V) = 1 - (z^2 + 1)(r^2 - 1)/(z^2 r^2 - 1), with A the block on
  {00, 11} and B the block on {01, 10}; for r != 1 the two are equal iff
  chi = pi/2 mod pi. Determinant values for V and fSWAP V are unequal.
- Astra review of that report (`091f3b8`), block 5: in position order the
  crossing gate is P V up to a sign common to the four basis states; the
  determinant condition identifies an abstract matchgate in the written
  basis; what is missing is that a many-packet evolution is represented by
  the corresponding circuit, and which preparations and measurements are
  admitted. (AI review: a pointer, not a source.)
- Flavour-packet gate, "Not claimed": flavour number N_A is conserved, each
  pair of packets crosses at most once in 1D.

Not known (not read; [UNVERIFIED] until read in the original):
- L. G. Valiant, matchgates and classical simulation (SIAM J. Comput.
  31 (2002); STOC 2001 version).
- B. M. Terhal and D. P. DiVincenzo, classical simulation of
  noninteracting-fermion circuits, Phys. Rev. A 65, 032325 (2002),
  arXiv:quant-ph/0108010.
- R. Jozsa and A. Miyake, matchgates and classical simulation of quantum
  circuits, Proc. R. Soc. A 464, 3089 (2008), arXiv:0804.4050: claimed to
  state that nearest-neighbour G(A, B) circuits with det A = det B, product
  computational-basis input and computational-basis output are classically
  simulable, and that adding SWAP (or non-nearest-neighbour action) gives
  universality.
- E. Knill, arXiv:quant-ph/0108033, fermionic linear optics.
Exact theorem statements, hypotheses (gate set, input class, output
class, strong versus weak simulation, adaptivity) and pages are to be
read at execution; nothing above is a premise.

Question: in the declared crossing architecture of the flavour code at
chi = pi/2, assuming the many-packet logical map is the ordered product of
the two-packet crossing gates (hypothesis F, a declared premise, not a
result), is the resulting family of computations inside a matchgate class
that the primary sources prove classically simulable, with the
preparations and readout admitted by the Thirring rules?

Abandonment of gate-only universality from crossings in this code and
rule at chi = pi/2 (conditional on F): verdict `MATCHGATE_SIMULABLE_UNDER_F`.
That is not a Thirring no-go: it leaves other couplings, codes, resources
and non-factorized evolutions untouched. Abandonment of this contract's
line without conclusion: the mapping to a nearest-neighbour matchgate
circuit fails (non-global signs, gates acting on non-adjacent qubits, or
a theorem hypothesis not met).

## Frozen architecture

Rule U = F J, chi = pi/2, flavour code, Q2-A carriers under U^2, all as in
the flavour-packet and co-moving contracts. N >= 2 flavour packets on the
infinite line, positive band, pairwise distinct momentum centres
K_1, ..., K_N (signs free), initial positions ordered and separated so that
every pair that crosses does so once, in the mu -> 0 regime of the two
promoted contracts. No ancillas, intermediate measurement, postselection,
adaptive control or parameter change. Admitted resources only:

- preparation: product states in the flavour basis (A/B per packet);
- readout: final flavour of each packet (computational basis), all
  packets or a subset;
- the time order of crossings fixed by the kinematics.

Logical qubits are indexed by **position order**. A crossing of the
packets in positions j, j+1 acts on qubits (j, j+1) by
G_j = s_j P V(r_j), s_j a sign to be derived, r_j the rapidity ratio of the
two packets, first factor = the packet arriving from the right.

Hypothesis F (premise, OPEN): the N-packet logical map, in the limit, is
the ordered product of the G_j over the crossing sequence, with leakage
-> 0. This contract does not prove or test F.

## Tasks

- T1 (sources). Acquire the four papers into `sources/` with SHA256 in
  `sources/README.md`; read the theorem statements and record
  `file.pdf p.N` for each hypothesis used: gate definition G(A, B),
  determinant condition, nearest-neighbour requirement, input and output
  classes, the type of simulation (marginal probabilities, sampling,
  exact or approximate), and the SWAP / non-nearest-neighbour
  universality statement.
- T2 (mapping). Prove that, under F, the logical map on (C^2)^(x N) in
  position order is a product of nearest-neighbour two-qubit gates
  s_j P V(r_j): derive the fermionic reordering sign s_j (one fermion per
  packet for both flavours), show it is common to all basis states of the
  pair and to the rest of the register, and that no crossing acts on
  non-adjacent positions.
- T3 (gate class). Exact: for every r > 0 at chi = pi/2, P V(r) = G(A, B)
  with A = 1, B = [[beta, alpha], [alpha, beta]], det A = det B, A, B
  unitary. Second route (robustness): exhibit P V(r) as exp(i H(r)) up to
  a global phase, with H quadratic in the Jordan-Wigner fermions of the
  two qubits, or show this fails; the two routes must agree.
- T4 (match). Check, hypothesis by hypothesis, that the admitted
  preparations, readout and gate sequence satisfy the cited theorem; state
  exactly which simulation notion follows.

Any computation: permanent verifier in `scripts/` committed before
execution, failed runs retained, exact command entries in
`.claude/settings.json`; reviewed verifiers reused read-only.

## Verdicts

- `MATCHGATE_SIMULABLE_UNDER_F`: T1-T4 succeed; under F, every admitted
  computation of the declared architecture is classically simulable in
  the sense of the cited theorem (stated precisely).
- `NOT_A_NN_MATCHGATE_CIRCUIT`: T2 or T3 fails (stated counter-structure);
  the A5 reading is withdrawn for this architecture.
- `THEOREM_HYPOTHESES_NOT_MET`: T2-T3 succeed but a hypothesis of the
  primary theorem (input, output, simulation notion) is not met; record
  which.
- `OPEN_AFTER_SOURCE_READING`: otherwise; record the open obligation.

All author PRELIMINARY pending independent review (separate permission).

## Not claimed by any verdict

Hypothesis F (three- or N-packet factorization); graded tensor structure
beyond the sign bookkeeping of T2; any statement at chi != pi/2, for other
codes, resources (ancillas, intermediate or adaptive measurement,
non-product inputs), packets or couplings; a Thirring no-go; universality
by other means. NOVELTY = OPEN: matchgate simulability and free-fermion
simulation are prior art; the contribution, if any, is the identification
of the crossing gates with that class.

## Execution bound

One working session. No search over packets, couplings or architectures.
Stop on a proved verdict or when a required source cannot be obtained or
read. After closure: balance in `state/CURRENT_STATE.md`; coexistence stays
OPEN; no promotion or merge authorized by this charter.

## User decisions (2026-11-14)

- Q-a: F stays a declared premise. The contract answers the conditional
  question F => simulability; factorization is a different problem.
- Q-b: T1 may download the four originals, read-only, into `sources/`,
  recording provenance, version and SHA256; only pages and statements
  actually read are cited; a source that cannot be verified stays
  [UNVERIFIED] and T1 is not closed.
- The user notes that Jozsa-Miyake's universality from enlarged resources
  does not imply that this restricted gate family becomes universal with
  SWAP. Recorded; no such claim is in scope.

## Before freezing

No source has been acquired or read for this contract; no computation has
been run. A user-supplied algebraic hint (AI-assisted, not a source, not a
premise) is recorded for T3 to check: at chi = pi/2, P V(r) has
{01,10} block [[b, -ic], [-ic, b]], b = 2r/(1+r^2), c = (r^2-1)/(r^2+1),
equal to exp[-i theta(r)/2 (XX + YY)], theta(r) = 2 arctan r - pi/2. In
the repo convention (co-moving report, Sec. 1) alpha = +ic, so the
off-diagonal sign differs and the exponent sign would flip; T3 must
derive the sign itself. The hint does not bear on T2, which stays the
priority: without T2 the identity of T3 does not apply the theorems.
