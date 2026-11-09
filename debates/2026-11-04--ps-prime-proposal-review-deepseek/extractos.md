# Extractos literales (preparado 2026-11-04, base 0d85366)

Generados con: `sed -n` + `nl` sobre el script (numeración original) y `pdftotext -layout -f 2 -l 2 sources/1803.01304v1.pdf` (líneas 1–40 de la salida, sin editar; la página tiene dos columnas intercaladas).

## scripts/verify_c_across_lattices_gate.py, l. 74–80, 92–97, 303–305, 348–364
```
74: EXPECTED_MASSLESS = {  # label: (r_in, c_0, number of vertices)
75:     "L1": (1, 1, 2), "L2": (R2 / 2, R2 / 2, 4),
76:     "L5a": (R3 / 3, R3 / 3, 8), "L5b": (R3 / 3, R3 / 3, 8),
77:     "L6a": (R3 / 2, sp.Rational(1, 2), 6), "L6c": (R3 / 2, sp.Rational(3, 4), 6),
78:     "L6d": (R3 / 2, sp.Rational(3, 4), 6), "L6e": (R2 / 2, R2 / 2, 4),
79:     "L6f": (R3 / 2, sp.Rational(3, 4), 6),
80: }
92: def u2(alpha, xi, zeta, theta):
93:     """JDW Eq. (1), 1803.01304v1 p.1."""
94:     return sp.exp(sp.I * alpha) * sp.Matrix([
95:         [sp.exp(sp.I * xi) * sp.cos(theta), sp.exp(sp.I * zeta) * sp.sin(theta)],
96:         [-sp.exp(-sp.I * zeta) * sp.sin(theta), sp.exp(-sp.I * xi) * sp.cos(theta)],
97:     ])
303: def jdw_shift(zs, read_L, read_R):
304:     """(S Psi)(X) = (psi^L(X+read_L), psi^R(X+read_R)): L moves by -read_L."""
305:     return monomial(zs, neg(read_L)) * PROJ_L + monomial(zs, neg(read_R)) * PROJ_R
348: ISO = [None, (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1)]  # g1=(1/2,1/2), g2=(-1/2,1/2)
349: ISO_GENS = [(sp.Rational(1, 2), sp.Rational(1, 2)), (-sp.Rational(1, 2), sp.Rational(1, 2))]
350: 
351: 
352: def row_L6e():
353:     """JDW Eq. (6) p.2: W^0 = W^3 W^2 W^1, W^j = U^j S^j,
354:     U^j = U(0, 0, -pi/2, (j-2) pi/4), S^j reads L at N_j, R at N_{j+3};
355:     isosceles neighbours X1..X6 of p.2."""
356:     zs = sp.symbols("z1:3")
357:     symbol = sp.eye(2)
358:     for j in (1, 2, 3):
359:         Uj = u2(0, 0, -sp.pi / 2, (j - 2) * sp.pi / 4)
360:         symbol = sp.expand(Uj * jdw_shift(zs, ISO[j], ISO[j + 3]) * symbol)
361:     check_unitary("L6e", symbol, zs)
362:     support = laurent_support(symbol, zs)
363:     report_row("L6e", support, ISO_GENS)
364:     return symbol, zs, support, ISO_GENS
```

## sources/1803.01304v1.pdf (JDW), p.2, texto extraído
```
                                                                                                                                 2

with W0 = Π6j=1 Wj where                                              A mass m can be added the same way as the other tri-
                                                                      angular lattice walk above.
        Wj = Rj−1 Uj Sj Rj ,
        Rj = U (0, π/2, 0, π/12 + (j − 1)π/6),
       Rj−1 = U (0, −π/2, 0, −π/12 − (j − 1)π/6),                     3. Three step walk on the triangular isosceles lattice

        Uj = U (0, 0, 0, 0) = 1.                                (2)
                                                                         We introduce a closely related walk, which approxi-
Introducing the operators Uj seems useless because, at                mates the Dirac equation also in three steps, but is de-
this stage, they all coincide with the unit operator. This            fined on an isosceles triangular lattice. Consider a lattice
is so because, as explained in Section IV below, these op-            of isosceles triangles of base  and perpendicular height
erators actually code for an electromagnetic field acting             /2. Each point X = (x, y) now has six neighbours de-
on the walk and we are considering only free walks in the             fined with the respective coordinates X1 = (x + , y),
present section. The more general case is described in                X2 = (x + /2, y + /2), X3 = (x − /2, y + /2), X4 =
Section IV.                                                           (x − , y), X5 = (x − /2, y − /2), X6 = (x + /2, y − /2).
   Set now ∆t = 3/2 and let  tend to zero. The formal               The corresponding translation operators Ŝi are defined
limit of this DQW exists and coincides then with the                  similar to the 3-step walk above. That is, (Ŝj Ψ)(X) =
mass-less Dirac equation γ µ ∂µ Ψ = 0 with x0 = t, x1 = x,            (ψ L (Nj (X)), ψ R (Nj+3 (X)))> . The DQW is then defined
x2 = y and                                                            as Ψ(t + ∆t) = Ŵ0 Ψ(t) where Ŵ0 = Ŵ3 Ŵ2 Ŵ1 with
                                  
                               0 1                                                 Ŵj = Ûj Ŝj ,
                  γ 0 = σ1 =         ,
                               1 0
                                                                                 Ûj = U (0, 0, −π/2, (j − 2)π/4).           (6)
                                  −i 0
                  γ 1 = −iσ3 =           ,
                                   0 i                                With the choice ∆t = , this DQW tends to the Dirac
                                
                                  0 −1
                                                                     equation with the gamma matrices now being γ 0 = σ1 ,
                  γ 2 = −iσ2 =            .            (3)            γ 1 = iσ2 and γ 2 = iσ3 . To add a non-vanishing
                                  1 0
                                                                      mass m, one can for example replace Û1 with Ûm =
A non-vanishing mass m can be added by replacing W0                   U (0, 0, −π/2, −π/4 + m).
by Wm = Um W0 with Um = U (0, 0, −π/2, 3m/2).

                                                                        4. Three step walk on the hexagonal honeycomb
  2. Three step walk on the equilateral triangular                                          lattice
```

## sources/1803.01304v1.pdf (JDW), p.1, Eq. (1), texto extraído (`pdftotext -layout -f 1 -l 1`, líneas 55–63 de la salida)
```
                                           coupled to various discrete gauge fields [18–24]. In par-           An arbitrary element U of U (2) can be parametrized
                                           ticular, some DQWs can be coupled to discrete electric            by four angles:
                                           and magnetic fields in a gauge invariant manner [19–21],
                                           and magnetic confinement as well as Bloch oscillations                                                                    !
                                           have been observed. A natural, yet unanswered question                                        iα    eiξ cos θ   eiζ sin θ
                                                                                                                    U (α, ξ, ζ, θ) = e                                 .   (1)
                                           is: Can similar results be replicated on non-square lat-                                           −e−iζ sin θ e−iξ cos θ
                                           tices and, if so, which aspects depend on the choice of
                                           lattice, and which do not? The present paper is a first           Let (x, y) be orthonormal coordinates on the plane and
```
