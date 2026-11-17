# S4 family against Arrighi-Facchini: regrouping / encoding identification

2026-11-17. Author: Claude Code (Claude Opus 5.5). Initial status
**OPEN / NOT EXECUTED**. User «push y redacta el contrato de la
reagrupación» (2026-11-17) authorized drafting; user «autorizo que
congeles» (2026-11-17) authorizes freezing by this commit. Execution needs
a separate user authorization. One contract; no
review, promotion or publication follows from it.

## Known, question, abandonment

Known (read in this or earlier sessions, with source):
- Family: `theory/S4_STRICT_CONE_COUNTEREXAMPLE.md` (`1dae941`), Secs. 2-5:
  C^4 = C^2_sigma ⊗ C^2_tau, 0<a<1, theta = pi/4, Fourier coefficients
  A_{h_s} = W P_x^{s_x} P_y^{s_y} P_z^{s_z} on exactly the eight BCC
  displacements, no on-site coefficient; A(0) = W with quasienergies
  ±pi/4, each a rank-two cluster; c_0 = a/sqrt3; C_infty^strict = C_micro
  (`CURRENT_STATE.md` Sec. 4.1, COUNTEREXAMPLE_VERIFIED). Isotropic in the
  sense of 1708.00826 (Sec. 4.1, promoted 2026-11-17, `c881b8c`).
- Arrighi-Facchini (AF), arXiv:1609.00305v2, `sources/1609.00305v2.pdf`,
  read 2026-11-02 (`reports/2026-11-02--s4-family-vs-arrighi-facchini.md`):
  speed set by compressing a traceless Hermitian unitary B (Eqs. (18a),
  (27)-(29)); (3+1) dynamics by operator splitting U = prod_i U^(i) of
  paired 1D walks with decoding/re-encoding (Sec. IV, Eq. (36) ff.);
  grouped field C^{4s}, continuum field C^{2s}; zeroth order
  E^(0)† W^(0) X E^(0) = I_2s ⊕ U (Eq. (16)); coins and encodings analytic
  in eps and spacetime dependent (Eqs. (9)-(10)). The 2026-11-02 report
  found no identification "as written" and did not attempt a regrouping
  or encoding search; it lists differences in step set (grouped ±2 shifts
  vs. eight BCC displacements) and node (U ≈ I at zeroth order vs.
  A(0) = W not a phase).
- `CURRENT_STATE.md` Sec. 4 table (user decision 2026-11-17, `beb1fb2`):
  the family is a candidate with restricted claim; AF is a mandatory
  structural antecedent; the regrouping check is a listed prerequisite.

Question: is there a homogeneous (constant-coin, constant-encoding, fixed
eps > 0) specialization of AF's (3+1) construction that is equivalent to
the s=4 family at theta = pi/4 for some 0<a<1, under the equivalences
declared below?

Abandonment of the line (the restricted novelty candidacy): if such an
equivalence is exhibited and verified exactly, the family is a
specialization of AF; record it as prior art and drop the candidacy.
If an invariant of the declared equivalence class separates the two for
every admissible AF parameter, the candidacy continues (AF remains a
structural antecedent). A missing decision yields OPEN, not either.

## Fixed objects (no change after freezing)

- Family: as above, theta = pi/4, a symbolic in (0,1).
- AF class: the homogeneous specialization of AF Sec. IV in d = 3, i.e.
  every coin W^(i), encoding E^(i) and pre-encoding of AF Eqs. (4)-(5),
  (9)-(10), (36) and following, taken constant in space and time, at a
  fixed eps > 0 (all eps > 0 admitted), with the internal dimension s of
  AF's construction chosen so that the grouped field is C^4 or a multiple
  admitting a C^4 reduction under (E4). Step 0 below writes this class
  explicitly from the PDF before any comparison; if the paper does not
  determine it uniquely, the ambiguity is recorded and each reading is
  treated as a separate subclass.
- Declared equivalences, and only these:
  (E1) conjugation by a constant unitary; (E2) global phase;
  (E3) orthogonal relabeling of the lattice compatible with the step sets;
  (E4) regrouping of cells by a finite-index sublattice (coarse-graining,
  as in 1511.03992 Sec. IV) and its inverse; (E5) regrouping of time
  steps, U -> U^n for a fixed n ≥ 1, on either side; (E6) encoding by a
  constant isometry between internal spaces, applied before and undone
  after, as AF's pre-encoding. Momentum-dependent basis changes are not
  admitted.

## Tasks

- Step 0 (source). From `sources/1609.00305v2.pdf`, write the AF
  homogeneous (3+1) one-step symbol U_AF(k; eps, parameters) explicitly,
  with its exact Fourier support and internal dimension, citing equation
  numbers. No computation before this text is written into the report.
- Step 1 (invariants). Define, prove invariance under (E1)-(E6) and
  compute exactly, for both objects, a finite list of invariants chosen
  before computing. Candidates: (i) the asymptotic strict support body of
  U^n / n, normalized for (E4)-(E5); (ii) the number of bands per
  fundamental cell after normalization; (iii) the quasienergy structure
  at the gapless node modulo (E2) and (E5) (e.g. cluster ranks and
  differences); (iv) the dimension of the commutant (irreducibility).
- Step 2 (decision). Either exhibit an explicit equivalence (maps and
  parameters) and verify the identity of symbols exactly, or show that a
  Step-1 invariant differs for every admissible AF parameter.
Exact SymPy only; one permanent verifier committed before running; no
numerical search substitutes for a proof of non-equivalence. Reviewed
verifiers are imported read-only if needed. Budget: one session; stop at
OPEN_AFTER_REGROUPING_ATTEMPT if Step 2 is not decided.

## Verdicts

- `AF_EQUIVALENT_IN_DECLARED_CLASS`: explicit equivalence verified.
- `AF_NOT_EQUIVALENT_IN_DECLARED_CLASS`: an invariant separates them for
  every admissible AF parameter (per subclass if Step 0 splits the class).
- `OPEN_AFTER_REGROUPING_ATTEMPT`: neither established within budget.
Author results PRELIMINARY until an independent review.

## Not claimed under any verdict

Non-equivalence under equivalences not declared (momentum-dependent
changes, inhomogeneous or eps-dependent maps, other papers' schemes);
anything about AF's inhomogeneous or continuum-limit setting; novelty
(a non-equivalence only removes one candidate antecedent). NOVELTY = OPEN.
