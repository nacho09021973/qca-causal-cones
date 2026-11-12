"""Permanent generator for the final scalar comparator and its mutation inventory.

Copies explicit definitions byte for byte. It does not generate or infer proofs.
Coverage is the block-5 work order: full target, fixed witnesses, phase sign and
uniformity, active indices, completion sign and uniformity, normalized identity
and uniformity, boundary positivity and the printed boundary integral.
Run once; existing artifacts are never overwritten.
"""
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
PROVENANCE = '8da0e09231ca9d7d6b6d5ea8861df3777be5ab18 plus local blocks 4 and 5'
SOURCES = {
    'Definitions': ['sqNorm', 'frequencyNorm', 'planeIndex', 'normalFrequency',
                    'centerCoordinate', 'phase', 'latticeBox', 'aliceSites',
                    'cutoff', 'profileF', 'profileS', 'cResource', 'phi0', 'resource',
                    'boundaryResource', 'alpha', 'criticalCoshSquared', 'criticalTilt',
                    'tiltWeight', 'amplitude', 'theta', 'transverseCoordinates', 'tau',
                    'psiIntegrand', 'psi', 'depthTerm', 'sPlus', 'leadingScale'],
    'FiniteProfile': ['indexedLayerDepth', 'layerGlobalFactor'],
    'RemainderBounds': ['layerNaturalIndex'],
    'ZeroModeDepth': ['geometricZeroModeSum'],
    'NormalPhase': ['unphasedZeroModeSum', 'normalPhaseError'],
    'DepthGeometry': ['depthPlaneIndex', 'activeDepthIndices'],
    'DepthCompletion': ['depthCompletionError'],
    'NormalizedRemainder': ['normalizedRemainder'],
    'Targets': ['AliceLayersB'],
}


def declaration(text, name):
    pattern = r'(?ms)^def '+re.escape(name)+r'\b.*?(?=^def |^end |^theorem |^/\-|^abbrev |\Z)'
    match = re.search(pattern, text)
    if match is None:
        raise ValueError(f'Missing definition {name}')
    return match.group().strip()


CLAIMS = [
    ('FullScalarClaim', 'AliceLayersB', 'aliceLayersB_proved'),
    ('ExplicitWitnessesClaim', '''∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, 2 ≤ N → ∀ η : Frequency,
      frequencyNorm η ≤ Real.pi/6 →
      Summable (depthTerm criticalTilt (theta N) (tau N η)) ∧
      ∃ E : ℂ, ‖E‖ ≤ C*(Real.rpow (N : ℝ) (-(1 : ℝ)/2)+|normalFrequency η|) ∧
        amplitude N criticalTilt η = (leadingScale N : ℂ)*(sPlus criticalTilt (theta N) (tau N η)+E)''',
     'aliceLayersB_explicit_witnesses'),
    ('BoundaryPositiveClaim', '0 < boundaryResource', 'boundaryResource_pos'),
    ('BoundaryIntegralClaim', '''boundaryResource = cResource*(16*Real.pi*
      ∫ k in (0 : ℝ)..1, k*(1-k^2)^2*Real.sin (k/4))''', 'boundaryResource_eq_paper_integral'),
    ('PhaseSignClaim', '''∀ N : ℕ, 0 < N → ∀ t : ℝ, ∀ η : Frequency,
      normalPhaseError N t η = geometricZeroModeSum N t η-unphasedZeroModeSum N t η''',
     'normalPhaseError_eq_difference'),
    ('PhaseUniformClaim', '''∀ t : ℝ, 0 < t →
      ∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, 0 < N → ∀ η : Frequency,
        ‖normalPhaseError N t η‖ ≤ C*|normalFrequency η|''', 'phase_error_uniform_exists'),
    ('ActiveIndicesClaim', '''∀ N : ℕ, 0 < N → ∀ j : ℕ,
      j ∈ activeDepthIndices N ↔ depthPlaneIndex N j ∈ (aliceSites N).image planeIndex''',
     'activeDepthIndices_membership'),
    ('CompletionSignClaim', '''∀ N : ℕ, 0 < N → ∀ t : ℝ, 0 < t → ∀ η : Frequency,
      depthCompletionError N t (tau N η) = sPlus t (theta N) (tau N η)-unphasedZeroModeSum N t η''',
     'depthCompletionError_eq_difference'),
    ('CompletionUniformClaim', '''∀ t : ℝ, 0 < t →
      ∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, 0 < N → ∀ τ : Tangent,
        ‖depthCompletionError N t τ‖ ≤ C/(N : ℝ)''', 'completion_error_uniform_exists'),
    ('NormalizedIdentityClaim', '''∀ N : ℕ, 0 < N → ∀ η : Frequency,
      amplitude N criticalTilt η = (leadingScale N : ℂ)*
        (sPlus criticalTilt (theta N) (tau N η)+normalizedRemainder N η)''',
     'normalizedRemainder_identity'),
    ('NormalizedUniformClaim', '''∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, 1 ≤ N → ∀ η : Frequency,
      frequencyNorm η ≤ Real.pi/6 → ‖normalizedRemainder N η‖ ≤
        C*(Real.rpow (N : ℝ) (-(1 : ℝ)/2)+|normalFrequency η|)''', 'normalized_error_uniform_exists'),
]

