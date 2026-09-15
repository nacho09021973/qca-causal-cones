# S4 strict-cone counterexample family

**Branch-local status:** analytic freeze for independent review.  
**Canonical state:** unchanged; `state/CURRENT_STATE.md` remains authoritative until a later explicit promotion commit.

## 1. Claim under test

The strong form of the working hypothesis was

\[
B_\infty^*:\qquad c_0=c_{\rm strict}^{\rm iso},
\]

with the strict asymptotic body defined from exact Fourier support under iteration.

This note gives an explicit `s=4` family on the same BCC neighborhood and the same non-trivial Pauli projective `D_2` symmetry class for which

\[
C_\infty^{\rm strict}=C_{\rm micro},\qquad
c_{\rm strict}^{\rm iso}=\frac1{\sqrt3},
\]

but

\[
c_0(a)=\frac{a}{\sqrt3},\qquad 0<a<1.
\]

Thus the strict causal body alone does not fix the Weyl slope once the internal multiplicity is enlarged from `s=2` to `s=4`.

This does **not** refute the classified `s=2` Pavia result.

## 2. Definition of the family

Let `sigma_i` act on the Pauli factor and `tau_i` on a two-dimensional multiplicity factor,

\[
\mathbb C^4=\mathbb C^2_\sigma\otimes\mathbb C^2_\tau.
\]

For

\[
0<a<1,\qquad b=\sqrt{1-a^2},
\]

define

\[
T_x=b\tau_x+a\tau_z,\qquad
T_y=b\tau_y+a\tau_z,\qquad
T_z=-b\tau_x+a\tau_z,
\]

and

\[
\Gamma_x=\sigma_x\otimes T_x,\qquad
\Gamma_y=\sigma_y\otimes T_y,\qquad
\Gamma_z=\sigma_z\otimes T_z.
\]

Each `T_i` is Hermitian and satisfies `T_i^2=I`, hence each `Gamma_i` is Hermitian and involutory.

The original one-parameter counterexample uses

\[
W=I\otimes e^{-i\pi\tau_z/4}
\]

and

\[
A_a(\mathbf k)
=W e^{-iq_x\Gamma_x}e^{-iq_y\Gamma_y}e^{-iq_z\Gamma_z},
\qquad q_i=k_i/\sqrt3.
\]

A useful two-parameter deformation is

\[
A_{a,\theta}(\mathbf k)
=W_\theta e^{-iq_x\Gamma_x}e^{-iq_y\Gamma_y}e^{-iq_z\Gamma_z},
\qquad
W_\theta=I\otimes e^{-i\theta\tau_z}.
\]

The counterexample itself requires only `theta=pi/4`.

## 3. Exact unitarity and BCC Fourier support

Because `Gamma_i^2=I`,

\[
e^{-iq_i\Gamma_i}=e^{-iq_i}P_i^+ + e^{iq_i}P_i^-,
\qquad
P_i^\pm=\frac{I\pm\Gamma_i}{2}.
\]

Therefore, with

\[
h_s=\frac{(s_x,s_y,s_z)}{\sqrt3},\qquad s_i\in\{\pm1\},
\]

and the repository Fourier convention `exp(-i k.h)`, the only Fourier coefficients are

\[
A_{h_s}^{(a,\theta)}
=W_\theta P_x^{s_x}P_y^{s_y}P_z^{s_z}.
\]

There are exactly eight BCC modes and no on-site coefficient `A_e`.

Unitarity is exact for every `k`, since the four factors in `A_{a,theta}(k)` are unitary.

## 4. Exact D2 covariance

Use

\[
R_x=\sigma_x\otimes I,\qquad
R_y=\sigma_y\otimes I,\qquad
R_z=\sigma_z\otimes I.
\]

These realize the same non-trivial Pauli projective class used by the minimal Weyl walk. They commute with `W_theta`. Conjugation by `R_x` fixes `Gamma_x` and flips `Gamma_y,Gamma_z`; cyclically for `R_y,R_z`. Hence

\[
R_l A_{a,\theta}(\mathbf k)R_l^\dagger
=A_{a,\theta}(l\mathbf k)
\]

for the binary rotations of the BCC tetrahedral generators.

## 5. Vertex survival and the strict asymptotic body

For a BCC vertex coefficient,

\[
\operatorname{tr}A_{h_s}^{(a,\theta)}
=
\frac12\left[
\cos\theta
+s_xs_ys_z\,a\left(\sin\theta-2(1-a^2)\cos\theta\right)
\right].
\]

At the counterexample point `theta=pi/4`, this becomes

\[
\operatorname{tr}A_{h_s}^{(a)}
=
\frac{\sqrt2}{4}
\left[1+s_xs_ys_z\,a(2a^2-1)\right].
\]

For `0<a<1`,

\[
|a(2a^2-1)|<1,
\]

so every trace is nonzero. Therefore no vertex coefficient is nilpotent.

Let `S_n` be the exact Fourier support of `A_a^n`. Since each `h_s` is an extreme vertex of

\[
C_{\rm micro}=\operatorname{conv}\{h_s\}
=[-1/\sqrt3,1/\sqrt3]^3,
\]

