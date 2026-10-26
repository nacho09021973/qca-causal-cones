#!/usr/bin/env bash
# Prepare the sealed input only. This script cannot send to a provider.
set -euo pipefail
encargo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_dir="$(git -C "$encargo_dir" rev-parse --show-toplevel)"
cd -- "$repo_dir"
sha256sum -c "$encargo_dir/inputs.sha256"
REVISION_SOLO_ENTRADA=1 revision-ciega deepseek "$encargo_dir" \
  theory/W4_LONG_WAVELENGTH_SPECTRUM_GATE.md \
  reports/2026-10-26--w4-spectrum-audit.md \
  scripts/verify_w4_long_wavelength_spectrum.py \
  scripts/verify_w4_spectrum_observables.py \
  scripts/certificate_utils.py \
  scripts/requirements.txt
