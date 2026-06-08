# ROTRNG Gap Map

## 1. Entropy Boundary / Assurance

可写 gap：很多 TRNG 论文报告 NIST/Dieharder 等统计测试，但对 entropy boundary、health tests、conditioning 前后的可证明边界说明不足。

适合支撑：`RO_TRNG_entropy_boundary`。

## 2. Jitter / Phase Noise Modeling

可写 gap：近年 TCHES/TCAS-I 论文开始强调 phase noise、flicker noise、jitter model，但模型如何指导 FPGA/ASIC 实现选择仍可继续细化。

## 3. Metastability / Latch-Based Entropy

可写 gap：latched RO、jitter-latch、metastable-cell 方法有高吞吐潜力，但跨器件、跨布局、跨 PVT 的稳定边界需要更系统的测量。

## 4. PUF-TRNG Dual Use

可写 gap：PUF/TRNG dual-mode 设计能提高硬件复用，但安全目标、entropy 目标和 reproducibility 目标之间存在 tension。

## 5. Attack Robustness

可写 gap：频率注入、active attack、environment change 等攻击下，RO-TRNG 的防护和在线诊断还需要与硬件开销共同评估。

## 6. Measurement Methodology

可写 gap：很多论文给出单点测试结果，但测量协议、board/device repeatability、route/timing context 对结论影响很大。

适合支撑：`RO_TRNG_entropy_boundary` 和未来 `RO_TRNG_tvlsi_sampler_aperture`。
