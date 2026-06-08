# Experiment and Result Writing Patterns

## 实验设置节

顶刊实验设置通常先保护可复现性：平台、工具、参数、样本、测量流程、baseline。它不急着解释结果。

审查问题：

- 平台和样本是否写清？
- baseline 是否公平？
- 控制变量是否明确？
- 统计口径是否统一？

## 结果节

顶刊结果节通常按 claim 排：

1. 先给能建立问题存在的结果。
2. 再给核心机制或方法有效性的结果。
3. 再给对比、消融、控制实验。
4. 最后给 SOTA 或 traceability。

每个结果块推荐四句：

- Setup：在什么条件下测。
- Observation：看到什么。
- Interpretation：它支撑哪个 claim。
- Boundary：它不说明什么。

## 表格密度控制

主文表格只保留会改变审稿人判断的证据。repeat、archive、traceability、toolflow sensitivity 可以保留在主文，但必须明确为什么它不是补充材料。

## RO-TRNG 当前稿件审查点

- Placement 是前置证据，不是最终 novelty。
- Restart/Warmup 说明 continuous-stream balance 不够。
- Sampler-side counterfactual 是核心边界测试。
- TDC 是 mechanism diagnostic，不是完整物理模型。
- Reduced-XOR 解释 final all64 能隐藏内部偏置。
