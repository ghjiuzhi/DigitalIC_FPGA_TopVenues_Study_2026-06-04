# 深度形态学对齐报告

这个报告按句子级审计当前稿件。它只指出位置、功能、风险和修订动作，不直接改写原稿。

## 总览

- 逐句记录：292 条。
- 存在 mismatch 或上下句跳跃的句子：110 条。

## 优先检查的句子记录

### ABS.S2

原句：This paper reports a two-board Zynq-7020 {} case study showing that this boundary can be insufficient: sampler-side physical implementation can substantially reshape measured restart behavior.

- 主功能：`GAP`（缺口）
- 顶刊期望角色：`PROBLEM`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`method`（方法 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=3; colon_count=1`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### ABS.S3

原句：Continuous-stream placement measurements on the primary board expose a large implementation dependence, from a biased placement with $p_1=0.337316$ and bit min-entropy 0.593606 to a near-balanced placement with $p_1=0.499969$ and bit min-entropy 0.999909.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`GAP`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`method`（方法 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`large`
- 标点模式：`hyphen_count=4; comma_count=1`
- 问题类型：`risk_word`
- 建议动作：`REPLACE_RISK_VERB`（替换高风险动词/泛词）

### ABS.S7

原句：Pairwise and exact counterfactual {} diagnostics show small phase correlations under the applied screens.

- 主功能：`RESULT`（结果）
- 顶刊期望角色：`BOUNDARY`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`small`
- 标点模式：`OK`
- 问题类型：`risk_word`
- 建议动作：`REPLACE_RISK_VERB`（替换高风险动词/泛词）

### ABS.S8

原句：Reduced-XOR, held-out sampler, warmup/aperture, and toolflow controls show that final all64 output can hide biased internal sampler-vector directions: on the second board, moving the sample RO to a held-out physical context changes warmup-10 all64 from $p_1=0.360614$ to 0.500718 while internal contributors remain biased and reorder, and a 12-capture original-vs-Explore matrix separates route-stable bias preservation from route-moving boundary cases.

- 主功能：`GAP`（缺口）
- 顶刊期望角色：`BOUNDARY`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`causal/generalization`（因果/泛化 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=10; colon_count=1; slash_count=1; comma_count=5`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### INTRODUCTION.P1.S3

原句：Placement, routing, clocking, reset sequencing, sampling, and readout can all affect the final bitstream.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`causal/generalization`（因果/泛化 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`comma_count=5`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### INTRODUCTION.P1.S5

原句：It is also where the physical entropy-source boundary should be drawn.

- 主功能：`BG`（背景）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=1`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### INTRODUCTION.P3.S2

原句：That abstraction is useful for design, but it can fail as a measurement boundary.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`method`（方法 claim） / `medium`（中）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`comma_count=1`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### INTRODUCTION.P3.S3

原句：In the measurements reported here, a placement that is near balanced in a continuous stream still shows warmup-dependent fixed-position restart bias.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `medium`（中）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`hyphen_count=2; comma_count=1`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### INTRODUCTION.P3.S4

原句：More importantly, small locked changes to the sample-RO physical implementation move restart behavior in both directions: a compact sampler configuration becomes biased when a restart-oriented sample-RO lock is imposed, and the baseline restart configuration is restored near balance when the compact sample-RO lock is imposed.

- 主功能：`BG`（背景）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`causal/generalization`（因果/泛化 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`small`
- 标点模式：`hyphen_count=4; colon_count=1; comma_count=2`
- 问题类型：`risk_word`
- 建议动作：`REPLACE_RISK_VERB`（替换高风险动词/泛词）

### INTRODUCTION.P4.S1

原句：{quote} When an FPGA {} is evaluated from hardware measurements, must the sampler-side physical implementation be included in the measured entropy-source boundary? {quote}

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`none`（无上一句）
- claim 类型/强度：`method`（方法 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`hyphen_count=2; question_mark_count=1; comma_count=1`
- 问题类型：`punctuation_issue`
- 建议动作：`CHANGE_PUNCTUATION`（调整标点）

### INTRODUCTION.P5.S2

原句：The claim is not that all FPGA {}s behave identically, nor that the present evidence is a complete {} validation package.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`method`（方法 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`comma_count=1`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### INTRODUCTION.P6.S4

原句：A {}-assisted diagnostic layer that constrains a simple persistent pairwise hard-locking explanation under the measured conditions.

- 主功能：`RESULT`（结果）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=2`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### INTRODUCTION.P6.S5

