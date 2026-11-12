"""Offline incremental Lean compilation. No lake invocation or dependency writes."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
PACKAGES = HERE.parent/'.lake/packages'
TOOLCHAIN = 'leanprover/lean4:v4.31.0'
MODULES = {
    'AliceLayers.Definitions': [],
    'AliceLayers.Targets': ['AliceLayers.Definitions'],
    'AliceLayers.Basic': ['AliceLayers.Targets'],
    'AliceLayers.Covolume': ['AliceLayers.Basic'],
    'AliceLayers.Reindex': ['AliceLayers.Covolume'],
    'AliceLayers.Poisson': ['AliceLayers.Reindex'],
    'AliceLayers.PoissonZero': ['AliceLayers.Poisson'],
    'AliceLayers.PsiIntermediate': ['AliceLayers.PoissonZero'],
    'AliceLayers.Dual': ['AliceLayers.PsiIntermediate'],
    'AliceLayers.SectionRegularity': ['AliceLayers.Dual'],
    'AliceLayers.SectionSecond': ['AliceLayers.SectionRegularity'],
    'AliceLayers.WeakParts': ['AliceLayers.SectionSecond'],
    'AliceLayers.TangentTransport': ['AliceLayers.WeakParts'],
    'AliceLayers.TangentSpectral': ['AliceLayers.TangentTransport'],
    'AliceLayers.FiniteProfile': ['AliceLayers.TangentSpectral'],
    'AliceLayers.RemainderBounds': ['AliceLayers.FiniteProfile'],
    'AliceLayers.DualDecay': ['AliceLayers.RemainderBounds'],
    'AliceLayers.ZeroModeDepth': ['AliceLayers.DualDecay'],
    'AliceLayers.DepthEnvelope': ['AliceLayers.ZeroModeDepth'],
    'AliceLayers.NormalPhase': ['AliceLayers.DepthEnvelope'],
    'AliceLayers.DepthGeometry': ['AliceLayers.NormalPhase'],
    'AliceLayers.DepthCompletion': ['AliceLayers.DepthGeometry'],
    'AliceLayers.NormalizedRemainder': ['AliceLayers.DepthCompletion'],
    'AliceLayers.Assembly': ['AliceLayers.NormalizedRemainder'],
    'AliceComparator.Challenge': [],
    'AliceComparator.Solution': ['AliceComparator.Challenge', 'AliceLayers.Basic'],
    'AliceComparator.AssertAxioms': [],
    'AliceLayers.AuxiliaryAudit': ['AliceLayers.Assembly', 'AliceComparator.AssertAxioms'],
    'AliceComparator.Axioms': ['AliceComparator.Solution', 'AliceComparator.AssertAxioms'],
    'AliceComparator.NewChallenge': [],
    'AliceComparator.NewSolution': ['AliceComparator.NewChallenge', 'AliceLayers.SectionRegularity'],
    'AliceComparator.NewAxioms': ['AliceComparator.NewSolution', 'AliceComparator.AssertAxioms'],
    'AliceComparator.SecondChallenge': [],
    'AliceComparator.SecondSolution': ['AliceComparator.SecondChallenge', 'AliceLayers.SectionSecond'],
    'AliceComparator.SecondAxioms': ['AliceComparator.SecondSolution', 'AliceComparator.AssertAxioms'],
    'AliceComparator.FinalChallenge': [],
    'AliceComparator.FinalSolution': ['AliceComparator.FinalChallenge', 'AliceLayers.Assembly'],
    'AliceComparator.FinalAxioms': ['AliceComparator.FinalSolution', 'AliceComparator.AssertAxioms'],
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    build = HERE/'build'
    build.mkdir(exist_ok=True)
    paths = [build, *(p/'.lake/build/lib/lean' for p in sorted(PACKAGES.iterdir()) if (p/'.lake/build/lib/lean').is_dir())]
    environment = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, paths)))
    keys = {}
    for module, dependencies in MODULES.items():
        relative = Path(*module.split('.'))
        source = HERE/relative.with_suffix('.lean')
        target = build/relative.with_suffix('.olean')
        state = target.with_suffix('.json')
        key = digest(source.read_bytes()+Path(__file__).read_bytes()+TOOLCHAIN.encode()
                     +str([keys[name] for name in dependencies]).encode())
        keys[module] = key
        target.parent.mkdir(parents=True, exist_ok=True)
        if module != 'AliceComparator.Axioms' and target.exists() and state.exists() and json.loads(state.read_text()).get('key') == key:
            continue
        command = ['elan', 'run', TOOLCHAIN, 'lean', '-o', str(target), str(relative.with_suffix('.lean'))]
        result = subprocess.run(command, cwd=HERE, env=environment, capture_output=True, text=True, timeout=120)
        print(result.stdout+result.stderr, end='', flush=True)
        if result.returncode:
            return result.returncode
        state.write_text(json.dumps({'key': key})+'\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
