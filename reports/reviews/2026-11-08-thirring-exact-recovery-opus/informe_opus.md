<!-- Procedencia (escrita por ~/herramientas/revision/revision_ciega.sh @ ce09890a0d5f68a6634f358eff2e477ac5f15ec7; lo que sigue a la cabecera es la respuesta sin editar)
script sha256 0bd5b169c5a1662e022af9b3d1a8d816f1dae50a2c2b6a347aa3b19c89bb14e0; biblioteca sha256 af8f09a6b0e93f91a9b34ccbeba6ef48360e8cd5c6971616365fbd9c0528d51c
estado: COMPLETED; salida: 0; motivo de fin: cli_exit_0 (estado operativo, no validación del contenido)
modelo: claude-opus-5-5, esfuerzo: high, vía: claude -p sellado (2.1.319 (Claude Code))
opus.json sha256 47acd714fa4bc3566a378ea7cd7126a3b6efed964d160bd81d3ab8177b86268f
inicio: 2026-11-08T21:24:19Z  fin: 2026-11-08T21:27:51Z
documento: /home/adnac/qca-causal-cones/theory/THIRRING_EXACT_RECOVERY_GATE.md ; último commit observado: 0212df6 ; sha256 de la copia enviada 58d09634e76a0d0e32e7ccc589be31c167a1571c460ebb30b273662a95308a69
documento: /home/adnac/qca-causal-cones/reports/2026-11-08--thirring-exact-recovery.md ; último commit observado: 0828861 ; sha256 de la copia enviada cfd56e10febe925275d64a4ce2d55a2176ccc6d281410c095f04a6d994a6e775
documento: /home/adnac/qca-causal-cones/scripts/verify_thirring_exact_recovery.py ; último commit observado: 578607b ; sha256 de la copia enviada ce8f96b9699b72bc0833943aad10548ab7e757a6b61e8dd6a1189021939eeacd
documento: /home/adnac/qca-causal-cones/reports/2026-11-08--thirring-exact-recovery.txt ; último commit observado: 0828861 ; sha256 de la copia enviada 02ccb2b51a4ce26a4f9ca0d8965df35ab01380425dcbf5d8b8a959a36b21dc75
documento: /home/adnac/qca-causal-cones/reports/2026-11-08--thirring-two-contacts.md ; último commit observado: 490269a ; sha256 de la copia enviada e715bb65cbb4aa14a0c5eb7f96d01c887c1fb1058a3975f1be31874d2b8ccabd
entrada_opus.txt sha256 ae1d7f374d83deb49419b6aaea9e68ffb4cbbe2b0ad9f45b553c214a02077ad1
respuesta sha256 40a0b496379bcb1b6cb0a472cc2dbe2619ea76191c5c82816e1e7f79e74a6c94
-->

# Revisión adversarial: no hay recuperación exacta para T ≥ 2 en el código M=1

## Veredicto

**Se sostiene.** He rederivado a mano los pasos (1)–(6) desde las definiciones de W, J, Γ y B y no encuentro ningún error, supuesto oculto ni hueco que invalide el teorema. Hay dos imprecisiones de redacción que conviene corregir: una en §3 y otra en §2. Ninguna cambia el resultado. El recuento 80/80 no interviene en este veredicto. El script solo lo he inspeccionado, no lo he ejecutado.

**Qué no he comprobado.** No he verificado los PDF (1711.03920, 1804.08508), el JSON, los hashes, los commits, ni el orden temporal de congelación del contrato. Tampoco ningún archivo Lean. Que W y U=FJ coincidan con el modelo publicado lo tomo del contrato. El informe de dos contactos lo uso solo como contraste aritmético del autor.

---

## Derivaciones críticas (hechas a mano)

### (1) Representación isométrica

- Γ = σ_z(−1)^x. W lleva R(x)→R(x+1) y L(x)→L(x−1) con amplitud ν, y R(x)↔L(x) con amplitud −iμ. Los tres movimientos invierten Γ.
- A = (R0, L1) tiene Γ=+1. B = (R1, L0) tiene Γ=−1.
- En cada sector, cada sitio aloja una sola componente. Por eso, al tiempo t, la posición determina la componente: A es R si y solo si (−1)^x = (−1)^t, y B es R si y solo si (−1)^x = −(−1)^t.
- El subespacio de dos fermiones "uno en Γ=+, otro en Γ=−" es la imagen isométrica de H₊⊗H₋ mediante ψ⊗φ ↦ √2·ψ∧φ.
  - W⊗W lo preserva: intercambia los dos sectores, y basta reetiquetar A como la partícula del sector (−1)^t.
  - J es diagonal en ocupaciones. Dos partículas de sectores opuestos en el mismo sitio están necesariamente en R y L, así que n_R n_L = 1 equivale a x_A = x_B.
  - No aparecen signos fermiónicos adicionales, porque c†(a) ↦ c†(Wa). El signo del orden A,B es común a U^T B y a F^T B y se cancela en V.