原句：A reduced-XOR counterfactual analysis showing same-data-RO direction anisotropy, warmup-dependent complement cancellation, line-direction controls, second-board original and held-out sampler mechanism checks, and a minimal toolflow/directive sensitivity matrix. {enumerate}

- 主功能：`BG`（背景）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`comparative`（比较 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=7; slash_count=1; comma_count=4`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### INTRODUCTION.P7.S2

原句：Section II summarizes related work and the measurement gap.

- 主功能：`GAP`（缺口）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`OK`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### INTRODUCTION.P7.S5

原句：Sections V--IX present continuous-stream placement, restart, sampler-side counterfactual, {}, and reduced-XOR evidence.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`comparative`（比较 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=4; comma_count=4`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### INTRODUCTION.P7.S6

原句：Section X discusses the entropy-source boundary, Section XI lists limitations and future measurements, and Section XII concludes.

- 主功能：`BOUNDARY`（边界）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=2`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### BACKGROUND_AND_MEASUREMENT_GAP.P1.S3

原句：Evaluation may include output statistics, entropy estimates, restart behavior, health-test boundaries, and conditioning documentation [Turan_2018,Lubicz_2015,Lubicz_2024].

- 主功能：`BG`（背景）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`limitation`（限制/边界 claim） / `medium`（中）
- 证据锚点：`Citation`（引用）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=6`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### BACKGROUND_AND_MEASUREMENT_GAP.P1.S4

原句：Prior work further shows that oscillator-based generators can be sensitive to implementation and environmental conditions, including security-relevant perturbations [Markettos_2009,Fischer_2008].

- 主功能：`RESULT`（结果）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`method`（方法 claim） / `medium`（中）
- 证据锚点：`Citation`（引用）
- 风险词：`无`
- 标点模式：`hyphen_count=2; comma_count=2`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### BACKGROUND_AND_MEASUREMENT_GAP.P2.S2

原句：Compact multi-RO, RO-PUF/TRNG, and DCM/metastability designs report area, throughput, portability, and platform tradeoffs, and some explicitly evaluate place-and-route dependence as part of the hardware study [Nannipieri_2021,RojasMunoz_2022,Frustaci_2023].

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`method`（方法 claim） / `low`（低）
- 证据锚点：`Citation;Experiment setup`（引用；实验设置）
- 风险词：`some`
- 标点模式：`hyphen_count=4; slash_count=2; comma_count=8`
- 问题类型：`risk_word`
- 建议动作：`REPLACE_RISK_VERB`（替换高风险动词/泛词）

### BACKGROUND_AND_MEASUREMENT_GAP.P2.S3

原句：These works motivate careful reporting of FPGA implementation details, but they do not replace a project-specific boundary diagnosis for the particular sampler, restart protocol, and routed implementation studied here.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`method`（方法 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=3`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### BACKGROUND_AND_MEASUREMENT_GAP.P3.S2

原句：They do not, by themselves, close the implementation-level measurement gap addressed here.

- 主功能：`GAP`（缺口）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`method`（方法 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=2`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### BACKGROUND_AND_MEASUREMENT_GAP.P3.S5

原句：Restart-style measurements sharpen the problem because they compare fixed positions across repeated starts and can expose startup-position effects that disappear in aggregate continuous streams [Turan_2018].

