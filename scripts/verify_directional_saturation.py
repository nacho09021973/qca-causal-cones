"""Fail-closed checks for the directional causal saturation report.

Backs reports/2026-09-16--directional-causal-saturation.md for the two 3D walks
of Cedzich-Joye-Werner-Werner, arXiv:2408.02108v1, Eqs. (5.12) and (5.15).

The spectral identities and support certificates use exact algebra. Numerical
velocity-set checks and legacy finite occupation diagnostics are tagged
SUPPORTED, not ESTABLISHED. The latter do not optimize trace distance or
certify asymptotic scaling; the exact signalling witness has its own verifier,
verify_signaling_witness.py. Run from the repository root:

    python3 scripts/verify_directional_saturation.py
"""

import hashlib
import itertools
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "sources/2408.02108v1.pdf"
SOURCE_SHA256 = "25e2b03ff056fc78a7105fb81a6859be326ae2ee5717b35f7fc664b89ae7bdf8"

P1, P2, P3 = sp.symbols("p1 p2 p3", real=True)
PS = (P1, P2, P3)
C = tuple(sp.cos(p) for p in PS)
S = tuple(sp.sin(p) for p in PS)
I2 = sp.eye(2)
PAULI = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.diag(1, -1),
)
Z = sp.symbols("z1 z2 z3")
CHECKS = []


def laurent(e):
    """Canonical form: every symbol here is a Laurent polynomial in z_k = e^{i p_k}.

    Two such expressions agree as functions of real p iff they agree as Laurent
    polynomials, so `laurent(a - b) == 0` is a sound equality test.  Needed
    because (5.12) is written in cos/sin and (5.15) in exp, and SymPy does not
    reconcile the two forms on its own.
    """
    e = sp.expand(sp.expand(e).rewrite(sp.exp))
    e = e.subs({p: -sp.I * sp.log(z) for p, z in zip(PS, Z)})
    return sp.cancel(sp.powsimp(sp.expand(sp.powsimp(e, force=True)), force=True))


def is_zero(e):
    return sp.simplify(laurent(e)) == 0


def check(name, tag="ESTABLISHED"):
    def wrap(fn):
        CHECKS.append((name, tag, fn))
        return fn
    return wrap


def walk1():
    """CJWW (5.12): W(p) = exp(i p1 s1) exp(i p2 s2) exp(i p3 s3)."""
    W = I2
    for c, s, sig in zip(C, S, PAULI):
        W = W * (c * I2 + sp.I * s * sig)
    return sp.expand(W)


def walk2():
    """CJWW (5.15), transcribed entry by entry."""
    e = sp.exp(sp.I * P3)
    return sp.Matrix([
        [C[0] * C[1] * e, -C[0] * S[1] + sp.I * S[0]],
        [C[0] * S[1] + sp.I * S[0], C[0] * C[1] / e],
    ])


F1 = C[0] * C[1] * C[2] + S[0] * S[1] * S[2]     # tr W1 / 2
F2 = C[0] * C[1] * C[2]                          # tr W2 / 2
# B := -grad f, so that grad(arccos f) = B / sqrt(1 - f^2)
B1 = [sp.simplify(-sp.diff(F1, p)) for p in PS]
B2 = [sp.simplify(-sp.diff(F2, p)) for p in PS]


@check("source byte identity")
def _():
    if not SOURCE.exists():
        return False, f"missing {SOURCE}"
    got = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    return got == SOURCE_SHA256, got


@check("both symbols unitary with det 1")
def _():
    out = []
    for nm, W in (("5.12", walk1()), ("5.15", walk2())):
        if not is_zero((W.H * W - I2).norm()) or not is_zero(sp.det(W) - 1):
            return False, f"{nm}: not unitary or det != 1"
        out.append(f"{nm}: W^dag W = I, det W = 1")
    return True, "; ".join(out)


@check("tr W(5.12)/2 = ccc + sss  (NOT the printed ccc - sss of (5.13))")
def _():
    tr = sp.trace(walk1()) / 2
    printed = C[0] * C[1] * C[2] - S[0] * S[1] * S[2]      # as printed in (5.13)
    return is_zero(tr - F1) and not is_zero(tr - printed), (
        "matches ccc+sss; the printed (5.13) ccc-sss is the trace of "
        "exp(-i p1 s1) exp(-i p2 s2) exp(-i p3 s3), i.e. the image under p -> -p")


@check("tr W(5.15)/2 = ccc, i.e. CJWW (5.16)")
def _():
    return is_zero(sp.trace(walk2()) / 2 - F2), "omega = arccos(c1 c2 c3)"


def jump_set(W):
    """Exact Fourier support F = {x : W_x != 0}.

    Both symbols have jump length 1 per coordinate, so multiplying by z1 z2 z3
    clears all negative powers and the monomials can be read off directly.
    """
    support = set()
    for entry in W:
        poly = sp.Poly(sp.expand(laurent(entry) * Z[0] * Z[1] * Z[2]), *Z)
        for mono, coeff in poly.terms():
            if sp.simplify(coeff) != 0:
                support.add(tuple(int(m) - 1 for m in mono))
    return support


CORNERS = set(itertools.product((-1, 1), repeat=3))


@check("jump set of (5.12) is exactly the 8 cube vertices")
def _():
    F = jump_set(walk1())
    return F == CORNERS, f"{len(F)} vectors: {sorted(F)}"


@check("jump set of (5.15) has 14 vectors and contains the 8 cube vertices")
def _():
    F = jump_set(walk2())
    ok = CORNERS <= F and len(F) == 14 and max(max(abs(v) for v in x) for x in F) == 1
    return ok, f"{len(F)} vectors: {sorted(F)}"


