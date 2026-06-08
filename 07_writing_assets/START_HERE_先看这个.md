# START HERE：先看这个

你现在这个目录不是“论文阅读目录”，而是一个写论文工具箱。第一次打开时，不要从 `related_work_matrix.csv` 开始硬啃，也不要试图一次看完 60 篇。正确方式是：先看你当前要完成什么任务，再去拿对应工具。

## 这个资产库解决什么问题

它帮你解决 5 件事：

1. **不知道怎么读论文**：用 `论文阅读卡片模板.md`，只抓论文里最有用的 8 个点。
2. **不知道怎么找 gap**：用 `related_work_matrix.csv` 和 `如何看懂related_work_matrix.md`，看别人方法的 limitation。
3. **不知道摘要和 Introduction 怎么写**：用 `abstract_intro_sentence_bank.md` 和 `从自己结果到论文初稿.md`。
4. **不知道图表怎么安排**：用 `figure_table_pattern_library.md`。
5. **不知道投哪个 venue**：用 `venue_pattern_matrix.csv` 和 `reviewer_checklist.md`。
6. **不知道第一句、第二句分别在干嘛**：用 `rhetorical_morphology_manual.md`，看顶刊的句子功能序列。

## 第一次使用只看这 3 个文件

1. `任务导航_我现在该看哪个文件.md`
   你先根据当前任务找到入口，不要直接翻全部文件。

2. `如何看懂related_work_matrix.md`
   这是主表说明书。你会知道 topic、contribution_type、evidence_type、paper_role 这些字段到底怎么用。

3. `从自己结果到论文初稿.md`
   当你有实验结果时，它告诉你怎么从结果反推论文主线。

如果你现在的问题是“顶刊论文第一句话在干嘛，第二句话在干嘛”，先看：

4. `rhetorical_morphology_manual.md`
   这是句子功能形态学入口，配套表在 `micro_style_audit_assets/topvenue_sentence_function_matrix.csv`。

## 一个最小例子

假设你做了一个 FPGA 上的 NTT/FHE 加速器：

- 先在 `related_work_matrix.csv` 里筛 `topic` 包含 `FPGA accelerator` 和 `cryptographic hardware` 的论文。
- 你会看到 TCAS-II 的 `A Lightweight and Hardware-Efficient NTT FPGA Accelerator for FHE Applications`。
- 看它不是为了复制内容，而是学它怎么把问题写窄：FHE 的瓶颈是 NTT，贡献是轻量 FPGA 架构，结果用 resource、latency、throughput-per-LUT 证明。
- 然后你再去 `abstract_intro_sentence_bank.md` 里套摘要结构。
- 如果你要学习摘要、Introduction、Results 每句话承担什么功能，再去 `rhetorical_morphology_manual.md` 看句子功能序列。

## 最重要的一句话

不要问“这 60 篇我怎么读完”。应该问：“我现在要写摘要、找 gap、做 related work，哪几篇最值得我看？”
