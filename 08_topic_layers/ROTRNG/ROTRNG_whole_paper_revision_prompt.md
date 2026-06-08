# ROTRNG Whole-Paper Revision Prompt

把这段给另一个 Codex。它的任务是先审查全篇，不是直接大改。

```text
You are reviewing the existing manuscript:

E:/Project/MLDSA/RO_TRNG/paper/RO_TRNG_entropy_boundary/manuscript/main.tex

Read first:

1. E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/07_writing_assets/micro_style_audit_assets/section_function_taxonomy.md
2. E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/07_writing_assets/micro_style_audit_assets/whole_paper_review_rubric.md
3. E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/07_writing_assets/micro_style_audit_assets/figure_role_taxonomy.md
4. E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/07_writing_assets/micro_style_audit_assets/table_role_taxonomy.md
5. E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/08_topic_layers/ROTRNG/ROTRNG_section_by_section_review_map.md
6. E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/08_topic_layers/ROTRNG/ROTRNG_figure_table_audit_sheet.csv

Task:

1. Do not rewrite immediately.
2. Produce a section-by-section issue list.
3. Produce a figure/table action list: retain, merge, compress, appendix, or revise caption.
4. Identify which numbers belong in the abstract and which belong only in result tables.
5. Identify every sentence that risks overclaiming certification, security, universal FPGA behavior, or physical-model completeness.
6. Then propose a minimal revision plan.

Rules:

- Do not invent results.
- Do not move the manuscript directory.
- Do not merge the TVLSI sampler-aperture manuscript.
- Keep the paper as a TIM-style measurement-boundary paper.
- Treat TDC and Reduced-XOR as diagnostic evidence, not full physical proof.
```
