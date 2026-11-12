# Fixed tetrahedral walk: infrared protocol and signal obligations

2026-11-10. Codex. **PRELIMINARY author analysis, not independently reviewed.**
Charter `theory/TETRAHEDRAL_IR_SIGNAL_GATE.md`, committed before execution
at `07d7ce6`. User authorized studying the signal under an IR protocol.

## Outcome

`OPEN_AFTER_IR_PROTOCOL_ANALYSIS`.

The fixed family satisfies the manuscript's asymptotic IR-admissibility
definition by the estimates below, including nonzero denominators. The
finite samples include exact reachability zeros and numerically nonzero
responses. No positive-signal theorem for all sufficiently large N, no
nonzero asymptotic coefficient, and no exponential rate have been proved.

Known: local c_IR=1/3 and an exact faster spectral branch in the same
tetrahedral walk. Question: what survives with actual admissible
preparation/encoding/detection? Stop a positive-signal conclusion on an
uncontrolled relative leakage or interference cancellation. The latter
remains the named obstruction; no parameters were changed to rescue it.

## 1. Protocol and separation

Use precisely the resource, unitary encoder and scalar effect in the
charter. Fourier signs here are hat psi(k)=sum exp(-ik.x)psi(x), so the
fixed U(k) implements the shifts +h/sqrt(3). No substitution of the adjoint
walk is made. The primitive lattice has cell volume V=4/(3sqrt(3)).

Let v=(-1,-1,-1)/sqrt(3), b_N=3Nv/4, R=N/32. Alice's and Bob's balls
have centres 0 and b_N and radius R. Then

    |y-x| >= 3N/4-2R = 11N/16 > N/3.

The relative-velocity ball has centre 3v/4 and radius 1/16. For a unit
tetrahedral vertex w the faces are w.z >= -1/3; at z=3v/4 the smallest
margin is 1/12. Hence the relative-velocity ball lies strictly inside
C_micro. These are geometrical separation statements, not reachability
of every site in that continuous envelope.

The momentum resource has exact compact support |k|<=1/N and constant
spinor chi=|up> tensor eta_+, with eta_+ the +1 eigenvector of n.sigma.
It lies in the positive nodal subspace at k=0; no exact finite-k band
projection or restriction to a single quasienergy branch is asserted.
The resource has a spatial tail already at Bob, as in the manuscript;
the observable is the difference between Alice's encoded and unencoded
bits on that same resource.

Normalisation follows directly from radial integration:

    integral_{|q|<=1} (1-|q|^2)^4 dq
       =4pi[1/3-4/5+6/7-4/9+1/11]=512pi/3465,
    Z_N=V*64/(3465 pi^2 N^3).

In position space phi_N(x)=sqrt(V) N^(-3/2) Phi_0(x/N) chi, with
Phi_0(w)=sqrt(3465)/(64pi^2) integral g(q) exp(iq.w)dq.
This matches the manuscript's scalar Fourier profile after restoring
the primitive-cell volume. In particular it is real and strictly
positive on |w|<=1/32: the integral's real part is bounded below by
cos(1/32) integral g>0.

## 2. Operator leakage on the actual lattice

Let a_j be the three primitive vectors specified in the charter and
D_j=T_{a_j}-I. In the chosen momentum cell theta_j=k.a_j lies in [-pi,pi).
For every momentum in that cell,

    sum_j |exp(i theta_j)-1|^2
       >= (4/pi^2) sum_j theta_j^2
       >= 4|k|^2/(3pi^2).

