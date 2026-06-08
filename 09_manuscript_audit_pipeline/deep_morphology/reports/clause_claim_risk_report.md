# 从句级 claim 风险报告

这个报告只检查需要从句级审计的句子：长句、冒号/分号句、relative clause、条件从句、多逗号句或中高强度 claim。

## 总览

- 从句记录：547 条。
- 需要动作的从句：351 条。

## issue 统计

- `colon_sentence_split_check`：234 条。
- `multi_claim_sentence`：147 条。
- `implication_without_evidence`：63 条。
- `hidden_boundary`：22 条。
- `risk_word`：22 条。
- `relative_clause_overclaim`：2 条。

## 优先检查样例

### ABS.S2 C1

从句：This paper reports a two-board Zynq-7020 {} case study showing

- 从句类型：`main_clause`
- 功能：`METHOD`（方法）
- claim：`measurement` / `low`
- 证据：`None`（无）
- issue：`multi_claim_sentence`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### ABS.S2 C2

从句：that  this boundary can be insufficient

- 从句类型：`relative_clause`
- 功能：`GAP`（缺口）
- claim：`descriptive` / `medium`
- 证据：`None`（无）
- issue：`multi_claim_sentence;implication_without_evidence;colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE;ADD_EVIDENCE_ANCHOR`（SPLIT_SENTENCE；补证据锚点）

### ABS.S2 C3

从句：:  sampler-side physical implementation can substantially reshape measured restart behavior.

- 从句类型：`colon_clause`
- 功能：`RESULT`（结果）
- claim：`method` / `medium`
- 证据：`None`（无）
- issue：`multi_claim_sentence;implication_without_evidence;colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE;ADD_EVIDENCE_ANCHOR`（SPLIT_SENTENCE；补证据锚点）

### ABS.S4 C1

从句：Restart measurements then show

- 从句类型：`main_clause`
- 功能：`RESULT`（结果）
- claim：`measurement` / `medium`
- 证据：`Experiment setup`（实验设置）
- issue：`multi_claim_sentence`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### ABS.S4 C2

从句：that  continuous-stream balance is not enough

- 从句类型：`relative_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`multi_claim_sentence;colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### ABS.S4 C3

从句：:  warmup bytes 8 and 10 trigger fixed-position diagnostic flags

- 从句类型：`colon_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `low`
- 证据：`None`（无）
- issue：`multi_claim_sentence;colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### ABS.S4 C4

从句：while  warmup bytes 11, 12, and 16 do not.

- 从句类型：`subordinate_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `low`
- 证据：`None`（无）
- issue：`multi_claim_sentence;colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### ABS.S5 C2

从句：:  imposing the restart-oriented sample-RO lock changes a compact sampler configuration toward biased restart behavior on both boards, with board-specific magnitudes.

- 从句类型：`colon_clause`
- 功能：`BG`（背景）
- claim：`causal/generalization` / `low`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### ABS.S7 C1

从句：Pairwise and exact counterfactual {} diagnostics show small phase correlations under the applied screens.

- 从句类型：`main_clause`
- 功能：`RESULT`（结果）
- claim：`measurement` / `medium`
- 证据：`None`（无）
- issue：`implication_without_evidence;hidden_boundary;risk_word`
- 建议动作：`ADD_EVIDENCE_ANCHOR;ADD_BOUNDARY;REPLACE_RISK_VERB`（补证据锚点；补边界条件；替换高风险动词/泛词）

### ABS.S8 C1

从句：Reduced-XOR, held-out sampler, warmup/aperture, and toolflow controls show

- 从句类型：`main_clause`
- 功能：`RESULT`（结果）
- claim：`comparative` / `medium`
- 证据：`None`（无）
- issue：`multi_claim_sentence;implication_without_evidence`
- 建议动作：`SPLIT_SENTENCE;ADD_EVIDENCE_ANCHOR`（SPLIT_SENTENCE；补证据锚点）

### ABS.S8 C2

从句：that  final all64 output can hide biased internal sampler-vector directions

- 从句类型：`relative_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `medium`
- 证据：`None`（无）
- issue：`multi_claim_sentence;implication_without_evidence;colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE;ADD_EVIDENCE_ANCHOR`（SPLIT_SENTENCE；补证据锚点）

### ABS.S8 C3

从句：:  on the second board, moving the sample RO to a held-out physical context changes warmup-10 all64 from $p_1=0.360614$ to 0.500718

- 从句类型：`colon_clause`
- 功能：`BG`（背景）
- claim：`causal/generalization` / `low`
- 证据：`None`（无）
- issue：`multi_claim_sentence;colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### ABS.S8 C4