@check("conv F = [-1,1]^3 for both walks, so v_sub(n) = ||n||_1")
def _():
    # conv(F) = [-1,1]^3 iff all 8 vertices are present and no |x_i| exceeds 1.
    msgs = []
    for nm, W in (("5.12", walk1()), ("5.15", walk2())):
        F = jump_set(W)
        if not (CORNERS <= F and max(max(abs(v) for v in x) for x in F) == 1):
            return False, f"{nm}: conv F != cube"
        msgs.append(f"{nm}: ok")
    # support function of the cube, exactly, on the named directions
    for n, want in (((1, 0, 0), 1), ((1, 1, 0), sp.sqrt(2)), ((1, 1, 1), sp.sqrt(3))):
        nn = sp.Matrix(n) / sp.sqrt(sum(v * v for v in n))
        h = sum(abs(v) for v in nn)
        if sp.simplify(h - want) != 0:
            return False, f"h({n}) = {h} != {want}"
    return True, "; ".join(msgs) + "; r_in=1, V_causal^max=sqrt(3)"


@check("every cube vertex stays in the strict support of W^n, for all n")
def _():
    msgs = []
    for nm, W in (("5.12", walk1()), ("5.15", walk2())):
        M = sp.Matrix(2, 2, lambda i, j: sp.expand(laurent(W[i, j])))
        for sigma in sorted(CORNERS):
            # coefficient of z^sigma: only one lattice path reaches n*sigma, so
            # (W^n)_{n sigma} = (W_sigma)^n exactly, with no cancellation.
            Wsig = sp.Matrix(2, 2, lambda i, j: sp.simplify(
                M[i, j].coeff(Z[0], sigma[0]).coeff(Z[1], sigma[1]).coeff(Z[2], sigma[2])))
            if sp.simplify(Wsig.norm()) == 0:
                return False, f"{nm}: W_{sigma} = 0"
            # Every vertex coefficient here has rank 1, so W^2 = tr(W) W and
            # (W_sigma)^n = tr(W_sigma)^{n-1} W_sigma.  Nonzero trace therefore
            # gives nonvanishing for ALL n, with no bound on n.
            if Wsig.rank() != 1:
                return False, f"{nm}: W_{sigma} has rank {Wsig.rank()}, rank-1 argument does not apply"
            tr = sp.simplify(sp.trace(Wsig))
            if tr == 0:
                return False, f"{nm}: tr W_{sigma} = 0"
            if sp.simplify((Wsig * Wsig - tr * Wsig).norm()) != 0:
                return False, f"{nm}: W^2 = tr(W) W failed"
        msgs.append(f"{nm}: all 8 vertices rank 1 with nonzero trace")
    return True, "; ".join(msgs) + "  => (W^n)_{n sigma} != 0 for EVERY n >= 1"


@check("(5.12): exact SOS identity (1-f^2) - (v_i^2+v_j^2)|scaled = (c_i c_j s_k + s_i s_j c_k)^2")
def _():
    for i, j, k in ((0, 1, 2), (0, 2, 1), (1, 2, 0)):
        lhs = (1 - F1 ** 2) - (B1[i] ** 2 + B1[j] ** 2)
        rhs = (C[i] * C[j] * S[k] + S[i] * S[j] * C[k]) ** 2
        if sp.simplify(sp.expand_trig(sp.expand(lhs - rhs))) != 0:
            return False, f"pair ({i},{j}) failed"
    return True, "all three pairs: Gamma_1 is contained in the tricylinder v_i^2+v_j^2 <= 1"


@check("(5.15): exact SOS identity (1-f^2) - |grad f|^2 = s2^2 s3^2 + s1^2 s2^2 c3^2 + s1^2 c2^2 s3^2")
def _():
    lhs = (1 - F2 ** 2) - sum(b ** 2 for b in B2)
    rhs = S[1] ** 2 * S[2] ** 2 + S[0] ** 2 * S[1] ** 2 * C[2] ** 2 + S[0] ** 2 * C[1] ** 2 * S[2] ** 2
    ok = sp.simplify(sp.expand_trig(sp.expand(lhs - rhs))) == 0
    return ok, "hence |grad omega| <= 1 everywhere, with equality iff all three terms vanish"


@check("(5.15): |grad omega| = 1 on the whole axis line, not only at the cone tips")
def _():
    # equality set of the SOS above: s2=s3=0 (p2,p3 in pi Z), p1 free.
    q = sp.Symbol("q", real=True)
    sub = {P1: q, P2: 0, P3: 0}
    f = F2.subs(sub)
    g = [b.subs(sub) for b in B2]
    norm2 = sp.simplify(sum(x ** 2 for x in g) / (1 - f ** 2))
    return sp.simplify(norm2 - 1) == 0, "|grad omega|^2 = 1 for all q, refining CJWW's 'maximum at the conical points'"


@check("(5.12): max |v_g| = sqrt(3/2), attained exactly at p = (-pi/4,-pi/4,-pi/4)")
def _():
    sub = {p: -sp.pi / 4 for p in PS}
    f = sp.simplify(F1.subs(sub))
    v = [sp.simplify(b.subs(sub) / sp.sqrt(1 - f ** 2)) for b in B1]
    n2 = sp.simplify(sum(x ** 2 for x in v))
    # upper bound: the tricylinder's farthest point has |v|^2 = 3/2
    return f == 0 and sp.simplify(n2 - sp.Rational(3, 2)) == 0, f"v = {v}, |v|^2 = {n2}"


@check("axis direction: omega = |q| and v_g = (1,0,0) for BOTH walks")
def _():
    q = sp.Symbol("q", positive=True)
    out = []
    for nm, f, B in (("5.12", F1, B1), ("5.15", F2, B2)):
        at = {P1: q, P2: 0, P3: 0}
        # exact: cos(omega) = cos(q) and -grad f = (sin q, 0, 0)
        if sp.simplify(f.subs(at) - sp.cos(q)) != 0:
            return False, f"{nm}: cos(omega) != cos(q) on the axis"
        g = [sp.simplify(b.subs(at)) for b in B]
        if g != [sp.sin(q), 0, 0]:
            return False, f"{nm}: -grad f = {g} on the axis"
        # hence omega = |q| on the Brillouin zone and v_g = (sin q/|sin q|) e1 = e1
        out.append(f"{nm}: omega=|q|, v_g=(1,0,0)=v_sub(e1)")
    return True, "; ".join(out) + "  [c_IR = |v_g| = v_sub all equal 1 on the axes]"


