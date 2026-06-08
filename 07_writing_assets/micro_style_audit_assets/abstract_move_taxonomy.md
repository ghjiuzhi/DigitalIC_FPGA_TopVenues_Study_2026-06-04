# Abstract Move Taxonomy

本文件是 `topvenue_sentence_function_matrix.csv` 使用的摘要功能标签说明。旧版的 coarse move 保留为直觉入口，但正式标注采用更细的 rhetorical morphology 标签。

## 细粒度标签

| 标签 | move | 摘要中的作用 |
| --- | --- | --- |
| `BG` | Background | 研究对象、应用场景或硬件约束为什么重要。 |
| `PROBLEM` | Bottleneck/Problem | 现有设计、评估、攻击或工具流卡在哪里。 |
| `GAP` | Research Gap | 现有工作没有覆盖的变量、平台、模型或边界。 |
| `LIMIT` | Prior Limitation | 已有方法的隐含假设或适用范围。 |
| `NEED` | Need | 为什么这个 gap 会影响指标、可信度或安全性。 |
| `TASK` | Task | 本文要解决的窄问题。 |
| `METHOD` | Method | 本文提出、研究、设计、实现或评估什么。 |
| `SETUP` | Evaluation Setup | 平台、实验、benchmark、FPGA/ASIC、工具链或攻击模型。 |
| `RESULT` | Numbers/Observation | 最强结果、测量数字、SOTA 对比或关键观察。 |
| `INTERPRET` | Interpretation | 结果说明的机制、设计取舍或安全含义。 |
| `BOUNDARY` | Bounded Implication | 结论适用范围和 claim 边界。 |
| `CONTRIB` | Contribution Signal | 摘要或引言中显式声明本文贡献、artifact 或 evidence chain。 |

## 常见摘要序列

5 句型：

```text
BG/PROBLEM -> GAP -> TASK/METHOD -> RESULT -> INTERPRET/BOUNDARY
```

7 句型：

```text
BG -> PROBLEM -> GAP/LIMIT -> TASK/METHOD -> SETUP -> RESULT -> INTERPRET/BOUNDARY
```

8 句型：

```text
BG -> PROBLEM -> PRIOR/LIMIT -> GAP -> METHOD -> SETUP -> RESULT -> BOUNDARY
```

## Venue 差异

- TCAS-I：允许完整背景和系统闭环，结果句要支撑标题里的指标词。
- TCAS-II：更短，问题、方法、数字要早出现。
- TVLSI：平台、实现规模、数据流、能效和可扩展性要进入摘要。
- TC：framework、system boundary、benchmark 和 artifact 意义更重要。
- TCAD：tool/model/flow 的输入、输出、benchmark 和限制要清楚。
- TCHES/CHES：threat model、security boundary 和 claim strength 要控制。

## 适合 RO-TRNG 当前稿件的版本

```text
BG -> measurement-boundary PROBLEM -> sampler-side GAP -> controlled-evidence METHOD -> restart/placement SETUP -> representative RESULT -> diagnostic BOUNDARY
```

也就是：

1. 说明 FPGA RO-TRNG 为什么重要。
2. 说明 RTL 级抽象无法完全捕捉实现相关测量行为。
3. 指出 sampler-side boundary 在 restart measurement 中仍不清楚。
4. 说明本文用 controlled placement/routing variants 检验边界。
5. 交代数据 RO 保持固定、sampler-side context 被扰动。
6. 给出 restart-balance 或 entropy-behavior 的关键观察。
7. 把结论限定在 evaluated FPGA、restart protocol 和 placement conditions 下。
