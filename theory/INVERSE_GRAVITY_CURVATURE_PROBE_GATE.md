# IG-S2 — constraint-preserving curvature-probe preflight

Date: 2026-10-08

Authorization: user accepted the proposed R-operator route and instructed
continuation. Branch: `research/inverse-gravity-design`.
Initial status: `OPEN`; freeze this file before computation.
Parent: `INVERSE_GRAVITY_DESIGN_CHARTER.md`.

## 1. Fixed domain

Full Gu–Wen N-type H_N, q=3 and six registers per cell, even periodic L>=4.
All four couplings are positive, comparable and independent of L.
IG1a clock convention, doubled coordinates and register order
xx,yy,zz,xy,yz,zx are unchanged.
Sources: local `biblioteca/arXiv-0907.1203.pdf`, Eqs.(47)–(48) p.15, full
N-type momentum term p.18, staggered continuum dictionary p.20.
No new Hamiltonian, large-U limit or ground-state ansatz is introduced.

## 2. Frozen compact operators and pair

R_xx, R_yy are the existing angle Weyl words of IG1b, centred at vertices.
R_xy is the twofold cyclic permutation of the printed R_yz on its xy face.
In Laurent coordinates t_a=a+a^-1 their relative stencils are
\[
 r_{xx}=(0,t_z^2,t_y^2,0,-t_yt_z,0),\qquad
 r_{yy}=(t_z^2,0,t_x^2,0,0,-t_zt_x),
\]
\[
 r_{xy}=(0,0,2t_xt_y,t_z^2,-t_zt_x,-t_zt_y).
\]
For each word, \(b_{ab}=(R_{ab}-R_{ab}^\dagger)/(2i)\).
Use N=L^3, p=(0,0,2pi/L) and chi_i=(-1)^(i_x+i_y+i_z) exp(-ip.i):
\[
 B_+(p)=\frac1{\sqrt{2N}}\sum_i\chi_i(b_{xx}(i)-b_{yy}(i)),
\]
\[
 B_\times(p)=-\frac1{\sqrt{2N}}\sum_i\chi_i
 e^{-ip\cdot(x+y)/2}b_{xy}(i+(x+y)/2).
\]
The face-offset phase is one along the chosen axis. Normalization and signs
match the preceding sine-angle probe pair. No momentum-dependent division
by p^2 is part of these local density definitions.

## 3. Frozen questions and acceptance criteria

1. Prove every chosen R and hence every B commutes with every S/V constraint.
   Check Laurent correlations and independently entered real-space overlaps.
2. Derive the full two-row tangent symbol around k_*=(pi,pi,pi), keeping the
   face-centre Fourier convention. On the axial slice identify its kernel,
   rank and derivative factor. Identify the TT coefficient tensors separately
   from any spectral claim or ground-space dimension.
3. Determine what this derivative factor would do to the matrix variational
   quotient *if* a controlled linear regime were available. At q=3 it is not
   permissible to replace sin(stencil.theta) by stencil.sin(theta) exactly.
4. Compute the exact reduction of [B^dag,[H_N,B]] and test any proposed
   state-independent p^4 bound with a momentum-product-state witness.
   Failure of that bound does not refute a true-ground-state estimate.

No true-ground correlator is assumed. The ground projector always refers to
the complete H_N ground space. Constraint-preserving probes do not imply
H_N preserves the constraint kernel.

## 4. Permanent finite certificate

After contract freeze, add `scripts/verify_inverse_gravity_curvature_probes.py`.
Certify the exact Laurent/real-space identities, axial symbol and TT
coefficient algebra. Check fixed L=4 and L=6 only for sparse-word translation
collisions and the printed H_J energy of each signed word acting on |0_L>.
Do not build a many-body Hamiltonian or extrapolate those finite checks.
An all-volume result requires an accompanying analytic proof.
Retain output after all assertions pass; preserve failures if they occur.

## 5. Verdicts and ceiling

`CONSTRAINT_PRESERVING_PROBE_PASS_AUTHOR_SIDE` and
`AXIAL_TANGENT_TENSOR_SYMBOL_PASS_AUTHOR_SIDE` certify their named algebra.
`STATE_INDEPENDENT_P4_BOUND_FAIL` rejects only that strong operator bound.
`GROUND_STATE_CORRELATION_AND_TENSOR_SPECTRUM_OPEN` is the default spectral
verdict until the actual matrix Rayleigh quotient is controlled.
No mode count, dispersion, Einstein or independent-review promotion follows.
