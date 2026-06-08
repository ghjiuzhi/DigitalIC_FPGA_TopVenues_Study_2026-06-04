# 顶刊论文修辞形态学手册

这个文件回答一个很具体的问题：论文里每一句话在干什么。目标不是收藏“高级句子”，而是学习顶刊论文如何把句子排成可复用的功能序列。

配套证据表见：

- `micro_style_audit_assets/topvenue_sentence_function_matrix.csv`
- `micro_style_audit_assets/venue_rhetorical_morphology_summary.md`
- `micro_style_audit_assets/abstract_move_taxonomy.md`

## 1. 句子功能标签

| 标签 | 功能 | 写作判断 |
| --- | --- | --- |
| `BG` | Background | 说明研究对象、应用场景或硬件约束为什么重要。 |
| `PROBLEM` | Problem | 指出当前瓶颈、挑战、风险或失败模式。 |
| `GAP` | Gap | 说明现有研究没有覆盖的变量、平台、模型或边界。 |
| `LIMIT` | Limitation | 解释已有方法的隐含假设和适用范围。 |
| `NEED` | Need | 说明这个 gap 为什么值得解决。 |
| `TASK` | Task | 把本文目标压成可测、可复现、可对比的问题。 |
| `METHOD` | Method | 说明本文采用的机制、架构、流程或控制变量。 |
| `SETUP` | Setup | 交代平台、workload、benchmark、FPGA/ASIC、工具链或攻击模型。 |
| `RESULT` | Result | 给出关键观察、指标或 SOTA 对比。 |
| `INTERPRET` | Interpretation | 解释结果说明了什么机制或设计取舍。 |
| `BOUNDARY` | Boundary | 收住 claim，说明结论在哪些条件下成立。 |
| `CONTRIB` | Contribution | 把贡献映射到概念、方法、实证或 artifact 证据。 |
| `TRANSITION` | Transition | 把上一段结论转成下一段问题。 |
| `ORG` | Organization | 说明论文结构安排。 |

真正要模仿的是序列，不是单句：

```text
Abstract = BG -> PROBLEM/GAP -> TASK/METHOD -> SETUP -> RESULT -> INTERPRET/BOUNDARY
Introduction = BG -> PROBLEM -> PRIOR/LIMIT -> GAP -> NEED -> METHOD -> CONTRIB -> ORG
Results paragraph = SETUP/QUESTION -> FIGURE/TABLE -> OBSERVATION -> RESULT -> INTERPRET -> BOUNDARY
Contribution block = conceptual -> methodological -> empirical -> artifact/audit
```

## 2. Abstract 的形态

顶刊摘要通常不是“背景越大越好”，而是用最少句子完成功能闭环。数字 IC / FPGA 论文尤其强调：对象、瓶颈、方法、平台、指标、边界必须互相支撑。

### 5 句型

适合 TCAS-II brief、短摘要、单点贡献论文。

| 句号 | 功能 | 作用 |
| --- | --- | --- |
| S1 | `BG/PROBLEM` | 用对象和瓶颈一起开场。 |
| S2 | `GAP` | 点出现有工作漏掉的变量或场景。 |
| S3 | `TASK/METHOD` | 说明本文做什么、怎么做。 |
| S4 | `RESULT` | 给出最强 1-3 个数字或观察。 |
| S5 | `INTERPRET/BOUNDARY` | 解释意义并限定适用范围。 |

### 7 句型

适合 TCAS-I、TVLSI、TCAD、TCHES/CHES 中多数实验型论文。

| 句号 | 功能 | 作用 |
| --- | --- | --- |
| S1 | `BG` | 说明对象为什么重要。 |
| S2 | `PROBLEM` | 说明当前瓶颈或风险。 |
| S3 | `GAP/LIMIT` | 指出现有工作没处理好的具体空白。 |
| S4 | `TASK/METHOD` | 说明本文研究或提出什么。 |
| S5 | `SETUP` | 说明平台、实验、实现或攻击模型。 |
| S6 | `RESULT` | 给出核心结果或 SOTA 对比。 |
| S7 | `INTERPRET/BOUNDARY` | 解释结果意义，同时收住 claim。 |

### 8 句型

适合系统复杂、证据链多、需要分开写机制和实验的论文。

```text
BG -> PROBLEM -> PRIOR/LIMIT -> GAP -> METHOD -> SETUP -> RESULT -> BOUNDARY
```

判断是否需要 8 句：如果方法包括架构、流程、实验控制和多个结果指标，`METHOD` 与 `SETUP` 不要挤在同一句。

## 3. Introduction 的形态

Introduction 更适合按段落看。成熟论文通常让每段承担一个主功能，而不是把背景、prior work、方法和贡献混在同一段。

