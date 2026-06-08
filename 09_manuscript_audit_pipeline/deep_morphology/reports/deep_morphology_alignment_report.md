# 深度形态学对齐报告

这个报告按句子级审计当前稿件。它只指出位置、功能、风险和修订动作，不直接改写原稿。

## 总览

- 逐句记录：292 条。
- 存在 mismatch 或上下句跳跃的句子：208 条。

## 优先检查的句子记录

### ABS.S1

原句：FPGA ring-oscillator true random number generators are commonly evaluated from oscillator-array structure and final output statistics.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`BG`
- 和上一句关系：`none`（无上一句）
- claim 类型/强度：`method`（方法 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=2`
- 问题类型：`role_mismatch`
- 建议动作：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（REFUNCTION_SENTENCE；REORDER_SENTENCE）

### ABS.S2

原句：This paper reports a two-board Zynq-7020 {} case study showing that this boundary can be insufficient: sampler-side physical implementation can substantially reshape measured restart behavior.

- 主功能：`GAP`（缺口）
- 顶刊期望角色：`PROBLEM`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`method`（方法 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=3; colon_count=1`
- 问题类型：`sentence_jump;unsupported_claim;role_mismatch`
- 建议动作：`ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;REFUNCTION_SENTENCE;REORDER_SENTENCE`（ADD_BRIDGE；补证据锚点；REFUNCTION_SENTENCE；REORDER_SENTENCE）

### ABS.S3

原句：Continuous-stream placement measurements on the primary board expose a large implementation dependence, from a biased placement with $p_1=0.337316$ and bit min-entropy 0.593606 to a near-balanced placement with $p_1=0.499969$ and bit min-entropy 0.999909.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`GAP`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`method`（方法 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`large`
- 标点模式：`hyphen_count=4; comma_count=1`
- 问题类型：`risk_word;role_mismatch`
- 建议动作：`REPLACE_RISK_VERB;REFUNCTION_SENTENCE;REORDER_SENTENCE`（替换高风险动词/泛词；REFUNCTION_SENTENCE；REORDER_SENTENCE）

### ABS.S4

原句：Restart measurements then show that continuous-stream balance is not enough: warmup bytes 8 and 10 trigger fixed-position diagnostic flags, while warmup bytes 11, 12, and 16 do not.

- 主功能：`RESULT`（结果）
- 顶刊期望角色：`METHOD`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`measurement`（测量/结果 claim） / `medium`（中）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`hyphen_count=2; colon_count=1; comma_count=3`
- 问题类型：`role_mismatch`
- 建议动作：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（REFUNCTION_SENTENCE；REORDER_SENTENCE）

### ABS.S5

原句：The central evidence is a bidirectional sampler-side counterfactual on the primary board, plus a repeated second-board check: imposing the restart-oriented sample-RO lock changes a compact sampler configuration toward biased restart behavior on both boards, with board-specific magnitudes.

- 主功能：`BG`（背景）
- 顶刊期望角色：`SETUP`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`causal/generalization`（因果/泛化 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=5; colon_count=1; comma_count=2`
- 问题类型：`role_mismatch`
- 建议动作：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（REFUNCTION_SENTENCE；REORDER_SENTENCE）

### ABS.S6

原句：On the second board, three-run forward warmup-4 and warmup-5 means are $p_1=0.450792$ and 0.445222, while the reverse compact-lock warmup-4 mean is 0.498300.

- 主功能：`BG`（背景）
- 顶刊期望角色：`RESULT`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=5; comma_count=2`
- 问题类型：`role_mismatch`
- 建议动作：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（REFUNCTION_SENTENCE；REORDER_SENTENCE）

### ABS.S7

原句：Pairwise and exact counterfactual {} diagnostics show small phase correlations under the applied screens.

- 主功能：`RESULT`（结果）
- 顶刊期望角色：`BOUNDARY`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`small`
- 标点模式：`OK`
- 问题类型：`sentence_jump;unsupported_claim;risk_word;role_mismatch`
- 建议动作：`ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;REPLACE_RISK_VERB;REFUNCTION_SENTENCE;REORDER_SENTENCE`（ADD_BRIDGE；补证据锚点；替换高风险动词/泛词；REFUNCTION_SENTENCE；REORDER_SENTENCE）

### ABS.S8

原句：Reduced-XOR, held-out sampler, warmup/aperture, and toolflow controls show that final all64 output can hide biased internal sampler-vector directions: on the second board, moving the sample RO to a held-out physical context changes warmup-10 all64 from $p_1=0.360614$ to 0.500718 while internal contributors remain biased and reorder, and a 12-capture original-vs-Explore matrix separates route-stable bias preservation from route-moving boundary cases.

