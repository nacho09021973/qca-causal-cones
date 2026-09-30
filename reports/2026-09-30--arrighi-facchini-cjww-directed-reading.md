# Directed reading: Arrighi–Facchini Paired QWs versus exact CJWW (5.15)

**Fecha:** 2026-09-30.  
**Tipo:** literature/preflight report, not a scientific gate.  
**Rama:** \`research/gravitational-normalization-gate\`.

## Question

Can the published Paired-QW construction of Arrighi and Facchini,
*Quantum walking in curved spacetime: (3+1) dimensions, and beyond*,
be used as an **exact flat bridge** for the frozen two-component CJWW
Eq. (5.15) walk, so that their published metric/tetrad prescription could
then deform CJWW without inventing a new elastic hopping rule?

## Primary source

P. Arrighi and S. Facchini, *Quantum Information and Computation* 17
(2017) 810–824, arXiv:1609.00305.

The reading used the journal text, especially Sections 2–7 and Eqs.
(16), (35), (36), together with the exact CJWW \`walk2()\` symbol already
frozen in this repository.

## 1. What the paper actually proves

The Paired-QW construction uses grouping and a local encoding. In one spatial
dimension the physical internal degree of freedom is \(2s\), while the grouped
local encoding/coin acts on \(4s\) components. The authors derive the
continuum class

\[
\partial_t\psi
=
B_1\partial_x\psi
+\frac12(\partial_xB_1)\psi
+iC\psi,
\]

with \(B_1,C\) Hermitian and the eigenvalues of \(B_1\) bounded by one.

Given \(B_1\) and \(C\), they explicitly solve for the zeroth-order encoding
and coin and then for the first-order correction. Their recap states that the
coin and encoding can be worked out from the target continuum matrices.

For higher spatial dimension the construction is **operator split**. For
each coordinate \(x_i\) there is a directional Paired QW \(U^{(i)}\), and one
full discrete update is

\[
\boxed{
U=\prod_i U^{(i)}.
}
\]

Each flat translation-invariant directional subwalk shifts only along its own
coordinate, so its Bloch symbol depends only on \(p_i\).

The continuum Hamiltonian is correspondingly the sum

\[
H=\sum_i H^{(i)}.
\]

For curved \(3+1\) Dirac they identify the \(B_1^{(i)}\) matrices from the
tetrad and put the mass/spin-connection terms in \(C\). They state that these
equations allow the QW parameters associated with a given bounded metric to
be found.

The paper later gives a lower-local-dimension implementation, using
\(U(2s)\) gates with partial shifts/swaps. It remains an operator-split
directional construction.

## 2. What the paper does not prove

The paper does **not** prove that an arbitrary pre-existing flat QW can be
embedded exactly into this family while preserving its one-step unitary.

In particular it does not:

- mention CJWW Eq. (5.15);
- prove exact equality with the Cedzich–Joye–Werner–Werner walk;
- prove local-unitary equivalence to that walk;
- preserve a specified arbitrary flat Bloch symbol as the zero-curvature
  member of the retro-engineered family;
- analyze the four \(+I\) species of CJWW;
- provide graph dynamics or matter-to-geometry backreaction.

Its main guarantee is a **continuum-limit guarantee** from a target PDE to a
newly constructed Paired QW.

## 3. Internal dimension is not the obstruction

The general theorem allows arbitrary even physical internal dimension \(2s\).
Choosing \(s=1\) gives a two-component physical field.

Therefore there is no immediate dimension-count obstruction to simulating a
two-component Weyl PDE.

The worked curved \(3+1\) Dirac example uses four-component Dirac matrices,
but the general Paired-QW continuum class itself is not restricted to four
components.

## 4. Exact flat-bridge necessary condition

In the homogeneous flat case, Eq. (36) plus the higher-dimensional operator
splitting imply a Bloch factorization of the form

\[
U_{\rm AF}(p_1,p_2,p_3)
=
U_1(p_1)U_2(p_2)U_3(p_3)
\]

in some fixed order, up to constant encoding/decoding conjugations.

A necessary condition for a factorization

\[
W(p)=A(p_i)B(p_j)C(p_k)
\]

is that, for the leftmost coordinate \(p_i\),

\[
(\partial_{p_i}W)W^{-1}
=
A'(p_i)A(p_i)^{-1}
\]

depend **only** on \(p_i\).

This condition is invariant under constant on-site conjugation.

## 5. CJWW (5.15) fails that necessary condition

For the frozen exact symbol

\[
W_2(p)=
\begin{pmatrix}
c_1c_2e^{ip_3}&-c_1s_2+i s_1\\
c_1s_2+i s_1&c_1c_2e^{-ip_3}
\end{pmatrix},
\]

direct exact differentiation gives, for example,

\[
(\partial_{p_1}W_2)W_2^{-1}
=
i
\begin{pmatrix}
-\sin p_2 & e^{ip_3}\cos p_2\\
e^{-ip_3}\cos p_2 & \sin p_2
\end{pmatrix}.
\]

It depends on both \(p_2\) and \(p_3\), so \(p_1\) cannot be the leftmost
single-coordinate factor.

The analogous exact matrices for \(p_2\) and \(p_3\) also depend on other
momenta. Therefore **no coordinate can be leftmost**.

Hence CJWW (5.15) cannot be written, in any permutation, as

\[
\boxed{
W_2(p)
=
U_{i}(p_i)U_j(p_j)U_k(p_k)
}
\]

with each factor depending on only one coordinate.

Constant local-unitary conjugation does not cure this obstruction.

## 6. Consequence for the standard Arrighi–Facchini architecture

The direct flat bridge

\[
\text{Arrighi–Facchini standard operator split}
\stackrel{?}{=}
\text{CJWW (5.15)}
\]

fails the necessary coordinate-factorization condition.

Thus the source is a valid **continuum curved-Dirac/Weyl construction
template**, but it is not an exact one-step deformation prescription for the
frozen CJWW (5.15) walk.

This is stronger than merely saying “the paper does not discuss CJWW”: the
standard flat architecture has a structural property that the exact CJWW
symbol lacks.

## 7. Caveats not settled by this reading

This report does not exclude all conceivable uses of Paired QWs.

It does not test:

- changing the microscopic time unit and matching one Paired-QW step to
  \(W_2^m\), \(m>1\);
- enlarging the unit cell/supercell and comparing a grouped CJWW symbol;
- adding ancillas and seeking a dilation rather than equality on the original
  two-component cell;
- abandoning the standard directional operator splitting;
- changing the flat matter walk from CJWW (5.15) to another Weyl walk.

Each of those changes the bridge quantifiers and would require independent
physical justification and a separately frozen contract.

In particular, time blocking or supercell enlargement must not be introduced
merely to evade the factorization obstruction found here.

## 8. Relation to CJWW (5.12)

The source's directional operator-splitting architecture is structurally much
closer to product-form Weyl walks such as CJWW Eq. (5.12),

\[
e^{ip_1\sigma_1}e^{ip_2\sigma_2}e^{ip_3\sigma_3},
\]

than to Eq. (5.15).

This is an architectural observation only. It does not authorize changing the
frozen matter model from (5.15).

## 9. Preflight verdict

\`\`\`
ARRIGHI_FACCHINI_DIRECTED_READING = COMPLETE

CONTINUUM_CURVED_WEYL/DIRAC_TEMPLATE = YES
TWO_COMPONENT_CONTINUUM_WEYL_COMPATIBILITY = YES
EXACT_ONE_STEP_CJWW_5_15_FLAT_BRIDGE =
  STRUCTURALLY_BLOCKED_IN_STANDARD_OPERATOR_SPLIT

SUPER_CELL / TIME_BLOCKED / ANCILLA BRIDGES = NOT TESTED
\`\`\`

This is a literature/preflight result, not a promoted scientific gate.

## 10. Recommendation

Do not freeze a positive
\`CJWW_TO_PAIRED_QW_FLAT_BRIDGE_GATE\` under the standard Arrighi–Facchini
operator-split architecture: its necessary flat factorization is already
incompatible with the exact CJWW (5.15) symbol.

If formal repository closure is desired, the next legitimate gate would be a
small **factorization no-go gate** that freezes the exact quantifiers
(one CJWW tick, original \(\mathbb C^2\) cell, constant local conjugation
allowed, no supercell/ancilla) and certifies the obstruction.

A constructive successor would need a genuinely different published
architecture, or an independently justified change of quantifiers.
