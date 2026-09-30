# CJWW Eq. (5.15) — momentum-space walk used by the W11 certificate

Transcribed from `scripts/verify_directional_saturation.py`, function `walk2()`
(lines 72–78 at commit `41d0e0d`), which the W11 certificate imports. In the
certificate, `PAULI = (sigma_1, sigma_2, sigma_3)` in the standard basis and
`c_k = cos p_k`, `s_k = sin p_k`.

```
W(p) = [[ c1 c2 e^{i p3},          -c1 s2 + i s1       ],
        [  c1 s2 + i s1,             c1 c2 e^{-i p3}   ]]
```

The Weyl node used in W11 is p = 0.
