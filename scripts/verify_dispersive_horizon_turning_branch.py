"""Verifier for theory/DISPERSIVE_HORIZON_TURNING_BRANCH_GATE.md (frozen at 08e0703;
POST_RESULTS_EXPLORATORY): transmission of the incident interior right-mover in
the sector -pi/2 < k < 0 (the branch that meets the turning point),

    T_ret(s, profile) = |S_{ext R, int R(k<0)}|^2,

at s in {1/50, 1/200}, for the sharp profile (N = 0), L = 4 (N = 32) and
L = 16 (N = 128).

Imports scripts/verify_dispersive_horizon_frequency_finite_l.py read-only after
a SHA256 check. That import re-runs the full frequency/finite-L verifier
(single-threaded, about 70 min, including the 61 + 53 + 33 checks it imports).
Its helpers (roots_boxes, ceil_log2_kappa, medium_p, M_site_p, t_profile,
solve_hp, rnd_CI, zdata) and its precision rule are reused unchanged.

Parallelism. After the import, the six (s, profile) cases are independent.
They run in up to 4 forked worker processes (multiprocessing, 'fork'),
longest first. Workers return plain Fractions; every check is made in the
parent. The results do not depend on the number of workers or on scheduling.

Per case (all certified quantities are exact rational intervals):
  R1  branch identification by the interval box of lambda (k = -arg lambda):
      exactly one interior right-mover with Re lambda > 0, Im lambda > 0
      (k in (-pi/2, 0), turning branch) and exactly one with Re lambda > 0,
      Im lambda < 0 (k in (0, pi/2), continuing branch);
  R2  full column of |S|^2 for unit-flux incidence on the turning branch
      (interior left-movers, exterior right-mover); its sum encloses 1;
      T_ret (decided), T_cont = |S_{ext R, int R(k>0)}|^2 (reported);
      S^H S encloses I;
  R3  T_ret + T_cont overlaps the sigma^2 enclosure of the same case computed
      by the imported verifier; at sharp z1 (s = 1/50) T_ret overlaps the
      reviewed |t_2|^2 of the transmission verifier.
Verdicts per case: TRANSMISSION_NONZERO_CERTIFIED (T_ret > 0, width <= 1e-6),
OPEN_AFTER_TRANSMISSION_ANALYSIS (a certification step failed or too wide),
S_MATRIX_NOT_ESTABLISHED (not a regular level).
Line: T_RET_DECREASING_AT_COMPUTED_L / T_RET_NOT_DECREASING / MIXED.

Written steps (not machine-checked) are listed in scripts/README.md.
"""
import hashlib
import importlib.util
import multiprocessing
import os
import pathlib
import time
from fractions import Fraction as Fr

import sympy as sp
from sympy import Rational as R

HERE = pathlib.Path(__file__).resolve().parent
SHA_FREQ = '3d585a541663ad7f51a539d728069d228e6a8473772ccc3ca90bb17a8ef80faa'
h_fr = hashlib.sha256((HERE / 'verify_dispersive_horizon_frequency_finite_l.py').read_bytes()).hexdigest()
assert h_fr == SHA_FREQ, 'imported frequency/finite-L verifier bytes changed'

spec = importlib.util.spec_from_file_location('freqfl', HERE / 'verify_dispersive_horizon_frequency_finite_l.py')
fr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fr)          # full frequency/finite-L run (and its imports)
tr, ch, rv = fr.tr, fr.ch, fr.rv
RI, CI = ch.RI, ch.CI
assert len(rv.checks) == 61 and len(ch.checks) == 53 and len(tr.checks) == 33 and len(fr.checks) == 43

checks = []
T0 = time.perf_counter()


def ok(label, cond):
    if not cond:
        raise AssertionError(label)
    checks.append(label)
    print(f'PASS {label}  [{time.perf_counter() - T0:.1f}s]', flush=True)


ok('H imported frequency/finite-L verifier has the reviewed SHA256 (checked before import); '
   '61 + 53 + 33 + 43 imported checks passed', True)