The last inequality follows because the primitive-vector Gram matrix
has diagonal 1 and off-diagonal -1/3, hence eigenvalues 1/3,4/3,4/3.
Thus ||(I-Pi') f|| <= C sqrt(N) (sum_j ||D_j f||^2)^(1/2).
The same Gram matrix gives ||D_j Pi||=O(N^-1) on |k|<=N^-1.

For X_N=V_N-I or E_N the fixed profile has bounded norm and lattice
differences O(N^-1), uniformly in its translate. Product differentiation
on the lattice (the exact shifted Leibniz identity) gives

    ||D_j(X_N Pi)||
       <= ||D_j X_N||_infinity + ||X_N|| ||D_j Pi|| = O(N^-1),
    ||(I-Pi')X_N Pi||=O(N^-1/2).

This proof uses the full momentum cell, not a continuum gradient that
would miss lattice zeros. It remains valid for the C1, piecewise smooth
profiles: only first finite differences and a global Lipschitz bound
are needed. Constants depend on the fixed radius ratio 1/32; no useful
small-N threshold is inferred.

## 3. Relative denominators and encoded state

An absolute leakage estimate is insufficient on its own. For the encoder,
test ||(V_N-I)Pi|| on phi_N. Since chi^dagger M chi=0 and M^2=I,

    ||(V_N-I)phi_N||^2
      =sum_x 2[1-cos(pi F_N(x)/2)] |phi_N(x)|^2.

Scaled lattice Riemann sums converge to the positive integral

    integral 2[1-cos(pi F(w)/2)] |Phi_0(w)|^2 dw > 0,
    F(w)=(1-1024|w|^2)_+^2.

The primitive-cell factors cancel the scaled site density. The integrand
is continuous, compactly supported, and positive on a neighbourhood of
zero. Hence ||(V_N-I)Pi|| has a fixed positive lower bound for all large N.
For E_N, use a band-limited resource translated to b_N. The same Riemann
sum argument gives ||E_N Pi|| bounded below, since h_N is positive near
its centre. Translation need not be a lattice translation for this test:
the phase exp(-ik.b_N) defines the shifted band-limited resource on L;
translated Riemann sums still converge, uniformly in the offset of b_N
within a primitive cell. Both relative operator leakages are O(N^-1/2).

For the state denominator, write

    a_N=<phi_N,V_N phi_N>=sum_x cos(pi F_N(x)/2)|phi_N(x)|^2.

It is real, 0<=a_N<1, and 1-a_N tends to the strictly positive integral
with factor 1-cos above. Strict inequality also holds at every integer
N>=8 because x=0 contributes positive resource weight and F_N(0)=1.
Consequently Delta_N!=0 and

    ||Delta_N||_1=2sqrt(1-a_N^2)

is bounded below for all sufficiently large N. Since Pi'phi_N=phi_N,

    ||Delta_N-Pi'Delta_N Pi'||_1
       <=2||(I-Pi')V_N phi_N||=O(N^-1/2).

Therefore eta_enc=O(N^-1/2) as well. All three ratios vanish, under the
definition frozen in the charter. This is an analytic author derivation;
the diagnostics do not establish these operator norms. Admissibility
also does not control relative errors on an exponentially small signal.

## 4. Signal evaluation and fixed finite-N diagnostics

Let r_N=U^N phi_N and a_N^diff=U^N(V_N-I)phi_N (distinct from the scalar
overlap a_N above). The exact stable expression is

    L_N=2 Re <r_N,E_N a_N^diff> + <a_N^diff,E_N a_N^diff>.

The first term may have either sign. A nonzero encoded difference, a
nonzero kernel, or a faster spectral mode alone does not prove L_N!=0.

The permanent script evolves only the compact difference on a sufficiently
large nonperiodic raw-coordinate grid. Its four coefficient channels are
W E_h with E_h=product_j(I+h_j G_j)/2, h_1h_2h_3=-1. No periodic resource
or FFT approximation to the narrow band is used. The unrestricted
reference and the resource at Alice are integrated over the exact ball
in rescaled momentum q=Nk, with tensor-product Gauss--Legendre/ring
cubatures of the two fixed orders. Order agreement is a sensitivity
diagnostic, not an interval-certified integration error.

| N | signed L_N, order 12 (diagnostic) | Interpretation |
| --- | --- | --- |
| 8 | 0 | exact unreachable-site zero, see below |
| 16 | 5.822948782703583e-8 | numerical nonzero only |
| 24 | 0 | exact unreachable-site zero |
| 32 | 2.139262372960612e-9 | numerical nonzero only |

Important: throughout this small-N set, the only site of strictly positive
Alice profile is the origin, and Bob's positive profile is only at b_N.
At N=32 there are eight additional boundary sites, but their profile is
exactly zero. These samples do not yet resolve the growing smooth regions
or demonstrate small leakage ratios at the sampled sizes. They cannot
establish the large-N regime just proved admissible. The frozen N set was
not extended after discovering this limitation.

## 5. Exact explanation of the two zeros

In raw integer coordinates an N-step path with counts n_0,n_1,n_2,n_3
for the four negative-parity vertices, displacement (-3N/4,-3N/4,-3N/4),
and sum counts N must satisfy

    n_0=13N/16,  n_1=n_2=n_3=N/16.

For N=8 and 24 these are not integers, so there is no path from the
only actively encoded site to the only actively measured site. Therefore
E_N U^N(V_N-I)phi_N=0 and L_N=0 exactly, independent of quadrature and
the reference tail. This is a second, combinatorial route to the zeros,
not a conclusion from observing floating-point zeros.

Integer counts for N=16 and 32 show only reachability; they do not exclude
unitary or interference cancellation. Their numerical nonzero results
are not relabelled as exact certificates.

## 6. Missing proof and closure

The unresolved step is a signed asymptotic or certified non-cancellation
bound for the exact interference-plus-square expression, for this fixed
family in its spatially resolved large-N regime. Neither the faster
spectral branch nor an absolute O(N^-1/2) leakage estimate supplies it.
No assertion that the observed signal is carried by UV modes or exclusively
by IR modes is supported by these computations. No N^-13/2 prefactor,
rate K, or positivity threshold is imported from CJWW.

The admissibility stage is complete as a PRELIMINARY analytic argument;
the operational nonzero theorem remains OPEN. Continuing would require
that named non-cancellation analysis, not a larger parameter scan or a
different protocol chosen after these data.

Reproduce the fixed diagnostics from the root:

    OPENBLAS_NUM_THREADS=1 python3 -B scripts/diagnose_tetrahedral_ir_signal.py

Data and script/base provenance: `2026-11-10--tetrahedral-ir-signal-diagnostic.json`;
stdout: `2026-11-10--tetrahedral-ir-signal-diagnostic-stdout.txt`.
Maximum norm error was below 1.5e-14; relative cubature differences at
the two nonzero samples were below 3.7e-14. These are internal numerical
consistency checks, not rigorous forward-error bounds. `git diff --check`
passed. The data file pins the final script hash and NumPy version.
No reviewed verifier was edited. No independent review, promotion or push.