从句：while  internal contributors remain biased and reorder, and a 12-capture original-vs-Explore matrix separates route-stable bias preservation from route-moving boundary cases.

- 从句类型：`subordinate_clause`
- 功能：`GAP`（缺口）
- claim：`descriptive` / `low`
- 证据：`None`（无）
- issue：`multi_claim_sentence;colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### ABS.S9 C1

从句：These measurements support a diagnostic claim rather than a certification claim

- 从句类型：`main_clause`
- 功能：`BG`（背景）
- claim：`measurement` / `medium`
- 证据：`Experiment setup`（实验设置）
- issue：`multi_claim_sentence`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### ABS.S9 C2

从句：:  sampler-side physical implementation is not passive readout in the evaluated implementations and should be included in the measured entropy-source boundary.

- 从句类型：`colon_clause`
- 功能：`RESULT`（结果）
- claim：`method` / `low`
- 证据：`None`（无）
- issue：`multi_claim_sentence;colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### INTRODUCTION.P1.S3 C1

从句：Placement, routing, clocking, reset sequencing, sampling, and readout can all affect the final bitstream.

- 从句类型：`main_clause`
- 功能：`SETUP`（实验/平台设置）
- claim：`causal/generalization` / `medium`
- 证据：`None`（无）
- issue：`implication_without_evidence`
- 建议动作：`ADD_EVIDENCE_ANCHOR`（补证据锚点）

### INTRODUCTION.P3.S3 C1

从句：In the measurements reported here, a placement

- 从句类型：`main_clause`
- 功能：`SETUP`（实验/平台设置）
- claim：`measurement` / `none`
- 证据：`Experiment setup`（实验设置）
- issue：`multi_claim_sentence`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### INTRODUCTION.P3.S3 C2

从句：that  is near balanced in a continuous stream still shows warmup-dependent fixed-position restart bias.

- 从句类型：`relative_clause`
- 功能：`RESULT`（结果）
- claim：`measurement` / `medium`
- 证据：`None`（无）
- issue：`multi_claim_sentence;implication_without_evidence`
- 建议动作：`SPLIT_SENTENCE;ADD_EVIDENCE_ANCHOR`（SPLIT_SENTENCE；补证据锚点）

### INTRODUCTION.P3.S4 C1

从句：More importantly, small locked changes to the sample-RO physical implementation move restart behavior in both directions

- 从句类型：`main_clause`
- 功能：`BG`（背景）
- claim：`causal/generalization` / `low`
- 证据：`None`（无）
- issue：`risk_word`
- 建议动作：`REPLACE_RISK_VERB`（替换高风险动词/泛词）

### INTRODUCTION.P3.S4 C2

从句：:  a compact sampler configuration becomes biased when a restart-oriented sample-RO lock is imposed, and the baseline restart configuration is restored near balance when the compact sample-RO lock is imposed.

- 从句类型：`colon_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `low`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### INTRODUCTION.P5.S3 C2

从句：:  in these measured implementations, sampler-side physical implementation is not passive readout, and a measurement boundary

- 从句类型：`colon_clause`
- 功能：`SETUP`（实验/平台设置）
- claim：`method` / `low`
- 证据：`Experiment setup`（实验设置）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### INTRODUCTION.P5.S3 C3

从句：that  excludes it would miss a major observed source of restart-behavior variation under the evaluated protocol.

- 从句类型：`relative_clause`
- 功能：`RESULT`（结果）
- claim：`method` / `low`
- 证据：`None`（无）
- issue：`hidden_boundary;colon_sentence_split_check`
- 建议动作：`ADD_BOUNDARY;SPLIT_SENTENCE`（补边界条件；SPLIT_SENTENCE）

### INTRODUCTION.P6.S3 C1

从句：A bidirectional primary-board sampler-side counterfactual, with a three-run second-board repeat check, showing

- 从句类型：`main_clause`
- 功能：`BG`（背景）
- claim：`measurement` / `low`
- 证据：`None`（无）
- issue：`multi_claim_sentence`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### INTRODUCTION.P6.S3 C2

从句：that  a sampler-centered physical perturbation can move restart behavior toward biased outcomes and restore near-balanced behavior in the reverse direction.

- 从句类型：`relative_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `medium`
- 证据：`None`（无）
- issue：`multi_claim_sentence;implication_without_evidence`
- 建议动作：`SPLIT_SENTENCE;ADD_EVIDENCE_ANCHOR`（SPLIT_SENTENCE；补证据锚点）

### INTRODUCTION.P6.S4 C2

从句：that  constrains a simple persistent pairwise hard-locking explanation under the measured conditions.

