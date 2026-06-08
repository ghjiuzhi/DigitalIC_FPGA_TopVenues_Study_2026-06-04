# paper_03 - A 380 fW Leakage Data Retention Flip-Flop for Short Sleep Periods

## 一句话定位
这篇 TCAS-II 论文围绕 **A 380 fW Leakage Data Retention Flip-Flop for Short Sleep Periods** 展开，核心是把一个明确的硬件/EDA/安全问题压缩成可实现、可度量、可对比的设计贡献。

## 为什么属于数字 IC / FPGA 方向
它的问题和评价指标落在硬件架构、数字电路实现、系统级验证或硬件安全/可靠性上，和数字 IC/FPGA 投稿方向相关。 本篇在 metadata 中标注的相关性是：digital standard-cell / flip-flop。

## 摘要写法
摘要适合按“问题对象 -> proposed method/architecture -> implementation/evaluation -> quantitative comparison”组织。对这篇题目来说，第一句应点出 digital standard-cell / flip-flop 的瓶颈，中间一句说明核心机制，最后用硬件指标或安全/精度指标收束 claim。

## Introduction 写法
Introduction 快速收束 gap，贡献列表短而硬，避免写成长综述。 这类题目最好把背景控制在 2-3 个层级：应用为什么重要、现有设计卡在哪里、本文为什么只解决这个窄 gap 也有价值。

## 方法/架构写法
方法通常先定义系统约束，再给出 architecture/circuit/protocol，并说明关键设计取舍。 写作上要避免只描述模块名称，而要说明数据、控制、存储或安全假设如何穿过整个结构。

## 实验/测量写法
实验围绕可量化指标展开：面积、功耗、频率、延迟、吞吐、准确性、鲁棒性或安全性。 如果是工具或安全类论文，还要补充 benchmark、ablation、攻击成功率或鲁棒性分析。

## 图表套路
图表承担从问题到结果的叙事：系统框图、关键模块图、波形/流程图和对比表。 图表顺序通常应先让读者看懂架构，再让读者相信指标。

## 可模仿写法
可以模仿它的段落功能：先用一句话钉住硬件瓶颈，再用一张架构图解释贡献，最后用一张 SOTA 表把资源、性能、能效或安全性讲硬。投稿时不要把贡献写成泛泛的“提出一种方法”，而要写成“在某平台/某约束下改善某指标”。
