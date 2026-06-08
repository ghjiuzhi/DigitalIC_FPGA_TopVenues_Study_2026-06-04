# paper_03 - A Heterogeneous RISC-V Based SoC for Secure Nano-UAV Navigation

## 一句话定位
这篇 TCAS-I 论文围绕 **A Heterogeneous RISC-V Based SoC for Secure Nano-UAV Navigation** 展开，核心是把一个明确的硬件/EDA/安全问题压缩成可实现、可度量、可对比的设计贡献。

## 为什么属于数字 IC / FPGA 方向
它关注处理器、SoC、RISC-V、ISA 扩展或微架构，是数字 IC 系统架构和硬件/软件协同方向。 本篇在 metadata 中标注的相关性是：digital IC / architecture。

## 摘要写法
摘要适合按“问题对象 -> proposed method/architecture -> implementation/evaluation -> quantitative comparison”组织。对这篇题目来说，第一句应点出 digital IC / architecture 的瓶颈，中间一句说明核心机制，最后用硬件指标或安全/精度指标收束 claim。

## Introduction 写法
Introduction 通常铺得比 brief 更完整：背景、痛点、gap、贡献列表，再解释系统级意义。 这类题目最好把背景控制在 2-3 个层级：应用为什么重要、现有设计卡在哪里、本文为什么只解决这个窄 gap 也有价值。

## 方法/架构写法
方法写作会先定义 workload 或 ISA/接口，再展开 datapath、控制、存储层次、互连和软件调用路径。 写作上要避免只描述模块名称，而要说明数据、控制、存储或安全假设如何穿过整个结构。

## 实验/测量写法
实验要同时报告 microbenchmark 和 application-level 结果，常用 IPC、cycles、frequency、area、power、speedup 和能效来证明系统价值。 如果是工具或安全类论文，还要补充 benchmark、ablation、攻击成功率或鲁棒性分析。

## 图表套路
图表通常包括 SoC block diagram、pipeline/vector lane 结构、memory hierarchy、benchmark breakdown 和 normalized comparison。 图表顺序通常应先让读者看懂架构，再让读者相信指标。

## 可模仿写法
可以模仿它的段落功能：先用一句话钉住硬件瓶颈，再用一张架构图解释贡献，最后用一张 SOTA 表把资源、性能、能效或安全性讲硬。投稿时不要把贡献写成泛泛的“提出一种方法”，而要写成“在某平台/某约束下改善某指标”。
