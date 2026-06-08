# paper_08 - Physics-Informed Surrogate Neural Network for Pacemaker Energy Harvesting Interfaces

## 一句话定位
这篇用 physics-informed surrogate neural network 从二极管 V-I 特征快速预测 leadless pacemaker 能量采集 AC-DC 接口输出，辅助器件选择。

## 摘要写法
摘要先说明低功耗能量采集 AC-DC 接口对 ICLP 可靠供电的重要性。随后指出二极管 conduction loss 与 leakage loss 互相冲突，SPICE 模型不一定可用。本文用 PINN 直接从 datasheet 特征预测输出。

## Introduction 写法
引言从可穿戴、植入式和 IoT 小型能量采集需求进入，收窄到心脏 leadless pacemaker 的短脉冲低功率能量输入。gap 是传统仿真/原型筛选二极管太慢。

## 方法/架构写法
方法把物理约束写进神经网络训练，让模型不只是数据拟合。它的写法把 ML 当设计自动化工具，而不是单独 AI 论文。

## 实验/测量写法
结果强调毫秒级评估、真实案例精度和对自动化设计循环的适配。对比重点是速度和在无可靠 SPICE 模型时的可用性。

## 图表套路
图表包括接口电路、V-I 特征、网络框架、预测误差和设计空间筛选结果。图表要证明“快”和“准”同时成立。

## 可模仿写法
AI-for-circuits brief 可学它：不要泛泛说用神经网络，而要把输入特征、物理约束和电路设计决策明确绑定。
