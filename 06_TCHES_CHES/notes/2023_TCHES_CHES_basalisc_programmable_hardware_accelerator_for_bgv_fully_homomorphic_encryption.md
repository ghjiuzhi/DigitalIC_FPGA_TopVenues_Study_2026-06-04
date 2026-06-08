# paper_01 - BASALISC: Programmable Hardware Accelerator for BGV Fully Homomorphic Encryption

## 一句话定位
这篇 TCHES/CHES 论文围绕 **BASALISC: Programmable Hardware Accelerator for BGV Fully Homomorphic Encryption** 展开，核心是把一个明确的硬件/EDA/安全问题压缩成可实现、可度量、可对比的设计贡献。

## 为什么属于数字 IC / FPGA 方向
它针对 DNN、GEMM、systolic array、neuromorphic 或专用 workload 的硬件加速，属于 ASIC/FPGA 加速器方向。 本篇在 metadata 中标注的相关性是：digital IC / architecture。

## 摘要写法
摘要适合按“问题对象 -> proposed method/architecture -> implementation/evaluation -> quantitative comparison”组织。对这篇题目来说，第一句应点出 digital IC / architecture 的瓶颈，中间一句说明核心机制，最后用硬件指标或安全/精度指标收束 claim。

## Introduction 写法
Introduction 会先明确 adversary model 或 cryptographic workload，再定位现有防护/加速器不足。 这类题目最好把背景控制在 2-3 个层级：应用为什么重要、现有设计卡在哪里、本文为什么只解决这个窄 gap 也有价值。

## 方法/架构写法
方法写法从 workload 特征出发，解释数据复用、并行粒度、PE 阵列、片上存储、调度和数据流。 写作上要避免只描述模块名称，而要说明数据、控制、存储或安全假设如何穿过整个结构。

## 实验/测量写法
实验通常报告 throughput、latency、TOPS/W、resource/area、power、accuracy，并和 GPU/CPU/FPGA/ASIC SOTA 对比。 如果是工具或安全类论文，还要补充 benchmark、ablation、攻击成功率或鲁棒性分析。

## 图表套路
讲故事的图是 workload decomposition、PE array、dataflow、memory traffic breakdown 和 roofline/Pareto 图。 图表顺序通常应先让读者看懂架构，再让读者相信指标。

## 可模仿写法
可以模仿它的段落功能：先用一句话钉住硬件瓶颈，再用一张架构图解释贡献，最后用一张 SOTA 表把资源、性能、能效或安全性讲硬。投稿时不要把贡献写成泛泛的“提出一种方法”，而要写成“在某平台/某约束下改善某指标”。
