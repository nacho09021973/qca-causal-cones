#!/usr/bin/env bash
# Prepare the sealed input only. This script cannot send to a provider.
set -euo pipefail
encargo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_dir="$(git -C "$encargo_dir" rev-parse --show-toplevel)"
cd -- "$repo_dir"
sha256sum -c "$encargo_dir/inputs.sha256"
mapfile -t docs < "$encargo_dir/docs.txt"
REVISION_SOLO_ENTRADA=1 revision-ciega gemini "$encargo_dir" "${docs[@]}"