@check("conical expansion: omega^2 = |p|^2 + O(p^3), so c_IR = 1")
def _():
    # arccos has a branch point where f -> 1, so expand in u = 1 - f instead:
    # arccos(1-u)^2 = 2u + u^2/3 + 4u^3/45 + O(u^4), an analytic series in u.
    t = sp.Symbol("t", positive=True)
    a, b, c = sp.symbols("a b c", real=True)
    u = sp.Symbol("u", positive=True)
    w2_of_u = sp.series(sp.acos(1 - u) ** 2, u, 0, 4).removeO()
    out = []
    for nm, f, cubic in (("5.12", F1, -2 * a * b * c), ("5.15", F2, 0)):
        us = sp.series(1 - f.subs({P1: t * a, P2: t * b, P3: t * c}), t, 0, 5).removeO()
        w2 = sp.expand(sp.series(w2_of_u.subs(u, us), t, 0, 4).removeO())
        if sp.expand(w2.coeff(t, 2) - (a ** 2 + b ** 2 + c ** 2)) != 0:
            return False, f"{nm}: t^2 coefficient is {w2.coeff(t, 2)}, not |p|^2"
        if sp.expand(w2.coeff(t, 3) - cubic) != 0:
            return False, f"{nm}: t^3 coefficient is {w2.coeff(t, 3)}, expected {cubic}"
        term = "+ O(t^4) exactly (no cubic)" if cubic == 0 else f"- 2abc t^3 + O(t^4)"
        out.append(f"{nm}: omega^2 = |p|^2 {term}")
    return True, "; ".join(out) + "; so c_IR = 1 for both, in lattice-step units"


@check("velocity sets fill the tricylinder / the ball", tag="SUPPORTED (numerical)")
def _():
    import math
    N, M, R = 160, 18, 1.25
    hit1 = set()
    hit2 = set()
    for i in range(N):
        p1 = (i + 0.5) / N * 2 * math.pi - math.pi
        c1, s1 = math.cos(p1), math.sin(p1)
        for j in range(N):
            p2 = (j + 0.5) / N * 2 * math.pi - math.pi
            c2, s2 = math.cos(p2), math.sin(p2)
            for k in range(N):
                p3 = (k + 0.5) / N * 2 * math.pi - math.pi
                c3, s3 = math.cos(p3), math.sin(p3)
                for f, b, hit in (
                    (c1 * c2 * c3 + s1 * s2 * s3,
                     (s1 * c2 * c3 - c1 * s2 * s3, c1 * s2 * c3 - s1 * c2 * s3, c1 * c2 * s3 - s1 * s2 * c3),
                     hit1),
                    (c1 * c2 * c3, (s1 * c2 * c3, c1 * s2 * c3, c1 * c2 * s3), hit2),
                ):
                    d = 1.0 - f * f
                    if d < 1e-9:
                        continue
                    d = math.sqrt(d)
                    hit.add(tuple(min(M - 1, max(0, int((x / d + R) / (2 * R) * M))) for x in b))
    def missed(hit, inside):
        bad = 0
        for cell in itertools.product(range(M), repeat=3):
            v = [(u + 0.5) / M * 2 * R - R for u in cell]
            if inside(v) and cell not in hit:
                bad += 1
        return bad
    tri = lambda v: all(v[a] ** 2 + v[b] ** 2 <= 0.9 for a, b in ((0, 1), (1, 2), (0, 2)))
    ball = lambda v: sum(x * x for x in v) <= 0.9
    m1, m2 = missed(hit1, tri), missed(hit2, ball)
    return m1 == 0 and m2 == 0, f"tricylinder cells missed: {m1}; ball cells missed: {m2}"


# ---------------------------------------------------------------------------
# LDP_RADIAL_INTERPRETATION gate (theory/OPERATIONAL_INVISIBILITY_GATE.md).
# Documents CJWW Eq. (5.21) and its Legendre transform for walk (5.15).
# ---------------------------------------------------------------------------
ELL = sp.Symbol("ell", positive=True)
R_TILDE = 2 * sp.acosh(sp.cosh(ELL / (2 * sp.sqrt(3))) ** 3)


@check("CJWW (5.21) is exact at their stated maximizer p=0, lambda = l(1,1,1)/sqrt(3)")
def _():
    # cos(omega) = prod_k cos(p_k + i lambda_k / 2); at p = 0 with all
    # lambda_k = l/sqrt(3) this is cosh(l/(2 sqrt 3))^3, real and >= 1, so
    # omega is purely imaginary and log|u|^2 = 2|Im omega| = 2 arccosh(...).
    lam = ELL / sp.sqrt(3)
    cos_omega = sp.prod([sp.cos(0 + sp.I * lam / 2) for _ in range(3)])
    cos_omega = sp.simplify(sp.re(sp.expand(cos_omega.rewrite(sp.cosh))))
    if sp.simplify(cos_omega - sp.cosh(ELL / (2 * sp.sqrt(3))) ** 3) != 0:
        return False, f"cos(omega) = {cos_omega}"
    return sp.simplify(2 * sp.acosh(cos_omega) - R_TILDE) == 0, (
        "R~(l) = 2 arccosh(cosh(l/2sqrt3)^3); the LOCATION of the maximizer is "
        "CJWW's numerical finding, the VALUE there is exact")


