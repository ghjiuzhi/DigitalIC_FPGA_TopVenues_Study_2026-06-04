# Number, Unit, and Symbol Style Guide

## 为什么数字字体会不一样

LaTeX 中 `$0.337316$` 是 math font，`0.337316` 是 text font，`\SI{0.337316}{}` 又由 siunitx 控制。混用会让摘要和正文数字看起来不一致。

## 推荐规则

- 普通测量数字统一用文本或 `siunitx`，不要一部分 math mode、一部分 text mode。
- 有变量名时变量进 math mode：`$p_1=0.337316$` 可以接受，但同类写法要统一。
- 单位用 `\SI{10}{\mebi\byte}` 或项目统一写法，不混用 `10 MiB`、`10~MiB`、`$10$ MiB`。
- 百分比统一：`97.2%` 或 `\SI{97.2}{\percent}`，不要混用。

## 小数位

- 小数位跟测量精度和统计意义走，不跟原始 CSV 机械走。
- 摘要只保留必要有效数字，通常 3-4 个有效数字足够。
- 表格中同列小数位统一。
- p-value、entropy、failure rate 这类指标要单独定义精度规则。

## 当前 RO-TRNG 稿件建议

- `$p_1=...$` 全文统一。
- `bit min-entropy` 保留同一小数位策略。
- `warmup-4`、`warmup 4`、`\texttt{WARMUP_BYTES}` 统一语义。
- `MiB`、packets、rows、captures 统一空格和单位写法。
