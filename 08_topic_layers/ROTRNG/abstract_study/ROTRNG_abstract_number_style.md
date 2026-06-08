# ROTRNG Abstract Number Style

## 摘要里该放什么数字

只放能支撑主 claim 的 2-4 个数字。RO-TRNG 当前稿件优先考虑：

- 一个 continuous-stream 对比数字，用来说明 placement sensitivity。
- 一个 restart/warmup boundary 数字，用来说明 continuous balance 不够。
- 一个 sampler-side counterfactual 数字，用来支撑核心 boundary claim。
- 一个 control/diagnostic 数字，只有在它显著降低替代解释时才放。

## 小数位

- `$p_1$` 建议统一 4-6 位，但摘要里可减少到 4 位左右，除非差异非常小。
- min-entropy 摘要里不应放太多位，通常 3-4 位有效数字足够。
- warmup 数字是离散参数，保持整数。
- correlation 或 diagnostic threshold 不宜放过多，除非它是核心反证。

## 字体和 LaTeX

- 如果写 `$p_1=0.337316$`，全文同类表达都使用 math mode。
- 单位类数字使用 `\SI{}` 或统一文本写法，不混用。
- 摘要避免 `3.14355\times 10^{-5}` 这类精细数字，除非它是核心 claim。

## 当前稿件风险

当前摘要数字密度偏高。下一轮应把结果分为：

- abstract keeper：主 claim 需要的代表数字。
- result-only：细节表格数字。
- remove/rephrase：不改变摘要结论的辅助数字。
