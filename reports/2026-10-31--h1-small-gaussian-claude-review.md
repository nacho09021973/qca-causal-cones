# Independent Claude review of the small Gaussian profile proof

Date: 2026-10-31. Branch: `research/schur-stability-audit`.
Candidate base: `11ea2d89310c025ec40e78b0fe2ea1cf75e29612`.
Review status: **INDEPENDENT_REVIEW_PASS / NO_MANDATORY_REPAIRS**.
Canonical promotion: **NOT_PERFORMED**.

The user explicitly requested «que lo revise claude», after receiving the
candidate proof. This authorizes this external review, superseding the
contract's earlier no-external-submission clause for this request only.
It does not authorize publication or automatic canonical promotion.

## Execution and independence

One sealed `revision-ciega opus` execution was requested, at most 900 s.
It completed normally: `claude-opus-5-5`, effort high, Claude Code 2.1.316,
2026-10-31 18:01:22–18:06:53 UTC, exit 0, final successful result.
The startup record reported no tools. Tools commit:
`ce09890a0d5f68a6634f358eff2e477ac5f15ec7`.

The [unaltered review](../debates/2026-10-31--h1-small-gaussian-claude-review/informe_opus.md),
[request](../debates/2026-10-31--h1-small-gaussian-claude-review/prompt.md),
[exact input](../debates/2026-10-31--h1-small-gaussian-claude-review/entrada_opus.txt),
raw provider stream and operational state are retained. `COMPLETED`
describes execution, distinct from the mathematical verdict below.

The author is Codex (OpenAI), reviewer Claude (Anthropic): one independent
cross-family agent review. It is not human review, multi-member consensus,
or a new review of every baseline result. The reviewer reads the verifiers
as text and explicitly does not claim to have run them or checked their
recorded execution counts.

## Reviewed snapshot

| Input | SHA256 |
| --- | --- |
| Candidate proof | `98e96a47fdb584e921210e71c07559b773a2bd85258ab8fc1606ac6bc5972611` |
| Corrected preregistered contract | `d739db6b4b476c79c4a51d9a26f0dcf03dda31b5c3d818b8b0d040f6e972cddd` |
| T1 definitions | `c320aaa5060f343f1f0e726f663058f62fb6c1d2f19f71da43ef4bd759e24e8d` |
| Promoted bridge | `caee6fa254fd83d64ac16ce6de2f04b359087e9a8f1668b0d4f93a089589bf65` |
| Current manuscript | `a3849451dbac2d3e3a68ace47b0b50ae2bbf5ae3f6902c8bc92b9c2d820a42c5` |
| Small-profile algebra verifier | `5647b1d52cce9392bac6d239ae4dd40b31b147b1e3541ee170b08c475990cfa2` |
| Flat Laplace verifier | `d008417debe149743396bfbeb7d55be11fe7aa00bce3b4aecebf6a50997884b2` |

Complete input SHA256:
`60df1c1e292ee78ff8416cad02addae2cccc391bb0c6d24ac3565c4acf5850b1`.
Provider stream SHA256:
`fc5f5d4c840ec5aabb626950311279d7fd9f9dd5beb0c02748087e8824850906`.
The reviewed candidate and all submitted scientific sources are unchanged
after review. Their historical pending-review headers refer to their
pre-review snapshot; this report records the later evidence.

## Mathematical verdict

| Block | Claude verdict |
| --- | --- |
| PROFILE_AND_PARITY | PASS |
| FIRST_CORRECTION | PASS |
| INTEGRATED_KERNEL | PASS |
| SCALE_BOUND | PASS |
| FULL_SIGNAL_SURVIVAL | PASS |
| SCOPE_AND_CODE | PASS |

Global verdict: **PASS**, conditional on the promoted Schur bridge and
the accepted flat sigma_2/I theorem. The reviewer checks their hypotheses
and application; it does not recertify their complete baseline proofs.
Mandatory repairs: **none**.

The accepted proof includes the exact evenness and quadratic correction
formula, the integrated tilted-kernel norm `O(N^-3/2)` over all eight
saddles, complete physical endpoint layer masses, and the uniform bound
`|F_N(epsilon)-F_N(0)| <= C epsilon^2 N^-13/2 exp(-K_*N)`.
It accepts uniform bridge constants on `|epsilon|<=1` for fixed W and hence
the existence of epsilon_0>0 and N_0<infinity such that for every
`|epsilon|<=epsilon_0`, `N>=N_0`, full L_+ is negative and
`|L_+|=Theta(N^-13/2 exp(-K_*N))`. The smaller-scale upper bound for L_-
is also accepted. No continuity argument valid only at fixed N substitutes
for these uniform estimates.

## Nonblocking comments and limits

Claude recommends naming the uniform-constant argument as an explicit
lemma, reducing notation collisions, noting the sharper fourth-order real
Taylor remainder, spelling out the equivalent positive Hessian formula,
and clarifying the Fourier pushforward sign convention. It labels these
nonblocking. No changes are applied to the reviewed scientific snapshot.

It also notes that two algebra checks are tautological and do not prove
the analytic bounds. Its PASS is based on the written mathematical proof,
not the check count. The review does not independently reproduce the
21-check or 58-check executions recorded by the author.

Open: sign/nonvanishing of the quadratic coefficient Q_N, a full
nonzero-epsilon asymptotic coefficient, and effective numerical epsilon_0
and N_0. No broader profile/pair class, general H1/H1c, E0,
POWER_13/2_STABILITY, E/AdS, physical implementation or novelty is certified.

## Recording without promotion

The canonical ledger records completion of the requested review only.
The scientific gate is not automatically promoted, and no main-branch
change, commit, push or publication follows from this review request.
No scientific code or candidate text is modified. Checks: completed final
provider result, frozen-source hashes and `git diff --check` for authored
changes. The original review/stream bytes, including any trailing whitespace,
are retained without editorial changes.

## Verifier reproduction — 2026-11-01

Added after the review, by Claude Code (Opus 5.5) at the user's request.
It reproduces the recorded check counts outside the author's run; it is
not a second review and certifies nothing beyond each script's README scope.

Base commit `11ea2d89310c025ec40e78b0fe2ea1cf75e29612`, 2026-11-01 UTC,
Python 3.12.3 in a fresh virtual environment with the pinned
`sympy==1.14.0`, `numpy==1.26.4` (the system interpreter is externally
managed and has no SymPy). Both scripts run from the repository root with
`python -B`; script bytes match the reviewed snapshot.

| Script | SHA256 | Result |
| --- | --- | --- |
| `scripts/verify_small_gaussian_profile_algebra.py` | `5647b1d52cce9392bac6d239ae4dd40b31b147b1e3541ee170b08c475990cfa2` | exit 0, 21 `[PASS]`, 0 failures |
| `scripts/verify_regional_laplace_coefficient_gate.py` | `d008417debe149743396bfbeb7d55be11fe7aa00bce3b4aecebf6a50997884b2` | exit 0, 58/58, 0 failures |

The algebra verifier still prints "analytic survival proof remains
unreviewed": that string is frozen in reviewed bytes and predates this
review; it is not changed. As the reviewer noted, neither count certifies
the analytic estimates.
