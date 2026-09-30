# ELASTIC_HOPPING_UNITARY_RESPONSE_GATE — execution

**Fecha:** 2026-09-30.  
**Contrato:** [ELASTIC_HOPPING_UNITARY_RESPONSE_GATE](../theory/ELASTIC_HOPPING_UNITARY_RESPONSE_GATE.md), frozen at commit \`15bc76bf052f3ea0988dd36f3f5bde5d02d6695e\`.  
**Certificado exacto:** [verify_elastic_hopping_orientation_obstruction.py](../scripts/verify_elastic_hopping_orientation_obstruction.py), added at commit \`f08b8847866662f669336352e8e9dbb04336babb\`.  
**Rama:** \`research/gravitational-normalization-gate\`.

## Verdict

\`\`\`
ELASTIC_HOPPING_UNITARY_RESPONSE_GATE =
UNITARY_ELASTIC_RESPONSE_INCONSISTENT

H0 = NOT_REACHED
H1 = FAIL_AT_MODEL_DEFINITION
H2-H5 = NOT_EXECUTED
FOUR_SPECIES_KILL_TEST = NOT_EXECUTED
\`\`\`

The gate fails before any species calculation because the frozen
bond-generator rule is not independent of the arbitrary orientation set
\(F_+\).

## 1. Frozen premise that fails

The contract defined

\[
K_u(p)
=
\sum_{h\in F_+}
\rho_h(u)
\left(
e^{ip\cdot h}W_h
+
e^{-ip\cdot h}W_h^\dagger
\right)
\]

and stated that the result should not depend on choosing \(h\) or \(-h\)
as the representative of the undirected bond.

That would require, for the CJWW Fourier blocks,

\[
W_{-h}=W_h^\dagger
\]

or an equivalent identity making the two representative choices coincide.

The exact CJWW (5.15) blocks do not satisfy this.

## 2. Exact obstruction

The certified 14-vector support consists of seven opposite pairs.

For example,

\[
W_{(1,0,0)}
=
\begin{pmatrix}
0&1/2\\
1/2&0
\end{pmatrix},
\]

whereas

\[
W_{(-1,0,0)}
=
\begin{pmatrix}
0&-1/2\\
-1/2&0
\end{pmatrix}
\ne
W_{(1,0,0)}^\dagger.
\]

Likewise, at a corner,

\[
W_{(1,1,1)}
=
\begin{pmatrix}
1/4&0\\
0&0
\end{pmatrix},
\]

while

\[
W_{(-1,-1,-1)}
=
\begin{pmatrix}
0&0\\
0&1/4
\end{pmatrix}.
\]

The obstruction is therefore not a numerical accident.

## 3. Two admissible orientation choices give different generators

Use the isotropic control \(u=I\), so

\[
\rho_h(I)=1
\]

for every bond, and evaluate at \(p=0\).

Two equally admissible orientation sets under the frozen text are

\[
F_+^{(+)}=\{h\in F:h_1=+1\},
\]

and

\[
F_+^{(-)}=\{h\in F:h_1=-1\}.
\]

The exact certificate gives

\[
K^{(+)}(0)
=
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\]

whereas

\[
K^{(-)}(0)
=
\begin{pmatrix}
1&-1\\
-1&1
\end{pmatrix}.
\]

Therefore

\[
\boxed{
K^{(+)}(0)\ne K^{(-)}(0).
}
\]

So the microscopic elastic response is not fixed by the physical undirected
bond strain alone; it still depends on an arbitrary directed representative.

## 4. Why this is a terminal failure

The gate's H5 rule forbids changing the orientation convention after
execution begins.

More importantly, merely fixing \(h_1=+1\) now would not repair the physical
problem: it would promote an arbitrary lattice orientation convention into
part of the elastic law without independent justification.

The model is therefore underdetermined at the point where the contract
claimed a species-blind bond response.

By the frozen terminal ordering,

\[
\boxed{
\texttt{UNITARY\_ELASTIC\_RESPONSE\_INCONSISTENT}
}
\]

must be taken before H2/H3.

No four-node metric calculation is performed.

## 5. What remains valid

The predecessor result is unchanged:

\[
\boxed{
\texttt{KINEMATIC\_COMMON\_EMBEDDING\_UNIVERSAL /
ELASTIC\_HOPPING\_RESPONSE\_OPEN}
}
\]

with

\[
h_*^{(\Lambda)}=a^2\Lambda\Lambda^T
\]

for all four decisive species and metric rank \(6/6\).

Likewise W12 remains unchanged and negative for the W6 Pauli-selective
control class.

## 6. Non-executed possible successor

There is an obvious orientation-independent mathematical repair:

start from the full bond-weighted CJWW symbol

\[
R_u(p)
=
\sum_{h\in F}
\rho_h(u)e^{ip\cdot h}W_h
\]

and take its Hermitian part,

\[
K_u^{\rm sym}(p)
=
\frac12\left(R_u(p)+R_u(p)^\dagger\right).
\]

This uses every directed CJWW hop exactly once and is Hermitian without
choosing \(F_+\).

However, this operator was **not** the frozen gate. It has not been justified
or tested here and cannot be substituted after the failure.

A separately frozen successor would be required before calculating its
four-species response.

## 7. Evidence level

\`\`\`
EVIDENCE =
EXACT_ALGEBRAIC_OBSTRUCTION /
FAIL_CLOSED /
NO_SPECIES_SEARCH_PERFORMED
\`\`\`
