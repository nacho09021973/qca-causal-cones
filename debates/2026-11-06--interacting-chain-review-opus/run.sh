#!/usr/bin/env bash
set -euo pipefail
cd /home/adnac/qca-causal-cones
taskdir=debates/2026-11-06--interacting-chain-review-opus
docs=(PROJECT_INSTRUCTIONS.md state/CURRENT_STATE.md)
for stem in interaction-vacuum-sector stationary-occupied-response occupied-second-order occupied-memory-kernel occupied-abel-memory occupied-memory-decay-audit low-energy-interacting-circuit yukawa-mediator-bridge yukawa-joint-flow-proof-scope yukawa-critical-cutoff-ir; do
  docs+=("reports/2026-11-06--$stem.md")
done
for stem in INTERACTING_VELOCITY_BRIDGE STATIONARY_OCCUPIED_RESPONSE OCCUPIED_SECOND_ORDER OCCUPIED_MEMORY_KERNEL OCCUPIED_ABEL_MEMORY OCCUPIED_MEMORY_DECAY LOW_ENERGY_INTERACTING_CIRCUIT YUKAWA_MEDIATOR_BRIDGE YUKAWA_JOINT_FLOW YUKAWA_CRITICAL_CUTOFF_IR; do
  docs+=("theory/${stem}_GATE.md")
done
docs+=(scripts/verify_interaction_vacuum_sector.py scripts/verify_stationary_occupied_response.py scripts/verify_occupied_second_order.py scripts/evaluate_occupied_memory_kernel.py scripts/evaluate_occupied_abel_memory.py scripts/verify_low_energy_circuit.py scripts/verify_yukawa_mediator_bridge.py scripts/verify_yukawa_joint_flow.py scripts/verify_yukawa_ir_scaling.py scripts/evaluate_yukawa_static_counterterms.py)
docs+=(reports/2026-11-06--occupied-memory-kernel-run.txt reports/2026-11-06--occupied-abel-memory-run.txt reports/2026-11-06--yukawa-static-counterterms.json reports/2026-11-06--yukawa-joint-flow-verifier.txt)
docs+=(sources/1102.0789v2.pdf sources/fei_giombi_klebanov_tarnopolsky_2016_yukawa.pdf)
printf '%s\n' "${docs[@]}" > "$taskdir/docs.txt"
sha256sum "${docs[@]}" > "$taskdir/inputs.sha256"
revision-ciega opus "$taskdir" "${docs[@]}" > "$taskdir/run.out" 2>&1
