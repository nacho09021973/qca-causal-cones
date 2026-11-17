# Encargo dirigido: rigidez de c_0 en el BCC más allá de s=2

2026-11-17. Preparado por Claude (claude-opus-5-5). Recorta el `prompt.md`
anterior (R1-R5, versión en `92556a5`, nunca enviada) a la única pregunta
que la vía abierta y `comprobacion.md` dejan como candidata. Usuario:
«COMMIT, PUSH y recorta prompt.md para enviárselo a Grok ya que gemini no
tiene saldo». Envío a Grok autorizado por esa instrucción.

Objetivo: saber si está publicado que, en d=3 sobre el conjunto de pasos
BCC, la velocidad emergente deja de estar fijada al pasar de la dimensión
interna mínima s=2 a s=4 con el mismo cuerpo causal estricto.
Resultado esperado: fuentes primarias candidatas con identificador,
sección/ecuación y cita breve, clasificadas SAME / SPECIAL CASE / RELATED;
lista explícita de lo no encontrado.
Rondas: una ejecución. Cierre: cada candidato comprobado en el original y
anotado en `comprobacion.md`. El informe localiza, no prueba; no se concluye
ausencia de una búsqueda fallida.
Lanzar: `python3 investigaciones/2026-11-17-c0-causal-body-prior-art/run_grok_prompt.py prompt.md dirigido`.

---
You are helping with a targeted prior-art search in mathematical physics.
You have web search and web fetch. Your job is to LOCATE primary sources,
not to judge or prove. Do not invent citations; if you cannot find
something, say "not found". For every source give authors, title, year,
arXiv ID or DOI, section/equation, and a verbatim quotation of at most 25
words. Mark any item you could not open in full text as "not read in full".
One research execution only; do not claim absence from a failed search.

Setting. Translation-invariant, finite-range discrete-time quantum walks /
one-particle quantum cellular automata on Z^3 with the body-centred-cubic
(BCC) step set: the eight displacements (+-1,+-1,+-1) (up to scale), no
on-site (zero-displacement) term, internal dimension s. The step is a
unitary Bloch symbol U(k), a matrix trigonometric polynomial.
Speeds, which must not be confused:
- c_0: the infrared coefficient, the slope of the eigenphase cone at a
  massless Weyl node of U(k).
- the strict causal body: the convex hull of the displacements that remain
  with nonzero coefficient in U(k)^n, divided by n, as n grows (exact
  support, not ballistic probability).
- group velocities and the ballistic propagation region (different again).

Already known (do not just repeat; say whether they go further):
- D'Ariano and Perinotti, arXiv:1306.1934: for the minimal nontrivial
  internal dimension s = 2, with unitarity, locality, homogeneity and
  discrete isotropy, the automaton on Z^3 exists only on the BCC graph and
  is essentially unique; c is the causal speed divided by sqrt(3).
- Di Molfetta and Arrighi, arXiv:1906.04483: in one dimension a fixed
  massless walk with nearest-neighbour shifts has continuously tunable
  speed c.
- Also known: Bisio-D'Ariano-Perinotti-Tosini arXiv:1601.04832 and
  arXiv:1601.04842; D'Ariano-Perinotti arXiv:1608.02004; Raynal
  arXiv:1703.05890; Farrelly-Short arXiv:1312.2852; Arrighi-Nesme-Forets
  (Dirac quantum walk in higher dimensions, 2014); Cedzich-Joye-Werner-
  Werner arXiv:2408.02108.

Claim to search for (unpublished, by the requesters): with the BCC step set
fixed, internal dimension s = 4, a fixed representation of the Klein group
D2 acting covariantly, irreducible dynamics, no on-site coefficient, there
is a one-parameter family whose rank-two Weyl clusters have isotropic speed
c_0 = a/sqrt(3) for every 0 < a < 1, while its strict causal body is the
whole cube (the same as for the s = 2 automaton, which has c_0 = 1/sqrt(3)).
So the s = 2 rigidity of c_0 does not survive enlarging the internal space.

Questions:

Q1. Is this claim, or an equivalent one, published: on the BCC (or any
    fixed 3D) step set, an internal dimension s > 2 automaton without an
    on-site term whose massless emergent speed differs from, or varies
    continuously below, that of the minimal s = 2 automaton?
Q2. Does any paper state that D'Ariano-Perinotti's uniqueness, or the
    value c = causal speed / sqrt(3), fails or changes for non-minimal
    internal dimension (s = 4 or larger), with the same step set and
    symmetry? Or, conversely, that it persists?
Q3. Four-component QCA on the BCC lattice (e.g. Dirac or doubled Weyl
    automata, coupled Weyl pairs, multi-flavour walks): do any have a
    massless sector whose speed is a free parameter, without on-site terms?
    Report what each example holds fixed (step set, exact support,
    symmetry, irreducibility) and whether its speed parameter comes from a
    mass/on-site term.
Q4. Any classification of s = 4 (or general s) isotropic BCC QCA that
    determines the possible emergent speeds.

Classification for each source: SAME (states the claim, any terminology),
SPECIAL CASE (a subclass or weaker version), RELATED (same objects,
different statement), with a one-line reason naming what the source holds
fixed. Order the answer by question. End with "not found" per question.
---
