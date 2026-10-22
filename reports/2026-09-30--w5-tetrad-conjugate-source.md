# W5_TETRAD_CONJUGATE_SOURCE_GATE — execution

> **Typographic reconstruction — 2026-10-22.** The text recorded on 2026-09-30
> (commit `d6fd210`) lost its LaTeX backslashes through an escape layer
> (`reports/2026-10-22--escape-corruption-audit.md`). The delimiters and commands
> have been restored by hand, including two lost `\nu` in \(T_{\mu\nu}\).
> `scripts/check_reconstruction.py` certifies that only backslashes were added.
> The formulas were checked against `scripts/verify_w5_tetrad_source.py`. That
> certificate could not pass under SymPy 1.14.0 until its fix at `cb1e038`; it
> passes now. No result or scope statement has changed.

**Fecha:** 2026-09-30.  
**Contrato:** [W5_TETRAD_CONJUGATE_SOURCE_GATE](../theory/W5_TETRAD_CONJUGATE_SOURCE_GATE.md), frozen at commit `5a1e51286804c60f26aee8ccb3d07b4d1f8859f7`.  
**Certificado simbólico:** [verify_w5_tetrad_source.py](../scripts/verify_w5_tetrad_source.py), added at commit `bd91e1ae0ffd4e006b83b8ff7816cbaf6fcb5db9`.  
**Rama:** `research/gravitational-normalization-gate`.

## Verdict

```
W5_TETRAD_CONJUGATE_SOURCE_GATE =
W5_TETRAD_CONJUGATE_SOURCE_PASS / STRESS_ENERGY_CONSERVATION_OPEN

S1 = PASS
S2 = PASS
S3 = PASS
S4 = PASS
S5 = OPEN
```

W5 replaces the arbitrary endpoint-occupation source of W3 by the same local
matter operator that is variationally conjugate to the tetrad-control
variable in the matter transport Hamiltonian.

## 1. Source operator

For edge family \(a\) and edge \(e=(x,x+d_a)\),

\[
J_e^{(a)}
=
i(|x+d_a\rangle\langle x|-|x\rangle\langle x+d_a|)
\otimes\sigma_a.
\]

The transport gate is

\[
T_e(g)=e^{-igZ_e\otimes J_e^{(a)}}.
\]

For a semiclassical geometry background \(z_e=\langle Z_e\rangle\), the
matter Hamiltonian receives

\[
\delta H_m=g\,z_eJ_e^{(a)}
\]

at leading order.

Therefore

\[
\boxed{
\frac{\partial H_m}{\partial z_e}
=
gJ_e^{(a)}
}
\]

within the declared perturbative reduction.

## 2. Repaired backreaction kick

Define

\[
R_e^{(T)}(\eta)
=
e^{-i\eta Y_e\otimes J_e^{(a)}}.
\]

Because \(Y_e\) and \(J_e^{(a)}\) are Hermitian, this gate is exactly unitary
for every real \(\eta\) and remains supported only on one geometry register
and the two matter endpoints.

\[
\boxed{\texttt{S1 = PASS}.}
\]

## 3. Exact update of the tetrad-control observable

The edge current obeys

\[
(J_e^{(a)})^2=A_e,
\qquad
(J_e^{(a)})^3=J_e^{(a)},
\]

where \(A_e\) is the endpoint projector.

Hence

\[
\cos(2\eta J_e)
=
I+(\cos2\eta-1)A_e,
\]

\[
\sin(2\eta J_e)
=
\sin2\eta\,J_e.
\]

The Heisenberg transform is

\[
R_e^{(T)\dagger}Z_eR_e^{(T)}
=
Z_e\cos(2\eta J_e)
-
X_e\sin(2\eta J_e).
\]

For an initially uncorrelated geometry/matter state define

\[
x_e=\langle X_e\rangle,\qquad
z_e=\langle Z_e\rangle,
\]

\[
a_e=\langle A_e\rangle,\qquad
j_e=\langle J_e^{(a)}\rangle.
\]

Then exactly

\[
\boxed{
z_e'
=
z_e\left[1+(\cos2\eta-1)a_e\right]
-
x_e\sin2\eta\,j_e.
}
\]

Therefore

\[
\boxed{
z_e'-z_e
=
-2\eta\,x_e j_e
-2\eta^2z_ea_e
+O(\eta^3).
}
\]

The leading source is the matter current/tetrad-conjugate operator \(J_e\),
not endpoint occupation.

\[
\boxed{\texttt{S2 = PASS}.}
\]

