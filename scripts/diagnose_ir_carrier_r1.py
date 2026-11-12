"""Stage A(iv) diagnostic of theory/IR_CARRIER_DICHOTOMY_GATE.md (regime R1).

For the R1 walks of the second general-rate diagnostic (CJWW (5.12), Pavia
A+, cyclic s=4), with the same regions, evaluates at each dominant momentum
with trivial character: omega = e^(i phi), the phase psi_k, the average
mu_k of the depth factor under H9(ii), and the conditions H6_k and H10_k
of draft Amendment 1 to the carrier charter. Reuses read-only the scripts
diagnose_general_ir_rate_round2.py and diagnose_general_ir_rate_polyhedra.py.
Floating point: a diagnostic, not a verification of any hypothesis.

Run from the repository root:
    python3 -B scripts/diagnose_ir_carrier_r1.py --output reports/<name>.json
"""
import argparse
import json
import sys
from fractions import Fraction
from math import gcd
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import diagnose_general_ir_rate_round2 as R2  # noqa: E402

P = R2.P
R1_IDS = ("W2", "W3", "W6", "W5")   # W5: erratum check of the round-2 tail only


def tail_full(wB, A, c, Q, col, d):
    """Free tail in the full internal space. P.tail works in nodal coordinates
    (A = Q^dagger D Q); attempt 1 passed Q[:, col] (full-space coordinates) to it,
    which mixes bases whenever Q is not the standard basis (W5, W6, Z7)."""
    e = np.eye(2)[:, col]
    R_nodal, I0, I1 = P.tail(wB, A, c, e, d)
    return Q @ R_nodal
N_TERMS = 400


def ext_gcd_solution(a):
    """integer n with a.n = gcd(a) (= 1 for primitive a)."""
    a = list(a)
    cur_g, cur = a[0], [1] + [0] * (len(a) - 1)
    for i in range(1, len(a)):
        x, y = cur_g, a[i]
        old_r, r = x, y
        old_s, s = 1, 0
        old_t, t = 0, 1
        while r != 0:
            q = old_r // r
            old_r, r = r, old_r - q * r
            old_s, s = s, old_s - q * s
            old_t, t = t, old_t - q * t
        cur = [c * old_s for c in cur]
        cur[i] = old_t
        cur_g = old_r
    if cur_g < 0:
        cur, cur_g = [-c for c in cur], -cur_g
    return cur, cur_g


def complex_hessian_log(sym, k, xi, lam_k):
    h = 1e-4
    d = len(k)
    f = lambda kk: np.log(sym.dominant(kk, xi)[0] / lam_k)
    H = np.zeros((d, d), complex)
    for a in range(d):
        for b in range(d):
            ea, eb = np.eye(d)[a] * h, np.eye(d)[b] * h
            H[a, b] = (f(k + ea + eb) - f(k + ea - eb) - f(k - ea + eb) + f(k - ea - eb)) / (4 * h * h)
    return -(H + H.T) / 2          # C = -Hess log lambda


