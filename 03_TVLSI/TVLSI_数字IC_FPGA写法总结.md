# TVLSI 数字 IC / FPGA 写法总结

## 该 venue 偏好的问题类型
TVLSI 更偏 VLSI 架构、实现和可扩展性，重视真实硬件约束下的系统级表现。

## 摘要常见结构
摘要会明确硬件平台、实现规模和性能/能效提升。

## Introduction 常见结构
Introduction 通常从 workload 和 VLSI bottleneck 写起，再强调现有硬件在可扩展、带宽或能效上的不足。

## 方法/架构常见结构
方法要把微架构、数据流、存储层次、并行度和实现限制讲清楚。

## 实验/测量常见结构
实验偏 implementation report 和 workload benchmark，SOTA 表是核心证据。

## 对数字 IC / FPGA 投稿最有用的模仿模板
1. 用具体 workload、算子、单元、攻击模型或设计流程开场。
2. 明确现有方案在 area、power、frequency、latency、throughput、accuracy、security 或 runtime 上的瓶颈。
3. 用一张主架构图承载核心贡献，不让读者在文字里找系统结构。
4. 把结果写成“平台 + 指标 + baseline + 改善幅度”，并说明限制条件。
