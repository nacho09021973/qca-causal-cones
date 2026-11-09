# S19 trace proof: execution and review record

Date: 2026-11-05. Author: Codex (OpenAI).
Repository baseline HEAD: 7e7bf7d0eec38b6ad0fc4a46872b2a90ed71db03.
Branch: research/schur-stability-audit. New artifacts have not been committed.
Unrelated pre-existing untracked directory
`debates/2026-11-04--ph-refutation-hex-s25-review-astra/` is untouched.

## Local exact verification

Command: `python3 -B scripts/verify_hex_trace_s19.py`.
Result: exit 0, 14/14 exact checks (SymPy; no floating-point computation).
Environment: Python 3.12.3, SymPy 1.14.0.
Permanent stdout: `reports/2026-11-05--hex-trace-s19-verifier.txt`.
Verifier SHA256:
`00505fe6fa67d579e1b5d3bb98dec34264939c37b407ef8b08d3d3959590e959`.
S19 proof SHA256 submitted for review:
`7ce0e1cec365c24ec6b8ca16f20c7c29db48dc2a33f7170b3537ba6b54f52cb4`.

The first verifier run returned 13/14 because it compared the syntactic
form of an inequality returned by SymPy. Comparing the exact solution
sets as intervals repaired that check; the final run and its saved stdout
are 14/14. No scientific formula changed because of that failure.
The second contradiction point is an exact alternative to the supplied C
evaluation: p=2q, cos q=3/5 gives -1997/1875.

## Independent review provenance

Authorized in this session by «autorizado, adelante» after the explicit
proposal to submit the proof for independent review. Tool: revision-ciega
from PATH, herramientas commit
`ce09890a0d5f68a6634f358eff2e477ac5f15ec7`.

Attempt 1: `debates/2026-11-05--hex-trace-s19-review-deepseek/`.
Operational FAILED, exit 6, DNS could not resolve api.deepseek.com inside
the sandbox. No report; not a scientific rejection and not a review.

Network retry: `debates/2026-11-05--hex-trace-s19-review-deepseek-network/`,
separate preserved folder, explicit sandbox escalation approved. Model
requested: deepseek-v4-pro. The launcher records exact sealed input,
input hash, provider finish state and tool provenance. Scope: S19 proof
and its analytic rigidity input; the general scalar-method analysis is
not submitted.

Completed 2026-11-05, 09:16:25--09:37:21 UTC; operational COMPLETED,
exit 0, provider finish_reason `stop`, returned model deepseek-v4-pro.
Scientific verdict: **PASS on all six requested blocks, no mandatory
repairs**. The reviewer re-derived the algebra and accepted the analytic
bridge, including the use of normal rigidity beyond minimal support.
It did not execute the verifier. This is one cross-family model review,
not human review or independent execution.

The S19 report's status header was updated after review; its mathematical
body and the verifier bytes were not changed. The reviewed input is
preserved exactly in `entrada_deepseek.txt`, hash
`de612d487c509b9c958d7b9642911fc8440b1486c221e7706322755ca5b803b3`.
Author response: `verificacion_autor.md` in the completed review folder.
No repair re-review was needed. The general scalar-method report is
PRELIMINARY and independently unreviewed.

No scientific promotion, CURRENT_STATE edit, commit or push is performed
by this record. The old promoted S19 result and certificate are unchanged.
