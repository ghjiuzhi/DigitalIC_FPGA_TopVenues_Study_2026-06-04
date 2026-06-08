# Top-Venue Micro Style Manual

这个文件专门回答“顶刊到底怎么取标题、怎么写摘要、数字怎么写、段落怎么接”的问题。它比前面的写法总结更细，重点是句子级和格式级模仿。

## 参考样本

本轮抽查了本地写法层中的代表样本：

- TCAS-I：`FREYA: A 0.023-mm²/Channel, 20.8-μW/Channel, Event-Driven 8-Channel SoC...`
- TCAS-I：`A High-Reliability, Non-CRP-Discard Arbiter PUF...`
- TCAS-II：`A Lightweight and Hardware-Efficient NTT FPGA Accelerator...`
- TVLSI：`A 66-Gb/s/5.5-W RISC-V Many-Core Cluster...`
- TC：`An FPGA-Based Open-Source Hardware-Software Framework...`
- TCAD：`When Random Is Bad: Selective CRPs...`
- TCHES：`RDS: FPGA Routing Delay Sensors...`

这些样本说明：顶刊标题和摘要并不是“形容词越多越好”，而是每个修饰词都要被结果、方法或应用边界支撑。

## 标题：2-3 个形容词怎么用

顶刊标题里的形容词通常分三类。

第一类：指标型形容词

- `High-Reliability`
- `Low-Latency`
- `High-Throughput`
- `Energy-Efficient`
- `Resource-Efficient`
- `Lightweight`

这类词必须能在摘要或实验表里找到数字支撑。比如标题写 `low-latency`，摘要或结果中就要有 latency；写 `resource-efficient`，就要有 LUT/FF/BRAM/DSP/area/power 对比。

第二类：机制型形容词

- `Event-Driven`
- `Restart-Based`
- `Boundary-Aware`
- `Counterfactual`
- `Delay-Difference`
- `Routing-Delay`

这类词说明“你靠什么机制解决问题”。它比泛泛的 `novel` 更像顶刊。

第三类：范围型形容词

- `FPGA-Based`
- `Sampler-Side`
- `Measurement-Driven`
- `Open-Source`
- `Side-Channel`
- `Post-Quantum`

这类词限定系统边界和应用场景，防止 claim 太大。

## 标题推荐公式

公式 A：`[Metric adjective] + [Mechanism adjective] + [Object] for [Application]`

适合硬件加速器、SoC、FPGA 架构。

例子风格：`A Lightweight and Hardware-Efficient NTT FPGA Accelerator for FHE Applications`

公式 B：`[Metric numbers]: A [mechanism] [system] for [application]`

适合有很强芯片测量结果的 TCAS-I/TVLSI。

例子风格：`FREYA: A 0.023-mm²/Channel, 20.8-μW/Channel, Event-Driven 8-Channel SoC...`

公式 C：`[Mechanism] as [Boundary/Primitive] in [Platform]`

适合你当前 RO-TRNG 稿件，因为它不是新架构，而是 boundary paper。

候选结构：

- `Sampler-Side Implementation as a Measured Entropy-Source Boundary in FPGA RO-TRNGs`
- `Restart-Based Evidence for Sampler-Boundary Effects in FPGA RO-TRNG Evaluation`
- `A Measurement-Driven Characterization of Sampler-Side Boundary Effects in FPGA RO-TRNGs`

公式 D：`When [assumption/problem] Is [unexpected]: [method] for [object]`

适合 TCAD/TCHES 风格，语气更锋利，但要克制。

候选结构：

- `When the Sampler Is Not Passive: Boundary-Aware Evaluation of FPGA RO-TRNGs`

## 摘要：顶刊常见句子功能

很多顶刊摘要第一句确实先写背景，但不是泛泛背景，而是“带约束的背景”。

标准 6 句结构：

