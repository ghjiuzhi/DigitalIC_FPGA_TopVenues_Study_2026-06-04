# Figure and Table Review Guide

这个文件用来审查图表。核心原则：图表不是装饰，而是 claim 的证据入口。

## 一张好图应该回答什么

每张图至少回答一个问题：

- 它解释系统边界吗？
- 它解释实验流程吗？
- 它支撑某个结果 claim 吗？
- 它比较本文和 prior work 的差异吗？
- 它暴露 limitation 吗？

如果一张图只能说明“我们也做了这个”，但不支撑 claim，就考虑删除、合并或放到 appendix。

## 当前 RO-TRNG 稿件推荐图表链

1. Boundary overview figure  
   画清 RO entropy source、sampler、counter/post-processing、measurement interface。用颜色或虚线标出本文争论的 measured entropy-source boundary。

2. Experimental protocol figure/table  
   说明 board、clock/reset、restart procedure、placement strategy、sample size、measurement scripts。这个表保护你的可复现性。

3. Placement/restart evidence figure  
   显示 physical implementation 和 restart behavior 改变观测结果。caption 要写清不是 universal FPGA claim。

4. Counterfactual sampler evidence figure/table  
   比较 sampler-side 改动前后结果。它是本文 boundary claim 的核心图表之一。

5. TDC/jitter proxy 或 reduced-XOR evidence  
   用来补强 mechanism 解释，避免只停留在统计现象。

6. Related-work/SOTA coverage table  
   列：work、venue/year、source type、platform、restart evidence、sampler boundary、attack/environment、limitation、relation to this paper。

7. Limitation table 或 paragraph  
   主动说明 platform、PVT、样本、测试标准、未覆盖 attack model。

## Caption 审查模板

每个 caption 应尽量包含：

`[What is measured] under [setup]. The result supports [claim] by showing [observable]. It does not imply [larger unsupported claim].`

例：

`Restart measurements under fixed placement show repeatable changes in the observed RO-TRNG output. The result supports the sampler-boundary claim by linking the readout path to measured behavior; it does not establish a universal FPGA-family entropy model.`

## 图表删改规则

删除：

- 只重复正文文字的图。
- 没有单位、setup、sample size 的结果图。
- 和主 claim 无关的“看起来不错”的统计图。

合并：

- 多张只展示同一变量不同 case 的图。
- 多个小表都在说明同一类 setup。

补充：

- 缺少 boundary overview。
- 缺少 SOTA coverage table。
- 缺少 limitation 或 scope 表述。
