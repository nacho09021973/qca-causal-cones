# Thirring composition line: documentary balance

2026-11-17. Author: Claude (Anthropic), claude-opus-5-5. DRAFT.
User «si adelante» to the proposal of a documentary balance (option 5 of
the session list), drafting only. No calculation, verifier, contract,
external transmission or promotion. Branch
`research/thirring-isolated-spectator`, base commit `b13cca9`.
Purpose: give the user the facts needed to decide whether to continue,
close or redirect the successive-collision line. The decision is the
user's; Sec. 5 is an author recommendation, not a result.

## 1. Known, question, abandonment criterion

Known (sources below, all read in this session): A5 is ESTABLISHED
conditional on F; the isolated spectator corollary is ESTABLISHED in its
frozen scope, conditional on H_pair; the two-collision geometry is a
DRAFT with status OPEN_MISSING_BOUND; the delayed (3,-2) bridge attempt
stopped OPEN_MISSING_BOUND and its single authorized attempt is spent.

Question: what can the successive-collision line yield for the project
question (coexistence of universal quantum computation and a
relativistic low-energy regime under one fixed rule), in the declared
code and resources, if every open obligation were closed?

Abandonment criteria already frozen for the line (none triggered):
the draft abandons the construction if the fixed geometry cannot supply
the isolated windows, or if persistent leakage or a different limiting
map is proved (`theory/THIRRING_TWO_SUCCESSIVE_COLLISIONS_DRAFT.md`,
"Known, question and abandonment"); the bridge contract abandons on
demonstrated nonzero asymptotic leakage or a different gate
(`theory/THIRRING_3_MINUS2_WINDOW_BRIDGE_GATE.md`). OPEN_MISSING_BOUND is
a stop, not an abandonment.

Missing so far: an abandonment criterion relative to the project question.
Proposed here for the user to accept or reject: abandon the composition
line as a coexistence line if, in the declared architecture, its best
possible outcome is a statement already known conditionally (Sec. 2).
By Sec. 2 this proposed criterion is met; it would not be met if the A5
scope reading of Sec. 2 is wrong, or if F were shown to fail with a clean
non-matchgate logical map.

## 2. What A5 already fixes

`state/CURRENT_STATE.md:5-31`, `theory/THIRRING_MATCHGATE_A5_GATE.md:93-95`,
`reports/2026-11-14--thirring-matchgate-a5.md:274-289`:

- F (premise, OPEN): the N-packet logical map in the limit is the ordered
  product of the crossing gates G_j = s_j P V(r_j), with leakage -> 0.
- Under F, at chi = pi/2, flavour code, product flavour inputs, final
  flavour readout, no ancilla, intermediate/adaptive measurement,
  postselection or control: each crossing is an allowable matchgate and
  the circuit is classically simulable (Valiant; Terhal-DiVincenzo;
  Jozsa-Miyake, pages cited there). Efficient universality by crossings
  alone in this architecture would imply BQP in P.
- Explicitly not covered: chi not congruent to pi/2 mod pi (there P V is
  not a matchgate for r != 1, and universality is not addressed); other
  resources (ancillas, intermediate or adaptive measurement, non-product
  inputs); other codes; non-factorized evolutions; finite mu.

Consequence for the line: in this architecture, proving F can only remove
the condition from a negative result. It cannot produce a positive
coexistence result. If F fails, the failure mode matters: leakage or a
non-limiting map would be a negative for the code; a different but clean
logical map would reopen the question.

## 3. Where the composition line stands

- Isolated spectator (`state/CURRENT_STATE.md:3932-3954`): one pair
  collision with a third, non-participating packet, K = (3,1,-2), T = 20L.
  REDUCES_TO_EXISTING_RESULTS, conditional on H_pair. This is the one-crossing
  case of F with a spectator, not a composition.
- Two successive collisions (`theory/THIRRING_TWO_SUCCESSIVE_COLLISIONS_DRAFT.md`;
  `state/CURRENT_STATE.md:3956-3968`): geometry selected, DRAFT, windows
  [0,20L] and [2 floor(27L/2), 28L]; crossing order (3,1), then (3,-2);
  (1,-2) crosses later. Three obligations open:
  1. the (3,-2) bridge in the delayed window;
  2. a free-gap estimate between windows;
  3. finite-mu admission of the second window.
- (3,-2) bridge (`theory/THIRRING_3_MINUS2_WINDOW_BRIDGE_GATE.md`;
  `reports/2026-11-17--thirring-delayed-bridge-lean-attempt.md`):
  OPEN_MISSING_BOUND. Only a conditional Lean transfer lemma compiles
  (`formal/ThirringWindow/Transfer.lean`); the comparison state and
  delayed-window tail bounds are not constructed. The contract allowed one
  bounded attempt; continuing needs a new charter.

