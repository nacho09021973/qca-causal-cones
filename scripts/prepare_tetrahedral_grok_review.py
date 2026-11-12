"""Prepare a reproducible review-only snapshot; no scientific calculation.

Retain mathematical derivations and definitions, omit prior review verdicts.
The manifest records source/output hashes and exact section selectors.
"""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'reports/reviews/2026-11-10-tetrahedral-ir-signal-grok'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    if any((OUT/name).exists() for name in ('grok.json','grok.log','estado_grok.json','informe_grok.md')):
        raise RuntimeError('Review artifacts already exist; do not overwrite a submitted input.')
    selectors = [
        ('reports/2026-11-10--tetrahedral-fable-local-audit.md',
         '## 1. Exact inputs checked independently',
         '## 7. Validation and what remains outside this audit', 'proof_candidate.md'),
        ('theory/TETRAHEDRAL_IR_SIGNAL_GATE.md', '## Fixed model, conventions and geometry',
         '## Stages and outcomes', 'protocol_definitions.md'),
        ('theory/POLYHEDRAL_CORONA_TETRA_PREFLIGHT_GATE.md', '## Frozen model and scope',
         '## Bounded execution', 'walk_definition.md'),
        ('papers/ir-corona/ir-corona.tex', r'\subsection{Infrared admissibility}',
         r'\begin{lemma}[Single-site operations are ultraviolet]', 'ir_admissibility_definition.tex')]
    entries = []
    for source, start, end, target in selectors:
        data = (ROOT/source).read_bytes()
        text = data.decode('utf-8')
        begin = text.index(start)
        stop = text.index(end, begin)
        selected = text[begin:stop]
        # Exclude the previous executed-checks paragraph as well as its verdict.
        if target == 'proof_candidate.md':
            selected = selected[selected.index('Checks cover'):]
            selected = '# Mathematical proof candidate for independent review\n\n'+selected
        encoded = selected.encode('utf-8')
        (OUT/target).write_bytes(encoded)
        entries.append(dict(source=source,source_sha256=digest(data),start_inclusive=start,
                            end_exclusive=end,output=target,output_sha256=digest(encoded),
                            note='For proof_candidate only: exclude initial executed-checks paragraph and prepend neutral title.'))
    manifest = dict(purpose='Review preparation only, no new mathematical result.',
                    git_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
                    working_tree=True,previous_verdicts_attached=False,entries=entries,
                    script_sha256=digest(Path(__file__).read_bytes()))
    (OUT/'input_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(OUT)


if __name__ == '__main__':
    main()
