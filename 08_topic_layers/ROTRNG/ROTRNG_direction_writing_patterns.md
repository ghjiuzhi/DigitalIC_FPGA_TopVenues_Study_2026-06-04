# ROTRNG Direction Writing Patterns

这个文件总结 ROTRNG/TRNG/PUF/entropy-source 方向论文常见写法。它服务于模仿“方向叙事”，不是替代逐篇阅读。

## 方向论文通常怎么立题

ROTRNG 相关论文很少只说“随机数更好”。它们通常围绕四个边界展开：

- Source boundary：随机性来自 RO、latch、PLL、TERO、metastability 还是组合结构。
- Sampling boundary：采样器、计数器、reset/restart、readout 是否只是观察者，还是会改变被测行为。
- Evaluation boundary：用 min-entropy、restart test、NIST tests、health tests、statistical tests 证明什么，不证明什么。
- Security boundary：frequency injection、environmental manipulation、aging/PVT、side-channel 或 active attacks 覆盖到哪里。

当前稿件最适合落在 sampling boundary + evaluation boundary，而不是 source architecture。

## 常见 Introduction 路线

1. 安全系统需要高质量随机数，FPGA RO-TRNG 易实现。
2. RO-TRNG 输出受物理实现、采样、重启、环境影响。
3. 既有工作分别研究架构、熵估计、攻击、PUF/TRNG 复用、标准测试。
4. 但如果 sampler/restart/measurement path 会影响观测结果，那么 entropy-source boundary 不能只按逻辑模块划。
5. 本文用测量证据链说明某个 boundary 需要被重新纳入评估。

## 方法部分常见写法

ROTRNG 方向方法部分一般不只给电路图，还要给 evaluation contract：

- 系统框图：RO、sampler、conditioning、readout、measurement point。
- 参数表：RO 数量、stage、clock/reset、sample length、board/FPGA、placement。
- 实验协议：restart、temperature/voltage/frequency、seed/placement、采样窗口。
- 统计方法：min-entropy、NIST、restart evidence、correlation、bias、throughput。
- 安全或扰动：injection、environment、PUF stability，若没做要写 limitation。

## 实验部分常见写法

实验一般按 claim 排，不按数据生成顺序排：

- Claim 1：物理实现会影响输出。给 placement/restart 证据。
- Claim 2：采样器不是纯 readout。给 counterfactual sampler 或替代 sampler 证据。
- Claim 3：机制解释合理。给 TDC、jitter proxy、phase relation 或 reduced-XOR 证据。
- Claim 4：和 prior work 的关系。给 SOTA/coverage table，不只比 throughput。
- Limitation：说明平台、PVT、攻击模型、认证边界。

## 当前稿件应模仿什么

要模仿：

- 把问题缩到一个可证的 boundary。
- 用多种测量证据互相支撑。
- 对 claim 主动加边界。
- 把 standards/security 作为 context，而不是无证据地宣称合规或抗攻击。

不要模仿：

- 只用 NIST pass/fail 当随机性证明。
- 只比吞吐、面积、功耗，忽略 measurement methodology。
- 只说“novel architecture”，但证据实际上是测量现象。
