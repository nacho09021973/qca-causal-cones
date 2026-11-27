"""Harness test (not a certificate) of scripts/verify_dispersive_horizon_heuristic_prediction.py,
authorized by the user after two failed runs of that verifier (2026-11-27,
«si, con la prueba previa»). It computes no transmission at any new point.

It executes the verifier's own top-level code, byte for byte as parsed by ast,
except the nodes that need the 37-min import chain or the worker pool:
  skipped: SHA check and import of the turning-branch verifier, the import-count
  assertion, the R0 loops (they need tr.H_of), the task list, the pool and the
  OUT assembly.
  injected instead: R0_OK = True at s = 1/80 and 1/40; a stub `fr` whose
  helpers (raw_fr, rnd_RI, fl, ce, dec, ri_str) and the RI class are extracted
  by ast from the reviewed files that define them; a stub `tb.res` holding the
  six calibration T_ret enclosures parsed from the recorded turning-branch run-1
  log; and a synthetic OUT.

Checks:
  A. Real data. The X enclosures pass the verifier's own check against the
     frozen prediction table, and the calibration rho printed in the reported
     section agree with reports/2026-11-27--dispersive-horizon-turning-branch-heuristic.txt
     (1.1114, 0.97121, 0.99219, 1.0076) to the digits printed there.
  B. Synthetic T_ret, labelled SYNTHETIC, chosen as X * rho_syn with a tiny
     width, to exercise every verdict path and the formatting code:
       S1 all within tolerance, B consistent, control controlled;
       S2 one INTERMEDIATE, one OUTSIDE_REJECTION_BAND, B violated,
          control sensitive -> HEURISTIC_REJECTED_AT_DECLARED_POINTS;
       S3 one point OPEN_AFTER_TRANSMISSION_ANALYSIS (status not computed),
          one INTERMEDIATE -> OPEN_AFTER_PREDICTION_TEST, B undecided;
       S4 one INTERMEDIATE, the rest within -> HEURISTIC_PARTIAL.
     The synthetic values are not results and must not be quoted as such.

Output: reports/2026-11-27--dispersive-horizon-heuristic-prediction-harness-test.txt.
"""
import ast
import contextlib
import hashlib
import io
import pathlib
import re
import types
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
VER = HERE / 'verify_dispersive_horizon_heuristic_prediction.py'
src = VER.read_text()
print(f'verifier {VER.name} sha256 {hashlib.sha256(VER.read_bytes()).hexdigest()}')


def extract(path, names):
    """Source of the named top-level defs/classes of a file (exact bytes)."""
    text = path.read_text()
    out = []
    for node in ast.parse(text).body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in names:
            out.append(ast.get_source_segment(text, node))
    assert len(out) == len(names), (path.name, names, len(out))
    return '\n\n'.join(out)


# ---------------------------------------------------------------- stub fr / RI
helpers = {'Fr': Fr}
exec(extract(HERE / 'verify_dispersive_horizon_channels.py', ['RI']), helpers)
exec(extract(HERE / 'verify_dispersive_horizon_frequency_finite_l.py', ['fl', 'ce', 'rnd_RI', 'raw_fr']), helpers)
exec(extract(HERE / 'verify_dispersive_horizon_transmission.py', ['dec', 'ri_str']), helpers)
RI = helpers['RI']
fr_stub = types.SimpleNamespace(**{k: helpers[k] for k in ('fl', 'ce', 'rnd_RI', 'raw_fr', 'dec', 'ri_str')},
                                checks=[])

# ---------------------------------------------------------------- calibration T_ret
TBLOG = ROOT / 'reports' / '2026-11-27--dispersive-horizon-turning-branch-run-1.txt'
pat = re.compile(r'^s=1/(\d+) L=(\d+): TRANSMISSION_NONZERO_CERTIFIED; T_ret in \[([0-9.]+), ([0-9.]+)\]')
cal = {}
for line in TBLOG.read_text().splitlines():
    m = pat.match(line)
    if m:
        cal[(int(m.group(1)), int(m.group(2)))] = (Fr(m.group(3)), Fr(m.group(4)))
