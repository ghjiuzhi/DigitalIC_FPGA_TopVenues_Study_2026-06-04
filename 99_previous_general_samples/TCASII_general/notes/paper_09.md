# paper_09 - TNNGen: Automated Design of Neuromorphic Sensory Processing Units

## 一句话定位
这篇提出 TNNGen，从 PyTorch temporal neural network 模型自动生成面向时间序列聚类的 neuromorphic sensory processing unit 后布局网表。

## 摘要写法
摘要先介绍 TNN 作为 SNN 特殊类别，依赖 spike timing 信息处理。随后指出近期 TNN 硬件设计依赖手工流程且缺少开源功能仿真框架。本文贡献是自动化设计 flow，从模型到 netlist。

## Introduction 写法
引言从 DNN 能耗问题和 TNN 的生物启发优势切入，快速收窄到设计自动化缺口。Brief 的引言包含 background，因为读者未必熟悉 TNN。

## 方法/架构写法
方法围绕 flow 展开：软件模型、功能仿真、macro/微架构映射和 physical design。它强调自动化而非单个算子优化。

## 实验/测量写法
实验给 post-layout 7 nm 面积、功耗、延迟等结果，说明自动生成设计仍然有竞争力。结果也服务于“flow 可行性”。

## 图表套路
图表包括 flow diagram、TNN 架构、benchmark 表和后布局指标。自动化论文必须让流程图承担主图功能。

## 可模仿写法
EDA/自动化 brief 可以学它：贡献不是某个最优电路，而是减少人工设计成本，因此结果要同时报质量和流程效率。
