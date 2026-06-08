# Title, Abstract, and Number Review Sheet

这个文件是下一轮改稿的审查表。改完标题和摘要后，逐项打勾。

## 标题审查

- 是否包含对象：RO-TRNG、entropy source、sampler-side implementation。
- 是否包含机制：restart、placement、counterfactual sampler、measurement-driven characterization。
- 是否包含边界：measured entropy-source boundary、sampler boundary、evaluation boundary。
- 是否最多使用 2 个核心修饰词。
- 每个修饰词是否能被正文 evidence 支撑。
- 是否避免 `novel`、`secure`、`robust`、`certified` 这类高风险词。

## 摘要审查

摘要 6 句功能：

1. 背景：对象为什么重要。
2. 问题：现有假设或做法哪里不够。
3. 方法：本文怎么解决。
4. 创新：核心机制或实验设计是什么。
5. 数字：最强 2-4 个结果。
6. 边界：本文 claim 到哪里为止。

检查点：

- 第一二句是否足够快地进入问题。
- 问题是否具体到 sampler-side measurement boundary。
- 方法是否不是泛泛 `we analyze`，而是列出 evidence chain。
- 数字是否来自正文表/图。
- 数字单位、小数位、字体是否统一。
- 最后一句是否避免过大 claim。

## 数字格式审查

同类数字：

- 小数位统一。
- 单位统一。
- 百分比统一。
- 不混用 `20.8 $\mu$W`、`20.8-μW`、`\SI{20.8}{\micro\watt}`。

推荐：

- 正文用 `siunitx`。
- 表格数值统一有效数字。
- 标题中只放最有卖点、最稳定的数字。
- 摘要中只放能支撑主 claim 的数字，不放边角结果。

## 句式审查

保留：

- `This paper examines...`
- `We characterize...`
- `The measurements indicate...`
- `Under the evaluated setup...`

替换：

- `prove` -> `indicate` 或 `show`
- `guarantee` -> `support`
- `secure` -> `security-relevant` 或删除
- `certified` -> `evaluated under...` 或删除
- `universal` -> `under the evaluated setup`
