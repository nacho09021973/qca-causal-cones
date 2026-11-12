# Causal body, emergent cone and geometric corona

Generate from the repository root with Python's standard library:

```sh
python3 -B scripts/visualize_causal_corona.py
```

Open `causal_corona.html` in a browser. It is self-contained, works offline
and requires no server. `--output PATH.html` selects another destination;
a `.provenance.json` sibling records script/output hashes, base Git and
the displayed model data. The base Git hash does not assert a clean tree.

## Reading the viewer

- Left: a spatial slice at time t, with three spatial axes. Drag to rotate;
  scroll to zoom. Nested causal bodies are earlier slices of the same model.
- Right: a radial space-time slice, with time vertical and positive radius
  horizontal. Choose a vertex, a face normal or the x axis. The region
  between the emergent ray and microscopic boundary is shaded amber.
- Cyan dots mark the emergent sphere. Amber dots sample the continuous
  geometric corona along fixed rays. Their density is deterministic and
  chosen for visibility, not calculated from a state or an observable.
- Pause or scrub time, switch models and export the 3D canvas to PNG.
- The **Superficies** switch fills the two boundaries with translucent
  triangles: cyan inner sphere and amber outer polyhedron. The opacity
  slider controls their visibility. These bound the corona volume; they
  do not interpolate the interior point cloud. The sphere mesh is a
  display approximation; the radius and ray calculations remain analytic.

The two recorded examples have different units and symbols and are never
overlaid as one walk:

| Model | Microscopic body | Local emergent speed |
| --- | --- | --- |
| Fixed cyclic s=4 walk | Four unit vertices (±1,±1,±1)/sqrt(3), product of signs -1 | 1/3 |
| Manuscript CJWW walk | Cube [-1,1]^3 | 1 |

Sources: `reports/2026-11-06--s4-cyclic-realization.md`,
`scripts/plot_s4_cyclic_realization.py`, and
`papers/ir-corona/ir-corona.tex` sections 2 and 4. These are a visualization's
input definitions, not a new independent scientific validation.

The tetrahedron's faces satisfy v.x >= -1/3 for its four vertices v,
so its radial boundary in direction n is
1 / max_v(-3 v.n). The cube's is 1 / max_i |n_i|. These are ray extents,
not support functions. The generator checks unit tetrahedral vertices,
pairwise dot products -1/3, vertex radius 1 and face-normal radius 1/3.
Thus the emergent sphere touches face centres, while a gap opens towards
vertices (cube vertex radius sqrt(3), face radius 1).

## Claim ceiling

Geometric illustration only. Points do not represent photons, a lattice
probability distribution, simulated unitary evolution, or the operational
signal delta(N). The continuous convex envelope need not consist entirely
of sites reachable at any particular integer time. Fractional t is a
visual interpolation; one microscopic update has duration 1.
For s=4 this does not establish the strict asymptotic causal body. For CJWW
this does not compute a finite-N signal, its exponent or the weighted
operational prefactor. No new gate, numerical experiment, or promotion.
