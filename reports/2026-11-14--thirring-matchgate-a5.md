# Thirring crossing-matchgate gate (A5): results

2026-11-14. Author: Claude Code (Claude Opus 5.5). **PRELIMINARY: written
argument plus exact author checks; one sealed cross-family review (Astra)
with repairs applied, re-review pending; no promotion.**

**Review (2026-11-14).** Astra `gpt-6-astra`, sealed revision-ciega, one
round, herramientas `2a7342b`, on `3fa82c8`:
[unaltered review](reviews/2026-11-14-thirring-matchgate-a5-astra/informe_astra.md).
REPAIR_REQUIRED; sign, adjacency and gate class PASS (no algebraic
correction). Repairs applied (each checked by the author; user «si, aplica
R1-R5 y re-revisión»):

- R1: W_ab is used only restricted to the one-fermion-per-packet sector
  (Sec. 2).
- R2: uniformity and precision were asserted, not shown. Sec. 5 now gives
  the classical input model, the exact computation of the crossing order
  (ties included) and the gate parameters, and separates the exact
  arithmetic model of Valiant / Terhal-DiVincenzo from the m-digit notion
  of Jozsa-Miyake; error propagation under finite-precision gate entries
  is stated as not re-derived. "Any subset" means one queried assignment.
- R3: Valiant pages corrected: Main Theorem and Theorem 4 p. 120,
  Measurement Theorem p. 121 (checked against the printed page numbers;
  the earlier text was shifted by one). Same fix in `sources/README.md`.
- R4: the universality conclusion is restated: simulability, and an
  efficient universal construction would imply BQP in P (Jozsa-Miyake
  pp. 3, 16); no unconditional separation is claimed (Secs. 1, 8).
- R5: "chi != pi/2" corrected to chi not congruent to pi/2 mod pi (Sec. 6).

Clarifications adopted: the spectator sign argument holds for any number
of spectators (each term of W has four pair operators); for k >= 4
coincidences, any *specified* resolution is simulable; Valiant's character
conventions (inputs as rows, complemented 0/1 reading) leave G unchanged
because G^T = G and (X(x)X) G (X(x)X) = G (Sec. 4); Terhal-DiVincenzo's
adaptive extension is specific (Sec. V, p. 16), not arbitrary adaptivity;
the Jordan-Wigner fermions of M4 are register fermions, not the physical
modes c_{p f}. The original text is in git at `3fa82c8`.

Contract [THIRRING_MATCHGATE_A5_GATE.md](../theory/THIRRING_MATCHGATE_A5_GATE.md),
frozen at `915e55f`. Authorizations (user, 2026-11-14): drafting; Q-a (F a
declared premise), Q-b (download sources), freezing; then «T2–T4: SÍ,
autorizados secuencialmente», with the order T2, T3, T4, «No presupongas
que la permutación fermiónica introduce únicamente una fase global»,
«Respeta el signo de alpha del repositorio», no PASS without complete
evidence. Sources acquired at `7fa79e7` and `a1cfd20` (`sources/README.md`; Valiant page numbers corrected in
the repair commit).
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
For the uniform input model of Sec. 5: by Valiant (STOC 2001, pp.
118-121) and Terhal-DiVincenzo (pp. 3-4), the probability of any one
queried outcome assignment on any subset of packets can be computed, and
outcomes sampled, in classical polynomial time (exact arithmetic model);
by Jozsa-Miyake (Theorem 1, p. 2; definition p. 3), <Z_k> on any single
packet can be computed to m digits in poly(N, m) time. Hence, under F,
by Jozsa-Miyake p. 3, a bounded-gap decision problem accepted on one
packet's final flavour by such circuits lies in P; an efficient universal
quantum computation by crossings alone at chi = pi/2, in this code with
these resources, would therefore imply BQP in P (Jozsa-Miyake p. 16).
No unconditional separation is claimed.

This is conditional on F and limited as stated in Sec. 6. It is not a
Thirring no-go.

