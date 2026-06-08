# TCAS-I 数字 IC / FPGA 写法总结

## 该 venue 偏好的问题类型
TCAS-I 喜欢完整电路/系统闭环：不仅要有新结构，还要有理论分析、实现细节和充分验证。

## 摘要常见结构
摘要常按“应用瓶颈-核心架构-关键指标-SOTA 对比”写，指标密度高。

## Introduction 常见结构
Introduction 通常铺得比 brief 更完整：背景、痛点、gap、贡献列表，再解释系统级意义。

## 方法/架构常见结构
方法部分强调电路/系统/算法协同，公式、框图、电路细节和设计取舍要互相支撑。

## 实验/测量常见结构
实验部分要求仿真、实测或 FPGA/ASIC 实现结果形成闭环，并用 SOTA 表证明位置。

## 对数字 IC / FPGA 投稿最有用的模仿模板
1. 用具体 workload、算子、单元、攻击模型或设计流程开场。
2. 明确现有方案在 area、power、frequency、latency、throughput、accuracy、security 或 runtime 上的瓶颈。
3. 用一张主架构图承载核心贡献，不让读者在文字里找系统结构。
4. 把结果写成“平台 + 指标 + baseline + 改善幅度”，并说明限制条件。
