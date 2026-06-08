# 审稿人检查表

## Claim 与证据
- 每个 abstract/conclusion 里的强 claim 是否有表格或图支撑。
- 是否避免了“best”、“first”、“optimal”等无法完全证明的词。
- 是否说明结果只在某 FPGA、工艺、benchmark、参数范围内成立。

## Baseline 与公平比较
- baseline 是否包含最近 3-5 年同类顶刊/会议。
- FPGA/ASIC/CPU/GPU 是否分开比较或解释归一化。
- 是否报告工具版本、频率约束、位宽、数据集、参数。

## 实现真实性
- 是否给出 resource/area、frequency、latency、throughput、power/energy。
- FPGA 是否说明器件型号；ASIC 是否说明工艺、面积、后端或仿真层级。
- 只做模型仿真时，是否避免声称 silicon-level conclusion。

## Related Work
- 是否按技术路线比较，而不是按年份流水账。
- 是否明确你的方法相对每类 prior work 的不同假设。
- 是否能从 related work 自然推出 gap。

## 图表
- 第一张图是否能讲清系统边界。
- SOTA 表是否有 normalized metric。
- 是否有 ablation 或 sensitivity 证明设计选择。

## 安全/密码方向额外检查
- threat model 是否明确。
- 安全指标和硬件开销是否同时报告。
- 是否说明剩余风险和攻击/防护假设。
