# W4_LONG_WAVELENGTH_SPECTRUM_GATE

> **Typographic reconstruction — 2026-10-26.** Backslashes restored by hand
> against `scripts/verify_w4_long_wavelength_spectrum.py`. No words,
> coefficients or criteria changed. The frozen contract remains
> `89d53c15b15cc75948bbcaded26f1110127164e9`. The discarded sector phase,
> momentum units and observable scope require the qualifications recorded in
> `reports/2026-10-26--w4-spectrum-reconstruction.md`.

**Fecha:** 2026-09-30.  
**Estado al congelar:** `AUTHORIZED_BY_DIRECT_USER_INSTRUCTION / NOT_EXECUTED`.  
**Rama:** `research/gravitational-normalization-gate`.

## 0. Input

W4 uses the geometry-only nearest-neighbor gate

\[
K_{ef}(\kappa)=e^{-i\kappa(I-S_{ef})}
\]

in an even/odd brickwork.

W4 proved finite-speed vacuum propagation of geometry defects. This gate asks
whether the **smooth long-wavelength geometry sector** is gapless.

## 1. One-dimensional reduction

For one geometry register species along one coordinate chain, restrict to the
one-defect sector above a homogeneous \(Z\)-polarized background.

Ignore the common bond phase. On a paired bond, partial SWAP acts as

\[
M(\kappa)=
\begin{pmatrix}
c&i s\\
i s&c
\end{pmatrix},
\qquad
c=\cos\kappa,\;s=\sin\kappa.
\]

Use a two-site unit cell \(A_m,B_m\).

## 2. L1 — exact Floquet dispersion for the declared same-sign brickwork

Derive the two-layer Bloch unitary and its quasienergy \(\omega(k)\).

Determine whether

\[
\omega(k)\to0
\]

at the smooth point \(k=0\), and whether the leading small-\(k\) dispersion
is linear.

## 3. L2 — location of any gapless node

If the gapless point is instead at the staggered momentum \(k=\pi\), record
that explicitly.

A \(k=\pi\) envelope may be mathematically gapless after demodulation, but it
does not automatically represent a smooth coarse metric \(z(x)\).

## 4. L3 — minimal sign-staggered repair

As a separately evaluated control inside this gate, replace the odd-bond
layer by the inverse-angle gate \(M(-\kappa)\).

Derive its Bloch dispersion and determine whether this moves a linear gapless
node to \(k=0\) while preserving the homogeneous geometry background.

This control does not automatically replace W4 in the canonical model; it
only tests whether a local repair exists.

## 5. Terminal states

1. `W4_SMOOTH_MODE_GAPPED / STAGGERED_GAPLESS_ONLY`.
2. `W4_SMOOTH_GAPLESS_PASS`.
3. `W4_REPAIR_AVAILABLE_SMOOTH_GAPLESS`.
4. `OPEN_AFTER_AUDIT`.

## 6. Claim ceiling

Even a smooth linear geometry mode in this 1D reduction is not a massless
spin-2 graviton and does not establish isotropic 3D relativistic geometry
propagation.