- 主功能：`INTERPRETATION`（解释）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `medium`（中）
- 证据锚点：`Citation;Experiment setup`（引用；实验设置）
- 风险词：`无`
- 标点模式：`hyphen_count=2`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### BACKGROUND_AND_MEASUREMENT_GAP.P4.S2

原句：FPGA {}s have a substantial instrumentation literature [Jian_Song_2006,Wu_2009,Wu_2012,Wang_2017], but raw bins are not automatically linear timing measurements.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`measurement`（测量/结果 claim） / `low`（低）
- 证据锚点：`Citation;Experiment setup`（引用；实验设置）
- 风险词：`substantial`
- 标点模式：`comma_count=4`
- 问题类型：`risk_word`
- 建议动作：`REPLACE_RISK_VERB`（替换高风险动词/泛词）

### BACKGROUND_AND_MEASUREMENT_GAP.P4.S3

原句：In this work, {} data are used conservatively: they help test mechanism explanations, especially persistent pairwise hard locking, but they are not used as calibrated picosecond-level jitter metrology.

- 主功能：`BG`（背景）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=1; colon_count=1; comma_count=3`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P1.S2

原句：The core entropy RTL contains eight data ROs, a nine-stage sample RO, sampled-data registers, and a final XOR reduction.

- 主功能：`BG`（背景）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=2; comma_count=3`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P2.S4

原句：It includes the data ROs, sample RO, sampled-data registers, sampler-side routing and local implementation, and the restart/warmup/reset timing that directly affects when early samples are taken.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`causal/generalization`（因果/泛化 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=2; slash_count=2; comma_count=4`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P2.S5

原句：FIFO buffering after entropy-bit formation, UART readout, host capture, and offline analysis are outside the entropy source, but they are part of the measurement chain and must be documented for reproducibility.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=4`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P3.S2

原句：It is not used as a complete {} validation.

- 主功能：`BG`（背景）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`OK`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P3.S3

原句：The 1000-row restart body follows the restart input shape used by the local {ea\_restart} flow, not an argument that 1000 rows alone is sufficient for certification.

- 主功能：`BG`（背景）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=1`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### EXPERIMENTAL_SETUP_AND_ANALYSIS_RULES.P4.S4

原句：Table tab:warmup reports the cutoff, maximum count, and resulting diagnostic outcome to keep the table compact; the diagnostic still inspects many fixed positions jointly and is not a collection of independent single-position claims.

- 主功能：`RESULT`（结果）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`evidences`（用证据承接上一句）
- claim 类型/强度：`measurement`（测量/结果 claim） / `low`（低）
- 证据锚点：`Table`（表）
- 风险词：`many`
- 标点模式：`hyphen_count=1; semicolon_count=1; colon_count=1; comma_count=2`
- 问题类型：`risk_word`
- 建议动作：`REPLACE_RISK_VERB`（替换高风险动词/泛词）

### PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P1.S2

原句：The contrast between {} and {} is the simplest entry point.

- 主功能：`BG`（背景）
- 顶刊期望角色：`QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`OK`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P1.S3

原句：In the 10 MiB rows, {} has $p_1=0.337316$, absolute bias 0.162684, and bit min-entropy 0.593606.

- 主功能：`BG`（背景）
- 顶刊期望角色：`QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=3`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P2.S2

原句：The same-column placement is near balanced by $p_1$ and bit min-entropy, but its adjacent-equal ratio differs from the strongest placements.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=3; comma_count=1`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P2.S3

原句：This motivates the restart and mechanism measurements: a single continuous-stream statistic cannot define the physical entropy-source boundary.

- 主功能：`NEED`（必要性）
- 顶刊期望角色：`QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`hyphen_count=2; colon_count=1`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### PLACEMENT_SENSITIVE_CONTINUOUS_STREAM_CHARACTERIZATION.P4.S2

原句：The summarized measurements report a maximum 10 MiB/repeat bit-min-entropy mean delta of 0.00841786 among paired placement rows.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`hyphen_count=2; slash_count=1`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）

