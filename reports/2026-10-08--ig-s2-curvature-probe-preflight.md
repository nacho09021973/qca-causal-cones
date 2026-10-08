# IG-S2 — constraint-preserving curvature probes

Date: 2026-10-08

Branch: `research/inverse-gravity-design`.
Contract preregistration: `6ef247d`,
`theory/INVERSE_GRAVITY_CURVATURE_PROBE_GATE.md`.
Permanent auxiliary code: `63ca29d`,
`scripts/verify_inverse_gravity_curvature_probes.py`.
User authorized this bounded R-operator route after the M3 Gram remained open.

Results, author-side:

- `CONSTRAINT_PRESERVING_PROBE_PASS_AUTHOR_SIDE`.
- `AXIAL_TANGENT_TENSOR_SYMBOL_PASS_AUTHOR_SIDE`.
- `STATE_INDEPENDENT_P4_BOUND_FAIL`.
- `GROUND_STATE_CORRELATION_AND_TENSOR_SPECTRUM_OPEN`.

## 1. Primary source and fixed pair

Gu–Wen, arXiv:0907.1203v3, local
`biblioteca/arXiv-0907.1203.pdf`, SHA256
`3b1af85075e346cf00b0b91824554f6f87bf494f6bfb9737c867f2a8c134fa0c`.
Read Eqs.(47)–(48) on p.15, the full N-type H_J on p.18 and the staggered
field dictionary on p.20. The diagonal R_xx/R_yy stencils are reused from the
existing IG1b helpers read-only; R_xy is transcribed as the twofold cyclic
permutation of the source's R_yz.

Use q=3, six registers per cell, even L>=4 and the same positive comparable
couplings. The centred stencils, in register order xx,yy,zz,xy,yz,zx, are
\[
 r_{xx}=(0,t_z^2,t_y^2,0,-t_yt_z,0),\quad
 r_{yy}=(t_z^2,0,t_x^2,0,0,-t_zt_x),
\]
\[
 r_{xy}=(0,0,2t_xt_y,t_z^2,-t_zt_x,-t_zt_y),\qquad t_a=a+a^{-1}.
\]
Variables are those of the doubled-coordinate lattice. R_xy is centred on
its xy face; the two diagonal words are centred at vertices.
Define \(b_{ab}=(R_{ab}-R_{ab}^\dagger)/(2i)\) and
\[
 B_+(p)=\frac1{\sqrt{2N}}\sum_i(-1)^i e^{-ip\cdot i}(b_{xx}-b_{yy}),
\quad
 B_\times(p)=-\frac1{\sqrt{2N}}\sum_i(-1)^i
 e^{-ip\cdot(i+(x+y)/2)}b_{xy}.
\]
Here N=L^3 and p=(0,0,2pi/L). These are finite-range compact densities,
not nonlocal divisions by the derivative factor.

## 2. Exact preservation of all constraints

Every chosen R is a pure X word, so it commutes with every scalar S.
For vector stencils
\[
 v_x=(t_x,0,0,t_y,0,t_z),\
 v_y=(0,t_y,0,t_x,t_z,0),\
 v_z=(0,0,t_z,0,t_y,t_x),
\]
the nine identities \(r_{ab}\cdot v_c=0\) are Laurent polynomial identities
over the integers. For example, for the newly transcribed off-diagonal word,
\[
 r_{xy}\cdot v_x=t_z^2t_y-t_zt_yt_z=0,\quad
 r_{xy}\cdot v_y=t_z^2t_x-t_zt_xt_z=0,
\]
\[
 r_{xy}\cdot v_z=2t_xt_yt_z-t_zt_xt_y-t_zt_yt_x=0.
\]
Each component stencil is inversion-even, so these products are the required
correlations for arbitrary relative translation, not only coincident centres.
Periodizing preserves the identities on the torus; reducing modulo 3 gives
the clock commutators. Independently entered real-space overlaps agree.
Hence every R, its adjoint, b_ab and both B commute with all S/V exactly.

This gives an improvement over the preceding single-angle probes:
\[
 [H_U,B_\alpha]=0,\qquad [H_g,B_\alpha]=0,
\]
the second equality because both are functions of commuting X words.
For the full, unchanged N-type Hamiltonian,
\[
 {\cal D}^R_{\alpha\beta}
 =[B_\alpha^\dagger,[H_N,B_\beta]]
 =[B_\alpha^\dagger,[H_J,B_\beta]].
\]
In particular the penalty couplings do not appear explicitly in the numerator.
They can still affect the ground state and its correlations.
H_N itself need not preserve the joint constraint kernel.

