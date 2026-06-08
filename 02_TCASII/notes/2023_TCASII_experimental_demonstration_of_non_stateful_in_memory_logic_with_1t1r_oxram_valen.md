# paper_02 - Experimental Demonstration of Non-Stateful In-Memory Logic With 1T1R OxRAM Valence Change Mechanism Memristors

## 一句话定位
这篇 TCAS-II 论文围绕 **Experimental Demonstration of Non-Stateful In-Memory Logic With 1T1R OxRAM Valence Change Mechanism Memristors** 展开，核心是把一个明确的硬件/EDA/安全问题压缩成可实现、可度量、可对比的设计贡献。

## 为什么属于数字 IC / FPGA 方向
它围绕 SRAM/MRAM/RRAM/CAM/CIM/PIM、memristor 或近存计算，属于数字存储、存算融合或新型计算电路。 本篇在 metadata 中标注的相关性是：in-memory logic / digital computing。

## 摘要写法
摘要适合按“问题对象 -> proposed method/architecture -> implementation/evaluation -> quantitative comparison”组织。对这篇题目来说，第一句应点出 in-memory logic / digital computing 的瓶颈，中间一句说明核心机制，最后用硬件指标或安全/精度指标收束 claim。

## Introduction 写法
Introduction 快速收束 gap，贡献列表短而硬，避免写成长综述。 这类题目最好把背景控制在 2-3 个层级：应用为什么重要、现有设计卡在哪里、本文为什么只解决这个窄 gap 也有价值。

## 方法/架构写法
方法通常从 cell/array/bitline 或 matchline 行为写起，再说明 sensing、读写时序、外围电路和系统级映射。 写作上要避免只描述模块名称，而要说明数据、控制、存储或安全假设如何穿过整个结构。

## 实验/测量写法
实验需要电路仿真或实测、PVT/Monte Carlo、能耗、延迟、面积、误码/稳定性，以及阵列规模扩展讨论。 如果是工具或安全类论文，还要补充 benchmark、ablation、攻击成功率或鲁棒性分析。

## 图表套路
关键图是 cell/array schematic、operation timing、waveform、distribution plot 和 area-energy-delay 对比表。 图表顺序通常应先让读者看懂架构，再让读者相信指标。

## 可模仿写法
可以模仿它的段落功能：先用一句话钉住硬件瓶颈，再用一张架构图解释贡献，最后用一张 SOTA 表把资源、性能、能效或安全性讲硬。投稿时不要把贡献写成泛泛的“提出一种方法”，而要写成“在某平台/某约束下改善某指标”。
