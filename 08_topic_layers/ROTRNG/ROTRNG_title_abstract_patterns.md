# ROTRNG Title and Abstract Patterns

这个文件专门服务 RO-TRNG/entropy-boundary 稿件，用来给标题、摘要、gap 和贡献句式找方向感。

## 标题关键词

可用关键词：

- `Ring-Oscillator TRNG`
- `Entropy-Source Boundary`
- `Sampler-Side Implementation`
- `Restart-Based Evaluation`
- `Measurement-Driven Characterization`
- `FPGA Implementation`
- `Jitter/Phase/Counterfactual Sampling`

慎用关键词：

- `Secure`：需要明确 attack model 和证据。
- `Certified`：需要完整认证流程。
- `Robust`：需要 PVT/attack/environment coverage。
- `Novel Architecture`：当前主线不是新架构。

## 标题候选结构

- `A Measurement-Driven Study of the Sampler-Side Boundary in FPGA Ring-Oscillator TRNGs`
- `Sampler-Side Implementation as a Measured Entropy-Source Boundary in FPGA RO-TRNGs`
- `Restart-Based Evidence for Sampler-Boundary Effects in FPGA Ring-Oscillator TRNG Evaluation`
- `Boundary-Aware Characterization of FPGA RO-TRNG Measurements`

这些只是结构样例。最终标题要以 `main.tex` 当前 claim 和 evidence table 为准。

## 摘要方向模板

`Ring-oscillator true random number generators are widely used in FPGA-based security systems because they can be built from digital resources. However, their evaluation often treats the sampler-side readout path as separate from the entropy source. This paper examines that assumption through [placement/restart/counterfactual/TDC evidence] on [platform]. The measurements show [bounded observation], indicating that [sampler-side implementation] should be included in [measured entropy-source boundary] under [conditions]. The study provides measurement evidence for boundary-aware RO-TRNG evaluation rather than a new certified TRNG architecture.`

## Gap 句式

- `Prior RO-TRNG designs optimize source structure and statistical quality, but they often leave the sampler-side measurement boundary implicit.`
- `Entropy-estimation and restart-test guidance clarifies how to evaluate outputs, but it does not by itself determine which physical blocks belong to the measured entropy source.`
- `Attack-oriented studies show that RO-TRNGs can be sensitive to external or implementation-level effects; this paper focuses on the internal measurement-boundary consequence of that sensitivity.`
- `The missing question is not whether RO-TRNGs can generate random bits, but whether the sampler-side implementation can be treated as outside the measured source.`

## 贡献句式

- `We frame sampler-side implementation as a measurement-boundary problem for FPGA RO-TRNG evaluation.`
- `We build an evidence chain that combines [methods] to test whether the sampler behaves as a passive readout stage.`
- `We report bounded measurements on [platform/setup] showing [observation], and discuss how this affects entropy-source evaluation.`
- `We clarify the scope and limitations of the evidence, including [platform/PVT/attack/certification boundaries].`
