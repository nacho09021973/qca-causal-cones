# Responses to Fable — work in progress

Author: Codex, 2026-11-10. Review preserved unchanged, SHA256
5700c53ee1c86007ed7194233a8c2d0ab7b93d7e6b25e310bbb15d9b31a339e3.
Responses are author repairs, not independently resolved objections.

Known: Fable identifies missing proof details and scope overclaims.
Question: can each objection be answered from the existing definitions
and primary evidence? Stop criterion: any unsupported step stays open;
no promotion or external delivery follows from author repairs.

Applied to authoritative TeX so far:

- C1: explicit Hessian positivity and extension across the origin,
  justifying attainment of the Legendre supremum.
- C6: operator-norm ratio distinguished from pointwise output fractions.
- I1–I3: scope of infrared control, recorded hard-cutoff cancellation,
  second saddle and dependence on profile vanishing order disclosed.
- L1–L2: upper-bound formalization qualified; ellipse inclusion separated
  from the unformalized boundary characterization.
- C7: removed the inference of an exact-signal accuracy threshold from
  the semi-analytic diagnostic.

## Continuation: author responses completed in the manuscript

C2: wrote the third-derivative variation estimate, uniform absolute control
at zero depth, reciprocal-lattice summability and weighted depth bounds.
C3: supplied derivative bounds for the exact band-limited free tail via
its Fourier interpolation and the Leibniz rule.
C4: stated transport to all eight half-period points and exponential
suppression of the reciprocal eigenvalue branch on small neighbourhoods.
C5: supplied a bound-only fourth-order profile argument: Alice layer
N^(-9/2), Bob layer N^(-5/2), Gaussian measure N^(-3/2), yielding N^(-17/2).
These are written author arguments, not machine-certified analytic lemmas.

C6: abstract paraphrase repaired as well as the definition's explanation.
C7: diagnostic limitations now stated explicitly, and accuracy-threshold
claims removed from abstract, introduction and discussion. No new data.
L1/L2: README and both manuscript versions qualified. Theorem numbering
in formal/README.md corrected to rate 4.3 and leading asymptotic 4.4.

N1: directly read sources/2408.02108v1.pdf pp. 17–18, equations
(5.19)–(5.21). With ell=2 sqrt(3)t, R_tilde(ell)=2 Phi(tu);
at r=sqrt(3)-1/2 the diagonal Legendre expression is twice K_*.
Added explicit attribution. This verifies the v1 relation, not identity
of equation numbering or wording in the published version.

TeX and Markdown mathematical additions synchronized. pdfLaTeX compilation
and git diff --check passed. Review SHA256 remains unchanged. No certificate
or Lean source was edited; no new diagnostic, certificate run or Lean build.

## Remaining obligations

All responses above have status RESPONDED_BY_AUTHOR, not independently
resolved. Section 7 as repaired requires another-family or human review.
OPEN: compare CJWW with the published text; obtain/read the three originals
missing from Fable's review; independently check priority and the remaining
unverified claims in its Sec. 1.3; fix delivery snapshot/archive and decide
what reproducibility run is necessary. The historical readiness hashes
identify the earlier reviewed draft, not this revised manuscript.
No publication, transmission, commit or push performed.
