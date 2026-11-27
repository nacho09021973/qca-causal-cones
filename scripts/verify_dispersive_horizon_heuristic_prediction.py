"""Verifier for theory/DISPERSIVE_HORIZON_HEURISTIC_PREDICTION_GATE.md (frozen at 35bf83f;
POST_RESULTS_EXPLORATORY): prospective test of the heuristic

    X(omega, L) = 1 / (1 + exp(4 pi omega L)),   omega = 2 atan(s),

against the certified turning-branch transmission

    T_ret = |S_{ext R, int R(k<0)}|^2   (unit-flux incidence),

at four new points, truncated tanh profile with N = 8L:
    Q1 (1/80, 8), Q2 (1/40, 8), Q3 (1/80, 16), Q4 (1/40, 16),
plus the truncation control Q4' = (1/40, 16) at N = 12L = 192.

Imports scripts/verify_dispersive_horizon_turning_branch.py read-only after a
SHA256 check. The import re-runs that verifier (38 checks) and, through it, the
frequency/finite-L, transmission, channels and transfer-matrix verifiers
(61 + 53 + 33 + 43 checks): level-1 reproduction of the six calibration cases,
including the sharp-z1 |t_2|^2 check that detects a branch swap. About 37 min
on the reference machine.

Its module-level function case((s, L, N, label)) is called unchanged for each
new case. It contains the regularity test at t = 5/16 and 7/16, the predeclared
precision p = 256 + 2(2N + 1) ceil(log2 kappa), the certified root boxes, the
flux normalization, R1 (branch identified by the sign of the lambda box), the
interval propagation, the certified matching solve, S^H S, the turning-branch
column and the T_ret / T_cont enclosures.

New in this file (the charter, Sec. 5):
  R0   regime per new s: the F1 (b)-type test. The discriminant in tau of
       H_A(tau) at z(s), as a polynomial in A, has exactly one root in
       [A(5/16), A(7/16)] and is nonzero at both ends; the leading coefficient
       of H_A is a nonzero number and deg H_A = 12. Reproduces the inline F1 (b)
       loop of the frequency verifier, which is not callable. The same test is
       run at the calibration points s = 1/50 and 1/200 as a cross-check
       (the frequency run-1 log reports one root there). The y* classification
       is not used (known defect, scripts/README.md).
  counts  channel counts (2, 4, 1, 3) per case; a mismatch makes the point
       REGIME_NOT_CERTIFIED (the turning-branch parent would abort instead).
  width   relative width of T_ret <= 1e-6 * T_ret.lo (the absolute 1e-6 of
       case's own verdict is not enough at Q4).
  X    exact rational enclosure. omega = 2 atan(1/q) from consecutive partial
       sums of the alternating atan series (0 < 1/q < 1, terms decreasing, so
       they bracket atan). pi from mpmath iv (outward rounding). exp from
       mpmath iv.exp at each endpoint of the rational exponent interval,
       converted exactly to Fractions. mpmath iv has no atan, hence the series.
  rho  rho = T_ret / X as a rational interval; per-point verdicts
       WITHIN_TOLERANCE / INTERMEDIATE / OUTSIDE_REJECTION_BAND, or
       REGIME_NOT_CERTIFIED / S_MATRIX_NOT_ESTABLISHED /
       OPEN_AFTER_TRANSMISSION_ANALYSIS, in the charter's order.
  B    r = rho(Q2) / rho(Q3): SCALING_CONSISTENT / SCALING_VIOLATED /
       SCALING_UNDECIDED.
  Q4'  TRUNCATION_CONTROLLED / TRUNCATION_SENSITIVE / TRUNCATION_UNDECIDED.
  line HEURISTIC_WITHIN_TOLERANCE_AT_DECLARED_POINTS /
       HEURISTIC_REJECTED_AT_DECLARED_POINTS / HEURISTIC_PARTIAL /
       OPEN_AFTER_PREDICTION_TEST.

Reported, not decided: kappa_eff = ln(1/T_ret - 1)/(4 pi omega L) (plain
mpmath, orientation), the sign pattern of ln rho, the monotonicity
T_ret(L = 16) < T_ret(L = 8) at each s, T_cont, sigma^2 = T_ret + T_cont, the
turning-branch column, and rho at the four calibration points (excluded from
every verdict).

Parallelism: after the import, the five cases run in up to 4 forked worker
processes ('fork'; Linux/WSL only), longest first, with Pool.map (order
preserved). Workers return plain Fractions; every PASS check and every verdict
is made in the parent. An open state can end with exit code 0: the summary
states are what count. Any failed PASS check or exception exits nonzero.

Written steps (not machine-checked) are listed in scripts/README.md.
"""
import hashlib
import importlib.util
import multiprocessing
import os
import pathlib
import time
from fractions import Fraction as Fr

