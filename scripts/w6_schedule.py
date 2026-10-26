"""An explicit conservative W6 scheduling witness, not a unique frozen ordering.

36 matter-coupled layers (all R then all T) and 54 geometry-only layers.
Species are serialized even when distinct factors could be updated in parallel.
"""

from itertools import product

from tetrad_transport import DIRECTIONS


def schedule():
    for kind in ("R", "T"):
        for a, r in product(range(3), repeat=2):
            for parity in range(2):
                yield kind, a, r, 0, parity
    for a, r, axis in product(range(3), repeat=3):
        for parity in range(2):
            yield "K", a, r, axis, parity


def validate_schedule(layers, size):
    """Exact finite-torus matching/coverage check; parity proof is in the report."""
    assert size >= 4 and size % 2 == 0
    assert len(layers) == 90
    sites = tuple(product(range(size), repeat=3))
    covered = set()
    for kind, a, r, axis, parity in layers:
        assert kind in ("R", "T", "K") and a in range(3) and r in range(3)
        assert parity in (0, 1) and axis in range(3)
        if kind != "K":
            assert axis == 0
        shift = DIRECTIONS[r] if kind != "K" else tuple(int(i == axis) for i in range(3))
        assert shift[axis] % 2 == 1
        endpoints = set()
        for x in sites:
            if x[axis] % 2 != parity:
                continue
            y = tuple((xi+di) % size for xi, di in zip(x, shift))
            assert x not in endpoints and y not in endpoints
            endpoints.update((x, y))
            key = kind, a, r, axis, x
            assert key not in covered
            covered.add(key)
        assert len(endpoints) == size**3
    expected = {(kind, a, r, 0, x) for kind in ("R", "T")
                for a, r in product(range(3), repeat=2) for x in sites}
    expected |= {("K", a, r, j, x) for a, r, j in product(range(3), repeat=3) for x in sites}
    assert covered == expected
    return len(covered)