the displacement `n h_s` can arise from only the word `h_s+...+h_s`. Its coefficient is therefore exactly

\[
(A_{h_s}^{(a)})^n\neq0.
\]

Hence every vertex of `C_micro` lies in `S_n/n` for every `n`, while every `n`-step average lies in `C_micro`. Thus

\[
\boxed{\operatorname{conv}(S_n/n)=C_{\rm micro}\quad\forall n\ge1}
\]

and consequently

\[
\boxed{C_\infty^{\rm strict}=C_{\rm micro}},\qquad
\boxed{c_{\rm strict}^{\rm iso}=1/\sqrt3}.
\]

For fixed `a`, the same vertex-survival conclusion persists on an open interval of `theta` around `pi/4` by continuity of the nonzero trace condition. No global all-`theta` strict-cone claim is made here.

## 6. Irreducibility

Suppose `X` commutes with all eight Fourier coefficients. Summing the coefficients gives

\[
W_\theta=\sum_s A_{h_s}^{(a,\theta)},
\]

and sign-weighted sums give

\[
W_\theta\Gamma_i=\sum_s s_i A_{h_s}^{(a,\theta)}.
\]

Therefore `X` commutes with `W_theta` and all three `Gamma_i`.

For `sin(theta) != 0`, the two eigenvalues of `W_theta` on the `tau_z` factor are distinct, so `[X,W_theta]=0` makes `X` block diagonal in the `tau_z` decomposition. Because `a!=0` and `b!=0`, commuting with `Gamma_x` forces the two blocks to coincide and to commute with `sigma_x`. Commuting with `Gamma_y` then forces that common block also to commute with `sigma_y`. The only such `2x2` matrix is scalar. Hence

\[
\boxed{\{X:[X,A_{h_s}]=0\ \forall s\}=\mathbb C I_4}.
\]

The family is not a direct sum of two decoupled `s=2` Weyl walks.

## 7. Weyl sectors and tunable velocity

At `k=0`,

\[
A_{a,\theta}(0)=W_\theta
\]

has two rank-two eigenspaces with eigenvalues `exp(-i theta)` and `exp(+i theta)`. For `0<theta<pi/2` they are spectrally separated by quasienergy

\[
\Delta\varepsilon=2\theta.
\]

On the `tau_z=+1` doublet,

\[
P_+\Gamma_iP_+=a\,\sigma_iP_+,
\]

so the first-order effective Hamiltonian is

\[
H_{\rm eff,+}
=\theta I_2
+\frac{a}{\sqrt3}\,\mathbf k\cdot\boldsymbol\sigma
+O(|\mathbf k|^2).
\]

The other doublet has the opposite linear orientation and the same speed magnitude. Therefore

\[
\boxed{c_0(a)=a/\sqrt3}.
\]

At `theta=pi/4`, for every `0<a<1`,

\[
0<c_0(a)<c_{\rm strict}^{\rm iso}=1/\sqrt3.
\]

This is the explicit counterexample to the strong `B_infty*` claim in the declared `s=4` class.

## 8. Two-parameter deformation and projector quantum metric

Let `P_+(k)` denote the rank-two spectral projector continuing the `exp(-i theta)` doublet near `k=0`, and define

\[
g_{ij}(0)=\frac12\operatorname{Tr}[(\partial_iP_+)(\partial_jP_+)].
\]

For a normal unitary,

\[
Q(\partial_iP_+)P_+
=
\frac{Q(\partial_iA)P_+}
{e^{-i\theta}-e^{+i\theta}},
\qquad Q=I-P_+.
\]

At `k=0`,

\[
\partial_{k_i}A=-\frac{i}{\sqrt3}W_\theta\Gamma_i,
\]

and the off-doublet part of `T_i` has magnitude `b=sqrt(1-a^2)`. Since `Tr(sigma_i^2)=2`,

\[
\boxed{g_{ij}(0)=\frac{1-a^2}{6\sin^2\theta}\,\delta_{ij}}.
\]

Thus

\[
\boxed{
 c_0^2+2\sin^2(\Delta\varepsilon/2)\,g_{ii}(0)
 =\frac13
 =(c_{\rm strict}^{\rm iso})^2
}
\]

(no sum on `i`). At `theta=pi/4`, the prefactor is one and this reduces to `c0^2+g_ii=1/3`.

This weighted identity is **established for this family only**. It is not promoted here to a general QCA theorem. The more primitive structural fact is the intra/inter-sector decomposition `a^2+b^2=1` of the microscopic involutions `Gamma_i`.

## 9. Scope and interpretation limits

1. The `s=2` Pavia classification and its fixed `c0=1/sqrt(3)` remain intact.
2. `A_{a,theta}(0)=W_theta` is not a global phase. The Weyl doublets live at nonzero Floquet quasienergy.
3. `C_infty^strict` is an exact-support body. Vertex amplitudes may decay exponentially with iteration even though they remain nonzero. No claim is made here about an essential/ballistic/Lieb-Robinson front defined by amplitude decay.
4. The weighted quantum-metric rule is a family identity, not yet a substrate principle.
5. No novelty claim is made by this note. Prior-art comparison is a separate gate.
