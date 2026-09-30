# F9 Pretko rank-2 tensor gauge preflight

Date: 2026-09-30.

## 1. Question

Can Pretko-type rank-2 tensor gauge theories be treated as a separate atlas
family after Gu-Wen, and what is their admissible status for the CJWW
matter-gravity programme?

This is a source preflight. It does not construct a QCA, add a CJWW matter
sector, or run a four-species metric test.

## 2. Primary sources read

Primary local PDFs:

```text
biblioteca/arXiv-1606.08857.pdf
biblioteca/arXiv-1702.07613.pdf
```

Read pages:

- `arXiv-1606.08857.pdf` pp.1-8.
- `arXiv-1702.07613.pdf` pp.1-6.

## 3. Source facts retained

Pretko 1606.08857 reviews symmetric rank-2 compact U(1) tensor gauge theories.
Pp.1-3 classify four rank-2 spin-liquid phases by Gauss law, mobility,
dispersion and number of gauge polarizations.

The relevant table on p.3 records:

- scalar charge: `partial_i partial_j E^ij = rho`, linear dispersion, five
  polarizations;
- traceless scalar charge: scalar Gauss law plus `E^i_i=0`, linear
  dispersion, four polarizations;
- vector charge: `partial_i E^ij = rho^j`, quadratic dispersion, three
  polarizations;
- traceless vector charge: vector Gauss law plus `E^i_i=0`, cubic dispersion,
  two polarizations.

Pretko 1702.07613 reads the scalar-charge rank-2 toy model as an emergent
gravity/fracton analogue. Pp.3-5 state the toy Gauss law
`partial_i partial_j E^ij = rho`, the gauge transformation
`A_ij -> A_ij + partial_i partial_j alpha`, and compare the scalar constraint
to the `00` component of linearized Einstein gravity. The same read section
also states the analogy is simplified: the toy model has energy-like scalar
charge but not the full energy/momentum structure of gravity.

## 4. Relation to existing in-repo records

The W8 prior-art correction already uses Pretko to cap novelty for rank-2
Gauss-law and 5-to-2 tensor-gauge mode counting:

```text
reports/2026-09-30--w8-prior-art-gauge-audit.md
```

The W8 TT gauge-completion audit proves a kinematic 5-to-2 quotient for the
project's W7 tensor variables, but leaves microscopic gauge embedding open.
Pretko supplies structural prior art for such constraint/gauge language; it
does not supply the missing CJWW microscopic gauge embedding.

## 5. Kill tests for atlas status

### F9.1 — independent identity

Is this distinct from Gu-Wen F8?

Result: PASS. Gu-Wen is a qubit/spin graviton-sector construction. Pretko is
a broader rank-2 tensor-gauge/fracton language organized by Gauss laws,
mobility restrictions and dispersion.

### F9.2 — direct CJWW/QW rule

Does either source provide a two-component CJWW walk, QCA update, or exact
flat matter sector?

Result: FAIL. The sources are continuum/effective tensor-gauge and spin-liquid
architectures, not CJWW/QW constructions.

### F9.3 — physical graviton match

Does the read material by itself give Einstein gravity coupled to CJWW matter?

Result: FAIL. Pretko 1702.07613 is explicitly a toy rank-2 model with an
analogy to gravity and an energy-like scalar charge, not the full coupled
Einstein-Weyl system.

### F9.4 — novelty ceiling

Can the project claim novelty for rank-2 Gauss-law constraints or 5-to-2
tensor-gauge polarization reduction?

Result: FAIL. Pretko is direct prior art for that structure.

## 6. Verdict

```text
F9_PRETKO_TENSOR_GAUGE_PREFLIGHT =
RANK2_GAUSS_LAW_PRIOR_ART /
DIRECT_CJWW_QCA_BRIDGE_ABSENT
```

Evidence level: primary-source preflight plus existing in-repo W8 records. No
new independent review.

## 7. Consequence

F9 is useful as a dictionary and claim ceiling:

1. it names the possible rank-2 Gauss-law architectures;
2. it separates scalar/vector charge and trace/traceless variants;
3. it records which variants have two polarizations or linear dispersion;
4. it warns that those virtues do not by themselves produce CJWW matter,
   source matching, reciprocal backreaction, or an exact QCA update.

Any future use of F9 as a constructive family needs a new contract specifying
which Gauss-law sector is chosen and how CJWW matter couples to it locally.