CLAIM_MUTATIONS = {
    'FullScalarClaim': ('AliceLayersB', 'AliceLayersB ∧ False'),
    'ExplicitWitnessesClaim': ('frequencyNorm η ≤ Real.pi/6', 'frequencyNorm η ≤ Real.pi/3'),
    'BoundaryPositiveClaim': ('0 < boundaryResource', '1 < boundaryResource'),
    'BoundaryIntegralClaim': ('16*Real.pi', '17*Real.pi'),
    'PhaseSignClaim': ('geometricZeroModeSum N t η-unphasedZeroModeSum N t η',
                       'geometricZeroModeSum N t η+unphasedZeroModeSum N t η'),
    'PhaseUniformClaim': ('∃ C : ℝ, 0 ≤ C ∧ ∀ N : ℕ, 0 < N →',
                          '∀ N : ℕ, 0 < N → ∃ C : ℝ, 0 ≤ C ∧'),
    'ActiveIndicesClaim': ('depthPlaneIndex N j ∈', '(depthPlaneIndex N j+1) ∈'),
    'CompletionSignClaim': ('(tau N η)-unphasedZeroModeSum', '(tau N η)+unphasedZeroModeSum'),
    'CompletionUniformClaim': ('C/(N : ℝ)', 'C/((N : ℝ)+1)'),
    'NormalizedIdentityClaim': ('(tau N η)+normalizedRemainder', '(tau N η)-normalizedRemainder'),
    'NormalizedUniformClaim': ('(Real.rpow (N : ℝ) (-(1 : ℝ)/2)+|normalFrequency η|)',
                               '(Real.rpow (N : ℝ) (-(1 : ℝ)/2)*|normalFrequency η|)'),
}


