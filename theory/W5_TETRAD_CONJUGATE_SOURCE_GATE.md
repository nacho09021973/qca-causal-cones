# W5_TETRAD_CONJUGATE_SOURCE_GATE

> **Typographic reconstruction — 2026-10-22.** The frozen text is commit `5a1e512`.
> It lost its LaTeX backslashes through an escape layer
> (`reports/2026-10-22--escape-corruption-audit.md`). The delimiters and commands
> have been restored by hand, including a lost `\nu` in \(T_{\mu\nu}\).
> `scripts/check_reconstruction.py` certifies that only backslashes were added.
> The formulas were checked against `scripts/verify_w5_tetrad_source.py`. The
> contract remains the version frozen at `5a1e512`.

**Fecha:** 2026-09-30.  
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`.  
**Rama:** `research/gravitational-normalization-gate`.

## 0. Input

Successor to:

```
W3_BACKREACTING_TETRAD_PASS
W4_AUTONOMOUS_GEOMETRY_DYNAMICS_PASS / GRAVITATIONAL_SOURCE_OPEN
```

The remaining W3/W4 source defect is that the geometry kick was driven by
endpoint occupation \(A_e\), not by a source derived from variation of the
matter dynamics with respect to the tetrad-control variable.

## 1. Frozen transport operator

For edge family \(a\) and oriented edge \(e=(x,x+d_a)\), retain

\[
J_e^{(a)}
=
i(|x+d_a\rangle\langle x|-|x\rangle\langle x+d_a|)
\otimes\sigma_a.
\]

The transport/tetrad gate remains

\[
T_e(g)=e^{-igZ_e\otimes J_e^{(a)}}.
\]

For a semiclassical background \(z_e=\langle Z_e\rangle\), the matter
Hamiltonian contribution is, to leading order,

\[
\delta H_m=g\,z_eJ_e^{(a)}.
\]

Thus the operator conjugate to \(z_e\) is

\[
\frac{\partial H_m}{\partial z_e}=gJ_e^{(a)}
\]

at the declared perturbative level.

## 2. Source repair

Replace only the W3 backreaction kick by

\[
R_e^{(T)}(\eta)
=
e^{-i\eta Y_e\otimes J_e^{(a)}}.
\]

The W4 geometry-only stiffness step is retained unchanged.

The couplings \(g\) and \(\eta\) remain independent dimensionless parameters;
no gravitational normalization is assumed.

## 3. Obligations

### S1 — exact local unitarity

\(R_e^{(T)}\) must be exactly unitary and bounded-range.

### S2 — source changes tetrad control

For an initially uncorrelated geometry/matter state derive the update of

\[
z_e=\langle Z_e\rangle.
\]

PASS requires a leading term proportional to

\[
j_e=\langle J_e^{(a)}\rangle.
\]

### S3 — variational reciprocity

The source appearing in the geometry update must be the same matter operator
that satisfies

\[
\partial H_m/\partial z_e=gJ_e^{(a)}
\]

in the transport sector.

### S4 — Weyl continuum interpretation

Show that the Fourier symbol of the summed current family is

\[
J_a(p)=2\sin(p\cdot d_a)\sigma_a
=
2d_a{}^i p_i\sigma_a+O(|p|^3).
\]

Therefore, in the Weyl continuum limit, the source is a directional
contraction of the operator conjugate to the spatial tetrad coefficient
\(e_a{}^i\).

This may be called a **tetrad-conjugate stress source**, not yet the full
stress-energy tensor.

### S5 — conservation/symmetry ceiling

A PASS requires an independent discrete conservation/gauge identity before
calling the source \(T_{\mu\nu}\).

If no such identity is present, record

`TETRAD_CONJUGATE_SOURCE_PASS / STRESS_ENERGY_CONSERVATION_OPEN`.

Do not manufacture a local energy density from Floquet quasienergy.

## 4. Terminal states

1. `W5_SOURCE_REPAIR_FAIL`.
2. `W5_TETRAD_CONJUGATE_SOURCE_PASS / STRESS_ENERGY_CONSERVATION_OPEN`.
3. `W5_STRESS_ENERGY_SOURCE_PASS`.
4. `OPEN_AFTER_AUDIT`.

## 5. Claim ceiling

Passing S1-S4 alone does not establish Einstein coupling. The continuum
variational relation between tetrads and fermionic stress-energy is the
motivation for the test, but the project must separately establish the
relevant conservation/symmetry structure of its own discrete model.
