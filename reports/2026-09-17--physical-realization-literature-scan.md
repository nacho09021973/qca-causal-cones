# 4B literature scan — adversarial, bibliographic only

**Date:** 2026-09-17. **Status:** `LITERATURE_SCAN / NOT_A_GATE_EXECUTION`.
Does **not** assign a terminal state of
`PHYSICAL_REALIZATION_ABSOLUTE_SCALE_GATE`. Does **not** reopen Sec. 8.20.
Does **not** charter 4A. Step 3 remains input.

**Hard question.**

> Does the literature contain a *natural* physical system — not merely a
> programmed simulator — whose microscopic dynamics can be identified
> with a local Weyl/Dirac quantum walk or QCA, with \(a\) and \(\tau\)
> physically fixed, such that its infrared Weyl cone is strictly narrower
> than its microscopic causal support, and such that that difference has
> a *known* observable?

A “no” is a valuable result: it locates where the theory paper ends and
speculation begins.

**Method.** Classify, do not fall in love. Three bins, and four charter
boxes scored only as literature coverage (`COVERED` / `PARTIAL` /
`ABSENT` / `ASSUMPTION`), never as `DERIVED` from CJWW (5.15).

| Bin | Meaning |
| --- | --- |
| `ENGINEERED_EMULATOR` | Photonics, trapped ions, cold atoms: \(a,\tau\) set by the experimenter. |
| `NATURAL_EFFECTIVE_ANALOG` | Weyl semimetals, graphene-like, Floquet materials: lattice and hoppings are material parameters, not a proposed substrate of spacetime. |
| `FUNDAMENTAL_CANDIDATE` | A proposal in which \(a,\tau\) would be scales of the physics itself. Only this bin can answer the original ambition. |

Four boxes of the 4B charter: (1) absolute scale, (2) physical
dictionary of modes / \(M=\sigma_j\) / \(M_B\) / narrow-band
preparation, (3) dimensional observable with an SI law, (4)
detectability of \(\delta\sim e^{-K_*\lambda/a}\).

---

## 0. Provisional answer to the hard question

**No** source in this scan fills all four boxes for a *natural* system
with the corona observable of Sec. 8.20.

What exists, robustly, is 4A-type evidence: discrete Dirac/Weyl dynamics
can be *implemented*. That is technically real and scientifically
useful. It does not identify CJWW (5.15) as the microscopic substrate of
nature, and it does not supply the operational infrared signal of the
Theorem as a laboratory or astrophysical observable.

The scan is not exhaustive. It is adversarial enough to block the
shortcut “there are ion-trap Dirac automata, therefore 4B is open in
the optimistic direction.”

---

## 1. `ENGINEERED_EMULATOR` — 4A antecedents, not 4B

These papers show that a Dirac cellular automaton / discrete-time
quantum walk can be run on hardware. The lattice and the clock are
programmed.

### 1.1 Trapped ions (1D)

