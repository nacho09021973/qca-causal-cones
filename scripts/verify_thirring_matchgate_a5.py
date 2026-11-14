#!/usr/bin/env python3
"""Exact checks for the Thirring crossing-matchgate gate (A5), tasks T2-T3.

Contract: theory/THIRRING_MATCHGATE_A5_GATE.md (frozen at 915e55f).
Report:   reports/2026-11-14--thirring-matchgate-a5.md

Family V(r) and its convention (alpha = +i(r^2-1)/(r^2+1) at chi = pi/2,
basis AA, AB, BA, BB = 00, 01, 10, 11, first factor = packet on the larger
coordinate before the crossing) from reports/2026-11-14--thirring-comoving-
packet.md; `alpha_beta`, `Vmat`, `SWAP` imported read-only from
scripts/verify_thirring_comoving_packet.py (not modified; SHA256 recorded).

Formalization of F used by T2 (stated in the report): a crossing of packets
a (right) and b (left) acts on the Fock space as the even operator
W_ab = sum v[(x'y'),(xy)] c+_{a x'} c+_{b y'} c_{b y} c_{a x}, identity on
everything else, and the N-packet map is the time-ordered product of the W's.

Certified (exact SymPy; Fock space by explicit Jordan-Wigner signs):
  S1  two packets: W_ab c+_{a x} c+_{b y}|0> = sum v c+_{a x'} c+_{b y'}|0>
      for a generic symbolic 4x4 v (16 symbols).
  S2  three packets, generic v: in the position-ordered register (creation
      string ordered right to left), a crossing of slots (1,2) with a
      spectator on the left of the string's tail acts as kron(-P v, 1), and a
      crossing of slots (2,3) with a spectator in front as kron(1, -P v): the
      sign is -1 on every basis state, independent of v and of the spectator.
  S3  W_ab commutes with c+ of a third packet on the logical sector (even).
  S4  three packets, v = V(r) at chi = pi/2, both time orders of the three
      crossings (theta_a > theta_b > theta_c): the Fock-level products equal
      the register products G12(y) G23(xy) G12(x) and G23(x) G12(xy) G23(y),
      G = -P V, x = r_ab, y = r_bc; and the two are equal (symbolic x, y).
  M1  G(r) = -P V(r) = G(A, B) with A = -1, B = -[[beta, alpha], [alpha, beta]]
      at chi = pi/2: A, B in SU(2) (unitary, det 1) for all r > 0.
  M2  Valiant p.118: the five matchgate identities hold for G(r), for both
      assignments of the middle rows/columns; B(4,4) != 0.
  M3  second route: P V(r) = exp(+i theta/2 (XX + YY)) with
      cos theta = 2r/(1+r^2), sin theta = (r^2-1)/(r^2+1),
      theta = 2 atan(r) - pi/2; the hint's exp(-i theta/2 (XX+YY)) has the
      opposite off-diagonal sign (recorded, checked unequal for r != 1).
  M4  Jordan-Wigner: with a1 = s- (x) 1, a2 = Z (x) s-,
      a1^+ a2 + a2^+ a1 = (XX + YY)/2, so P V(r) = exp(i theta H),
      H quadratic.

Not certified: F itself; T2's argument that crossings are always between
position-adjacent packets (written); T4 (matching the theorem hypotheses,
written against the sources).
"""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "reports/2026-11-14--thirring-matchgate-a5"
_spec = importlib.util.spec_from_file_location("co", ROOT / "scripts/verify_thirring_comoving_packet.py")
co = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(co)
alpha_beta, Vmat, SWAP = co.alpha_beta, co.Vmat, co.SWAP
I = sp.I
CHECKS = []


def exact(name, cond):
    CHECKS.append(dict(name=name, passed=bool(cond)))


def zero(x):
    return sp.simplify(sp.cancel(sp.expand(x))) == 0


def zero_matrix(M):
    return all(zero(e) for e in M)


