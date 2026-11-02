"""EXPLORATORY, not a certificate. HEX_CEILING gate (theory/HEX_CEILING_GATE.md), T2.

Builds the hexagonal saturation system (facet-normal layer sums plus
unitarity) for a given support and runs a grevlex Groebner basis over the
complex field. A basis {1} would prove inconsistency (hence no real
solution); any other basis decides nothing about real solutions.
Recorded runs (2026-11-02, sympy 1.14.0): "minimal" -> 8 free real
parameters, 144 equations, basis != {1} in 0.5 s (consistent over C; the
real contradiction is certified by verify_hex_ceiling_gate.py with a lex
basis and a negative discriminant); "ball19" -> 56 free real parameters,
730 equations, not finished within a 900 s cap (timeout 124).
Usage: python -B scripts/explore_hex_saturation_support.py minimal|ball19
"""
import sys, time
import sympy as sp
R3=sp.sqrt(3); I2=sp.eye(2)
SX=sp.Matrix([[0,1],[1,0]]); SY=sp.Matrix([[0,-sp.I],[sp.I,0]])
which=sys.argv[1]
# lattice coords (a,b): h = a g1 + b g2, g1=(1,0), g2=(1/2,sqrt3/2)
if which=="minimal":
    verts=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]   # radius 1
    pts=verts+[(0,0)]
else:  # radius-2 hexagonal ball, 19 points
    pts=[(a,b) for a in range(-2,3) for b in range(-2,3) if max(abs(a),abs(b),abs(a+b))<=2]
    verts=[(2,0),(0,2),(-2,2),(-2,0),(0,-2),(2,-2)]
cart=lambda h: (h[0]+h[1]/sp.Integer(2), h[1]*R3/2)
# facet normals: edges d = v_{k+1}-v_k for k=0,1,2 ; outward normal at angles 30,90,150
edges=[(verts[k+1][0]-verts[k][0], verts[k+1][1]-verts[k][1]) for k in range(3)]
angles=[sp.pi/6, sp.pi/2, 5*sp.pi/6]
def layer(h,d):  # integer proportional to h.n (outward normal = -Rot90(d) for ccw polygon)
    p,q=d; a,b=h
    return -(b*p-a*q)
syms=[]
def gen(i):
    e=sp.symbols(f"u{i}_0:8",real=True); syms.extend(e)
    return sp.Matrix([[e[0]+sp.I*e[1],e[2]+sp.I*e[3]],[e[4]+sp.I*e[5],e[6]+sp.I*e[7]]])
A={h:gen(i) for i,h in enumerate(pts)}
lin=[]
for d,ang in zip(edges,angles):
    m={h:layer(h,d) for h in pts}
    top=max(m.values()); 
    Pp=(I2+sp.cos(ang)*SX+sp.sin(ang)*SY)/2; Pm=I2-Pp
    for lv in sorted(set(m.values())):
        S=sum((A[h] for h in pts if m[h]==lv), sp.zeros(2))
        tgt=Pp if lv==top else (Pm if lv==-top else sp.zeros(2))
        for e in (S-tgt):
            e=sp.expand(e); lin+=[sp.expand(sp.re(e)),sp.expand(sp.im(e))]
lin=[sp.nsimplify(x) for x in lin]
sol=sp.solve(lin,syms,dict=True)
print("layer system solutions:",len(sol))
sol=sol[0]
free=sorted(set().union(*[sp.sympify(v).free_symbols for v in sol.values()])|{s for s in syms if s not in sol},key=str)
print("free real parameters:",len(free))
As={h:A[h].subs(sol) for h in pts}
blocks={}
for h1 in pts:
    for h2 in pts:
        d=(h1[0]-h2[0],h1[1]-h2[1])
        blocks.setdefault(d,[sp.zeros(2),sp.zeros(2)])
        blocks[d][0]+=As[h1]*As[h2].H; blocks[d][1]+=As[h2].H*As[h1]
eqs=set()
for d,(m1,m2) in blocks.items():
    tgt=I2 if d==(0,0) else sp.zeros(2)
    for M in (m1-tgt,m2-tgt):
        for e in M:
            e=sp.expand(e)
            for part in (sp.expand(sp.re(e)),sp.expand(sp.im(e))):
                if part!=0: eqs.add(part)
print("quadratic equations:",len(eqs)); sys.stdout.flush()
t=time.time()
G=sp.groebner(list(eqs),*free,order="grevlex")
print("groebner done in %.1fs; basis == {1}: %s; size %d"%(time.time()-t, list(G.exprs)==[1], len(G.exprs)))