## 4. Variational reciprocity

The matter-to-geometry source is \(j_e=\langle J_e\rangle\).

The geometry-to-matter transport coefficient satisfies

\[
\frac{\partial H_m}{\partial z_e}=gJ_e.
\]

Thus the same microscopic observable controls both directions:

\[
\boxed{
\text{geometry variation}
\leftrightarrow
J_e
\leftrightarrow
\text{geometry backreaction}.
}
\]

This is the discrete variational reciprocity missing from W3/W4.

\[
\boxed{\texttt{S3 = PASS}.}
\]

## 5. Weyl continuum interpretation

For a uniform oriented family with displacement \(d_a\),

\[
J_a(p)
=
2\sin(p\cdot d_a)\sigma_a.
\]

Near the Weyl node,

\[
\boxed{
J_a(p)
=
2d_a{}^i p_i\,\sigma_a
+
O(|p|^3).
}
\]

The matter Hamiltonian has the form

\[
H_m
=
-\sigma^a E_a{}^i p_i+\cdots
\]

under the convention inherited from the CJWW symbol. Variation with respect
to a spatial tetrad coefficient produces an operator proportional to

\[
\sigma^a p_i.
\]

Thus the W5 source is a directional lattice representative of the operator
conjugate to the spatial tetrad.

It is therefore legitimate within this gate to call \(J_e\) a

\[
\boxed{\text{tetrad-conjugate stress source}}
\]

in the continuum/variational sense.

This is deliberately weaker than identifying it with the complete
stress-energy tensor.

\[
\boxed{\texttt{S4 = PASS}.}
\]

## 6. Conservation and symmetry remain open

The present project has not derived:

- a discrete local time-translation symmetry yielding a local energy
  continuity law for the full Floquet matter+geometry system;
- a discrete diffeomorphism identity;
- a local Lorentz Ward identity;
- a conserved symmetric \(T_{\mu\nu}\);
- the time-time and mixed components required for a complete 3+1
  stress-energy tensor.

The flat CJWW translation invariance and unitary quasienergy spectrum do not
by themselves provide those identities once the geometry is dynamical.

Therefore the project must not rename \(J_e\) as \(T_{\mu\nu}\).

\[
\boxed{\texttt{S5 = OPEN}.}
\]

## 7. Relation to W4

Combining W4 and W5 now gives the following toy-model chain:

\[
\text{tetrad-conjugate matter source}
\longrightarrow
z_e
\longrightarrow
E_a{}^i
\longrightarrow
h^{ij},
\]

while

\[
z_e
\longrightarrow
K_\kappa
\longrightarrow
\text{autonomous vacuum propagation of geometry}.
\]

This is materially stronger than the W3 endpoint-occupation source.

## 8. What is still missing before Einstein structure

The remaining obstruction is now symmetry/conservation rather than mere
backreaction:

1. identify a complete coarse spacetime tetrad, including temporal/lapse/shift
   structure or a controlled gauge-fixed equivalent;
2. derive the relevant discrete/continuum Ward identities;
3. show that the matter source entering geometry dynamics is the conserved
   stress-energy object required by those identities;
4. identify the geometry mode content and determine whether a massless spin-2
   sector exists.

Only after those steps would comparison with a linearized Einstein equation be
meaningful.

## 9. Terminal decision

S1-S4 pass; S5 is not established.

Therefore

\[
\boxed{
\texttt{W5\_TETRAD\_CONJUGATE\_SOURCE\_PASS /
STRESS\_ENERGY\_CONSERVATION\_OPEN}
}
\]

is the terminal state.

## Review repairs — 2026-10-22

Independent sealed reviews (Astra, DeepSeek): **ACCEPT_WITH_REPAIRS**
([author verification](../debates/2026-10-22--w3-w6-review-astra/verificacion_autor.md)).
The text above is kept; these repairs restrict it where they conflict.

1. δH_m=g z J and ∂H_m/∂z=gJ are leading-order semiclassical relations for the transport generator in a background ⟨Z⟩, not a full effective Hamiltonian.
2. S2 is exact for product (uncorrelated) inputs. Reciprocity is a first-step/mean-field statement, not a closed dynamical equation after entanglement.
3. "Tetrad-conjugate stress source" means only the demonstrated directional variational relation. The certificate checks one scalar symbol, not J_a(p) for a=1,2,3 or the variational derivative.

Evidence: REVIEWED_ACCEPT_WITH_REPAIRS (two independent reviews), repaired scope as above.
Pending certificate obligations are recorded in the author verification.
