# Independent review: Alice-local preparation signalling witness

Date: 2026-09-16. **Verdict: PASS. Mandatory repairs: none.**

This is a separate agent's independent review of the finite witness, not
external human review, multi-member consensus, or ratification. The reviewer
read the project instructions, canonical Sections 8 and 8.12, the new report,
both verifier implementations, the frozen theorem and its earlier review.
The earlier PASS was not used as authority for the new algebra. No reviewed
input or canonical state was edited. This report is the only file created by
the reviewer. No commit or push was made.

The result supports the evidence label
**`ALICE_LOCAL_PREPARATION_SIGNALING_WITNESS_PROVED / INDEPENDENTLY_REVIEWED`**
for this finite protocol and the input bytes below. This review does not
itself change `state/CURRENT_STATE.md` or inherit an optimal-D gate PASS.

Baseline: `research/b-infinity-post-s4-gate`,
`HEAD=dc9776016ad540ef54a1714e510b378670fa42d9`.

| Reviewed input | SHA256 |
|---|---|
| `reports/2026-09-16--alice-local-preparation.md` | `00f160f6a1c563297dc033ed45c565d17e363759a08922248763c888a4d3bd9e` |
| `scripts/verify_directional_saturation.py` | `37a769814d8e273a27568b2ff9a996a86580033c4cc7225e4a1f00cd208816de` |
| `scripts/verify_signaling_witness.py` | `4953009ebf838b98e0dd095e4cbeefdde1bc65a83ee716e96d1ce3eb9ee58d17` |
| `theory/COUPLING_MAP_SIGNALING_WITNESS.md` | `9493cfa7135645acbc9dd8c10718cf33467632514fdd821d561c3257adaa6ae2` |
| `state/CURRENT_STATE.md` | `ede139471d4217d8f84c11c27d67800f11fbd8ca5f49a90f60da0f49d9388b28` |

## 1. Exact complete preparation — PASS

Use the existing convention: the Laurent coefficient of `W` at `x-z` is
`W_{x,z}`, and one-particle states evolve by `S=W†`. Set
`z_j=exp(i p_j)`, `c_j=(z_j+z_j^-1)/2`,
`s_j=(z_j-z_j^-1)/(2i)`, and write

\[
W=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad
a=c_1c_2z_3,\ d=c_1c_2z_3^{-1},\quad
b=-c_1s_2+i s_1,\ c=c_1s_2+i s_1.
\]

Here `d=conj(a)`, `c=-conj(b)` on the real momentum torus, and
`|a|²+|b|²=1`. Thus `det W=1` and

\[
S=\begin{pmatrix}d&-b\\-c&a\end{pmatrix},\qquad
S^2=2fS-I,\qquad f=c_1c_2c_3.
\]

Consequently the **entire** prepared state is specified exactly by the
following generating polynomial and coefficient convention:

\[
\chi(x)=[z_1^{x_1}z_2^{x_2}z_3^{x_3}]
\begin{pmatrix}
2c_1c_2c_3(c_1s_2-i s_1)\\
c_1^2c_2^2(1+z_3^2)-1
\end{pmatrix}.
\tag{1}
\]

This is `S²|0,down>`, not a state chosen by solving for desired Bob
amplitudes. Direct independent Laurent arithmetic gave 38 populated sites
and matched every vector against the existing two-step helper. Equation (1)
also proves, without a support scan:

- All first-coordinate exponents are even, so `chi(1,1,1)=0`.
- The upper entry has third exponent `±1`; its origin coefficient vanishes.
- The lower origin coefficient is `(1/2)(1/2)-1=-3/4`.
- Support lies in `[-2,2]^3`; unitary evolution gives total norm one.

For `P=P_0`, `Q=I-P`, this yields
`P chi=-(3/4)|0,down>`, `||P chi||²=9/16`, `||Q chi||²=7/16`.
The initial state is exactly `|0,down>`, with vacuum at every other site.
It has fixed particle number and an even density operator under fermion
parity. A local particle is an allowed initial resource; no even operation
creating an odd particle from vacuum is assumed.

## 2. Identical pre-choice histories and causal origin — PASS

The binary input is supplied exogenously at Alice in `T=2`, independently of
the prepared state. This is the operational intervention defining the
protocol; it is not a claim about metaphysical free choice. No initial state,
preparation map, timing or earlier operation is conditioned on that input.

Writing `rho_initial=|0,down><0,down|`, both conditional histories satisfy

\[
\rho^{(0)}(T)=\rho^{(1)}(T)
=S^T\rho_{\rm initial}(S^\dagger)^T,
\qquad T=0,1,2^-.
\tag{2}
\]

Therefore every observable of the model has identical pre-choice statistics;
there is no earlier bit encoding in its matter state. The conditional
histories first differ at `T=2+`:

\[
\rho^{(b)}(2^+)=U_b|\chi\rangle\langle\chi|U_b^\dagger,
\qquad U_b=I-2bP
\]

on the one-particle sector. The full Fock-space operation is `I` or
`exp(i pi n_0)=diag(1,-1,-1,1)`, local, even, unitary and number conserving.
All subsequent dynamics are again common. The implementation constructs one
`prepared` object before forming the two `choices`; the only changed
component is at the origin. This agrees exactly with (2).

The choice is a relative phase because both `P chi` and `Q chi` are nonzero.
It is neither a different preparation nor a global phase. At `T=2-` Bob is
vacant; the local operation at Alice leaves him vacant at `T=2+` as well.
The shared, spatially extended preparation predates the message and carries
no message-dependent information. Comparing cones from `T=2` is therefore
appropriate for the subsequent communication. Measuring the full preparation
duration from `T=0` would address a different causal question.

## 3. Arms, amplitudes and probabilities — PASS

For `y=(1,1,1)`, the one-step coefficient is
`K_1(0,y)=diag(0,1/4)`. Hence

\[
a_B=(SP\chi)_y=-\frac3{16}\downarrow.
\]

An independent extraction from the prepared polynomial gives the total
amplitude `v_0=(S³|0,down>)_y`. Equivalently, Cayley-Hamilton gives
`S³=(4f²-1)S-2fI`. Its down component is `(4f²-1)a-2f`.
The coefficient at `(1,1,1)` is

\[
4\left(\frac38\right)^2\frac12-\frac14-\frac14
=-\frac7{32}.
\]

The upper component `-(4f²-1)b` has even third exponents and contributes
zero. Thus

\[
r_B=(SQ\chi)_y=v_0-a_B=-\frac1{32}\downarrow,
\qquad v_1=-a_B+r_B=\frac5{32}\downarrow.
\]

These are coherent contributions from the same local initial resource. For
the already declared local non-vacuum projection
`M_B=diag(0,1,1,1)`,

\[
p_0=\frac{49}{1024},\quad p_1=\frac{25}{1024},\quad
p_1-p_0=-4\operatorname{Re}(a_B^\dagger r_B)=-\frac3{128}.
\]

The local states are `diag(1-p_b,0,p_b,0)`. The magnitude of the probability
difference is `3/128>0`; the standard effect inequality for
`D=(1/2)||rho_1-rho_0||_1` gives `D>=3/128`, with no factor-of-two error.
No optimization is needed or claimed.

## 4. Both cones from the encoding event — PASS

Expanding the inspected symbol yields
`W=I+i(p1 sigma1-p2 sigma2+p3 sigma3)+O(|p|²)`; the eigenvalue magnitudes
of the linear generator are `|p|`, so `c_IR=1` in lattice-step units.
All one-step exponents lie in `[-1,1]^3`, and all eight corners have nonzero
diagonal coefficients. Thus `C_micro=[-1,1]^3`.

The relevant events are `A=(2,0)` and `B=(3,(1,1,1))`:

\[
\Delta T=1,\qquad |y|=\sqrt3>c_{IR}\Delta T=1,
\qquad \|y\|_\infty=1.
\]

Bob is outside the emergent cone of the message and on the microscopic
boundary. The nonzero `K_1(0,y)` proves membership in the exact causal support,
not merely in its convex hull. The unchanged free dynamics prepares the
state within the microscopic cone from the initial resource. From `T=0` to
`T=3`, `sqrt(3)<3`, so this protocol does not place Bob outside the emergent
cone of the initial preparation event. It violates no microscopic causal
support bound. These two references are consistently separated in the report.

## 5. Controls and implementation isolation — PASS

The reviewed controls have the appropriate scope:

- With zero preparation time the gate is a global phase. After one step the
  origin is empty, since every jump has first coordinate `±1`, so the gate
  acts trivially. No broader minimality claim follows.
- Without the encoding operation the final states coincide. This follows
  from the intervention formula, not solely from the code's identity check.
- Removing the `P/Q` coherence replaces the density by
  `P|chi><chi|P+Q|chi><chi|Q`, which commutes with the encoding. The two full
  output states then coincide. The local occupation is
  `||a_B||²+||r_B||²=37/1024` in both branches. This is a counterfactual
  diagnostic, not an added preparation step.
- At `(2,0,0)` one step after encoding the kernel from Alice is zero, and
  the computed full local states coincide. More generally, the evolved
  Bob algebra then has no Alice component and commutes with an even local
  Alice operation.
- The global norms and local density matrices were checked exactly. The
  helper `reduced_state` is valid here because all pure inputs to it are
  normalized; the dephasing control normalizes its components before
  weighting their reduced states.

