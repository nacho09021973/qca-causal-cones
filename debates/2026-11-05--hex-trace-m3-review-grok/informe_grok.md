<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: grok-4.7, esfuerzo: por defecto del CLI, vía: grok CLI sellado como CIRO de Sanedrín (grok 1.0.34 (3736acbc8658) [stable])
grok.json sha256 a552e5bd8333bd7db08c11f24c3196971b8c9480f5e0ecebc43f35e932b505e2
llamadas a herramienta intentadas (denegadas): 0
inicio: 2026-11-05T11:17:47Z  fin: 2026-11-05T11:32:49Z
documento: /home/ignac/qca-causal-cones/debates/2026-11-05--hex-trace-m3-review-grok/material_m3.md ; último commit observado: sin versionar ; sha256 de la copia enviada 48cf8f698224c273a7b5659567d5d5b397b17f7964bbc1235678b841dea7524b
documento: /home/ignac/qca-causal-cones/scripts/verify_hex_trace_m3.py ; último commit observado: ad84207 ; sha256 de la copia enviada 88a20b3d99b2164b91557d48b69fb113e3e3e5adf7662c088347a0146669998f
entrada_grok.txt sha256 517bc5336a6e7b9876b5fc8685eaaffc6486aec0359f35e92b7a6c0aa1a6ccf8
respuesta sha256 0d3898fb31f288a83e24207b5e060ba1ba21632c7578c70e03ca7d7ef9e60c4f
-->

The scalar certificate and the walk bridge are valid. Global verdict: **PASS**. No mandatory mathematical or documentary repair remains. The program was not executed; the four-point certificate was recomputed by hand.

## Global: PASS

Items 1–4 and 6 close the stated class: no real scalar in the normalized 37-point class meets the facet conditions inside \([-1,1]\), and no \(s=2\) walk in the stated node/isotropy/exact-hull class attains \(c_0=r_{\mathrm{in}}(H)\). Item 5 matches what the script actually implements; its disclosed limits are real and do not touch the explicit certificate.

## 1. Physical normalization, 37-point support, D6 averaging — PASS

\(g_1=(1,0)\), \(g_2=(1/2,\sqrt{3}/2)\). Dividing the hex-norm ball of radius 3 by 3 sends the six extreme frequencies to the vertices \(R^j g_1\), \(j=0,\ldots,5\), at Euclidean radius 1. The convex hull \(H\) is that regular hexagon. The side length equals the circumradius, so the inradius is \(\cos 30^\circ=\sqrt{3}/2\).

Lattice-point count under \(\max(|i|,|j|,|i+j|)\le 3\): for \(i=0,\pm1,\pm2,\pm3\) the admissible \(j\)-runs have lengths \(7,6,6,5,5,4,4\), total \(37\). The same count for radius 1 is the origin plus six points.

On a unit facet normal \(n\), \(k=tn\) gives \((p,q)=(k\cdot g_1/3,\,k\cdot g_2/3)\) along \(p=0\), \(q=0\), or \(p=q\), and \(r|t|\) becomes \(3|q|\), \(3|p|\), or \(3|p|\) respectively. Cosine is even, so the three opposite normals add nothing. The required traces are \(\cos(3q)\), \(\cos(3p)\), \(\cos(3p)\).

Full dihedral symmetry of this hexagon (rotations and reflections) preserves \(\Lambda/3\), \(S\), \(H\), and the six normal lines. The group average of a real candidate stays real, stays in \([-1,1]\), keeps value 1 at the origin, keeps support in \(S\), and still equals \(\cos(rt)\) on every normal line, because the normals are permuted and \(\cos(rt)=\cos(r(-t))\). It is enough to rule out invariant averages.

## 2. Double divisibility, Newton support, two real parameters — PASS

\[
f_0=\frac{\cos 3p+\cos 3q+\cos 3(p-q)-1}{2}
\]
is real and invariant, supported on the six vertices of \(H\) plus the origin, equals 1 at the origin, and matches the three cosines. For an invariant candidate, \(d=f-f_0\) vanishes on the three mirrors.

The identity \(\sin^2(\theta/2)=(1-\cos\theta)/2\) gives
\[
\Delta=\sin^2\frac p2\sin^2\frac q2\sin^2\frac{p-q}2=\frac{(1-\cos p)(1-\cos q)(1-\cos(p-q))}{8}.
\]
With \(z=e^{ip}\), \(w=e^{iq}\),
\[
\sin^2\frac p2=-\frac{(z-1)^2}{4z},\quad
\sin^2\frac q2=-\frac{(w-1)^2}{4w},\quad
\sin^2\frac{p-q}2=-\frac{(z-w)^2}{4zw},
\]
and the product is exactly
\[
\Delta=-\frac{(z-1)^2(w-1)^2(z-w)^2}{64 z^2 w^2}.
\]

