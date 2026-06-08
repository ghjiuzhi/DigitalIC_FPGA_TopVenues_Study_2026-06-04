# Venue Rhetorical Morphology Summary

本文件基于 `topvenue_sentence_function_matrix.csv` 汇总 01-06 六个 venue 的句子功能形态。统计范围为 60 篇论文，1377 条功能单元；每篇至少包含 Abstract、Introduction、Results、Contribution 四类记录。部分 Introduction 和 Results 来自 notes-derived fallback，适合做写法归纳，不适合当作严格语言学标注。

## 总体规律

数字 IC / FPGA 顶刊共同的写法链条是：

```text
object/context -> bottleneck -> specific gap -> method/control variable -> implementation/evaluation setup -> result numbers -> bounded implication
```

最值得模仿的不是某个动词，而是“每个 claim 都有边界和证据”。标题、摘要、贡献、图表、实验表应互相支撑。

## TCAS-I

TCAS-I 偏完整电路/系统闭环。摘要和 Introduction 往往允许更完整的背景和问题铺垫，但最后必须落到实现、测量、SOTA comparison 或安全指标。

- Abstract：常见 `BG -> PROBLEM -> METHOD -> SETUP -> RESULT -> BOUNDARY`，数字密度可以高，但数字要服务系统闭环。
- Introduction：适合 6 段结构，背景、痛点、prior limit、gap、approach、contribution 都可以展开。
- Results：强调 FPGA/ASIC 实现、frequency、area、power、latency、throughput、安全指标和对比表。
- Contribution：不要只说 proposed method，要写成“在某平台/约束下改善某指标”。

## TCAS-II

TCAS-II 是 express contribution，摘要是最重要的战场。它不喜欢长综述，更喜欢直接把一个单元、算子、sensing scheme 或紧凑架构说硬。

- Abstract：推荐 5 句型，`BG/PROBLEM -> GAP -> METHOD -> RESULT -> BOUNDARY`。
- Introduction：快速收束，不要写成 TCAS-I 式大背景。
- Results：重点是一张局部创新的硬指标表，证明资源、时延、能耗、精度或安全收益。
- Contribution：贡献列表要短，通常 2-3 条足够。

## TVLSI

TVLSI 更关注真实硬件约束下的架构、数据流、存储层次、并行度和可扩展性。论文要让读者看到实现限制如何塑造方法。

- Abstract：常见 metric-led 或 context-led opening，很快进入平台、规模、吞吐、能效和可扩展性。
- Introduction：从 workload 或 VLSI bottleneck 写起，强调 bandwidth、memory hierarchy、parallelism、timing closure。
- Results：implementation report 和 benchmark 是核心证据，最好把架构参数和 workload 绑定解释。
- Contribution：贡献应落在 architecture/dataflow/implementation tradeoff，而不是泛泛 algorithm novelty。

## TC

TC 偏系统和架构，尤其看重 framework、platform、benchmark、co-design 和 workload 证据。它比电路类 venue 更需要说明系统边界。

- Abstract：常见 `GAP/PROBLEM -> SYSTEM/METHOD -> SETUP -> RESULT -> INTERPRET`。
- Introduction：需要解释为什么这个系统问题不是局部优化，而是影响可用性、可扩展性或安全研究流程。
- Results：benchmark、open-source framework、hardware-software stack、workflow evidence 比单个硬件数字更重要。
- Contribution：可以包含 artifact contribution，但必须说明 artifact 解决什么研究或工程阻塞。

## TCAD

TCAD 更偏建模、自动化、工具流、设计空间和安全分析方法。写法要把方法的输入、输出、假设、benchmark 和验证协议说清楚。

- Abstract：常见 problem-led 或 model/tool-flow-led opening。
- Introduction：prior work 的 limitation 很关键，要说明现有 flow、model、attack、analysis 在什么条件下不够。
- Results：benchmark、ablation、runtime、accuracy、attack success rate、design-space comparison 是常见证据。
- Contribution：方法贡献和实证贡献要分开写，避免“工具有效”但没有适用范围。

## TCHES/CHES

TCHES/CHES 对安全边界、threat model、实验可复现和 claim 强度非常敏感。句子常带有更明确的 boundary control。

- Abstract：常见 `PROBLEM -> GAP -> METHOD/ATTACK/COUNTERMEASURE -> EVIDENCE -> BOUNDARY`。
- Introduction：需要说明 attacker model、implementation assumptions、evaluation scope。
- Results：不仅要写数字，还要解释数字如何支持安全 claim 或攻击/防护机制。
- Contribution：适合写 conceptual boundary、methodology、empirical evidence、artifact/audit 四类贡献。

## 读表建议

在 `topvenue_sentence_function_matrix.csv` 中可以这样筛：

- 写摘要：筛 `section_type=Abstract`，再按目标 venue 看 `function_chain`。
- 写 Introduction：筛 `section_type=Introduction`，重点看 `BG/CONTEXT`、`PROBLEM/GAP`、`TASK/METHOD`。
- 写实验结果：筛 `section_type=Results`，看 `SETUP/RESULT` 和 `RESULT/INTERPRET` 如何连。
- 写贡献：筛 `section_type=Contribution`，看每篇如何把贡献压成可验证的主张。