## 2. F, as used

F (declared premise, contract): the N-packet logical map, in the mu -> 0
limit, is the time-ordered product of two-packet crossing maps, each acting
on its pair with the other packets as spectators, with leakage -> 0.

Formalization used for T2 (stated here so that T2 has a definite object):
a crossing of packets a and b, with a on the larger coordinate before the
crossing, acts, on the logical sector with exactly one fermion per packet,
as the restriction of the even operator

    W_ab = sum_{x,y,x',y'} V(r_ab)[(x'y'),(xy)] c+_{a x'} c+_{b y'} c_{b y} c_{a x},

which on that sector is the identity on the spectator factors (R1). The
formula is not a unitary on the whole Fock space (it annihilates states
with an empty packet); no extension outside the code is defined or
assumed. Here r_ab = e^{theta_a - theta_b}, and
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
the result is not checked: every *specified* resolution is a simulable
nearest-neighbour circuit, which is what Sec. 5 uses (a fixed
lexicographic resolution); F's map at such coincidences is defined only
once a resolution is specified. Each pair crosses at most once, so the circuit has
at most N(N-1)/2 gates.

**Sign (certified, not assumed).** For a generic symbolic 4x4 v (16
symbols), in the explicit Jordan-Wigner Fock model of three packets:

- a crossing of slots (1,2) maps the register by kron(-P v, 1), with the
  third packet behind the pair in the creation string;
- a crossing of slots (2,3) maps it by kron(1, -P v), with the first packet
  in front;
- the same holds with the packets relabelled (S2), and W_ab commutes with
  the creation operator of a third packet on the logical sector (S3).
  For any number of spectators: each term of W_ab has four operators of
  the pair, so moving a spectator creation operator past it gives
  (-1)^4 = 1.

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
  Conventions: Valiant indexes inputs by rows (a transpose relative to the
  verifier) and mentions a complemented 0/1 reading (p. 120); since
  G^T = G and (X (x) X) G (X (x) X) = G (block A = -1, B symmetric with equal
  diagonal), the character is the same numerical matrix under either
  convention.
- Second route: P V(r) = exp(+i theta(r)/2 (XX + YY)), theta(r) =
  2 atan(r) - pi/2 (cos theta = 2r/(1+r^2), sin theta = (r^2-1)/(r^2+1)),
  and with a1 = s- (x) 1, a2 = Z (x) s-, a1^+ a2 + a2^+ a1 = (XX + YY)/2: the
  gate is generated by a quadratic fermionic Hamiltonian, the
  Terhal-DiVincenzo H2 type (p. 4). The two routes agree. These are
  register fermions, not the physical modes c_{p f}.
- The user's hint exp(-i theta/2 (XX + YY)) has the opposite off-diagonal
  sign (differs by 2i sin theta, nonzero for r != 1). The repository
  convention gives the + sign. Both signs are matchgates, so the verdict
  does not depend on it.

## 5. T4: hypotheses of the theorems

**Classical input model (R2).** An instance is N, distinct rationals
K_1, ..., K_N, rationals x_1(0), ..., x_N(0) with distinct values, the
product flavour input (a bitstring), and the queried output (a subset of
packets with one assignment, or a request for one sample). Input size n =
total bit length. From it, classically:

1. *Which pairs cross, and the final order.* v_p = K_p/sqrt(1 + K_p^2) is
   increasing in K_p, so packets p, q cross iff (x_p - x_q)(K_p - K_q) > 0
   (the one on the right is faster to the left); rational comparisons.
2. *Crossing order, ties included.* t_pq = (x_p - x_q)/(v_p - v_q).
   Deciding t_pq < t_rs or t_pq = t_rs is deciding the sign of
   (x_p - x_q)(v_r - v_s) - (x_r - x_s)(v_p - v_q), a rational combination of
   at most four numbers K_i/sqrt(1 + K_i^2) = sign(K_i) sqrt(K_i^2/(1+K_i^2)).
   The sign of a rational combination of at most four square roots of
   rationals is decided exactly by a bounded number of isolate-and-square
   steps, each polynomial in the bit length (written; standard, not
   machine-checked here). Sorting the at most N(N-1)/2 crossing events
   uses O(N^2 log N) such comparisons. Coincidences of k >= 3 packets
   (equal t at one point) are resolved by a fixed lexicographic rule
   (Sec. 3).
