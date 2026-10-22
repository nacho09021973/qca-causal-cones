"""Run every scripts/verify_*.py from the repository root and record the outcome.

Usage (from the repo root):
    python3 -B scripts/run_all_verifiers.py --output reports/<date>--verifier-sweep.tsv

Each verifier runs in its own process with a timeout. The record lists the
git HEAD, Python/SymPy/NumPy versions, and per script: exit code, wall time
and the last non-empty output line. A nonzero exit or timeout is a failure.
This runner certifies nothing scientific by itself; it reports whether the
existing certificates still execute as committed.
Exits nonzero if any verifier fails.
"""

import argparse
import glob
import os
import subprocess
import sys
import time


def last_line(text):
    lines = [l for l in text.strip().splitlines() if l.strip()]
    return lines[-1][:200] if lines else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--timeout", type=int, default=900)
    args = ap.parse_args()

    head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                          text=True).stdout.strip()
    import numpy
    import sympy

    rows = []
    failures = 0
    for path in sorted(glob.glob("scripts/verify_*.py")):
        t0 = time.time()
        try:
            p = subprocess.run([sys.executable, "-B", path], capture_output=True,
                               text=True, timeout=args.timeout)
            code, out = p.returncode, p.stdout + p.stderr
        except subprocess.TimeoutExpired:
            code, out = "TIMEOUT", ""
        dt = time.time() - t0
        if code != 0:
            failures += 1
        rows.append((os.path.basename(path), str(code), f"{dt:.1f}",
                     last_line(out).replace("\t", " ")))
        print(f"{rows[-1][1]:>7}  {rows[-1][2]:>7}s  {rows[-1][0]}", flush=True)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(f"# git_head\t{head}\n# python\t{sys.version.split()[0]}\n"
                f"# sympy\t{sympy.__version__}\n# numpy\t{numpy.__version__}\n"
                f"# timeout_s\t{args.timeout}\n")
        f.write("script\texit\tseconds\tlast_line\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    print(f"\n{len(rows)} verifiers, {failures} failed; record: {args.output}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
