# 投稿形态学对齐总览

这个总览汇总当前 manuscript 在全文（paper）、章节（section）、段落（paragraph）、句子（sentence）、从句（clause）、图（figure）、表（table）、引用（citation）和标点（punctuation）层面的顶刊形态偏离。报告只生成 revision packet，不直接重写 manuscript。

## 总体状态

- 顶刊清洗后 corpus：1271 条功能单元。
- manuscript 逐句记录：292 条。
- 从句记录：547 条。
- 图表记录：9 个。
- citation 记录：7 条。
- 必须修改：236 项；建议修改：339 项；可选修改：0 项。

## 必须修改

- `ABS.S1`：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（重写句子功能；调整句子顺序）。ABS.S1: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `SETUP` 与顶刊期望 `BG` 不一致。；ABS.S1: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S2`：`ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;REFUNCTION_SENTENCE;REORDER_SENTENCE`（补桥接句/桥接短语；补证据锚点；重写句子功能；调整句子顺序）。ABS.S2: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。；ABS.S2: ADD_EVIDENCE_ANCHOR（补证据锚点）：该位置存在 `medium` 强度 claim，但证据锚点为 `None`。；ABS.S2: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `GAP` 与顶刊期望 `PROBLEM` 不一致。；ABS.S2: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S3`：`REPLACE_RISK_VERB;REFUNCTION_SENTENCE;REORDER_SENTENCE`（替换高风险动词/泛词；重写句子功能；调整句子顺序）。ABS.S3: REPLACE_RISK_VERB（替换高风险动词/泛词）：存在高风险动词、泛词或 AI 味表达，需要替换成可证实表述。；ABS.S3: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `SETUP` 与顶刊期望 `GAP` 不一致。；ABS.S3: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S4`：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（重写句子功能；调整句子顺序）。ABS.S4: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `RESULT` 与顶刊期望 `METHOD` 不一致。；ABS.S4: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S5`：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（重写句子功能；调整句子顺序）。ABS.S5: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `BG` 与顶刊期望 `SETUP` 不一致。；ABS.S5: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S6`：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（重写句子功能；调整句子顺序）。ABS.S6: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `BG` 与顶刊期望 `RESULT` 不一致。；ABS.S6: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S7`：`ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;REPLACE_RISK_VERB;REFUNCTION_SENTENCE;REORDER_SENTENCE`（补桥接句/桥接短语；补证据锚点；替换高风险动词/泛词；重写句子功能；调整句子顺序）。ABS.S7: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。；ABS.S7: ADD_EVIDENCE_ANCHOR（补证据锚点）：该位置存在 `medium` 强度 claim，但证据锚点为 `None`。；ABS.S7: REPLACE_RISK_VERB（替换高风险动词/泛词）：存在高风险动词、泛词或 AI 味表达，需要替换成可证实表述。；ABS.S7: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `RESULT` 与顶刊期望 `BOUNDARY` 不一致。；ABS.S7: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S8`：`ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;SPLIT_SENTENCE;REFUNCTION_SENTENCE;REORDER_SENTENCE`（补桥接句/桥接短语；补证据锚点；拆句；重写句子功能；调整句子顺序）。ABS.S8: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。；ABS.S8: ADD_EVIDENCE_ANCHOR（补证据锚点）：该位置存在 `medium` 强度 claim，但证据锚点为 `None`。；ABS.S8: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。；ABS.S8: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `GAP` 与顶刊期望 `BOUNDARY` 不一致。；ABS.S8: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S9`：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（重写句子功能；调整句子顺序）。ABS.S9: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `RESULT` 与顶刊期望 `BOUNDARY` 不一致。；ABS.S9: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `INTRODUCTION.P1.S3`：`ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;SPLIT_SENTENCE`（补桥接句/桥接短语；补证据锚点；拆句）。INTRODUCTION.P1.S3: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。；INTRODUCTION.P1.S3: ADD_EVIDENCE_ANCHOR（补证据锚点）：该位置存在 `medium` 强度 claim，但证据锚点为 `None`。；INTRODUCTION.P1.S3: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `INTRODUCTION.P1.S5`：`ADD_BRIDGE`（补桥接句/桥接短语）。INTRODUCTION.P1.S5: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。
- `INTRODUCTION.P3.S2`：`ADD_BRIDGE`（补桥接句/桥接短语）。INTRODUCTION.P3.S2: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。
- `INTRODUCTION.P3.S3`：`ADD_BRIDGE`（补桥接句/桥接短语）。INTRODUCTION.P3.S3: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。
- `INTRODUCTION.P5.S2`：`ADD_BRIDGE`（补桥接句/桥接短语）。INTRODUCTION.P5.S2: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。
- `INTRODUCTION.P6.S3`：`ADD_EVIDENCE_ANCHOR`（补证据锚点）。INTRODUCTION.P6.S3: ADD_EVIDENCE_ANCHOR（补证据锚点）：该位置存在 `medium` 强度 claim，但证据锚点为 `None`。
- `INTRODUCTION.P6.S4`：`ADD_BRIDGE`（补桥接句/桥接短语）。INTRODUCTION.P6.S4: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。
- `INTRODUCTION.P6.S5`：`ADD_BRIDGE;SPLIT_SENTENCE`（补桥接句/桥接短语；拆句）。INTRODUCTION.P6.S5: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。；INTRODUCTION.P6.S5: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `INTRODUCTION.P7.S2`：`ADD_BRIDGE`（补桥接句/桥接短语）。INTRODUCTION.P7.S2: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。
- `INTRODUCTION.P7.S5`：`ADD_BRIDGE;SPLIT_SENTENCE`（补桥接句/桥接短语；拆句）。INTRODUCTION.P7.S5: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。；INTRODUCTION.P7.S5: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `INTRODUCTION.P7.S6`：`ADD_BRIDGE`（补桥接句/桥接短语）。INTRODUCTION.P7.S6: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。

