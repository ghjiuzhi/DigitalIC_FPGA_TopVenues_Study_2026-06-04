# TCAS-II 数字 IC / FPGA 写法总结

## 该 venue 偏好的问题类型
TCAS-II 偏短平快的 express contribution：一个算子、一个单元、一个 sensing scheme 或一个紧凑架构即可成文。

## 摘要常见结构
摘要不宜铺陈，直接给问题、方案和最关键的 2-3 个数字。

## Introduction 常见结构
Introduction 快速收束 gap，贡献列表短而硬，避免写成长综述。

## 方法/架构常见结构
方法部分用一张主框图加少量公式说明机制，突出“为什么这个结构更省/更快/更稳”。

## 实验/测量常见结构
实验以表格为核心，重点证明局部创新带来的资源、时延、能耗或安全收益。

## 对数字 IC / FPGA 投稿最有用的模仿模板
1. 用具体 workload、算子、单元、攻击模型或设计流程开场。
2. 明确现有方案在 area、power、frequency、latency、throughput、accuracy、security 或 runtime 上的瓶颈。
3. 用一张主架构图承载核心贡献，不让读者在文字里找系统结构。
4. 把结果写成“平台 + 指标 + baseline + 改善幅度”，并说明限制条件。
