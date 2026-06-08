# 深度形态学审计管线

这个目录用于把论文审计粒度从“章节级评价”降到“句子、从句、claim 动词、证据锚点、标点”的级别。

核心原则：

```text
不要以章节为单位审计。
要以句子、从句、claim 动词、证据锚点、标点为单位审计。
```

运行命令：

```powershell
python 09_manuscript_audit_pipeline\deep_morphology\audit_deep_morphology.py
```

## 输出文件

- `schemas/sentence_morphology_schema.md`：逐句审计字段说明。
- `schemas/clause_morphology_schema.md`：从句级 claim 拆解说明。
- `schemas/punctuation_morphology_schema.md`：标点级审计说明。
- `corpus/topvenue_sentence_morphology.csv`：顶刊语料逐句数据库。
- `corpus/topvenue_function_sequence_profiles.md`：顶刊各章节功能序列画像。
- `corpus/topvenue_paper_sequence_archetypes.csv`：每篇论文每个 section 的精确序列、压缩序列和组织范式。
- `corpus/topvenue_venue_archetype_matrix.csv`：venue 与组织范式的交叉统计。
- `manuscript/manuscript_sentence_morphology.csv`：当前 RO-TRNG 稿件逐句数据库。
- `manuscript/manuscript_clause_morphology.csv`：当前稿件从句级 claim 风险数据库。
- `manuscript/figure_table_inventory.csv`：图表元素级审计清单。
- `manuscript/citation_function_matrix.csv`：引用和句子功能绑定表。
- `calibration/gold_sentence_labels_template.csv`：50 句人工 gold-label 校准模板。
- `reports/deep_morphology_alignment_report.md`：当前稿件和顶刊形态的对齐报告。
- `reports/abstract_deep_sentence_morphology.md`：摘要逐句专项报告。
- `reports/results_deep_paragraph_morphology.md`：Results 段落专项报告。
- `reports/clause_claim_risk_report.md`：从句级 claim 风险报告。
- `reports/figure_table_element_morphology_report.md`：图表元素级形态报告。
- `reports/corpus_extraction_quality_report.md`：顶刊语料清洗质量报告。
- `reports/annotation_accuracy_report.md`：人工标注后的准确率报告。

## 注意

- 这个管线只生成审计数据和报告，不改写稿件原文。
- CSV 字段名保留英文，方便脚本稳定和后续筛选。
- Markdown 报告和说明默认使用中文，便于直接阅读和改稿。
