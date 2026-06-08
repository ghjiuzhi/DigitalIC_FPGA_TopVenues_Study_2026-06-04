# ROTRNG Style to Manuscript Bridge

这个文件把“方向层写法”直接映射到 `RO_TRNG_entropy_boundary` 的正文修改任务。

## 当前稿件一句话定位

当前稿件应写成：一篇 measurement-driven entropy-boundary paper，用 FPGA RO-TRNG 的 placement、restart、sampler counterfactual、TDC/reduced-XOR 等证据，说明 sampler-side implementation 不能被默认排除在 measured entropy-source boundary 之外。

## 章节映射

Title：

- 写 boundary，不写 generic study。
- 写 sampler-side 或 measurement boundary，不写 new TRNG architecture。

Abstract：

- 第一层：RO-TRNG evaluation 的隐含假设。
- 第二层：本文 evidence chain。
- 第三层：平台和实验边界。
- 第四层：bounded implication。

Introduction：

- 背景：RO-TRNG 是 FPGA security 常见模块。
- 痛点：随机性评估受 sampling/restart/implementation 影响。
- 文献：architecture、entropy estimation、attack、PUF/TRNG、standards 各自解决一部分。
- gap：sampler-side measured boundary 没有被当前文献直接回答。
- 贡献：boundary framing + measurement evidence chain + bounded implication。

Related Work：

- 不要写成论文列表。
- 每组只做一件事：说明 prior work 覆盖了什么，以及本文为什么仍然需要。
- 重点加入 core literature selection 中的 foundational、recent ROTRNG、security context。

Method：

- 明确 measurement contract：什么被改变，什么被控制，什么被测量。
- 每个实验方法都要回到 boundary claim。
- 不要把实验脚本细节淹没在正文里，可把冗余细节放 appendix 或 notes。

Results：

- 按 claim 排结果，不按时间顺序。
- 每个结果末尾写一句 interpretation 和一句 limitation。

Discussion：

- 主动说清：这不是 SP800-90B certification，不是 universal FPGA-family model，不是完整 attack-resistance proof。
- 说明未来 TVLSI 扩展线可以进一步做 sampler-aperture evidence，但当前稿件不混写。

## 给修改 Codex 的操作清单

1. 先从 `claim_evidence_table.md` 抽取 3 个主 claim。
2. 用这 3 个 claim 重写 abstract 和 contribution list。
3. 用 `core_literature_selection.csv` 改 related work 的分组。
4. 检查每张图表是否对应一个 claim。
5. 用 `post_edit_review_checklist.md` 自查后再结束。
