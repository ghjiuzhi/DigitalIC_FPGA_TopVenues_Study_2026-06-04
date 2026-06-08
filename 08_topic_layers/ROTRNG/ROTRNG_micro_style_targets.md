# ROTRNG Micro Style Targets

这个文件把顶刊微观写法转成当前 RO-TRNG 方向稿件的具体目标。

## 本稿标题目标

标题应该让审稿人看到：

- 本文对象：FPGA RO-TRNG。
- 本文机制：sampler-side implementation、restart-based evaluation、measurement evidence。
- 本文 claim：measured entropy-source boundary。

优先候选风格：

1. `Sampler-Side Implementation as a Measured Entropy-Source Boundary in FPGA RO-TRNGs`
2. `Restart-Based Evidence for Sampler-Boundary Effects in FPGA RO-TRNG Evaluation`
3. `A Measurement-Driven Characterization of Sampler-Side Boundary Effects in FPGA RO-TRNGs`

不建议：

- `A Novel Secure RO-TRNG...`
- `A Robust FPGA TRNG...`
- `Study on Randomness...`

## 本稿摘要目标

推荐摘要骨架：

1. Background：FPGA RO-TRNG 为什么重要。
2. Problem：现有评估把 sampler/readout 当成边界外部，restart 测量下这个假设不稳。
3. Method：placement、restart、counterfactual sampler、TDC/reduced-XOR 构成 evidence chain。
4. Innovation：不是新 TRNG，而是 measurement-boundary framing。
5. Numbers：放最强结果，统一小数位和单位。
6. Claim：sampler-side implementation should be considered inside the measured entropy-source boundary under the evaluated setup。

## 本稿 Introduction 目标

段落 1：FPGA RO-TRNG 在安全系统中的用途。

段落 2：RO-TRNG 评估依赖物理实现和采样路径，不只是逻辑电路。

段落 3：已有工作覆盖架构、统计测试、熵估计、攻击、PUF/TRNG，但没有直接回答 sampler-side boundary。

段落 4：本文把问题定义为 measurement-boundary problem。

段落 5：贡献列表，最多 3 条。

## 本稿数字目标

- 不为了“顶刊感”硬塞数字进标题。
- 摘要数字只放最能支撑 boundary claim 的结果。
- 所有数字回查 `claim_evidence_table.md`。
- 小数位由证据精度决定，不要为了显得精确而保留多位。

## 本稿用词目标

推荐：

- `measurement-boundary`
- `sampler-side implementation`
- `restart-based evaluation`
- `counterfactual sampler evidence`
- `under the evaluated FPGA setup`
- `indicates that`

避免：

- `certifies`
- `proves randomness`
- `secure TRNG`
- `universal behavior`
- `all FPGA families`
