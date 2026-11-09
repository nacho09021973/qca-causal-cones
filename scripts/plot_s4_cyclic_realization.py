"""Visualize the fixed s=4 walk; numerical illustration, not a new proof.

Run from repository root:
PYTHONNOUSERSITE=1 python3 -B scripts/plot_s4_cyclic_realization.py
The environment flag avoids mixed user/system Matplotlib installations.
Writes PNG, PDF, sampled data and provenance to reports/figures/s4_cyclic/.
Known: exact author verifier gives c=1/3 and tetrahedral support.
Question: how do the exact bands depart from the local cones?
Stop: fail on unitarity, axial-spectrum or small-momentum slope mismatch.
No fitting, parameter search, wave-packet dynamics or external data.
"""
import hashlib
import itertools
import json
import os
from pathlib import Path
import subprocess
import tempfile

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir())/'qca-mpl-cache'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'reports/figures/s4_cyclic'
I = np.eye(2, dtype=complex)
J = np.eye(4, dtype=complex)
pauli = np.array([[[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]])
G = [np.kron(p, p) for p in pauli]
W = (J-1j*np.kron(I, sum(pauli)/np.sqrt(3)))/np.sqrt(2)
unitarity_errors = []


def bands(k):
    U = W.copy()
    for ki, gi in zip(k, G):
        x = ki/np.sqrt(3)
        U = U@(np.cos(x)*J-1j*np.sin(x)*gi)
    unitarity_errors.append(float(np.max(np.abs(U.conj().T@U-J))))
    # lambda=exp(-i omega). Windows below do not cross the branch cut.
    return np.sort(-np.angle(np.linalg.eigvals(U)))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    kaxis = np.linspace(-0.8, 0.8, 321)
    axis_bands = np.array([bands([x, 0, 0]) for x in kaxis])
    analytic = []
    for k in kaxis:
        x = k/np.sqrt(3)
        phi = [np.arccos((np.cos(x)-e*np.sin(x)/np.sqrt(3))/np.sqrt(2))
               for e in (-1, 1)]
        analytic.append(sorted([-phi[0], -phi[1], phi[0], phi[1]]))
    axial_error = float(np.max(np.abs(axis_bands-np.array(analytic))))
    grid = np.linspace(-0.28, 0.28, 61)
    X, Y = np.meshgrid(grid, grid)
    surface = np.array([[bands([x, y, 0]) for x, y in zip(xs, ys)]
                        for xs, ys in zip(X, Y)])
    directions = np.array([[1, 0, 0], [1, 1, 0], [1, 1, 1]], dtype=float)
    directions /= np.linalg.norm(directions, axis=1)[:, None]
    radii = np.linspace(0.002, 0.8, 180)
    radial = np.array([[bands(r*d) for r in radii] for d in directions])
    # Half-splitting/r removes motion of the band's midpoint at finite k.
    speeds = (radial[:, :, 3]-radial[:, :, 2])/(2*radii)
    tiny_r = 1e-5
    tiny_speeds = []
    for d in directions:
        b = bands(tiny_r*d)
        tiny_speeds.append(float((b[3]-b[2])/(2*tiny_r)))
    max_u = max(unitarity_errors)
    assert max_u < 1e-12, max_u
    assert axial_error < 1e-12, axial_error
    assert max(abs(v-1/3) for v in tiny_speeds) < 1e-5, tiny_speeds
    # Positive and negative pairs remain separated in every displayed sample.
    assert np.min(surface[:, :, 2]) > 0 and np.max(surface[:, :, 1]) < 0
    assert np.min(radial[:, :, 2]) > 0 and np.max(radial[:, :, 1]) < 0

    plt.rcParams.update({'font.size': 10, 'axes.spines.top': False,
                         'axes.spines.right': False})
    fig = plt.figure(figsize=(14, 11), layout='constrained')
    ax = fig.add_subplot(221, projection='3d')
    raw = np.array(list(itertools.product((-1, 1), repeat=3)))
    vertices = raw[np.prod(raw, axis=1) == -1]/np.sqrt(3)
    absent = raw[np.prod(raw, axis=1) == 1]/np.sqrt(3)
    faces = [[vertices[i] for i in ids] for ids in itertools.combinations(range(4), 3)]
    ax.add_collection3d(Poly3DCollection(faces, alpha=0.14, facecolor='#2878a5',
                                        edgecolor='#2878a5'))
    ax.scatter(*vertices.T, color='#14678d', s=55, label='4 saltos no nulos')
    ax.scatter(*absent.T, color='#aaaaaa', marker='x', s=45, label='4 coeficientes nulos')
    for v in vertices:
        ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color='#14678d', alpha=.7)
    ax.set(xlabel='x', ylabel='y', zlabel='z', title='A. Soporte microscópico de un paso')
    ax.set_box_aspect((1, 1, 1))
    ax.legend(loc='upper left', fontsize=8)
    ax = fig.add_subplot(222, projection='3d')
    for index, color in [(2, '#d98a28'), (3, '#2878a5')]:
        ax.plot_surface(X, Y, surface[:, :, index]-np.pi/4,
                        color=color, alpha=.85, linewidth=0, rcount=45, ccount=45)
    ax.set(xlabel='$k_x$', ylabel='$k_y$', zlabel=r'$\omega-\pi/4$',
           title='B. Bandas exactas cerca del nodo +π/4 (kz=0)')
    ax.view_init(elev=21, azim=-55)
    ax = fig.add_subplot(223)
    for j in range(4):
        ax.plot(kaxis, axis_bands[:, j], color='#2878a5' if j >= 2 else '#d98a28', lw=2)
    for center in (-np.pi/4, np.pi/4):
        for sign in (-1, 1):
            ax.plot(kaxis, center+sign*abs(kaxis)/3, 'k--', lw=1, alpha=.6)
    ax.plot([], [], 'k--', label='Aproximación local: ±π/4 ± |kx|/3')
    ax.set(xlabel='$k_x$ (ky=kz=0)', ylabel='Cuasienergía ω [rad/paso]',
           title='C. Dos cruces nodales; cuatro bandas')
    ax.legend(fontsize=8)
    ax.grid(alpha=.2)
    ax = fig.add_subplot(224)
    for speed, name in zip(speeds, ['eje (100)', 'diagonal (110)', 'diagonal (111)']):
        ax.plot(radii, speed, label=name, lw=2)
    ax.axhline(1/3, color='black', linestyle='--', label='Límite lineal: 1/3')
    ax.set(xlabel='r = |k|', ylabel='[ω superior − ω inferior] / (2r)',
           title='D. Apertura del par +π/4 fuera del límite lineal')
    ax.legend(fontsize=8)
    ax.grid(alpha=.2)
    fig.suptitle('Walk s=4: tetraedro microscópico y conos locales\n'
                 'Diagonalización del constructor fijo · ilustración numérica de autor', fontsize=16)
    fig.savefig(OUT/'s4_cyclic.png', dpi=180)
    fig.savefig(OUT/'s4_cyclic.pdf')
    plt.close(fig)
    np.savez_compressed(OUT/'sampled_bands.npz', kaxis=kaxis, axis_bands=axis_bands,
                        grid=grid, surface_bands=surface, directions=directions,
                        radii=radii, radial_bands=radial, half_splitting_over_r=speeds)
    metadata = {
        'script': str(Path(__file__).relative_to(ROOT)),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
        'git_note': 'Working-tree artifacts; HEAD is not a claim that these files are committed.',
        'numpy': np.__version__, 'matplotlib': matplotlib.__version__,
        'max_unitarity_error': max_u, 'max_axial_analytic_error': axial_error,
        'tiny_radius': tiny_r, 'half_splitting_over_r_at_tiny_radius': tiny_speeds,
        'half_splitting_over_r_at_r_0_8': speeds[:, -1].tolist(),
        'meaning': 'Numerical illustration, not independent review; finite-r opening is not group velocity.',
        'source_report': 'reports/2026-11-06--s4-cyclic-realization.md',
    }
    (OUT/'provenance.json').write_text(json.dumps(metadata, indent=2)+'\n')
    print(json.dumps(metadata, indent=2))
    print('Figures:', OUT/'s4_cyclic.png', OUT/'s4_cyclic.pdf')


if __name__ == '__main__':
    main()