- 从句类型：`relative_clause`
- 功能：`RESULT`（结果）
- claim：`measurement` / `low`
- 证据：`None`（无）
- issue：`hidden_boundary`
- 建议动作：`ADD_BOUNDARY`（补边界条件）

### BACKGROUND_AND_MEASUREMENT_GAP.P1.S2 C1

从句：Oscillator-based TRNG work also warns

- 从句类型：`main_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`multi_claim_sentence`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### BACKGROUND_AND_MEASUREMENT_GAP.P1.S2 C2

从句：that  test-passing streams can contain deterministic or pseudo-random structure unless the source model and sampling assumptions are examined carefully [Baudet_2011,Bochard_2010].

- 从句类型：`relative_clause`
- 功能：`BG`（背景）
- claim：`causal/generalization` / `medium`
- 证据：`Citation`（引用）
- issue：`multi_claim_sentence`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### BACKGROUND_AND_MEASUREMENT_GAP.P1.S4 C1

从句：Prior work further shows

- 从句类型：`main_clause`
- 功能：`RESULT`（结果）
- claim：`measurement` / `medium`
- 证据：`None`（无）
- issue：`multi_claim_sentence;implication_without_evidence`
- 建议动作：`SPLIT_SENTENCE;ADD_EVIDENCE_ANCHOR`（SPLIT_SENTENCE；补证据锚点）

### BACKGROUND_AND_MEASUREMENT_GAP.P1.S4 C2

从句：that  oscillator-based generators can be sensitive to implementation and environmental conditions, including security-relevant perturbations [Markettos_2009,Fischer_2008].

- 从句类型：`relative_clause`
- 功能：`BG`（背景）
- claim：`method` / `medium`
- 证据：`Citation`（引用）
- issue：`multi_claim_sentence`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### BACKGROUND_AND_MEASUREMENT_GAP.P2.S2 C1

从句：Compact multi-RO, RO-PUF/TRNG, and DCM/metastability designs report area, throughput, portability, and platform tradeoffs, and some explicitly evaluate place-and-route dependence as part of the hardware study [Nannipieri_2021,RojasMunoz_2022,Frustaci_2023].

- 从句类型：`main_clause`
- 功能：`SETUP`（实验/平台设置）
- claim：`method` / `low`
- 证据：`Citation;Experiment setup`（引用；实验设置）
- issue：`risk_word`
- 建议动作：`REPLACE_RISK_VERB`（替换高风险动词/泛词）

### BACKGROUND_AND_MEASUREMENT_GAP.P3.S4 C1

从句：If an evaluation records only final output statistics, it may miss

- 从句类型：`main_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `medium`
- 证据：`None`（无）
- issue：`multi_claim_sentence;implication_without_evidence`
- 建议动作：`SPLIT_SENTENCE;ADD_EVIDENCE_ANCHOR`（SPLIT_SENTENCE；补证据锚点）

### BACKGROUND_AND_MEASUREMENT_GAP.P3.S4 C2

从句：which  physical substructure shaped those statistics.

- 从句类型：`relative_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`multi_claim_sentence`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### BACKGROUND_AND_MEASUREMENT_GAP.P3.S5 C1

从句：Restart-style measurements sharpen the problem because they compare fixed positions across repeated starts and can expose startup-position effects

- 从句类型：`main_clause`
- 功能：`INTERPRETATION`（解释）
- claim：`measurement` / `medium`
- 证据：`Experiment setup`（实验设置）
- issue：`multi_claim_sentence`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### BACKGROUND_AND_MEASUREMENT_GAP.P3.S5 C2

从句：that  disappear in aggregate continuous streams [Turan_2018].

- 从句类型：`relative_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`multi_claim_sentence`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### BACKGROUND_AND_MEASUREMENT_GAP.P4.S2 C1

从句：FPGA {}s have a substantial instrumentation literature [Jian_Song_2006,Wu_2009,Wu_2012,Wang_2017], but raw bins are not automatically linear timing measurements.

- 从句类型：`main_clause`
- 功能：`SETUP`（实验/平台设置）
- claim：`measurement` / `low`
- 证据：`Citation;Experiment setup`（引用；实验设置）
- issue：`risk_word`
- 建议动作：`REPLACE_RISK_VERB`（替换高风险动词/泛词）

### BACKGROUND_AND_MEASUREMENT_GAP.P4.S3 C2

从句：:  they help test mechanism explanations, especially persistent pairwise hard locking, but they are not used as calibrated picosecond-level jitter metrology.

- 从句类型：`colon_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `low`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### BACKGROUND_AND_MEASUREMENT_GAP.P5.S2 C1

从句：Existing {} analysis can separate oscillator source, sampler, post-processing, and validation boundary for modeling or certification.

- 从句类型：`main_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `medium`
- 证据：`None`（无）
- issue：`implication_without_evidence`
- 建议动作：`ADD_EVIDENCE_ANCHOR`（补证据锚点）

