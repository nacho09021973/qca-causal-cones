"""Orientation only (not a certificate): compare the certified turning-branch
transmissions T_ret of reports/2026-11-27--dispersive-horizon-turning-branch-run-1.txt
with the charter heuristic of theory/DISPERSIVE_HORIZON_TURNING_BRANCH_GATE.md,

    X(s, L) = 1 / (1 + exp(2 pi omega / alpha)),  alpha = 1/(2L),  omega = 2 atan(s),

i.e. X = 1/(1 + exp(4 pi omega L)) (Sabsovich et al. form with the author's
identification alpha = |dv/dx| at the horizon; [UNVERIFIED]).

Reads the T_ret enclosures from the recorded log (after a SHA256 check) and
evaluates X with mpmath at 40 digits. Floating point here is only for the
comparison; no verdict depends on it.
"""
import hashlib
import pathlib
import re
from fractions import Fraction as Fr

import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOG = ROOT / 'reports' / '2026-11-27--dispersive-horizon-turning-branch-run-1.txt'

data = LOG.read_bytes()
sha = hashlib.sha256(data).hexdigest()
print(f'log {LOG.name} sha256 {sha}')

mp.mp.dps = 40
pat = re.compile(r'^s=(\d+)/(\d+) L=(\d+): TRANSMISSION_NONZERO_CERTIFIED; T_ret in \[([0-9.]+), ([0-9.]+)\]')
rows = []
for line in data.decode().splitlines():
    m = pat.match(line)
    if m:
        s = Fr(int(m.group(1)), int(m.group(2)))
        L = int(m.group(3))
        lo, hi = Fr(m.group(4)), Fr(m.group(5))
        rows.append((s, L, lo, hi))
assert len(rows) == 4, f'expected 4 finite-L summary lines, found {len(rows)}'

print(f'{"s":>6} {"L":>3} {"heuristic X":>14} {"T_ret (log lower bound)":>24} {"T_ret / X":>10}')
for s, L, lo, hi in rows:
    om = 2 * mp.atan(mp.mpf(s.numerator) / s.denominator)
    X = 1 / (1 + mp.exp(4 * mp.pi * om * L))
    T = mp.mpf(lo.numerator) / lo.denominator
    print(f'{str(s):>6} {L:>3} {mp.nstr(X, 8):>14} {mp.nstr(T, 8):>24} {mp.nstr(T / X, 5):>10}')
