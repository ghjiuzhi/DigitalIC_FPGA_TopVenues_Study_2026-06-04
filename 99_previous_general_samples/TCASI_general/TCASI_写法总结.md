# TCAS-I 近年论文写法总结

## 样本说明
本目录整理了 10 篇 2024-2025 年 IEEE Transactions on Circuits and Systems I: Regular Papers 的开放版本论文，覆盖忆阻/混沌、5G LDPC、RF 滤波、PUF、RISC-V SoC、可持续 RF、后量子密码硬件、事件驱动生物传感 SoC 和 ADC。PDF 均来自机构库、作者/学校开放仓储或开放版本入口，下载状态见 `metadata/papers.csv`。

## TCAS-I 论文的共同结构
1. **摘要先报问题，再报指标。** 大多数摘要不是文学式背景，而是快速说明应用约束、现有痛点、本文方法和量化结果。电路类论文尤其喜欢把带宽、功耗、面积、SNDR、吞吐、BER、S 参数等指标放进摘要。
2. **Introduction 的核心是 gap，不是综述。** 它们通常用 2-4 段建立应用压力，再用一段压缩相关工作，随后明确“现有方法还不能同时满足 A/B/C”。贡献列表通常非常具体，写成算法、架构、实现、测量四层。
3. **方法部分强调可复现的设计逻辑。** TCAS-I 不喜欢只展示调参结果。好的论文会解释为什么选择这个模型、拓扑、数据路径或制造流程，并把限制条件讲清楚。
4. **实验必须闭合到系统指标。** 理论/算法论文要落到硬件复杂度或 FPGA/ASIC 实现；电路论文要落到实测曲线和 SOTA 表；系统论文要落到端到端任务。
5. **图表是主线，不是装饰。** 第一批图负责讲架构和问题，后半部分图负责证明性能，最后的对比表负责回答“比别人强在哪里”。

## 常见章节模板
适合模仿的 TCAS-I 骨架如下：

```text
Title: 指明对象 + 方法/指标 + 应用场景
Abstract: 背景约束 -> gap -> proposed method -> key implementation -> measured/simulated results
I. Introduction:
  应用压力
  相关工作分组
  未满足的多目标约束
  Contributions
II. Background / Problem Formulation:
  标准、模型、符号、baseline 或设计约束
III. Proposed Method / Architecture:
  核心思想
  数学/电路/数据路径推导
  关键设计取舍
IV. Implementation:
  电路、版图、FPGA/ASIC、制造或测试设置
V. Results:
  功能验证
  指标曲线
  SOTA comparison table
VI. Conclusion:
  重申贡献、主要指标和适用边界
```

## 摘要的可套用顺序
可按下面顺序写：

1. 领域约束：某应用需要同时满足性能、能耗、面积、可靠性或可持续性。
2. 现有不足：已有方法在其中一两个指标上可以，但不能同时满足全部约束。
3. 本文方案：提出某算法、架构、拓扑、制造流程或系统。
4. 关键机制：用一句话说清楚方案为什么有效。
5. 结果：给 3-5 个最能打的指标和对比对象。

## 引言的写法套路
TCAS-I 的引言通常避免空泛口号。更有效的是：

- 第一段：应用趋势和硬约束，例如 5G 标准、nano-UAV 功耗、低压 ADC、电子废弃物。
- 第二段：已有路线分组，每组一句优点和一句代价。
- 第三段：提出“同时满足”问题，例如性能/复杂度、RF 响应/群时延、可靠性/CRP 利用率、供电灵活性/SNDR。
- 第四段：本文贡献，用编号列出，每条都对应后文一个章节或实验。

## 图表组织规律
- **架构图**：最好出现在方法开头，让读者先建立系统地图。
- **理论图/等效电路图**：用于证明方法不是经验调参。
- **测量曲线**：要把仿真和实测放在一起，展示偏差来源。
- **SOTA 表格**：最后集中比较关键指标，表头要选择能支撑本文贡献的指标。
- **实物/芯片/PCB/FPGA 图**：增强“真的做出来了”的可信度。

## 对自己投稿最有用的启发
1. 写贡献时不要只写“提出一种新方法”，要写“解决了哪组互相冲突的约束”。
2. 所有方法创新都要配一个指标闭环：算法有误码/复杂度，电路有实测，系统有端到端任务。
3. 对比表要提前设计，因为它反过来决定论文需要补哪些实验。
4. 摘要和 Introduction 里的每个强主张，都应该能在后文找到图、表或公式支撑。
5. Conclusion 不要新增卖点，只回收摘要中的承诺，并说明主要适用范围。

## 建议仿写模板
如果你要写 TCAS-I 风格论文，可以先填这几个句子：

```text
Existing [class of methods] can achieve [advantage], but they suffer from [limitation] when [application constraint].
To address this issue, this paper proposes [method/architecture], which [core mechanism].
The proposed design is implemented in/on [technology/platform] and evaluated using [measurement/simulation/task].
Compared with prior works, it achieves [metric 1], [metric 2], and [metric 3], while maintaining [constraint].
```

中文思路就是：先定义冲突约束，再给方法，再给实现，再给可比较指标。TCAS-I 论文的“高级感”大多来自这个闭环，而不是来自复杂措辞。
