# Thirring flavour-packet gate

2026-11-14. Author: Claude Code (Claude Opus 5.5). Initial status **OPEN**.
Freeze this document (commit) before any execution.

## Authorization and budget

The Thirring coexistence line stopped on 2026-11-09 after its two-contract
budget («no automatic third contract»). This contract is a **new explicit
user authorization**, not a budget reset: after the read-only evaluation of
2026-11-14 the user replied «me gusta tu plan, adelante, autorizado» and,
asked separately, decided the quantifier below. One contract; mandatory
balance on closure; no further contract follows automatically.

**Q2-A decision (user, 2026-11-14):** a packet of definite flavour (defined
below) counts as a low-energy carrier **under U^2**: the reference rule for
the relativistic regime is the same fixed rule taken two steps at a time.
Under a single step U the flavour alternates A <-> B; this is admitted.
Q1-B, Q3-A and Q4-A apply unchanged.

## Known, question, abandonment

Known (read this session):
- sources/1711.03920v1.pdf p.3: Lemma 1 (exactly four degenerate
  two-particle solutions: swap and pi-shifted partners) and Eq. (12)
  (interacting solutions in sectors (+,+) and (+,-) with phases T_+, T_-).
- reports/2026-11-09--thirring-low-energy-packet.md Secs. 3-4: Gamma
  structure, U(1-P) = F(1-P) exactly with P = (1 - Gamma_1 Gamma_2)/2, exact
  P-sector eigenfunctions in sector (+,+), packet/scattering bridge and tail
  bounds; verdict NO_ENTANGLER_IN_DECLARED_PACKET_CODE for the band code
  (PRELIMINARY, repaired, not re-reviewed).
- state/CURRENT_STATE.md, entry «Thirring, conceptual correction —
  2026-11-14» (`0ca0685`): candidate phases T_+ != T_- unless z^2 = 1; the
  XXZ reading is not certified.

Question: in the limit mu -> 0, does the autonomous collision of two
flavour packets act on the declared flavour code as a unitary logical gate
with vanishing leakage, and is that gate non-diagonal in the flavour basis?

Abandonment of the flavour route (this code and rule): a positive
asymptotic leakage, or a limiting logical action that is diagonal in the
flavour basis (exchange amplitude zero). Neither is a Thirring no-go.

## Frozen construction

Rule and parameters as contract 2 (`theory/THIRRING_LOW_ENERGY_PACKET_GATE.md`):
infinite line, two fermions, U = F J, chi = pi/2, nu = sqrt(1 - mu^2),
0 < mu < 1/10, limit mu -> 0. Fourier convention |q> = (2pi)^(-1/2)
sum_x e^{-iqx}|x>, normalized positive-band v_q^+, W and component labels
R, L as in `scripts/verify_thirring_low_energy_packet.py` (`W_pre`).
No ancillas, intermediate measurement, postselection, external control or
parameter change. Ideal preparation and final readout in the declared modes.

Flavour: Gamma = sigma_z (-1)^x with sigma_z = +1 on R, exactly the Gamma of
check P2 in that verifier. One-particle projectors Pi_A = (1 + Gamma)/2,
Pi_B = (1 - Gamma)/2.

Packets (envelope, width and distances of contract 2): h(t) = sqrt(15)/4
(1 - t^2) on |t| <= 1, delta = mu^(3/2), L = ceil(mu^(-2)), T = 4L (even).
- right packet phi_r: positive band, momentum centre +mu (k = 1), envelope
  delta^(-1/2) h((q - mu)/delta), translated to x = +L by e^{iqL};
- left packet phi_l: positive band, momentum centre -2mu (k = 2), envelope
  delta^(-1/2) h((q + 2mu)/delta), translated to x = -L by e^{-iqL}.

