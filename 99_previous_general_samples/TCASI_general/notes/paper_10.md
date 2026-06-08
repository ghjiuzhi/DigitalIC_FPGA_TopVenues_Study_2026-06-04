# paper_10 - A Supply-Voltage-Flexible Third-Order Passive Delta-Sigma Modulator

## 一句话定位
这篇设计 4 MHz 带宽三阶离散时间无源 Delta-Sigma 调制器，通过 switched-capacitor loop filter 和 amplifier-less 架构实现 0.4-0.9 V 供电灵活性与 71.9 dB peak SNDR。

## 摘要写法
摘要直接给出核心指标：供电范围、阶数、带宽、无源结构和 peak SNDR。随后说明为什么无源 loop filter 带来供电/时钟灵活性，也带来 quantizer noise 与 loop response 设计挑战。最后用实际设计结果证明这些挑战被处理。

## Introduction 写法
引言围绕低电压 ADC 的问题展开：有源放大器在低压下线性、增益和功耗都困难。gap 写法非常电路化：无源 Delta-Sigma 有潜力，但缺少可综合、可解释、带宽和 SNDR 足够好的实现。

## 方法/架构写法
方法部分先剖析 passive Delta-Sigma modulator 的两个关键挑战，再提出 loop filter、quantizer、SC 实现和系统参数选择。它不是只给最终电路，而是解释“为什么这样选”。

## 实验/测量写法
实验重点是 SNDR、带宽、供电范围、功耗、FoM、频谱和与 ADC SOTA 的对比。TCAS-I ADC 论文的结果表通常会非常密集，审稿人会从 FoM/带宽/工艺/面积/供电同时判断贡献。

## 图表套路
图表包括系统框图、loop filter/SC 电路、噪声或传递函数分析、芯片/测试设置、输出频谱和 SOTA 表格。ADC 图表的核心是让指标来源可追溯。

## 可模仿写法
写 ADC 论文时可模仿它的“挑战先行”结构：先把无源方案的硬伤讲出来，再逐个解决，最后用测量指标证明不是概念设计。