# ---------------- Fock space ----------------
# state: dict {occupation tuple: coefficient}; modes 2*p + f (packet p, flavour f)
NMODES = 6


def cdag(m, st):
    out = {}
    for occ, c in st.items():
        if occ[m]:
            continue
        sgn = (-1) ** sum(occ[:m])
        new = list(occ); new[m] = 1
        out[tuple(new)] = out.get(tuple(new), 0) + sgn * c
    return out


def cann(m, st):
    out = {}
    for occ, c in st.items():
        if not occ[m]:
            continue
        sgn = (-1) ** sum(occ[:m])
        new = list(occ); new[m] = 0
        out[tuple(new)] = out.get(tuple(new), 0) + sgn * c
    return out


def add(a, b, k=1):
    out = dict(a)
    for o, c in b.items():
        out[o] = out.get(o, 0) + k * c
    return out


VAC = {tuple([0] * NMODES): sp.Integer(1)}
PAIRS = [(0, 0), (0, 1), (1, 0), (1, 1)]   # (x, y) = flavours; index 2x + y


def W(a, b, v):
    """Even operator of the crossing of packet a (first) with packet b."""
    def op(st):
        res = {}
        for j, (x, y) in enumerate(PAIRS):
            # operator order c+_{a x'} c+_{b y'} c_{b y} c_{a x}: rightmost acts first
            t = cann(2 * b + y, cann(2 * a + x, st))
            if not t:
                continue
            for i, (xp, yp) in enumerate(PAIRS):
                if v[i, j] == 0:
                    continue
                res = add(res, cdag(2 * a + xp, cdag(2 * b + yp, t)), v[i, j])
        return res
    return op


def string(packets, flavours):
    """c+_{p1 f1} c+_{p2 f2} ... |0>, leftmost operator = first slot."""
    st = VAC
    for p, f in reversed(list(zip(packets, flavours))):
        st = cdag(2 * p + f, st)
    return st


def inner(a, b):
    return sp.expand(sum(sp.conjugate(c) * b.get(o, 0) for o, c in a.items()))


def register_map(op, order_in, order_out, n):
    basis = list(itertools.product((0, 1), repeat=n))
    M = sp.zeros(2 ** n, 2 ** n)
    for j, fin in enumerate(basis):
        img = op(string(order_in, fin))
        for i, fout in enumerate(basis):
            M[i, j] = inner(string(order_out, fout), img)
    return M


def generic_v():
    return sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"v{i}{j}"))


def check_S1():
    v = generic_v()
    M = register_map(W(0, 1, v), (0, 1), (0, 1), 2)
    exact("S1-two-packets-identity-order-gives-v", zero_matrix(M - v))


def check_S2():
    v = generic_v()
    I2 = sp.eye(2)
    # slots right-to-left hold packets (0, 1, 2); crossing of packets 0,1 (slots 1,2)
    M12 = register_map(W(0, 1, v), (0, 1, 2), (1, 0, 2), 3)
    exact("S2-crossing-slots(1,2)-equals-kron(-Pv,1)", zero_matrix(M12 - sp.kronecker_product(-SWAP * v, I2)))
    # crossing of packets 1,2 (slots 2,3), packet 0 in front of the string
    M23 = register_map(W(1, 2, v), (0, 1, 2), (0, 2, 1), 3)
    exact("S2-crossing-slots(2,3)-equals-kron(1,-Pv)", zero_matrix(M23 - sp.kronecker_product(I2, -SWAP * v)))
    # different spectator labelling: packets (2, 0, 1) in slots, crossing 2 with 0
    M = register_map(W(2, 0, v), (2, 0, 1), (0, 2, 1), 3)
    exact("S2-relabelled-crossing-equals-kron(-Pv,1)", zero_matrix(M - sp.kronecker_product(-SWAP * v, I2)))