- 主功能：`GAP`（缺口）
- 顶刊期望角色：`BOUNDARY`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`causal/generalization`（因果/泛化 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=10; colon_count=1; slash_count=1; comma_count=5`
- 问题类型：`sentence_jump;unsupported_claim;punctuation_issue;role_mismatch`
- 建议动作：`ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;SPLIT_SENTENCE;REFUNCTION_SENTENCE;REORDER_SENTENCE`（ADD_BRIDGE；补证据锚点；SPLIT_SENTENCE；REFUNCTION_SENTENCE；REORDER_SENTENCE）

### ABS.S9

原句：These measurements support a diagnostic claim rather than a certification claim: sampler-side physical implementation is not passive readout in the evaluated implementations and should be included in the measured entropy-source boundary.

- 主功能：`RESULT`（结果）
- 顶刊期望角色：`BOUNDARY`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`method`（方法 claim） / `medium`（中）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`hyphen_count=2; colon_count=1`
- 问题类型：`role_mismatch`
- 建议动作：`REFUNCTION_SENTENCE;REORDER_SENTENCE`（REFUNCTION_SENTENCE；REORDER_SENTENCE）

### INTRODUCTION.P1.S3

原句：Placement, routing, clocking, reset sequencing, sampling, and readout can all affect the final bitstream.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`causal/generalization`（因果/泛化 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`comma_count=5`
- 问题类型：`sentence_jump;unsupported_claim;punctuation_issue`
- 建议动作：`ADD_BRIDGE;ADD_EVIDENCE_ANCHOR;SPLIT_SENTENCE`（ADD_BRIDGE；补证据锚点；SPLIT_SENTENCE）

### INTRODUCTION.P1.S5

原句：It is also where the physical entropy-source boundary should be drawn.

- 主功能：`BG`（背景）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=1`
- 问题类型：`sentence_jump`
- 建议动作：`ADD_BRIDGE`（ADD_BRIDGE）

### INTRODUCTION.P3.S2

原句：That abstraction is useful for design, but it can fail as a measurement boundary.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`method`（方法 claim） / `medium`（中）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`comma_count=1`
- 问题类型：`sentence_jump`
- 建议动作：`ADD_BRIDGE`（ADD_BRIDGE）

### INTRODUCTION.P3.S3

原句：In the measurements reported here, a placement that is near balanced in a continuous stream still shows warmup-dependent fixed-position restart bias.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `medium`（中）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`hyphen_count=2; comma_count=1`
- 问题类型：`sentence_jump`
- 建议动作：`ADD_BRIDGE`（ADD_BRIDGE）

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
- 问题类型：`sentence_jump`
- 建议动作：`ADD_BRIDGE`（ADD_BRIDGE）

### INTRODUCTION.P6.S3

原句：A bidirectional primary-board sampler-side counterfactual, with a three-run second-board repeat check, showing that a sampler-centered physical perturbation can move restart behavior toward biased outcomes and restore near-balanced behavior in the reverse direction.

- 主功能：`BG`（背景）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`measurement`（测量/结果 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=6; comma_count=2`
- 问题类型：`unsupported_claim`
- 建议动作：`ADD_EVIDENCE_ANCHOR`（补证据锚点）

### INTRODUCTION.P6.S4

原句：A {}-assisted diagnostic layer that constrains a simple persistent pairwise hard-locking explanation under the measured conditions.

- 主功能：`RESULT`（结果）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=2`
- 问题类型：`sentence_jump`
- 建议动作：`ADD_BRIDGE`（ADD_BRIDGE）

### INTRODUCTION.P6.S5

原句：A reduced-XOR counterfactual analysis showing same-data-RO direction anisotropy, warmup-dependent complement cancellation, line-direction controls, second-board original and held-out sampler mechanism checks, and a minimal toolflow/directive sensitivity matrix. {enumerate}

- 主功能：`BG`（背景）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`comparative`（比较 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=7; slash_count=1; comma_count=4`
- 问题类型：`sentence_jump;punctuation_issue`
- 建议动作：`ADD_BRIDGE;SPLIT_SENTENCE`（ADD_BRIDGE；SPLIT_SENTENCE）

### INTRODUCTION.P7.S2

原句：Section II summarizes related work and the measurement gap.

- 主功能：`GAP`（缺口）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`OK`
- 问题类型：`sentence_jump`
- 建议动作：`ADD_BRIDGE`（ADD_BRIDGE）

### INTRODUCTION.P7.S5

原句：Sections V--IX present continuous-stream placement, restart, sampler-side counterfactual, {}, and reduced-XOR evidence.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`comparative`（比较 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=4; comma_count=4`
- 问题类型：`sentence_jump;punctuation_issue`
- 建议动作：`ADD_BRIDGE;SPLIT_SENTENCE`（ADD_BRIDGE；SPLIT_SENTENCE）

### INTRODUCTION.P7.S6