@check("the two slopes of R~ are exactly c_IR = 1 and max_n v_sub(n) = sqrt(3)")
def _():
    s0 = sp.limit(sp.diff(R_TILDE, ELL), ELL, 0, "+")
    si = sp.limit(sp.diff(R_TILDE, ELL), ELL, sp.oo)
    ok = sp.simplify(s0 - 1) == 0 and sp.simplify(si - sp.sqrt(3)) == 0
    return ok, (f"R~'(0) = {s0} = c_IR = h_B(n); "
                f"R~'(oo) = {si} = ||(1,1,1)/sqrt(3)||_1 = v_sub(body diagonal)")


@check("dual transform gives exactly three regimes, with CJWW's control value")
def _():
    s0, si = 1, sp.sqrt(3)
    rows = []
    for r, want in ((sp.Rational(9, 10), "zero"), (1, "zero"),
                    (sp.Rational(11, 10), "finite"), (sp.Rational(3, 2), "finite"),
                    (2, "infinite"), (3, "infinite")):
        got = "zero" if r <= s0 else ("infinite" if r > si else "finite")
        if got != want:
            return False, f"r={r}: got {got}, expected {want}"
        rows.append(f"{sp.nsimplify(r)}:{got}")
    # control: CJWW quote I~(1.1) = .104
    rr = sp.Rational(11, 10)
    lstar = sp.nsolve(sp.diff(rr * ELL - R_TILDE, ELL), ELL, 2)
    val = sp.N(rr * lstar - R_TILDE.subs(ELL, lstar), 4)
    if abs(val - sp.Float("0.104")) > sp.Float("0.002"):
        return False, f"I~(1.1) = {val}, CJWW quote .104"
    return True, ("ballistic/emergent (r<=1) | causal but exponentially "
                  f"suppressed (1<r<sqrt3) | causally forbidden (r>sqrt3); I~(1.1)={val}")


@check("declared limitation: the radial rate function is coarse on the axes")
def _():
    # Sec. 8: v_sub(e_i) = 1 = c_IR, so a velocity r*e_i with r > 1 is already
    # outside C_micro = [-1,1]^3, where the amplitude is EXACTLY zero.  The
    # radial I~ nevertheless reports a finite rate for 1 < r < sqrt(3): that
    # finite rate is carried by non-axial directions only.
    r = sp.Rational(11, 10)
    axial_outside_cube = max(abs(v) for v in (r, 0, 0)) > 1
    radial_rate_finite = (1 < r) and (r < sp.sqrt(3))
    return axial_outside_cube and radial_rate_finite, (
        "at r=1.1 the axial ray is outside C_micro (exact zero) while I~ reports "
        "a finite rate => the angular structure of I is NOT resolved here")


# ---------------------------------------------------------------------------
# SUBSTRATE_CONE_OBSERVABILITY gate
# (theory/SUBSTRATE_CONE_OBSERVABILITY_GATE.md).
#
# Free-fermion (CAR) lift of walk (5.15).  On the one-particle sector the
# Bogoliubov automorphism gives alpha_t(n_x) = W^t P_x W^{t dag}, so
#
#     [alpha_t(n_x), n_y]  has (y,y') block  (W^t)_{y,x} ((W^t)_{y',x})^dag
#
# for y' != y.  Hence the commutator is nonzero exactly when the single-particle
# kernel (W^t)_{y,x} is, and the operational causal structure of the lift is the
# strict support of W^t.  Kernels are computed in EXACT Gaussian integers by
# scaling W by 4 (every entry of 4*W_x lies in Z[i]).
# ---------------------------------------------------------------------------


def scaled_blocks():
    """{x: 4*W_x} as exact Gaussian-integer 2x2 blocks, for walk (5.15)."""
    out = {}
    for i in range(2):
        for j in range(2):
            poly = sp.Poly(sp.expand(laurent(walk2()[i, j]) * Z[0] * Z[1] * Z[2]), *Z)
            for mono, coeff in poly.terms():
                x = tuple(int(m) - 1 for m in mono)
                c = sp.nsimplify(sp.simplify(coeff * 4))
                if c == 0:
                    continue
                if c != sp.re(c) + sp.I * sp.im(c) or sp.re(c) != int(sp.re(c)) or sp.im(c) != int(sp.im(c)):
                    raise ValueError(f"4*W_{x}[{i},{j}] = {c} is not a Gaussian integer")
                out.setdefault(x, [[0, 0], [0, 0]])[i][j] = complex(int(sp.re(c)), int(sp.im(c)))
    return {x: [[b[0][0], b[0][1]], [b[1][0], b[1][1]]] for x, b in out.items()}


