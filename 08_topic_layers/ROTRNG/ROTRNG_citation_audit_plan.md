# ROTRNG Citation Audit Plan

这个文件用于审查当前稿件的参考文献引用。它不要求立刻改正文。

## 当前状态

- `references.bib` 有 27 条 BibTeX。
- `main.tex` 当前引用 18 个 cite key。
- 未引用条目需要判断是补进 related work、留作备用，还是删除。

## 引用分层

Foundational:

- Sunar、Fischer、Wold、Bochard、Baudet 等用于 RO-TRNG 基础、早期实现和输出测试风险。

Standard/evaluation:

- NIST SP800-90B/Turan 用于 evaluation guidance，不用于 certification claim。
- Lubicz 系列可用于 entropy computation/certified-rate context，但要避免暗示本文通过认证。

Recent TRNG/FPGA:

- 近年 TCAS/TVLSI/TCHES/TCAD TRNG、PUF/TRNG、phase-noise、flicker-noise、PLL-TRNG、latched RO 工作用于 gap 和方向定位。

TDC/instrumentation:

- Jian Song、Wu、Wang 等用于 TDC 背景和 instrumentation limits。

Attack/security:

- Frequency injection/attack 文献用于 motivation 和 sensitivity context，不支撑本文抗攻击。

## 审查问题

1. 每个 related-work 句子是否有具体引用？
2. 每个引用是否只承担它能支撑的功能？
3. 是否缺少近年 TRNG/entropy-model 文献来支撑 gap？
4. 是否有未引用 BibTeX 条目应该删除？
5. 是否有 citation dumping，需要拆成两句？
