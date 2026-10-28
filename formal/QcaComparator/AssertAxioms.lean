-- Copia de ~/herramientas/lean/HerramientasLean/AssertAxioms.lean (herramientas 25cac80). No editar aquí.
import Lean

/-!
# `#assert_standard_axioms`

Fuente: `~/herramientas/lean/HerramientasLean/AssertAxioms.lean`. Un proyecto Lean que lo use
copia este fichero tal cual y anota en su cabecera el commit de herramientas del que viene
(`git -C ~/herramientas rev-parse --short HEAD`): Lake necesita el código dentro del proyecto.
Sólo usa el núcleo de Lean; no depende de Mathlib.

`#assert_standard_axioms a b c` falla si alguna de esas constantes depende de un axioma distinto
de `propext`, `Classical.choice` y `Quot.sound`; en particular de `sorryAx`, o de
`Lean.ofReduceBool`, que introduce `native_decide`. Si todas pasan, emite un único mensaje con el
número de constantes comprobadas, pensado para fijarlo con `#guard_msgs`:

```lean
/-- info: 2 theorems use only propext, Classical.choice, Quot.sound -/
#guard_msgs in
#assert_standard_axioms Foo.bar Foo.baz
```

Fijar el número impide que una constante se caiga de la lista sin que se note.
-/

open Lean Elab Command in
/-- Falla salvo que cada constante nombrada dependa sólo de los tres axiomas estándar. -/
elab "#assert_standard_axioms " ids:ident* : command => do
  let allowed := [``propext, ``Classical.choice, ``Quot.sound]
  for id in ids do
    let name ← liftCoreM (realizeGlobalConstNoOverloadWithInfo id)
    let axioms ← liftCoreM (collectAxioms name)
    let extra := axioms.toList.filter (· ∉ allowed)
    unless extra.isEmpty do
      throwErrorAt id m!"'{name}' depends on non-standard axioms: {extra}"
  logInfo m!"{ids.size} theorems use only propext, Classical.choice, Quot.sound"
