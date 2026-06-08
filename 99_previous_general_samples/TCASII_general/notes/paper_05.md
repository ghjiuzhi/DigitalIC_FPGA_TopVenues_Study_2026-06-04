# paper_05 - A Cryo-CMOS Triple Tail Comparator With Capacitive Over-Neutralization

## 一句话定位
这篇分析低温 bulk CMOS 中 dopant freeze-out 引发 dynamic comparator hysteresis，并提出 triple-tail comparator 与 capacitive over-neutralization 进行抑制。

## 摘要写法
摘要先给出低温效应的物理根因：bulk resistance 在 4.2 K 附近大幅增加。随后说明由此产生 latch memory effect 和 hysteresis，再给统计表征方法与新 comparator 方案。

## Introduction 写法
引言从 quantum computing、粒子物理和低温探测等 Cryo-CMOS 需求出发，指出现有低温建模多关注 DC，而 ADC/comparator 的 transient effect 仍不足。

## 方法/架构写法
主体先解释 freeze-out 如何造成 hysteresis，再介绍测量方法和电路补偿结构。它的强点是把器件物理、统计测量和电路拓扑放在同一条逻辑线上。

## 实验/测量写法
实验强调低温下输入等效噪声、hysteresis 电压和新结构的抑制效果。低温电路 brief 的指标不多，但必须非常可信。

## 图表套路
图表包括 strongARM/comparator 拓扑、低温机理图、统计分布和测量曲线。读者需要先相信现象，再相信方案。

## 可模仿写法
器件效应驱动的电路 brief 可以学它：先把异常现象量化，再提出针对性结构，而不是先给电路再解释原因。