- La convención del script coincide: s = parity(T−1), A mueve +s·parity(x) y B mueve −s·parity(y).

### (2) Rayos extremos y la identidad Π_T U^T B = R_T D

Cada paso desplaza −1, 0 o +1. La permanencia es la rama de masa, que invierte la componente.

| Destino | Desde el modo 0 | Desde el modo 1 |
|---|---|---|
| A en T | todo a la derecha, amplitud ν^T, camino único | L en 1 no puede ir a la derecha en el primer paso; si fuera a la izquierda no llegaría; queda permanencia inicial más T−1 pasos a la derecha, amplitud −iμν^{T−1}; una permanencia posterior dejaría L y bloquearía el avance |
| A en 1−T | simétrico: −iμν^{T−1} | simétrico: ν^T |
| B en T+1 | solo desde R1, amplitud ν^T | — (L0 necesitaría desplazamiento T+1 > T) |
| B en −T | solo desde L0, amplitud ν^T | — |

Los productos ψ_A^a(x_A)·ψ_B^b(x_B) dan exactamente R_T = ν^{2T−1}G:

- G es unitaria: los bloques [[ν, −iμ], [−iμ, ν]] tienen columnas ortonormales porque −iμν + iμν = 0.
- Las cuatro coordenadas son distintas para todo T ≥ 1, ya que T ≠ 1−T y T+1 ≠ −T.

