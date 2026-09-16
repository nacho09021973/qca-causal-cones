# Independent review of the frozen signalling witness

Date: 2026-09-16. **Overall verdict: PASS within the four requested points.**
Mandatory repairs: **none**.

This is one separate agent's independent review, performed before commit. It
is not external human review, multi-member consensus, or ratification. The
reviewer reconstructed the algebra and checked implementation semantics before
using the existing verifier as corroboration. No reviewed input was edited.

Baseline: branch `research/b-infinity-post-s4-gate`,
HEAD `0b3f4f534d9c7f6c32a5305a34495055fe4749ee`.
The review is tied to these working-tree bytes, including uncommitted inputs:

| Input | SHA256 |
|---|---|
| `theory/COUPLING_MAP_SIGNALING_WITNESS.md` | `9493cfa7135645acbc9dd8c10718cf33467632514fdd821d561c3257adaa6ae2` |
| `scripts/verify_signaling_witness.py` | `4953009ebf838b98e0dd095e4cbeefdde1bc65a83ee716e96d1ce3eb9ee58d17` |
| Imported `scripts/verify_directional_saturation.py` | `b6494dde083b34e34e745f2a35cba61ef3cffb63ce45f5c0afd9258eefd9d252` |

The resource hypothesis is essential: the common pre-choice preparation has
coherence between Alice and **Bob's own site**, already available before the
local choice. This review establishes no preparation protocol starting with
resources localized around Alice. The global state has exactly one particle;
its density operator respects parity superselection, and the intervention and
measurement are even local operators.

## 1. Analytic derivation of the probabilities — PASS

Use exactly the declared Laurent convention: the coefficient at displacement
`x-z` is `K_t(x,z)`. Write the supplied walk as

\[
W=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad
a=c_1c_2e^{ip_3},\quad d=c_1c_2e^{-ip_3},\quad
b=-c_1s_2+i s_1,\quad c=c_1s_2+i s_1.
\]

For real momenta, `d=conj(a)` and `c=-conj(b)`, while
`|a|^2+|b|^2=c_1^2(c_2^2+s_2^2)+s_1^2=1`.
Thus this symbol is unitary, independently of the verifier's PASS labels.

The entries of its square are `a^2+bc`, `b(a+d)`, `c(a+d)`,
`d^2+bc`. At exponent `(-2,-2,-2)`, only `d^2` can contribute:
`bc` has zero third exponent, `a^2` has third exponent `+2`, and the
off-diagonal entries have third exponent `+1` or `-1`. Each coefficient
of `e^{-2ip_j}` in `cos(p_j)^2` is `1/4`, hence

\[
A:=K_2(0,y)=\operatorname{diag}(0,1/16),\qquad y=(2,2,2).
\]

For exponent zero, the same third-coordinate argument excludes every term
except `bc` in the diagonal entries. Direct multiplication gives
`bc=-c_1^2 s_2^2-s_1^2`; its constant coefficient is
`-(1/2)(1/2)-1/2=-3/4`. Consequently

\[
B:=K_2(y,y)=-\frac34 I_2.
\]

The stipulated Heisenberg evolution `W^2 P_y W^{2 dagger}` means that
states evolve by `W^{2 dagger}`. Its `(y,x)` block is `K_2(x,y)^dagger`,
so the Bob amplitude for the two post-choice states is exactly

\[
v_b=\frac{(-1)^b A^\dagger\downarrow+B^\dagger\downarrow}{\sqrt2}.
\]

The phase gate changes the Alice arm's sign only. Therefore
`v_0=-11 down/(16 sqrt(2))` and `v_1=-13 down/(16 sqrt(2))`, giving

\[
p_0=\frac{121}{512},\qquad p_1=\frac{169}{512},\qquad
p_1-p_0=\frac{48}{512}=\frac3{32}>0.
\]

The independent interference check is
`down^dagger A B^dagger down=-3/64`; the probability difference is
`-2 Re(down^dagger A B^dagger down)=3/32`. Both arms and the factor
`1/sqrt(2)` are required; there is no omission of Bob's pre-existing arm.

## 2. Exact correspondence with the verifier — PASS

The imported `walk2()` supplies precisely the four entries above. `laurent()`
uses `z_j=exp(i p_j)`, consistently with the frozen convention. Every entry
has exponents between `-1` and `1` in each coordinate; multiplying by
`z1*z2*z3` and subtracting one from each polynomial exponent in
`exact_blocks()` therefore recovers all one-step coefficient matrices without
truncation. `square_kernel()` uses the matrix product `left*right` and summed
displacements, exactly the coefficient convolution for `W^2`.

