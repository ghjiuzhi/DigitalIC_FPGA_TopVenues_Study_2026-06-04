# Manuscript Style Imitation Guide

这个文件给修改正文的 Codex 使用。目标不是复制 60 篇论文的原句，而是模仿它们的“段落功能”：每一段解决什么问题，每一张图承担什么证据，每一个 claim 如何被限定。

## 先做什么

修改 `RO_TRNG_entropy_boundary` 前，先读三类材料：

1. 写法层：`07_writing_assets\title_abstract_intro_patterns.md`、`figure_table_review_guide.md`、`post_edit_review_checklist.md`。
2. 方向层：`08_topic_layers\ROTRNG\ROTRNG_style_to_manuscript_bridge.md`、`ROTRNG_direction_writing_patterns.md`。
3. 正文层：`evidence\claim_evidence_table.md`、`evidence\related_work_matrix.md`、`manuscript\main.tex`。

读完后只回答一个问题：这篇稿子最应该被写成什么？本稿当前应定位为 measurement-driven entropy-boundary paper，而不是新 TRNG architecture paper，也不是 SP800-90B certification report。

## 标题怎么仿照

顶刊标题通常不是“研究某某”，而是把对象、机制、边界和平台放在一起。标题要让审稿人一眼知道 paper 的 claim 边界。

可用结构：

- `A Measurement-Boundary Study of [object] in [platform/context]`
- `[Mechanism]-Aware Evaluation of [object] Under [condition]`
- `When [assumption] Fails: [method] for [object] in [platform]`
- `[Evidence type] Characterization of [boundary/mechanism] in [system]`

RO-TRNG 稿件标题建议包含：

- 对象：RO-TRNG entropy source 或 sampler-side implementation。
- 机制：restart behavior、placement dependence、sampler aperture、counterfactual sampler evidence。
- 边界：measured entropy-source boundary、measurement boundary、implementation boundary。
- 平台：FPGA 或 Zynq-7020，只有在证据足够时再写进标题。

避免：

- `Study of...`
- `Research on...`
- `A Novel RO-TRNG...`，除非正文真的提出并验证了新架构。
- `Secure/Robust/Certified...`，除非证据链能支撑安全或认证级 claim。

## 摘要怎么仿照

摘要按 5 句功能写，不要一开始就堆指标。

1. Problem：指出已有 RO-TRNG 评估容易把 sampler 当成 passive readout，导致 entropy-source boundary 不清楚。
2. Method：说明本文用 placement/restart/counterfactual sampler/TDC/reduced-XOR 等证据链检查 boundary。
3. Setup：交代平台、板卡、实验边界和 measurement setup。
4. Evidence：只放最能支撑主 claim 的 2-3 个结果，不把所有表格搬进摘要。
5. Bounded claim：把结论限定在测量边界和当前硬件范围内。

英文模板：

`Existing [RO-TRNG evaluation practice] often treats [sampler/readout block] as [assumption], leaving [boundary] under-specified. This paper presents [measurement method/evidence chain] to examine [specific boundary] on [platform]. Across [setup], the results show that [strongest bounded evidence]. These observations indicate that [sampler-side implementation] should be considered part of [measured entropy-source boundary] under [conditions].`

审查时问：

- 摘要有没有说清“问题是什么”，而不是只说“我们做了很多实验”？
- 有没有把 platform 和条件说清？
- 有没有把 `indicate/suggest/observed` 和 `demonstrate/prove/certify` 区分开？
- 有没有出现证据表里没有的数字？

## Introduction 怎么仿照

Introduction 建议按四段推进：

1. 场景段：TRNG 是 root-of-trust/cryptographic hardware 的基础，RO-TRNG 因 FPGA 友好而常用。
2. 痛点段：RO-TRNG 的随机性不是抽象算法属性，而受 physical implementation、sampling、restart 和 measurement procedure 影响。
3. gap 段：已有文献分别覆盖 architecture、entropy estimation、attacks、PUF-TRNG 和 standards，但 sampler-side measurement boundary 没被系统说清。
4. contribution 段：本文给出 measurement-driven evidence chain，说明 sampler-side implementation 需要纳入被测 entropy-source boundary。

写 gap 时不要说“没人做过 TRNG”这种大话。要写成：

`However, these lines of work do not directly answer whether [specific block/operation] can be treated as outside the measured entropy-source boundary when [measurement condition] changes.`

贡献列表建议 3 条以内：

- 一个 boundary framing。
- 一套 measurement/evidence chain。
- 一个 bounded empirical finding 或 practical implication。

## Related Work 怎么仿照

不要按年份流水账。按“它们解决什么、没解决什么”分组：

- Foundations and entropy estimation：说明经典 RO-TRNG 和 entropy 评估给了基本问题框架。
- FPGA TRNG/PUF architectures：说明很多工作关注 source design、throughput、area、randomness tests。
- Security and environmental sensitivity：说明 attacks、injection、PVT、frequency manipulation 相关。
- Measurement and restart methodology：说明 restart/health tests/measurement setup 对评估有影响。
- 本文 gap：这些工作没有把 sampler-side implementation 作为 entropy-boundary 问题直接测出来。

每组最后一句都要服务本文，不要只介绍别人。

## 图表怎么仿照

图表必须按 evidence chain 排，而不是按“我有什么图就放什么图”排。

推荐顺序：

1. Boundary overview figure：画清 RO、sampler、counter、post-processing、measurement point，标出争议边界。
2. Experimental setup figure/table：板卡、placement、restart protocol、sample size、clock/reset/control。
3. Evidence figures：placement effect、restart behavior、sampler counterfactual、TDC/jitter proxy、reduced-XOR。
4. SOTA/related-work table：比较文献是否覆盖 sampler boundary、restart evidence、implementation sensitivity、security context。
5. Limitation table 或 discussion paragraph：说明当前平台、样本、PVT、测试标准边界。

每张图的 caption 都应包含：

- 测了什么。
- 在什么 setup 下测。
- 这张图支撑哪个 claim。
- 不支撑什么更大的 claim。

## 修改顺序

1. 先改 title/abstract/introduction，不碰结果数字。
2. 再补 related work 的分组和 gap。
3. 再检查 figure/table narrative 是否能支撑 introduction 的 claim。
4. 最后用 `post_edit_review_checklist.md` 做四轮自查。

禁止事项：

- 不发明结果。
- 不夸大成 universal FPGA-family conclusion。
- 不把 TVLSI sampler-aperture 扩展稿混进当前 TIM 主线。
- 不把本稿写成标准认证报告。