assert len(cal) == 4, cal
print(f'calibration log {TBLOG.name} sha256 {hashlib.sha256(TBLOG.read_bytes()).hexdigest()}')

# ---------------------------------------------------------------- select verifier nodes
SKIP = ('hashlib.sha256', 'assert h_tb', 'R0_OK = {}', 'spec_from_file_location', 'module_from_spec', "sys.modules['turnbr']",
        'exec_module', 'fr, tr, ch, rv = ', 'RI = tb.RI', 'assert (len(rv.checks)', 'r0(sv)',
        'tasks = []', 'in [CONTROL] + sorted', 'nworkers = ', "print(f'Running", 'ctx = ',
        'with ctx.Pool', 'OUT = {}', 'out in zip(tasks, results)')
tree = ast.parse(src)
kept, skipped = [], []
for node in tree.body:
    seg = ast.get_source_segment(src, node)
    (skipped if any(s in seg for s in SKIP) else kept).append(node)
print(f'verifier top-level nodes: {len(tree.body)}; kept {len(kept)}; skipped {len(skipped)}:')
for node in skipped:
    print(f'    line {node.lineno}: {ast.get_source_segment(src, node).splitlines()[0][:90]}')
assert len(skipped) == 21, len(skipped)
code = compile(ast.Module(body=kept, type_ignores=[]), str(VER), 'exec')


def make_out(T, Tc, status='COMPUTED'):
    if status != 'COMPUTED':
        return dict(status=status, counts=(2, 4, 1, 3), reason='SYNTHETIC failure')
    return dict(status='COMPUTED', counts=(2, 4, 1, 3), ret_lam='SYNTHETIC', cont_lam='SYNTHETIC',
                p=0, beta=Fr(1, 10), unitary=True,
                col_sum=(Fr(999999, 10**6), Fr(1000001, 10**6)),
                row_lams=['SYNTHETIC'], row_sectors=['neg'], col=[(T.lo, T.hi)],
                T_ret=(T.lo, T.hi), T_cont=(Tc.lo, Tc.hi))


def run(scenario, rho_syn, ctrl_factor, open_pid=None):
    """Execute the kept verifier code; return captured stdout."""
    import sympy
    R = sympy.Rational
    tb_stub = types.SimpleNamespace(
        res={(R(1, s), L): dict(status='COMPUTED', T_ret=v) for (s, L), v in cal.items()},
        checks=[0] * 38)
    ns = {'__name__': 'harness', '__file__': str(VER), 'fr': fr_stub, 'tb': tb_stub, 'RI': RI,
          'rv': types.SimpleNamespace(checks=[0] * 61), 'ch': types.SimpleNamespace(checks=[0] * 53),
          'tr': types.SimpleNamespace(checks=[0] * 33),
          'R0_OK': {R(1, 80): True, R(1, 40): True}, 'OUT': {}}
    # The OUT dict is filled after XE exists: wrap via a two-phase exec. Phase 1 runs
    # everything up to the first use of OUT (certify_case is only called later), so
    # OUT can be filled before the calls by giving OUT a lazy filler.
    class LazyOut(dict):
        def __missing__(self, pid):
            XE = ns['XE']
            base = 'Q4' if pid == 'Q4p' else pid
            if pid == open_pid:
                return make_out(None, None, status='OPEN_AFTER_TRANSMISSION_ANALYSIS')
            r = Fr(rho_syn[base]) * (Fr(ctrl_factor) if pid == 'Q4p' else 1)
            X = XE[base]
            T = RI(X.lo * r, X.lo * r * (1 + Fr(1, 10**9)))
            return make_out(T, RI(1 - T.hi - Fr(1, 10**3), 1 - T.lo - Fr(1, 10**3)))
    ns['OUT'] = LazyOut()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(code, ns)
    text = buf.getvalue()
    print(f'\n===== scenario {scenario} (SYNTHETIC T_ret except calibration) =====')
    for line in text.splitlines():
        if not line.startswith('    '):
            print('  ' + line)
    return text