For any complete constraint eigenspace, each B preserves that eigenspace.
Applied to a true H_N ground state that mixes constraint sectors, this says
that B does not change the instantaneous constraint eigenvalues; it does not
prove decoupling of defect excitations in the energy spectrum.

## 3. Axial tangent symbol and exact limits of its interpretation

For a formal commuting infinitesimal angle field, the linearization of
\((R-R^\dagger)/(2i)\) is the angle stencil r.theta. This is an algebraic
tangent calculation, not an assumption about actual q=3 fluctuations.
Use Fourier phases at the actual register centres and k=k_*+p, with
k_*=(pi,pi,pi). Then
\[
 t_x=t_y=0,\qquad t_z=-2\sin(p_z/2),\qquad
 a(p)=t_z^2=4\sin^2(p_z/2).
\]
Let M_A be the preceding angle-probe coefficient matrix:
\[
 M_A=\frac1{\sqrt2}
 \begin{pmatrix}1&-1&0&0&0&0\\0&0&0&-1&0&0\end{pmatrix}.
\]
The curvature pair has the exact axial tangent matrix
\[
 M_R(p)=a(p)\begin{pmatrix}-1&0\\0&1\end{pmatrix}M_A.
\]
The face phases agree between the input xy register and output R_xy centre,
so they do not alter this relative multiplier.
For nonzero p on the declared IR sequence, rank M_R=2; at p=0 its rank is zero.
Its kernel consists of theta_xx=theta_yy, theta_xy=0 and arbitrary theta_zz,
theta_yz,theta_zx.
The scalar tangent constraint along this axis is
\(a(p)(\theta_{xx}+\theta_{yy})=0\).
On its transverse subspace the two surviving combinations are the trace-free
diagonal difference and the xy component. The coefficient tensors
\(e^+=\operatorname{diag}(1,-1,0)/\sqrt2\) and
\(e^\times_{xy}=e^\times_{yx}=1/\sqrt2\) obey e.p=0 and tr e=0.
The source's off-diagonal field factor is included in M_A's cross normalization.

Thus the pair detects the two formal axial TT components, with multiplier
a(p)=p^2+O(p^4). Rank two here is a rank of a *linear observation map*, not the
number of physical quantum modes. It supplies no exact SO(3) helicity
classification at finite q and no estimate of ground spectral weights.

## 4. Consequences for a variational quotient

If a controlled low-energy representation established
\(B(p)=a(p)U A(p)\) with U=diag(-1,1) on the relevant ground/excitation
vectors, then its ground-subtracted Gram and energy matrices would transform as
\[
 G_R=a(p)^2 U G_A U^\dagger,\qquad
 F_R=a(p)^2 U F_A U^\dagger.
\]
The generalized Rayleigh eigenvalues would therefore be unchanged.
For the illustrative conditional scaling \(G_A\asymp |p|^{-1}\) and
\(F_A=O(1)\), this gives \(G_R\asymp |p|^3\),
\(F_R=O(p^4)\), and a quotient O(|p|).
The curvature Gram would *decrease*, not grow like L.

This statement is conditional on an actual controlled relation between the
operators on those states. In the compact model,
sin(stencil.theta) is not equal to stencil.sin(theta).
Replacing the nonlinear word by its tangent may add higher-field/contact
contributions to both matrices. These have no error estimate at fixed q=3.
One cannot insert the formal p^4 multiplier into the exact numerator or
conclude that the full exact Gram scales as p^3.

## 5. Explicit obstruction to a uniform operator p^4 bound

The product vector |0_L> has all momenta zero and H_J energy zero. Use it
solely as an operator-norm witness. Each R word shifts a finite number of
momenta modulo 3, so its H_J cost can be evaluated without a Hamiltonian matrix.
Retain the printed negative trace-cosine coupling:
\[
 H_J/\tilde J=3\left[\sum_{\text{diagonal registers}}f(L)
 +2\sum_{\text{face registers}}f(L)
 -\tfrac12\sum_{\text{vertices}}f(\sum_aL^{aa})\right],
 \quad f(t)=\tfrac32\mathbf1_{t\ne0\bmod3}.
\]

