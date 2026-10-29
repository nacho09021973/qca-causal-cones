# Encargo: fuentes primarias de las referencias de la app «Cono IR: Universalidad vs Emergencia»

- Origen: la app generada por IA `https://cono-ir-universalidad-vs-emergencia.ai.studio/`, que
  el usuario compartió el 2026-10-29. Sus referencias se extrajeron del paquete JavaScript, sin
  ejecutarlo. Solo Collins et al. (gr-qc/0403053) está en `biblioteca/`. Todas las demás
  carecen de PDF en el repo.
- Autorización directa del usuario: «busca esos papers con investigacion-gemini».
- Objetivo: localizar la fuente primaria de cada referencia, con datos bibliográficos exactos y
  un enlace a una copia de acceso abierto (arXiv si existe). Comprobar también si la atribución
  que hace la app es fiel. Preparar la nota preliminar de la pregunta A (universalidad de `c`
  entre especies).
- Resultado esperado: una tabla por referencia con autores, título, año, revista, arXiv/DOI, URL
  de acceso abierto y lo que dice la fuente frente a lo que dice la app.
- Máximo: una ronda, más la vía abierta (`prompt_abierto.md`). Cierre: informes recibidos y
  `comprobacion.md` con cada cita contrastada en el original descargado.
- El informe localiza, no prueba. Herramienta: `investigacion-gemini` del PATH,
  ~/herramientas `a32e189`.

---
I need a precise literature search in theoretical physics. For each item below give the primary
source: authors, exact title, year, journal with volume and pages, arXiv identifier and/or DOI,
and a URL to an open-access copy if one exists. Then say what the source actually establishes
and whether the attributed claim (quoted from a web app, which may be wrong) is faithful.
Distinguish clearly between what you found in a source and what you infer. If you cannot find a
source, or are unsure an identifier is correct, say so explicitly. Do not guess identifiers.

1. Chadha and Nielsen, "Lorentz invariance as a low-energy phenomenon". The app calls it
   "Chadha-Nielsen (1976)" and attributes to it an infrared attractor: Lorentz-violating
   velocity differences between species flow to zero in the IR under gauge interactions.
   Give the correct year and journal. Say which theory and approximation the result holds in
   (for example: gauge theory, one loop, which couplings).
2. G. E. Volovik on Fermi points: topological invariant N_3 in momentum space, and emergent
   relativistic (Weyl) spectra and emergent Lorentz invariance near Fermi points. The app claims
   that the topology protects the cone and that "Lorentz invariance and the speed c emerge with
   absolute rigidity at low energies". Give the primary paper(s) and/or book (for example, "The
   Universe in a Helium Droplet"). Say whether the topology protects the existence of the node
   only, or also a common speed shared by different species.
3. J. Collins, A. Perez, D. Sudarsky, L. Urrutia, H. Vucetich, "Lorentz invariance and quantum
   gravity: an additional fine-tuning problem?", gr-qc/0403053, Phys. Rev. Lett. 93, 191301
   (2004). The app writes the induced correction as proportional to g^2 (Lambda_UV / M_Pl)^2 and
   claims fine-tuning "of 1 part in 10^23". Check both against the paper.
4. Hořava–Lifshitz gravity and anisotropic scaling z = 3 flowing to z = 1 in the IR (Hořava 2009;
   and any paper on the IR recovery of Lorentz invariance in Lifshitz-type field theories,
   including the problem of different IR speeds for different species).
5. W. G. Unruh, "Experimental black-hole evaporation?" (acoustic metric), and a standard review
   of analogue gravity (Barceló, Liberati, Visser, Living Reviews in Relativity). The app claims
   each excitation sees its own acoustic metric, so there is no common cone without a coupling
   gauge field.
6. GW170817 and GRB 170817A: the speed-of-gravity bound (LIGO/Virgo, Fermi-GBM, INTEGRAL joint
   paper, ApJL 2017). The app says the signals arrived within 1.7 s after about 130 million
   light years. Give the stated bound on |v_GW − c|/c.
7. Fermi-LAT, GRB 090510 (Abdo et al., Nature 2009): a 31 GeV photon and the limit on linear
   energy-dependent photon speed. The app says less than 0.82 s of delay over about 7 billion
   light years. Give the paper and the stated numbers.
8. IceCube PeV neutrinos as constraints on superluminal neutrino velocity: absence of
   pair-emission or decay, Cohen–Glashow-type processes. Give the primary constraint papers.
9. Vacuum Cherenkov bound on electron Lorentz violation from electrons of order 100 TeV, for
   example from the Crab Nebula synchrotron/IC spectrum or from cosmic-ray electrons. Give the
   primary paper and the numbers.
10. A standard review of experimental and astrophysical bounds on Lorentz violation in
    matter/photon speed differences: for example Mattingly, Living Reviews 2005; Liberati, CQG
    2013; Kostelecký–Russell "Data Tables".

Output: one table row per item, then a short note per item on fidelity of the app's claim.
Keep each note factual.
---
