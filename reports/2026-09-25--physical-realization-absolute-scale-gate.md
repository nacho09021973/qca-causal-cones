# 8.21 — PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE execution

Date: 2026-09-25.

## Verdict

\`\`\`
PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE = NO_ABSOLUTE_SCALE_DERIVABLE
EVIDENCE = EXECUTED / PRELIMINARY / NO_INDEPENDENT_REVIEW
4A = NOT_CHARTERED / NOT_EXECUTED
\`\`\`

This closes the 4B question under the frozen contract without reopening
Secs. 8.15–8.20. It does **not** weaken the closed model theorem. It does
not say that the response is physically impossible. It says that the frozen
CJWW (5.15) structure, together with the checked external literature, does
not determine an absolute microscopic scale or provide a natural physical
identification of the complete Sec. 8.20 protocol.

The terminal state is not
\`PHYSICAL_MAP_EXISTS_BUT_UNOBSERVABLE\`: that label requires a defensible
physical map and SI observable first. Here the map itself is missing.

## 1. Frozen input

Inherited without rederivation:

\[
\delta(N)=|C(\theta_N)|N^{-13/2}e^{-K_*N}
\left(1+O(N^{-1/2})\right),
\qquad
\theta_N=\left\{\frac{\sqrt3\,N}{4}\right\},
\]

for the twelve frozen Pauli encoder–detector pairs, with
\(K_*=I(v_*)>0\), \(C(\theta_N)\) uniformly nonzero, and the geometry

\[
A_N=B_2(0,N/4),\qquad
B_N=B_2(N(1,1,1),N/4).
\]

The symbolic dimensional dictionary of Sec. 8.15 is also inherited:

\[
x=an,\quad t=N\tau,\quad k=p/a,\quad
E=\hbar\omega/\tau,\quad c_{\rm IR}^{\rm phys}=a/\tau.
\]

No encoder, detector, profile, geometry, walk or asymptotic is varied.

## 2. Step 1 — exact conditional dimensional restoration

Let \(L_c\) be the physical distance between the centres of the two regional
balls. Then

\[
L_c=\sqrt3\,aN,\qquad
R_A=R_B=\frac{aN}{4}=\frac{L_c}{4\sqrt3}.
\]

If \(c_{\rm IR}^{\rm phys}=c\), then

\[
\tau=\frac{a}{c},\qquad
T=N\tau=\frac{L_c}{\sqrt3\,c},
\qquad
N=\frac{L_c}{\sqrt3\,a}.
\]

The frozen narrow-band profile \(g(Np)\), supported on \(|Np|\le1\),
has physical wave-number support

\[
|k|\le \frac1{aN}=\frac{\sqrt3}{L_c}.
\]

Near the Weyl node this corresponds conditionally to an infrared energy
scale of order

\[
E_{\rm IR}\sim\hbar c|k|
\lesssim \frac{\sqrt3\,\hbar c}{L_c}.
\]

The phase substitution is explicit. The coefficient does **not** depend on
\(\{N/4\}\); its frozen definition is

\[
\theta_N=\left\{\frac{\sqrt3\,N}{4}\right\}.
\]

Since \(N=L_c/(\sqrt3 a)\),

\[
\theta_N
=
\left\{\frac{\sqrt3}{4}\frac{L_c}{\sqrt3 a}\right\}
=
\left\{\frac{L_c}{4a}\right\}.
\]

Therefore the response law becomes, conditionally on the absolute lattice
spacing \(a\),

\[
\boxed{
\delta(L_c;a)=
\left|C\!\left(\left\{\frac{L_c}{4a}\right\}\right)\right|
\left(\frac{L_c}{\sqrt3\,a}\right)^{-13/2}
\exp\!\left[-\frac{K_*}{\sqrt3}\frac{L_c}{a}\right]
\left(1+O\!\left(\sqrt{\frac{a}{L_c}}\right)\right).
}
\]

Equivalently, at fixed duration \(T\), since \(N=cT/a\),

\[
\theta_N
=
\left\{\frac{\sqrt3\,cT}{4a}\right\},
\]

and hence

\[
\delta(T;a)=
\left|C\!\left(\left\{\frac{\sqrt3\,cT}{4a}\right\}\right)\right|
(cT/a)^{-13/2}
e^{-K_*cT/a}
\left(1+O(\sqrt{a/(cT)})\right).
\]

This is a valid dimensional restoration, but it remains a family indexed by
the unknown \(a\). It does not satisfy criterion 1.

A useful structural consequence is that at fixed physical centre separation
\(L_c\), the duration \(T\), regional radii and IR momentum width are all fixed
by \(L_c\) and \(c\), whereas the suppression exponent depends on the
unresolved microscopic ratio \(L_c/a\).

## 3. Criterion 1 — absolute scale

**Score: FAIL.**

The frozen model supplies only \(a/\tau=c\). No in-repo result fixes
\(a\) or \(\tau\) absolutely.

The targeted literature recheck confirms the earlier 2026-09-17 scan:

- programmable trapped-ion and photonic Dirac-QCA experiments physically set
  their encoded step and clock, but these are engineered simulators (4A), not
  an identification of CJWW (5.15) as microscopic spacetime;
- QCA/QED phenomenology constrains possible lattice spacings through Lorentz
  violation, but provides bounds rather than a measured or derived value of
  \(a\);
- Planck-scale identifications remain assumptions, not consequences of the
  frozen walk.

Most importantly, Mlodinow and Brun use observational constraints to place
**upper bounds** on a QCA lattice spacing. A bound does not determine the
absolute scale, and that QED QCA is not the frozen CJWW (5.15) protocol.

No physically motivated relation additional to \(a/\tau=c\) was found that
fixes \(a\) for this model.

## 4. Criterion 2 — physical dictionary

**Score: FAIL for 4B.**

No checked source identifies a natural system whose microscopic dynamics is
the frozen three-dimensional CJWW (5.15) walk together with all of:

- the two internal components;
- the four Pauli encoders \(M\);
- the detector effects \(M_B\);
- the regional Alice/Bob profiles;
- the \(g(Np)\) narrow-band preparation.

There are partial dictionaries in three distinct senses, none sufficient:

1. **Engineered simulators.** Trapped-ion and photonic DQCA platforms map
   coin/internal states, positions and measurements to hardware degrees of
   freedom. They are 4A antecedents and do not establish a natural 4B map.
2. **Natural effective analogs.** Graphene/Weyl-material language supplies
   pseudospin/band degrees and physical lattice constants, but no checked
   source identifies the exact frozen CJWW dynamics or its corona observable.
3. **Fundamental QCA proposals.** Weyl/Dirac/QED QCA programs interpret
   two-component fields physically, but the absolute lattice scale is not
   derived and the observables studied are different (dispersion,
   anisotropy, interferometric phase, etc.).

A formal relabeling of the two components as spin or pseudospin is not enough
under the charter.

## 5. Criterion 3 — dimensional apparatus observable

**Score: CONDITIONAL FORM AVAILABLE / NOT CLOSED PHYSICALLY.**

The frozen \(\delta=|L|\) is dimensionless. If — and only if — a physical
dictionary made \(M_B\) a binary detector effect for repeated trials, a
generic count law would be

\[
|\Delta n|
=
\eta\,\mathcal R\,T_{\rm int}\,\delta(L_c;a),
\]

where \(\mathcal R\) is a trial/event rate in s\(^{-1}\),
\(T_{\rm int}\) is integration time in seconds, and \(\eta\) is an overall
detection efficiency. This is an explicit conditional apparatus law.

However, \(\eta\), \(\mathcal R\), the physical event represented by \(M_B\),
and the preparation procedure are not supplied by the frozen model or by a
natural-system identification. Therefore this formula does not close
criterion 3. It is only the SI/count form that would follow once criterion 2
were solved.

## 6. Criterion 4 — detectability

**Score: CONDITIONAL DIAGNOSTIC ONLY; no natural-map verdict.**

Because criteria 1 and 2 fail, there is no defensible physical substitution
on which to base a terminal detectability claim.

Nevertheless the frozen bound already shows the scale problem. Using

\[
\delta(N)\le36N^4e^{-JN},\qquad
J=(1-\sqrt3/2)\log2\approx0.0928641,
\]

and \(N=L_c/(\sqrt3 a)\), any hypothesis with \(a\ll L_c\) is
nonperturbatively suppressed.

As a **diagnostic only**, if one imposes the Planck-length assumption
\(a=\ell_P\) and chooses \(L_c=1\) m, then

\[
N\approx3.57\times10^{34},\qquad
JN\approx3.32\times10^{33},
\]

so even the one-sided bound is of order smaller than roughly

\[
10^{-1.44\times10^{33}}
\]

up to the polynomial factor. This is not a prediction because
\(a=\ell_P\) is not derived and no physical dictionary has been established.

The same logic applies, even more strongly, to very small lattice-spacing
bounds obtained in other QCA phenomenology. Those bounds cannot be imported
as the scale of CJWW (5.15).

## 7. Targeted 2026 literature recheck

The execution rechecked the literature scan against current sources.

- C. Huerta Alderete et al., *Quantum walks and Dirac cellular automata on a
  programmable trapped-ion quantum computer*, **Nature Communications 11,
  3720 (2020)**, DOI **10.1038/s41467-020-17519-4**: engineered QW/DCA
  simulator.
- A. Suprano et al., *Photonic cellular automaton simulation of relativistic
  quantum fields: Observation of Zitterbewegung*, **Phys. Rev. Research 6,
  033136 (2024)**, DOI **10.1103/PhysRevResearch.6.033136**: engineered
  photonic DQCA simulator.
- Leonard Mlodinow and Todd A. Brun, *Bounds on quantum cellular automaton
  lattice spacing from data on Lorentz violation*, **Phys. Rev. D 112,
  074513 (2025)**, published **23 October 2025**, DOI
  **10.1103/5w6s-jr1d**, arXiv:**2506.20136**: observational **upper bounds**
  on the spacing of a QED QCA, not an absolute determination and not this
  frozen protocol.
- The targeted academic search also returned the standard discrete-spacetime
  Dirac/Weyl QCA literature and simulation-oriented 3+1D quantum walks, but
  no natural system satisfying all four 4B boxes for the frozen law.

This is a targeted recheck, not an exhaustive no-go theorem about all future
physical realizations.

## 8. Terminal-state decision

The ordered terminal-state table is applied as written.

- \`PHYSICAL_MAP_ABSOLUTE_AND_DETECTABLE\`: no — criteria 1–3 fail.
- \`PHYSICAL_MAP_EXISTS_BUT_UNOBSERVABLE\`: no — no defensible physical map
  exists first.
- \`PHYSICAL_MAP_CONDITIONAL_ONLY\`: no — the available symbolic/count
  formulas are not attached to a natural physical dictionary for the frozen
  walk.
- \`NO_ABSOLUTE_SCALE_DERIVABLE\`: **yes** — the frozen structure determines
  only \(a/\tau=c\); no additional physically motivated relation fixes the
  microscopic scale, and no useful natural map closes criteria 2–4.

Therefore

\[
\boxed{\texttt{PHYSICAL\_REALIZATION\_ABSOLUTE\_SCALE\_GATE
= NO\_ABSOLUTE\_SCALE\_DERIVABLE}.}
\]

## 9. Claim ceiling and project consequence

This result means:

- the mathematical Sec. 8.20 law remains intact;
- the project does **not** establish that nature has a causal cone wider than
  the observed relativistic cone;
- the frozen model does **not** yield a parameter-free prediction in metres,
  seconds or detector counts;
- assigning a Planck scale remains an explicit assumption;
- engineered realization remains a separate, unchartered 4A project.

No further theoretical signalling gate is opened by this result.
