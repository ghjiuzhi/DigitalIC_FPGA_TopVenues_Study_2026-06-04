# Post-Edit Review Checklist

这个文件给你用来审查另一个 Codex 改完的稿子。你不需要先通读 60 篇文献，只要按下面顺序查，就能判断稿子有没有“像顶刊论文那样稳”。

## 第一轮：Claim-Evidence 审查

目标：防止正文说得比证据更大。

逐项检查：

- 摘要里的每个强 claim，都能在 `evidence\claim_evidence_table.md` 找到对应证据。
- Introduction 贡献列表里的每条贡献，都对应至少一张图、一个表或一个实验过程。
- `demonstrate/prove/guarantee/certify` 这类强词没有滥用。
- 平台边界写清楚：board、FPGA family、placement、restart protocol、sample size、measurement setup。
- 没有把单平台观察写成所有 FPGA、所有 RO-TRNG、所有 PVT 条件都成立。

你可以直接问 Codex：请列出摘要每一句 claim 对应的 evidence 文件和表/图编号。

## 第二轮：写法层审查

目标：检查它有没有模仿顶刊的段落功能。

标题：

- 是否包含对象、机制或边界？
- 是否避免 `Study of`、`Research on`？
- 是否没有宣称“新架构”，除非正文真的有新架构？

摘要：

- 是否按 problem -> method -> setup -> evidence -> bounded claim 展开？
- 第一二句是否能让审稿人知道 paper gap？
- 结果数字是否只放最关键的，不堆实验流水账？

Introduction：

- 是否从应用背景收窄到 measurement boundary？
- gap 是否具体到 sampler-side implementation/restart/measurement，而不是泛泛说“已有工作不足”？
- contribution list 是否不超过 3-4 条，且每条可验证？

Related Work：

- 是否按技术路线分组？
- 每组最后是否回到本文 gap？
- 是否有近期 TCAS/TVLSI/TCHES/CHES/安全硬件相关论文支撑上下文？

## 第三轮：ROTRNG 方向层审查

目标：检查方向术语和 TRNG 逻辑是否稳。

- `entropy source`、`sampler`、`conditioning`、`restart`、`health test`、`NIST SP800-90B` 没有混用。
- 本文没有声称通过 SP800-90B certification，除非有完整认证流程。
- NIST、restart、min-entropy、statistical test 的表述没有把“测试通过”写成“安全证明”。
- 对 attacks/environmental sensitivity 的讨论是 related context，不是无证据地宣称抗攻击。
- PUF-TRNG dual-use 文献只用于背景或边界比较，不把 PUF claim 混入 TRNG claim。

## 第四轮：Venue-Fit 审查

目标：确保当前主线仍像 TIM/measurement paper，而不是被改成 TVLSI design-rule paper。

- 主叙事是 measurement boundary、evaluation methodology、evidence chain。
- 电路/FPGA 实现细节服务测量结论，不变成版图规则或架构优化主线。
- SOTA 表比较的是 evaluation/boundary coverage，不只是 throughput/area/power。
- limitations 写得主动：当前平台、当前实验边界、未来扩展到 TVLSI 的可能方向。

## 最后验收

让另一个 Codex 输出 4 个清单：

1. 改了哪些段落。
2. 每个新增 claim 对应哪个 evidence。
3. 新增/删除了哪些 reference，为什么。
4. 哪些地方仍不确定，建议你人工确认。
