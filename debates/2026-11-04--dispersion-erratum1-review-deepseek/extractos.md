# Extractos literales con numeración original (preparado 2026-11-04, base 648be9c)

## scripts/verify_dispersion_corrections_gate.py, l. 555–580
```
555:     groups = {}
556:     print("== Part 1: symbols imported read-only (parent checks re-run on import, not counted here)")
557:     rows = {}
558:     zs1 = sp.symbols("w1:2")
559:     zs2 = sp.symbols("w1:3")
560:     sym, _ = WD.published_symbol(1, 1, zs1)
561:     rows["L1"] = dict(symbol=sym, zs=zs1, gens=[(1,)], sigma=+1, substrate="line", N=6, c0=sp.Integer(1))
562:     sym, _ = WD.published_symbol(2, 1, zs2)
563:     rows["L2"] = dict(symbol=sym, zs=zs2, gens=[(1, 0), (0, 1)], sigma=+1, substrate="square", N=6, c0=R2 / 2)
564:     n_parent_before = len(P.CHECKS)
565:     for label, fn in (("L6e", P.row_L6e), ("L5a", P.row_L5a), ("L5b", P.row_L5b), ("L6a", P.row_L6a),
566:                       ("L6c", P.row_L6c), ("L6d", P.row_L6d), ("L6f", P.row_L6f)):
567:         symbol, zs, support, gens = fn()
568:         sub = {"L6e": "square", "L5a": "cubic", "L5b": "cubic"}.get(label, "hexagon")
569:         rows[label] = dict(symbol=symbol, zs=zs, gens=gens, sigma=-1, substrate=sub,
570:                            N=4 if sub == "cubic" else 6, c0=P.EXPECTED_MASSLESS[label][1])
571:     record("parent row constructors pass their own checks on import",
572:            all(ok for _, ok, _ in P.CHECKS[n_parent_before:]), f"{len(P.CHECKS) - n_parent_before} parent checks")
573:     rows["L3"] = dict(symbol=laurent_matrix_from_p(DS.walk2()), zs=DS.Z, gens=[(1, 0, 0), (0, 1, 0), (0, 0, 1)],
574:                       sigma=+1, substrate="cubic", N=4, c0=1 / R3)
575:     rows["L4"] = dict(symbol=laurent_matrix_from_p(DS.walk1()), zs=DS.Z, gens=[(1, 0, 0), (0, 1, 0), (0, 0, 1)],
576:                       sigma=+1, substrate="cubic", N=4, c0=1 / R3)
577:     zs3 = sp.symbols("z1:4")
578:     rows["L3s4"] = dict(symbol=row_L3s4_symbol(A_SYM, zs3), zs=zs3, gens=[(1 / R3, 0, 0), (0, 1 / R3, 0), (0, 0, 1 / R3)],
579:                         sigma=-1, substrate="cubic", N=4, c0=A_SYM / R3)
580:     # L6b: V = U^3 on the white-triangle lattice, orientation blocks.
```

## scripts/verify_dispersion_corrections_gate.py, l. 804–815
```
804:     ceiling = ["L2", "L6e", "L3", "L5a", "L5b[+i]", "L5b[-i]", "L4"]
805:     he = {}
806:     for label in ceiling:
807:         he[label] = results[label]["lowest_aniso"]
808:     print(f"  He (ceiling rows have nonzero anisotropy): {all(he.values())}; per row {he}")
809:     hf = {}
810:     n3 = sp.symbols("n1:4", real=True)
811:     for sub, members in (("square", ["L2", "L6e"]), ("BCC", ["L3", "L5a", "L5b[+i]"]),
812:                          ("hexagon", ["L6a", "L6c", "L6d", "L6f", "L6b[block 0]"])):
813:         ns_ = n2 if sub != "BCC" else n3
814:         pairs = {}
815:         for x, y in itertools.combinations(members, 2):
```

## scripts/verify_directional_saturation.py, l. 60–82
```
60:         return fn
61:     return wrap
62: 
63: 
64: def walk1():
65:     """CJWW (5.12): W(p) = exp(i p1 s1) exp(i p2 s2) exp(i p3 s3)."""
66:     W = I2
67:     for c, s, sig in zip(C, S, PAULI):
68:         W = W * (c * I2 + sp.I * s * sig)
69:     return sp.expand(W)
70: 
71: 
72: def walk2():
73:     """CJWW (5.15), transcribed entry by entry."""
74:     e = sp.exp(sp.I * P3)
75:     return sp.Matrix([
76:         [C[0] * C[1] * e, -C[0] * S[1] + sp.I * S[0]],
77:         [C[0] * S[1] + sp.I * S[0], C[0] * C[1] / e],
78:     ])
79: 
80: 
81: F1 = C[0] * C[1] * C[2] + S[0] * S[1] * S[2]     # tr W1 / 2
82: F2 = C[0] * C[1] * C[2]                          # tr W2 / 2
```