| 段落 | 功能 | 写法 |
| --- | --- | --- |
| P1 | `BG` | 从应用、workload、安全场景或硬件约束开场。 |
| P2 | `PROBLEM` | 把重要性压到具体瓶颈，例如 area、power、latency、throughput、security、runtime、measurement validity。 |
| P3 | `PRIOR/LIMIT` | 说明已有研究解决了什么，但隐含了什么条件。 |
| P4 | `GAP/NEED` | 明确本文要打的空白，以及为什么这个空白会影响评价或设计。 |
| P5 | `TASK/METHOD` | 把 gap 变成本文可执行的问题、架构或实验。 |
| P6 | `CONTRIB` | 列 2-4 条贡献，每条能对应图、表、实验或 artifact。 |
| P7 | `ORG` | 可选，短句交代结构。 |

Introduction 中最容易出问题的是 P3 到 P4：不要只写“已有方法很多”，要写“已有方法主要关注 A，因此 B 在 C 条件下仍不清楚”。

## 4. Results 段落形态

结果段不是表格的口头复述。一个可靠的结果段通常按这个顺序走：

```text
Question/setup -> figure/table reference -> observation -> quantified result -> interpretation -> caveat/boundary
```

| 功能 | 句子要回答的问题 |
| --- | --- |
| `SETUP` | 这组结果在什么平台、参数、workload、攻击模型或放置条件下得到？ |
| `RESULT` | 图表显示了什么观察？最关键数字是什么？ |
| `INTERPRET` | 这个数字说明了机制、架构或安全边界的什么变化？ |
| `BOUNDARY` | 这个观察在哪些条件下成立，不能推出什么？ |

数字 IC / FPGA 论文中，结果句最好有四个元素：

```text
platform/condition + metric + baseline/comparison + improvement or observation
```

## 5. Contribution block 的形态

贡献不是随便列亮点。顶刊常见贡献可以分成四类，最好每类都能追到证据。

| 类型 | 功能 | 证据 |
| --- | --- | --- |
| Conceptual contribution | 重新定义问题、边界或评价对象。 | 问题定义、threat model、measurement boundary。 |
| Methodological contribution | 给出实验、控制变量、工具流或架构方法。 | 方法节、算法、实验流程、实现流程。 |
| Empirical contribution | 给出可复查发现和指标。 | 图、表、benchmark、ablation、SOTA comparison。 |
| Artifact/audit contribution | 给出工具、数据、开源平台或审计表。 | repository、dataset、artifact appendix、复现实验说明。 |

推荐 3 条贡献结构：

```text
1. Concept: We formulate/identify/characterize ...
2. Method: We design/evaluate/implement ...
3. Evidence: We show/measure/demonstrate ..., under ...
```

## 6. RO-TRNG 写作模板

如果用于当前 RO-TRNG 稿件，可以把形态压成下面的模板。

Abstract：

```text
S1 [BG]: FPGA RO-TRNGs are useful because they use digital resources as lightweight entropy sources.
S2 [PROBLEM]: Their measured behavior can depend on physical implementation details that are not visible at RTL.
S3 [GAP]: The sampler-side implementation boundary remains insufficiently characterized under restart-based measurements.
S4 [TASK/METHOD]: This paper evaluates the measured entropy-source boundary through controlled sampler-side placement and routing variants.
S5 [SETUP]: The data-RO structure is held fixed while sampler-side LOC/BEL and local implementation context are perturbed.
S6 [RESULT]: Measurements show that nominally equivalent RTL instances can produce different restart-balance behavior.
S7 [BOUNDARY]: The evidence supports including sampler-side implementation context in the measured entropy-source boundary for the evaluated setup.
```

Introduction：

```text
P1 BG: Why FPGA RO-TRNGs matter.
P2 PROBLEM: Why implementation context can affect measured entropy behavior.
P3 PRIOR/LIMIT: What prior TRNG and RO work measures, and what boundary it assumes.
P4 GAP/NEED: Why sampler-side context is a missing but consequential boundary.
P5 METHOD: Controlled placement/routing variants and restart evidence.
P6 CONTRIB: Boundary formulation, controlled methodology, empirical evidence.
P7 ORG: Optional roadmap.
```

Results paragraph：

```text
SETUP: We compare fixed data-RO variants with sampler-side implementation perturbations.
RESULT: The restart-balance distribution changes across nominally equivalent RTL instances.
INTERPRET: This indicates that the sampler path behaves as part of the measured boundary, not only as passive readout.
BOUNDARY: The claim is limited to the evaluated FPGA, constraints, restart protocol, and placement conditions.
```

## 7. 使用方法

1. 写摘要时，先选 5/7/8 句型，再给每句话贴标签。
2. 写 Introduction 时，先写段落功能链，再填内容。
3. 写 Results 时，检查每段是否有 setup、observation、number、interpretation、boundary。
4. 写贡献时，检查每条贡献是否能指向方法节、图、表或 artifact。
5. 写完后，用 `topvenue_sentence_function_matrix.csv` 过滤同 venue、同 section 的样本，看顶刊如何安排同类功能。
