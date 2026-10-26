# Imported question: does interaction renormalize the IR speed per species in Δt = Δx QCA?

> **Provenance.** Prepared in `~/simulacion-red` (commits `dea341c`, `1d9a9b0`, `c7228e1`)
> on 2026-10-26 for import into `qca-causal-cones`. The question was formulated by Claude
> (AI-generated) while working on physical tests of the simulation hypothesis. The human
> instruction was literally: «deja la pregunta preparada para importar al qca -casual-cones».
> Nothing here has been reviewed by another model family. No gate is opened or promoted by
> importing this file.

## Relation to the canonical state

This is a sub-question of **A — IR universality** (`state/CURRENT_STATE.md` §4: "Why do
distinct low-energy species share the same effective relativistic cone/speed?", OPEN). Here
the *free* species universality and the B-family matching questions are taken as they stand
in the repo. The new ingredient is **radiative renormalization by interactions**.

## Question

In a discrete-time, finite-range QCA with Δt = Δx and *interacting* species (e.g. the 3+1
QED QCA of Eon–Di Molfetta–Magnifico–Arrighi), suppose the free IR speeds are equal,
`c_0^(i) = c_0` for all i. Does the interaction shift them by species-dependent amounts at
leading order in the couplings, with no suppression by powers of `kΔx`?

- **Q1 (generic).** In a QCA class with only cubic (or BCC) spatial symmetry and discrete
  time translation, are the dimension-4 operators that change `c^(i)` per species allowed
  by the symmetries? If so, is the one-loop shift `δc^(i)/c ~ O(g_i²)` (Collins mechanism)?
- **Q2 (protection).** Is there a symmetry of the QCA that forbids those operators and
  plays the custodial role that Collins et al. say is missing in real time? Candidates:
  - the discrete Lorentz covariance of Arrighi–Facchini–Forets (1+1 only);
  - the nonlinear Poincaré realization of Bisio–D'Ariano–Perinotti (free Weyl walk; F17 in
    the atlas);
  - a hidden hypercubic symmetry if the QCA step is the analytic continuation of an
    isotropic Euclidean transfer matrix (see "Background", point 3).
- **Q3 (bound).** If Q1 holds and Q2 fails, then observed species-universality of `c`
  (|δc_ij| ≲ 10⁻²¹–10⁻²², Coleman–Glashow as cited by Beane et al. p.9) forces tuning of the
  bare parameters per species. That would be a constraint on QCA-as-fundamental-substrate
  that is **independent of Δx** and much stronger than the dispersion bounds on Δx.

## Why it matters for this repo

`B_max` and the strong form of `B_infty^*` are already rejected (§4). If the answer to Q1
is yes and to Q2 is no, then even a QCA with exact *free* species universality would lose
it under interaction. The open question A would then have to be answered by tuning or by a
new symmetry, not by kinematics of the causal body.

## Background (read in primary sources, 2026-10-26)

1. **Collins, Perez, Sudarsky, Urrutia, Vucetich**, gr-qc/0403053.
   - p.1–2: a Planck-scale preferred-frame cutoff produces species-dependent `c` shifts of
     relative size O(g²) (0.1 %–10 %), unsuppressed by E/E_P.
   - p.4, eq. A.2: ξ = (g²/6π²)[1 + 2∫dx x f′(x)²], independent of the cutoff Λ.
   - p.3: they ask for a custodial symmetry forbidding dim-4 Lorentz violation without being
     the full Lorentz group and say none is known. They restrict to real time, not imaginary
     time.
2. **Beane, Davoudi, Savage**, arXiv:1210.1847, p.4 and footnote 3: in Euclidean lattice
   QCD the hypercubic symmetry protects against dim-4 Lorentz violation; Hamiltonian
   formulations "are also possible".
3. **Carena, Lamm, Li, Liu**, arXiv:2107.01166.
   - p.5, eqs. 29–31: trotterized real-time evolution is the analytic continuation δ_τ → iδ_t
     of the Euclidean transfer matrix on an *anisotropic* lattice.
   - p.5: changes in a_t "are compensated by modifying the bare speed of light"; a_t must be
     set nonperturbatively.
   - p.6, eq. 34: real-time correlators are the spectral sum of the Euclidean ones.
4. **Lin et al. (HadSpec)**, arXiv:0810.3588.
   - p.2: breaking hypercubic down to cubic lets dim-4 operators mix, so the action must be
     tuned nonperturbatively.
   - p.3: gauge and fermion anisotropies are tuned separately (γ_g = 4.3, γ_f = 3.4).
   - p.10: the measured `c` of π and ρ is 2–3σ from 1.
5. **Eon, Di Molfetta, Magnifico, Arrighi**, arXiv:2205.03148, p.2: 3+1 QED QCA with
   Δt = Δx; the light speed equals the circuit speed. It cites three discrete forms of
   Lorentz covariance (refs. 17–19), not yet read.
6. **Mlodinow, Brun**, arXiv:2506.20136, p.16–18: free cubic QCA photon has
   `v = c[1 − kΔx·s(θ,φ)]`, which is direction-dependent with zero angular average. No
   interaction treated.

Derivation by Claude in `~/simulacion-red/notas/2026-10-26-refutacion-tiempo-real.md`, not
reviewed:
- An isotropic Euclidean lattice yields a real-time generator H = −ln T / a whose low-energy
  spectrum inherits hypercubic protection.
- So *continuous-time* evolution derived from such a T avoids per-species tuning, at the
  cost of H not being strictly local.
- Open for this repo: whether a *strictly local, discrete-time* QCA can inherit the same
  protection.

## What would close it

- **Yes to Q1, no to Q2:** an explicit one-loop (or exact small-lattice) computation in a
  declared interacting QCA class showing `δc^(i) ≠ δc^(j)` at O(g²), together with a
  symmetry argument that no allowed term cancels it.
- **Protection:** a symmetry of the QCA step that maps the dim-4 species-speed operators to
  zero, verified on a declared class.
- In both cases, state the class (graph, cell dimension, s, symmetries) as the repo does for
  W- and F-items.

## Suggested first step (not executed)

A bounded primary-source preflight in the repo's F-family style:
- read Arrighi–Facchini–Forets 2014, Bisio–D'Ariano–Perinotti 2017 and Debbasch 2019 (Eon
  et al. refs. 17–19);
- read the interacting Thirring QCA (Bisio et al., PRA 97, 032132, 2018) and its
  perturbative treatment (Bisio et al., Entropy 27, 198, 2025);
- find whether any of them computes interaction-induced renormalization of the propagation
  speed.

Only then decide whether a computation is warranted.