def check_S3():
    v = generic_v()
    ok = True
    for f in (0, 1):
        for x, y in PAIRS:
            st = string((0, 1), (x, y))
            lhs = W(0, 1, v)(cdag(2 * 2 + f, st))
            rhs = cdag(2 * 2 + f, W(0, 1, v)(st))
            d = add(lhs, rhs, -1)
            ok &= all(zero(c) for c in d.values())
    exact("S3-W-commutes-with-spectator-creation", ok)


def G(r):
    return -SWAP * Vmat(r, -I)


def check_S4():
    x, y = sp.symbols("x y", positive=True)
    I2 = sp.eye(2)
    rab, rbc, rac = x, y, x * y
    a, b, c = 0, 1, 2
    # order 1: (ab), then (ac), then (bc); slots right-to-left start (a, b, c)
    def seq(ops):
        def f(st):
            for o in ops:
                st = o(st)
            return st
        return f
    o1 = seq([W(a, b, Vmat(rab, -I)), W(a, c, Vmat(rac, -I)), W(b, c, Vmat(rbc, -I))])
    M1 = register_map(o1, (a, b, c), (c, b, a), 3)
    R1 = sp.kronecker_product(G(y), I2) * sp.kronecker_product(I2, G(x * y)) * sp.kronecker_product(G(x), I2)
    exact("S4-order1-Fock=G12(y)G23(xy)G12(x)", zero_matrix(M1 - R1))
    o2 = seq([W(b, c, Vmat(rbc, -I)), W(a, c, Vmat(rac, -I)), W(a, b, Vmat(rab, -I))])
    M2 = register_map(o2, (a, b, c), (c, b, a), 3)
    R2 = sp.kronecker_product(I2, G(x)) * sp.kronecker_product(G(x * y), I2) * sp.kronecker_product(I2, G(y))
    exact("S4-order2-Fock=G23(x)G12(xy)G23(y)", zero_matrix(M2 - R2))
    exact("S4-both-orders-equal", zero_matrix(R1 - R2))