## 建议修改

- `INTRODUCTION.P3.S1`：`ADD_BOUNDARY`（补边界条件）。INTRODUCTION.P3.S1: ADD_BOUNDARY（补边界条件）：需要补充适用条件、实验边界或不可外推范围。
- `INTRODUCTION.P3.S4`：`REPLACE_RISK_VERB`（替换高风险动词/泛词）。INTRODUCTION.P3.S4: REPLACE_RISK_VERB（替换高风险动词/泛词）：存在高风险动词、泛词或 AI 味表达，需要替换成可证实表述。
- `INTRODUCTION.P4.S1`：`CHANGE_PUNCTUATION`（调整标点）。INTRODUCTION.P4.S1: CHANGE_PUNCTUATION（调整标点）：标点形态影响技术论文语气或句子清晰度。
- `BACKGROUND_AND_MEASUREMENT_GAP.P1.S1`：`SPLIT_SENTENCE`（拆句）。BACKGROUND_AND_MEASUREMENT_GAP.P1.S1: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `BACKGROUND_AND_MEASUREMENT_GAP.P3.S1`：`SPLIT_SENTENCE`（拆句）。BACKGROUND_AND_MEASUREMENT_GAP.P3.S1: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `BACKGROUND_AND_MEASUREMENT_GAP.P3.S3`：`SPLIT_SENTENCE`（拆句）。BACKGROUND_AND_MEASUREMENT_GAP.P3.S3: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `BACKGROUND_AND_MEASUREMENT_GAP.P4.S2`：`REPLACE_RISK_VERB;SPLIT_SENTENCE`（替换高风险动词/泛词；拆句）。BACKGROUND_AND_MEASUREMENT_GAP.P4.S2: REPLACE_RISK_VERB（替换高风险动词/泛词）：存在高风险动词、泛词或 AI 味表达，需要替换成可证实表述。；BACKGROUND_AND_MEASUREMENT_GAP.P4.S2: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `DESIGN_AND_MEASUREMENT_WORKFLOW.P1.S3`：`SPLIT_SENTENCE`（拆句）。DESIGN_AND_MEASUREMENT_WORKFLOW.P1.S3: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `DESIGN_AND_MEASUREMENT_WORKFLOW.P2.S2`：`SPLIT_SENTENCE`（拆句）。DESIGN_AND_MEASUREMENT_WORKFLOW.P2.S2: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1`：`SPLIT_SENTENCE`（拆句）。DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S2`：`SPLIT_SENTENCE`（拆句）。DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S2: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `DESIGN_AND_MEASUREMENT_WORKFLOW.P4.S2`：`SPLIT_SENTENCE`（拆句）。DESIGN_AND_MEASUREMENT_WORKFLOW.P4.S2: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `DESIGN_AND_MEASUREMENT_WORKFLOW.P5.S1`：`SPLIT_SENTENCE`（拆句）。DESIGN_AND_MEASUREMENT_WORKFLOW.P5.S1: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `DESIGN_AND_MEASUREMENT_WORKFLOW.P5.S2`：`SPLIT_SENTENCE`（拆句）。DESIGN_AND_MEASUREMENT_WORKFLOW.P5.S2: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P2.S1`：`SPLIT_SENTENCE`（拆句）。EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P2.S1: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P3.S1`：`ADD_BOUNDARY`（补边界条件）。EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P3.S1: ADD_BOUNDARY（补边界条件）：需要补充适用条件、实验边界或不可外推范围。
- `EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P4.S4`：`REPLACE_RISK_VERB;SPLIT_SENTENCE`（替换高风险动词/泛词；拆句）。EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P4.S4: REPLACE_RISK_VERB（替换高风险动词/泛词）：存在高风险动词、泛词或 AI 味表达，需要替换成可证实表述。；EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P4.S4: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P4.S6`：`SPLIT_SENTENCE`（拆句）。EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P4.S6: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `RESTART_AND_WARMUP_CHARACTERIZATION.P3.S1`：`SPLIT_SENTENCE`（拆句）。RESTART_AND_WARMUP_CHARACTERIZATION.P3.S1: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `RESTART_AND_WARMUP_CHARACTERIZATION.P4.S3`：`REPLACE_RISK_VERB`（替换高风险动词/泛词）。RESTART_AND_WARMUP_CHARACTERIZATION.P4.S3: REPLACE_RISK_VERB（替换高风险动词/泛词）：存在高风险动词、泛词或 AI 味表达，需要替换成可证实表述。

## 可选修改

- 低风险术语统一、图表微调和局部标点微调可在 must/should 完成后处理。