### RESTART_AND_WARMUP_CHARACTERIZATION.P4.S3

原句：Repeated warmup scans place the observed transition at $10 < {WARMUP\_BYTES} 11$, with warmup 11 still a boundary observation rather than a large-margin engineering rule.

- 主功能：`RESULT`（结果）
- 顶刊期望角色：`QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`measurement`（测量/结果 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`large`
- 标点模式：`hyphen_count=1; comma_count=1`
- 问题类型：`risk_word`
- 建议动作：`REPLACE_RISK_VERB`（替换高风险动词/泛词）

### RESTART_AND_WARMUP_CHARACTERIZATION.P6.S3

原句：The repeated warmup-10 flagged outcomes and warmup-11 no-flag outcomes support a narrow measured transition, but they should not be generalized as a universal warmup threshold across boards, placements, PVT conditions, or tool runs.

- 主功能：`RESULT`（结果）
- 顶刊期望角色：`QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `very_high`（很高）
- 证据锚点：`None`（无）
- 风险词：`universal`
- 标点模式：`hyphen_count=3; comma_count=4`
- 问题类型：`unsupported_claim;overstrong_claim;risk_word`
- 建议动作：`ADD_EVIDENCE_ANCHOR;WEAKEN_CLAIM;REPLACE_RISK_VERB`（补证据锚点；削弱 claim；替换高风险动词/泛词）

### SAMPLER_SIDE_COUNTERFACTUALS.P4.S2

原句：Each row summarizes three 1000-row restart artifacts on the same second board; these are capture repeats under the listed condition, not additional boards or PVT points.} tab:board2counter {tabular}{llrrrrrl} Condition & Warmup & $n$ & Mean $p_1$ & Std. $p_1$ & Min.

- 主功能：`BOUNDARY`（边界）
- 顶刊期望角色：`QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`limitation`（限制/边界 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=1; semicolon_count=1; colon_count=1; comma_count=1`
- 问题类型：`none`
- 建议动作：`ADD_BOUNDARY`（补边界条件）

### SAMPLER_SIDE_COUNTERFACTUALS.P4.S3

原句：Min-H & Max worst $x$ & Reading \\ {} compact baseline & 4 & 3 & 0.494077 & 0.000501 & 0.981366 & 556 & compact reference \\ {} compact baseline & 5 & 3 & 0.522394 & 0.001229 & 0.933152 & 576 & compact reference, high-side \\ {} compact baseline & 11 & 3 & 0.490700 & 0.000272 & 0.972532 & 562 & compact reference \\ {} forward lock & 4 & 3 & 0.450792 & 0.001106 & 0.861432 & 719 & repeated biased shift \\ {} forward lock & 5 & 3 & 0.445222 & 0.000603 & 0.848214 & 666 & repeated biased shift \\ {} forward lock & 11 & 3 & 0.411363 & 0.000294 & 0.763719 & 663 & stronger biased shift \\ {} reverse lock & 4 & 3 & 0.498300 & 0.000544 & 0.993649 & 573 & reverse near balance \\ {tabular} {table*}

- 主功能：`RESULT`（结果）
- 顶刊期望角色：`QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- 和上一句关系：`evidences`（用证据承接上一句）
- claim 类型/强度：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`high`
- 标点模式：`hyphen_count=2; comma_count=1`
- 问题类型：`risk_word`
- 建议动作：`REPLACE_RISK_VERB`（替换高风险动词/泛词）

### SAMPLER_SIDE_COUNTERFACTUALS.P6.S3

原句：At warmup 4, changing from the compact {} reference to the forward {} lock moves the mean $p_1$ from 0.494077 to 0.450792 and raises the maximum worst fixed-position count from 556 to 719.

- 主功能：`BG`（背景）
- 顶刊期望角色：`QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=1`
- 问题类型：`none`
- 建议动作：`KEEP`（保留）