def mu_value(C, uhat, absu, sigma, rho_a, rho_b, m):
    d = C.shape[0]
    Qb, _ = np.linalg.qr(np.column_stack([uhat, np.eye(d)]))
    T = Qb[:, 1:d]
    n_ = uhat
    Cnn = n_ @ C @ n_
    Ctt = T.T @ C @ T
    Ctn = T.T @ C @ n_
    S = Ctt - np.outer(Ctn, Ctn) / Cnn
    a = 3 + m / 2
    total = 0j
    terms = []
    for n in range(-N_TERMS, N_TERMS + 1):
        sp_ = sigma + 2j * np.pi * n
        sm_ = sigma - 2j * np.pi * n
        Mn = S / 2 + (rho_a / (2 * absu * sp_) + rho_b / (2 * absu * sm_)) * np.eye(m)
        ev = np.linalg.eigvals(Mn)
        gauss = np.pi ** (m / 2) / np.prod(np.sqrt(ev))
        pref = (2 * np.pi ** (m / 2) * absu) ** 2 * (absu * sp_) ** (-a) * (absu * sm_) ** (-a)
        t = pref * gauss
        total += t
        if abs(n) <= 2:
            terms.append([float(t.real), float(t.imag)])
    return total, terms, complex(Cnn), np.linalg.eigvals(S).tolist()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    rows = [r for r in R2.walk_list() if r[0] in R1_IDS]
    results = []
    for wid, name, builder, phase in rows:
        out = R2.analyse2(wid, name, builder, phase)
        M, zs, gens = builder()
        terms = P.laurent_terms(M, zs)
        basis, steps = P.lattice_data(terms, gens)
        d = len(gens)
        m = d - 1
        sym = P.Symbol(terms, steps)
        B = np.array([[float(x) for x in b] for b in basis]).T
        lam0, Qn, A, c, _ = P.node(sym, d, phase)
        xi = np.array(out["xi_star"])
        vstar = np.array(out["v_star"])
        rho = out["rho"]
        Vn = np.array([float(x) for x in P.choose_vertex(steps, d, sym)])
        uhat = xi / np.linalg.norm(xi)
        cvec = B.T @ uhat
        j = int(np.argmax(np.abs(cvec)))
        q = [Fraction(float(ci / cvec[j])).limit_denominator(12) for ci in cvec]
        den = 1
        for x in q:
            den = den * x.denominator // gcd(den, x.denominator)
        ints = [int(x * den) for x in q]
        g = 0
        for x in ints:
            g = gcd(g, abs(x))
        mu_int = [x // g for x in ints]
        u_phys = np.linalg.inv(B).T @ np.array(mu_int, float)
        if np.dot(u_phys, uhat) < 0:
            u_phys, mu_int = -u_phys, [-x for x in mu_int]
        absu = float(np.linalg.norm(u_phys))
        kappa = float(np.linalg.norm(xi) / absu)
        nvec, gg = ext_gcd_solution(mu_int)
        assert gg == 1 and sum(a * b for a, b in zip(nvec, mu_int)) == 1
        x0 = B @ np.array(nvec, float)
        wB = Vn - rho * uhat
        tails = [tail_full(wB, A, c, Qn, col, d) for col in range(2)]
        if wid == "W5":
            zero = [p for p in out["dominant_points"] if p["is_zero"]]
            _, e0, _, _ = sym.dominant(np.array(zero[0]["k"]), xi)
            cosz = [float(abs(np.vdot(e0, R)) / (np.linalg.norm(e0) * np.linalg.norm(R))) for R in tails]
            res = dict(id=wid, name=name, erratum_check=True, tail_norms=[float(np.linalg.norm(R)) for R in tails],
                       cos_angle_e0_tail=cosz, H5=bool(all(np.linalg.norm(R) > 1e-8 for R in tails)),
                       H10_sufficient_tail_part=bool(all(x < 1 - 1e-6 for x in cosz)))
            results.append(res)
            print(f"{wid} {name}: erratum check H5={res['H5']} cos(e0,tail)={np.round(cosz, 6).tolist()}")
            continue
        dom = [p for p in out["dominant_points"] if p["trivial_character"]]
        info = []
        fs = []
        for p in dom:
            k = np.array(p["k"])
            lam_k, e_k, f_k, _ = sym.dominant(k, xi)
            fs.append(f_k)
            omega = np.exp(1j * np.dot(k, x0))
            phi = float(np.angle(omega))
            sigma = kappa + 1j * phi
            C = complex_hessian_log(sym, k, xi, lam_k)
            mu, first, Cnn, Seig = mu_value(C, uhat, absu, sigma, rho, rho, m)
            psi = float(np.angle(lam_k)) + (-float(np.angle(lam0))) - phi * float(np.dot(u_phys, vstar))
            cos_tail = [float(abs(np.vdot(e_k, R)) / (np.linalg.norm(e_k) * np.linalg.norm(R))) for R in tails]
            info.append(dict(k=k.tolist(), phi=phi, sigma=[sigma.real, sigma.imag],
                             psi_mod_2pi=float(np.mod(psi, 2 * np.pi)),
                             C_real_eigs=np.linalg.eigvalsh(C.real).tolist(),
                             C_imag_norm=float(np.abs(C.imag).max()),
                             mu=[float(mu.real), float(mu.imag)], abs_mu=float(abs(mu)),
                             mu_terms_n_minus2_to_2=first,
                             cos_angle_e_k_tail=cos_tail,
                             H10_k=bool(all(x < 1 - 1e-6 for x in cos_tail))))
        es = [sym.dominant(np.array(p["k"]), xi)[1] for p in dom]

        def independent(vs, i):
            others = [vs[j] for j in range(len(vs)) if j != i]
            if not others:
                return True
            Fo = np.column_stack(others)
            Fa = np.column_stack(others + [vs[i]])
            so = np.linalg.svd(Fo / np.linalg.norm(Fo, axis=0), compute_uv=False)
            sa = np.linalg.svd(Fa / np.linalg.norm(Fa, axis=0), compute_uv=False)
            return bool(np.sum(sa > 1e-6) > np.sum(so > 1e-6))

        for i, item in enumerate(info):
            item["H6_k"] = independent(fs, i)            # left, as in draft Amendment 1
            item["H6_k_right"] = independent(es, i)      # right-vector variant (not in the amendment)
        res = dict(id=wid, name=name, K_star=out["K_star"], rho=rho, u_int=mu_int, abs_u=absu,
                   kappa=kappa, x0=x0.tolist(), xi_on_axis_defect=out["xi_on_axis_defect"],
                   trivial_dominant=info)
        results.append(res)
        print(f"{wid} {name}: K*={out['K_star']:.5f} |u|={absu:.4f} kappa={kappa:.5f}")
        for item in info:
            print(f"    k={np.round(item['k'], 4).tolist()} phi={item['phi']:.5f} |mu|={item['abs_mu']:.4e} "
                  f"mu={item['mu']} H6_k={item['H6_k']} H6_k_right={item['H6_k_right']} H10_k={item['H10_k']} psi={item['psi_mod_2pi']:.5f}")
        sys.stdout.flush()
    meta = dict(charter="theory/IR_CARRIER_DICHOTOMY_GATE.md", stage="A(iv) diagnostic",
                script_sha256=P.sha(__file__), round2_sha256=P.sha(R2.__file__), n_terms=N_TERMS,
                numpy=np.__version__,
                nature="floating-point diagnostic; not a verification of H6_k, H9_k or H10_k")
    args.output.write_text(json.dumps(dict(meta=meta, walks=results), indent=2, default=str) + "\n")


if __name__ == "__main__":
    main()
