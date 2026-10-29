"""Exact class derivation (Step 4b-1) of theory/MINIMAL_S2_RIGIDITY_GATE.md for the five faithful
classes left by stage (a) (reports/2026-10-29--minimal-s2-step00.md).

Parametrization (exact, no numerical group identification):
  For a faithful class, rho: G -> SO(3) is (up to SO(3) conjugation, absorbed by a constant basis
  change W) the inclusion G subset SO(3). Write T_h = a_h I + b_h . sigma with a_h in C, b_h in C^3.
  Conjugation by the spin-1/2 lift of g acts as b -> g b (g an integer signed permutation matrix),
  a -> a. Covariance T_{gh} = R_g T_h R_g^dagger is then a_{gh} = a_h, b_{gh} = g b_h. Per G-orbit
  of N_3, the base coefficient b_{h0} is restricted to the fixed space of Stab(h0), and the orbit
  is filled by covariance (well-definedness is checked).

Per class it computes the reduced Groebner basis (grevlex, exact) of the real unitarity system.
  basis == [1]   -> EMPTY_CLASS (no complex, hence no real, solution);
  otherwise      -> a real point is sought among the reviewed Pavia symbols, transported to the
                    class convention; if found -> UNITARY_SYMBOLS_EXIST; else the class is
                    OPEN_AFTER_CLASS_DERIVATION (an ideal different from (1) is not existence).
A per-class time limit implements the stage budget; a timeout gives OPEN_AFTER_CLASS_DERIVATION.

What it does NOT certify: completeness of the dimension/components of nonempty classes, nodes,
c_0, c_strict^iso, Q-a, or anything about DEP19 (A30), which is only an external cross-check.
"""

import itertools
import signal
import sys
import time

import sympy as sp

sys.path.insert(0, "scripts")
import verify_minimal_s2_step00 as S0  # this charter's stage (a) certificate, read-only
import verify_irreducible_isotropy_step01 as S1  # reviewed helpers, read-only
from certificate_utils import sym_zero

CHECKS = 0
I = sp.I
PAULI = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
N3 = S0.N3
LIMIT = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 600


def require(cond, label):
    global CHECKS
    if not cond:
        print(f"[FAIL] {label}")
        raise SystemExit(1)
    CHECKS += 1
    print(f"[PASS] {label}", flush=True)


def matvec(M, v):
    return [sum(M[i][k] * v[k] for k in range(3)) for i in range(3)]


def class_symbol(G, tag):
    """Covariant symbol with rho = inclusion; returns (T, real params)."""
    T, params = {}, []
    for oi, orb in enumerate(S0.orbits(G, N3)):
        h0 = min(orb)
        stab = [g for g in G if S0.act(g, h0) == h0]
        a = sp.symbols(f"a{oi}_r a{oi}_i", real=True)
        bs = sp.symbols(f"b{oi}_0:6", real=True)
        b = [bs[2 * j] + I * bs[2 * j + 1] for j in range(3)]
        # fixed space of Stab(h0): g b = b for all g in stab (real linear conditions on Re, Im)
        eqs = []
        for g in stab:
            gb = matvec(g, b)
            eqs += [sp.re(gb[j] - b[j]) for j in range(3)] + [sp.im(gb[j] - b[j]) for j in range(3)]
        sol = sp.solve([e for e in eqs if e != 0], bs, dict=True) if any(e != 0 for e in eqs) else [{}]
        sol = sol[0]
        b = [sp.expand(x.subs(sol)) for x in b]
        free = sorted(set().union(*[sp.sympify(x).free_symbols for x in b]) | set(a), key=str)
        params += free
        base = (a[0] + I * a[1]) * sp.eye(2) + sum((b[j] * PAULI[j] for j in range(3)), sp.zeros(2))
        for g in G:
            h = S0.act(g, h0)
            gb = matvec(g, b)
            Th = (a[0] + I * a[1]) * sp.eye(2) + sum((gb[j] * PAULI[j] for j in range(3)), sp.zeros(2))
            if h in T:
                if not sym_zero(T[h] - Th):
                    raise AssertionError(f"{tag}: ill-defined orbit map")
            else:
                T[h] = sp.expand(Th)
    return T, params


def class_symbol_linear(G, tag):
    """Second construction: all eight T_h free (a_h, b_h), covariance imposed as linear equations
    a_{gh} = a_h, b_{gh} = g b_h for every g in G and h in N_3, then solved."""
    vars_, T, eqs = [], {}, []
    coef = {}
    for k, h in enumerate(N3):
        xs = sp.symbols(f"y{k}_0:8", real=True)
        vars_ += list(xs)
        coef[h] = ([xs[0] + I * xs[1]], [xs[2 + 2 * j] + I * xs[3 + 2 * j] for j in range(3)])
    for g in G:
        for h in N3:
            a, b = coef[h]
            a2, b2 = coef[S0.act(g, h)]
            gb = matvec(g, b)
            for d in [a2[0] - a[0]] + [b2[j] - gb[j] for j in range(3)]:
                eqs += [sp.re(d), sp.im(d)]
    sol = sp.solve([e for e in eqs if e != 0], vars_, dict=True)[0]
    for h in N3:
        a, b = coef[h]
        T[h] = sp.expand(((a[0] * sp.eye(2) + sum((b[j] * PAULI[j] for j in range(3)),
                                                   sp.zeros(2)))).subs(sol))
    params = sorted(set().union(*[M.free_symbols for M in T.values()]), key=str)
    return T, params


