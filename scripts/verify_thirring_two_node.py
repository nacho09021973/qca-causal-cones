#!/usr/bin/env python3
"""Permanent author verifier for THIRRING_TWO_NODE_GATE.md.

Run from any directory with Python >=3.10 and NumPy. No random inputs, downloads,
or temporary scientific scripts. Writes the JSON and readable log next to the
report. Direct trajectory and antisymmetric lattice propagators do NOT use the
predicted logical gate. Finite checks corroborate, not replace, the proof.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import platform
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
STEM = ROOT / "reports/2026-11-08--thirring-two-node"
TOL = 2e-12
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
CHECKS = []


def check(name, error, tol=TOL):
    error = float(error)
    CHECKS.append({"name": name, "error": error, "tolerance": tol,
                   "pass": bool(np.isfinite(error) and error < tol)})


def kron_all(factors):
    out = np.ones((1, 1), dtype=complex)
    for f in factors:
        out = np.kron(out, f)
    return out


def pauli(n, indices, op=X):
    return kron_all([op if i in indices else I for i in range(n)])


def gate(n, i, j, chi):
    z = np.exp(1j * chi)
    return (1 + z) / 2 * np.eye(2**n) + (z - 1) / 2 * pauli(n, (i, j))


def code_on_offsets(starts, M):
    """Columns are products of f and Pi f, in labeled disjoint mode sectors."""
    return kron_all([
        np.column_stack((np.ones(2*M), (-1.0)**(s + np.arange(2*M))))
        / np.sqrt(2*M) for s in starts
    ])


def trajectory_phase(starts, velocities, M, steps, chi):
    """Microscopic contact evolution, each step J then F, on initial offsets."""
    shape = (2*M,) * len(starts)
    coords = np.indices(shape)
    initial = [starts[i] + coords[i] for i in range(len(starts))]
    phase = np.ones(shape, dtype=complex)
    for t in range(steps):
        contacts = np.zeros(shape, dtype=int)
        for i, j in itertools.combinations(range(len(starts)), 2):
            if velocities[i] != velocities[j]:
                contacts += (initial[i] + velocities[i]*t ==
                             initial[j] + velocities[j]*t)
        phase *= np.exp(1j * chi * contacts)
    return phase.reshape(-1)


def projected_trajectory(starts, velocities, M, steps, chi):
    B = code_on_offsets(starts, M)
    check(f"gram:{starts}:{M}", np.linalg.norm(B.conj().T @ B - np.eye(B.shape[1])))
    evolved = trajectory_phase(starts, velocities, M, steps, chi)[:, None] * B
    K = B.conj().T @ evolved
    residual = np.linalg.norm(evolved - B @ K, ord=2)
    return K, residual**2


def two_packet_checks():
    rows = []
    for M in (1, 2, 8, 32):
        for chi in (0., .7, np.pi/2, np.pi):
            starts, steps = (-4*M, 4*M), 5*M+1
            K, leak = projected_trajectory(starts, (1, -1), M, steps, chi)
            S = gate(2, 0, 1, chi)
            err = np.linalg.norm(K - S, ord=2)
            check(f"two-packet-map:M={M}:chi={chi}", err)
            check(f"two-packet-leak:M={M}:chi={chi}", leak)
            check(f"two-packet-unitarity:M={M}:chi={chi}",
                  np.linalg.norm(K.conj().T @ K - np.eye(4)))
            v = K[:, 0]
            concurrence = 2*abs(v[0]*v[3]-v[1]*v[2])
            check(f"concurrence:M={M}:chi={chi}", abs(concurrence-abs(np.sin(chi))))
            rows.append(dict(M=M, chi=chi, steps=steps, map_error=err,
                             worst_leakage=leak, concurrence_00=concurrence))
    # Deliberately incomplete crossing: closure need not hold mid-collision.
    partial, leak = projected_trajectory((-16, 16), (1, -1), 4, 17, np.pi/2)
    check("partial-crossing-is-not-a-closed-gate", 0. if leak > .01 else 1.)
    for i in (0, 1):
        Xi = pauli(2, (i,))
        check(f"partial-crossing-still-preserves-parity:{i}", np.linalg.norm(partial@Xi-Xi@partial))
    return rows, dict(M=4, steps=17, chi=np.pi/2, worst_leakage=leak)


def antisymmetric_lattice_checks():
    """Full two-fermion amplitudes, actual spatial motion; no trajectory formula."""
    rows = []
    L = 64
    modes = np.arange(2*L)
    dest = 2*((modes//2 + np.where(modes % 2 == 0, 1, -1)) % L) + modes % 2
    contact = ((modes[:, None]//2 == modes[None, :]//2) &
               (modes[:, None] % 2 != modes[None, :] % 2))

    def basis(M, starts):
        orbitals = []
        for spin, s in enumerate(starts):
            pair = []
            sites = np.arange(s, s+2*M)
            for node in (0, 1):
                v = np.zeros(2*L, dtype=complex)
                v[2*sites+spin] = (-1.0)**(node*sites) / np.sqrt(2*M)
                pair.append(v)
            orbitals.append(pair)
        return np.array([(np.outer(r, l)-np.outer(l, r))/np.sqrt(2)
                         for r in orbitals[0] for l in orbitals[1]])

    for M in (1, 2, 3):
        starts, steps = (8, 8+6*M), 4*M+1
        # All trajectories stay away from the periodic boundary.
        assert starts[0] + steps + 2*M < L
        assert starts[1] - steps >= 0
        initial = basis(M, starts)
        output = basis(M, (starts[0]+steps, starts[1]-steps))
        for chi in (0., .7, np.pi/2, np.pi):
            evolved = initial.copy()
            phase = np.where(contact, np.exp(1j*chi), 1)
            for _ in range(steps):
                moved = np.zeros_like(evolved)
                moved[:, dest[:, None], dest[None, :]] = evolved * phase
                evolved = moved
            # Natural moving-envelope basis uses Pi AFTER the translation:
            # each node-1 state acquires (-1)^steps.
            K = output.reshape(4, -1).conj() @ evolved.reshape(4, -1).T
            expected = (pauli(2, (0, 1), Z) if steps % 2 else np.eye(4)) @ gate(2, 0, 1, chi)
            err = np.linalg.norm(K-expected, ord=2)
            reconstructed = (output.reshape(4, -1).T @ K).T.reshape(evolved.shape)
            leak = np.linalg.norm((evolved-reconstructed).reshape(4, -1), ord=2)**2
            anti = np.linalg.norm(evolved + evolved.transpose(0, 2, 1))
            check(f"fermionic-map:M={M}:chi={chi}", err)
            check(f"fermionic-leak:M={M}:chi={chi}", leak)
            check(f"fermionic-antisymmetry:M={M}:chi={chi}", anti)
            rows.append(dict(M=M, L=L, steps=steps, chi=chi,
                             map_error=err, worst_leakage=leak, antisymmetry_error=anti))
    return rows


def composition_checks():
    rows = []
    for M in (1, 2, 4, 8):
        for chi in (0., .7, np.pi/2, np.pi):
            starts = (-8*M, 0, 8*M)
            for steps, edges in ((6*M+1, [(0, 1)]), (10*M+1, [(0, 1), (0, 2)])):
                K, leak = projected_trajectory(starts, (1, -1, -1), M, steps, chi)
                expected = np.eye(8, dtype=complex)
                for i, j in edges:
                    expected = gate(3, i, j, chi) @ expected
                err = np.linalg.norm(K-expected, ord=2)
                check(f"three-packet-composition:M={M}:chi={chi}:t={steps}", err)
                check(f"three-packet-leak:M={M}:chi={chi}:t={steps}", leak)
                rows.append(dict(M=M, chi=chi, steps=steps, edges=edges,
                                 map_error=err, worst_leakage=leak))
    return rows


def obstruction_checks():
    # Intentionally larger than the physical gate set: independent Z flips,
    # arbitrary XX collision angles and arbitrary local X rotations. Still
    # monomial in the X basis, so failure here covers the smaller actual set.
    n = 3
    B = kron_all([H]*n)
    U = np.eye(2**n, dtype=complex)
    for i, j, angle in ((0, 1, .7), (1, 2, 1.1), (0, 2, .4)):
        U = gate(n, i, j, angle) @ pauli(n, (i,), Z) @ U
        U = (np.cos(.37)*np.eye(2**n)+1j*np.sin(.37)*pauli(n, (j,))) @ U
    in_parity_basis = B.conj().T @ U @ B
    absolute = np.abs(in_parity_basis)
    check("overgrant-monomial-one-entry-per-column", np.max(abs(absolute.max(axis=0)-1)))
    check("overgrant-monomial-one-entry-per-row", np.max(abs(absolute.max(axis=1)-1)))
    check("overgrant-monomial-other-entries-zero", np.max(np.minimum(absolute, abs(absolute-1))))

    # |+>_X is a definite parity state. H sends it to |0>_node,
    # with parity probabilities (1/2,1/2), impossible for a monomial unitary.
    plus = np.array([1., 1.]) / np.sqrt(2)
    target = H @ plus
    fidelity = abs(np.vdot(plus, target))**2
    minus = np.array([1., -1.]) / np.sqrt(2)
    check("H-witness-both-parities-fidelity-one-half", max(abs(fidelity-.5),
          abs(abs(np.vdot(minus, target))**2-.5)))
    # An arbitrary ancilla state and a diagonal-in-X interaction cannot turn
    # a definite data parity into a superposition, even on discarding ancilla.
    ancilla = np.array([np.sqrt(.3), np.exp(.31j)*np.sqrt(.7)])
    state = gate(2, 0, 1, .7) @ np.kron(plus, ancilla)
    matrix = state.reshape(2, 2)
    reduced = matrix @ matrix.conj().T
    check("ancilla-preserves-definite-data-parity",
          np.linalg.norm(reduced-np.outer(plus, plus)))
    check("chi-pi-is-minus-product-XX", np.linalg.norm(gate(2, 0, 1, np.pi)+np.kron(X, X)))
    return dict(H_witness_max_fidelity=float(fidelity),
                H_witness_min_trace_distance=float(np.sqrt(1-fidelity)),
                overgrant_monomial_error=float(np.max(np.minimum(absolute, abs(absolute-1)))))


def physical_checks():
    # Fourier convention e^{ikx}, actual right shift has eigenvalue e^{-ik}.
    q = np.linspace(-.2, .2, 81)
    dispersion_error = 0.
    for k in q:
        W = np.diag([np.exp(-1j*k), np.exp(1j*k)])
        Wpi = np.diag([np.exp(-1j*(k+np.pi)), np.exp(1j*(k+np.pi))])
        dispersion_error = max(dispersion_error, np.linalg.norm(Wpi+W))
    check("two-node-quasienergy-shift", dispersion_error)
    # Finite-ring quadrature of infinite-line packet Fourier density; these
    # numbers are diagnostics, not certified integrals. Bound in report is exact.
    N, cutoff = 65536, .3
    k = 2*np.pi*np.fft.fftfreq(N)
    rows = []
    for M in (1, 2, 8, 32, 128):
        f = np.zeros(N)
        f[:2*M] = 1/np.sqrt(2*M)
        g = f * (-1.0)**np.arange(N)
        probability = abs(np.fft.fft(f, norm="ortho"))**2
        probability_pi = abs(np.fft.fft(g, norm="ortho"))**2
        check(f"Fourier-node-shift:M={M}",
              np.linalg.norm(probability_pi-np.roll(probability, N//2)))
        tail = float(probability[abs(k)>cutoff].sum())
        bound = min(1., 1/(2*M*np.sin(cutoff/2)**2))
        rows.append(dict(M=M, fft_points=N, cutoff=cutoff,
                         finite_ring_tail_probability=tail, infinite_line_tail_upper_bound=float(bound)))
    return dict(node_dispersion_error=float(dispersion_error), packet_tails=rows)


def main():
    two, partial = two_packet_checks()
    fermionic = antisymmetric_lattice_checks()
    composition = composition_checks()
    obstruction = obstruction_checks()
    physical = physical_checks()
    provenance = {}
    for rel in ("scripts/verify_thirring_two_node.py", "theory/THIRRING_TWO_NODE_GATE.md",
                "sources/1804.08508v1.pdf", "2026-11-08--thirring-primera-colision.md"):
        path = ROOT / rel
        provenance[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    result = dict(python=platform.python_version(), numpy=np.__version__,
                  seed=None, tolerance=TOL, contract_commit="fd1ef6c",
                  sha256=provenance, checks=CHECKS, two_packet=two,
                  incomplete_crossing=partial, fermionic=fermionic,
                  composition=composition, obstruction=obstruction, physical=physical)
    STEM.with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
    passed = sum(c["pass"] for c in CHECKS)
    lines = [f"Checks: {passed}/{len(CHECKS)}", f"Python {platform.python_version()}, NumPy {np.__version__}",
             f"Contract commit: fd1ef6c; deterministic, no random seed",
             "All errors are floating-point diagnostics, not interval certificates.",
             f"Max two-packet map error: {max(r['map_error'] for r in two):.17g}",
             f"Max antisymmetric map error: {max(r['map_error'] for r in fermionic):.17g}",
             f"Max three-packet map error: {max(r['map_error'] for r in composition):.17g}",
             f"Max closed-code leakage: {max(r['worst_leakage'] for r in two+fermionic+composition):.17g}",
             f"Incomplete-crossing leakage: {partial['worst_leakage']:.17g}",
             f"H witness maximum fidelity: {obstruction['H_witness_max_fidelity']:.17g}"]
    lines.extend(f"{'PASS' if c['pass'] else 'FAIL'} {c['name']}: {c['error']:.5g}" for c in CHECKS)
    log = "\n".join(lines)+"\n"
    STEM.with_name(STEM.name+"-verifier.txt").write_text(log)
    print("\n".join(lines[:10]))
    if passed != len(CHECKS):
        for c in CHECKS:
            if not c["pass"]:
                print(c)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
