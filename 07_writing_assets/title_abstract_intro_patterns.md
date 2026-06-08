# Title, Abstract, and Introduction Patterns

这个文件把 60 篇顶刊样本中最可迁移的写法抽成模板。模板是自写句式，不是原文摘抄。

## 标题模式

模式 1：对象 + 边界 + 平台

`[Boundary/Measurement] Characterization of [Object] in [Platform]`

适合当前 RO-TRNG 稿，因为主线是 measurement boundary。

模式 2：机制 + 评估对象

`[Mechanism]-Aware Evaluation of [Object] Under [Condition]`

适合强调 restart、sampling、placement、jitter、phase noise。

模式 3：问题反转式

`When [Common Assumption] Is Not Passive: [Method] for [Object]`

适合指出 sampler 不是简单 readout 的稿件，但标题要克制，避免过度戏剧化。

模式 4：方法 + claim 边界

`A [Method]-Driven Study of [Boundary] in [System]`

比 `Study of` 更好，因为把 method 和 boundary 说清了。

## 摘要句式模板

Problem 句：

`Although [technology] is widely used for [application], its evaluation often assumes that [component/process] is outside [boundary].`

Gap 句：

`This assumption becomes difficult to justify when [physical condition or measurement operation] changes [observable behavior].`

Method 句：

`We examine this boundary through [evidence chain], using [platform/setup] as the measurement vehicle.`

Evidence 句：

`The measurements show that [bounded observation], while [limitation or condition] remains controlled.`

Claim 句：

`These results indicate that [component/process] should be treated as part of [measured boundary] for [scope], rather than as a purely passive readout stage.`

Limitation 句：

`The conclusion is limited to [platform/setup/condition] and is intended as measurement evidence, not a certification claim.`

## Introduction 段落模板

第一段：应用背景

`True random number generators are a basic component in cryptographic and embedded security systems. Ring-oscillator-based TRNGs are attractive on FPGAs because they require no dedicated analog block and can be implemented with ordinary digital resources.`

第二段：问题收窄

`However, the randomness observed from an RO-TRNG is not determined by the oscillator alone. The sampling path, reset/restart procedure, placement, and measurement interface can alter what is actually being evaluated.`

第三段：文献 gap

`Prior work has studied RO-TRNG architectures, entropy estimation, attacks, and implementation sensitivity. These studies provide the foundation for evaluating entropy sources, but they do not directly answer whether the sampler-side implementation can be excluded from the measured entropy-source boundary under restart-based measurements.`

第四段：本文做什么

`This paper frames the issue as a measurement-boundary problem. Instead of proposing a new TRNG architecture, it builds an evidence chain around [placement/restart/counterfactual sampler/TDC/reduced-XOR] to test whether the sampler-side implementation behaves as a passive readout stage.`

## Contribution List 模板

可用 3 条：

1. `We formulate [sampler-side implementation] as a measurement-boundary issue for FPGA RO-TRNG evaluation.`
2. `We construct a measurement evidence chain using [methods] on [platform/setup].`
3. `We show that [bounded observation], indicating that [boundary implication] under [conditions].`

不要写：

- `We propose a secure TRNG`，除非有完整安全评估。
- `We pass NIST tests and therefore prove randomness`。
- `This is the first...`，除非做过充分检索并能证明。
