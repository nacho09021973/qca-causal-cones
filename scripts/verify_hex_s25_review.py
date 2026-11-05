"""S25 review: exact integer geometry, independent of the original enumerator.

Run: python3 -B scripts/verify_hex_s25_review.py
Coordinates (a,b) denote a*g1+b*g2 before radius normalization.
H25 is |2a+3b|, |-a+2b|, |3a+b| <= 7.
Every point has Euclidean norm <= sqrt(7), hence |a|,|b| <=
2*sqrt(7/3) < 4; the enumeration [-3,3]^2 is exhaustive.
No imported project module, floating point or symbolic approximation.
This checks geometry, not the analytic rigidity or T2 theorem.
"""


def rotate(p):
    a, b = p
    return -b, a + b


def orbit(p):
    result = set()
    for _ in range(6):
        result.add(p)
        p = rotate(p)
    return result


def levels(p):
    a, b = p
    return 2*a + 3*b, -a + 2*b, -3*a - b


def main():
    checks = []

    def check(label, condition):
        checks.append(bool(condition))
        print(f"[{'PASS' if condition else 'FAIL'}] {label}")

    points = {(a, b) for a in range(-3, 4) for b in range(-3, 4)
              if all(abs(v) <= 7 for v in levels((a, b)))}
    vertices = orbit((2, 1))
    check('25 points and 6 vertices', len(points) == 25 and len(vertices) == 6
          and vertices <= points)
    check('circumradius bound for every point',
          all(a*a+a*b+b*b <= 7 for a, b in points))
    check('rotation preserves support', {rotate(p) for p in points} == points)
    tables = []
    forced = set()
    for axis in range(3):
        layers = {i: {p for p in points if levels(p)[axis] == i}
                  for i in range(-7, 8)}
        tables.append([len(layers[i]) for i in range(7, -8, -1)])
        check(f'axis {axis}: extreme layers contain only edge vertices',
              len(layers[7]) == len(layers[-7]) == 2
              and layers[7] | layers[-7] <= vertices)
        forced |= set.union(set(), *(layers[i] for i in range(-6, 7)
                                    if len(layers[i]) == 1))
    expected = [2, 1, 1, 2, 1, 2, 2, 3, 2, 2, 1, 2, 1, 1, 2]
    check('all three complete layer tables', all(t == expected for t in tables))
    print('layer sizes:', tables[0])
    check('singletons remove exactly 18 nonvertex nonzero points',
          len(forced) == 18 and points-forced == vertices | {(0, 0)})
    # A centered R-invariant lattice hexagon contained in H25 has a
    # nonzero vertex in points. Its full six-point orbit is sufficient
    # and necessary for containment by convexity.
    smaller_orbits = {tuple(sorted(orbit(p))) for p in points-vertices-{(0, 0)}
                      if orbit(p) <= points}
    expected_orbits = {tuple(sorted(orbit(p))) for p in [(1, 0), (1, 1), (2, 0)]}
    check('only smaller centered lattice hexagons are S7, S13, S19',
          smaller_orbits == expected_orbits)
    for v, count in [((1, 0), 7), ((1, 1), 13), ((2, 0), 19)]:
        # Independently test convex containment using oriented edge cross products.
        ordered = [v]
        for _ in range(5):
            ordered.append(rotate(ordered[-1]))
        def inside(p):
            for u, w in zip(ordered, ordered[1:]+ordered[:1]):
                if (w[0]-u[0])*(p[1]-u[1])-(w[1]-u[1])*(p[0]-u[0]) < 0:
                    return False
            return True
        check(f'smaller hull {v} contains {count} lattice points',
              sum(inside(p) for p in points) == count)
    # Reflection y -> -y acts on lattice coordinates by (a,b)->(a+b,-b).
    reflect = lambda p: (p[0]+p[1], -p[1])
    check('mirror vertex orbit is H25 prime',
          {reflect(p) for p in vertices} == orbit((1, 2)))
    print(f'{sum(checks)}/{len(checks)} checks passed')
    return 0 if all(checks) else 1


if __name__ == '__main__':
    raise SystemExit(main())