class Timeout(Exception):
    pass


def _alarm(signum, frame):
    raise Timeout


def pavia_point(G):
    """Return a Pavia chirality covariant under G with rho = inclusion, or None."""
    z = sp.symbols("z1:4")
    for ch in (1, -1):
        M, _ = S1.WD.published_symbol(3, ch, z)
        T2 = {}
        for v in N3:
            mono = sp.prod([zi ** (vi + 1) for zi, vi in zip(z, v)])
            T2[tuple(-x for x in v)] = M.applyfunc(
                lambda e: sp.Poly(sp.expand(e * sp.prod(z)), *z).coeff_monomial(mono))
        def coeffs(X):
            return [sp.simplify((X * P).trace() / 2) for P in PAULI]
        ok = all(sym_zero(sp.Matrix(coeffs(T2[S0.act(g, h)])) -
                          sp.Matrix(matvec(g, coeffs(T2[h]))))
                 and sym_zero(T2[S0.act(g, h)].trace() - T2[h].trace())
                 for g in G for h in N3)
        if ok:
            return ch
    return None


def main():
    t0 = time.time()
    classesP = []
    subs = {S0.closure([a, b]) for a in S0.O for b in S0.O}
    pairs_pm = [(v, tuple(-x for x in v)) for v in N3 if v[0] == 1]
    choices = [frozenset(c) for c in itertools.product(*pairs_pm)]
    for G in subs:
        for S in choices:
            if (all(S0.act(g, v) in S for g in G for v in S) and len(S0.orbits(G, S)) == 1
                    and not any(any(S0.conj(g, G) == H and frozenset(S0.act(g, v) for v in S) == Tt
                                    for g in S0.O) for H, Tt in classesP)):
                classesP.append((G, S))
    classesF = []
    for G in subs:
        if len(S0.orbits(G, N3)) == 1 and not any(any(S0.conj(g, G) == H for g in S0.O)
                                                  for H in classesF):
            classesF.append(G)
    named = {}
    for G, S in classesP:
        named[{(4, "tetrahedron"): "V4_tet_Pauli", (12, "tetrahedron"): "T_tet",
               (4, "face"): "C4_face"}[(len(G), S0.kind(S))]] = G
    for G in classesF:
        named[{8: "D4", 24: "O"}[len(G)]] = G
    require(sorted(named) == ["C4_face", "D4", "O", "T_tet", "V4_tet_Pauli"],
            "the five faithful classes of stage (a) are reconstructed (families P and F)")

    results = {}
    signal.signal(signal.SIGALRM, _alarm)
    for name in ("O", "T_tet", "D4", "C4_face", "V4_tet_Pauli"):
        G = named[name]
        T, params = class_symbol(G, name)
        require(len(T) == 8, f"{name}: covariant symbol defined on all of N_3, "
                f"{len(params)} real parameters")
        eqs = S1.unitarity_equations(T, 2)
        t1 = time.time()
        signal.alarm(LIMIT)
        try:
            unit = S1.groebner_is_unit(eqs, params)
            signal.alarm(0)
        except Timeout:
            results[name] = f"OPEN_AFTER_CLASS_DERIVATION (Groebner timeout {LIMIT} s)"
            print(f"      {name}: {results[name]}", flush=True)
            continue
        if unit:
            results[name] = "EMPTY_CLASS"
            require(True, f"{name}: unitarity ideal is (1) -> EMPTY_CLASS "
                    f"({time.time() - t1:.0f} s)")
            # second construction (linear covariance on free T_h), must agree
            T2, p2 = class_symbol_linear(G, name)
            signal.alarm(LIMIT)
            try:
                unit2 = S1.groebner_is_unit(S1.unitarity_equations(T2, 2), p2)
                signal.alarm(0)
            except Timeout:
                unit2 = None
            require(unit2 is True and len(p2) == len(params),
                    f"{name}: second construction (linear covariance on free T_h, {len(p2)} real "
                    "parameters) also gives the unit ideal")
        else:
            T2, p2 = class_symbol_linear(G, name)
            require(len(p2) == len(params),
                    f"{name}: second construction has the same number of real parameters "
                    f"({len(p2)})")
            ch = pavia_point(G)
            results[name] = (f"UNITARY_SYMBOLS_EXIST (Pavia chirality {ch})" if ch
                             else "OPEN_AFTER_CLASS_DERIVATION (ideal != (1), no certified real point)")
            print(f"      {name}: ideal != (1) ({time.time() - t1:.0f} s); {results[name]}", flush=True)
            if ch:
                require(True, f"{name}: real point = Pavia chirality {ch}, covariant with rho = "
                        "inclusion and unitary (step-01 control)")
    print(f"      results: {results}")
    print(f"VERDICT: {CHECKS}/{CHECKS} exact checks passed in {time.time() - t0:.0f} s. "
          f"Per class: {results}")


if __name__ == "__main__":
    main()
