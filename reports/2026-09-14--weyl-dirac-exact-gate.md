# Standard Weyl/Dirac battery: exact derivation

Date: 2026-09-14. Baseline: `44ad178`. Evidence: analytic derivation plus the
[permanent symbolic verifier](../scripts/verify_weyl_dirac_gate.py), governed by
the [pre-execution contract](2026-09-14--weyl-dirac-gate-contract.md).

**Local result; canonical promotion pending.** This report does not revise
`state/CURRENT_STATE.md`, close a general conjecture, or open the scope gate.
It supplies the completed calculation for the seven standard symbols below.
No independent human review or novelty audit is claimed.

## 1. Result and claim ceiling

In unit-neighbor, unit-time coordinates, every declared standard Weyl case has

\[
r_d:=r_{\rm in}(C_{\rm micro})=c_0=\frac1{\sqrt d},
\qquad V_{\rm causal}^{\max}=1.
\]

For its standard Dirac coupling, at fixed \(0<m<1\), put

\[
n=\sqrt{1-m^2},\qquad M=\arcsin m,\qquad F=M\cot M=\frac{Mn}{m}.
\]

Then the two extraction procedures give different exact Taylor coefficients:

\[
\boxed{c_H=r_dF,\qquad c_{\omega^2}=r_d\sqrt F},
\qquad 0<c_H<c_{\omega^2}<r_d.
\]

Thus finite-mass equality with the inradius is false under either specified
extraction. Massless matching is exact in these cases; both ratios approach
one as the dimensionless mass approaches zero. These results neither explain
why all species should share a cone nor establish B* for an entire model class.

## 2. Inputs and attribution boundaries

