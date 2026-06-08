# paper_06 - A Multi-GHz Inverter-Based ASDM With Distortion Cancellation

## 一句话定位
这篇提出完全基于 pseudo-digital inverter 的 asynchronous sigma-delta modulator，通过 delay-based 量化器和失真抵消实现多 GHz 运行。

## 摘要写法
摘要先说明 ASDM 架构和多 GHz 目标，再指出量化器和 loop filter 均使用 inverter 结构。核心卖点是用合适尺寸设计让 quantizer 非线性补偿 transconductor 非线性，最后给 CMOS 实测结果。

## Introduction 写法
引言先解释 ASDM 无需时钟、可将输入变成二值信号，适合 ADC 前端和 class-D 等场景。随后引出高速实现的主要瓶颈：环路非线性与量化器速度。

## 方法/架构写法
方法从 ASDM 基本原理讲起，再展开 pseudo-differential inverter cascade、Nauta transconductor 和 distortion cancellation。Brief 写法很紧：每个电路块只保留最必要解释。

## 实验/测量写法
实验给频率、工艺、振荡范围、失真/线性度和功耗等指标。电路 brief 需要用少量关键测量图快速证明“真的快、且失真被控制”。

## 图表套路
图表包括 ASDM 框图、inverter-based 电路、频谱/输出波形和性能表。图表围绕一个问题：高速 inverter 化是否损害线性。

## 可模仿写法
短电路论文可学它的聚焦：围绕一个结构创新和一个补偿机制展开，不分散到太多应用。
