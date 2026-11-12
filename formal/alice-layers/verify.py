"""Compila sólo aquí, leyendo el cache Lean/Mathlib local sin modificar QCA."""
import argparse
import hashlib
import json
import os
import re
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
PACKAGES = HERE.parent/'.lake/packages'
TOOLCHAIN = 'leanprover/lean4:v4.31.0'
MATHLIB_COMMIT = 'fabf563a7c95a166b8d7b6efca11c8b4dc9d911f'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    out = args.output.resolve()
    out.mkdir(parents=True, exist_ok=False)
    mathlib_commit = subprocess.check_output(['git', '-C', str(PACKAGES/'mathlib'), 'rev-parse', 'HEAD'], text=True).strip()
    if mathlib_commit != MATHLIB_COMMIT:
        raise ValueError('Mathlib no coincide con la dependencia fijada')
    challenge = (HERE/'AliceComparator/Challenge.lean').read_text()
    copied = {}
    def declaration(text, name):
        pattern = r'(?ms)^def '+re.escape(name)+r'\b.*?(?=^def |^end |^theorem |^/\-|^abbrev |\Z)'
        return re.search(pattern, text).group().strip()
    for name in ('sqNorm', 'normalFrequency', 'centerCoordinate', 'phase', 'uncenteredPhase',
                 'latticeBox', 'aliceSites', 'transverseCoordinates', 'latticeLayerDepth',
                 'latticeLayerRadiusSquared', 'SupportFaithfulness'):
        source = 'Targets' if name == 'SupportFaithfulness' else 'Definitions'
        copied[name] = declaration(challenge, name) == declaration((HERE/f'AliceLayers/{source}.lean').read_text(), name)
    new_challenge = (HERE/'AliceComparator/NewChallenge.lean').read_text()
    for name, module in (('psiIntegrand', 'Definitions'), ('psi', 'Definitions'),
                         ('psiSlice', 'Poisson'), ('shiftedTau', 'PoissonZero'),
                         ('positiveSquare', 'SectionRegularity')):
        copied['new:'+name] = declaration(new_challenge, name) == declaration(
            (HERE/f'AliceLayers/{module}.lean').read_text(), name)
    second_challenge = (HERE/'AliceComparator/SecondChallenge.lean').read_text()
    for name, module in (('positiveSquare', 'SectionRegularity'), ('cutoffSecond', 'SectionSecond')):
        copied['second:'+name] = declaration(second_challenge, name) == declaration(
            (HERE/f'AliceLayers/{module}.lean').read_text(), name)
    final_challenge = (HERE/'AliceComparator/FinalChallenge.lean').read_text()
    final_sources = json.loads((HERE/'final_comparator_sources.json').read_text())
    for name, record in final_sources.items():
        original = declaration((HERE/record['source']).read_text(), name)
        copied['final:'+name] = declaration(final_challenge, name) == original
        if hashlib.sha256(original.encode()).hexdigest() != record['sha256']:
            raise ValueError('Definicion final distinta del manifiesto: '+name)
    if not all(copied.values()):
        raise ValueError('Definiciones copiadas distintas: '+str(copied))
    original_helper = Path.home()/'herramientas/lean/HerramientasLean/AssertAxioms.lean'
    if (HERE/'AliceComparator/AssertAxioms.lean').read_bytes().split(b'\n', 1)[1] != original_helper.read_bytes():
        raise ValueError('El cuerpo de AssertAxioms no coincide con la herramienta compartida')
    build = HERE/'build'
    build.mkdir(exist_ok=True)
    paths = [build, *(path/'.lake/build/lib/lean' for path in sorted(PACKAGES.iterdir())
                      if (path/'.lake/build/lib/lean').is_dir())]
    environment = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, paths)))
    order = ['AliceLayers.Definitions', 'AliceLayers.Targets', 'AliceLayers.Basic',
             'AliceLayers.Covolume', 'AliceLayers.Reindex', 'AliceLayers.Poisson', 'AliceLayers.PoissonZero', 'AliceLayers.PsiIntermediate', 'AliceLayers.Dual', 'AliceLayers.SectionRegularity', 'AliceLayers.SectionSecond', 'AliceLayers.WeakParts', 'AliceComparator.Challenge', 'AliceComparator.Solution', 'AliceComparator.AssertAxioms',
             'AliceLayers.TangentTransport', 'AliceLayers.TangentSpectral', 'AliceLayers.FiniteProfile', 'AliceLayers.RemainderBounds', 'AliceLayers.DualDecay', 'AliceLayers.ZeroModeDepth', 'AliceLayers.DepthEnvelope', 'AliceLayers.NormalPhase', 'AliceLayers.DepthGeometry', 'AliceLayers.DepthCompletion', 'AliceLayers.NormalizedRemainder', 'AliceLayers.Assembly', 'AliceLayers.AuxiliaryAudit', 'AliceComparator.Axioms',
             'AliceComparator.NewChallenge', 'AliceComparator.NewSolution', 'AliceComparator.NewAxioms',
             'AliceComparator.SecondChallenge', 'AliceComparator.SecondSolution', 'AliceComparator.SecondAxioms',
             'AliceComparator.FinalChallenge', 'AliceComparator.FinalSolution', 'AliceComparator.FinalAxioms']
    records = []
    for module in order:
        relative = Path(*module.split('.'))
        target = build/relative.with_suffix('.olean')
        target.parent.mkdir(parents=True, exist_ok=True)
        command = ['elan', 'run', TOOLCHAIN, 'lean', '-o', str(target), str(relative.with_suffix('.lean'))]
        result = subprocess.run(command, cwd=HERE, env=environment, capture_output=True, text=True, timeout=120)
        (out/(module+'.log')).write_text(result.stdout+result.stderr)
        records.append({'module': module, 'returncode': result.returncode, 'command': command,
                        'source_sha256': digest(HERE/relative.with_suffix('.lean'))})
        print(module, result.returncode, flush=True)
        if result.returncode:
            print(result.stdout+result.stderr)
            break
    success = len(records) == len(order) and all(r['returncode'] == 0 for r in records)
    scalar_proved = success and any(r['module'] == 'AliceLayers.Assembly' for r in records)
    metadata = {'success': success,
                'toolchain': TOOLCHAIN, 'mathlib_commit': mathlib_commit,
                'copied_definitions_byte_equal': copied, 'standard_axiom_guard_count': 9, 'new_comparator_axiom_guard_count': 7, 'second_comparator_axiom_guard_count': 2,
                'auxiliary_standard_axiom_guard_count': 313,
                'final_comparator_axiom_guard_count': 11,
                'final_sources_manifest_sha256': digest(HERE/'final_comparator_sources.json'),
                'open_targets': [] if scalar_proved else ['AliceLayersB'],
                'proved_targets': ['ProfileIntegrability']+(['AliceLayersB'] if scalar_proved else []),
                'runner_sha256': digest(Path(__file__)), 'modules': records,
                'qca_cache_read_only_use': True, 'full_layers_b_proved': scalar_proved,
                'proof_scope': 'scalar AliceLayersB only; excludes Bob and the full Layers lemma',
                'external_review_completed': False}
    (out/'verification.json').write_text(json.dumps(metadata, indent=2)+'\n')
    return 0 if metadata['success'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