C. Huerta Alderete *et al.*, *Quantum walks and Dirac cellular automata
on a programmable trapped-ion quantum computer*, Nat. Commun. **11**,
3720 (2020), [arXiv:2002.02537](https://arxiv.org/abs/2002.02537).

Five-qubit encoding of a 1D walker on \(^{171}\mathrm{Yb}^+\) in a Paul
trap; up to five steps; Dirac cellular automaton with tunable mass
(\(\theta_2\) as mass). The authors present it as a *circuit-based
implementation* and a simulator of the discretized Dirac equation.

| Box | Coverage |
| --- | --- |
| (1) scale | `ABSENT` as physics of nature. \(a,\tau\) are gate times and an encoded position, not spacetime. |
| (2) dictionary | `PARTIAL` for a 1D coin/mass. Not the 3D CJWW (5.15) pair \((M,M_B)\), not Euclidean balls, not \(g(Np)\). |
| (3) observable | `COVERED` as emulator: site occupation after \(N\le5\) steps. Not the corona law. |
| (4) detectability | Irrelevant: \(N\) is five, not \(e^{-K_*N}\). |

**Bin: `ENGINEERED_EMULATOR`.** Excellent 4A precedent. Not 4B.

### 1.2 Photonic DQCA (1+1)

A. Geraldi *et al.* (and collaborators), *Photonic cellular automaton
simulation of relativistic quantum fields: observation of
Zitterbewegung*, Phys. Rev. Research **6**, 033136 (2024),
[arXiv:2402.07672](https://arxiv.org/abs/2402.07672).

First photonic platform for a 1+1 Dirac QCA. Position encoded in the
orbital angular momentum of single photons; eight steps; Zitterbewegung
as the benchmark signature. Explicitly a *digital quantum simulation*.

| Box | Coverage |
| --- | --- |
| (1) | `ABSENT` as fundamental scale. OAM steps are not metres of spacetime. |
| (2) | `PARTIAL`: coin in polarization, position in OAM. 1+1 only. |
| (3) | `COVERED` as emulator: OAM distribution, Zitterbewegung. Not \(\delta_{M,M_B}(N)\). |
| (4) | Irrelevant at eight steps. |

**Bin: `ENGINEERED_EMULATOR`.** Same verdict.

### 1.3 Split-step / simulator theory

Mallick, Chandrashekar, *Dirac Quantum Cellular Automaton from
Split-step Quantum Walk*, arXiv:1509.08851. Theoretical bridge
DH–DCA–QW aimed at experimental QW implementations. Simulator design,
not a natural system.

**Bin: `ENGINEERED_EMULATOR` (theory for 4A).**

---

## 2. `NATURAL_EFFECTIVE_ANALOG` — dictionary, not substrate

These systems have a real lattice and a real \(c_{\mathrm{IR}}\)
(Fermi velocity). The lattice constant is a material number. That is
not the original ambition.

### 2.1 Honeycomb / triangular Dirac walks

Arrighi, Di Molfetta, Márquez-Martín, Pérez, *The Dirac equation as a
quantum walk over the honeycomb and triangular lattices*, Phys. Rev. A
**97**, 062111 (2018), [arXiv:1803.01015](https://arxiv.org/abs/1803.01015).

Jay, Debbasch, Wang, *Dirac quantum walks on triangular and honeycomb
lattices*, Phys. Rev. A **99**, 032113 (2019).

Continuum limit = Dirac in 2+1 dimensions on graphene-like grids.
Relevant to charter box (2): two sublattice / coin degrees of freedom
on a physical lattice. The papers *simulate* Dirac on those graphs;
they do not claim graphene’s electrons *are* a QCA of CJWW type in 3D,
nor do they exhibit a corona outside an isotropic Weyl ball with an
Alice/Bob protocol.

Graphene itself: \(a\approx 1.42\,\mathrm{Å}\) is a carbon–carbon
distance, \(\tau\) is not a fundamental clock, \(v_F\approx c/300\).
Hopping range is chemically finite; the “microscopic causal body” of a
tight-binding model is not the object of Sec. 8.20, and no paper in
this scan measures an IR-controlled operational response in a
tight-binding corona.

**Bin: `NATURAL_EFFECTIVE_ANALOG`.** Useful for the dictionary. Does
not answer the hard question.

### 2.2 Weyl semimetals and “causal” cones in energy–momentum

Gooth *et al.*-type literature on Weyl fermions; in particular
*Causal structure of interacting Weyl fermions in condensed matter
systems*, Nat. Commun. **14** (2023),
[doi:10.1038/s41467-023-37931-w](https://www.nature.com/articles/s41467-023-37931-w).

The “light cone” here is an *energy–momentum* analogue (Weyl cone,
Fermi velocity). It is not a spacetime causal body \(C_{\mathrm{micro}}\)
versus \(B(c_{\mathrm{IR}})\) for a discrete-time walk, and the
observable is a CDW gap / metal–insulator criterion, not
\(\delta_{M,M_B}(N)\).

**Bin: `NATURAL_EFFECTIVE_ANALOG`.** Do not import its vocabulary as
if it were Sec. 8.4.

---

## 3. `FUNDAMENTAL_CANDIDATE` — the only bin that could answer 4B

Here \(a,\tau\) are proposed as scales of the physics. In every case
checked, \(a=\ell_P\) (or a bound on \(\Delta x\)) is an
`ASSUMPTION` or an *upper bound from other observables*, not a
derivation, and the observable is **not** the infrared corona signal.

### 3.1 Pavia Weyl/Dirac/Maxwell QCA as a theory of fields

D’Ariano, Perinotti, Phys. Rev. A **90**, 062106 (2014);
Bisio, D’Ariano, Perinotti, Tosini, arXiv:1601.04832 and 1601.04842;
Bisio, D’Ariano, Perinotti, Ann. Phys. (2016), QCA theory of light.

The automaton is dimensionless; the Planckian reading is an
interpretation of discreteness. Phenomenology: vacuum dispersion,
small longitudinal photon polarization, gamma-ray burst tests of
energy-dependent speed. D’Ariano–Perinotti already note that the
causal speed on the lattice is \(\sqrt3\,c\) in \(d=3\) (one site per
Planck time versus \(c\) from the Weyl slope). That is the geometric
gap of type (U), in their normalization. It is **not** an
Alice/Bob infrared protocol, and \(a=\ell_P\) remains interpretive.

| Box | Coverage |
| --- | --- |
| (1) | `ASSUMPTION` (Planck units). \(a/\tau=c_{\mathrm{IR}}^{\mathrm{phys}}\) still a calibration. |
| (2) | `PARTIAL`: Weyl two-component field. Not the frozen \((M,M_B)\) protocol. |
| (3) | `PARTIAL`: GRB dispersion, thermodynamics of gases — different observables. |
| (4) | Discussed for those other observables, not for \(e^{-K_*N}N^{-13/2}\). |

**Bin: `FUNDAMENTAL_CANDIDATE` (incomplete).** Closest in spirit to
the original ambition. Does not fill the four boxes for *this* law.

### 3.2 Bounds on lattice spacing from Lorentz violation

Mlodinow, Brun, *Bounds on QCA Lattice Spacing from Data on Lorentz
Violation*, arXiv:2506.20136 (2025). QCA corresponding to QED;
anisotropy and \(c\)-deviation; GRB bound
\(\Delta x\lesssim 5.8\times10^{-36}\,\mathrm{m}\) (near \(\ell_P\))
and weaker resonator bound \(\Delta x\lesssim 6.5\times10^{-26}\,\mathrm{m}\).

Brun, Mlodinow, *Detection of discrete spacetime by matter
interferometry*, arXiv:1802.03911: neutron interferometer phase
linear in \(\Delta x\); current accuracy would bound
\(10^{-27}\)–\(10^{-31}\,\mathrm{m}\).

These papers treat \(\Delta x\) as a fundamental unknown and bound it
from **dispersion / anisotropy / interferometric phase**, not from the
regional Laplace signal. If one *assumes* \(a\sim\ell_P\) and a
macroscopic \(\lambda\), charter criterion (4) for *our* \(\delta\) is
immediately astronomical: \(N\sim\lambda/a\) is of order
\(10^{35}\) per metre, so \(e^{-K_*N}\) is not a laboratory number.
That is a *candidate* for `PHYSICAL_MAP_EXISTS_BUT_UNOBSERVABLE` **if
and only if** boxes (1)–(3) were already closed for this protocol.
They are not: (1) is still `ASSUMPTION`, (2) and (3) are a different
observable.

**Bin: `FUNDAMENTAL_CANDIDATE` (incomplete).** Relevant to criteria
(1) and (4) *under a Planck assumption*. Not a positive 4B map.

### 3.3 Bialynicki-Birula 1994

Weyl, Dirac, Maxwell on a lattice as QCA. Supplies the dimensional
dictionary form \(r=(i,j,k)a\), \(\Delta t\), and \(a=c\Delta t\) as a
continuum-matching convention (already audited in Sec. 8.15). Does
not fix numerical \(a\).

**Bin: `FUNDAMENTAL_CANDIDATE` (dictionary form only).** Already
inherited as `DIMENSIONAL_MAP_CONDITIONAL`.

---

## 4. Scoreboard against the hard question

| Source | Bin | Natural system? | \(a,\tau\) fixed by physics? | Corona vs IR cone? | Known observable of *that* gap? |
| --- | --- | --- | --- | --- | --- |
| Huerta Alderete *et al.* 2020 | emulator | no | no | 1D Dirac CA, not 3D corona | occupation of encoded sites |
| Geraldi *et al.* 2024 | emulator | no | no | 1+1 DQCA | Zitterbewegung in OAM |
| Arrighi *et al.* 2018; Jay *et al.* 2019 | analog / theory | graphene-like, not claimed as QCA-of-nature | material \(a\), not \(\tau\) of spacetime | continuum Dirac on honeycomb | none for the Sec. 8.20 signal |
| Weyl-semimetal “causal cones” 2023 | analog | crystal | Fermi velocity, not QCA clock | energy–momentum analogue | CDW gap, not \(\delta\) |
| Pavia QCA program | fundamental, incomplete | proposed | Planck `ASSUMPTION` | geometric \(\sqrt3\,c\) vs \(c\) noted | GRB dispersion, not \(\delta\) |
| Mlodinow–Brun 2018/2025 | fundamental, incomplete | proposed | *bounded*, not derived | LIV / anisotropy | interferometry, GRB; not \(\delta\) |

No row is “yes” in every column. Therefore the hard question, on this
scan, is **no**.

---

## 5. What this does *not* decide

- It does not assign `NO_ABSOLUTE_SCALE_DERIVABLE`,
  `PHYSICAL_MAP_CONDITIONAL_ONLY`, or
  `PHYSICAL_MAP_EXISTS_BUT_UNOBSERVABLE`. Those are terminal states of
  an executed 4B gate. This file is a literature input to that gate.
- It does not weaken Sec. 8.20. Absence of a natural map is compatible
  with a complete theory paper.
- It does not open 4A. The ion and photonic papers are recorded as
  technical antecedents *if* 4A is ever chartered.
- It does not authorize Planck fiat as `DERIVED`.

## 6. Where the theory paper ends

On present evidence:

- **Model (I):** closed (the draft in `papers/`).
- **Nature (N):** not established; no literature row fills the four
  boxes.
- **Experiment:** not designed; existing hardware answers 4A-type
  questions.

That is exactly the separation required by the 4B charter. If a later
pass finds a `FUNDAMENTAL_CANDIDATE` that actually supplies (1)–(4)
for this law, it should be added as a new row, not by relabelling an
emulator.
