# TCAD 数字 IC / FPGA 写法总结

## 该 venue 偏好的问题类型
TCAD 偏 CAD/EDA、设计空间探索、可靠性、安全和硬件设计方法论，要求方法可推广。

## 摘要常见结构
摘要会明确输入、输出、优化目标和 QoR 改善。

## Introduction 常见结构
Introduction 要把现有工具链或设计流程的痛点说清，gap 常是 scalability、accuracy、runtime 或 robustness。

## 方法/架构常见结构
方法部分算法味更重，需要模型定义、约束、流程和复杂度/收敛性说明。

## 实验/测量常见结构
实验要有标准 benchmark、baseline、ablation、runtime 和 QoR 表。

## 对数字 IC / FPGA 投稿最有用的模仿模板
1. 用具体 workload、算子、单元、攻击模型或设计流程开场。
2. 明确现有方案在 area、power、frequency、latency、throughput、accuracy、security 或 runtime 上的瓶颈。
3. 用一张主架构图承载核心贡献，不让读者在文字里找系统结构。
4. 把结果写成“平台 + 指标 + baseline + 改善幅度”，并说明限制条件。