For R_xx|0> or R_yy|0>, the central vertex has two diagonal values 2,
contributing 9/4 inside brackets; four neighbours have one value 1, each
contributing 3/4. Four face values -1 contribute 3 each.
The total is \(3(9/4+4(3/4)+12)=207/4\).
For R_xy|0>, four vertices have a single diagonal value 2, contributing
3/4 each; there are eleven nonzero face registers, contributing 3 each.
The total is \(3(4(3/4)+33)=108\).
The inverse words have equal energies.

All signed translated words used here are distinct for every even L>=4.
For diagonal words a species has one coefficient 2 and two coefficients 1;
changing the sign interchanges those multiplicities. A translation must
preserve the uniquely identified centre. Different diagonal word species are
distinguished by their nonzero diagonal register types.
Off-diagonal R_xy has only the zz diagonal species, on a four-vertex xy square,
with all coefficients 2 (all 1 for its inverse). Its square fixes its centre
on L>=4. It cannot coincide with either diagonal word.
These sparse support arguments prove the all-volume distinctness; the
two declared finite tori supply auxiliary checks, not an extrapolation.

Orthogonality of the shifted basis vectors makes all Fourier phases cancel
and all mixed matrix elements zero. Since H_U/H_g commute with B, the exact
matrix expectation of the full double commutator is
\[
 \langle0_L|{\cal D}^R(p)|0_L\rangle
 =\tilde J\,\operatorname{diag}(207/4,54).
\]
It is independent of p and L. Therefore, for example,
\(\|{\cal D}^R_{++}(p_L)\|\ge207\tilde J/4>0\).
No L-independent operator-norm bound of order p_L^4 is possible.
This does not bound the expectation in the true ground state and does not
reject the same pair under a ground-specific estimate.

Locality and 1/sqrt(N) normalization still give a uniform O(J) operator bound.
One explicit conservative choice is
\(\|z^\dagger{\cal D}^Rz\|\le4158\tilde J\|z\|^2\):
a local H_J term intersects at most fourteen translated probe densities
(a trace term sees 5 R_xx, 5 R_yy and 4 R_xy centres).
Cauchy–Schwarz and the double-commutator inequality give factor 4*14.
A diagonal R density touches terms of total norm
\(6(9J/2)+4(9J)+5(9J/4)=297J/4\); an xy density touches
\(4(9J/2)+11(9J)+4(9J/4)=126J\).
The squared coefficients sum to |z_+|^2 for the two diagonal families and
|z_cross|^2/2 for the xy family. The bound is
\(4158J|z_+|^2+3528J|z_\times|^2\le4158J\|z\|^2\).
This O(1) bound does not by itself imply the desired low excitation energy.

## 6. Reproduction

Both contract and code were committed before execution. Command:

```sh
python3 -B scripts/verify_inverse_gravity_curvature_probes.py \
  --output reports/2026-10-08--ig-s2-curvature-probe-certificate.txt
```

Observed exit 0, SymPy 1.14.0, exact arithmetic.
Certificate: `reports/2026-10-08--ig-s2-curvature-probe-certificate.txt`.
It checks nine Laurent and real-space overlap identities, the new off-diagonal
transcription, axial symbol, TT coefficient algebra and sparse-word costs.
On L=4 and L=6 it finds respectively 384 and 1296 distinct signed translated
words and verifies they have zero vector charge.
It does not compute a ground state, excitation spectrum or state correlations.
No completed earlier verifier was modified.

## 7. Decision and single next obligation

Keep this fixed curvature pair as the better constraint-preserving probe
candidate. Its exact constraint admission is established author-side;
its physical tensor spectral admission remains OPEN.
The passage from the tangent derivative factor to actual low-energy spectral
weight needs a proof and cannot be replaced by the linear symbol calculation.

The single remaining spectral obligation for the pair is
\[
 G_R(p_L)>0,\qquad
 F_R(p_L)\preceq C|p_L|G_R(p_L)
\]
in a true H_N ground state with the complete ground projector removed.
A sufficient possible route is the ground-specific estimates
\(D_R\preceq C_Dp_L^4 I_2\),
\(G_R\succeq g_R|p_L|^3I_2\); neither is currently proved.
A smaller exact F_R estimate could also work without controlling all of D_R.
Failure of these particular sufficient estimates does not refute every
possible quotient bound.

No claimed improvement in scientific maturity: the result is an exact
observable-admission/tangent-symbol preflight with a concrete obstruction to
an automatic operator-norm spectral argument. True-vacuum control, mode
separation, QCA energy–tick bridge and Einstein dynamics remain OPEN.
