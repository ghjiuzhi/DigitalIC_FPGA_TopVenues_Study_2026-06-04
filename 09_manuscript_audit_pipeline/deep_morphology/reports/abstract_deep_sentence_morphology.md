# 摘要逐句深度形态学报告

顶刊目标序列：`BG -> PROBLEM -> GAP -> METHOD -> SETUP -> RESULT -> BOUNDARY`。

当前摘要序列：`SETUP -> GAP -> SETUP -> RESULT -> BG -> BG -> RESULT -> GAP -> RESULT`。

## ABS.S1

原句：FPGA ring-oscillator true random number generators are commonly evaluated from oscillator-array structure and final output statistics.

- 当前功能：`SETUP`（实验/平台设置）
- 该位置期望功能：`BG`
- claim：`method`（方法 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 建议动作：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（REFUNCTION_SENTENCE；REORDER_SENTENCE）

## ABS.S2

原句：This paper reports a two-board Zynq-7020 {} case study showing that this boundary can be insufficient: sampler-side physical implementation can substantially reshape measured restart behavior.

- 当前功能：`GAP`（缺口）
- 该位置期望功能：`PROBLEM`
- claim：`method`（方法 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`无`
- 建议动作：`ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;REFUNCTION_SENTENCE;REORDER_SENTENCE`（ADD_BRIDGE；补证据锚点；REFUNCTION_SENTENCE；REORDER_SENTENCE）

## ABS.S3

原句：Continuous-stream placement measurements on the primary board expose a large implementation dependence, from a biased placement with $p_1=0.337316$ and bit min-entropy 0.593606 to a near-balanced placement with $p_1=0.499969$ and bit min-entropy 0.999909.

- 当前功能：`SETUP`（实验/平台设置）
- 该位置期望功能：`GAP`
- claim：`method`（方法 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`large`
- 建议动作：`REPLACE_RISK_VERB;REFUNCTION_SENTENCE;REORDER_SENTENCE`（替换高风险动词/泛词；REFUNCTION_SENTENCE；REORDER_SENTENCE）

## ABS.S4

原句：Restart measurements then show that continuous-stream balance is not enough: warmup bytes 8 and 10 trigger fixed-position diagnostic flags, while warmup bytes 11, 12, and 16 do not.

- 当前功能：`RESULT`（结果）
- 该位置期望功能：`METHOD`
- claim：`measurement`（测量/结果 claim） / `medium`（中）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 建议动作：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（REFUNCTION_SENTENCE；REORDER_SENTENCE）

## ABS.S5

原句：The central evidence is a bidirectional sampler-side counterfactual on the primary board, plus a repeated second-board check: imposing the restart-oriented sample-RO lock changes a compact sampler configuration toward biased restart behavior on both boards, with board-specific magnitudes.

- 当前功能：`BG`（背景）
- 该位置期望功能：`SETUP`
- claim：`causal/generalization`（因果/泛化 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 建议动作：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（REFUNCTION_SENTENCE；REORDER_SENTENCE）

## ABS.S6

原句：On the second board, three-run forward warmup-4 and warmup-5 means are $p_1=0.450792$ and 0.445222, while the reverse compact-lock warmup-4 mean is 0.498300.

- 当前功能：`BG`（背景）
- 该位置期望功能：`RESULT`
- claim：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 建议动作：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（REFUNCTION_SENTENCE；REORDER_SENTENCE）

## ABS.S7

原句：Pairwise and exact counterfactual {} diagnostics show small phase correlations under the applied screens.

- 当前功能：`RESULT`（结果）
- 该位置期望功能：`BOUNDARY`
- claim：`measurement`（测量/结果 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`small`
- 建议动作：`ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;REPLACE_RISK_VERB;REFUNCTION_SENTENCE;REORDER_SENTENCE`（ADD_BRIDGE；补证据锚点；替换高风险动词/泛词；REFUNCTION_SENTENCE；REORDER_SENTENCE）

## ABS.S8

原句：Reduced-XOR, held-out sampler, warmup/aperture, and toolflow controls show that final all64 output can hide biased internal sampler-vector directions: on the second board, moving the sample RO to a held-out physical context changes warmup-10 all64 from $p_1=0.360614$ to 0.500718 while internal contributors remain biased and reorder, and a 12-capture original-vs-Explore matrix separates route-stable bias preservation from route-moving boundary cases.

- 当前功能：`GAP`（缺口）
- 该位置期望功能：`BOUNDARY`
- claim：`causal/generalization`（因果/泛化 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`无`
- 建议动作：`ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;SPLIT_SENTENCE;REFUNCTION_SENTENCE;REORDER_SENTENCE`（ADD_BRIDGE；补证据锚点；SPLIT_SENTENCE；REFUNCTION_SENTENCE；REORDER_SENTENCE）

## ABS.S9

原句：These measurements support a diagnostic claim rather than a certification claim: sampler-side physical implementation is not passive readout in the evaluated implementations and should be included in the measured entropy-source boundary.

- 当前功能：`RESULT`（结果）
- 该位置期望功能：`BOUNDARY`
- claim：`method`（方法 claim） / `medium`（中）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 建议动作：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（REFUNCTION_SENTENCE；REORDER_SENTENCE）

## 改写前的功能计划

`BG -> PROBLEM -> GAP -> METHOD -> SETUP -> RESULT -> BOUNDARY`。
