# LaTeX IEEE Polish Checklist

## 双栏浮动体

- `figure*`/`table*` 只用于确实需要跨栏的内容。
- 单栏能读清的图表优先单栏。
- 表格过宽时先考虑删列、合并列、移 appendix，而不是无脑 `table*`。

## Caption 和 label

- `\caption{...}` 后紧跟 `\label{...}`。
- label 前缀统一：`fig:`、`tab:`、`sec:`、`eq:`。
- caption 不只写标题，要写 setup 和 claim。

## 空格和连接

- 用 `Fig.~\ref{}`、`Table~\ref{}` 避免断行。
- 范围用 en dash：`0.0001--0.0009`。
- 复合修饰用 hyphen：`restart-oriented`、`sampler-side`。

## 编译警告

审稿前至少查：

- undefined references
- missing citations
- overfull hbox
- underfull vbox only if visually严重
- bibliography warnings

## 当前稿件审查点

- 表格很多，优先检查 overfull 和 caption 是否能独立理解。
- 所有强结果数字应能追到表格、evidence 或 artifact。
