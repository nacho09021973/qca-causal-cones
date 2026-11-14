# Thirring crossing-matchgate gate (A5): results

2026-11-14. Author: Claude Code (Claude Opus 5.5). **PRELIMINARY: written
argument plus exact author checks; no independent review; no promotion.**

Contract [THIRRING_MATCHGATE_A5_GATE.md](../theory/THIRRING_MATCHGATE_A5_GATE.md),
frozen at `915e55f`. Authorizations (user, 2026-11-14): drafting; Q-a (F a
declared premise), Q-b (download sources), freezing; then «T2–T4: SÍ,
autorizados secuencialmente», with the order T2, T3, T4, «No presupongas
que la permutación fermiónica introduce únicamente una fase global»,
«Respeta el signo de alpha del repositorio», no PASS without complete
evidence. Sources acquired at `7fa79e7` and `a1cfd20` (`sources/README.md`).
Verifier `scripts/verify_thirring_matchgate_a5.py`, committed before
running at `eae7876`; it imports the co-moving verifier read-only.
One run, 26/26 exact ([output](2026-11-14--thirring-matchgate-a5.txt),
[record](2026-11-14--thirring-matchgate-a5.json)). A manual negative
control (comparison with +P v instead of -P v) fails, as it should; it
produces no retained result.

## 1. Verdict

`MATCHGATE_SIMULABLE_UNDER_F` (author, PRELIMINARY). Assume F (Sec. 2).
Then, in the flavour code at chi = pi/2, with the admitted resources
(product flavour-basis input, final flavour readout of any subset of
packets, no ancilla, intermediate or adaptive measurement, postselection
or control), the logical map of N packets is a circuit of nearest-neighbour
gates G = -P V(r) on the position-ordered register, each an allowable
matchgate G(A, B) with A = -1, B = -[[beta, alpha], [alpha, beta]] in SU(2).
By Valiant (STOC 2001, pp. 118-120) and Terhal-DiVincenzo (p. 3-4), the
probabilities of computational-basis outcomes on any subset of packets
can be computed, and outcomes sampled, in classical polynomial time; by
Jozsa-Miyake (Theorem 1, p. 2), so can <Z_k> on any single packet for any
product input. Hence, under F, crossings alone at chi = pi/2 do not give
universal quantum computation in this code with these resources: by the
remark of Jozsa-Miyake p. 3, bounded-error decision problems solved by
such circuits with computational-basis inputs would lie in P.

This is conditional on F and limited as stated in Sec. 6. It is not a
Thirring no-go.

## 2. F, as used

F (declared premise, contract): the N-packet logical map, in the mu -> 0
limit, is the time-ordered product of two-packet crossing maps, each acting
on its pair with the other packets as spectators, with leakage -> 0.

Formalization used for T2 (stated here so that T2 has a definite object):
a crossing of packets a and b, with a on the larger coordinate before the
crossing, acts on the fermionic Fock space as the even operator

    W_ab = sum_{x,y,x',y'} V(r_ab)[(x'y'),(xy)] c+_{a x'} c+_{b y'} c_{b y} c_{a x},

identity on all other occupations, r_ab = e^{theta_a - theta_b}, where
c+_{p f} creates the freely evolved packet p with flavour f (packet labels
by identity, readout frame B_out = F^T B_mu as in the promoted reports).
On two packets this is the promoted two-packet result, whose columns are
(sqrt2 Pi_{f_a} phi_a) wedge (sqrt2 Pi_{f_b} phi_b) = c+_{a f_a} c+_{b f_b}|0>,
first factor = the packet on the larger coordinate (flavour gate: right
packet; co-moving gate: fast packet at +L) (S1).

## 3. T2: the physical crossing as s P V on adjacent slots

**Register.** Between crossings the packet order in x is constant. Define
the position-ordered basis |f_1 ... f_N>_pos = c+_{pi(1) f_1} ... c+_{pi(N) f_N}|0>,
pi(k) the packet in slot k counted from the right. Readout of a slot is
readout of the flavour of a known packet, since pi is classically known.

**Adjacency (written).** Packet centres move on straight lines
x_p(t) = x_p(0) - t v_p with pairwise distinct v_p (distinct K, v = tanh
theta increasing). If packets p and s coincide at t* and q was strictly
between them for t < t*, then by continuity x_q(t*) lies between
x_p(t*) = x_s(t*), so q coincides too. Hence a crossing of exactly two
packets is always between adjacent slots. A simultaneous coincidence of
k >= 3 packets reverses a block of adjacent slots; any resolution of it
into pairwise crossings is a sequence of adjacent transpositions, so it
is still a nearest-neighbour circuit. For k = 3 both resolutions give the
same operator (S4: Fock-level products equal G12(y) G23(xy) G12(x) and
G23(x) G12(xy) G23(y), and these are equal). For k >= 4 the uniqueness of
the result is not checked; it is not needed for simulability, only for F
to define a unique map. Each pair crosses at most once, so the circuit has
at most N(N-1)/2 gates.

**Sign (certified, not assumed).** For a generic symbolic 4x4 v (16
symbols), in the explicit Jordan-Wigner Fock model of three packets:

- a crossing of slots (1,2) maps the register by kron(-P v, 1), with the
  third packet behind the pair in the creation string;
- a crossing of slots (2,3) maps it by kron(1, -P v), with the first packet
  in front;
- the same holds with the packets relabelled (S2), and W_ab commutes with
  the creation operator of a third packet on the logical sector (S3).

