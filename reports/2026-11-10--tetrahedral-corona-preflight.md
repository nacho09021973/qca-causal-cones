# Fixed tetrahedral corona: axial spectral preflight

2026-11-10. Codex. PRELIMINARY, exact author check only; no independent
review or promotion. Contract:
`theory/POLYHEDRAL_CORONA_TETRA_PREFLIGHT_GATE.md`, preregistration commit
`8eed315d65567ccc191820810420dae2baed4325`. The target axial point was
selected while designing the preflight, as recorded in the charter.

## Question and fixed rule

Can the manuscript's global group-velocity bound by its emergent ball be
transferred from CJWW to the existing cyclic s=4 tetrahedral walk?
Known inputs are the U(k), lattice and phases recorded in
`reports/2026-11-06--s4-cyclic-realization.md` sections 4--5 and the original
verifier, used read-only. The local speed is c_IR=1/3. Stop direct transfer
if a simple branch has a component faster than this speed. This preflight
does not ask whether an arbitrary polyhedron is a QCA support.

## Exact axial witness

On k=(sqrt(3)x,0,0), diagonalising the first-factor sigma_x with
eigenvalue eps=±1 gives the exact 2x2 block

    B_eps(x) = W_tau (cos x I - i eps sin x sigma_x),
    W_tau = [I - i(sigma_x+sigma_y+sigma_z)/sqrt(3)]/sqrt(2).

Its determinant is one and its semitrace is

    f_eps(x) = [cos x - eps sin x/sqrt(3)]/sqrt(2).

For the branch omega=acos f_eps (lambda=exp(-i omega)), the physical
derivative is

    partial omega / partial k_x = -f'_eps(x) / [sqrt(3) sqrt(1-f_eps(x)^2)].

At x=0 it equals eps/3, confirming the local speed in this axis.
At x=pi/2, k_x=sqrt(3)pi/2, f_eps=-eps/sqrt(6), f'_eps=-1/sqrt(2), hence

    partial omega / partial k_x = 1/sqrt(5) > 1/3.

The four eigenvalues there are the numbers

    ±1/sqrt(6) ± i sqrt(5/6),

with independent sign choices; all are distinct. Therefore the full
four-dimensional eigenphase branches are differentiable in a
neighbourhood of that momentum. This is not a derivative through a
degenerate crossing. A directional component lower-bounds the gradient
norm, so V_grp^max >= 1/sqrt(5) > c_IR. This does not calculate V_grp^max
itself. The axial component is below the axial causal support ceiling
1/sqrt(3); no conflict with finite range is implied.

Independent algebraic route within the author check: differentiate the
explicit eigenvalue lambda=f-i sqrt(1-f^2), and evaluate
i lambda'/(sqrt(3)lambda). This gives the same 1/sqrt(5); the characteristic
equation and each eigenvalue's block determinant are also checked.

## Outcome and limits

`GLOBAL_IR_BALL_BOUND_REFUTED_BY_AXIAL_WITNESS`.

The tetrahedral model has spectral group velocities outside its local IR
ball. Thus its geometric corona cannot be interpreted wholesale as the
non-ballistic region of the CJWW example. The negative result concerns
that global spectral-bound hypothesis, not the existence of an operational
response outside the local IR cone. The user-level question about such a
response remains OPEN for this tetrahedral rule.

No preparation, encoder or detector was constructed here; no wavepacket
or photon was simulated. A simple-branch velocity witness alone does not
prove a finite-N detection signal, IR admissibility, non-vanishing of the
operational coefficient, or the same exponential rate and prefactor as in
the manuscript. No maximum group-speed body or strict asymptotic support
body has been computed. The geometric viewer remains a geometry-only
illustration and is not evidence for these spectral statements.

The next scientific contract would need to decide between an operational
protocol outside the local cone in the presence of faster spectral modes,
or a non-ballistic sector outside the full group-velocity body. Neither
continuation is automatic under this preflight's stop rule.

## Reproduction

    python3 -B scripts/verify_tetrahedral_corona_preflight.py

24/24 exact SymPy author checks passed, exit 0. Stdout:
`reports/2026-11-10--tetrahedral-corona-preflight-verifier.txt`.
Verifier SHA256:
`ab424a484520f12d0909ebd839ef0708299cebd5bca8d8f20f69d56320e06f27`.
No numerical scan, tolerance or externally generated claim was used.