In `evolve()`, an input at `x` contributes `matrix.H*vector` to `x-d`
for a kernel block at displacement `d`. Since `d=x-y`, this implements
`K_2(x,y)^dagger` at output `y`, not the opposite propagation convention.
`phase_choice()` negates exactly the origin component. The preparation uses
the two stipulated sites, down spin, and equal normalized amplitudes.

`reduced_state()` correctly traces a fixed-one-particle pure state: the local
vacuum probability is one minus local occupation, the local one-particle
block is `v*v.H`, and the local double-occupation block vanishes. Vacuum and
one-particle local components have orthogonal environment states, so no
missing local vacuum/particle coherence is discarded. The full local gate is
`diag(1,-1,-1,1)` and the measurement is `diag(0,1,1,1)`, matching the
theorem on the complete two-mode local Fock space.

The existing controls also match their stated scope. A particle at Alice
acquires only a global phase. Each component of the incoherent equal mixture
has an invariant density matrix. The axial reduced-state comparison uses the
same original preparation, observed at `(3,0,0)`, as the witness states.

Execution from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_signaling_witness.py
Exit status: 0
17/17 exact checks passed. Existence witness only; no optimum or asymptotic claim.
```

The execution uses exact SymPy arithmetic in the witness path and checks both
evolved global norms. Importing the other module does not run its `main()` or
its unrelated numerical diagnostics. The verifier does not itself compute a
trace norm or prove the general effect inequality; that analytic step is
reviewed in point 4. This is consistent with a theorem backed by finite exact
checks, rather than a claim that the script alone supplies every proof step.

## 3. Causal location of the vertex and axial control — PASS

The first-order symbol is
`I+i(p1 sigma1-p2 sigma2+p3 sigma3)+O(|p|^2)`. The eigenvalue magnitudes of
its linear generator are `|p|`, so the declared lattice-step normalization
has `c_IR=1`. All one-step Laurent exponents lie in `[-1,1]^3`, and all
eight corners occur with nonzero diagonal coefficients. Their convex hull
is therefore exactly `C_micro=[-1,1]^3`.

At time two, `|y|=2 sqrt(3)>2=c_IR*t`, while `||y||_infinity=2`.
Hence `y` is outside the emergent ball and is a vertex **on** the boundary
of `t*C_micro=[-2,2]^3`. Membership in this convex body alone would not prove
membership in the exact support. Here the directly derived nonzero
`K_2(0,y)` supplies that additional evidence: the Schrödinger block from
Alice to Bob is its nonzero adjoint. No strict-interior claim or replacement
of exact support by the whole convex body is needed.

For `(3,0,0)`, two-step coefficients have first coordinate at most two in
absolute value, so `K_2(0,(3,0,0))=0`. The evolved Bob generators have no
Alice component; Alice's even local unitary commutes with that algebra.
This proves the stated state-independent axial no-signalling control,
whereas the script's reduced-state equality checks the specified state.

## 4. Trace-distance normalization and effect bound — PASS

The claimed convention is
`D(rho_0,rho_1)=(1/2)||rho_1-rho_0||_1`.
For the Hermitian trace-zero difference `Delta=rho_1-rho_0`, its positive
and negative parts have equal trace,
`Tr Delta_+=Tr Delta_-=(1/2)||Delta||_1`. If `0<=E<=I`, then

\[
-\operatorname{Tr}\Delta_-
\leq\operatorname{Tr}(E\Delta)
\leq\operatorname{Tr}\Delta_+.
\]

Consequently `|Tr(E Delta)|<=D`, with **no extra factor of two** in the
probability-difference bound. For the specified non-vacuum effect, this gives
`D>=|p_1-p_0|=3/32`.

The local states have the explicit diagonal form
`diag(1-p_b,0,p_b,0)`, so the density-matrix difference has entries
`(-3/32,0,3/32,0)`. This is an additional direct consistency check of the
normalization; no search over measurements or protocols is involved. The
reviewed theorem only requires its stated lower bound.

On the full local Fock space the occupation operator is
`n_y=diag(0,1,1,2)`, which is not an effect. The actual measurement is
`E_y=diag(0,1,1,1)`, a norm-one even projection. Their equality on this
fixed-one-particle protocol justifies computing the event probability from
`||v_b||^2` without applying an invalid full-space norm-one bound to `n_y`.

The PASS establishes this finite existence witness under the explicit
distributed-resource hypothesis. It does not establish the original
optimal-D gate, an Alice-localized preparation protocol, experimental
feasibility, asymptotic scaling, novelty, or any additional gate.