原句：Section X discusses the entropy-source boundary, Section XI lists limitations and future measurements, and Section XII concludes.

- 主功能：`BOUNDARY`（边界）
- 顶刊期望角色：`BG/PROBLEM/GAP/METHOD/CONTRIBUTION`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=2`
- 问题类型：`sentence_jump`
- 建议动作：`ADD_BRIDGE`（ADD_BRIDGE）

### BACKGROUND_AND_MEASUREMENT_GAP.P1.S1

原句：FPGA {}s use oscillator-derived timing uncertainty, sampling logic, and combining or conditioning logic to generate random bits [Sunar_2007,Fischer_2008,Wold_2009,Bochard_2009].

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`none`（无上一句）
- claim 类型/强度：`limitation`（限制/边界 claim） / `low`（低）
- 证据锚点：`Citation`（引用）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=5`
- 问题类型：`punctuation_issue`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### BACKGROUND_AND_MEASUREMENT_GAP.P1.S3

原句：Evaluation may include output statistics, entropy estimates, restart behavior, health-test boundaries, and conditioning documentation [Turan_2018,Lubicz_2015,Lubicz_2024].

- 主功能：`BG`（背景）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`limitation`（限制/边界 claim） / `medium`（中）
- 证据锚点：`Citation`（引用）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=6`
- 问题类型：`sentence_jump;punctuation_issue`
- 建议动作：`ADD_BRIDGE;SPLIT_SENTENCE`（ADD_BRIDGE；SPLIT_SENTENCE）

### BACKGROUND_AND_MEASUREMENT_GAP.P1.S4

原句：Prior work further shows that oscillator-based generators can be sensitive to implementation and environmental conditions, including security-relevant perturbations [Markettos_2009,Fischer_2008].

- 主功能：`RESULT`（结果）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`method`（方法 claim） / `medium`（中）
- 证据锚点：`Citation`（引用）
- 风险词：`无`
- 标点模式：`hyphen_count=2; comma_count=2`
- 问题类型：`sentence_jump`
- 建议动作：`ADD_BRIDGE`（ADD_BRIDGE）

### BACKGROUND_AND_MEASUREMENT_GAP.P2.S2

原句：Compact multi-RO, RO-PUF/TRNG, and DCM/metastability designs report area, throughput, portability, and platform tradeoffs, and some explicitly evaluate place-and-route dependence as part of the hardware study [Nannipieri_2021,RojasMunoz_2022,Frustaci_2023].

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`method`（方法 claim） / `low`（低）
- 证据锚点：`Citation;Experiment setup`（引用；实验设置）
- 风险词：`some`
- 标点模式：`hyphen_count=4; slash_count=2; comma_count=8`
- 问题类型：`sentence_jump;risk_word;punctuation_issue`
- 建议动作：`ADD_BRIDGE;REPLACE_RISK_VERB;SPLIT_SENTENCE`（ADD_BRIDGE；替换高风险动词/泛词；SPLIT_SENTENCE）

### BACKGROUND_AND_MEASUREMENT_GAP.P2.S3

原句：These works motivate careful reporting of FPGA implementation details, but they do not replace a project-specific boundary diagnosis for the particular sampler, restart protocol, and routed implementation studied here.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`method`（方法 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=3`
- 问题类型：`sentence_jump`
- 建议动作：`ADD_BRIDGE`（ADD_BRIDGE）

### BACKGROUND_AND_MEASUREMENT_GAP.P3.S1

原句：These foundations cover RO construction, statistical assessment, standards-oriented entropy-source evaluation, active perturbation, and TDC instrumentation.

- 主功能：`BG`（背景）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`none`（无上一句）
- claim 类型/强度：`method`（方法 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=2; comma_count=4`
- 问题类型：`punctuation_issue`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### BACKGROUND_AND_MEASUREMENT_GAP.P3.S2

原句：They do not, by themselves, close the implementation-level measurement gap addressed here.

- 主功能：`GAP`（缺口）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`method`（方法 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=2`
- 问题类型：`sentence_jump`
- 建议动作：`ADD_BRIDGE`（ADD_BRIDGE）

### BACKGROUND_AND_MEASUREMENT_GAP.P3.S3

原句：A final bitstream is not merely an abstract RTL object; it is a routed physical implementation with local interconnect, resource placement, control logic, and measurement readout.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`method`（方法 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`semicolon_count=1; comma_count=3`
- 问题类型：`punctuation_issue`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### BACKGROUND_AND_MEASUREMENT_GAP.P3.S4

原句：If an evaluation records only final output statistics, it may miss which physical substructure shaped those statistics.

- 主功能：`BG`（背景）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`descriptive`（描述性 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`comma_count=1`
- 问题类型：`unsupported_claim`
- 建议动作：`ADD_EVIDENCE_ANCHOR`（补证据锚点）

