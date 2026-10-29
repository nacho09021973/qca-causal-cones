# Prior art: rigidez mínima s=2

Fecha de búsqueda: 2026-10-29. Alcance: revisión bibliográfica, no cálculo ni evaluación independiente de demostraciones. Se consultaron las instrucciones, el estado, el charter, el informe preliminar y la auditoría P17 indicados, y el índice local de biblioteca. La enumeración de cinco clases es preliminar y está pendiente de revisión; no se usa aquí como resultado establecido. Enlaces a PDF locales en `pdf/`; paginación: páginas del PDF arXiv, salvo indicación contraria.

## 1. Referencia [31] y distinguibilidad

| Fuente | Relevancia |
| --- | --- |
| P17: D’Ariano, Erba y Perinotti (2017), abajo | Eq. (2) se exige y la nota [23] remite a [31], descrito como inédito. |
| DEP19: D’Ariano, Erba y Perinotti (2019), abajo | Distingue explícitamente una isotropía más débil de la condición adicional equivalente a Eq. (2); no se identifica como [31]. |

**P17.** Giacomo Mauro D’Ariano, Marco Erba y Paolo Perinotti, “Isotropic quantum walks on lattices and the Weyl equation”, *Physical Review A* **96**, 062101 (2017), [arXiv:1708.00826](https://arxiv.org/abs/1708.00826), [DOI](https://doi.org/10.1103/PhysRevA.96.062101). Original leído: PDF arXiv pp. 2 y 16, definición 1, Eq. (2) y notas [23], [31]. La nota [23] enuncia una noción operativa reforzada de homogeneidad y dice que Eq. (2) se sigue de ella, remitiendo los detalles a [31]; [31] solo identifica autores y estado inédito. No ofrece una demostración a partir de la mera invariancia por traslaciones. No hay información bibliográfica suficiente en [31] para identificar una publicación posterior con seguridad.

**DEP19.** Giacomo Mauro D’Ariano, Marco Erba y Paolo Perinotti, “Chirality from quantum walks without a quantum coin”, *Physical Review A* **100**, 012105 (2019), [arXiv:1902.10227](https://arxiv.org/abs/1902.10227), [DOI](https://doi.org/10.1103/PhysRevA.100.012105). Original leído: PDF arXiv pp. 3–4, definición 6 y Eq. (11), y pp. 17–21, apéndice A. Los autores exigen representación fiel en su definición de isotropía, presentan Eq. (11) como condición adicional y afirman que se omite cuando el grafo de Cayley se supone en lugar de derivarse de su noción de homogeneidad. Esto es relevante para interpretar la hipótesis, pero no demuestra que traslación y unitariedad impliquen la condición. La relación exacta entre su noción operativa y la del charter no está demostrada aquí.

## 2. Trabajos relacionados y clasificación sin Eq. (2)

| Fuente | Relevancia |
| --- | --- |
| DEP19 (2019) | Apéndice A.2 afirma derivar las familias generales s=2 BCC mediante unitariedad, antes de imponer isotropía; candidato prioritario para cotejar. |
| Raynal (2017) | Derivación BCC con hipótesis de irreducibilidad; no equivale automáticamente al charter. |
| D’Ariano y Perinotti (2014) | Construcción previa citada por P17 y DEP19; representación fiel y otros supuestos. |
| D’Ariano, Mosco, Perinotti y Tosini (2017) | Propagador exacto de la solución Weyl, no clasificación del conjunto más amplio. |

**DEP19, hallazgo principal.** El apéndice A.2, pp. 18–21 del PDF, parte de los cuatro generadores tetraédricos y sus inversos, resuelve las ecuaciones de unitariedad y presenta la familia (A30), con parámetros y condición `α1 α2 = α3 α4`, más un unitario común. Los autores la presentan como familia más general s=2 en BCC; en el texto se comprueba también la ausencia del término on-site. La derivación mostrada en esa parte no invoca Eq. (11) ni fija los grupos C4, D4 u O. **Inferencia para el repo:** es prior art potencialmente decisivo para parametrizar el problema sin Eq. (2), pero no se ha auditado su exhaustividad ni trasladado sus equivalencias, fases, supuestos de coeficientes no nulos, representación y covarianza a las cinco clases del charter; tampoco se ha verificado que clasifique estas clases o los nodos. No debe tratarse como resolución automática del gate. El artículo cita P17 como [33], según bibliografía del original.

**Raynal.** Philippe Raynal, “Simple derivation of the Weyl and Dirac quantum cellular automata”, *Physical Review A* **95**, 062344 (2017), [arXiv:1703.05890](https://arxiv.org/abs/1703.05890), [DOI](https://doi.org/10.1103/PhysRevA.95.062344). Original: PDF pp. 2, 4 y 8, secciones II, III.E–F. Parte de BCC y dos dimensiones internas y recuerda irreducibilidad de la representación; su clasificación no se traslada sin comprobar hipótesis. Es anterior a P17 y cita P14.

**P14.** Giacomo Mauro D’Ariano y Paolo Perinotti, “Derivation of the Dirac equation from principles of information processing”, *Physical Review A* **90**, 062106 (2014), [arXiv:1306.1934](https://arxiv.org/abs/1306.1934), [DOI](https://doi.org/10.1103/PhysRevA.90.062106). Original: PDF pp. 2–4 y apéndice A: hipótesis de isotropía con representación fiel, además de restricciones geométricas; obtiene soluciones Weyl BCC en la clase tratada. La representación fiel es una hipótesis propia de esta formulación, no una prueba para representaciones arbitrarias.

**Path-sum.** Giacomo Mauro D’Ariano, Nicola Mosco, Paolo Perinotti y Alessandro Tosini, “Path-sum solution of the Weyl quantum walk in 3 + 1 dimensions”, *Philosophical Transactions of the Royal Society A* **375**, 20160394 (2017), [arXiv:1705.08552](https://arxiv.org/abs/1705.08552), [DOI](https://doi.org/10.1098/rsta.2016.0394). Original: [texto publicado, sección 3](https://pmc.ncbi.nlm.nih.gov/articles/PMC5628258/). Para el Weyl BCC ya especificado, obtiene el propagador como suma de caminos; permite estudiar cancelaciones, pero no se ha localizado en esa lectura una clasificación de los grupos pedidos. Cita P14; su preprint es anterior a P17.

## 3. Pendiente IR, cono y propagación

| Fuente | Relevancia |
| --- | --- |
| P14 (2014) | Compara explícitamente escala relativista y velocidad causal de un sitio por paso, con normalización concreta. |
| D’Ariano, Mosco, Perinotti y Tosini (2016) | Dispersión y velocidad de grupo del walk de Dirac/Weyl 3D; propagación de paquetes. |
| Baryshnikov, Brady, Bressler y Pemantle (2011) | Región factible asintótica para familias de QW 2D; no es soporte estricto. |
| Kempf y Portugal (2009) | Velocidad de grupo para QW sobre grafos de Cayley abelianos; lectura de resumen. |
| Path-sum (2017) | Fórmula de amplitudes finitas 3D útil para estudiar soporte exacto; no se atribuye comparación de velocidades sin lectura adicional. |

**P14, comparación explícita.** PDF arXiv pp. 8–9, sección VII y Eq. (64): los autores comparan la velocidad relativista con la velocidad causal de un sitio por paso y dan un factor √3 en su convención 3D; también describen propagación superior a la velocidad IR con probabilidad pequeña. Esto compara magnitudes concretas de su geometría, pero no establece por sí solo igualdad o desigualdad con `c_strict^iso` del charter: deben cotejarse dirección, norma, unidad espacial, definición de soporte estricto y límite. La figura o una probabilidad pequeña no prueban soporte estrictamente nulo.

**D’Ariano et al. 2016.** Giacomo Mauro D’Ariano, Nicola Mosco, Paolo Perinotti y Alessandro Tosini, “Discrete Time Dirac Quantum Walk in 3+1 Dimensions”, *Entropy* **18**, 228 (2016), [arXiv:1603.06442](https://arxiv.org/abs/1603.06442), [DOI](https://doi.org/10.3390/e18060228). Original: [sección 2, ecuación (10)](https://www.mdpi.com/1099-4300/18/6/228). Para la solución BCC fijada da la relación de dispersión y define la velocidad de grupo para paquetes estrechos; no se identifica aquí con el radio del soporte estricto.

**BBBP.** Yuliy Baryshnikov, Wil Brady, Andrew Bressler y Robin Pemantle, “Two-dimensional quantum random walk”, *Journal of Statistical Physics* **142**, 78–107 (2011), [arXiv:0810.5495](https://arxiv.org/abs/0810.5495), [DOI](https://doi.org/10.1007/s10955-010-0098-2). Original: resumen arXiv y PDF pp. 1–2, 4. Estudia familias 2D y la forma de la región factible, definida mediante decaimiento exponencial y escala balística, con métodos de funciones generadoras; esa región no es automáticamente la región de amplitud estrictamente no nula, ni una comparación general con la pendiente Weyl.

**Kempf–Portugal.** Achim Kempf y Renato Portugal, “Group velocity of discrete-time quantum walks”, *Physical Review A* **79**, 052317 (2009), [DOI](https://doi.org/10.1103/PhysRevA.79.052317). Solo [resumen editorial](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.79.052317): velocidades de fase y grupo calculables para caminatas en grafos de Cayley abelianos y propuesta de tiempos de llegada; no se ha verificado una comparación con soporte estricto ni un identificador arXiv.

## 4. Isotropía cúbica completa y otras redes

| Fuente | Relevancia |
| --- | --- |
| P17 (2017) | Clasificación en d≤3 con su definición y Eq. (2); en d=3 da BCC y representación proyectiva de Pauli. |
| DEP19 (2019) | Estudia redes BCC y cuadrada y extensiones no abelianas; no es una clasificación demostrada aquí de O, D4 o C4 para el charter. |
| Raynal (2017) | BCC con representación irreducible; no declara equivalencia con clasificación bajo O completo. |

P17, original pp. 4–7, propone clasificación de grafos y soluciones bajo sus condiciones explícitas; no se debe aplicar su exclusión de redes o grupos a un problema que elimina Eq. (2) sin una prueba adicional. DEP19, secciones IV–V y apéndice A, estudia extensiones de grupos y coarse-graining: el no-go para scalar isotrópico en d≥2 concierne esa construcción y no es un no-go para todos los QW s=2. No se ha encontrado una clasificación aplicable bajo simetría octaédrica completa sin la condición adicional.

## Búsquedas y cobertura

- Índice local `biblioteca/INDICE.md`: `quantum walk|isotrop|weyl|lieb.robinson|ballistic`; se revisaron los documentos del encargo.
- Buscador web, con acceso a arXiv y originales: `"Isotropic quantum walks on lattices" "distinguishability" Perinotti`; `"D'Ariano" "Perinotti" "unpublished" isotropic quantum walk homogeneity`; `"D'Ariano" "Perinotti" "distinguishability" isotropy quantum walks`; `"quantum walks" "isotropy" "homogeneity" "distinguishability"`.
- Clasificación y citas: `"1708.00826" cited isotropic quantum walks classification 2021`; `"Isotropic quantum walks on lattices and the Weyl equation" cited classification`; `"Simple derivation of the Weyl and Dirac quantum cellular automata" isotropic quantum walk subsequent`; `"Derivation of the Dirac equation from principles of information processing" "isotropic" quantum walks 2020`; `"isotropic quantum walks" "Perinotti" "2023" lattice`; `"isotropic quantum walks" "Erba" "2020" classification groups`; `"quantum walks" "isotropy" "octahedral" classification`; `"quantum walks" cubic lattice isotropy octahedral coin classification`.
- Propagación: `quantum walk Weyl dispersion group velocity light cone maximum propagation three dimensions`; `"Lieb Robinson" "quantum walks" discrete time propagation bounds`; `quantum walk multidimensional ballistic propagation limit velocities Baryshnikov Brady Bressler Pemantle 0810.5495`.
- Páginas de autores: `site:qubit.it quantum walks isotropic D'Ariano Perinotti publications` y [lista QUIT de publicaciones de D’Ariano](https://wordpress.qubit.it/people/dariano/publications-dariano/), que incluye Bisio, Erba, Perinotti y Tosini en coautorías. No se han examinado exhaustivamente las páginas individuales de todos ellos.
- Google Scholar: intento directo de búsqueda por título exacto de P17, [consulta](https://scholar.google.com/scholar?q=%22Isotropic+quantum+walks+on+lattices+and+the+Weyl+equation%22), inaccesible desde la herramienta. No se ha podido recorrer su listado de citas; la búsqueda por web no lo sustituye. El seguimiento de citas de P14, P17 y Raynal es parcial y no exhaustivo.
- PDF arXiv descargados con identificadores verificados; P17 se copió del PDF local del índice. La conexión directa inicial falló por DNS y se repitió con acceso autorizado. Los PDF se conservan bajo `pdf/`, sin incorporarlos a biblioteca.

## No localizado

- Publicación identificable con certeza como la referencia inédita [31] de P17, o derivación de Eq. (2) desde la sola homogeneidad por traslaciones y unitariedad, en las fuentes revisadas.
- Clasificación publicada, cotejada aquí, de las cinco clases del charter por C4, D4, O y representaciones no fieles sin Eq. (2). El apéndice de DEP19 es un candidato relevante que exige cotejo detallado, no una ausencia de clasificación general BCC.
- Teorema localizado que compare específicamente `c_0` con `c_strict^iso` tal como se define en el charter; tampoco se verificó una cota Lieb–Robinson específica adicional para QW en esta búsqueda. Cedzich–Joye–Werner–Werner se excluyó por instrucción.
- Clasificación aplicable sin Eq. (2) para simetría octaédrica completa o para todas las redes 3D distintas de BCC.

Estas ausencias son resultados de búsqueda acotados, no pruebas de inexistencia. No se formula ninguna afirmación de novedad.
