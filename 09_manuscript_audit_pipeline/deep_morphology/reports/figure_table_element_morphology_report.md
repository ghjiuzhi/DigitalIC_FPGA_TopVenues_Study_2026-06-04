# 图表元素级形态报告

这个报告检查图表是否承担清楚的论文叙事功能：caption 是否有对象/条件/结论/备注，正文是否先引用再解释，caption 和正文 claim 是否一致。

## 总览

- 图表记录：9 个。
- 缺少正文 first mention：0 个。
- caption/body 需要核对：1 个。

## 图表逐项审计

### figure `fig:boundary`

caption：Operational measured boundary used in this paper. The sampler side, local physical implementation, and restart/warmup/reset timing that directly affects sampling are inside the evaluated entropy-source boundary; post-XOR FIFO buffering, UART, host capture, and offline analysis are measurement/readout elements.

- caption 功能序列：`OBJECT -> TAKEAWAY`
- 角色：`architecture`
- first mention：`ABS.S2`
- 正文是否解释看什么：`no`
- 正文是否给定量：`yes`
- caption/body 一致性：`consistent`
- 表格 note 需求：`no`
- 单位/缩写问题：`none`

### figure `fig:workflow`

caption：Evidence workflow. The sampler-side counterfactual is the central boundary test; the other measurements establish context, constrain mechanisms, and explain how final-output statistics can hide internal structure.

- caption 功能序列：`OBJECT`
- 角色：`workflow`
- first mention：`INTRODUCTION.P7.S3`
- 正文是否解释看什么：`no`
- 正文是否给定量：`no`
- caption/body 一致性：`consistent`
- 表格 note 需求：`no`
- 单位/缩写问题：`none`

### table `tab:setup`

caption：Experimental platform and capture configuration.

- caption 功能序列：`OBJECT -> CONDITION`
- 角色：`setup`
- first mention：`DESIGN_AND_MEASUREMENT_WORKFLOW.P1.S1`
- 正文是否解释看什么：`no`
- 正文是否给定量：`yes`
- caption/body 一致性：`consistent`
- 表格 note 需求：`no`
- 单位/缩写问题：`none`

### table `tab:sp800summary`

caption：Selected non-IID entropy-assessment summaries.

- caption 功能序列：`OBJECT -> TAKEAWAY`
- 角色：`comparison`
- first mention：`RESTART_AND_WARMUP_CHARACTERIZATION.P2.S1`
- 正文是否解释看什么：`yes`
- 正文是否给定量：`yes`
- caption/body 一致性：`consistent`
- 表格 note 需求：`no`
- 单位/缩写问题：`none`

### table `tab:warmup`

caption：{} restart warmup transition. ``Flag'' means at least one fixed bit position exceeds the displayed MSB-route cutoff $X_ {cutoff}=605$; archived LSB-route checks use $X_ {cutoff}=632$.

- caption 功能序列：`OBJECT`
- 角色：`concept`
- first mention：`ABS.S4`
- 正文是否解释看什么：`yes`
- 正文是否给定量：`yes`
- caption/body 一致性：`consistent`
- 表格 note 需求：`no`
- 单位/缩写问题：`check_units_or_abbreviations`

### figure `fig:samplerlock`

caption：Sample-RO lock schematic for the counterfactual. Only the listed sample-RO LUT assignments are the intended constraint perturbation in this comparison; implemented local routing and neighborhood effects may still vary.

- caption 功能序列：`OBJECT -> TAKEAWAY`
- 角色：`result`
- first mention：`SAMPLER_SIDE_COUNTERFACTUALS.P13.S1`
- 正文是否解释看什么：`yes`
- 正文是否给定量：`no`
- caption/body 一致性：`consistent`
- 表格 note 需求：`no`
- 单位/缩写问题：`check_units_or_abbreviations`

### table `tab:tdccal`

caption：8 MiB {} code-density calibration boundary.

- caption 功能序列：`OBJECT`
- 角色：`concept`
- first mention：`TDC_ASSISTED_MECHANISM_DIAGNOSIS.P5.S3`
- 正文是否解释看什么：`no`
- 正文是否给定量：`yes`
- caption/body 一致性：`consistent`
- 表格 note 需求：`no`
- 单位/缩写问题：`none`

### figure `fig:reducedxorconstruct`

caption：Reduced-XOR construction. The experiment compares the final all64 output, same-data-RO directions, complements that remove one direction from the final XOR, and line-direction controls that XOR across data ROs at one sampler phase.

- caption 功能序列：`OBJECT -> CONDITION`
- 角色：`concept`
- first mention：`REDUCED_XOR_COUNTERFACTUALS.P1.S2`
- 正文是否解释看什么：`yes`
- 正文是否给定量：`no`
- caption/body 一致性：`consistent`
- 表格 note 需求：`no`
- 单位/缩写问题：`none`

### figure `fig:reducedxor`

caption：Warmup-10 reduced-XOR $p_1$ values for the complete run01 direction map. The left group contains all64 followed by same-data-RO directions; the right group contains complements. Bar patterns distinguish the groups for grayscale viewing.

- caption 功能序列：`OBJECT`
- 角色：`concept`
- first mention：`REDUCED_XOR_COUNTERFACTUALS.P1.S2`
- 正文是否解释看什么：`yes`
- 正文是否给定量：`no`
- caption/body 一致性：`check_caption_body_takeaway`
- 表格 note 需求：`no`
- 单位/缩写问题：`none`

## caption-only storyline

- `fig:boundary`：figure fig:boundary: architecture; OBJECT -> TAKEAWAY
- `fig:workflow`：figure fig:workflow: workflow; OBJECT
- `tab:setup`：table tab:setup: setup; OBJECT -> CONDITION
- `tab:sp800summary`：table tab:sp800summary: comparison; OBJECT -> TAKEAWAY
- `tab:warmup`：table tab:warmup: concept; OBJECT
- `fig:samplerlock`：figure fig:samplerlock: result; OBJECT -> TAKEAWAY
- `tab:tdccal`：table tab:tdccal: concept; OBJECT
- `fig:reducedxorconstruct`：figure fig:reducedxorconstruct: concept; OBJECT -> CONDITION
- `fig:reducedxor`：figure fig:reducedxor: concept; OBJECT