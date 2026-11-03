# Extracto literal de state/CURRENT_STATE.md en el commit 3e20c70 (numeración original de líneas)

```
  760  **direction-dependent; in general, no.**
  761  
  762  ### 8.1 Three objects, never identified
  763  
  764  For the two 3D finite-range walks of CJWW `sources/2408.02108v1.pdf`,
  765  Eqs. (5.12) and (5.15):
  766  
  767  `B(c_IR) ⊆ Γ ⊆ C_micro`,
  768  
  769  - `B(c_IR)`: the emergent isotropic IR light cone;
  770  - `Γ`: the ballistic / group-velocity propagation body;
  771  - `C_micro = conv F`: the strict microscopic causal body of the finite step set `F`.
  772  
  773  `Γ ⊆ C_micro` is general (CJWW Lemma 4.1: the rate function is `+∞` outside
  774  `conv F`). `B(c_IR) ⊆ Γ` is **not** general and is asserted here only for these
  775  two walks; CJWW Sec. 5.3 exhibits a non-convex `Γ`, so no convexity of `Γ` may
  776  be assumed.
  777  
  778  ### 8.2 The canonical saturation function
  779  
  780  For both walks `C_micro = [-1,1]^3`, hence for `||n̂||_2 = 1`
  781  
  782  `v_sub(n̂) := h_{C_micro}(n̂) = ||n̂||_1`,
  783  
  784  and, in the normalization `c_IR = 1`, the canonical directional saturation
  785  function is the **support-function ratio**
  786  
  787  `S(n̂) := h_{B(c_IR)}(n̂) / h_{C_micro}(n̂) = 1/||n̂||_1`.
  788  
  789  `S(n̂) = 1` only for the six axial directions `n̂ = ±e_i`; `S(n̂) < 1` for every
  790  non-axial direction, with `S_min = S((1,1,1)/sqrt(3)) = 1/sqrt(3)`.
  791  
  792  `S_min` is a **descriptive scalar summary only**. The full directional function
  793  `S(·)` is the canonical object. No scalar separates the two walks: `c_IR/r_in`
  794  is `1` and `S_min` is `1/sqrt(3)` for both; their difference lives in `Γ`.
  795  
  796  ### 8.3 Walk (5.12)
  797  
  798  `B(1) ⊊ Γ_1 ⊊ [-1,1]^3`, with `sup|∇ω| = sqrt(3/2) > c_IR`, attained exactly at
  799  `p = (-π/4,-π/4,-π/4)`. This walk contains finite-momentum ballistic modes
  800  faster than the emergent IR light speed while remaining inside `C_micro`.
  801  `Γ_1 ⊆` tricylinder is exact (SOS identity); the reverse inclusion is numerical.
  802  
  803  ### 8.4 Walk (5.15) — the clean counterexample
  804  
  805  `Γ_2 = B(1) ⊊ [-1,1]^3`, with `sup|∇ω| = c_IR = 1`.
  806  
  807  This refutes the identification
  808  
  809  `sup|v_g| = c_IR  ⟹  IR light cone = microscopic causal boundary`.
  810  
  811  Even when **all ballistic propagation respects `c_IR`**, the substrate permits
  812  causal propagation outside the relativistic ball in non-axial directions.
```