The mirror \(p=0\) is fixed by \((p,q)\mapsto(-p,q-p)\), which is reflection through the corresponding symmetry axis of \(H\). Invariance plus \(d(0,q)\equiv 0\) gives \(\partial_q d=0\) and \(2\partial_p d=-\partial_q d\) on that line, so both derivatives vanish. In the Laurent ring, \(\partial_p=iz\partial_z\), hence \((z-1)^2\) divides \(d\). The other two reflections give \((w-1)^2\) and \((z-w)^2\). These are pairwise non-associate primes (\(C[z^{\pm1},w^{\pm1}]/(z-1)\cong C[w^{\pm1}]\), and likewise for the others; zero sets differ). Therefore their product divides \(d\), and \(d=\Delta\cdot h\) with \(h\) Laurent. Reality and invariance pass to \(h\) off the zero set of \(\Delta\), hence everywhere.

Each factor \(1-\cos\) has Newton segment of hex-radius 1, in the three directions \((1,0)\), \((0,1)\), \((1,-1)\). The Minkowski sum is the hexagon of radius 2: the six sign patterns produce the vertices \((\pm2,0)\), \((0,\pm2)\), \((\pm2,\mp2)\), each with coefficient \((-1/2)^3/8=-1/64\neq 0\). So the Newton polygon of \(\Delta\) is exactly \(H_2\). Support functions in the six facet directions add. Support of \(d\) in \(H_3\) forces support of \(h\) in \(H_1\). The integer points of \(H_1\) are the origin and one six-point orbit. Invariant real \(h\) is therefore \(\alpha+\beta S_1\) with
\[
S_1=2\bigl(\cos p+\cos q+\cos(p-q)\bigr)
\]
and \(\alpha,\beta\in\mathbb{R}\). This is necessary. It does not claim that any such \(f\) is bounded.

## 3. Four realizable evaluations and necessary inequalities — PASS

On \(p=2q\), \(x=\cos q\) runs through \([-1,1]\). Chebyshev reduction gives
\[
f_0=\frac{T_6(x)+2T_3(x)-1}{2},\quad
\Delta=\frac{(1-x^2)(1-x)^2}{4},\quad
S_1=4x^2+4x-2.
\]
For \(x\in(-1,1)\), \(\Delta>0\), so \(-1\le f\le 1\) is exactly
\[
\alpha+S_1\beta\le\frac{1-f_0}{\Delta},\qquad
-\alpha-S_1\beta\le\frac{1+f_0}{\Delta}.
\]

Recomputed values:

| \(x\) | \(f_0\) | \(\Delta\) | \(S_1\) |
|---|---|---|---|
| \(5/16\) | \(-1206391/1048576\) | \(27951/262144\) | \(-23/64\) |
| \(-1/2\) | \(1\) | \(27/64\) | \(-3\) |
| \(3/8\) | \(-17671/16384\) | \(1375/16384\) | \(1/16\) |
| \(13/16\) | \(-1265351/1048576\) | \(783/262144\) | \(249/64\) |

These match the dossier. The selected upper, lower, upper, lower bounds reduce to
\begin{align*}
\alpha-\frac{23}{64}\beta&\le\frac{204997}{10164},\\
-\alpha+3\beta&\le\frac{128}{27},\\
\alpha+\frac1{16}\beta&\le\frac{6811}{275},\\
-\alpha-\frac{249}{64}\beta&\le-\frac{7475}{108}.
\end{align*}
The reductions used were \((1-f_0)/\Delta=2254967/111804=204997/10164\) at \(x=5/16\), \(2/(27/64)=128/27\) at \(x=-1/2\), \(34055/1375=6811/275\) at \(x=3/8\), and \((1+f_0)/\Delta=-216775/3132=-7475/108\) at \(x=13/16\). All four abscissae lie in \((-1,1)\).

## 4. Positive weights, cancellation, negative constant — PASS

The weights \(64/169\), \(64/169\), \(64/245\), \(64/245\) are positive. They are forced by the \(\beta\)-slopes:
\[
3-\frac{23}{64}=\frac{169}{64},\qquad
\frac1{16}-\frac{249}{64}=-\frac{245}{64}.
\]
The \(\alpha\)-coefficients are \(+1,-1,+1,-1\) and cancel in pairs. The first pair contributes \(+\beta\) and the second \(-\beta\). The combined inequality is \(0\le C\) with
\[
C=\frac{64}{169}\left(\frac{204997}{10164}+\frac{128}{27}\right)
+\frac{64}{245}\left(\frac{6811}{275}-\frac{7475}{108}\right).
\]
The first sum is \(2278637/91476\), so the first term is \(36458192/3864861\). The second difference is \(-1320037/29700\), so the second term is \(-21120592/1819125\). Common denominator
\[
3^3\cdot5^3\cdot7^2\cdot11^2\cdot13^2=3381753375
\]
gives
\[
C=-\frac{7362262528}{3381753375}<0.
\]
Approximate size \(-2.177\) agrees with the fraction. Thus \(0\le C<0\). No real \((\alpha,\beta)\) meets even these four necessary inequalities, so no invariant scalar candidate lies in \([-1,1]\), and no real scalar candidate exists.

## 5. Software coverage and limits — PASS