def main():
    challenge = ['import Mathlib', '', '/-!',
                 'Final scalar comparator. Imports no project modules or project structures.',
                 'Definitions copied verbatim from the manifest final_comparator_sources.json.',
                 'Claim selection: block 5 of ORDEN_TRABAJO_2026-11-11.md, not all auxiliary lemmas.',
                 'Source herramientas: '+PROVENANCE+'.',
                 'This file can be read independently of all implementation proof modules.',
                 '-/', 'noncomputable section', 'open scoped BigOperators',
                 'open MeasureTheory', 'namespace AliceFinalChallenge', '',
                 'local notation "Lattice" => (Fin 3 → ℤ)',
                 'local notation "Frequency" => (Fin 3 → ℝ)',
                 'local notation "Tangent" => (Fin 2 → ℝ)', '']
    mutations = []
    manifest = {}
    mismatch = r'(?i)AliceComparator/FinalSolution\.lean[^\n]*error:[^\n]*type mismatch'
    for module, names in SOURCES.items():
        text = (HERE/f'AliceLayers/{module}.lean').read_text()
        for name in names:
            original = declaration(text, name)
            manifest[name] = {'source': f'AliceLayers/{module}.lean',
                              'sha256': hashlib.sha256(original.encode()).hexdigest()}
            challenge.extend([original, ''])
            signature, body = original.split(':=', 1)
            body = body.strip()
            if name in {'latticeBox', 'aliceSites', 'activeDepthIndices'}:
                changed = '∅'
            elif name in {'transverseCoordinates', 'tau'}:
                changed = f'fun i => ({body}) i + 1'
            elif name == 'AliceLayersB':
                changed = 'False'
            else:
                changed = f'({body}) + 1'
            mutations.append(dict(nombre='definition: '+name, fichero='AliceComparator/FinalChallenge.lean',
                                  antes=original, despues=signature+':=\n  '+changed, espera=mismatch))
    solution = ['import AliceComparator.FinalChallenge', 'import AliceLayers.Assembly', '',
                'set_option maxHeartbeats 1000000', 'namespace AliceFinalSolution', '']
    for name, statement, theorem in CLAIMS:
        original = f'def {name} : Prop :=\n  {statement}'
        challenge.extend([original, ''])
        solution.extend([f'theorem {name} : AliceFinalChallenge.{name} :=',
                         f'  @AliceLayers.{theorem}', ''])
        before, after = CLAIM_MUTATIONS[name]
        if original.count(before) != 1:
            raise ValueError(f'Non-unique claim mutation {name}')
        mutations.append(dict(nombre='claim: '+name, fichero='AliceComparator/FinalChallenge.lean',
                              antes=original, despues=original.replace(before, after, 1), espera=mismatch))
    mutations.append(dict(nombre='axioms: full scalar proof replaced by sorry',
                          fichero='AliceComparator/FinalSolution.lean',
                          antes='  @AliceLayers.aliceLayersB_proved', despues='  sorry',
                          espera=r'(?s)AliceComparator/FinalAxioms\.lean.*non-standard axioms: \[sorryAx\]'))
    challenge.extend(['end AliceFinalChallenge', ''])
    solution.extend(['end AliceFinalSolution', ''])
    axioms = ['import AliceComparator.FinalSolution', 'import AliceComparator.AssertAxioms', '',
              f'/-- info: {len(CLAIMS)} theorems use only propext, Classical.choice, Quot.sound -/',
              '#guard_msgs in', '#assert_standard_axioms']
    axioms.extend('  AliceFinalSolution.'+name for name, _, _ in CLAIMS)
    specs = ['# Generated by write_final_comparator.py; source remains permanent.', 'timeout = 180', '']
    for entry in mutations:
        specs.append('[[mutacion]]')
        specs.extend(f'{key} = {json.dumps(value, ensure_ascii=False)}' for key, value in entry.items())
        specs.append('')
    artifacts = {
        'AliceComparator/FinalChallenge.lean': '\n'.join(challenge),
        'AliceComparator/FinalSolution.lean': '\n'.join(solution),
        'AliceComparator/FinalAxioms.lean': '\n'.join(axioms)+'\n',
        'final_comparator_sources.json': json.dumps(manifest, ensure_ascii=False, indent=2)+'\n',
        'mutaciones_final.toml': '\n'.join(specs)+'\n',
    }
    for path in artifacts:
        if (HERE/path).exists():
            raise FileExistsError(path)
    for path, text in artifacts.items():
        (HERE/path).write_text(text)
    print(f'Generated: {len(manifest)} definitions, {len(CLAIMS)} claims, {len(mutations)} mutations')


if __name__ == '__main__':
    main()