1. 背景句：说明对象为什么重要。
2. 问题句：说明现有做法的具体不足。
3. 解决句：本文提出/研究/构建什么方法。
4. 创新句 1-2：说明机制、架构或实验设计的新点。
5. 数字句：给最强 2-4 个结果。
6. 边界句：说明结论适用范围或意义。

RO-TRNG 摘要可按这个顺序写：

1. `Ring-oscillator TRNGs are widely used in FPGA-based security systems because they can be implemented with digital resources.`
2. `However, their evaluation often treats the sampler-side readout path as outside the entropy source, leaving the measured boundary unclear under restart-based measurements.`
3. `This paper studies this boundary through placement, restart, counterfactual sampler, and timing-related evidence on the evaluated FPGA setup.`
4. `The key idea is to test whether sampler-side implementation behaves as a passive readout stage or changes the measured entropy behavior.`
5. `Measurements show [your strongest numbers], under [setup].`
6. `The results indicate that sampler-side implementation should be included in the measured entropy-source boundary for this evaluation scope.`

## 数字和单位怎么写

标题里可以出现数字，但只有在数字是卖点时才放。

常见形式：

- `0.023-mm²/Channel`
- `20.8-μW/Channel`
- `66-Gb/s/5.5-W`
- `8K@30FPS`
- `97.2%`

LaTeX 建议：

- 正文和摘要中的数字单位用 `siunitx`：`\SI{20.8}{\micro\watt}`、`\SI{0.023}{\milli\meter\squared}`。
- 百分比用 `\SI{97.2}{\percent}` 或统一写 `97.2%`，不要有时 math mode、有时 text mode。
- 变量或公式用 math mode，测量数字尽量用 text/siunitx，不要把普通数字写成 `$20.8$` 导致字体和周围不同。
- 标题里 IEEE LaTeX 对单位较敏感，过复杂的 `\SI{}` 可能影响标题；可用文本形式，但全文要统一。

小数位规则：

- 不要机械保留很多位。
- 和测量精度一致：实验仪器、采样统计、表格比较能支撑几位，就写几位。
- improvement 百分比通常 1 位小数足够，例如 `12.4%`。
- 面积/功耗如果来自版图或工具报告，可保留 2-3 位有效数字，例如 `0.023 mm²`。
- 熵、概率、p-value、failure rate 要根据统计意义决定，不要只为了好看保留 4-6 位。
- 同一类指标在同一张表里小数位必须统一。

## 段落怎么组织

顶刊段落通常不是“想到哪写哪”，而是每段承担一个功能。

Introduction 段落链：

1. Context：为什么这个系统重要。
2. Constraint：这个方向受什么硬件/安全/测量约束。
3. Existing work：已有工作怎么解决一部分。
4. Gap：剩下哪个具体问题没解决。
5. This work：本文怎样定义问题、怎样验证。
6. Contributions：三条以内，全部能映射到 evidence。

段落衔接常用功能句：

- `However, this abstraction becomes fragile when...`
- `This distinction matters because...`
- `Existing studies have mainly focused on..., whereas...`
- `In contrast, this paper treats ... as a measurement-boundary problem.`
- `The goal is not to certify ..., but to quantify whether ...`

## 用词：顶刊更喜欢什么

更稳的词：

- `examines`
- `characterizes`
- `evaluates`
- `indicates`
- `is consistent with`
- `under the evaluated setup`
- `measurement evidence`
- `bounded implication`

少用或慎用：

- `proves`
- `guarantees`
- `perfect`
- `secure`
- `robust`
- `universal`
- `certified`
- `novel`，除非新在哪里非常明确。

## 对当前 RO-TRNG 稿件的直接建议

标题不要堆 2-3 个空泛形容词。建议用 2 个技术修饰：

- 一个机制词：`Restart-Based`、`Sampler-Side`、`Measurement-Driven`。
- 一个边界词：`Entropy-Source Boundary`、`Boundary-Aware`。

摘要不要先写很长大背景。第一句话写背景，第二句话立刻转到问题。第三句开始写方法。数字只放最关键的 2-3 个，并且统一单位和小数位。