def pair(x):                         # RI -> (lo, hi) of Fractions (picklable)
    return (x.lo, x.hi)


def unpair(p):
    return RI(p[0], p[1])


def sector(lam):
    """'neg' if k = -arg lambda in (-pi/2, 0), 'pos' if in (0, pi/2), else None
    (decided by the interval box)."""
    if lam.re.lo > 0 and lam.im.lo > 0:
        return 'neg'
    if lam.re.lo > 0 and lam.im.hi < 0:
        return 'pos'
    return None


def case(task):
    """Worker: one (s, L, N) case. Returns plain data; raises on unexpected errors."""
    sv, Lv, N, label = task
    cw, sw, zz, zI = fr.zdata(sv)
    out = dict(label=label, status=None)
    for tt in (fr.T_INT, fr.T_EXT):
        H, Nn = tr.HN_at(tt, cw, sw)
        if not (H.degree() == 12 and sp.gcd(H, H.diff(tr.tau)).degree() == 0
                and sp.gcd(H, Nn).degree() == 0):
            out['status'] = 'S_MATRIX_NOT_ESTABLISHED'
            return out
    try:
        base = fr.roots_boxes(fr.T_INT * (2 * fr.T_INT - 1), zz, 256) + \
            fr.roots_boxes(fr.T_EXT * (2 * fr.T_EXT - 1), zz, 256)
        e = fr.ceil_log2_kappa(base)
        p = 256 + 2 * (2 * N + 1) * e
        fr.note(f'{label}: ceil(log2 kappa) = {e}; predeclared precision p = {p} bits; N = {N}')
        mi = fr.medium_p(fr.T_INT, zI, zz, cw, sw, p, f'{label} interior t=5/16')
        me = fr.medium_p(fr.T_EXT, zI, zz, cw, sw, p, f'{label} exterior t=7/16')
        out['counts'] = (mi['nR'], mi['nL'], me['nR'], me['nL'])
        secs = [sector(m['lam']) for m in mi['R']]
        out['sectors'] = secs
        if not (len(secs) == 2 and secs.count('neg') == 1 and secs.count('pos') == 1):
            raise fr.NotCertified(f'branch identification failed (sectors {secs})')
        c_ret, c_cont = secs.index('neg'), secs.index('pos')
        int_out = mi['L'] + mi['ev_large']
        ext_out = me['R'] + me['ev_small']
        int_in, ext_in = mi['R'], me['L']
        vecs = [m['Y'] for m in int_out] + [m['Y'] for m in int_in]
        ts = {x: fr.t_profile(x, Lv, N, p) for x in range(-N - 1, N + 2)}
        for x in range(-N - 1, N + 1):
            Mx = fr.M_site_p(ts[x], ts[x + 1], zI, p)
            vecs = [[fr.rnd_CI(y, p) for y in ch.matvec(Mx, v)] for v in vecs]
        prop_out, prop_in = vecs[:len(int_out)], vecs[len(int_out):]
        cols = prop_out + [[-y for y in m['Y']] for m in ext_out]
        if len(cols) != 12:
            raise fr.NotCertified('matching matrix is not 12 x 12')
        A = [[cols[k][i] for k in range(12)] for i in range(12)]
        Bcols = [[-y for y in v] for v in prop_in] + [m['Y'] for m in ext_in]
        sols, beta = fr.solve_hp(A, Bcols, p)
        out['beta'] = beta
        Fout = [m['aF'] for m in mi['L']] + [m['aF'] for m in me['R']]
        Fin = [m['aF'] for m in int_in] + [m['aF'] for m in ext_in]
        out_rows = list(range(mi['nL'])) + list(range(len(int_out), len(int_out) + me['nR']))
        nI, nO = len(Bcols), len(out_rows)
        absS2 = [[sols[c][r].abs2() * Fout[ri] / Fin[c] for c in range(nI)]
                 for ri, r in enumerate(out_rows)]
        sq_out = [ch.sqrt_RI(f) for f in Fout]
        sq_in = [ch.sqrt_RI(f) for f in Fin]
        S = [[sols[c][r] * CI(sq_out[ri] / sq_in[c]) for c in range(nI)] for ri, r in enumerate(out_rows)]
        SHS = [[sum((S[r][a].conj() * S[r][b] for r in range(nO)), CI(0)) for b in range(nI)]
               for a in range(nI)]
        out['unitary'] = all(fr.contains0(SHS[a][b] - (CI(1) if a == b else CI(0)))
                             for a in range(nI) for b in range(nI))
        if not all(fr.cmag(SHS[a][b]) < 2 for a in range(nI) for b in range(nI)):
            raise fr.NotCertified('S^H S enclosure too wide to be informative')
        er = mi['nL']
        col = [absS2[ri][c_ret] for ri in range(nO)]
        csum = RI(0)
        for v in col:
            csum = csum + v
        out['col'] = [pair(v) for v in col]
        out['col_sum'] = pair(csum)
        out['row_lams'] = [fr.ci_str(m['lam'], 12) for m in mi['L']] + [fr.ci_str(m['lam'], 12) for m in me['R']]
        out['row_sectors'] = [sector(m['lam']) for m in mi['L']] + [sector(m['lam']) for m in me['R']]
        out['ret_lam'] = fr.ci_str(int_in[c_ret]['lam'], 12)
        out['cont_lam'] = fr.ci_str(int_in[c_cont]['lam'], 12)
        out['T_ret'] = pair(absS2[er][c_ret])
        out['T_cont'] = pair(absS2[er][c_cont])
        out['p'] = p
        out['status'] = 'COMPUTED'
        fr.note(f'{label}: done')
        return out
    except fr.NotCertified as exc:
        out['status'] = 'OPEN_AFTER_TRANSMISSION_ANALYSIS'
        out['reason'] = str(exc)
        return out


