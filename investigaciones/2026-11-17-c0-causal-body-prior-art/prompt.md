# Encargo: prior art de la cadena c_0 <= c_strict^iso <= r_in(C_micro)

2026-11-17. Preparado por Claude (claude-opus-5-5) a petición del usuario
(«si, prepara el encargo de búsqueda»). NO ENVIADO: el envío a Gemini
requiere permiso explícito del usuario.

Objetivo: saber, antes de escribir nada, si el contenido de un posible
artículo sobre `c_0` y el cuerpo causal ya está publicado.
Resultado esperado: lista de fuentes primarias candidatas, cada una con
identificador, página/ecuación y frase citada, clasificada según los
criterios del encargo; y lista explícita de lo no encontrado.
Rondas: una por vía (este `prompt.md` con el resultado; `prompt_abierto.md`
solo con la pregunta). Cierre: cada cita comprobada en el original y
anotada en `comprobacion.md`; el informe localiza, no prueba.
Lanzar: `investigacion-gemini investigaciones/2026-11-17-c0-causal-body-prior-art`
y `... prompt_abierto.md`. Anotar `git -C ~/herramientas rev-parse --short HEAD`.

Solo se envía el texto entre las dos líneas `---`.

---
You are helping with a prior-art search in mathematical physics. You have
Google search. Your job is to LOCATE primary sources, not to judge or prove.
Do not invent citations. If you cannot find something, say "not found"
explicitly. For every source give: authors, title, year, arXiv ID or DOI,
the page/section/equation number, and a short verbatim quotation of the
passage that supports your classification. Mark any item you could not
open in full text as "not read in full".

Setting. Translation-invariant, finite-range discrete-time quantum walks
(QW) and quantum cellular automata (QCA) on lattices Z^d (or a
d-dimensional lattice), with internal dimension s (a "coin" space C^s).
In momentum space one step is a unitary Bloch symbol U(k), a matrix
Laurent/trigonometric polynomial whose Fourier support is the finite step
set S in Z^d. Definitions used by the authors of the possible article:

- C_micro: the microscopic causal body, the convex hull of the step set S
  (the region reachable per step). r_in(C_micro): its inradius around the
  origin (largest centred ball inside it).
- c_strict^iso: the largest speed v such that, asymptotically, the exact
  support of U^n contains the ball of radius v n (strict asymptotic
  isotropic speed; the strict asymptotic support body of U^n / n).
- c_0: the low-energy (emergent) speed, the slope of the eigenphase cone
  at a massless Weyl/Dirac node of U(k).

Results the authors have (not yet published; treat them as the claims to
search for):

(R1) c_strict^iso <= r_in(C_micro), and the group velocity of every band
     lies in C_micro. (The authors already regard this as Bernstein's
     inequality for trigonometric polynomials applied to eigenphases, i.e.
     classical; they want the earliest and best QW/QCA statements of it,
     including multi-band/matrix versions.)
(R2) c_0 <= c_strict^iso: the emergent speed at a node is bounded by the
     strict asymptotic speed (proved on the 8-step body-centred-cubic step
     set; checked case by case elsewhere).
(R3) The substrate does not fix c_0: with the step set and the full strict
     causal body fixed (C_infty^strict = C_micro), a family with internal
     dimension s = 4 on the BCC step set has c_0 = a/sqrt(3) varying
     continuously for 0 < a < 1, while the standard s = 2 Weyl walk on the
     same step set has c_0 = 1/sqrt(3) = r_in.
(R4) Row-by-row equality/inequality: c_0 = r_in on the line, square and
     BCC/cubic walks considered; on one hexagonal/triangular substrate two
     published walks (Arrighi-Di Molfetta-Marquez-Martin-Perez honeycomb/triangular walks,
     arXiv:1803.01015; Jay-Debbasch-Wang triangular walks,
     arXiv:1803.01304) give c_0/r_in = 1/sqrt(3) and sqrt(3)/2; one
     triangular row has c_strict^iso < r_in.
(R5) The thesis: the lattice/neighbourhood fixes only an upper bound on
     the emergent speed; the walk (coin, internal structure) decides where
     below it c_0 falls.

Sources the authors already know (do not just repeat them; say if they
contain R1-R5): Bisio-D'Ariano-Perinotti-Tosini arXiv:1601.04832 and
arXiv:1601.04842; D'Ariano-Perinotti arXiv:1608.02004; Farrelly-Short
arXiv:1312.2852; Arrighi et al. arXiv:1803.01015; Jay et al.
arXiv:1803.01304; Cedzich-Joye-Werner-Werner arXiv:2408.02108
(exponential tail estimates; ballistic region and group velocities);
Mlodinow-Brun arXiv:2011.05597 and arXiv:2506.20136; Arrighi-Facchini-Forets
arXiv:1505.07023.

Questions:

Q1. Is R1 stated in the QW/QCA literature (group velocity or emergent
    speed bounded by the convex hull / inradius of the neighbourhood),
    including matrix-valued or multi-band versions and equality cases?
    Also give the classical sources for Bernstein's inequality for
    trigonometric polynomials in several variables with spectrum in a
    convex body (support-function form) and its equality cases.
Q2. Is R2 or an equivalent statement published (emergent node speed
    bounded by the asymptotic exact-support / light-cone speed of U^n)?
Q3. Is R3 or an equivalent published: an explicit example where the
    lattice, step set and microscopic light cone are fixed but the
    emergent speed of light varies (continuously or between two values),
    e.g. by changing the coin or the internal dimension? Any statement
    that the emergent c is or is not determined by the neighbourhood?
Q4. Are the specific values in R4 (emergent speed relative to the
    neighbourhood inradius, for 2D hexagonal/triangular walks) published,
    or a comparison of emergent speeds of different walks on the same 2D
    lattice?
Q5. Any review or paper that states the general picture R5.

Classification for each source and question:
- SAME: states the same content (any terminology or notation), as a
  theorem, proposition, remark or worked example.
- SPECIAL CASE: states it for a subclass (e.g. 1D only, one walk).
- RELATED: same objects, different statement.
Order the answer by question. End with a list "not found" per question.
---