Written reason: after the crossing, packet b is on the right, so the
position-ordered string has c+_{b y'} c+_{a x'} = -c+_{a x'} c+_{b y'}
(distinct modes anticommute; every packet holds exactly one fermion for
both flavours, so the sign does not depend on flavours). The pair is
adjacent in the string, and W_ab is even, so spectators contribute no sign.
Therefore s = -1 on every basis state of the register, for every crossing,
independent of V; the product of signs is (-1)^(number of crossings), a
global phase of the whole computation. This is a derived statement under
the formalization above, not an assumption.

Free evolution between crossings: under U^2 both flavour components of a
packet carry the same phase e^{-2i omega(q)} (flavour report Sec. 3), and
it is absorbed in the comparison frame; it does not act on flavour.

## 4. T3: gate class with the repository sign

Certified (M1-M4), r > 0, chi = pi/2, alpha = +i (r^2 - 1)/(r^2 + 1),
beta = 2r/(1 + r^2):

- G(r) = -P V(r) has nonzero entries only in the parity pattern; on
  {00, 11} it is A = -1; on {01, 10} it is B = -[[beta, alpha], [alpha, beta]];
  A and B are unitary with det 1, so G = G(A, B) in the sense of
  Jozsa-Miyake eq. (1) (p. 2) and of Terhal-DiVincenzo eq. (1) (p. 3,
  U^1, U^2 in SU(2)).
- Valiant's five matchgate identities (p. 118; signs checked on the page
  image) hold for G(r) under both assignments of the middle rows and
  columns, and B(4,4) = -1 != 0, so Proposition 3 (p. 118) applies.
- Second route: P V(r) = exp(+i theta(r)/2 (XX + YY)), theta(r) =
  2 atan(r) - pi/2 (cos theta = 2r/(1+r^2), sin theta = (r^2-1)/(r^2+1)),
  and with a1 = s- (x) 1, a2 = Z (x) s-, a1^+ a2 + a2^+ a1 = (XX + YY)/2: the
  gate is generated by a quadratic fermionic Hamiltonian, the
  Terhal-DiVincenzo H2 type (p. 4). The two routes agree.
- The user's hint exp(-i theta/2 (XX + YY)) has the opposite off-diagonal
  sign (differs by 2i sin theta, nonzero for r != 1). The repository
  convention gives the + sign. Both signs are matchgates, so the verdict
  does not depend on it.

## 5. T4: hypotheses of the theorems

| Hypothesis (source, page) | Architecture under F | Status |
| --- | --- | --- |
| Gates on bits with indices differing by one (Valiant Main Theorem (b), p. 119; T-D Thm 1, p. 3; J-M Thm 1(i), p. 2) | adjacent slots of the position register (Sec. 3) | met |
| Only parity-pattern entries nonzero; matchgate realizable (Valiant p. 118-119, Prop. 3 with B(4,4) != 0) | M1, M2 | met |
| G(A, B), A, B in SU(2) (T-D p. 3) or U(2) with equal det (J-M p. 2) | M1 | met |
| Input: computational-basis bitstring (Valiant, T-D) / any product state (J-M) | product flavour-basis states | met |
| Output: k-bit subset marginals and sampling (T-D (2), (3), p. 4; Valiant Thm 4, p. 119; Measurement Theorem, p. 120) / single line <Z_k> (J-M) | final flavour of any subset of packets | met |
| No adaptivity needed (J-M; T-D also cover adaptive) | none admitted | met |
| Poly-size, uniform family | <= N(N-1)/2 gates; crossing order and r_pq = a(K_p)/a(K_q) computed classically from (K_p, x_p(0)) by sorting crossing times | met |

Simulation notion obtained: classical polynomial-time evaluation of the
outcome probabilities of any subset of packets and polynomial-time
sampling, for computational-basis (flavour product) inputs (Valiant,
Terhal-DiVincenzo); computation of <Z_k> to m digits in poly(N, m) time
for any product input (Jozsa-Miyake p. 3 definition). The gate parameters
r_pq are real algebraic numbers when the K_p are rational; precision
handling is that of the cited theorems (not re-derived here).

## 6. Scope and what is not shown

- Everything is conditional on F (multi-packet factorization), which is
  OPEN; the Fock formalization in Sec. 2 is the reading of F used.
- The logical map is the mu -> 0 limit; finite-mu corrections are not
  covered.
- Only chi = pi/2, this flavour code, these resources. For chi != pi/2 and
  r != 1, P V is not a matchgate (co-moving report, A5), and nothing here
  says whether crossings there are universal.
- Not shown: universality or its absence with other resources (ancillas,
  intermediate or adaptive measurement, non-product inputs), other codes,
  or non-factorized evolutions; a Thirring no-go; uniqueness of F's map at
  >= 4-fold coincidences.
- Knill (quant-ph/0108033) was acquired and not used.
- NOVELTY = OPEN: matchgate simulability, free-fermion simulation and the
  Yang-Baxter / six-vertex structure are prior art; the contribution, if
  any, is the identification of the crossing gates with that class.

## 7. What the verifier does and does not certify

Certified (26/26 exact): S1-S4 (Fock-model sign bookkeeping for generic
v, spectator independence, three-packet sequences), M1-M4 (gate class,
Valiant identities, exponential form, Jordan-Wigner). Not certified: F;
the adjacency argument (written); T4 (written, against the sources and
pages listed in `sources/README.md`).

## 8. Balance

Contract closed. Coexistence stays OPEN. Under F, the crossing
architecture at chi = pi/2 in the flavour code is excluded as a route to
universality with the admitted resources. Independent review needs
separate permission; no further contract follows automatically.
