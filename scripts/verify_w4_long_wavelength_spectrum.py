"""Exact symbolic certificate for theory/W4_LONG_WAVELENGTH_SPECTRUM_GATE.md."""

import sympy as sp


def main():
    k, kap = sp.symbols("k kap", real=True)
    c, s = sp.cos(kap), sp.sin(kap)

    A = sp.Matrix([[c, sp.I*s],[sp.I*s, c]])
    Bp = sp.Matrix([[c, sp.I*s*sp.exp(-sp.I*k)],
                    [sp.I*s*sp.exp(sp.I*k), c]])
    Bm = sp.Matrix([[c, -sp.I*s*sp.exp(-sp.I*k)],
                    [-sp.I*s*sp.exp(sp.I*k), c]])

    Up = sp.simplify(Bp*A)
    Um = sp.simplify(Bm*A)

    trp = sp.simplify(sp.trace(Up)/2)
    trm = sp.simplify(sp.trace(Um)/2)

    assert sp.simplify(trp - (c**2-s**2*sp.cos(k))) == 0
    assert sp.simplify(trm - (c**2+s**2*sp.cos(k))) == 0
    assert sp.simplify(Up.det()-1) == 0
    assert sp.simplify(Um.det()-1) == 0
    print("[PASS] same-sign cos omega = c^2-s^2 cos k")
    print("[PASS] sign-staggered cos omega = c^2+s^2 cos k")

    assert sp.simplify(trp.subs(k, 0)-sp.cos(2*kap)) == 0
    assert sp.simplify(trp.subs(k, sp.pi)-1) == 0
    print("[PASS] same-sign brickwork is gapless at k=pi, not generically at k=0")

    assert sp.simplify(trm.subs(k, 0)-1) == 0
    q=sp.symbols("q", real=True)
    near0=sp.series(trm.subs(k,q),q,0,4)
    target=1-sp.sin(kap)**2*q**2/2
    assert sp.simplify(sp.series(trm.subs(k,q)-target,q,0,4).removeO()) == 0
    print("[PASS] sign-staggered repair has cos omega = 1-sin(kap)^2 k^2/2+O(k^4)")
    print("[PASS] hence omega = |sin(kap)| |k| + O(|k|^3) near k=0")

    print("\nVERDICT: W4 smooth mode is gapped, but an opposite-sign second layer gives a local smooth-gapless repair.")


if __name__ == "__main__":
    main()
