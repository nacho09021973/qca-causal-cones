# EMPIRICAL_SUBSTRATE_CONE_SURVEY — outcome

**Contract:** [`EMPIRICAL_SUBSTRATE_CONE_SURVEY_GATE.md`](../theory/EMPIRICAL_SUBSTRATE_CONE_SURVEY_GATE.md), frozen at `416dde1` before surveying.

**Verdict, split by what it applies to:**

- For the **scalar** variable ("is there any spacelike signalling?"):
  `DIRECT_CONSTRAINTS_FOUND` — Bell no-signalling tests bound exactly this.
- For the **directional structure** isolated in Sec. 8.10 (the window
  `ct < L < v_sub(n̂)t`, off-axis only): `NO_CURRENT_OPERATIONAL_TEST`.

## 1. The trap, stated first

The most likely misreading of this literature would be to apply
**Salart et al. 2008** (`v > 10⁴ c` for an influence in a privileged frame) or
**Bancal et al. 2012** (any finite-speed `v > c` hidden influence leads to
superluminal signalling) to our model, and conclude it is excluded — since its
influence has speed `≤ √3 c`, far below `10⁴ c`.

**That is a category error.** Those experiments constrain models in which the
superluminal influence is *responsible for* the observed quantum correlations.
In the lift of Sec. 8.10 the Bell correlations come from the ordinary quantum
state; the outside-cone tail is an extra, exponentially suppressed, **non-
explanatory** effect. Salart and Bancal bound a strictly stronger hypothesis and
do **not** bound our variable. Recording this is the main result of the survey.

## 2. Category A — direct on the exact variable

**Bell no-signalling tests.** Whether Alice's setting shifts Bob's marginal at
spacelike separation *is* `D(L,t) > 0`. The geometry is also right: Bell tests
sit just barely spacelike, `L` slightly above `ct`, which lies inside the
model's accessible window `ct < L < √3 ct`.

But the bound is weak and contested. Adenier and Khrennikov analyse the Hensen
et al. loophole-free CHSH data and report that by enlarging the event-ready
sample one can exhibit "a violation of the no-signaling principle with a
statistical significance at least similar to that of the reported violation of
the CHSH inequality, if not stronger" (abstract read directly from
`arXiv:1606.00784v3`). This is generally attributed to systematics and
post-selection, not to real superluminal influence — but it fixes the
**empirical precision**: no-signalling is verified only to finite-sample
statistics, at roughly the percent-to-permille level.

**Against a model prediction of `10^(-8.4e41)` over one second** (contract
Sec. 1), the gap is ~`10^41` orders of magnitude **in the exponent**.

## 3. Category B — indirect only, excluded by contract Sec. 2.1

LIV dispersion limits (LHAASO / GRB 221009A), `GW170817` speed comparison, the
SME data tables, vacuum-Cherenkov and threshold processes. All bound `v_g`,
dispersion or species comparison. Sec. 8 **proves** `sup|v_g| = c` is compatible
with influence outside `B(c)`, so these do not constrain the variable at all,
however strong they are. Not re-verified here; out of scope by the contract.

## 4. Category C — analogue realization, not a constraint

Lieb-Robinson experiments — Cheneau et al., *Light-cone-like spreading of
correlations in a quantum many-body system* (Nature 481, 484, 2012;
`arXiv:1111.0776`), and later trapped-ion and cold-atom work — **observe**
effective light cones with exponentially suppressed tails outside them, in
engineered lattice systems. This is the structure of Sec. 8.10 made visible, at
micron lattice scales. It is evidence that the structure is physically real and
measurable; it is **not** a constraint on nature's fundamental cone.

## 5. What this means

The scalar question is tested, but only to the precision at which Bell
experiments verify no-signalling, which is many tens of orders of magnitude
short of anything a Planck-scale substrate would produce. The **directional**
question — whether influence outside `B(c)` has the anisotropic window structure
`ct < L < v_sub(n̂)t` with exact silence on the axes — is touched by no existing
observation known to this survey.

So `c = ` fundamental causal boundary is, in the operational sense isolated in
Sec. 8.10, **not merely unproved but essentially untested**; and by the
falsifiability asymmetry it cannot be established by null results anyway.

## 6. Evidence tags

- Adenier–Khrennikov abstract: **verified from primary PDF**.
- Salart 2008, Bancal 2012, Cheneau 2012: identified via search; abstracts and
  headline numbers **not re-verified against the primary sources**. Tagged
  `SUPPORTED`, adequate for the classification made here (which turns on what
  variable each constrains, not on its numerical value), **not** for citing any
  number as established.
- The `10^(-8.4e41)` figure is ours, computed under the contract's premise.

## Sources

- [Bancal et al., *Quantum non-locality based on finite-speed causal influences leads to superluminal signalling*, Nature Physics (2012)](https://www.nature.com/articles/nphys2460) — [arXiv:1110.3795](https://arxiv.org/abs/1110.3795)
- [Salart et al., *Testing the speed of 'spooky action at a distance'*, Nature 454, 861 (2008)](https://www.nature.com/articles/nature07121) — [arXiv:0808.3316](https://arxiv.org/abs/0808.3316)
- [Adenier & Khrennikov, *Test of the no-signaling principle in the Hensen loophole-free CHSH experiment*, arXiv:1606.00784](https://arxiv.org/pdf/1606.00784)
- [Cheneau et al., *Light-cone-like spreading of correlations in a quantum many-body system*, Nature 481, 484 (2012)](https://www.nature.com/articles/nature10748) — [arXiv:1111.0776](https://arxiv.org/abs/1111.0776)
