# paper_10 - A Lightweight and Hardware-Efficient NTT FPGA Accelerator for FHE Applications

## 一句话定位
这篇针对 FHE 中 NTT/INTT 的存储和乘法开销，提出 compact MDC 架构、twiddle factor generator 和 DSP-efficient multiplier。

## 摘要写法
摘要先说明 NTT/INTT 是 FHE 多项式乘法核心。随后给出两个具体优化：只存初始阶段 twiddle factor、后续在线生成，以及非标准 tiling 的乘法器。最后用 97.2% memory saving 和 ATP/TPE 对比收束。

## Introduction 写法
引言从 FHE/PQC 的 polynomial multiplication 瓶颈进入，解释 NTT 将复杂度从平方级降到 n log n。接着比较 SDF/MDC 架构的性能/资源取舍，顺势引出存储优化。

## 方法/架构写法
方法部分压缩但清楚：NTT pipeline、MDC 数据流、TFG、乘法器映射。每个模块都对一个硬件代价负责，逻辑链很硬。

## 实验/测量写法
结果以 FPGA 资源、memory、DSP、ATP、TPE 和文献对比为核心。密码硬件 brief 强依赖表格，因为速度、面积和存储都要一起看。

## 图表套路
图表包括 NTT 架构、TFG 机制、乘法器结构和 SOTA 对比表。主图要解释为什么能省存储而不牺牲吞吐。

## 可模仿写法
加速器 brief 可模仿它的“瓶颈资源命名”：明确说本文省的是 memory、DSP 还是 latency，再围绕这个资源组织整篇。