3. *Gate parameters.* r_pq = a(K_p)/a(K_q), a(K) = sqrt(1 + K^2) + K; the
   entries beta = 2r/(1+r^2), alpha = i(r^2-1)/(r^2+1) lie in
   Q(sqrt(1+K_p^2), sqrt(1+K_q^2)) and are computable to m bits in time
   polynomial in n and m.

So the circuit (at most N(N-1)/2 gates, their slots and parameters) is
generated uniformly in time polynomial in n, exactly up to the parameter
values, which are given exactly as algebraic numbers or to any requested
precision.

| Hypothesis (source, page) | Architecture under F | Status |
| --- | --- | --- |
| Gates on bits with indices differing by one (Valiant Main Theorem (b), p. 120; T-D Thm 1, pp. 3-4; J-M Thm 1(i), p. 2) | adjacent slots of the position register (Sec. 3) | met |
| Only parity-pattern entries nonzero; matchgate realizable (Valiant Prop. 3, p. 118, B(4,4) != 0) | M1, M2 | met |
| G(A, B), A, B in SU(2) (T-D pp. 3-4) or U(2) with equal det (J-M eq. (1), p. 2) | M1 | met |
| Input: computational-basis bitstring (Valiant, T-D) / product state (J-M) | product flavour-basis bitstring | met |
| Output: probability of one queried assignment on a k-bit subset, and sampling (T-D items (2), (3), p. 4; Valiant Thm 4, p. 120; Measurement Theorem, p. 121) / single line <Z_k> (J-M pp. 2-3) | final flavour of a subset of packets | met |
| Adaptivity | none admitted (T-D cover a specific adaptive extension, Sec. V, p. 16, not needed here) | met |
| Poly-size, uniform family | above: <= N(N-1)/2 gates, generated in time poly(n) | met (written) |

Simulation notion obtained (R2):
- Valiant / Terhal-DiVincenzo: polynomial-time algorithms (Pfaffians) for
  the probability of one queried assignment on any subset, and for
  sampling, in an exact arithmetic model on the gate entries.
- Jozsa-Miyake: <Z_k> on one line to m digits in poly(N, m) time (their
  definition, p. 3, which they state their Theorem 1 achieves).
- Not re-derived here: error propagation when the algebraic gate entries
  are replaced by m-bit approximations in the subset-marginal and sampling
  algorithms (additive error of the probabilities, total-variation error
  of sampling). Claims about many-line outputs are therefore stated in
  the exact arithmetic model; the single-line m-digit claim is that of
  Jozsa-Miyake.

## 6. Scope and what is not shown

- Everything is conditional on F (multi-packet factorization), which is
  OPEN; the Fock formalization in Sec. 2 is the reading of F used.
- The logical map is the mu -> 0 limit; finite-mu corrections are not
  covered.
- Only chi = pi/2, this flavour code, these resources. For chi not
  congruent to pi/2 mod pi and r != 1, P V is not a matchgate (co-moving
  report, A5; chi = 3 pi/2 also meets the condition), and nothing here says
  whether crossings there are universal (R5).
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
the adjacency argument (written); T4 including the input model and the
square-root sign decision (written, against the sources and pages listed
in `sources/README.md`); finite-precision error propagation.

## 8. Balance

Contract closed. Coexistence stays OPEN. Under F, the crossing
architecture at chi = pi/2 in the flavour code is classically simulable
with the admitted resources in the senses of Sec. 5; an efficient
universal construction from it would imply BQP in P. No unconditional
impossibility is claimed. No further contract follows automatically.
