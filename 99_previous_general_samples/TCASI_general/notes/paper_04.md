# paper_04 - A High-Reliability, Non-CRP-Discard Arbiter PUF Based on Delay Difference Quantization

## 一句话定位
这篇针对 FPGA 上 Arbiter PUF 可靠性差的问题，提出 delay difference quantization 机制，在不丢弃 challenge-response pair 的前提下提高稳定性和抗攻击能力。

## 摘要写法
摘要先定义 PUF 的 IoT 身份认证价值，再指出 APUF 在 FPGA 实现中可靠性差。本文贡献用“非丢弃 CRP、量化延迟差、可靠性提升、ML attack resistance”组织，最后用实验指标证明安全与可用性。

## Introduction 写法
引言从轻量级硬件安全和 IoT 资源限制出发，回顾 APUF、XOR-APUF、helper data 或 CRP discard 等方案。gap 很明确：很多提升可靠性的方式会降低 CRP 利用率或引入额外成本。

## 方法/架构写法
方法部分先解释传统 APUF 的不稳定来源，再引入 delay difference quantization，把模拟/延迟差异转成更稳健的判决信息。架构说明强调它如何嵌入 FPGA 资源，以及为什么不必丢弃不稳定 CRP。

## 实验/测量写法
实验围绕可靠性、唯一性、随机性、资源消耗、误码率和机器学习攻击展开。TCAS-I 的安全硬件论文通常会同时给“功能指标”和“攻击场景”，否则审稿人会觉得只证明了电路能跑。

## 图表套路
常见图包括 PUF 架构、延迟差分布、BER/可靠性曲线、资源表、与已有 PUF 的对比表。安全论文的对比表会特别密，因为需要同时说服硬件和安全两类读者。

## 可模仿写法
可模仿它的 gap 表述：先承认已有方法有效，再指出代价不可接受，然后把新方法包装成“保留优点、去掉代价”的折中设计。
