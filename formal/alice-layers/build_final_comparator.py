"""Compile only the final comparator against already verified project objects, offline.

Used by lean-mutar; it deliberately does not run the byte-equality verifier, so
mutations must be rejected by FinalSolution.lean or FinalAxioms.lean themselves.
Run verify.py before and after the mutation campaign to validate all dependencies.
"""
import os
from pathlib import Path
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import HERE, PACKAGES, TOOLCHAIN


def main():
    paths = [HERE/'build', *(p/'.lake/build/lib/lean' for p in sorted(PACKAGES.iterdir())
                            if (p/'.lake/build/lib/lean').is_dir())]
    environment = dict(os.environ, LEAN_PATH=os.pathsep.join(map(str, paths)))
    for module in ('AliceComparator.FinalChallenge', 'AliceComparator.FinalSolution',
                   'AliceComparator.FinalAxioms'):
        relative = Path(*module.split('.'))
        target = HERE/'build'/relative.with_suffix('.olean')
        target.parent.mkdir(parents=True, exist_ok=True)
        command = ['elan', 'run', TOOLCHAIN, 'lean', '-o', str(target), str(relative.with_suffix('.lean'))]
        result = subprocess.run(command, cwd=HERE, env=environment, capture_output=True, text=True, timeout=120)
        print(result.stdout+result.stderr, end='', flush=True)
        if result.returncode:
            return result.returncode
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
