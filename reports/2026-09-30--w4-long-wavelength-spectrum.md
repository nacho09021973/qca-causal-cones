# W4_LONG_WAVELENGTH_SPECTRUM_GATE — execution

**Fecha:** 2026-09-30.  
**Contrato:** [W4_LONG_WAVELENGTH_SPECTRUM_GATE](../theory/W4_LONG_WAVELENGTH_SPECTRUM_GATE.md), frozen at commit `89d53c15b15cc75948bbcaded26f1110127164e9`.  
**Certificado exacto:** [verify_w4_long_wavelength_spectrum.py](../scripts/verify_w4_long_wavelength_spectrum.py), added at commit `6d22b365e71d619803425c4ca93b2d045abc8b42`.  
**Rama:** `research/gravitational-normalization-gate`.

## Verdict

```
W4_LONG_WAVELENGTH_SPECTRUM_GATE =
W4_REPAIR_AVAILABLE_SMOOTH_GAPLESS

DECLARED_W4 = SMOOTH_MODE_GAPPED / STAGGERED_GAPLESS_ONLY
SIGN_STAGGERED_CONTROL = SMOOTH_LINEAR_GAPLESS_IN_1D
```

The original same-sign partial-SWAP brickwork propagates geometry defects but
does not have a gapless smooth (kapprox0) mode. A minimal local sign repair
moves the linear node to (k=0).

## 1. Same-sign W4 brickwork

Ignoring the common bond phase, one partial-SWAP layer in the one-defect
sector acts as

[
M(kappa)=
egin{pmatrix}
c&i s\\
i s&c
end{pmatrix},
qquad c=coskappa,quad s=sinkappa.
]

With a two-site unit cell and the second matching shifted by one lattice site,
the two-layer Bloch unitary has determinant one and

[
oxed{
cosomega_+(k)
=
c^2-s^2cos k.
}
]

At (k=0),

[
cosomega_+(0)=c^2-s^2=cos2kappa.
]

Thus for generic small nonzero (kappa),

[
omega_+(0)=2|kappa|+O(kappa^3),
]

so the smooth mode is gapped.

At (k=pi),

[
cosomega_+(pi)=c^2+s^2=1.
]

For (k=pi+q),

[
cosomega_+
=
1-rac12s^2q^2+O(q^4),
]

hence

[
omega_+(pi+q)
=
|s|,|q|+O(|q|^3).
]

Therefore the original W4 does have a linear gapless excitation, but it is
staggered at the Brillouin-zone edge rather than a smooth (k=0) geometry
mode.

## 2. Why the staggered node is not enough

A (k=pi) excitation can be demodulated mathematically into a slowly varying
envelope. But the microscopic tetrad-control expectation alternates sign at
the lattice scale.

The W3/W6 coarse metric construction assumed slowly varying (z(x)). No
derived coarse-graining map currently identifies the staggered geometry mode
with that smooth metric variable.

Therefore the (k=pi) node cannot be promoted to a macroscopic gravitational
wave merely by relabeling momentum.

## 3. Sign-staggered repair

As a control, keep the first matching at (+kappa) and use the inverse angle
(-kappa) on the second matching.

The second layer becomes

[
M(-kappa)
=
egin{pmatrix}
c&-is\\
-is&c
end{pmatrix}
]

with the appropriate Bloch shifts.

The two-layer unitary again has determinant one, but now

[
oxed{
cosomega_-(k)
=
c^2+s^2cos k.
}
]

At (k=0),

[
cosomega_-(0)=1.
]

For small (k),

[
cosomega_-(k)
=
1-rac12s^2k^2+O(k^4),
]

so

[
oxed{
omega_-(k)
=
|sinkappa|,|k|
+O(|k|^3).
}
]

Thus the sign-staggered local repair has a genuinely smooth linear gapless
geometry mode in the 1D reduction.

## 4. Homogeneous background remains exact

Each local generator (I-S_{ef}) annihilates an identical pair
(|n_0,n_0angle).

Changing (kappa	o-kappa) therefore does not alter the exact homogeneous
background stability:

[
K_{pmkappa}|n_0,n_0angle=|n_0,n_0angle.
]

The repair changes the excitation spectrum without introducing background
drift.

## 5. Scientific consequence

The W4 statement must be split:

- finite-speed autonomous geometry propagation: retained;
- smooth massless long-wavelength geometry mode in the original same-sign
  brickwork: rejected;
- local sign-staggered repair producing a smooth linear mode in one dimension:
  established.

The repaired 1D speed is

[
v_g^{m geom}=|sinkappa|
]

in geometry-lattice sites per full two-layer step.

## 6. What remains open

The 1D repair does not yet establish a 3D isotropic relativistic geometry
sector.

In particular, the project has not shown that combining repaired updates in
three spatial directions gives

[
omega^2=c_g^2(k_1^2+k_2^2+k_3^2)+O(|k|^4)
]

for the relevant tensor modes.

Nor has it identified a massless spin-2 representation or transverse-traceless
constraint.

## 7. Terminal decision

[
oxed{
	exttt{W4\_REPAIR\_AVAILABLE\_SMOOTH\_GAPLESS}
}
]

is the terminal state.

A successor may replace the W4 stiffness brickwork by the sign-staggered
version, but must separately verify the multidimensional/tensor spectrum.