### BACKGROUND_AND_MEASUREMENT_GAP.P5.S3 C1

从句：The measurements here show

- 从句类型：`main_clause`
- 功能：`RESULT`（结果）
- claim：`measurement` / `medium`
- 证据：`Experiment setup`（实验设置）
- issue：`multi_claim_sentence`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### BACKGROUND_AND_MEASUREMENT_GAP.P5.S3 C2

从句：that , for the evaluated implementations, treating the sampler side as passive readout is not a safe measurement abstraction.

- 从句类型：`relative_clause`
- 功能：`SETUP`（实验/平台设置）
- claim：`method` / `low`
- 证据：`Experiment setup`（实验设置）
- issue：`multi_claim_sentence`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P2.S1 C1

从句：Operationally, this paper uses ``measured entropy-source boundary'' to mean the set of physical and temporal implementation elements whose controlled or observed variation can materially change measured output behavior under the evaluated protocol.

- 从句类型：`main_clause`
- 功能：`METHOD`（方法）
- claim：`causal/generalization` / `medium`
- 证据：`None`（无）
- issue：`implication_without_evidence;hidden_boundary`
- 建议动作：`ADD_EVIDENCE_ANCHOR;ADD_BOUNDARY`（补证据锚点；补边界条件）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P2.S3 C1

从句：Figure fig

- 从句类型：`main_clause`
- 功能：`RESULT`（结果）
- claim：`descriptive` / `none`
- 证据：`Figure`（图）
- issue：`multi_claim_sentence`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P2.S3 C2

从句：: boundary shows the boundary used here.

- 从句类型：`colon_clause`
- 功能：`RESULT`（结果）
- claim：`measurement` / `medium`
- 证据：`None`（无）
- issue：`multi_claim_sentence;implication_without_evidence;colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE;ADD_EVIDENCE_ANCHOR`（SPLIT_SENTENCE；补证据锚点）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C2

从句：;  (sample) at (2.7,0.95) {9-stage\ RO}

- 从句类型：`appositive_or_coordinate_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C3

从句：;  (routes) at (2.7,-0.95) {sampler-side\ / placement}

- 从句类型：`appositive_or_coordinate_clause`
- 功能：`SETUP`（实验/平台设置）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C4

从句：;  (regs) at (5.2,0) {64 sampled\ vector}

- 从句类型：`appositive_or_coordinate_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C5

从句：;  (xor) at (7.6,0) {all64 XOR\ bit}

- 从句类型：`appositive_or_coordinate_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C6

从句：;  (restart) at (5.2,-1.35) {restart / warmup\ condition}

- 从句类型：`appositive_or_coordinate_clause`
- 功能：`BOUNDARY`（边界）
- claim：`limitation` / `none`
- 证据：`None`（无）
- issue：`hidden_boundary;colon_sentence_split_check`
- 建议动作：`ADD_BOUNDARY;SPLIT_SENTENCE`（补边界条件；SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C7

从句：;  (fifo) at (10.0,0.45) {FIFO / UART}

- 从句类型：`appositive_or_coordinate_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C8

从句：;  (host) at (12.2,0.45) {host capture}

- 从句类型：`appositive_or_coordinate_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C9

从句：;  (analysis) at (11.1,-1.05) {entropy / restart\ analysis}

- 从句类型：`appositive_or_coordinate_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C10

从句：;  (data) -- (regs)

- 从句类型：`parenthetical_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C11

从句：;  (sample) -- (regs)

- 从句类型：`parenthetical_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C12

从句：;  (routes) -- (regs)

- 从句类型：`parenthetical_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C13

从句：;  (restart) -- (regs)

- 从句类型：`parenthetical_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C14

从句：;  (regs) -- (xor)

- 从句类型：`parenthetical_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C15

从句：;  (xor) -- (fifo)

- 从句类型：`parenthetical_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C16

从句：;  (fifo) -- (host)

- 从句类型：`parenthetical_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C17

从句：;  (host) -- (analysis)

- 从句类型：`parenthetical_clause`
- 功能：`BG`（背景）
- claim：`descriptive` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C18

从句：: measured entropy-source boundary}] {}

- 从句类型：`colon_clause`
- 功能：`RESULT`（结果）
- claim：`measurement` / `none`
- 证据：`None`（无）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P3.S1 C19

从句：: measurement/readout chain}] {}

- 从句类型：`colon_clause`
- 功能：`SETUP`（实验/平台设置）
- claim：`measurement` / `none`
- 证据：`Experiment setup`（实验设置）
- issue：`colon_sentence_split_check`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）