The standard Weyl inputs and transpose partners are in
[Bisio et al., arXiv:1601.04832v1](https://arxiv.org/abs/1601.04832v1),
PDF p.6, equations (15)-(17). The logarithm formula is (20), p.7.
The Dirac block with the dagger is independently printed in
[Bisio et al., arXiv:1601.04842v1, equation (9)](https://arxiv.org/html/1601.04842v1#S2.E9).

Two source inconsistencies matter: the sentence after (15) in 1601.04832v1
reverses the sign of its scalar phase argument; (23) omits the lower-right
dagger. Use the matrix trace and the latter source's unitary block, respectively.
Equation (27) of 1601.04832v1 is not an exact fixed-mass Taylor formula:
the factor in (26) at zero is \(M/m\), not one. The derivation below retains it.
These observations were checked against PDF pages 6-7, not only HTML extraction.

The geometry, mass-coefficient comparison, interval proof, and scaling below
are derived here from these inputs. They are not attributed as new theorems
of the source papers. The third indexed review, arXiv:1608.02004v1, was
cross-read but is not needed for the verification chain.

## 3. Frozen coordinates, support and geometry

Let \(\mathbf k\) be dimensionless Cartesian momentum, and
\(q_j=k_j/\sqrt d\). Use the Fourier convention
\(W(\mathbf k)=\sum_{\mathbf h}e^{-i\mathbf k\cdot\mathbf h}W_{\mathbf h}\).
Define one step to be the complete update, including all factors below.

Extraction of the nonzero Fourier matrices gives

\[
N_d=\{(\epsilon_1,\ldots,\epsilon_d)/\sqrt d:
\epsilon_j\in\{-1,1\}\},\qquad d=1,2,3.
\]

All these neighbors have length one. Explicit positive generating sets can be
chosen as \(\{1\}\) in d=1, \(\{(1,1),(1,-1)\}/\sqrt2\) in d=2, and
\(\{(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\}/\sqrt3\) in d=3;
include their negatives. The last four sum to zero and generate the BCC lattice.

There are no absent corners concealed by the convex hull: each Fourier matrix
is nonzero. A product construction below supplies them explicitly; the
verifier also extracts them from the expanded published matrices.
Consequently

\[
C_d=[-1/\sqrt d,1/\sqrt d]^d,\quad
h_{C_d}(\hat\nu)=\frac{\sum_j|\hat\nu_j|}{\sqrt d}.
\]

For \(\|\hat\nu\|_2=1\), the one-norm lies between 1 and \(\sqrt d\).
Coordinate-axis directions attain the minimum; equal-magnitude directions
attain the maximum. This proves \(r_d=1/\sqrt d\) and maximum support one.
The checker independently enumerates supporting facets, obtaining \(2d\)
facets at distance \(1/\sqrt d\), and checks all vertex norms.

This is the locality hull defined by the freeze. It does not assert nonzero
propagator amplitude at every point in the hull after arbitrarily many steps.

## 4. Exact symbols and phases

For standard Pauli matrices define \(R_j(q)=\exp(-iq\sigma_j)\). The following
factorizations are exact algebraic reconstructions of the input matrices:

| Dimension | Symbol | Ordered product |
| --- | --- | --- |
| 1 | A | \(R_z(k)\) |
| 2 | A | \(R_x(q_x)R_y(q_y)\) |
| 2 | B | \(A^T\) |
| 3 | A+ | \(R_x(q_x)R_y(-q_y)R_z(q_z)\) |
| 3 | B+ | \((A^+)^T\) |
| 3 | A- | \(R_x(q_x)R_y(q_y)R_z(q_z)\) |
| 3 | B- | \((A^-)^T\) |

Each factor has Fourier coefficients \((I\pm\sigma_j)/2\); consecutive
distinct Pauli axes have nonzero projector products. This gives exactly all
the declared corners. Transposition preserves support and eigenvalues.
The extra on-site rotation mentioned after (16) is fixed to its standard
zero value, not swept or classified here. Constant internal basis changes
preserve the scalar conclusions in this battery.

Write \(W=uI-i\sigma\cdot\mathbf v\), with
\(u^2+|\mathbf v|^2=1\). Its characteristic polynomial is
\(\lambda^2-2u\lambda+1\). Hence its eigenvalues are
\(e^{\pm i\theta}\), \(\theta=\arccos u\), near the zero node. In d=1 one
may instead follow signed branches \(\pm k\); the positive phase is locally
\(|k|\). This distinction does not affect the speed coefficient.

The products give \(u=\cos k\) in d=1, \(u=\cos q_x\cos q_y\) in d=2, and
\(u=\cos q_x\cos q_y\cos q_z\pm\sin q_x\sin q_y\sin q_z\) for A±.
The sign is fixed by \(u=\operatorname{tr}W/2\), not an independent phase choice.

For all seven cases,

\[
u=1-\frac{|\mathbf k|^2}{2d}+O(|\mathbf k|^3),\quad
H_W=i\log W=\frac{\theta}{\sin\theta}\sigma\cdot\mathbf v
=\frac1{\sqrt d}\sum_j\Sigma_j k_j+O(|\mathbf k|^2),
\]

where \(\{\Sigma_i,\Sigma_j\}=2\delta_{ij}I\). Some symbols reflect a Pauli
axis; replacing that reflection silently by an identical matrix would be
incorrect, but its speed is unchanged. The displayed remainder is sufficient
in all dimensions; d=1,2 have no cubic scalar term. It follows that
\(\theta=c_0|\mathbf k|+O(|\mathbf k|^2)\), \(c_0=1/\sqrt d=r_d\).
This is an exact coefficient, not an exactly linear finite-momentum dispersion.

## 5. Fixed-mass Dirac logarithm

Using block Pauli matrices \(\tau_j\), set
\(\alpha_j=\tau_z\otimes\sigma_j\) and
\(\beta=-\tau_x\otimes I\). These anticommute and square to the identity.
The fixed sign of \(\beta\) implements the positive off-diagonal \(imI\):

\[
D=nuI-iQ,\qquad Q=n\boldsymbol\alpha\cdot\mathbf v+m\beta,
\qquad Q^2=(1-n^2u^2)I.
\]

Thus \(D^2-2nuD+I=0\). Its trace is \(4nu\), so away from coincident
phases each eigenphase occurs twice. On the principal branch near zero,

\[
\omega=\arccos(nu),\qquad
H_D=\frac{\omega}{\sin\omega}Q,\qquad
M=\omega(0)=\arccos n=\arcsin m.
\]

The formula follows directly by exponentiating \(Q/\sin\omega\), whose square
is the identity. It establishes the logarithm without an uncontrolled
matrix-log series at fixed nonzero mass.

Since \(\nabla u(0)=0\), the prefactor has no linear momentum correction.
With \(\alpha'_j=\tau_z\otimes\Sigma_j\),

\[
H_D=M\beta+\frac{Mn}{m\sqrt d}\sum_j\alpha'_j k_j
+O(|\mathbf k|^2).
\]

This proves \(c_H=r_dMn/m\) in the fixed on-site basis. Holding m fixed
while replacing \(M/m\) by one would be an additional approximation.
For \(0<m<1\) all spatial Fourier matrices remain nonzero; the on-site
coupling adds the origin, which leaves the hull and inradius unchanged.

In d=1 the constant permutation of zero-based components `(0,2,3,1)` gives
two identical blocks \(\left(\begin{smallmatrix}ne^{-ik}&im\\im&ne^{ik}\end{smallmatrix}\right)\).
Thus the same calculation covers the minimal two-component Dirac automaton;
the checker verifies this reduction explicitly.

## 6. Dispersion curvature and the missing mass correction

Implicit differentiation of \(\cos\omega=nu\), with m fixed, gives

\[
\omega=M+\frac{nr_d^2}{2m}|\mathbf k|^2+O(|\mathbf k|^3),\qquad
\omega^2=M^2+\frac{Mnr_d^2}{m}|\mathbf k|^2+O(|\mathbf k|^3).
\]

Define \(c_{\omega^2}\) as the positive square root of that isotropic
quadratic coefficient. Then \(c_{\omega^2}^2=r_d^2F\), whereas
\(c_H^2=r_d^2F^2\). In particular \(\nabla\omega(0)=0\) is not either speed.

There is no contradiction: the quadratic Hamiltonian contains a mass-direction
term \(b|\mathbf k|^2\beta\), with

\[
b=\frac{r_d^2n}{2m}(1-F),\qquad
c_H^2+2Mb=r_d^2F=c_{\omega^2}^2.
\]

Other quadratic terms lie in the spatial Clifford span and anticommute with
the constant mass term; they do not contribute at this order to \(H_D^2\).
The verifier differentiates the exact phase and prefactor separately and
checks the equality including \(2Mb\). A concrete negative control in d=1
at \(m=1/\sqrt2\) gives
\(c_{\omega^2}^2-c_H^2=\pi(4-\pi)/16>0\).

## 7. Interval proof, endpoints and continuum limit

For \(0<M<\pi/2\), define \(g(M)=\sin M-M\cos M\).
It has \(g(0)=0\) and \(g'(M)=M\sin M>0\). Hence
\(0<F=M\cos M/\sin M<1\). This proves the strict ordering for the
entire open mass interval, independent of finite samples or symbolic inequality
heuristics. Consequently \(F<\sqrt F<1\).

The small-mass expansions are

\[
\frac{c_H}{r_d}=1-\frac{m^2}{3}-\frac{2m^4}{15}+O(m^6),\qquad
\frac{c_{\omega^2}}{r_d}=1-\frac{m^2}{6}-\frac{29m^4}{360}+O(m^6).
\]

At m=0, handle the removable logarithm-prefactor singularity directly using
the Weyl blocks: both coefficients are \(r_d\). At m=1, hopping vanishes,
\(D=i\tau_x\otimes I\), \(H_D=(\pi/2)\beta\); the active support is
\(\{0\}\), and its inradius and all spatial coefficients are zero.
Keeping a declared substrate neighborhood instead would keep its positive
inradius; that different endpoint convention must be stated explicitly.
The limit of the active bodies from \(m<1\) is not the active body at m=1.

For a genuine joint continuum scaling, put
\(\mathbf k=\varepsilon\mathbf p\), \(m=\varepsilon\mu\), with fixed
\(\mathbf p,\mu\), and scale the physical step as
\(\Delta t=\varepsilon\tau_0\), neighbor length \(a=\varepsilon a_0\).
The product and block formulas give

\[
D(\varepsilon\mathbf p,\varepsilon\mu)
=I-i\varepsilon\left(r_d\sum_j\alpha'_j p_j+\mu\beta\right)
+O(\varepsilon^2).
\]

Analyticity of the matrix logarithm at I then proves
\(H_D/\varepsilon\to r_d\sum_j\alpha'_j p_j+\mu\beta\).
With \(\mathbf p=a_0\mathbf p_{\rm phys}\), the physical spatial coefficient
is \(a_0r_d/\tau_0\), equal to the physical inradius. This is a local
finite-matrix continuum statement at fixed rescaled momentum and mass;
it is not a full propagator convergence theorem on arbitrary states.

## 8. Classification

| Comparison | d=1 | d=2 | d=3 | Meaning |
| --- | --- | --- | --- | --- |
| massless c_0 = r_in | EXACT | EXACT | EXACT | Declared standard symbols, node zero |
| fixed-mass c_H = r_in | FALSE | FALSE | FALSE | Every 0<m<1 |
| fixed-mass c_omega2 = r_in | FALSE | FALSE | FALSE | Every 0<m<1 |
| fixed-mass c_H = c_omega2 | FALSE | FALSE | FALSE | Every 0<m<1 |
| both ratios tend to one | ASYMPTOTIC | ASYMPTOTIC | ASYMPTOTIC | m tends to zero; joint scaling as above |
| c_0 = V_causal^max | EXACT | FALSE | FALSE | Full-update unit-neighbor geometry |
| an unspecified finite-lattice c_IR | CONVENTION_DEPENDENT | CONVENTION_DEPENDENT | CONVENTION_DEPENDENT | Extraction and log/basis conventions required |

The numerical factors depend on coordinates: if \(q=k/\sqrt d\) is used as
momentum, the dual displacements become \(\sqrt d\,h\), so both c_0 and the
inradius become one. A common spatial/time change rescales both coefficients
and the hull together; it cannot repair a false finite-mass equality.
Likewise, transposition, a constant internal unitary, or a consistent reversal
of all eigenphase signs does not alter the speed magnitudes. A momentum-dependent
basis change or a different logarithm branch is a different extraction
convention and is excluded by this contract.

## 9. Reproduction and proposed disposition

From the repository root, using the dependency pinned in
`scripts/requirements.txt`:

```sh
python3 scripts/verify_weyl_dirac_gate.py --output reports/2026-09-14--weyl-dirac-verification.md
```

The [machine record](2026-09-14--weyl-dirac-verification.md) includes all
seven rows, exact-check count and provenance hashes. It supplements the
analytic interval and continuum arguments here; it is not a formal proof
assistant certificate or a replacement for source review.

Proposed canonical disposition for a later reason-recording commit:
standard-family massless and continuum matches verified; exact fixed-mass
matches rejected for the two frozen coefficients; general A, B*_0 and B*_cont
remain open. Preserve the initial freeze report as history. Broader activity
remains subject to `state/CURRENT_STATE.md` and its scope restriction.