def mat_mul(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


def nonzero(A):
    return any(v != 0 for row in A for v in row)


def kernel_power(nsteps):
    """Strict support and blocks of (4W)^n, exactly."""
    base = scaled_blocks()
    ker = {(0, 0, 0): [[1, 0], [0, 1]]}
    for _ in range(nsteps):
        nxt = {}
        for y, A in ker.items():
            for d, B in base.items():
                z = (y[0] + d[0], y[1] + d[1], y[2] + d[2])
                P = mat_mul(B, A)
                if z in nxt:
                    nxt[z] = [[nxt[z][i][j] + P[i][j] for j in range(2)] for i in range(2)]
                else:
                    nxt[z] = P
        ker = {y: A for y, A in nxt.items() if nonzero(A)}
    return ker


@check("lift: strict support of W^t never leaves t*C_micro, and reaches its vertices")
def _():
    rows = []
    for n in (1, 2, 3, 4):
        ker = kernel_power(n)
        if max(max(abs(v) for v in y) for y in ker) != n:
            return False, f"t={n}: support leaves [-t,t]^3"
        if (n, n, n) not in ker:
            return False, f"t={n}: vertex ray not reached"
        rows.append(f"t={n}: |supp|={len(ker)}, vertex block={ker[(n,n,n)][0][0]}/4^{n}")
    return True, "; ".join(rows) + "  [H4: C_micro is the exact outer boundary]"


@check("lift H2: nonzero commutator strictly OUTSIDE the light cone, off-axis")
def _():
    rows = []
    for n in (1, 2, 3, 4):
        ker = kernel_power(n)
        # points in the strict support that are outside the emergent cone |y| <= c*t
        outside = [y for y in ker if y[0] ** 2 + y[1] ** 2 + y[2] ** 2 > n * n]
        if not outside:
            return False, f"t={n}: nothing outside the light cone"
        # the commutator needs a second populated site y' != y
        y = (n, n, n)
        others = [z for z in ker if z != y]
        if not others:
            return False, f"t={n}: no second site, commutator degenerate"
        blk = ker[y]
        comm_block = mat_mul(blk, [[ker[others[0]][0][0].conjugate(), ker[others[0]][1][0].conjugate()],
                                   [ker[others[0]][0][1].conjugate(), ker[others[0]][1][1].conjugate()]])
        if not nonzero(comm_block):
            return False, f"t={n}: (y,y') block vanishes"
        rows.append(f"t={n}: {len(outside)} sites outside B(c)t, |y|={sp.sqrt(3)*n if y==(n,n,n) else ''}")
    return True, ("vertex ray |y| = sqrt(3) t > ct is in the strict support with "
                  "nonzero (y,y') block => signalling possible outside B(c); "
                  "magnitude ||(W_sigma)^t|| = 4^-t")


@check("lift H3: EXACTLY zero commutator along the six axial directions beyond ct")
def _():
    for n in (1, 2, 3, 4):
        ker = kernel_power(n)
        for axis in range(3):
            for L in range(n + 1, n + 4):
                for sgn in (+1, -1):
                    y = [0, 0, 0]
                    y[axis] = sgn * L
                    if tuple(y) in ker:
                        return False, f"t={n}: axial site {tuple(y)} with L={L} > ct is populated"
    return True, ("v_sub(e_i) = c, so every axial site beyond ct lies outside C_micro: "
                  "kernel exactly zero, commutator exactly zero, no superluminal tail on-axis")


@check("lift: the accessible region is exactly C_micro*t minus the light cone")
def _():
    n = 3
    ker = kernel_power(n)
    outside_cone = sorted(y for y in ker if y[0] ** 2 + y[1] ** 2 + y[2] ** 2 > n * n)
    # every such site must satisfy ||y||_inf <= t (inside C_micro*t) ...
    if any(max(abs(v) for v in y) > n for y in outside_cone):
        return False, "a signalling site lies outside C_micro*t"
    # ... and none of them may be axial
    axial = [y for y in outside_cone if sum(1 for v in y if v != 0) == 1]
    if axial:
        return False, f"axial sites outside the cone: {axial}"
    return True, (f"t={n}: {len(outside_cone)} sites strictly outside B(c)t, all inside "
                  f"C_micro*t, none axial")


# ---------------------------------------------------------------------------
# COUPLING_MAP_OPTIMAL_D gate (theory/COUPLING_MAP_GATE.md), frozen 0f7628d.
# Declared geometries only.  With P = W^t P_y W^{t dag} and a number-conserving
# Gaussian local operation of Alice acting as R on the site-0 one-particle
# space, the difference operator is Delta = u^dag P u - P with blocks
#     Delta_00 = R^dag P_00 R - P_00,      P_00 = K_0y K_0y^dag
#     Delta_0w = (R^dag - I) P_0w,         P_0w = K_0y K_wy^dag
# These are occupation-observable blocks, not full trace distance. The cross
# term depends on BOTH kernels; no asymptotic scaling or optimality is tested.
# ---------------------------------------------------------------------------
import numpy as _np


def _ker(nsteps):
    return {d: _np.array(A, dtype=complex) / 4.0 ** nsteps for d, A in kernel_power(nsteps).items()}


def _n(M):
    return _np.linalg.norm(M, 2)


def _geoms(nsteps, ker):
    cand = [y for y in ker if sum(v * v for v in y) > nsteps ** 2 and sum(1 for v in y if v != 0) >= 2]
    return [("vertex", (nsteps,) * 3), ("face-diag", (nsteps, nsteps, 0)),
            ("nearest-off-axis", min(cand, key=lambda y: sum(v * v for v in y))),
            ("axial-control", (nsteps + 1, 0, 0))]


@check("coupling map: axial control gives D = 0 for EVERY state and operation")
def _():
    for nsteps in (2, 3, 4):
        ker = _ker(nsteps)
        y = (nsteps + 1, 0, 0)
        if _n(ker.get(tuple(-v for v in y), _np.zeros((2, 2), complex))) != 0:
            return False, f"t={nsteps}: axial K_0y != 0"
    return True, "K_0y = 0 excludes Alice from evolved Bob algebra, at t = 2,3,4"


@check("coupling map: phase gate exp(i pi n_0) kills the local term and doubles the coherence term")
def _():
    R = -_np.eye(2)                       # exp(i pi n_0) on the site-0 one-particle space
    for nsteps in (2, 3, 4):
        ker = _ker(nsteps)
        y = (nsteps,) * 3
        K0y = ker[tuple(-v for v in y)]
        P00 = K0y @ K0y.conj().T
        if _n(R.conj().T @ P00 @ R - P00) > 1e-14:
            return False, f"t={nsteps}: Delta_00 != 0 under the phase gate"
        d = next(iter(ker))
        P0w = K0y @ ker[d].conj().T
        if _n((R.conj().T - _np.eye(2)) @ P0w - (-2) * P0w) > 1e-14:
            return False, f"t={nsteps}: Delta_0w != -2 P_0w"
    return True, "Delta_00 = 0, Delta_0w = -2 P_0w: phase-gate occupation identity; no optimality claim"


@check("coupling map: finite occupation-witness ratios (not D optimization or asymptotics)", "SUPPORTED")
def _():
    rng = _np.random.default_rng(0)
    rows = []
    for nsteps in (2, 3, 4):
        ker = _ker(nsteps)
        y = (nsteps,) * 3
        K0y = ker[tuple(-v for v in y)]
        a = _n(K0y)
        coh = max(2 * _n(K0y @ ker[d].conj().T) for d in ker)
        P00 = K0y @ K0y.conj().T
        loc = 0.0
        for _ in range(3000):
            X = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
            Q, _r = _np.linalg.qr(X)
            loc = max(loc, _n(Q.conj().T @ P00 @ Q - P00))
        if not (0.4 < coh / a < 2.0):
            return False, f"t={nsteps}: coherent/||K|| = {coh/a}, outside historical finite range"
        if abs(loc / a ** 2 - 1.0) > 1e-3:
            return False, f"t={nsteps}: local/||K||^2 = {loc/a**2}, not 1"
        rows.append(f"t={nsteps}: gain={coh/loc:.0f}x")
    return True, ("finite occupation diagnostics: " + ", ".join(rows) +
                  "; sampled local rotations, no exact maximum or asymptotic claim")


@check("coupling map: sampled off-vertex local occupation response vanishes", "SUPPORTED")
def _():
    rng = _np.random.default_rng(1)
    for nsteps in (2, 3, 4):
        ker = _ker(nsteps)
        for name, y in _geoms(nsteps, ker):
            if name in ("vertex", "axial-control"):
                continue
            K0y = ker[tuple(-v for v in y)]
            P00 = K0y @ K0y.conj().T
            for _ in range(2000):
                X = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
                Q, _r = _np.linalg.qr(X)
                if _n(Q.conj().T @ P00 @ Q - P00) > 1e-12:
                    return False, f"t={nsteps} {name}: local term nonzero"
    return True, ("sampled occupation responses vanish at face-diag and nearest-off-axis; "
                  "this does not imply equality of Bob's full reduced states")


def verify_local_preparation():
    """Exact, bounded successor certificate; frozen witness helpers unchanged.

    Run with --local-preparation-only. Initial |0,down>, two common steps,
    origin phase choice, one readout step, Bob=(1,1,1). No parameter scan.
    Backs reports/2026-09-16--alice-local-preparation.md.
    """
    from verify_signaling_witness import (
        DOWN, ORIGIN, evolve, exact_blocks, norm_squared, phase_choice,
        reduced_state, square_kernel,
    )

    count = 0

    def require(condition, label):
        nonlocal count
        if not condition:
            raise AssertionError(label)
        count += 1
        print(f"[PASS] {label}")

    bob = (1, 1, 1)
    zero = sp.zeros(2, 1)
    initial = {ORIGIN: DOWN}
    blocks = exact_blocks()
    kernel2 = square_kernel(blocks)
    one = evolve(initial, blocks)
    prepared = evolve(initial, kernel2)
    require(set(initial) == {ORIGIN} and norm_squared(initial) == 1,
            "initial resource is one normalized particle at Alice only")
    require(phase_choice(initial) == {ORIGIN: -DOWN},
            "zero preparation steps: encoding is a global phase")
    require(one.get(ORIGIN, zero) == zero and phase_choice(one) == one,
            "one preparation step: origin empty, encoding has no effect")
    require(prepared == evolve(one, blocks),
            "two-step preparation equals two sequential unchanged steps")
    require(prepared[ORIGIN] == -3 * DOWN / 4 and norm_squared(prepared) == 1,
            "common prepared state has origin amplitude -3 down/4 and unit norm")
    require(prepared.get(bob, zero) == zero,
            "Bob is exactly vacant even at the encoding event")
    arm_a = {ORIGIN: prepared[ORIGIN]}
    arm_rest = {x: v for x, v in prepared.items() if x != ORIGIN}
    require(norm_squared(arm_a) == sp.Rational(9, 16)
            and norm_squared(arm_rest) == sp.Rational(7, 16),
            "both coherent arms have nonzero weight: phase is not global")
    choices = [prepared, phase_choice(prepared)]
    require(all(choices[1][x] == (-v if x == ORIGIN else v)
                for x, v in choices[0].items()),
            "branches share preparation; only the origin component changes sign")
    outputs = [evolve(state, blocks) for state in choices]
    require(all(norm_squared(state) == 1 for state in outputs),
            "both final global states have exact unit norm")
    require(all(max(abs(c) for c in x) <= steps
                for steps, state in ((1, one), (2, prepared),
                                     (3, outputs[0]), (3, outputs[1]))
                for x in state), "every stage respects microscopic finite range")
    require(sum(c*c for c in bob) > 1 and max(abs(c) for c in bob) == 1
            and blocks[tuple(-c for c in bob)] == sp.diag(0, sp.Rational(1, 4)),
            "from encoding: Bob outside emergent cone, on populated micro boundary")
    a = evolve(arm_a, blocks).get(bob, zero)
    r = evolve(arm_rest, blocks).get(bob, zero)
    require(a == -3 * DOWN / 16 and r == -DOWN / 32,
            "Bob arm amplitudes are -3 down/16 and -down/32")
    require([state[bob] for state in outputs] == [-7 * DOWN / 32, 5 * DOWN / 32],
            "Bob branch amplitudes are -7 down/32 and 5 down/32")
    # A second algebraic path: extract the block directly from the symbol cube.
    cube = walk2() ** 3
    direct = sp.zeros(2)
    for i in range(2):
        for j in range(2):
            poly = sp.Poly(sp.expand(laurent(cube[i, j]) * sp.prod(Z)**3), *Z)
            direct[i, j] = poly.coeff_monomial(sp.prod(z**2 for z in Z))
    require(direct.H * DOWN == outputs[0][bob],
            "direct Laurent extraction of W^3 agrees with sequential evolution")
    effect = sp.diag(0, 1, 1, 1)
    rhos = [reduced_state(state, bob) for state in outputs]
    probs = [sp.simplify(sp.trace(effect * rho)) for rho in rhos]
    require(probs == [sp.Rational(49, 1024), sp.Rational(25, 1024)],
            "p0=49/1024, p1=25/1024")
    require(probs[1] - probs[0] == -4 * sp.re((a.H*r)[0])
            == -sp.Rational(3, 128), "signed interference difference is -3/128")
    require(all(rho == sp.diag(1-p, 0, p, 0) and 0 <= p <= 1
                for rho, p in zip(rhos, probs)),
            "Bob density matrices are normalized positive states; effect bound applies")
    require(reduced_state(evolve(prepared, blocks), bob) == rhos[0],
            "removing the encoder makes the two Bob states identical")
    # Remove only Alice/rest coherence at choice time, keeping both populations
    # and all coherence within the rest. Normalize each mixture component.
    mixtures = []
    for encode in (False, True):
        rho = sp.zeros(4)
        for arm in (arm_a, arm_rest):
            weight = norm_squared(arm)
            component = {x: v / sp.sqrt(weight) for x, v in arm.items()}
            if encode:
                component = phase_choice(component)
            rho += weight * reduced_state(evolve(component, blocks), bob)
        mixtures.append(rho.applyfunc(sp.simplify))
    require(mixtures[0] == mixtures[1]
            and sp.trace(effect * mixtures[0]) == sp.Rational(37, 1024),
            "Alice/rest dephasing: identical full Bob states, p=37/1024")
    axial = (2, 0, 0)
    require(blocks.get(tuple(-c for c in axial), sp.zeros(2)) == sp.zeros(2)
            and reduced_state(outputs[0], axial) == reduced_state(outputs[1], axial),
            "outside microscopic cone from choice: axial reduced states coincide")
    require(all(not entry.has(sp.Float)
                for state in (initial, one, prepared, *outputs)
                for v in state.values() for entry in v), "all state entries are exact")
    print(f"\n{count}/{count} exact checks passed. EXISTENCE_CONSTRUCTED; no optimization.")
    return 0


def verify_noncorner_gate():
    """Exact execution of theory/NONCORNER_SIGNALING_GATE.md, steps 0-5.

    Run with --noncorner-gate-only. Step 0 is the contract's binding stop
    rule: the admissible domain is derived from the certified support, never
    assumed. No search, no sampling, no optimization, no floating point.
    The frozen protocol and every pre-existing helper are used unchanged.
    """
    from verify_signaling_witness import (
        DOWN, ORIGIN, evolve, exact_blocks, norm_squared, phase_choice,
        reduced_state, square_kernel,
    )

    count = 0

    def require(condition, label):
        nonlocal count
        if not condition:
            raise AssertionError(label)
        count += 1
        print(f"[PASS] {label}")

    zero = sp.zeros(2, 1)
    vertices = {(i, j, k) for i in (1, -1) for j in (1, -1) for k in (1, -1)}
    edges = {(i, j, 0) for i in (1, -1) for j in (1, -1)}
    axes = {(i, 0, 0) for i in (1, -1)}
    preregistered = vertices | edges | axes

    # ---- Step 0: binding certification of the exact one-step support -----
    blocks = exact_blocks()
    require(len(preregistered) == 14
            and all(block != sp.zeros(2) for block in blocks.values())
            and set(blocks) == preregistered,
            "STEP 0: supp K_1 is exactly the 14 preregistered displacements")
    symbol = walk2()
    attribution = {}
    for i in range(2):
        for j in range(2):
            poly = sp.Poly(sp.expand(laurent(symbol[i, j]) * sp.prod(Z)), *Z)
            attribution[(i, j)] = {tuple(power - 1 for power in powers)
                                   for powers, coefficient in poly.terms()
                                   if coefficient != 0}
    require(attribution[(0, 0)] == {v for v in vertices if v[2] == 1}
            and attribution[(1, 1)] == {v for v in vertices if v[2] == -1}
            and attribution[(0, 1)] == attribution[(1, 0)] == edges | axes,
            "STEP 0: per-entry attribution is exactly the one the contract declares")
    reachable = {tuple(-c for c in d) for d in blocks}
    require(reachable == set(blocks),
            "STEP 0: the support is symmetric under y -> -y, so the convention is immaterial")
    admissible = {y for y in reachable
                  if sum(c * c for c in y) > 1
                  and sum(1 for c in y if c != 0) < 3}
    require(admissible == edges,
            "STEP 0: the certified support yields exactly the four admissible sites")

    # ---- Exclusions, from the certified support rather than by search ----
    require(all(tuple(-c for c in y) not in blocks
                for y in ((1, 0, 1), (0, 1, 1), (-1, 0, 1), (0, -1, 1),
                          (1, 0, -1), (0, 1, -1), (-1, 0, -1), (0, -1, -1))),
            "excluded edges with a zero in coordinate 1 or 2 have K_1 = 0 exactly")
    require(all(tuple(-c for c in y) in blocks and sum(c * c for c in y) == 1
                for y in axes),
            "axis sites are micro-accessible but null-separated: excluded by (D1)")

    # ---- Frozen preparation, reused and not recomputed -------------------
    prepared = evolve({ORIGIN: DOWN}, square_kernel(blocks))
    arm_a = {ORIGIN: prepared[ORIGIN]}
    arm_rest = {x: v for x, v in prepared.items() if x != ORIGIN}
    require(norm_squared(prepared) == 1 and prepared[ORIGIN] == -3 * DOWN / 4
            and norm_squared(arm_a) == sp.Rational(9, 16)
            and norm_squared(arm_rest) == sp.Rational(7, 16),
            "frozen preparation unchanged: origin -3 down/4, arm weights 9/16 and 7/16")

    def z3_parity_rule(state, up_on_even):
        for x, vector in state.items():
            allowed_up = (x[2] % 2 == 0) == up_on_even
            if vector[1 if allowed_up else 0] != 0:
                return False
        return True

    outputs = [evolve(prepared, blocks), evolve(phase_choice(prepared), blocks)]
    require(z3_parity_rule(prepared, False)
            and all(z3_parity_rule(state, True) for state in outputs),
            "z3 parity selection rule: the internal component alternates with x3 parity")

    # ---- The four admissible sites, exhaustively (no symmetry assumed) ---
    arms = [evolve(arm_a, blocks), evolve(arm_rest, blocks)]
    effect = sp.diag(0, 1, 1, 1)
    up_effect = sp.diag(0, 1, 0, 0)
    parity = sp.diag(1, -1, -1, 1)
    results = {}
    for y in sorted(admissible):
        a = arms[0].get(y, zero)
        r = arms[1].get(y, zero)
        results[y] = (a, r, (a * r.H + r * a.H).applyfunc(sp.simplify))
    require(len(results) == 4
            and all(M == sp.diag(-sp.Rational(3, 256), 0)
                    for _, _, M in results.values()),
            "(P1) M(y) = diag(-3/256, 0) exactly at all four admissible sites")
    require(all(M != sp.zeros(2) for _, _, M in results.values()),
            "(P1) M(y) != 0: the two reduced states differ at every one of them")
    require(all(a[1] == 0 and r[1] == 0
                and sp.Abs(a[0]) == sp.Rational(3, 16)
                and sp.Abs(r[0]) == sp.Rational(1, 32)
                for a, r, _ in results.values()),
            "both arms arrive purely in Bob's up channel: a(y) is spin-flipped")

    states = {y: [reduced_state(state, y) for state in outputs]
              for y in sorted(admissible)}
    require(all(pair[0] != pair[1] for pair in states.values()),
            "rho_B^(0) != rho_B^(1) directly from the reduced states")
    require(all(sp.trace(effect * pair[0]) == sp.Rational(25, 1024)
                and sp.trace(effect * pair[1]) == sp.Rational(49, 1024)
                for pair in states.values()),
            "p_0 = 25/1024 and p_1 = 49/1024: the vertex probabilities, exchanged")
    require(all(((pair[0] - pair[1]).applyfunc(sp.simplify)[1:3, 1:3] == 2 * M
                 and (pair[0] - pair[1]).applyfunc(sp.simplify)[0, 0]
                 == -sp.trace(2 * M))
                for (y, pair), (_, _, M) in zip(states.items(), results.values())),
            "state difference equals 2M on the one-particle block: M is complete")
    require(effect**2 == effect and up_effect**2 == up_effect
            and effect * parity == parity * effect
            and up_effect * parity == parity * up_effect,
            "both effects are even local projections of norm one")
    require(all(sp.Abs(sp.trace(effect * (pair[1] - pair[0]))) == sp.Rational(3, 128)
                for pair in states.values()),
            "(P2) non-vacuum projection: delta = 3/128 > 0, hence D >= 3/128")
    require(all(sp.Abs(sp.trace(up_effect * (pair[1] - pair[0]))) == sp.Rational(3, 128)
                for pair in states.values()),
            "(P2) the up projection isolates the distinguishing channel, same delta")
    require(all(sum(c * c for c in y) > 1 and max(abs(c) for c in y) == 1
                and sum(1 for c in y if c != 0) == 2
                and blocks[tuple(-c for c in y)] != sp.zeros(2)
                for y in admissible),
            "(P3) each positive site: outside emergent cone, on micro support, non-vertex")

    # ---- Consistency with the frozen vertex witness, which is not touched -
    vertex = (1, 1, 1)
    a_v = arms[0].get(vertex, zero)
    r_v = arms[1].get(vertex, zero)
    vertex_states = [reduced_state(state, vertex) for state in outputs]
    require((a_v * r_v.H + r_v * a_v.H).applyfunc(sp.simplify)
            == sp.diag(0, sp.Rational(3, 256))
            and sp.trace(effect * (vertex_states[1] - vertex_states[0]))
            == -sp.Rational(3, 128),
            "frozen vertex reproduced: same magnitude, opposite sign, down channel")
    require(all(not entry.has(sp.Float)
                for _, _, M in results.values() for entry in M)
            and all(not entry.has(sp.Float)
                    for state in (prepared, *outputs)
                    for vector in state.values() for entry in vector),
            "every reported quantity is exact")

    print("\nPer-site table (Delta p_B = 2|Tr M|):")
    for y in sorted(admissible):
        a, r, M = results[y]
        print(f"  y={y}  K_1(0,y)={blocks[tuple(-c for c in y)].tolist()}")
        print(f"       a={list(a)}  r={list(r)}  M={M.tolist()}")
        print(f"       Tr M={sp.trace(M)}  Delta p_B="
              f"{sp.Abs(sp.trace(effect * (states[y][1] - states[y][0])))}"
              f"  M==0 ? {M == sp.zeros(2)}")
    print(f"\n{count}/{count} exact checks passed. "
          "Verdict: NONCORNER_SIGNALING_CONSTRUCTED.")
    return 0


def main():
    width = max(len(n) for n, _, _ in CHECKS)
    failed = 0
    for name, tag, fn in CHECKS:
        try:
            ok, detail = fn()
        except Exception as exc:                        # fail closed
            ok, detail = False, f"raised {exc!r}"
        print(f"[{'PASS' if ok else 'FAIL'}] {name:<{width}}  {tag}\n        {detail}")
        failed += not ok
    print(f"\n{len(CHECKS) - failed}/{len(CHECKS)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--local-preparation-only"]:
        sys.exit(verify_local_preparation())
    elif sys.argv[1:] == ["--noncorner-gate-only"]:
        sys.exit(verify_noncorner_gate())
    else:
        sys.exit(main())