results = {}
results['S1'] = run('S1', {'Q1': 1, 'Q2': 1, 'Q3': Fr(102, 100), 'Q4': Fr(95, 100)}, Fr(10001, 10000))
results['S2'] = run('S2', {'Q1': 1, 'Q2': Fr(7, 10), 'Q3': 1, 'Q4': Fr(4, 10)}, Fr(103, 100))
results['S3'] = run('S3', {'Q1': 1, 'Q2': 1, 'Q3': Fr(13, 10), 'Q4': 1}, 1, open_pid='Q2')
results['S4'] = run('S4', {'Q1': Fr(3, 2), 'Q2': 1, 'Q3': 1, 'Q4': 1}, Fr(1005, 1000))

EXPECT = {
    'S1': ['Q1: rho', 'WITHIN_TOLERANCE', 'B (Q2, Q3): SCALING_CONSISTENT',
           "Q4' truncation control: TRUNCATION_CONTROLLED",
           'Line verdict candidate: HEURISTIC_WITHIN_TOLERANCE_AT_DECLARED_POINTS'],
    'S2': ['Q2 s=1/40 L=8 N=64: INTERMEDIATE', 'Q4 s=1/40 L=16 N=128: OUTSIDE_REJECTION_BAND',
           'B (Q2, Q3): SCALING_VIOLATED', "Q4' truncation control: TRUNCATION_SENSITIVE",
           'Line verdict candidate: HEURISTIC_REJECTED_AT_DECLARED_POINTS'],
    'S3': ['Q2 s=1/40 L=8 N=64: OPEN_AFTER_TRANSMISSION_ANALYSIS', 'Q3 s=1/80 L=16 N=128: INTERMEDIATE',
           'B (Q2, Q3): SCALING_UNDECIDED', 'Line verdict candidate: OPEN_AFTER_PREDICTION_TEST'],
    'S4': ['Q1 s=1/80 L=8 N=64: INTERMEDIATE', "Q4' truncation control: TRUNCATION_UNDECIDED",
           'Line verdict candidate: HEURISTIC_PARTIAL'],
}
print('\n===== assertions =====')
for sc, exps in EXPECT.items():
    for e in exps:
        assert e in results[sc], (sc, e)
    print(f'  {sc}: expected verdict strings present ({len(exps)})')

# A. real data: X table check passed in every scenario (ok() would have raised), and
# the calibration rho agree with the recorded heuristic comparison.
REF = {('1/50', '4'): '1.1114', ('1/50', '16'): '0.97121', ('1/200', '4'): '0.99219', ('1/200', '16'): '1.0076'}
cal_pat = re.compile(r'^\s+s = (1/\d+) L = (\d+): rho in \[([0-9.]+), ([0-9.]+)\]$', re.M)
found = {(m.group(1), m.group(2)): (Fr(m.group(3)), Fr(m.group(4))) for m in cal_pat.finditer(results['S1'])}
assert set(found) == set(REF), found
for key, ref in REF.items():
    lo, hi = found[key]
    digits = len(ref.replace('.', '').lstrip('0'))
    q = Fr(10) ** (-(len(ref.split('.')[1])))
    assert abs(lo - Fr(ref)) <= q / 2 + Fr(1, 10**12), (key, lo, ref)
    print(f'  calibration rho s = {key[0]} L = {key[1]}: [{float(lo):.10f}, {float(hi):.10f}] '
          f'matches recorded {ref}')
for sc in results:
    assert results[sc].count('agrees with the frozen prediction table') == 4
print('  X enclosures pass the frozen-table check (4 points) in every scenario')
print('\nAll harness assertions passed.')