S_PTS = (R(1, 50), R(1, 200))
PROFILES = ((None, 0, 'sharp'), (4, 32, 'L=4'), (16, 128, 'L=16'))
tasks = []
for Lv, N, pname in reversed(PROFILES):                 # longest first
    for sv in S_PTS:
        tasks.append((sv, Lv, N, f'R s={sv} {pname} N={N}'))

nworkers = min(4, os.cpu_count() or 1)
print(f'Running {len(tasks)} cases on {nworkers} worker process(es) (fork)', flush=True)
ctx = multiprocessing.get_context('fork')
with ctx.Pool(nworkers) as pool:
    results = pool.map(case, tasks, chunksize=1)
res = {}
for (sv, Lv, N, label), out in zip(tasks, results):
    res[(sv, Lv)] = out

# ----------------------------------------------------------------- checks in the parent
EXPECTED = (2, 4, 1, 3)
verdict = {}
for (sv, Lv, N, label) in tasks:
    out = res[(sv, Lv)]
    if out['status'] == 'S_MATRIX_NOT_ESTABLISHED':
        print(f'{label}: S_MATRIX_NOT_ESTABLISHED (not a regular level)')
        verdict[(sv, Lv)] = 'S_MATRIX_NOT_ESTABLISHED'
        continue
    if 'counts' in out:
        ok(f'{label}: channel counts {EXPECTED} (interior R/L, exterior R/L; reviewed counts)',
           out['counts'] == EXPECTED)
    if out['status'] != 'COMPUTED':
        print(f'{label}: OPEN_AFTER_TRANSMISSION_ANALYSIS ({out.get("reason")})')
        verdict[(sv, Lv)] = 'OPEN_AFTER_TRANSMISSION_ANALYSIS'
        continue
    ok(f'{label}: R1 turning branch identified by box sign (one right-mover with k in (-pi/2, 0), '
       f'lambda in {out["ret_lam"]}; one with k in (0, pi/2), lambda in {out["cont_lam"]})', True)
    ok(f'{label}: matching matrix certified invertible (||I - R A D|| <= {fr.dec(out["beta"], 6, True)} < 1/2)',
       out['beta'] < Fr(1, 2))
    ok(f'{label}: S^H S encloses the identity', out['unitary'])
    cs = unpair(out['col_sum'])
    ok(f'{label}: R2 turning-branch column of |S|^2 sums to an enclosure of 1', cs.lo <= 1 <= cs.hi)
    print(f'{label}: turning-branch column (outgoing channel: lambda box, sector, |S|^2):')
    for lam_s, sec, v in zip(out['row_lams'], out['row_sectors'], out['col']):
        print(f'    {lam_s}  [{sec}]  {fr.ri_str(unpair(v), 20)}')
    Tret, Tcont = unpair(out['T_ret']), unpair(out['T_cont'])
    print(f'{label}: T_ret in {fr.ri_str(Tret, 20)}; T_cont in {fr.ri_str(Tcont, 20)}; p = {out["p"]}')
    # R3: sum against the imported sigma^2 of the same case
    if Lv is None:
        v2, Q2, _ = fr.F2[sv]
    else:
        v2, Q2, _ = fr.F3[(sv, Lv)]
    tot = Tret + Tcont
    ok(f'{label}: R3 T_ret + T_cont overlaps the imported sigma^2 enclosure of the same case',
       Q2 is not None and tot.lo <= Q2.hi and Q2.lo <= tot.hi)
    if Lv is None and sv == R(1, 50):
        t2 = tr.S1[4][1].abs2()
        ok(f'{label}: R3 at sharp z1, T_ret overlaps the reviewed |t_2|^2 of the transmission verifier',
           Tret.lo <= t2.hi and t2.lo <= Tret.hi)
    if Tret.lo > 0 and Tret.width() <= Fr(1, 10**6):
        verdict[(sv, Lv)] = 'TRANSMISSION_NONZERO_CERTIFIED'
    else:
        verdict[(sv, Lv)] = 'OPEN_AFTER_TRANSMISSION_ANALYSIS'
    print(f'{label}: verdict {verdict[(sv, Lv)]}', flush=True)