import mpmath as mp
from mpmath import iv
import sympy as sp
from sympy import Rational as R

HERE = pathlib.Path(__file__).resolve().parent
SHA_TB = '397f72b3a9293fe1784dfb9e3d4da8a616f215999c3c97adee006d7d880e0676'
h_tb = hashlib.sha256((HERE / 'verify_dispersive_horizon_turning_branch.py').read_bytes()).hexdigest()
assert h_tb == SHA_TB, 'imported turning-branch verifier bytes changed'

spec = importlib.util.spec_from_file_location('turnbr', HERE / 'verify_dispersive_horizon_turning_branch.py')
tb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tb)          # full turning-branch run (and its imports)
fr, tr, ch, rv = tb.fr, tb.tr, tb.ch, tb.rv
RI = tb.RI
assert (len(rv.checks), len(ch.checks), len(tr.checks), len(fr.checks), len(tb.checks)) == (61, 53, 33, 43, 38)

checks = []
T0 = time.perf_counter()


def ok(label, cond):
    if not cond:
        raise AssertionError(label)
    checks.append(label)
    print(f'PASS {label}  [{time.perf_counter() - T0:.1f}s]', flush=True)


ok('H imported turning-branch verifier has the reviewed SHA256 (checked before import); '
   '61 + 53 + 33 + 43 + 38 imported checks passed', True)

# ----------------------------------------------------------------- declared design (frozen)
EXPECTED_COUNTS = (2, 4, 1, 3)
POINTS = [                                      # id, s, L, N
    ('Q1', R(1, 80), 8, 64),
    ('Q2', R(1, 40), 8, 64),
    ('Q3', R(1, 80), 16, 128),
    ('Q4', R(1, 40), 16, 128),
]
CONTROL = ('Q4p', R(1, 40), 16, 192)
# Frozen prediction table of the charter (Sec. 3), orientation digits.
X_TABLE = {'Q1': Fr('0.0749419'), 'Q2': Fr('0.00652543'), 'Q3': Fr('0.00652034'), 'Q4': Fr('4.31406e-5')}
TOL = (Fr(4, 5), Fr(5, 4))                      # A: tolerance band
REJ = (Fr(1, 2), Fr(2))                         # A: rejection band
B_CONS = (Fr(10, 11), Fr(11, 10))               # B: consistency band
B_VIOL = (Fr(4, 5), Fr(5, 4))                   # B: violation if disjoint from this
REL_W = Fr(1, 10**6)                            # relative width of T_ret
TR_OK, TR_BAD = Fr(1, 10**3), Fr(1, 10**2)      # truncation thresholds

ok('H declared design: Q1-Q4 = (1/80, 8), (1/40, 8), (1/80, 16), (1/40, 16) with N = 8L; '
   'control Q4\' = (1/40, 16), N = 192',
   all(N == 8 * L for _, _, L, N in POINTS) and CONTROL[3] == 12 * CONTROL[2])


# ----------------------------------------------------------------- R0: regime per s
def r0(sv):
    cw, sw, _, _ = fr.zdata(sv)
    HA = tr.H_of(tr.Asym, cw, sw)
    lc = sp.expand(HA.LC())
    Dsc = sp.Poly(sp.discriminant(HA.as_expr(), tr.tau), tr.Asym)
    nD = Dsc.count_roots(fr.A_INT, fr.A_EXT)
    good = (lc.is_number and lc != 0 and HA.degree() == 12 and nD == 1
            and Dsc.eval(fr.A_INT) != 0 and Dsc.eval(fr.A_EXT) != 0)
    print(f'R0 s = {sv}: leading coefficient {lc}; deg H_A = {HA.degree()}; discriminant degree '
          f'{Dsc.degree()} in A; roots in [A(5/16), A(7/16)]: {nD}; endpoints nonzero: '
          f'{Dsc.eval(fr.A_INT) != 0 and Dsc.eval(fr.A_EXT) != 0}', flush=True)
    return good, nD


for sv in (R(1, 50), R(1, 200)):
    g, nD = r0(sv)
    ok(f'R0 cross-check at calibration s = {sv}: one discriminant root in [A(5/16), A(7/16)] '
       f'(as in the frequency run-1 log)', g and nD == 1)