Distance to F: even all three obligations closed give two ordered
crossings in one fixed geometry (and still not the later (1,-2) crossing).
F is a statement for N packets and arbitrary crossing sequences. No
inductive scheme from two windows to N is written in the repo
[UNVERIFIED that none exists elsewhere; not searched beyond the files
cited]. Each extra window, so far, has needed its own bridge.

## 4. Budget history

`state/CURRENT_STATE.md:304-307, 339-356`: the 2026-11-09 decision fixed
two further Thirring coexistence contracts with mandatory closure; the
budget was declared exhausted and the line stopped as OPEN. Later
Thirring contracts (flavour, co-moving, A5, spectator, bridge) were each
authorized explicitly by the user (e.g. line 154: «not a budget reset»).
Q4-A (rule-only resources) is recorded as binding for «the next
contract» of that decision; whether it still binds a new contract with
ancillas or measurement is a user decision.

## 5. Options for the user

A. **Continue F in this architecture.** Next step would be a new charter
   auditing obligations 1-3 together (session option 2), then the bridge
   proof. Yield at best: two-crossing composition, a step towards an
   unconditional matchgate-simulability statement in this code and these
   resources. Does not advance coexistence positively. Cost: several
   analytic gates, each needing review.

B. **Close the composition line as OPEN.** Record: A5 conditional on F
   stands; spectator corollary stands; two-collision draft and (3,-2)
   bridge stop OPEN_MISSING_BOUND; no Thirring no-go. Cost: one state
   entry.

C. **Move to a case A5 does not cover, still under F as a premise.**
   E.g. chi not congruent to pi/2 mod pi, where P V(r) is not a matchgate.
   The first question would be exact algebra: do the gates available from
   admissible rapidity ratios generate a universal set on the flavour
   register? Caveats: the promoted pair bridges and the flavour code are
   at chi = pi/2 only [their extension to other chi is UNVERIFIED]; the
   user criterion of 2026-11-14 (`state/CURRENT_STATE.md:179-180`) asks
   first for a physically well-defined logical operation. A positive
   algebraic answer would be conditional on F and on new bridges.

D. **Change resources or code** (ancillas, measurement, non-product
   inputs, another code or model). Requires a new contract and a decision
   on Q4-A. Broadest option; highest risk of scope drift.

Any option chosen needs, in its charter and before any computation, the
three points: what is known (with source), the concrete question, and
the result that forces abandoning that line. Proposed starting points:

- A: known Secs. 2-3; question = obligations 1-3 for the fixed geometry;
  abandon on the frozen criteria above (leakage, different map, windows
  not isolated).
- C: known Sec. 2 plus the co-moving Part A algebra; question = whether
  the gates from admissible rapidity ratios at the chosen chi generate a
  dense subgroup on the flavour register; abandon if they are proved to
  lie in a proper closed subgroup, or if no pair bridge can be admitted at
  that chi.
- D: to be fixed in its own charter; it cannot start without the three.

Author recommendation (opinion, not a result): B now, then decide between
C and stopping the Thirring coexistence line. A is justified only if an
unconditional negative in this specific architecture is itself wanted as
a deliverable (e.g. for the paper), since its best outcome is already
known conditionally.

## 6. Not claimed

No new mathematical statement; no change to any status in
`state/CURRENT_STATE.md`; no claim that F is true or false, that the
(3,-2) bridge fails, that crossings at other chi are universal, or of
novelty. F = OPEN; COEXISTENCE = OPEN; NOVELTY = OPEN.

## 7. User decision — 2026-11-17

User «acepto el criterio, commit y registra B». The proposed abandonment
criterion of Sec. 1 is accepted, and option B is adopted: the composition
line (two successive collisions, delayed (3,-2) bridge) is closed as a
coexistence line, status OPEN_MISSING_BOUND at stop. A5 conditional on F
and the isolated spectator corollary keep their promoted scope. No
Thirring no-go; F, coexistence and novelty OPEN. Choice between option C
and stopping the Thirring coexistence line is pending; nothing further is
authorized by this decision. Sec. 6 refers to the balance as drafted; the
status change is recorded in `state/CURRENT_STATE.md` with this decision.

## 8. Correction to option C and user decision to stop — 2026-11-17

Correction (author, after a Codex comment pasted by the user): the order
proposed for option C in Sec. 5 was wrong. Consistent with the user
criterion of 2026-11-14 (`state/CURRENT_STATE.md:179-180`), a C contract
must first ask whether a physically well-defined gate exists at one fixed
chi (pair bridge admitted at that chi, leakage -> 0), and only then
whether the available gates are universal. Not being a matchgate does not
imply universality. A positive result under C would rest on two open
conditions: new pair bridges at that chi (the promoted ones are at
chi=pi/2 only) and F. Proposed abandonment criterion for such a
contract: demonstrated nonvanishing asymptotic leakage, or no pair bridge
admissible at that chi.

User decision: «si» to stopping the Thirring coexistence line. Status
OPEN; no Thirring no-go. Option C is not chartered; if reopened, it starts
from the bounded question above under a new contract.
