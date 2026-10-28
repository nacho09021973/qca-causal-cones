<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ 352f6c8aacaefa57b9aeee415dbecc3f6249f01e; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 f363e072101d7766d1075b6f4a24e3fc84dc92e541016af9ccd448a5e2108db4; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: claude-opus-5-5, esfuerzo: high, vía: claude -p sellado (2.1.312 (Claude Code))
opus.json sha256 9ad2d5dc65dca9ca85aa588fed75ab08a8fdf083a04ff89ba810bb268e1fbd02
inicio: 2026-10-28T10:36:08Z  fin: 2026-10-28T10:38:13Z
documento: /home/ignac/herramientas/pruebas/ai_scientist/qca_2026-10-28/call_02/request.json ; último commit observado: sin versionar ; sha256 de la copia enviada ca520a22741bf90f34b9bdd9dc4758bd60a6ec7d9a38929c490101a887820245
entrada_opus.txt sha256 7b13ed16f6d452979d492d84ca3a45596456980f783ab132114ae8bbcc2ab385
respuesta sha256 277ec818da6201de86af2ce5f42a9cd33ae22b90c160d07fb935dd8a67d7cb47
-->

THOUGHT:
Round-2 attack on the Round-1 proposal against the three required criteria. Everything below is an unchecked algebra sketch written in this response, at PRELIMINARY level at most. Nothing was executed, and none of it is a result for the record.

- **Circularity: passes.** T_1(tau) is defined by coefficient bounds, independently of U.
- **Auxiliary preparation: passes.** No preparation criterion is used.
- **Overlap with the Gaussian obstruction: fails, and the Round-1 repair mislocated the gap.** Round 1 said the live content starts at the arc/Jensen template's threshold, where the phases of D_E begin to matter. That is wrong.
  - Write f = lambda exp(-i theta B) g on one link, with the other variables fixed and B = a z + b/z + c.
  - Multiplying by exp(-i theta a z) shifts the Phragmen-Lindelof indicator exactly by a cosine of amplitude |theta a|.
  - The standard property h(t) + h(t+pi) >= 0 for nonzero functions of exponential type [UNVERIFIED in this session; edge cases with polynomial or zero analytic parts unchecked] then forces tau >= |theta a|/2.
  - Optimizing the arcs in the Jensen template reaches only |theta a|/pi. The step from there to |theta a|/2 uses growth alone and needs no D_E.
  - The bound is saturated by g = exp[i theta (a z + b/z)/2], f = exp[-i theta (a z + b/z)/2]. This is a half-angle version of the §3.D control.
  - So tau* is elementary, and the proposed second check (Polya indicator on a single-link control) uses the same calculus as the first. It is not logically distinct.
- **Above the threshold, the question is arithmetic, not analytic.** In the single-link toy (fermions frozen, D_F omitted), take the D_E angle alpha = pi. The chirp exp(i alpha E²) becomes the parity z -> -z, and the half-angle g above is an exact eigenvector of D_M D_E with lambda = 1.
  - So any T_1 rejection must use the arithmetic of alpha = epsilon² g_E²/2 (UNVERIFIED extraction, nominally 1/2), coupled to D_F and Gauss.
  - That is a kicked-rotor-type Diophantine problem with factorial tails. It is much harder than Round 1 rated.
  - The kicked-rotor analogy [UNVERIFIED] suggests that genuine eigenvectors at non-resonant alpha, if they exist, have exponential tails outside T_1.
  - So a successful rejection would most likely exclude a class that the plausible references are not in. That is close to the "state already excluded or irrelevant" failure the brief warns about.

Repair was considered: drop the tau* sub-goal and keep only the alpha-arithmetic question. It would keep a near-vacuous outcome, lower feasibility, and sit two steps removed from A.int. That does not justify a calculation charter. **Decision: withdraw.** No replacement candidate is proposed; choosing the next reference-state question returns to the user. The ratings are unverified self-assessments, not evidence or gate verdicts. The pending DeepSeek re-review is not anticipated.

NEW IDEA JSON:
```json
{
  "Name": "eon_exponential_type_tail_threshold_withdrawn",
  "Title": "WITHDRAWN: exponential-type tail-class stationarity test for Eon v4 references (A.int)",
  "Experiment": "WITHDRAWN AT ROUND 2. No calculation charter is recommended. Nothing was executed; experiment.py is a placeholder and is unused. The sketches below are unchecked author-side algebra written in this response, PRELIMINARY at most, and must not enter CURRENT_STATE as results. (1) What was proposed: in the frozen finite-volume Eon v4 Gauss sector (arXiv:2205.03148v4 eqs (34)-(37), U = D_M D_E D_F, exact magnetic exponential (21)/(36), untruncated integer rotors, L>=3 torus, epsilon=1, m=pi/4, g_E=g_M=1, G_x = div E_x + N_x - 2 = 0), decide whether any pure eigenvector of U has electric Fourier series of finite exponential type tau (class T_1(tau)). Also locate the threshold tau* below which the arc/Jensen template of report section 3, as repaired in the unreviewed 2026-10-28 addendum, already excludes eigenvectors. (2) Reason for withdrawal A, the threshold sub-goal is not a research question: on one link with the other variables fixed and B = a z + b/z + c, the multiplier exp(-i theta a z) shifts the indicator exactly. The property h(t) + h(t+pi) >= 0 [UNVERIFIED; edge cases unchecked] then gives tau >= |theta a|/2. This is saturated by g = exp[i theta (a z + b/z)/2], f = exp[-i theta (a z + b/z)/2], a half-angle form of the report section 3.D control. The Round-1 claim that D_E matters from the template threshold onward was wrong. The proposed second check used the same calculus and was not logically distinct. (3) Reason for withdrawal B, the live region is arithmetic: in a single-link toy (fermions frozen, D_F omitted, a control only), D_E angle alpha = pi turns the chirp into the parity z -> -z, and the half-angle g is an exact eigenvector of D_M D_E. Any rejection at the frozen alpha = epsilon^2 g_E^2/2 (extraction UNVERIFIED) therefore requires Diophantine control of alpha coupled to D_F and Gauss. (4) Reason for withdrawal C, vacuity: the kicked-rotor analogy (Casati-Chirikov-Ford-Izrailev; Fishman-Grempel-Prange; all UNVERIFIED) suggests that eigenvectors at non-resonant alpha, if any, have exponential tails, outside T_1. A full T_1 rejection would most likely exclude a class that contains no plausible reference. It would add nothing to physical selection, vacuum existence, point spectrum or A.int. (5) What remains usable, without promotion: the observation that growth hypotheses alone cannot exclude exponential type >= |theta a|/2 per link, and that beyond it only the arithmetic of the D_E angle can. This is a scoping note on the existing Gaussian obstruction, dependent on that obstruction's unreviewed addendum template. It is not a new obstruction. (6) Not done and not authorized: no replacement candidate, no exponential-tail or spectral-classification follow-up, no vacuum, correlator, speed, loop or gate promotion, no anticipation of the pending DeepSeek re-review. Any next reference-state question requires a new user decision and its own charter.",
  "Interestingness": 2,
  "Feasibility": 3,
  "Novelty": 2
}
```
