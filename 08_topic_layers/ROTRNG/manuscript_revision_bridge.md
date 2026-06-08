# Manuscript Revision Bridge

## Target Manuscript

Primary target for this bridge:

`E:/Project/MLDSA/RO_TRNG/paper/RO_TRNG_entropy_boundary`

Do not modify or merge:

`E:/Project/MLDSA/RO_TRNG/paper/RO_TRNG_tvlsi_sampler_aperture`

## Revision Order

1. Read `metadata/core_literature_selection.csv`.
2. Compare it with `RO_TRNG_entropy_boundary/evidence/related_work_matrix.md`.
3. Add missing core sources only if they support the current manuscript's measurement-boundary story.
4. Update `refs/references.bib` only for cited sources.
5. Rewrite the Introduction gap around measurement boundary, sampler-side implementation, restart behavior, and entropy-source evaluation.
6. Check abstract claims against `evidence/claim_evidence_table.md`.
7. Do not promote the paper to SP800-90B certification or universal FPGA-family claims.

## What To Change First

First-pass edits should focus on:
- Related work matrix.
- References.
- Introduction gap.
- Abstract claim boundary.

Avoid first-pass edits to:
- Results tables.
- Figures.
- TVLSI expansion material.
- Claims requiring new experiments.

## Expected Output From Another Codex

The other Codex should produce:
- A short audit of missing or weak related-work coverage.
- A proposed patch plan for related work, references, and Introduction.
- Edits only after confirming claim-evidence alignment.