Logical qubit of each packet: |0> = flavour A, |1> = flavour B. The four
columns are B_mu|f_r f_l> = (sqrt2 Pi_{f_r} phi_r) wedge (sqrt2 Pi_{f_l} phi_l),
right packet first in the creation order. Admission checks (not assumptions):
||Pi_f phi||^2 = 1/2 exactly, columns orthonormal, B_mu an isometry.

Output frame B_out = F^T B_mu (comparison/readout frame, not an applied
inverse evolution). T even, so the flavour of each free packet is restored.
No other packet, centre, time, frame or code basis is admissible; no local
basis change may be chosen after results.

## Low-energy admission under U^2

Show: U^2 maps each flavour packet to the same flavour, acting on its
positive-band part as e^{-2i omega(q)} and on its Gamma-partner (negative
band near q + pi) with the same phase; both parts share the group velocity;
omega(mu K)/mu -> sqrt(1 + K^2) on the support. This is the Q2-A admission
decided above; it does not establish an interacting relativistic QFT limit.

## Observables and success

K_mu = B_out^* U^T B_mu, E_mu = (I - B_out B_out^*) U^T B_mu, operator
norms uniform over logical inputs.

- S1: ||E_mu|| -> 0.
- S2: a fixed unitary V on C^2 tensor C^2 and phases alpha_mu with
  ||K_mu - e^{i alpha_mu} V|| -> 0.
- S3: V non-diagonal in the flavour basis: an explicit pair f != f' with
  |<f'|V|f>| > 0 in the limit, value given exactly.
- S4: V entangling: explicit product input, strictly positive limiting
  entanglement measure.

Candidate (hypothesis H_flav, OPEN, from the session reading, not a
premise): V = 1 on |AA>, |BB>; on {|AB>, |BA>} the matrix [[al, be], [be, al]]
with al = (T_+ + T_-)/2, be = (T_+ - T_-)/2 evaluated at the limiting
rapidities, up to convention-dependent phases. Execution must derive V
independently, including which sector and momentum labels (total momentum
P versus P + pi) each phase belongs to, and the antisymmetrization.

## Method

Exact analytic packet/scattering analysis first, reusing the contract-2
bridge (exact eigenfunctions, unitarity, tail and phase-variation bounds)
and extending it to the (+,-) sector with Eq. (12) lower sign. The bridge
must be proved for these normalized finite-time packets; a plane-wave phase
without it decides nothing. No finite scan or fit decides an asymptotic
claim. Any computation: permanent verifier committed before execution,
failed runs retained, exact command entries added to `.claude/settings.json`.
Reviewed verifiers are reused read-only, never modified. Written analytic
steps are listed separately from machine checks.

## Verdicts

- `FLAVOUR_PACKET_EXCHANGE_GATE_IN_DECLARED_CODE`: S1-S4 proved.
- `FLAVOUR_PACKET_GATE_DIAGONAL`: S1-S2 proved, S3 fails (route abandoned).
- `NO_FLAVOUR_PACKET_GATE`: S1 or S2 disproved (route abandoned).
- `OPEN_AFTER_BOUNDED_EXACT_ATTEMPT`: otherwise; record the open obligation.

All author PRELIMINARY pending independent review (separate permission).

## Not claimed by any verdict

Universality (flavour number N_A is conserved under U^2, so the gates
preserve Hamming weight on raw qubits; each pair of packets crosses at most
once in 1D), composability with controlled error, a relativistic
interacting QFT limit, Thirring no-go, novelty (NOVELTY = OPEN; conservation
obstructions and exchange-based encoded universality are prior art).

## Execution bound

One working session, one construction, no parameter or packet search. Stop
on a proved verdict or when a required estimate cannot be closed. After
closure: balance in `state/CURRENT_STATE.md`; coexistence stays OPEN unless
actually proved; no promotion or merge authorized by this charter.

## Before freezing

No packet evolution, scattering evaluation or numerical experiment has been
performed for this construction. Packet choices are inherited from
contract 2 with one centre per side; they are not optimized.