# ---------------- T3 ----------------
def check_M():
    r = sp.symbols("r", positive=True)
    Gm = G(r)
    A = sp.Matrix([[Gm[0, 0], Gm[0, 3]], [Gm[3, 0], Gm[3, 3]]])
    B = sp.Matrix([[Gm[1, 1], Gm[1, 2]], [Gm[2, 1], Gm[2, 2]]])
    al, be = alpha_beta(r, -I)
    exact("M1-alpha-repo-sign=+i(r^2-1)/(r^2+1)", zero(al - I * (r**2 - 1) / (r**2 + 1)))
    exact("M1-A=-1", zero_matrix(A + sp.eye(2)))
    exact("M1-B=-[[beta,alpha],[alpha,beta]]", zero_matrix(B + sp.Matrix([[be, al], [al, be]])))
    exact("M1-parity-pattern(zeros-off-blocks)",
          all(Gm[i, j] == 0 for i in range(4) for j in range(4)
              if (i in (0, 3)) != (j in (0, 3))))
    for nm, X in (("A", A), ("B", B)):
        Xc = X.applyfunc(lambda e: sp.conjugate(e))
        exact(f"M1-{nm}-unitary", zero_matrix(Xc.T * X - sp.eye(2)))
        exact(f"M1-det{nm}=1", zero(X.det() - 1))
    # Valiant p.118 identities; index 1..4 = (empty, {i}, {j}, {i,j}); two middle assignments.
    # Signs as printed in the PDF (minus signs checked on the page image, see report).
    for tag, perm in (("00,01,10,11", [0, 1, 2, 3]), ("00,10,01,11", [0, 2, 1, 3])):
        Bv = sp.Matrix(4, 4, lambda i, j: Gm[perm[i], perm[j]])
        e = lambda i, j: Bv[i - 1, j - 1]
        ids = [e(1, 1) * e(4, 4) - e(2, 2) * e(3, 3) - e(1, 4) * e(4, 1) + e(2, 3) * e(3, 2),
               e(2, 1) * e(4, 4) - e(2, 2) * e(4, 3) - e(4, 1) * e(2, 4) + e(2, 3) * e(4, 2),
               e(3, 1) * e(4, 4) + e(3, 3) * e(4, 2) - e(4, 1) * e(3, 4) - e(3, 2) * e(4, 3),
               e(1, 3) * e(4, 4) + e(3, 3) * e(2, 4) - e(1, 4) * e(4, 3) - e(2, 3) * e(3, 4),
               e(1, 2) * e(4, 4) - e(2, 2) * e(3, 4) - e(1, 4) * e(4, 2) + e(3, 2) * e(2, 4)]
        exact(f"M2-Valiant-five-identities-{tag}", all(zero(t) for t in ids))
        exact(f"M2-B(4,4)!=0-{tag}", not zero(e(4, 4)))
    # M3 second route
    th = sp.symbols("theta", real=True)
    X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -I], [I, 0]])
    H = (sp.kronecker_product(X, X) + sp.kronecker_product(Y, Y)) / 2
    E = sp.simplify((I * th * H).exp())
    target = sp.Matrix([[1, 0, 0, 0], [0, sp.cos(th), I * sp.sin(th), 0],
                        [0, I * sp.sin(th), sp.cos(th), 0], [0, 0, 0, 1]])
    exact("M3-exp(i theta (XX+YY)/2)=1+[[cos,i sin],[i sin,cos]]+1",
          all(sp.simplify((E - target)[k].rewrite(sp.exp)) == 0 for k in range(16)))
    cth, sth = 2 * r / (1 + r**2), (r**2 - 1) / (r**2 + 1)
    PV = SWAP * Vmat(r, -I)
    exact("M3-PV(r)=target(cos=2r/(1+r^2),sin=(r^2-1)/(r^2+1))",
          zero_matrix(PV - target.subs({sp.cos(th): cth, sp.sin(th): sth})))
    thr = 2 * sp.atan(r) - sp.pi / 2
    exact("M3-theta=2atan(r)-pi/2", zero(sp.expand_trig(sp.cos(thr)) - cth) and zero(sp.expand_trig(sp.sin(thr)) - sth))
    hint = target.subs({sp.cos(th): cth, sp.sin(th): -sth})     # exp(-i theta (XX+YY)/2)
    diff = (PV - hint)[1, 2]
    exact("M3-hint-sign-differs-for-r!=1", zero(diff - 2 * I * sth) and not zero(sth.subs(r, 2)))
    # M4 Jordan-Wigner
    sm = sp.Matrix([[0, 1], [0, 0]]); Z = sp.diag(1, -1); I2 = sp.eye(2)
    a1 = sp.kronecker_product(sm, I2); a2 = sp.kronecker_product(Z, sm)
    exact("M4-JW-a1^+a2+a2^+a1=(XX+YY)/2", zero_matrix(a1.T * a2 + a2.T * a1 - H))
    exact("M4-JW-anticommutation", zero_matrix(a1 * a2 + a2 * a1) and zero_matrix(a1 * a1.T + a1.T * a1 - sp.eye(4)))


def main():
    check_S1(); check_S2(); check_S3(); check_S4(); check_M()
    paths = ("scripts/verify_thirring_matchgate_a5.py", "scripts/verify_thirring_comoving_packet.py",
             "theory/THIRRING_MATCHGATE_A5_GATE.md")
    data = dict(checks=CHECKS,
                provenance={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths})
    OUT.with_suffix(".json").write_text(json.dumps(data, indent=2) + "\n")
    passed = sum(c["passed"] for c in CHECKS)
    lines = [f"Author checks: {passed}/{len(CHECKS)} exact (SymPy {sp.__version__})."]
    lines += [f"{'PASS' if c['passed'] else 'FAIL'} {c['name']}" for c in CHECKS]
    OUT.with_suffix(".txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    if passed != len(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