Read only; not executed. Static count of the scheduled rows is 146: the stereographic set has 8 parameters, 22 of the 64 pairs have \(\Delta=0\), leaving 42 points and 84 inequalities; the slice \(x=j/16\), \(j=-16,\ldots,16\), drops the two endpoints, leaving 31 points and 62 inequalities.

The script’s formulas match the dossier: torus samples use rational points on the circle and the Laurent expressions for \(f_0\), \(\Delta\), and \(S_1\); the slice uses \(T_6\), \(T_3\), and the closed forms checked above. Two-variable Fourier–Motzkin elimination, and the weights \(1/B\) and \(-1/B\) extracted from a crossed upper/lower pair, are the right exact elimination. For the two slopes above they reproduce \(64/169\) and \(64/245\). The post-check (Laurent substitution, nonnegative weights, zero linear coefficients, negative constant) tests a certificate directly. A feasible finite sample is printed as open, not as a global witness. Cardinality checks \(37\) and \(7\) agree with the enumeration in item 1.

Limits, already stated in the dossier and confirmed by reading the script: averaging, divisibility, the Newton reduction, and facet rigidity are not mechanized. The 300-second stamp excludes the substitution recheck. The support test checks cardinalities, not the orbit structure. The slice recheck passes through \(\sqrt{1-x^2}\) even though \(f_0\), \(\Delta\), and \(S_1\) are rational in \(x\). Those are operational. They do not change the hand-checked four-row certificate, and a failure there would not turn a wrong identity into a silent pass of that arithmetic.

## 6. Phase / trace / facet bridge and strict non-attainment — PASS

Let \(U\) be unitary, \(2\times2\), Fourier support \(F\subset S\) with \(\mathrm{conv}(F)=H\), \(U(0)=e^{-i\phi}I\), and phase-removed generator \(A(n)\) Hermitian, traceless, and isotropic, \(A(n)^2=c_0^2|n|^2 I\). Hermiticity fixes the convention \(\partial_t|_{0}U_{\mathrm{tilde}}(tn)=-iA(n)\). At \(c_0=r=\sqrt{3}/2\) and \(|n|=1\), the eigenvalues of \(A(n)\) are \(+r\) and \(-r\), each of rank one.

Set \(f_U(k)=\operatorname{Re}\operatorname{Tr}U_{\mathrm{tilde}}(k)/2\). Then \(-1\le f_U\le 1\), \(f_U(0)=1\), and the support lies in \(F\cup(-F)\subset S\).

On a unit facet normal, projections of frequencies in \(S\) are integer multiples of \(\delta=r/3\), between \(-r\) and \(r\). For \(n=(0,1)\), \(h\cdot n=j r/3\); for the normals at \(30^\circ\) and \(150^\circ\), the projections are \((i+j)r/3\) and \(-ir/3\). Along \(k=sn/\delta\), the compressed matrix element \(q(s)=\langle x,U_{\mathrm{tilde}}(sn/\delta)x\rangle\) has order at most \(N=3\). For the \(+r\) eigenvector, \(q(0)=1\) and \(q'(0)=-ir/\delta=-iN\), and \(|q|\le 1\).

\(P(z)=z^N q(s)\), \(z=e^{is}\), is analytic, \(|P|\le 1\) on the disk, \(P(1)=1\), and
\[
iP'(1)=iN+q'(0)=0.
\]
A nonconstant holomorphic self-map of the disk cannot have angular derivative 0 at a boundary point where the value is 1 (Hopf’s lemma on \(|P|^2\), or Julia–Carathéodory). Thus \(P\equiv 1\), so \(q(s)=e^{-iNs}\). Equality in Cauchy–Schwarz gives \(U_{\mathrm{tilde}}(tn)x=e^{-irt}x\). Replacing \(s\) by \(-s\) for the eigenvalue \(-r\) gives the opposite phase. Therefore
\[
U_{\mathrm{tilde}}(tn)=e^{-irt}P_+(n)+e^{irt}P_-(n),\qquad f_U(tn)=\cos(rt).
\]
The same holds on every facet normal. The D6 average of \(f_U\) is a scalar candidate excluded by items 2–4. Hence \(c_0=r\) is impossible in this class.

The matching ceiling is the same Bernstein bound: order at most 3, \(|q|\le 1\), and \(q(0)=1\) give \(|q'(0)|\le 3\), so \(c_0\le r\). Equality is the case just excluded, so \(c_0<r_{\mathrm{in}}(H)\). Exactness of the hull is part of the stated class; the contradiction already uses \(F\subset S\), scalar node, \(s=2\), and isotropy. No product factorization is used. Nothing is claimed for other radii, orientations, or a uniform gap.

## Optional improvements

None of these affects the verdict.

- Write the one-line convention \(\partial_t|_0 U_{\mathrm{tilde}}(tn)=-iA(n)\) next to \(q'(0)=-iN\). Hermiticity already fixes it.
- Say “order at most 3” rather than “degree \(N=3\)”.
- Name the combined constant \(C\), not an undefined \(a\).
- In the script, test the six-point orbit as a set, and recheck the slice by Chebyshev arithmetic without square roots.

No mandatory objection remains.