R0_OK = {}
for sv in (R(1, 80), R(1, 40)):
    R0_OK[sv], _ = r0(sv)
    print(f'R0 s = {sv}: {"regime certified (one real fold)" if R0_OK[sv] else "REGIME_NOT_CERTIFIED"}',
          flush=True)


# ----------------------------------------------------------------- enclosure of X
def atan_inv_RI(q, terms=40):
    """atan(1/q), q integer >= 2: consecutive partial sums of the alternating series bracket it."""
    x = Fr(1, q)
    S, prev = Fr(0), None
    for n in range(terms):
        prev = S
        S += (-1) ** n * x ** (2 * n + 1) / (2 * n + 1)
    lo, hi = min(S, prev), max(S, prev)
    assert x ** (2 * terms + 1) / (2 * terms + 1) < Fr(1, 2**300)
    return RI(lo, hi)


def pi_RI():
    iv.prec = 320
    P = iv.pi
    return RI(fr.raw_fr(P._mpi_[0]), fr.raw_fr(P._mpi_[1]))


def exp_lo(a):                      # lower bound of exp(a), a a positive Fraction
    iv.prec = 320
    return fr.raw_fr(iv.exp(iv.mpf(a.numerator) / a.denominator)._mpi_[0])


def exp_hi(a):
    iv.prec = 320
    return fr.raw_fr(iv.exp(iv.mpf(a.numerator) / a.denominator)._mpi_[1])


PI = pi_RI()
ok('X pi enclosure contains 3.14159265358979323846 and has width < 2^-300',
   PI.lo < Fr('3.14159265358979323846264') < PI.hi and PI.hi - PI.lo < Fr(1, 2**300))


def X_RI(sv, Lv):
    q = sv.q
    assert sv.p == 1
    om = atan_inv_RI(q) * 2
    a = fr.rnd_RI(RI(4 * PI.lo * om.lo * Lv, 4 * PI.hi * om.hi * Lv), 300)  # all factors > 0
    Elo, Ehi = exp_lo(a.lo), exp_hi(a.hi)
    assert 0 < Elo <= Ehi
    return RI(1 / (1 + Ehi), 1 / (1 + Elo)), om, a     # X decreasing in the exponent


XE = {}
for pid, sv, Lv, N in POINTS:
    X, om, a = X_RI(sv, Lv)
    XE[pid] = X
    print(f'{pid} s = {sv} L = {Lv}: omega in {fr.ri_str(om, 24)}; 4 pi omega L in {fr.ri_str(a, 20)}; '
          f'X in {fr.ri_str(X, 20)}', flush=True)
    ok(f'{pid}: X enclosure positive, relative width < 1e-60, and agrees with the frozen prediction '
       f'table value {X_TABLE[pid]} to relative 1e-5',
       X.lo > 0 and (X.hi - X.lo) < X.lo * Fr(1, 10**60)
       and abs(X.lo / X_TABLE[pid] - 1) < Fr(1, 10**5))


# ----------------------------------------------------------------- the five cases
def pair_RI(p):
    return RI(p[0], p[1])


def ratio(a, b):                    # a, b positive RI -> RI of a/b
    assert a.lo > 0 and b.lo > 0
    return RI(a.lo / b.hi, a.hi / b.lo)


def inside(x, band):
    return band[0] <= x.lo and x.hi <= band[1]


def disjoint(x, band):
    return x.hi < band[0] or x.lo > band[1]


tasks = []
for pid, sv, Lv, N in [CONTROL] + sorted(POINTS, key=lambda t: -t[3]):    # longest first
    if R0_OK[sv]:
        tasks.append((sv, Lv, N, f'{pid} s={sv} L={Lv} N={N}'))
nworkers = min(4, os.cpu_count() or 1)
print(f'Running {len(tasks)} cases on {nworkers} worker process(es) (fork)', flush=True)
ctx = multiprocessing.get_context('fork')
with ctx.Pool(nworkers) as pool:
    results = pool.map(tb.case, tasks, chunksize=1)
OUT = {}
for (sv, Lv, N, label), out in zip(tasks, results):
    OUT[label.split()[0]] = out


