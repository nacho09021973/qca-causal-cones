# Prior art for a possible article "Waiting for the bursts" — source check

2026-11-09. Requested by the user («si, busca el prior art»). Located with WebSearch
(standard); key passages read in the original (arXiv abstract pages via WebFetch, and
full text of arXiv:2506.20136 via alphaXiv). Search summaries only located papers.

## Read in the original

| Source | What was read | Relevance |
| --- | --- | --- |
| L. Mlodinow, T.A. Brun, "Bounds on QCA Lattice Spacing from Data on Lorentz Violation", arXiv:2506.20136v1 (25 Jun 2025) | Abstract; Secs. II-III passages; Eqs. (5)-(6), (51)-(53); conclusions | **Direct overlap.** QED/massless-boson quantum walk on a cubic lattice: direction-dependent speed correction, superluminal and subluminal in different directions, averaging to zero; propagation along lattice axes at c; "If the direction of an event is within one of the planes corresponding to v_x = 0, v_y = 0 or v_z = 0, the dispersion would be zero"; "it is possible for an observation to be 'unlucky'"; recommends "limits derived separately from observations of multiple events in different directions". Uses LHAASO E_QG,1 ≳ 1e20 GeV with an RMS angular factor: Δx ≲ 5.8e-36 m, "within a little more than a factor of 2 of the Planck length". States there is no birefringence in their model (helicities degenerate), i.e. a D1-type dictionary. Also uses cavity anisotropy bounds. |
| S.R. Beane, Z. Davoudi, M.J. Savage, "Constraints on the Universe as a Numerical Simulation", arXiv:1210.1847 | Abstract | Simulation hypothesis with a lattice; b^-1 ≳ 1e11 GeV from the cosmic-ray cutoff; signature: rotational symmetry breaking reflecting the lattice in the highest-energy cosmic rays. Unimproved Wilson fermions on a cubic lattice. |
| A. Bisio, G.M. D'Ariano, P. Perinotti, "Special Relativity in a Discrete Quantum Universe", arXiv:1503.01017 | Abstract | Lorentz group recovered at low energy from QCA symmetries; nonlinear (DSR-type) distortion at the Planck scale. The abstract makes no GRB statement (a search summary claimed one; not confirmed). |

## Located, not read (`[UNVERIFIED]`)

- Bibeau-Delisle, Bisio, D'Ariano, Perinotti, Tosini, "Doubly-Special Relativity from Quantum
  Cellular Automata", arXiv:1310.6760 (EPL 109, 50003, 2015).
- Bisio, D'Ariano, Tosini et al., arXiv:1601.04842 (Weyl/Dirac/Maxwell QCA phenomenology,
  flight-time proposal); arXiv:1806.03940 (Dirac quantum walk, GRB remark).
- A July 2026 single-author preprint claiming discreteness does not force linear dispersion
  (identity not established).

## Consequence for the article (assessment, not a result)

- Already in the literature (Mlodinow–Brun 2025): an LHAASO-based upper bound on a QCA lattice
  spacing near the Planck length; the existence of blind planes for a cubic-lattice walk; the
  "unlucky orientation" issue; the advice to use several events in different directions;
  a non-birefringent (D1-type) dictionary. Beane et al. (2012): the simulation framing and
  lattice-induced anisotropy as a signature.
- Not located in what was read (candidate contributions, NOVELTY remains OPEN):
  1. the exact escape count (any ≤ 3 directions can be hidden on the coordinate planes) and the
     resulting minimum of 4 well-placed sources for an orientation-independent bound;
  2. the source-strength bottleneck (X > 9 E_Pl needed for a robust H_min exclusion of the
     cubic super-c rows; LHAASO gives 0.549 ell_P at best);
  3. the wave-vector vs propagation-direction distinction: in propagation directions on the
     blind planes the order-2 term does not vanish (-(2/3) r1^2 r2^2 for L5a/L5b/L4). Mlodinow–
     Brun state zero dispersion on v_i = 0 planes; whether this conflicts with their model needs
     their Eq. (48), not read;
  4. "ceiling does not imply unbeatable c" and "unbeatable c does not require saturation" across
     the 13 declared rows;
  5. an orientation-independent exclusion of the L3s4 subfamily under H_min.

## Full reading of Mlodinow–Brun (arXiv:2506.20136v1), added 2026-11-09

Read in full (Secs. I-IV, Eqs. (1)-(57)). Model: 6-dimensional internal space, gamma_j =
sigma_Z ⊗ J_j, U_k = exp(-i k_x Δx γ_X) exp(-i k_y Δx γ_Y) exp(-i k_z Δx γ_Z) (Eq. 16);
phase phi(k) = arccos((c_x c_y + c_x c_z + c_y c_z + s_x s_y s_z - 1)/2) (Eq. 42); doubly
degenerate (two helicities, no birefringence). Group speed v_g = c(1 - k_x k_y k_z Δx/k^2 + ...)
(Eq. 46); in velocity-direction angles v_g = c(1 - (kΔx) s(θ,φ)), s = cos θ sin^2 θ cos φ sin φ
= n1 n2 n3 (Eqs. 47-50). They claim sqrt(<s^2>) = sqrt(4π/105) ≈ 0.346 (Eq. 51) and derive
Δx ≲ ħc/(0.346 × 1e20 GeV) ≈ 5.8e-36 m (Eqs. 52-53). Max difference 0.385 c E/E_QG,1 (Eq. 54).
Blind planes stated at first order in velocity direction ("If the direction of an event is
within one of the planes ... v_x = 0, v_y = 0 or v_z = 0, the dispersion would be zero").

Author checks by hand (NOT yet verified by a versioned script; `PRELIMINARY`):
1. max |n1 n2 n3| on the sphere = 1/(3 sqrt3) ≈ 0.192 (AM-GM; also implied by their Eq. 54:
   0.385 = 2 × 0.192). A root-mean-square cannot exceed the maximum, so 0.346 is impossible.
   The known moment <x^2 y^2 z^2> over the unit sphere is 1/105, so sqrt(<s^2>) = 1/sqrt(105)
   ≈ 0.0976; their value equals sqrt(∫ s^2 dΩ) without division by 4π. Corrected Eq. (52):
   Δx ≲ ħc/(0.0976 × 1e20 GeV) ≈ 2.0e-35 m, slightly above the Planck length 1.6e-35 m.
2. Expanding their Eq. (42): cos phi ≈ 1 - k^2/2 + k_x k_y k_z/2, so phi ≈ kΔx - k_x k_y k_z Δx^2/(2k),
   half the term written in their Eq. (43). With the factor 1/2 the radial group speed is
   c(1 - n1 n2 n3 kΔx), consistent with their Eq. (46). Probably a typo in Eq. (43) only.
3. Their blind-plane statement is correct at first order in propagation direction; the
   repository's order-2 residual in propagation direction is a refinement, not a contradiction.
