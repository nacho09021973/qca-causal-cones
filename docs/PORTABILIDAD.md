# Trabajar desde otro ordenador

Esta guía cubre una instalación local en Linux o macOS con terminal POSIX.
En Windows se pueden usar los mismos pasos dentro de WSL. No cambia ningún
gate ni sustituye la lectura de `PROJECT_INSTRUCTIONS.md` y
`state/CURRENT_STATE.md`. El ejemplo usa la rama de investigación actual:
para otra rama, elige explícitamente la que corresponda.

## 1. Descargar el repositorio

Con Git instalado y acceso al repositorio:

```sh
git clone --branch research/inverse-gravity-design https://github.com/nacho09021973/qca-causal-cones.git
cd qca-causal-cones
git status --short --branch
git rev-parse HEAD
```

Si el repositorio es privado, configura antes tu acceso a GitHub. Comprueba
que la rama y el commit son los que necesitas; una descarga posterior puede
contener un commit más reciente que los informes históricos.

## 2. Preparar Python

Los certificados documentan Python 3.12 y `scripts/requirements.txt` fija
SymPy 1.14.0 y NumPy 1.26.4. Instala Python 3.12 con soporte `venv` y acceso
a los paquetes. Desde la raíz del repositorio:

```sh
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r scripts/requirements.txt
python --version
python -c 'import sympy, numpy; print("sympy", sympy.__version__, "numpy", numpy.__version__)'
```

`.venv/` es local y no se versiona. Reactiva el entorno al abrir otra terminal;
`deactivate` lo desactiva. La instalación requiere acceso a un índice de
paquetes o a una copia local de los paquetes correspondientes. No se ha
comprobado esta instalación en todas las plataformas.

## 3. Comprobar la copia

Desde la raíz, con el entorno activado:

```sh
python -B scripts/text_integrity.py --check
python -B scripts/test_text_integrity.py
python -B scripts/verify_w4_long_wavelength_spectrum.py
python -B scripts/verify_w4_spectrum_observables.py
python -B scripts/run_all_verifiers.py --output /tmp/qca-verifier-sweep.tsv
```

El barrido enumera los `verify_*.py` existentes, registra HEAD, versiones,
estados y tiempos, y devuelve error si alguno falla. El archivo en `/tmp` es
un registro local reemplazable; para conservar un resultado de trabajo, usa
una ruta de informe apropiada y conserva también la procedencia de las entradas.
El barrido comprueba ejecución, no demuestra por sí solo los argumentos ni
reabre gates. Consulta cada contrato e informe para conocer sus límites.

## 4. Restaurar la biblioteca

`biblioteca/` está excluida de Git: el clon no incluye sus PDFs, índices ni
otros archivos locales. `sources/` sí contiene documentos versionados, pero
no constituye una copia completa de `biblioteca/`. Para recuperar la biblioteca
anterior, copia **la carpeta completa** desde una copia de confianza o una
copia de seguridad, manteniendo nombres y estructura, hasta
`qca-causal-cones/biblioteca/`. El índice existente permite localizar PDFs;
comprueba que los archivos citados realmente están presentes. Si no tienes
esa copia, un índice regenerado solo describirá los documentos disponibles,
no recuperará los ausentes.

Para regenerar el índice, hace falta además el repositorio compartido
`herramientas`, con acceso autorizado a su remoto:

```sh
git clone https://github.com/nacho09021973/herramientas.git "$HOME/herramientas"
python "$HOME/herramientas/biblioteca_catalog/build_catalog.py" --repo .
```

Si `~/herramientas` ya existe, usa la instalación existente y verifica su
versión con `git -C "$HOME/herramientas" rev-parse HEAD`; no la sobrescribas.
La generación usa los archivos versionados `scripts/biblioteca_catalog/curated.csv`
y `tags.csv` y los documentos presentes. No edites `INDICE.md` a mano. Antes
de investigar, consulta el índice y lee los originales; el índice no demuestra
las afirmaciones. Las herramientas externas de revisión y sus credenciales
requieren configuración separada y permiso explícito para enviar textos.

## 5. Comprobar cambios antes de sincronizar

`git status --short --branch` muestra los cambios versionados y los archivos
nuevos no ignorados. No muestra `biblioteca/` ni `.venv/`; respalda la biblioteca
por separado. Antes de actualizar una copia con trabajo local, revisa su estado
y evita sobrescribir cambios. El estado científico vigente es el de
`state/CURRENT_STATE.md` de la rama y el commit que estés utilizando.
