# S4 family against Arrighi-Facchini: regrouping attempt — execution

2026-11-17. Author: Claude Code (Claude Opus 5.5). Contract
`theory/S4_AF_REGROUPING_GATE.md`, preregistration `098cb33`. User «push
y autorizo ejecucion». Branch `research/thirring-isolated-spectator`.
Author verdict: **`OPEN_AFTER_REGROUPING_ATTEMPT`**. No computation was
run, so no verifier was written; everything below is reading of the
source and short algebra stated in the text. PRELIMINARY, unreviewed.

## Step 0 — the homogeneous AF class, from the PDF

Source `sources/1609.00305v2.pdf` (read 2026-11-17, Secs. II-IV, PDF
pp. 2-5).

1D Paired QW (Sec. II, p. 2). The field is psi(t,x) in C^s ⊕ C^s = C^{2s}
on Z. Pairs psi(t,x-1) ⊕ psi(t,x+1) are grouped into phi(t,x), x in 2Z,
and encoded by a unitary E, phi' = E phi. A coin W' on C^{4s} takes the
upper 2s components of phi'(t,x-2) and the lower 2s of phi'(t,x+2) to
produce phi'(t+2,x); "this Paired QW ... phrased in terms of phi' and
s' = 2s is therefore but a subcase of the usual QW definition" (p. 2).
Encodings and decodings cancel between steps (Fig. 3). Eq. (5)-(6):
phi(t+2,x) = G(phi(t,x-2) ⊕ phi(t,x+2)),
G = E†(t+2,x) W'(t,x) (P' ⊕ P)(E(t,x-2) ⊕ E(t,x+2)).

Homogeneous specialization (constant W', E; fixed eps). In the grouped,
encoded description it is a usual QW on the lattice 2Z with internal space
C^{4s} and two displacements ±2 (one grouped site):
U_1D(k) = W' · (e^{-2ik} Π_up + e^{+2ik} Π_down) (up to the convention of
which block moves which way), Π_up, Π_down the projectors on the two 2s
blocks. On the ungrouped field psi, by Eq. (6) an output psi(x∓1) depends
on psi(x-3), psi(x-1), psi(x+1), psi(x+3): support {-4,-2,0,2,4} per
paired step, period 2 along the axis, and only one of the two parity
sublattices is involved (the other evolves independently, Fig. 1).

(3+1) by operator splitting (Sec. IV, p. 5, Eq. (36)):
G^(i) = E†^(i)(x0+2) W^(i) (P' ⊕ P)(E^(i)(x_i-2) ⊕ E^(i)(x_i+2)), with the
Hadamard pre-encoding of Eq. (4) included in E^(i) and performed along
x_i; U^(i) on l^2(Z^n) ⊗ C^{2s}, U^(i) ≈ I - 2i eps H^(i), and
psi(x0+2) = prod_i U^(i) psi, "decoding and re-encoding between each
sub-step". Homogeneous specialization: each U^(i) is translation invariant
by 2 e_i and by e_j (j ≠ i); the product is invariant under 2Z^3, with
16s components per 2Z^3 cell on psi.

Readings that the paper leaves open (recorded, per contract): the
direction convention of the ±2 shifts; whether the two parity sublattices
per axis are both evolved or one is discarded; and whether a fixed eps > 0
walk is meant to satisfy the zeroth-order condition Eq. (16),
E^(0)† W^(0) X E^(0) = I_2s ⊕ U, exactly (it is a condition on the eps -> 0
expansion, not on a fixed-eps walk). Each reading would be a subclass.

Dimension count: with s = 2 the AF continuum field is C^4, as the family;
the family regrouped on an index-8 sublattice of its BCC lattice has 32
components, as the AF walk on a 2Z^3 cell (16s = 32). Dimensions do not
separate the two.

## Step 1 — invariants considered (chosen before any calculation)

(i) Asymptotic strict support body of U^n/n, up to the scale fixed by
(E4)-(E5). Family: the cube conv{h_s} (C_infty^strict = C_micro, Sec. 4.1).
AF homogeneous: each U^(i) moves along e_i only, the product has an axis-
aligned cube as support hull. Both are cubes, so the shape does not
separate them; whether the AF strict body is the whole cube (vertex
coefficients non-nilpotent) was not checked.

(ii) Bands per fundamental cell after normalization: equal (32) for s = 2,
as above. Does not separate.

(iii) Quasienergy structure at the node modulo (E2), (E5). Family:
A(0) = W = I ⊗ exp(-i pi tau_z/4), quasienergies ±pi/4, two rank-two
clusters. But W^4 = I ⊗ exp(-i pi tau_z) = -I, so under (E5) with n = 4
and (E2) the family's node becomes a single rank-four cluster at 0, like
AF's U ≈ I at zeroth order. Under the declared class this invariant does
not separate them either.

(iv) Commutant of the Fourier coefficients (irreducibility). Not
computed. Its behaviour under (E4) (regrouping turns sublattice
translations into internal operators) was not worked out, so it is not
yet a usable invariant.

## Structural observation (not a decision)

Both objects are operator-splitting products of three axis-wise factors.
The family is W e^{-iq_xGamma_x} e^{-iq_yGamma_y} e^{-iq_zGamma_z}; each
factor is a pure conditional shift (Gamma_i an involution with two rank-two
eigenspaces), and the low-energy speed is the compression
P_+ Gamma_i P_+ = a sigma_i P_+ onto an eigenspace of W
(`theory/S4_STRICT_CONE_COUNTEREXAMPLE.md`). That is AF's mechanism
(speed from compressing a traceless Hermitian unitary B, Eqs. (18a),
(27)-(29)), already recorded on 2026-09-15 and 2026-11-02. The differences
that remain are structural, not yet invariants: the family has no
grouping, no encoding, and a single coin W per step outside the three
factors, with each factor a coinless shift of length one; AF has a coin
per axis, a pairing to ±2 shifts, and decoding/re-encoding between axes.
Neither an explicit equivalence nor an invariant separating them for
every admissible AF parameter was obtained.

## Verdict and what a successor would need

`OPEN_AFTER_REGROUPING_ATTEMPT`. The contract's budget (one session) ends
here. A successor contract would need to:
1. fix one reading of the homogeneous AF class (the three open points of
   Step 0) and write U_AF(k) explicitly as a matrix symbol;
2. either construct an explicit map (e.g. realize each coinless factor
   e^{-iq Gamma_i}, paired by (E4), as an AF paired step with W' = I and a
   suitable E, and absorb W into the encodings), or
3. find an invariant robust under (E5) with (E2): candidates are the
   number of Weyl nodes in the folded Brillouin zone counted without time
   regrouping, or the commutant dimension after (E4).
Until then the candidacy status is unchanged (`CURRENT_STATE.md` Sec. 4
table): AF is a structural antecedent; whether the family is a
specialization of AF is OPEN. NOVELTY = OPEN.