`git diff dc97760 -- scripts/verify_directional_saturation.py` contains
exactly one added function and a final CLI dispatch change. An AST comparison
confirmed all pre-existing top-level imports, definitions, decorators,
registrations and assignments are unchanged after removing that new function
and comparing the final guard separately. The previous default call still
invokes the unchanged `main()`; only the exact argument list
`['--local-preparation-only']` invokes the new check.

The new helper imports are inside its function, so the added import cycle
does not execute during ordinary import or default invocation. In the
explicit new path, the ordinary module import exposes unchanged helpers and
does not run either module's `main()`. The historical callback registry and
the frozen witness path remain intact.

Byte comparisons against `dc97760` confirmed the old theorem, its independent
review, `verify_signaling_witness.py` and `state/CURRENT_STATE.md` are unchanged.
The old directional script hash is
`b6494dde083b34e34e745f2a35cba61ef3cffb63ce45f5c0afd9258eefd9d252`;
its new hash records the isolated extension, not a byte-identical whole file.

## 6. Executed evidence and independent reproduction

Executed from the repository root, all with exit status zero:

```text
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_directional_saturation.py --local-preparation-only
21/21 exact checks passed.

PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_signaling_witness.py
17/17 exact checks passed.

PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_directional_saturation.py
27/27 checks passed.
```

The last invocation is a regression run of the existing default suite. Its
historical numerical diagnostics retain their SUPPORTED classification; they
are not part of the new exact proof and imply no new optimization result.

The following exact command was also executed. It reconstructs the prepared
state directly from a separately transcribed Laurent symbol, before comparing
to the existing helpers. No new executable script or cache was written.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'
import sys
import sympy as sp
sys.path.insert(0,'scripts')
import verify_signaling_witness as h
z=sp.symbols('z1:4')
c=[(v+1/v)/2 for v in z]
s=[(v-1/v)/(2*sp.I) for v in z]
a=c[0]*c[1]*z[2]; b=-c[0]*s[1]+sp.I*s[0]
cc=c[0]*s[1]+sp.I*s[0]; d=c[0]*c[1]/z[2]
S=sp.Matrix([[d,-b],[-cc,a]])
f=c[0]*c[1]*c[2]
chi=sp.Matrix([-2*f*b,2*f*a-1])
assert all(sp.cancel(e)==0 for e in S*S*sp.Matrix([0,1])-chi)
def coeffs(vec,bound):
    result={}
    for i,e in enumerate(vec):
        for powers,coeff in sp.Poly(sp.expand(e*sp.prod(z)**bound),*z).terms():
            if coeff:
                x=tuple(v-bound for v in powers)
                result.setdefault(x,sp.zeros(2,1))[i]=coeff
    return result
state=coeffs(chi,2)
expected=h.evolve({h.ORIGIN:h.DOWN},h.square_kernel(h.exact_blocks()))
assert state==expected
assert h.norm_squared(state)==1
assert all(x[0]%2==0 for x in state)
origin=state[(0,0,0)]
assert origin==sp.Matrix([0,-sp.Rational(3,4)])
y=(1,1,1)
assert y not in state
out=coeffs(S*chi,3)
arm=coeffs(S*origin,1)[y]
rest=out[y]-arm
assert arm==sp.Matrix([0,-sp.Rational(3,16)])
assert rest==sp.Matrix([0,-sp.Rational(1,32)])
assert out[y]==sp.Matrix([0,-sp.Rational(7,32)])
print('INDEPENDENT_LAURENT_RECONSTRUCTION_PASS')
print('prepared support size:',len(state))
print('origin:',list(origin),'a:',list(arm),'r:',list(rest))
print('full prepared state (site: up,down):')
for x,v in sorted(state.items()): print(x,tuple(v))
PY
```

Output included `INDEPENDENT_LAURENT_RECONSTRUCTION_PASS` and
`prepared support size: 38`, followed by the full exact coefficient list.
The proof in Sections 1–4 establishes the physical interpretation; these
executions corroborate the algebra and implementation, rather than replacing
that argument with a check count.

## 7. Claim ceiling

The review establishes a finite signalling witness in the unchanged declared
CAR model from a particle initially at Alice only. Spatial coherence is
generated before an independent local message choice; Bob's own site is
vacant when that choice occurs. One later step changes a local probability
outside the emergent cone of that choice and within exact microscopic causal
support. No externally prepared Alice–Bob arm is required.

This does not prove signalling while the state remains confined to Alice at
encoding, optimal trace distance, an optimal protocol, experimental
feasibility, asymptotic behaviour, or a violation of microscopic causality.
The localized resource is not restricted to a low-energy sector. This is one
independent agent review of a precisely delimited construction; the canonical
record and the older witness retain their existing bytes and scope.
