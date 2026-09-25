# EMPIRICAL_SUBSTRATE_CONE_SURVEY — outcome

**Contract:** [`EMPIRICAL_SUBSTRATE_CONE_SURVEY_GATE.md`](../theory/EMPIRICAL_SUBSTRATE_CONE_SURVEY_GATE.md), frozen at `416dde1` before surveying.

**Verdict, in three levels** (revised 2026-09-16 after review; see Sec. 7):

| | |
| --- | --- |
| **Scalar no-signalling** | experimentally tested, to finite precision |
| **Directional causal tail of Sec. 8.10** | no specific localized operational test |
| **Exact equality `C_fundamental = B(c)`** | **not established** by null results |

In contract categories: `DIRECT_CONSTRAINTS_FOUND` for the scalar variable,
`NO_CURRENT_OPERATIONAL_TEST` for the directional structure — subject to the
missing coupling map of Sec. 7, which blocks any *quantitative* transfer from
the former to our `D`.

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

Adenier and Khrennikov analyse the Hensen et al. loophole-free CHSH data and
report that by enlarging the event-ready sample one can exhibit "a violation of
the no-signaling principle with a statistical significance at least similar to
that of the reported violation of the CHSH inequality, if not stronger"
(abstract read directly from `arXiv:1606.00784v3`).

**Correction to the first version of this report.** That paper was used here to
assert that "the real empirical level is percent-to-permille". **That was an
overreach and is withdrawn.** It is a contested reanalysis of one dataset,
attributed by others to systematics and post-selection; it is neither a
universal bound nor a calibrated confidence interval for our `D`, and the
interpretation of such marginal deviations is itself under discussion in the
later literature. What it does establish is weaker and still useful:
no-signalling is verified **to finite statistical precision on specific
datasets**, not exactly. No numerical empirical level is claimed by this survey.

Whatever that level is, it is separated from a model prediction of
`10^(-8.4e41)` over one second (contract Sec. 1) by a margin no plausible
tightening could close.

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

The scalar question is tested, to finite precision. The **directional** question
— whether influence outside `B(c)` has the anisotropic window structure
`ct < L < v_sub(n̂)t` with exact silence on the axes — is touched by no existing
observation known to this survey.

The conclusion is therefore **not** "essentially untested" (an earlier, looser
phrasing, withdrawn) but the sharper:

> **The exact equality `C_fundamental = B(c)` is not established experimentally.**

**Epistemological asymmetry, taken as firm.** No finite sequence of null results
can prove `D = 0` exactly; it can only produce ever smaller upper bounds. A
reproducible positive result outside `B(c)` could, by contrast, falsify the
identification of `c` with the fundamental causal boundary.

## 6. The missing coupling map — the real obstacle

Sec. 8.10 gives `[A(t), B] ≠ 0`, hence `∃` a state and an intervention with
`D > 0`. It does **not** give that the particular protocol of a standard Bell
test is that intervention. Converting an experimental bound on Bell marginals
into a quantitative bound on the tail of the lift requires a
**coupling/protocol map**: which physical observable realizes `A`, which
realizes `B`, and which preparation actually exploits the commutator.

No such map exists here. Until it does, the scalar bound constrains the right
*kind* of variable but cannot be converted into a number about our `D`. This,
not the size of the effect, is what blocks the empirical question.

## 7. Revision note

The first version of this report (`5b6f6c4`) was revised after review on two
points: the withdrawn percent-level claim in Sec. 2, and the sharpening of
Sec. 5 from "essentially untested" to the exact-equality statement. The
classification of Salart/Bancal as a category error (Sec. 1) is unchanged and
was the survey's main result.

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
