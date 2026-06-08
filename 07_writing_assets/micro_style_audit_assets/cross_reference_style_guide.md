# Cross-Reference Style Guide

## IEEE 常用写法

- 图：`Fig.~\ref{fig:name}`，句首可写 `Figure~\ref{fig:name}`。
- 表：`Table~\ref{tab:name}`。
- 节：`Section~\ref{sec:name}` 或 `Sections~\ref{sec:a} and~\ref{sec:b}`。
- 公式：`(\ref{eq:name})` 或 `equation~(\ref{eq:name})`。

## 避免

- 裸 `\ref{}`：读者不知道是图、表还是节。
- `figure \ref{}` 小写不统一。
- caption 有 label，但正文从未引用。
- 正文说“as shown below/above”，双栏排版会让 below/above 失效。

## 审查清单

- 每个 figure/table 至少被正文引用一次。
- 正文第一次引用图表的位置在图表附近或之前。
- caption 与正文对同一图表的 claim 一致。
- appendix/supplement 的图表不要在主文里承担唯一核心证据。
