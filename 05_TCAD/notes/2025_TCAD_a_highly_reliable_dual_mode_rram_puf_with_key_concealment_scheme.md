# paper_08 - A Highly Reliable Dual-Mode RRAM PUF With Key Concealment Scheme

## 一句话定位
这篇 TCAD 论文围绕 **A Highly Reliable Dual-Mode RRAM PUF With Key Concealment Scheme** 展开，核心是把一个明确的硬件/EDA/安全问题压缩成可实现、可度量、可对比的设计贡献。

## 为什么属于数字 IC / FPGA 方向
它面向密码算法、PQC/FHE、PUF、侧信道或故障攻击防护，核心贡献落在安全硬件、加速器或硬件安全验证。 本篇在 metadata 中标注的相关性是：memory / CIM。

## 摘要写法
摘要适合按“问题对象 -> proposed method/architecture -> implementation/evaluation -> quantitative comparison”组织。对这篇题目来说，第一句应点出 memory / CIM 的瓶颈，中间一句说明核心机制，最后用硬件指标或安全/精度指标收束 claim。

## Introduction 写法
Introduction 要把现有工具链或设计流程的痛点说清，gap 常是 scalability、accuracy、runtime 或 robustness。 这类题目最好把背景控制在 2-3 个层级：应用为什么重要、现有设计卡在哪里、本文为什么只解决这个窄 gap 也有价值。

## 方法/架构写法
方法一般先把算法/攻击模型拆成硬件瓶颈或泄漏路径，再给出算子架构、防护机制、传感器或评估流程。 写作上要避免只描述模块名称，而要说明数据、控制、存储或安全假设如何穿过整个结构。

## 实验/测量写法
实验既要有 area/latency/throughput/power，也要有安全指标，例如 attack success rate、leakage assessment、fault coverage 或 security level。 如果是工具或安全类论文，还要补充 benchmark、ablation、攻击成功率或鲁棒性分析。

## 图表套路
关键图包括 threat model、算子数据流、硬件架构、安全实验流程和 SOTA comparison table。 图表顺序通常应先让读者看懂架构，再让读者相信指标。

## 可模仿写法
可以模仿它的段落功能：先用一句话钉住硬件瓶颈，再用一张架构图解释贡献，最后用一张 SOTA 表把资源、性能、能效或安全性讲硬。投稿时不要把贡献写成泛泛的“提出一种方法”，而要写成“在某平台/某约束下改善某指标”。
