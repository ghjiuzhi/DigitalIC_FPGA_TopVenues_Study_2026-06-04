# Citation and Reference Style Guide

这个文件回答“参考文献怎么引用”。重点不是多引用，而是每个引用都有明确功能。

## IEEE 引用位置

- 引用通常放在支撑句的句末：`... has been studied in FPGA RO-TRNGs \cite{Sunar_2007,Fischer_2008}.`
- 不要把整段最后塞 6-8 篇文献，让读者不知道哪篇支撑哪句话。
- 如果一句话包含两个不同 claim，最好拆成两句分别引用。
- 标准文献只支撑 standard/guidance，不支撑“本文通过认证”。

## 引用粒度

- Foundational references：支撑定义、经典问题、早期 RO-TRNG 架构。
- Recent references：支撑“近年仍然关注什么”和 gap。
- Standard references：支撑 evaluation guidance、restart/health-test 语境。
- Instrumentation references：支撑 TDC 或 measurement method 背景。
- Attack/security references：支撑 sensitivity/motivation，不自动支撑抗攻击。

## 避免 citation dumping

坏例子：

`RO-TRNGs have been widely studied \cite{a,b,c,d,e,f,g}.`

好例子：

`Early RO-TRNG work established oscillator-array constructions \cite{a,b}. Later entropy-model and standard-oriented work clarified that output tests alone do not define the source boundary \cite{c,d}.`

## 当前 RO-TRNG 稿件规则

- `Sunar/Fischer/Wold/Bochard/Baudet`：基础和早期 warning。
- `Turan`：SP800-90B guidance，不是 certification。
- `Lubicz`：entropy computation/certified-rate context，要谨慎避免暗示本文认证。
- `Wu/Wang/Jian Song`：TDC instrumentation context。
- `Markettos`：attack sensitivity motivation，不是本文 attack-resistance evidence。