# ----------------------------------------------------------------- summary
print('\nSUMMARY')
for sv in S_PTS:
    for Lv, N, pname in PROFILES:
        out = res[(sv, Lv)]
        extra = ''
        if out['status'] == 'COMPUTED':
            extra = (f'; T_ret in {fr.ri_str(unpair(out["T_ret"]), 20)}'
                     f'; T_cont in {fr.ri_str(unpair(out["T_cont"]), 20)}; p = {out["p"]}')
        print(f's={sv} {pname}: {verdict[(sv, Lv)]}{extra}')

decided = all(verdict[(sv, Lv)] == 'TRANSMISSION_NONZERO_CERTIFIED' for sv in S_PTS for Lv, _, _ in PROFILES)
if decided:
    T = {(sv, Lv): unpair(res[(sv, Lv)]['T_ret']) for sv in S_PTS for Lv, _, _ in PROFILES}
    dec_ = all(T[(sv, None)].lo > T[(sv, 4)].hi and T[(sv, 4)].lo > T[(sv, 16)].hi for sv in S_PTS)
    notdec = all(T[(sv, 16)].lo >= T[(sv, None)].hi for sv in S_PTS)
    print(f'Line: strict decrease sharp > L=4 > L=16 at both points: {dec_}')
    print(f'Line: abandonment condition T_ret(L=16) >= T_ret(sharp) at both points: {notdec}')
    if dec_:
        line = 'T_RET_DECREASING_AT_COMPUTED_L'
    elif notdec:
        line = 'T_RET_NOT_DECREASING'
    else:
        line = 'MIXED'
else:
    line = 'NOT_DECIDABLE (some case is not TRANSMISSION_NONZERO_CERTIFIED)'
print(f'Line verdict candidate: {line}')
print(f'{len(checks)} turning-branch checks PASS '
      f'(after {len(rv.checks)} + {len(ch.checks)} + {len(tr.checks)} + {len(fr.checks)} imported checks)')