## theory/SUBSTRATE_SATURATION_PHASE0_GATE_AMENDMENT_1.md, l. 130–165
```
130: 4. **Substrate: author finding, hand derivation, not checked by any
131:    script; re-derived by gpt-6.1-sol (review point 4, PASS).** Read from
132:    the printed symbols:
133:    - (5.12) is the product of `cos p_a + i sin p_a σ_a`, each factor with
134:      Fourier support `{±e_a}`; the composite support is exactly
135:      `{±1}^3`. The group it generates is `{x ∈ Z^3 : x_1 ≡ x_2 ≡ x_3
136:      (mod 2)}`, the BCC lattice, which up to the scale `1/sqrt3` is the
137:      substrate of L3 and L5a (`N_3`, CS l. 486). Its scalar part
138:      `cos p_1 cos p_2 cos p_3 + sin p_1 sin p_2 sin p_3`
139:      (`verify_directional_saturation.py` l. 81, `F1`) has the form of the
140:      d = 3 published symbol with chirality `+1`
141:      (`verify_weyl_dirac_gate.py` l. 68); whether (5.12) coincides with
142:      one of the L3 symbols up to the declared symmetries is not checked
143:      here.
144:    - (5.15) has entries `cos p_1 cos p_2 e^{±i p_3}` (steps `(±1,±1,±1)`),
145:      `cos p_1 sin p_2` (steps `(±1,±1,0)`) and `sin p_1` (steps
146:      `(±1,0,0)`). These generate `Z^3`. The convex hull is still
147:      `[-1,1]^3`.
148:    - Hence the source label «Z^3» of C_ACROSS l. 78 holds for the
149:      generated group of (5.15) and not for that of (5.12). This refers to
150:      the generated group required by frozen Sec. 2.3: (5.12) can be
151:      written on the ambient `Z^3`, where it preserves each of the four BCC
152:      cosets; it is not impossible to formulate it there. Both walks have `C_micro` a cube, so the shape column
153:      of the audit is unchanged; the substrate count of audit F3 changes:
154:      the «cube substrate of L4» is the `Z^3` group of (5.15), and (5.12)
155:      is a further walk on the BCC substrate.
156: 5. **Pair.** `(r_in, c_0) = (1/sqrt3, 1/sqrt3)` from the c-across-lattices
157:    table l. 147, as before; the addendum's CJWW-unit pair `(1, 1)` is
158:    shown only for consistency.
159: 
160: **Recorded inconsistency, not repaired here.** The frozen contract
161: `theory/DISPERSION_CORRECTIONS_ACROSS_LATTICES_GATE.md` (l. 63, 67)
162: assigns `walk2()` (CJWW (5.15)) to row L3 «BCC» and `walk1()` (CJWW (5.12))
163: to row L4 «cube», whereas C_ACROSS_LATTICES_GATE l. 76 and 78 declare L3 as
164: the standard battery and L4 as both CJWW walks, and item 4 above places
165: (5.12) on the BCC group and (5.15) on `Z^3`. This amendment does not rely
```

## state/CURRENT_STATE.md, l. 2424–2456
```
2424: row), He (ceiling rows with `d >= 2` have a nonzero anisotropic
2425: coefficient), Hf (rows on one substrate do not share the correction) are
2426: OPEN. Verdicts: `CORRECTIONS_TABLE_COMPLETE` / `_PARTIAL_<reason>`; per
2427: hypothesis `CONFIRMED_IN_DECLARED_ROWS` / `REFUTED_BY_ROW_<Id>` /
2428: `DECIDED_BY_SYMMETRY`. Execution: report plus
2429: `scripts/verify_dispersion_corrections_gate.py`, then independent
2430: cross-family review, then a separate promotion. No claim about our
2431: universe, no general QCA law, no novelty claim.
2432: 
2433: Execution (2026-11-02): [report](../reports/2026-11-02--dispersion-corrections-across-lattices.md),
2434: verifier `scripts/verify_dispersion_corrections_gate.py` (SHA256
2435: `b7c451e213b60a0ae22e5c2ad15630abe5f5f4ee1c7c3d11dc660f43ffdb9a7e`,
2436: 81/81 after the review repairs; 79/79 at the reviewed `791f0d80d279`).
2437: Status `CORRECTIONS_TABLE_PARTIAL_VALIDITY_SCALE_AND_VGRP_OPEN`,
2438: PRELIMINARY until promotion; reviews Gemini PASS, Grok REPAIR_REQUIRED, repairs applied;
2439: bounded re-review Gemini PASS, Grok PASS. **Promoted 2026-11-02** by
2440: direct user instruction («si, promuévelo») in the frozen scope below.
2441: Findings: the lowest correction
2442: is a relative-order-`|k|` term `beta` exactly in the six rows whose walk
2443: group lacks inversion (L5a, L5b, L4 with `T_d`; L6a, L6b with `D_3`;
2444: L3s4), and `alpha` elsewhere; the harmonic content matches the walk's
2445: group in every row (the `D_6` rows L6c, L6d, L6f are isotropic through
2446: relative order `|k|^2`, first `cos 6 theta` at `|k|^4`). Hd
2447: `REFUTED_BY_ROW_L1` (`alpha_0 = 0`, exactly linear) and by L3s4 for
2448: `0 < a < a* = sqrt3 sqrt(17 - sqrt154)/9`; every other row has
2449: `alpha_0 < 0`. He `CONFIRMED_IN_DECLARED_ROWS` (L2, L6e `cos 4 theta`; L3
2450: `K4`; L5a, L5b, L4 `n1 n2 n3`). Hf `REFUTED_BY_ROW_L6e` (L2 and L6e
2451: identical; also L5a = the `+i` Weyl block of L5b, and L6d = L6f through
2452: `|k|^2`). Scale of
2453: validity OPEN in `d >= 2`; `V_grp^max` OPEN. No physical interpretation.
2454: 
2455: ## 14. Hexagonal supremum (M1) — chartered 2026-11-03
2456: 
```

