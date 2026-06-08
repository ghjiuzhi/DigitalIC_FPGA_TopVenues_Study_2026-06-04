# ROTRNG Detail Review Prompt

把下面这段给另一个 Codex。任务是细节审查，不是直接改正文。

```text
You are reviewing details of:

E:/Project/MLDSA/RO_TRNG/paper/RO_TRNG_entropy_boundary

Read:

1. E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/07_writing_assets/micro_style_audit_assets/citation_reference_style_guide.md
2. E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/07_writing_assets/micro_style_audit_assets/bibtex_quality_checklist.md
3. E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/07_writing_assets/micro_style_audit_assets/cross_reference_style_guide.md
4. E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/07_writing_assets/micro_style_audit_assets/number_unit_symbol_style_guide.md
5. E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/07_writing_assets/micro_style_audit_assets/claim_language_risk_lexicon.md
6. E:/DigitalIC_FPGA_TopVenues_Study_2026-06-04/08_topic_layers/ROTRNG/ROTRNG_reference_usage_matrix.csv
7. E:/Project/MLDSA/RO_TRNG/paper/RO_TRNG_entropy_boundary/manuscript/main.tex
8. E:/Project/MLDSA/RO_TRNG/paper/RO_TRNG_entropy_boundary/refs/references.bib

Do not edit files yet. Produce:

1. Citation map: cite key -> line -> sentence function.
2. Unused references: keep/cite/delete recommendation.
3. Missing citation candidates for unsupported related-work claims.
4. Number/unit/math-mode inconsistencies with line numbers.
5. Cross-reference and caption issues by label.
6. Abbreviation/keyword inconsistencies.
7. Claim-risk sentences using prove/certify/secure/robust/universal/complete.
8. Appendix candidates for tables or traceability details.

Rules:

- Do not invent citations or results.
- Do not claim SP800-90B certification.
- Treat TDC and Reduced-XOR as diagnostic evidence.
- Every recommendation must include a file line number or LaTeX label.
```
