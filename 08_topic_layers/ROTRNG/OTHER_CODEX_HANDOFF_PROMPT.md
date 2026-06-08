# Prompt For Another Codex

你正在修改一个已有 RO-TRNG 论文工作区。你的任务不是重新下载文献，也不是重构目录，而是基于已有“写法层 + ROTRNG 方向层 + 正文 evidence”改进当前稿件的写法、related work、Introduction gap 和 claim framing。

## Paths

- Writing-style library: `E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/07_writing_assets`
- ROTRNG direction corpus: `E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/08_topic_layers/ROTRNG`
- Active manuscript to revise: `E:/Project/MLDSA/RO_TRNG/paper/RO_TRNG_entropy_boundary`
- Do not edit as the main target: `E:/Project/MLDSA/RO_TRNG/paper/RO_TRNG_tvlsi_sampler_aperture`

## Main Goal

Revise `RO_TRNG_entropy_boundary` into a clearer measurement-driven entropy-boundary paper. It should argue, with bounded evidence, that sampler-side implementation should be considered in the measured entropy-source boundary of the evaluated FPGA RO-TRNG setup.

Do not rewrite it as:

- a new TRNG architecture paper,
- an SP800-90B certification report,
- a universal FPGA-family entropy model,
- a TVLSI design-rule paper,
- or a merged version of the separate sampler-aperture manuscript.

## Read First

Read these files before editing prose:

1. `E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/07_writing_assets/manuscript_style_imitation_guide.md`
2. `E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/07_writing_assets/title_abstract_intro_patterns.md`
3. `E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/07_writing_assets/post_edit_review_checklist.md`
4. `E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/07_writing_assets/figure_table_review_guide.md`
5. `E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/08_topic_layers/ROTRNG/literature_status.md`
6. `E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/08_topic_layers/ROTRNG/metadata/core_literature_selection.csv`
7. `E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/08_topic_layers/ROTRNG/manuscript_revision_bridge.md`
8. `E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/08_topic_layers/ROTRNG/ROTRNG_style_to_manuscript_bridge.md`
9. `E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/08_topic_layers/ROTRNG/ROTRNG_direction_writing_patterns.md`
10. `E:/Project/MLDSA/RO_TRNG/paper/RO_TRNG_entropy_boundary/evidence/claim_evidence_table.md`
11. `E:/Project/MLDSA/RO_TRNG/paper/RO_TRNG_entropy_boundary/evidence/related_work_matrix.md`
12. `E:/Project/MLDSA/RO_TRNG/paper/RO_TRNG_entropy_boundary/manuscript/main.tex`

## Revision Priority

1. Extract the paper's 3 strongest supported claims from `claim_evidence_table.md`.
2. Rewrite or audit the title, abstract, and contribution list so they match those claims.
3. Strengthen the Introduction gap around sampler-side measurement boundary, restart behavior, and implementation-sensitive evaluation.
4. Update or audit related work coverage using `core_literature_selection.csv`.
5. Update `refs/references.bib` only for sources actually cited in `main.tex`.
6. Check whether figure/table captions support the same claim chain. Do not invent figures or results.

## Style-Layer Imitation Requirement

Imitate paragraph function, not wording.

Use this shape:

- Title: object + mechanism/boundary + platform or setup.
- Abstract: problem -> method -> setup -> evidence -> bounded claim.
- Introduction: application context -> measurement problem -> prior-work gap -> this paper contribution.
- Related Work: group by technical route, not by year.
- Figures/tables: every figure or table must support a named claim.

Use cautious claim language:

- Prefer `observed`, `indicates`, `suggests`, `is consistent with`, `under this setup`.
- Avoid `proves`, `guarantees`, `certifies`, `secure`, `robust`, `universal` unless evidence explicitly supports it.

## ROTRNG Direction Requirements

Keep these distinctions clear:

- `entropy source` is not automatically the same as `sampler` or `conditioning`.
- Passing statistical tests is not the same as proving security.
- SP800-90B can be discussed as guidance/context only unless the manuscript contains a full certification workflow.
- Attack and environmental papers can motivate sensitivity, but do not claim attack resistance without experiments.
- PUF-TRNG literature may support context, but do not mix identity/stability claims into TRNG entropy claims.

## Hard Rules

- Do not move manuscript folders.
- Do not restructure the literature library.
- Do not merge `RO_TRNG_tvlsi_sampler_aperture` into this manuscript.
- Do not redownload papers.
- Do not invent experimental results, device parameters, figures, tables, or comparison numbers.
- Every abstract-level and conclusion-level claim must trace to `evidence/claim_evidence_table.md` or another explicit local evidence file.
- If evidence is missing, write a TODO/risk note instead of fabricating support.

## Required Self-Review Before Finishing

Run these four checks and report the result:

1. Claim-evidence review: map every strong claim to evidence.
2. Writing-style review: check title, abstract, Introduction, contribution list, related work structure, and captions against the writing assets.
3. ROTRNG terminology review: check entropy boundary, sampler, restart, NIST/SP800-90B, security/attack wording.
4. Venue-fit review: ensure the manuscript remains a TIM-style measurement paper, not a TVLSI design-rule paper.

## Deliver Back To The User

At the end, report:

- files changed,
- claims strengthened or weakened,
- citations added/removed and why,
- unresolved evidence gaps,
- any sentence that the user should manually approve because it may be too strong.
