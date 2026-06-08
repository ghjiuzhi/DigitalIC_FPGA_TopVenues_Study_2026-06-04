# Abbreviation and Keyword Style Guide

## 首次出现

首次出现写全称加缩写：

- true random number generator (TRNG)
- ring oscillator (RO)
- physical unclonable function (PUF)
- time-to-digital converter (TDC)
- field-programmable gate array (FPGA)

之后固定用同一个缩写或宏。

## 复数和连字符

- `TRNGs`、`ROs`、`PUFs`。
- `RO-TRNG` 作复合修饰时保持连字符。
- 不混用 `ROTRNG`、`RO TRNG`、`RO-TRNG`，除非宏统一输出。

## Keywords

Keywords 应覆盖对象、平台、方法和评估边界：

- FPGA
- ring oscillator
- true random number generator
- entropy source
- restart test
- sampler
- time-to-digital converter

## 当前稿件审查点

- `\rotrng{}` 宏输出是否与 title/abstract/keywords 一致。
- `SP800-90B`、`NIST SP 800-90B`、`SP 800-90B` 统一一种写法。
- `TDC` 不要在摘要首次裸出现，除非已定义。