def certify_case(pid, sv, Lv, N):
    """Parent-side checks for one case. Returns (state, T_ret RI or None)."""
    label = f'{pid} s={sv} L={Lv} N={N}'
    if not R0_OK[sv]:
        print(f'{label}: REGIME_NOT_CERTIFIED (R0 failed; not computed)')
        return 'REGIME_NOT_CERTIFIED', None
    out = OUT[pid]
    if out['status'] == 'S_MATRIX_NOT_ESTABLISHED':
        print(f'{label}: S_MATRIX_NOT_ESTABLISHED (not a regular level)')
        return 'S_MATRIX_NOT_ESTABLISHED', None
    if 'counts' in out and out['counts'] != EXPECTED_COUNTS:
        print(f'{label}: REGIME_NOT_CERTIFIED (channel counts {out["counts"]} != {EXPECTED_COUNTS})')
        return 'REGIME_NOT_CERTIFIED', None
    if 'counts' in out:
        ok(f'{label}: channel counts {EXPECTED_COUNTS} (interior R/L, exterior R/L)', True)
    if out['status'] != 'COMPUTED':
        print(f'{label}: OPEN_AFTER_TRANSMISSION_ANALYSIS ({out.get("reason")})')
        return 'OPEN_AFTER_TRANSMISSION_ANALYSIS', None
    ok(f'{label}: R1 turning branch identified by box sign (k in (-pi/2, 0), lambda in {out["ret_lam"]}; '
       f'continuing branch k in (0, pi/2), lambda in {out["cont_lam"]}); p = {out["p"]}', True)
    fails = []
    if not out['beta'] < Fr(1, 2):
        fails.append('matching matrix not certified invertible')
    if not out['unitary']:
        fails.append('S^H S does not enclose I')
    cs = pair_RI(out['col_sum'])
    if not cs.lo <= 1 <= cs.hi:
        fails.append('column sum does not enclose 1')
    if fails:
        print(f'{label}: OPEN_AFTER_TRANSMISSION_ANALYSIS ({"; ".join(fails)})')
        return 'OPEN_AFTER_TRANSMISSION_ANALYSIS', None
    ok(f'{label}: matching matrix certified invertible (||I - R A D|| <= {fr.dec(out["beta"], 6, True)} < 1/2)', True)
    ok(f'{label}: S^H S encloses the identity', True)
    ok(f'{label}: turning-branch column of |S|^2 sums to an enclosure of 1', True)
    print(f'{label}: turning-branch column (outgoing channel: lambda box, sector, |S|^2):')
    for lam_s, sec, v in zip(out['row_lams'], out['row_sectors'], out['col']):
        print(f'    {lam_s}  [{sec}]  {fr.ri_str(pair_RI(v), 20)}')
    T, Tc = pair_RI(out['T_ret']), pair_RI(out['T_cont'])
    print(f'{label}: T_ret in {fr.ri_str(T, 24)}; T_cont in {fr.ri_str(Tc, 20)}; '
          f'sigma^2 = T_ret + T_cont in {fr.ri_str(T + Tc, 20)}', flush=True)
    if not (T.lo > 0 and T.hi - T.lo <= REL_W * T.lo):
        print(f'{label}: OPEN_AFTER_TRANSMISSION_ANALYSIS (T_ret not positive or relative width > 1e-6)')
        return 'OPEN_AFTER_TRANSMISSION_ANALYSIS', None
    return 'CERTIFIED', T


STATE, TRET, RHO = {}, {}, {}
for pid, sv, Lv, N in POINTS:
    st, T = certify_case(pid, sv, Lv, N)
    if st != 'CERTIFIED':
        STATE[pid] = st
        continue
    TRET[pid] = T
    rho = ratio(T, XE[pid])
    RHO[pid] = rho
    if inside(rho, TOL):
        STATE[pid] = 'WITHIN_TOLERANCE'
    elif disjoint(rho, REJ):
        STATE[pid] = 'OUTSIDE_REJECTION_BAND'
    elif inside(rho, (REJ[0], TOL[0])) and rho.hi < TOL[0] or inside(rho, (TOL[1], REJ[1])) and rho.lo > TOL[1]:
        STATE[pid] = 'INTERMEDIATE'
    else:
        STATE[pid] = 'OPEN_AFTER_TRANSMISSION_ANALYSIS'      # rho meets two bands
    print(f'{pid}: rho = T_ret / X in {fr.ri_str(rho, 12)} -> {STATE[pid]}', flush=True)

