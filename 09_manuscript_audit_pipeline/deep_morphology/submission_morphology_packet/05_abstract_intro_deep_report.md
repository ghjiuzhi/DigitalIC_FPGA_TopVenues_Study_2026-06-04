# Abstract / Introduction 深度报告

这一部分检查摘要和引言是否按顶刊功能链展开。

- `ABS.S1` `SETUP`（实验/平台设置）→ `REFUNCTION_SENTENCE;REORDER_SENTENCE`（重写句子功能；调整句子顺序）：ABS.S1: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `SETUP` 与顶刊期望 `BG` 不一致。；ABS.S1: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S2` `GAP`（缺口）→ `ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;REFUNCTION_SENTENCE;REORDER_SENTENCE`（补桥接句/桥接短语；补证据锚点；重写句子功能；调整句子顺序）：ABS.S2: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。；ABS.S2: ADD_EVIDENCE_ANCHOR（补证据锚点）：该位置存在 `medium` 强度 claim，但证据锚点为 `None`。；ABS.S2: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `GAP` 与顶刊期望 `PROBLEM` 不一致。；ABS.S2: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S3` `SETUP`（实验/平台设置）→ `REPLACE_RISK_VERB;REFUNCTION_SENTENCE;REORDER_SENTENCE`（替换高风险动词/泛词；重写句子功能；调整句子顺序）：ABS.S3: REPLACE_RISK_VERB（替换高风险动词/泛词）：存在高风险动词、泛词或 AI 味表达，需要替换成可证实表述。；ABS.S3: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `SETUP` 与顶刊期望 `GAP` 不一致。；ABS.S3: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S4` `RESULT`（结果）→ `REFUNCTION_SENTENCE;REORDER_SENTENCE`（重写句子功能；调整句子顺序）：ABS.S4: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `RESULT` 与顶刊期望 `METHOD` 不一致。；ABS.S4: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S5` `BG`（背景）→ `REFUNCTION_SENTENCE;REORDER_SENTENCE`（重写句子功能；调整句子顺序）：ABS.S5: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `BG` 与顶刊期望 `SETUP` 不一致。；ABS.S5: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S6` `BG`（背景）→ `REFUNCTION_SENTENCE;REORDER_SENTENCE`（重写句子功能；调整句子顺序）：ABS.S6: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `BG` 与顶刊期望 `RESULT` 不一致。；ABS.S6: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S7` `RESULT`（结果）→ `ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;REPLACE_RISK_VERB;REFUNCTION_SENTENCE;REORDER_SENTENCE`（补桥接句/桥接短语；补证据锚点；替换高风险动词/泛词；重写句子功能；调整句子顺序）：ABS.S7: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。；ABS.S7: ADD_EVIDENCE_ANCHOR（补证据锚点）：该位置存在 `medium` 强度 claim，但证据锚点为 `None`。；ABS.S7: REPLACE_RISK_VERB（替换高风险动词/泛词）：存在高风险动词、泛词或 AI 味表达，需要替换成可证实表述。；ABS.S7: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `RESULT` 与顶刊期望 `BOUNDARY` 不一致。；ABS.S7: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S8` `GAP`（缺口）→ `ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;SPLIT_SENTENCE;REFUNCTION_SENTENCE;REORDER_SENTENCE`（补桥接句/桥接短语；补证据锚点；拆句；重写句子功能；调整句子顺序）：ABS.S8: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。；ABS.S8: ADD_EVIDENCE_ANCHOR（补证据锚点）：该位置存在 `medium` 强度 claim，但证据锚点为 `None`。；ABS.S8: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。；ABS.S8: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `GAP` 与顶刊期望 `BOUNDARY` 不一致。；ABS.S8: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `ABS.S9` `RESULT`（结果）→ `REFUNCTION_SENTENCE;REORDER_SENTENCE`（重写句子功能；调整句子顺序）：ABS.S9: REFUNCTION_SENTENCE（重写句子功能）：当前功能 `RESULT` 与顶刊期望 `BOUNDARY` 不一致。；ABS.S9: REORDER_SENTENCE（调整句子顺序）：句子顺序不符合目标功能链，需要前移、后移或并入相邻句。
- `INTRODUCTION.P1.S3` `SETUP`（实验/平台设置）→ `ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;SPLIT_SENTENCE`（补桥接句/桥接短语；补证据锚点；拆句）：INTRODUCTION.P1.S3: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。；INTRODUCTION.P1.S3: ADD_EVIDENCE_ANCHOR（补证据锚点）：该位置存在 `medium` 强度 claim，但证据锚点为 `None`。；INTRODUCTION.P1.S3: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `INTRODUCTION.P1.S5` `BG`（背景）→ `ADD_BRIDGE`（补桥接句/桥接短语）：INTRODUCTION.P1.S5: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。
- `INTRODUCTION.P3.S1` `INTERPRETATION`（解释）→ `ADD_BOUNDARY`（补边界条件）：INTRODUCTION.P3.S1: ADD_BOUNDARY（补边界条件）：需要补充适用条件、实验边界或不可外推范围。
- `INTRODUCTION.P3.S2` `SETUP`（实验/平台设置）→ `ADD_BRIDGE`（补桥接句/桥接短语）：INTRODUCTION.P3.S2: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。
- `INTRODUCTION.P3.S3` `SETUP`（实验/平台设置）→ `ADD_BRIDGE`（补桥接句/桥接短语）：INTRODUCTION.P3.S3: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。
- `INTRODUCTION.P3.S4` `BG`（背景）→ `REPLACE_RISK_VERB`（替换高风险动词/泛词）：INTRODUCTION.P3.S4: REPLACE_RISK_VERB（替换高风险动词/泛词）：存在高风险动词、泛词或 AI 味表达，需要替换成可证实表述。
- `INTRODUCTION.P4.S1` `SETUP`（实验/平台设置）→ `CHANGE_PUNCTUATION`（调整标点）：INTRODUCTION.P4.S1: CHANGE_PUNCTUATION（调整标点）：标点形态影响技术论文语气或句子清晰度。
- `INTRODUCTION.P5.S2` `SETUP`（实验/平台设置）→ `ADD_BRIDGE`（补桥接句/桥接短语）：INTRODUCTION.P5.S2: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。
- `INTRODUCTION.P6.S3` `BG`（背景）→ `ADD_EVIDENCE_ANCHOR`（补证据锚点）：INTRODUCTION.P6.S3: ADD_EVIDENCE_ANCHOR（补证据锚点）：该位置存在 `medium` 强度 claim，但证据锚点为 `None`。
- `INTRODUCTION.P6.S4` `RESULT`（结果）→ `ADD_BRIDGE`（补桥接句/桥接短语）：INTRODUCTION.P6.S4: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。
- `INTRODUCTION.P6.S5` `BG`（背景）→ `ADD_BRIDGE;SPLIT_SENTENCE`（补桥接句/桥接短语；拆句）：INTRODUCTION.P6.S5: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。；INTRODUCTION.P6.S5: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `INTRODUCTION.P7.S2` `GAP`（缺口）→ `ADD_BRIDGE`（补桥接句/桥接短语）：INTRODUCTION.P7.S2: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。
- `INTRODUCTION.P7.S5` `SETUP`（实验/平台设置）→ `ADD_BRIDGE;SPLIT_SENTENCE`（补桥接句/桥接短语；拆句）：INTRODUCTION.P7.S5: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。；INTRODUCTION.P7.S5: SPLIT_SENTENCE（拆句）：一句话承载多个 claim 或从句过载，建议拆分。
- `INTRODUCTION.P7.S6` `BOUNDARY`（边界）→ `ADD_BRIDGE`（补桥接句/桥接短语）：INTRODUCTION.P7.S6: ADD_BRIDGE（补桥接句/桥接短语）：上下句关系跳跃，需要桥接前后论证。
