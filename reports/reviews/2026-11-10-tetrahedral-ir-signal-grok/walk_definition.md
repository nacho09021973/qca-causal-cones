## Frozen model and scope

- d=3, internal dimension 4, one update lasts 1, lengths unchanged.
- Lattice: equal-parity integer triples divided by sqrt(3).
- G_i=sigma_i tensor sigma_i;
  W=I_2 tensor [I_2-i(sigma_x+sigma_y+sigma_z)/sqrt(3)]/sqrt(2).
- U(k)=W product_{i=x,y,z}[cos(k_i/sqrt(3))I_4
  -i sin(k_i/sqrt(3))G_i], fixed xyz order.
- F={(-1,-1,-1),(-1,1,1),(1,-1,1),(1,1,-1)}/sqrt(3).
  C_micro=conv F, nodes at k=0 with phases ±pi/4; local speed 1/3.
- D2 and cyclic proper tetrahedral covariance as in the existing model;
  no changed representation, coefficient, node, normalization or parameter.
- All eigenphases of this same rule are included in the global-bound test.
  No irreducibility classification is attempted.