# truncation control
st4p, T4p = certify_case(*CONTROL)
if 'Q4' in TRET and st4p == 'CERTIFIED':
    qr = ratio(T4p, TRET['Q4'])
    if inside(qr, (1 - TR_OK, 1 + TR_OK)):
        TRUNC = 'TRUNCATION_CONTROLLED'
    elif disjoint(qr, (1 - TR_BAD, 1 + TR_BAD)):
        TRUNC = 'TRUNCATION_SENSITIVE'
    else:
        TRUNC = 'TRUNCATION_UNDECIDED'
    print(f"Q4': T_ret(N = 192) / T_ret(N = 128) in {fr.ri_str(qr, 12)} -> {TRUNC}", flush=True)
else:
    TRUNC = 'TRUNCATION_UNDECIDED'
    print(f"Q4': {TRUNC} (control or Q4 not certified: {st4p})", flush=True)

# B: equal-omega L pair
CERT = ('WITHIN_TOLERANCE', 'INTERMEDIATE', 'OUTSIDE_REJECTION_BAND')
if STATE['Q2'] in CERT and STATE['Q3'] in CERT:
    rB = ratio(RHO['Q2'], RHO['Q3'])
    if inside(rB, B_CONS):
        BV = 'SCALING_CONSISTENT'
    elif disjoint(rB, B_VIOL):
        BV = 'SCALING_VIOLATED'
    else:
        BV = 'SCALING_UNDECIDED'
    print(f'B: r = rho(Q2) / rho(Q3) in {fr.ri_str(rB, 12)} -> {BV}', flush=True)
else:
    BV = 'SCALING_UNDECIDED'
    print(f'B: {BV} (Q2 or Q3 not certified)', flush=True)

# line
ids = [p[0] for p in POINTS]
if any(STATE[i] == 'OUTSIDE_REJECTION_BAND' for i in ids):
    LINE = 'HEURISTIC_REJECTED_AT_DECLARED_POINTS'
elif all(STATE[i] == 'WITHIN_TOLERANCE' for i in ids):
    LINE = 'HEURISTIC_WITHIN_TOLERANCE_AT_DECLARED_POINTS'
elif all(STATE[i] in CERT for i in ids):
    LINE = 'HEURISTIC_PARTIAL'
else:
    LINE = 'OPEN_AFTER_PREDICTION_TEST'

# ----------------------------------------------------------------- reported data (not decided)
print('\nREPORTED DATA (orientation; no verdict depends on it)')
mp.mp.dps = 50
for pid, sv, Lv, N in POINTS:
    if pid in TRET:
        T, rho = TRET[pid], RHO[pid]
        Tm = mp.mpf(T.lo.numerator) / T.lo.denominator
        om = 2 * mp.atan(mp.mpf(1) / sv.q)
        keff = mp.log(1 / Tm - 1) / (4 * mp.pi * om * Lv)
        sgn = '+' if rho.lo > 1 else ('-' if rho.hi < 1 else '?')
        print(f'{pid}: kappa_eff = {mp.nstr(keff, 8)}; sign of ln rho: {sgn}')
for sv in (R(1, 80), R(1, 40)):
    a = {8: 'Q1' if sv == R(1, 80) else 'Q2', 16: 'Q3' if sv == R(1, 80) else 'Q4'}
    if a[8] in TRET and a[16] in TRET:
        print(f's = {sv}: T_ret(L = 16) < T_ret(L = 8) by disjoint enclosures: '
              f'{TRET[a[16]].hi < TRET[a[8]].lo}')
print('Calibration points (excluded from every verdict; T_ret re-certified by the import):')
for sv in (R(1, 50), R(1, 200)):
    for Lv in (4, 16):
        o = tb.res[(sv, Lv)]
        if o.get('status') == 'COMPUTED':
            Xc, _, _ = X_RI(sv, Lv)
            print(f'    s = {sv} L = {Lv}: rho in {fr.ri_str(ratio(pair_RI(o["T_ret"]), Xc), 10)}')

# ----------------------------------------------------------------- summary
print('\nSUMMARY')
for pid, sv, Lv, N in POINTS:
    extra = f'; rho in {fr.ri_str(RHO[pid], 12)}' if pid in RHO else ''
    print(f'{pid} s={sv} L={Lv} N={N}: {STATE[pid]}{extra}')
print(f"Q4' truncation control: {TRUNC}")
print(f'B (Q2, Q3): {BV}')
print(f'Line verdict candidate: {LINE}')
print(f'{len(checks)} heuristic-prediction checks PASS '
      f'(after {len(rv.checks)} + {len(ch.checks)} + {len(tr.checks)} + {len(fr.checks)} + {len(tb.checks)} imported checks)')