Fases en la evolución con interacción. La amplitud es la suma sobre pares de caminos de la amplitud libre por z^{#coincidencias}, evaluadas en t = 0, …, T−1. J actúa antes de cada F; no hay J en t=T.

- Para t ≥ 1, cualquier camino de A cumple 1−t ≤ x_A(t) ≤ t.
- En cambio, x_B(t) = t+1 (rayo derecho) o x_B(t) = −t (rayo izquierdo).
- Por tanto, la única coincidencia posible es en t=0 y depende solo de la entrada. Recorriendo las cuatro filas obtengo las fases (1, z, z, 1) en las columnas 00, 01, 10, 11. Así, Π_T U^T B = R_T D para todo T ≥ 1.

### (3) V queda forzada a D

- Si U^T B = F^T B V, entonces R_T V = R_T D. Como R_T es invertible (det ≠ 0 porque ν ≠ 0), V = D.
- Lo mismo vale columna a columna. Si U^T B|01⟩ = F^T B v, entonces v = z·e₀₁. ✓

### (4) Telescopaje

- UB = FBD implica Δ_T = (U^{T−1} − F^{T−1})FBD.
- La identidad Uⁿ − Fⁿ = Σ_{j=0}^{n−1} U^{n−1−j}(U−F)F^j, con U−F = F(J−I) y k = j+1, da Σ_{k=1}^{T−1} U^{T−1−k} F(J−I) F^k BD. ✓
- La fuente k actúa tras k pasos libres. Después quedan 1 + (T−1−k) = T−k pasos. ✓

### (5) Cono relativo, coincidencia inicial y coeficiente

- La separación x_A − x_B cambia como mucho en 2 por paso, y J no mueve posiciones. Desde la fuente k: |x_A − x_B| ≤ 2(T−k) < 2(T−1) para k ≥ 2. ✓
- Término k=1 sobre la entrada 01:
  - D|01⟩ = z|01⟩.
  - FB|01⟩ = (ν R1 − iμ L0)_A ⊗ (ν L(−1) − iμ R0)_B.
  - La única coincidencia es (0,0), con A en L y B en R, y amplitud −μ²z.
- Llegar a q_T exige que A vaya siempre a la izquierda y B siempre a la derecha (las componentes lo permiten). Es un único par de caminos, de peso ν^{2T−2}. La separación crece estrictamente, así que no hay coincidencias nuevas.
- Resultado: ⟨q_T|Δ_T|01⟩ = −μ²z(z−1)ν^{2T−2}. Con z = i vale μ²(1+i)ν^{2T−2}, y en numeradores sobre 25^T, (9·4^{2T−2}, 9·4^{2T−2}). ✓

### (6) Cota de fuga y exponentes

- Π_T U^T B = R_T K_T + Π_T E_T, luego Π_T E_T = R_T(D − K_T). Con ‖R_T^{−1}‖ = ρ_T^{−1} y ‖Π_T‖ = 1 sale la primera desigualdad.
- Como Δ = E + B_T(K−D) y B_T es isométrica, ‖E|01⟩‖ ≥ |z−1|μ²ν^{2T−2}·ρ/(1+ρ) = |z−1|μ²ν^{4T−3}/(1+ν^{2T−1}).
- Elevando al cuadrado: ν^{8T−6}. ✓ Además p₀₁ = ‖E|01⟩‖² porque U^T B|01⟩ es unitario.
- Contrastes numéricos:
  - Cota en T=2: 2·0,1296·0,8¹⁰/1,512² ≈ 0,012174. En T=3: ≈ 0,0026489. ✓
  - p₀₁(2): la columna 01 de K₂ del informe previo da 1 − (81² + 544² + 2·108²)/625² = 0,165888. Coincide con el registro y con λ·9/25.

---

## Objeciones, ordenadas por gravedad (todas menores, ninguna invalidante)

1. **§3, justificación de "A queda estrictamente detrás".**
   - Problema: el alcance de una celda por paso no basta por sí solo. En la entrada 10, A y B empiezan ambos en 1, y A podría empatar con B si pudiera avanzar en el primer paso. Lo impide que A en 1 sea L.
   - Reparación: escribir que 1−t ≤ x_A(t) ≤ t para t ≥ 1 por la componente inicial de cada modo de A. Alternativamente, enumerar las coincidencias de los caminos únicos de A ya derivados.
2. **§2, isometría solo afirmada.**
   - Problema: el texto la afirma pero no da el mapa.
   - Reparación: añadir tres líneas con el mapa √2·ψ∧φ, la preservación del subespacio por W⊗W y J, el reetiquetado alternante, y la cancelación del signo de orden en V. La segunda implementación lo corrobora para T ≤ 4, pero eso no sustituye la frase.
3. **§4, redacción.**
   - "Cada componente se desplaza" debería decir "cada partícula se desplaza".
4. **Script y registro (inspección, no ejecución).**
   - Correspondencia con la prueba: la propagación es J antes de F, las coordenadas y G·4^{2T−1} son correctas, la diferencia usa D₀₁ = i, y p₀₁ se calcula por proyección, no suponiendo K=D.
   - El control `finite-cone-support` es laxo: usa −T como cota inferior de A cuando la real es 1−T. La ausencia de periodicidad es cierta por construcción del diccionario.
   - El registro imprime `0` como "rigorous_lower_bound" en T=1, mientras el informe dice "no aplicable". Es cosmético.
   - No se contrasta ningún parámetro fuera de los congelados, así que la extensión de §1 descansa solo en la prueba manual.
   - Límites de la segunda implementación:
     - Solo cubre T ≤ 4, en coma flotante con tolerancia 2e−12.
     - Usa un anillo de 20 sitios. El soporte cabe en [2, 11], así que no hay retorno.
     - Es del mismo autor.
     - Es un contraste genuino de la representación de sectores y de la convención de `embed`, pues compara frente a Fock antisimétrico con máscara de contacto completa. No cubre T = 6, 8, 12.

---

## (8) Extensión y distinción exacto/aproximado

- **Hipótesis efectivamente usadas.**
  - ν ≠ 0, para invertir R_T y para el factor ν^{2T−2}.
  - μ ≠ 0, para el coeficiente μ².
  - z ≠ 1, es decir, χ ∉ 2πℤ.
  - μ² + ν² = 1, para la unitariedad y para ‖R_T^{−1}‖ = ρ^{−1} en la cota.
- La unicidad de caminos es combinatoria y no depende de los valores. Por tanto, 0 < μ, ν < 1 con z ≠ 1 bastan, como se afirma.
- **Exacto frente a aproximado.** La cota tiende a 0 con T y no es un no-go aproximado. El informe lo dice correctamente, y la tabla no se usa para inferir asintótica.

---

## Alcance que acepto

Se fijan las siguientes hipótesis:

- W como está escrito, con μ, ν reales en (0,1) y μ² + ν² = 1.
- U = FJ, con la fase antes del paso libre y χ constante, e^{iχ} ≠ 1.
- Recta infinita.
- El código M=1 declarado, con A = (R0, L1), B = (R1, L0), sectores Γ opuestos y salida F^T B.

Bajo ellas:

- **Para todo T ≥ 2**, no existe V ∈ ℂ^{4×4} con U^T B = F^T B V. En particular no existe ninguna unitaria entrelazante.
- Ni siquiera la columna 01 está en el rango de F^T B.
- Los rayos extremos fuerzan V = D, y
  p₀₁(T) ≥ |z−1|²μ⁴ν^{8T−6}/(1+ν^{2T−1})² > 0.
- En T = 1 la puerta D es exacta.

**Fuera de alcance:**

- Recuperación aproximada.
- Otros códigos de salida, auxiliares o medidas.
- El orden U' = JF, que es otro problema.
- Anillos finitos con T comparable a L/2, donde los rayos extremos dan la vuelta.
- Formalización Lean del caso de tiempo arbitrario.
- Que las definiciones coincidan con los PDF, que no he verificado.

El resultado sigue siendo del autor más esta revisión; no está formalizado.
