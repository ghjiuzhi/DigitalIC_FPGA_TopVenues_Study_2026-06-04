# Deep Morphology Audit Pipeline

This module moves the writing audit unit from section-level comments to sentence, clause, claim, evidence-anchor, and punctuation records.

Primary command:

```powershell
python 09_manuscript_audit_pipeline\deep_morphology\audit_deep_morphology.py
```

Generated outputs:

- `corpus/topvenue_sentence_morphology.csv`
- `corpus/topvenue_function_sequence_profiles.md`
- `manuscript/manuscript_sentence_morphology.csv`
- `manuscript/citation_function_matrix.csv`
- `reports/deep_morphology_alignment_report.md`
- `reports/abstract_deep_sentence_morphology.md`
- `reports/results_deep_paragraph_morphology.md`

The pipeline reads the local top-venue corpus in `07_writing_assets` and the active RO-TRNG manuscript source listed in `08_topic_layers/ROTRNG/metadata/active_manuscripts.csv`. It does not rewrite the manuscript.
