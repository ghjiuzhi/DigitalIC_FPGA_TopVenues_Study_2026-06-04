# paper_06 - A Lightweight and Hardware-Efficient NTT FPGA Accelerator for FHE Applications

## 一句话定位
这篇 TCAS-II 论文围绕 **A Lightweight and Hardware-Efficient NTT FPGA Accelerator for FHE Applications** 展开，核心是把一个明确的硬件/EDA/安全问题压缩成可实现、可度量、可对比的设计贡献。

## 为什么属于数字 IC / FPGA 方向
它直接围绕 FPGA 上的结构映射、资源占用、时延、吞吐或可靠性展开，是数字硬件实现论文的典型样本。 本篇在 metadata 中标注的相关性是：FPGA cryptographic accelerator / FHE。

## 摘要写法
摘要适合按“问题对象 -> proposed method/architecture -> implementation/evaluation -> quantitative comparison”组织。对这篇题目来说，第一句应点出 FPGA cryptographic accelerator / FHE 的瓶颈，中间一句说明核心机制，最后用硬件指标或安全/精度指标收束 claim。

## Introduction 写法
Introduction 快速收束 gap，贡献列表短而硬，避免写成长综述。 这类题目最好把背景控制在 2-3 个层级：应用为什么重要、现有设计卡在哪里、本文为什么只解决这个窄 gap 也有价值。

## 方法/架构写法
方法通常从算法或数据流开始，落到 PE/流水线/存储组织/控制逻辑，再说明定点位宽、并行度、资源复用和时序收敛取舍。 写作上要避免只描述模块名称，而要说明数据、控制、存储或安全假设如何穿过整个结构。

## 实验/测量写法
实验最看重 FPGA 型号、综合/实现工具、LUT/FF/DSP/BRAM、frequency、latency、throughput、power，以及和已有 FPGA/ASIC 方案的归一化对比。 如果是工具或安全类论文，还要补充 benchmark、ablation、攻击成功率或鲁棒性分析。

## 图表套路
最有用的图是 top-level architecture、dataflow、pipeline timing、memory banking 和 resource/performance table。 图表顺序通常应先让读者看懂架构，再让读者相信指标。

## 可模仿写法
可以模仿它的段落功能：先用一句话钉住硬件瓶颈，再用一张架构图解释贡献，最后用一张 SOTA 表把资源、性能、能效或安全性讲硬。投稿时不要把贡献写成泛泛的“提出一种方法”，而要写成“在某平台/某约束下改善某指标”。