### BACKGROUND_AND_MEASUREMENT_GAP.P3.S5

原句：Restart-style measurements sharpen the problem because they compare fixed positions across repeated starts and can expose startup-position effects that disappear in aggregate continuous streams [Turan_2018].

- 主功能：`INTERPRETATION`（解释）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`measurement`（测量/结果 claim） / `medium`（中）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`hyphen_count=2`
- 问题类型：`sentence_jump`
- 建议动作：`ADD_BRIDGE`（ADD_BRIDGE）

### BACKGROUND_AND_MEASUREMENT_GAP.P4.S2

原句：FPGA {}s have a substantial instrumentation literature [Jian_Song_2006,Wu_2009,Wu_2012,Wang_2017], but raw bins are not automatically linear timing measurements.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`measurement`（测量/结果 claim） / `low`（低）
- 证据锚点：`Citation;Experiment setup`（引用；实验设置）
- 风险词：`substantial`
- 标点模式：`comma_count=4`
- 问题类型：`risk_word;punctuation_issue`
- 建议动作：`REPLACE_RISK_VERB;SPLIT_SENTENCE`（替换高风险动词/泛词；SPLIT_SENTENCE）

### BACKGROUND_AND_MEASUREMENT_GAP.P4.S3

原句：In this work, {} data are used conservatively: they help test mechanism explanations, especially persistent pairwise hard locking, but they are not used as calibrated picosecond-level jitter metrology.

- 主功能：`BG`（背景）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=1; colon_count=1; comma_count=3`
- 问题类型：`sentence_jump`
- 建议动作：`ADD_BRIDGE`（ADD_BRIDGE）

### BACKGROUND_AND_MEASUREMENT_GAP.P5.S2

原句：Existing {} analysis can separate oscillator source, sampler, post-processing, and validation boundary for modeling or certification.

- 主功能：`BG`（背景）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`descriptive`（描述性 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=3`
- 问题类型：`unsupported_claim`
- 建议动作：`ADD_EVIDENCE_ANCHOR`（补证据锚点）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P1.S2

原句：The core entropy RTL contains eight data ROs, a nine-stage sample RO, sampled-data registers, and a final XOR reduction.

- 主功能：`BG`（背景）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`descriptive`（描述性 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=2; comma_count=3`
- 问题类型：`sentence_jump`
- 建议动作：`ADD_BRIDGE`（ADD_BRIDGE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P1.S3

原句：With the evaluated parameters, the sampled-data vector has 64 bits, formed from eight data ROs sampled across eight sample-RO phases; the final output bit is the XOR reduction of that vector.

- 主功能：`BG`（背景）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`method`（方法 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=2; semicolon_count=1; comma_count=2`
- 问题类型：`punctuation_issue`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P2.S1

原句：Operationally, this paper uses ``measured entropy-source boundary'' to mean the set of physical and temporal implementation elements whose controlled or observed variation can materially change measured output behavior under the evaluated protocol.

- 主功能：`METHOD`（方法）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`none`（无上一句）
- claim 类型/强度：`causal/generalization`（因果/泛化 claim） / `medium`（中）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=1; comma_count=1`
- 问题类型：`unsupported_claim`
- 建议动作：`ADD_EVIDENCE_ANCHOR`（补证据锚点）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P2.S2

原句：Under that definition, the boundary is not a certification boundary; it is the boundary needed to interpret the hardware measurements.

- 主功能：`BOUNDARY`（边界）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`elaborates`（展开上一句）
- claim 类型/强度：`measurement`（测量/结果 claim） / `low`（低）
- 证据锚点：`Experiment setup`（实验设置）
- 风险词：`无`
- 标点模式：`semicolon_count=1; comma_count=1`
- 问题类型：`punctuation_issue`
- 建议动作：`SPLIT_SENTENCE`（SPLIT_SENTENCE）

### DESIGN_AND_MEASUREMENT_WORKFLOW.P2.S4

原句：It includes the data ROs, sample RO, sampled-data registers, sampler-side routing and local implementation, and the restart/warmup/reset timing that directly affects when early samples are taken.

- 主功能：`SETUP`（实验/平台设置）
- 顶刊期望角色：`SECTION_SPECIFIC`
- 和上一句关系：`jumps`（跳跃，缺少桥接）
- claim 类型/强度：`causal/generalization`（因果/泛化 claim） / `low`（低）
- 证据锚点：`None`（无）
- 风险词：`无`
- 标点模式：`hyphen_count=2; slash_count=2; comma_count=4`
- 问题类型：`sentence_jump;punctuation_issue`
- 建议动作：`ADD_BRIDGE;SPLIT_SENTENCE`（ADD_BRIDGE；SPLIT_SENTENCE）
