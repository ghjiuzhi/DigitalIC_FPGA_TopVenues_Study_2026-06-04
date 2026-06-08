# 顶刊句子功能序列画像

这个文件把本地 01-06 顶刊语料里的句子功能做成可模仿的序列画像。字段名保持英文是为了脚本稳定，正文说明全部用中文。

## 这份文档怎么读

- 它不是论文内容综述，而是写法结构说明：每一句在 Abstract、Introduction、Results、Contribution 里承担什么功能。
- `154 条` 这类数字表示句子/功能单元数量，不是论文数量，也不是实验数量。例如看到 `RESULT 154 条`，意思是语料中有 154 个摘要句子或功能单元被标成结果句。
- 高频功能说明顶刊在该章节最常做什么；它是写作重心提示，不是要求你机械照抄比例。
- 标签名保留英文，便于和 CSV 对照；括号里的中文告诉你它在论文中的实际作用。

## 数字怎么理解

- 当前顶刊语料逐句记录：1271 条。
- 当前稿件逐句记录：292 条。
- 覆盖论文数量：60 篇。
- `sentence_function`：这句话的主功能，例如背景、问题、缺口、方法、设置、结果、解释、边界。
- `claim_type`：这句话在提出哪类 claim，例如描述、方法、测量、因果、比较、泛化或限制。
- `claim_strength`：claim 的力度。`low/medium` 多用于描述和受限结论；`high/very_high` 需要数字、图表、实验或引用支撑。
- `has_number`：是否含数字。数字多不等于写得好；顶刊通常把数字放在 RESULT 或 SETUP 句里，用来支撑比较和边界。
- `punctuation_pattern`：标点形态，例如逗号过多、分号、破折号。它帮助判断句子是否塞了太多功能。
- `transition_pattern`：句子功能链，例如 `METHOD/SETUP` 或 `RESULT/INTERPRET`，用于判断一句话是在铺方法、给结果，还是从结果转解释。

## 顶刊怎么写

顶刊的共同特征不是句子华丽，而是每句话有明确任务：先让读者知道问题为什么重要，再说明已有方法哪里不够，然后交代本文做什么、怎么验证、结果说明什么、边界在哪里。

- 好的 Abstract 像压缩版论文：背景很短，问题和缺口清楚，方法不展开细节，结果必须有信息量，最后给解释或边界。
- 好的 Introduction 像论证链：背景不是堆知识，而是不断收窄到本文问题；每段都要把读者推向“为什么必须做本文”。
- 好的 Results 段不是堆数字：先说要回答的问题，再给实验设置或图表，再观察现象、量化差异、解释原因，最后说明适用边界。
- 好的 Contribution block 很短但很硬：每条贡献都要能映射到一个概念、方法、实证结果或 artifact/audit 产物。

## RO-TRNG 仿写

- 写 Abstract 时，不要一开始讲太多 FPGA/TRNG 常识；先用 1 句背景接住读者，再用 1-2 句指出 sampler-side、placement、restart 或 entropy boundary 的问题。
- 写 Introduction 时，每段只推进一个功能：背景段负责建立任务，问题段负责暴露不确定性，缺口段负责指出现有评价缺什么，方法段负责说明本文如何隔离变量。
- 写 Results 时，每段开头先给问题句，例如“这一组实验检查 X 是否来自 Y”；结果句必须绑定数字、表格或图；解释句要把数字变成机制判断。
- 写边界时要主动：说明结果在哪些 FPGA、seed、placement、restart 条件下成立，避免把受控实验写成普遍定律。

## 是否统一组织

先说结论：顶刊不是完全统一按一种逐句顺序组织。逐句精确序列往往每篇都不同，但压缩到高层功能后，会出现少数可复用的组织范式。

- `exact_sequence` 是每篇论文真实的逐句功能顺序。
- `collapsed_sequence` 会把连续重复功能压缩，方便看高层组织方式。
- `archetype` 是把相近顺序归成一种组织范式，用来回答“有几篇属于这种组织方式”。
- `venue 偏好` 是每个 venue 的 10 篇样本内分布：6/10 以上称为强倾向，3-5/10 称为混合分布，`*_X 部分证据型` 不用于推断偏爱。

## Abstract

- 高频主功能：`RESULT`（结果）153 条，`INTERPRET`（解释）142 条，`PROBLEM`（问题）59 条，`METHOD`（方法）58 条，`BG`（背景）38 条，`SETUP`（实验/平台设置）38 条，`GAP`（缺口）16 条，`NEED`（必要性）14 条。
- 数字句：161 条；图引用句：0 条；表引用句：0 条。
- 目标功能链：`BG -> PROBLEM -> GAP -> METHOD/SETUP -> RESULT -> INTERPRET/BOUNDARY`。
- 这一节为什么这样写：摘要的任务是让读者在很短时间内看懂：领域背景是什么、本文抓住哪个未解决问题、用什么方法隔离或验证、结果给出什么证据、结论边界在哪里。

### 功能拆解

- `BG`：给读者最小背景，不讲教材。RO-TRNG 可写成“FPGA TRNG 的熵质量受实现细节影响”。
- `PROBLEM`：把背景压成具体麻烦。RO-TRNG 可写 sampler、placement、restart 或评价协议会改变可观测熵。
- `GAP`：指出现有工作没隔离什么变量，不能只说“研究不足”。
- `METHOD/SETUP`：说明本文如何构造对照、平台、指标和审计流程。
- `RESULT`：给可验证发现，优先绑定数字、表格或明确比较对象。
- `INTERPRET/BOUNDARY`：说明结果意味着什么，以及在哪些条件下成立。

### RO-TRNG 仿写规则

- 摘要不要把每个技术细节都塞进去；目标是 5-8 句内完成“背景、问题、缺口、方法、设置、结果、边界”。

### 组织范式总表

这张表回答：全体 60 篇里，有几篇属于这种组织方式；每种功能平均多少句。

| 范式 | 论文数 | 占比 | 平均句数 | 平均功能句数 | 代表论文 |
| --- | --- | --- | --- | --- | --- |
| ABS_A 完整摘要链 | 27 | 45% | 9.0 | INTERPRET=2.6; RESULT=2.0; METHOD=1.4; PROBLEM=1.0; BG=0.7; SETUP=0.6; NEED=0.3; BOUNDARY=0.2; GAP=0.2 | 01_TCASI:paper_01; 01_TCASI:paper_02; 01_TCASI:paper_07 |
| ABS_B 问题-方法-结果型 | 4 | 7% | 8.5 | RESULT=3.5; METHOD=1.5; PROBLEM=1.0; SETUP=1.0; BG=0.8; GAP=0.5; NEED=0.2 | 01_TCASI:paper_03; 03_TVLSI:paper_08; 04_TC:paper_04 |
| ABS_C 方法-验证-结果型 | 8 | 13% | 9.2 | RESULT=4.6; INTERPRET=2.2; METHOD=1.2; SETUP=0.6; NEED=0.4; BG=0.1 | 02_TCASII:paper_01; 02_TCASII:paper_02; 02_TCASII:paper_04 |
| ABS_D 结果密集型 | 7 | 12% | 8.7 | RESULT=5.0; INTERPRET=1.9; BG=0.9; PROBLEM=0.6; BOUNDARY=0.1; GAP=0.1; NEED=0.1 | 01_TCASI:paper_06; 01_TCASI:paper_08; 02_TCASII:paper_03 |
| ABS_E 压缩/非典型型 | 14 | 23% | 8.6 | INTERPRET=2.9; PROBLEM=1.7; RESULT=1.0; SETUP=0.9; BG=0.7; BOUNDARY=0.5; GAP=0.5; METHOD=0.4; NEED=0.1 | 01_TCASI:paper_04; 01_TCASI:paper_05; 02_TCASII:paper_07 |

### venue 偏好表

这张表回答：某个顶刊类别是不是偏爱某种组织范式。这里的“偏爱”只是当前 10 篇样本内的写法倾向，不是该 venue 的官方规则。

| venue | 范式 | 论文数 | 占比 | 平均功能句数 | 判断 |
| --- | --- | --- | --- | --- | --- |
| TC | ABS_A 完整摘要链 | 4/10 | 0.40 | INTERPRET=2.5; METHOD=1.5; RESULT=1.5; PROBLEM=1.0; BG=0.8; BOUNDARY=0.5; SETUP=0.5; GAP=0.2 | mixed_preference：混合分布 |
| TC | ABS_B 问题-方法-结果型 | 1/10 | 0.10 | BG=1.0; METHOD=1.0; PROBLEM=1.0; RESULT=1.0 | minor_pattern：少数样本 |
| TC | ABS_C 方法-验证-结果型 | 1/10 | 0.10 | INTERPRET=2.0; RESULT=2.0; METHOD=1.0; SETUP=1.0 | minor_pattern：少数样本 |
| TC | ABS_D 结果密集型 | 1/10 | 0.10 | RESULT=4.0; INTERPRET=2.0; BG=1.0; PROBLEM=1.0 | minor_pattern：少数样本 |
| TC | ABS_E 压缩/非典型型 | 3/10 | 0.30 | INTERPRET=2.7; SETUP=2.0; BOUNDARY=1.0; BG=0.7; PROBLEM=0.7; GAP=0.3; RESULT=0.3 | mixed_preference：混合分布 |
| TCAD | ABS_A 完整摘要链 | 6/10 | 0.60 | INTERPRET=3.7; METHOD=1.5; PROBLEM=1.5; RESULT=1.3; BG=0.8; GAP=0.3; BOUNDARY=0.2; NEED=0.2; SETUP=0.2 | strong_preference：强倾向 |
| TCAD | ABS_C 方法-验证-结果型 | 1/10 | 0.10 | RESULT=5.0; METHOD=2.0; BG=1.0 | minor_pattern：少数样本 |
| TCAD | ABS_D 结果密集型 | 1/10 | 0.10 | RESULT=5.0; INTERPRET=3.0; NEED=1.0; PROBLEM=1.0 | minor_pattern：少数样本 |
| TCAD | ABS_E 压缩/非典型型 | 2/10 | 0.20 | INTERPRET=2.0; RESULT=1.5; BG=1.0; METHOD=1.0; PROBLEM=1.0; SETUP=1.0; GAP=0.5 | minor_pattern：少数样本 |
| TCAS-I | ABS_A 完整摘要链 | 5/10 | 0.50 | INTERPRET=1.8; RESULT=1.8; METHOD=1.0; BG=0.8; SETUP=0.8; PROBLEM=0.6; GAP=0.4; NEED=0.4 | mixed_preference：混合分布 |
| TCAS-I | ABS_B 问题-方法-结果型 | 1/10 | 0.10 | RESULT=6.0; METHOD=2.0; BG=1.0; PROBLEM=1.0 | minor_pattern：少数样本 |
| TCAS-I | ABS_D 结果密集型 | 2/10 | 0.20 | RESULT=3.5; INTERPRET=1.5; BG=1.0; BOUNDARY=0.5 | minor_pattern：少数样本 |
| TCAS-I | ABS_E 压缩/非典型型 | 2/10 | 0.20 | PROBLEM=3.5; INTERPRET=3.0; RESULT=1.5; BG=0.5; METHOD=0.5; NEED=0.5 | minor_pattern：少数样本 |
| TCAS-II | ABS_A 完整摘要链 | 3/10 | 0.30 | RESULT=3.7; INTERPRET=2.7; BG=1.0; METHOD=1.0; PROBLEM=0.7; NEED=0.3; SETUP=0.3 | mixed_preference：混合分布 |
| TCAS-II | ABS_C 方法-验证-结果型 | 3/10 | 0.30 | RESULT=4.3; INTERPRET=3.7; METHOD=1.0; NEED=0.7; SETUP=0.3 | mixed_preference：混合分布 |
| TCAS-II | ABS_D 结果密集型 | 3/10 | 0.30 | RESULT=6.3; INTERPRET=1.7; BG=1.0; PROBLEM=0.7; GAP=0.3 | mixed_preference：混合分布 |
| TCAS-II | ABS_E 压缩/非典型型 | 1/10 | 0.10 | INTERPRET=7.0; SETUP=2.0; BG=1.0 | minor_pattern：少数样本 |
| TCHES/CHES | ABS_A 完整摘要链 | 6/10 | 0.60 | INTERPRET=2.3; RESULT=1.8; METHOD=1.7; PROBLEM=1.0; SETUP=1.0; BOUNDARY=0.5; BG=0.3; NEED=0.2 | strong_preference：强倾向 |
| TCHES/CHES | ABS_B 问题-方法-结果型 | 1/10 | 0.10 | RESULT=3.0; GAP=2.0; METHOD=2.0; BG=1.0; NEED=1.0; PROBLEM=1.0 | minor_pattern：少数样本 |
| TCHES/CHES | ABS_E 压缩/非典型型 | 3/10 | 0.30 | PROBLEM=2.7; INTERPRET=1.3; BG=0.7; BOUNDARY=0.7; GAP=0.7; METHOD=0.7; SETUP=0.7; RESULT=0.3 | mixed_preference：混合分布 |
| TVLSI | ABS_A 完整摘要链 | 3/10 | 0.30 | INTERPRET=2.7; RESULT=2.7; METHOD=1.3; PROBLEM=1.0; SETUP=1.0; NEED=0.7; BG=0.3; GAP=0.3 | mixed_preference：混合分布 |
| TVLSI | ABS_B 问题-方法-结果型 | 1/10 | 0.10 | RESULT=4.0; SETUP=4.0; METHOD=1.0; PROBLEM=1.0 | minor_pattern：少数样本 |
| TVLSI | ABS_C 方法-验证-结果型 | 3/10 | 0.30 | RESULT=5.7; INTERPRET=1.7; METHOD=1.3; SETUP=1.0; NEED=0.3 | mixed_preference：混合分布 |
| TVLSI | ABS_E 压缩/非典型型 | 3/10 | 0.30 | INTERPRET=3.7; RESULT=2.0; PROBLEM=1.7; GAP=1.0; BG=0.7; BOUNDARY=0.7; NEED=0.3 | mixed_preference：混合分布 |

## Introduction

- 高频主功能：`INTERPRET`（解释）199 条，`BG`（背景）92 条，`PROBLEM`（问题）48 条，`RESULT`（结果）25 条，`GAP`（缺口）23 条，`NEED`（必要性）12 条，`SETUP`（实验/平台设置）11 条，`METHOD`（方法）4 条。
- 数字句：213 条；图引用句：0 条；表引用句：2 条。
- 目标功能链：`BG -> PROBLEM -> GAP -> NEED -> TASK/METHOD -> RESULT/CONTRIB -> ORG`。
- 这一节为什么这样写：引言不是加长版摘要。顶刊引言会反复解释为什么这个问题值得做，所以 `INTERPRET` 往往很多：它们负责把背景事实翻译成研究动机、评价缺口和本文设计选择。

### 功能拆解

- `BG`：建立读者共同知识，但只保留会导向本文问题的背景。
- `PROBLEM`：从系统、电路、工具链或安全评价中抽出具体矛盾。
- `GAP`：说明已有论文、标准测试或工具流程没有解决哪个判断问题。
- `NEED`：把 gap 变成必要性，告诉读者为什么现在必须做这件事。
- `TASK/METHOD`：提前给出本文任务和变量隔离思路。
- `RESULT/CONTRIB`：用短句预告核心发现和贡献，不展开所有数据。
- `ORG`：最后一两句安排论文结构。

### RO-TRNG 仿写规则

- RO-TRNG 引言建议用 5-7 段：应用背景、实现敏感性、现有测试/论文限制、本文问题定义、实验设计、贡献、文章结构。

### 组织范式总表

这张表回答：全体 60 篇里，有几篇属于这种组织方式；每种功能平均多少句。

| 范式 | 论文数 | 占比 | 平均句数 | 平均功能句数 | 代表论文 |
| --- | --- | --- | --- | --- | --- |
| INT_A 背景-问题-缺口-任务-贡献型 | 23 | 38% | 10.0 | INTERPRET=4.8; BG=2.0; RESULT=1.1; PROBLEM=1.0; SETUP=0.4; NEED=0.3; METHOD=0.2; GAP=0.1; BOUNDARY=0.0 | 01_TCASI:paper_01; 01_TCASI:paper_03; 01_TCASI:paper_04 |
| INT_B 背景解释型 | 13 | 22% | 9.5 | INTERPRET=5.3; BG=2.5; PROBLEM=1.4; BOUNDARY=0.2; SETUP=0.2; ORG=0.1 | 01_TCASI:paper_10; 03_TVLSI:paper_10; 04_TC:paper_02 |
| INT_C 问题缺口驱动型 | 4 | 7% | 9.2 | INTERPRET=3.5; BG=2.5; PROBLEM=2.0; NEED=0.8; GAP=0.5 | 01_TCASI:paper_02; 01_TCASI:paper_08; 05_TCAD:paper_08 |
| INT_E 非典型引言型 | 1 | 2% | 9.0 | INTERPRET=5.0; BG=3.0; NEED=1.0 | 05_TCAD:paper_04 |
| INT_X 部分证据型 | 19 | 32% | 1.0 | GAP=1.0 | 02_TCASII:paper_01; 02_TCASII:paper_02; 02_TCASII:paper_03 |

### venue 偏好表

这张表回答：某个顶刊类别是不是偏爱某种组织范式。这里的“偏爱”只是当前 10 篇样本内的写法倾向，不是该 venue 的官方规则。

| venue | 范式 | 论文数 | 占比 | 平均功能句数 | 判断 |
| --- | --- | --- | --- | --- | --- |
| TC | INT_A 背景-问题-缺口-任务-贡献型 | 5/10 | 0.50 | INTERPRET=4.6; BG=1.8; PROBLEM=1.2; RESULT=1.0; NEED=0.8; SETUP=0.4 | mixed_preference：混合分布 |
| TC | INT_B 背景解释型 | 5/10 | 0.50 | INTERPRET=5.0; BG=2.6; PROBLEM=1.4 | mixed_preference：混合分布 |
| TCAD | INT_A 背景-问题-缺口-任务-贡献型 | 5/10 | 0.50 | INTERPRET=4.2; BG=2.0; PROBLEM=1.0; RESULT=1.0; GAP=0.4; NEED=0.4; SETUP=0.4 | mixed_preference：混合分布 |
| TCAD | INT_B 背景解释型 | 2/10 | 0.20 | INTERPRET=5.0; BG=3.0; PROBLEM=0.5 | minor_pattern：少数样本 |
| TCAD | INT_C 问题缺口驱动型 | 2/10 | 0.20 | INTERPRET=3.0; BG=2.5; PROBLEM=2.5; NEED=1.0 | minor_pattern：少数样本 |
| TCAD | INT_E 非典型引言型 | 1/10 | 0.10 | INTERPRET=5.0; BG=3.0; NEED=1.0 | minor_pattern：少数样本 |
| TCAS-I | INT_A 背景-问题-缺口-任务-贡献型 | 7/10 | 0.70 | INTERPRET=4.9; BG=2.4; RESULT=1.0; PROBLEM=0.7; METHOD=0.4; NEED=0.1; SETUP=0.1 | strong_preference：强倾向 |
| TCAS-I | INT_B 背景解释型 | 1/10 | 0.10 | INTERPRET=7.0; BG=2.0 | minor_pattern：少数样本 |
| TCAS-I | INT_C 问题缺口驱动型 | 2/10 | 0.20 | INTERPRET=4.0; BG=2.5; PROBLEM=1.5; GAP=1.0; NEED=0.5 | minor_pattern：少数样本 |
| TCAS-II | INT_X 部分证据型 | 10/10 | 1.00 | GAP=1.0 | insufficient_evidence：部分证据型，不用于推断 venue 偏好 |
| TCHES/CHES | INT_A 背景-问题-缺口-任务-贡献型 | 5/10 | 0.50 | INTERPRET=5.8; BG=1.6; PROBLEM=1.2; RESULT=1.2; SETUP=0.8; BOUNDARY=0.2; METHOD=0.2; NEED=0.2 | mixed_preference：混合分布 |
| TCHES/CHES | INT_B 背景解释型 | 4/10 | 0.40 | INTERPRET=5.8; PROBLEM=2.5; BG=2.2; BOUNDARY=0.5; SETUP=0.5 | mixed_preference：混合分布 |
| TCHES/CHES | INT_X 部分证据型 | 1/10 | 0.10 | GAP=1.0 | insufficient_evidence：部分证据型，不用于推断 venue 偏好 |
| TVLSI | INT_A 背景-问题-缺口-任务-贡献型 | 1/10 | 0.10 | INTERPRET=4.0; BG=3.0; RESULT=2.0 | minor_pattern：少数样本 |
| TVLSI | INT_B 背景解释型 | 1/10 | 0.10 | INTERPRET=4.0; BG=2.0; ORG=1.0 | minor_pattern：少数样本 |
| TVLSI | INT_X 部分证据型 | 8/10 | 0.80 | GAP=1.0 | insufficient_evidence：部分证据型，不用于推断 venue 偏好 |

注意：`部分证据型` 多半表示该篇在当前语料中只有局部 Introduction/Results 功能单元，不能把它解读成该 venue 真喜欢短结构。

## Results

- 高频主功能：`RESULT`（结果）162 条，`SETUP`（实验/平台设置）62 条，`ORG`（结构安排）21 条，`PROBLEM`（问题）11 条，`NEED`（必要性）2 条，`GAP`（缺口）1 条，`METHOD`（方法）1 条。
- 数字句：140 条；图引用句：4 条；表引用句：10 条。
- 目标功能链：`QUESTION -> SETUP/FIGURE/TABLE -> OBSERVATION -> QUANTIFICATION -> INTERPRETATION -> BOUNDARY -> TRANSITION`。
- 这一节为什么这样写：结果段的核心不是“我们测了很多”，而是“每组实验回答一个问题”。`RESULT` 数量高说明顶刊把观察和量化判断写得很密；`SETUP` 数量也高，说明读者必须先知道比较条件。

### 功能拆解

- `QUESTION`：段首明确本段回答什么问题。
- `SETUP/FIGURE/TABLE`：交代平台、变量、指标、图表或表格。
- `OBSERVATION`：描述图表里最明显的趋势。
- `QUANTIFICATION`：给数字、差值、比例或排序。
- `INTERPRETATION`：解释为什么会这样，连接到机制。
- `BOUNDARY`：说明哪些条件下不能外推。
- `TRANSITION`：把本段发现导向下一组实验。

### RO-TRNG 仿写规则

- RO-TRNG 结果段每段最好只回答一个变量问题，例如 sampler-side、placement、restart、routing 或 seed，不要把多个 claim 混进一句长句。

### 组织范式总表

这张表回答：全体 60 篇里，有几篇属于这种组织方式；每种功能平均多少句。

| 范式 | 论文数 | 占比 | 平均句数 | 平均功能句数 | 代表论文 |
| --- | --- | --- | --- | --- | --- |
| RES_A 设置-多结果-解释型 | 11 | 18% | 9.8 | RESULT=6.1; SETUP=2.6; ORG=0.9; NEED=0.1; PROBLEM=0.1 | 01_TCASI:paper_06; 01_TCASI:paper_08; 03_TVLSI:paper_10 |
| RES_B 结构化实验段型 | 7 | 12% | 9.6 | RESULT=3.6; SETUP=3.0; ORG=1.4; PROBLEM=1.3; METHOD=0.1; NEED=0.1 | 01_TCASI:paper_07; 04_TC:paper_10; 05_TCAD:paper_09 |
| RES_C 结果密集型 | 2 | 3% | 9.5 | RESULT=9.0; ORG=0.5 | 01_TCASI:paper_10; 05_TCAD:paper_04 |
| RES_D 短结果链型 | 4 | 7% | 7.5 | RESULT=4.0; SETUP=3.0; GAP=0.2; PROBLEM=0.2 | 01_TCASI:paper_02; 01_TCASI:paper_03; 04_TC:paper_06 |
| RES_X 部分证据型 | 36 | 60% | 1.0 | RESULT=1.0 | 01_TCASI:paper_01; 01_TCASI:paper_04; 01_TCASI:paper_05 |

### venue 偏好表

这张表回答：某个顶刊类别是不是偏爱某种组织范式。这里的“偏爱”只是当前 10 篇样本内的写法倾向，不是该 venue 的官方规则。

| venue | 范式 | 论文数 | 占比 | 平均功能句数 | 判断 |
| --- | --- | --- | --- | --- | --- |
| TC | RES_A 设置-多结果-解释型 | 4/10 | 0.40 | RESULT=5.8; SETUP=2.2; ORG=1.2; NEED=0.2; PROBLEM=0.2 | mixed_preference：混合分布 |
| TC | RES_B 结构化实验段型 | 1/10 | 0.10 | SETUP=6.0; RESULT=3.0; ORG=1.0 | minor_pattern：少数样本 |
| TC | RES_D 短结果链型 | 1/10 | 0.10 | SETUP=5.0; RESULT=3.0 | minor_pattern：少数样本 |
| TC | RES_X 部分证据型 | 4/10 | 0.40 | RESULT=1.0 | insufficient_evidence：部分证据型，不用于推断 venue 偏好 |
| TCAD | RES_A 设置-多结果-解释型 | 2/10 | 0.20 | RESULT=5.5; SETUP=3.5; ORG=1.0 | minor_pattern：少数样本 |
| TCAD | RES_B 结构化实验段型 | 1/10 | 0.10 | RESULT=4.0; SETUP=4.0; ORG=2.0 | minor_pattern：少数样本 |
| TCAD | RES_C 结果密集型 | 1/10 | 0.10 | RESULT=8.0; ORG=1.0 | minor_pattern：少数样本 |
| TCAD | RES_D 短结果链型 | 1/10 | 0.10 | SETUP=5.0; RESULT=3.0; PROBLEM=1.0 | minor_pattern：少数样本 |
| TCAD | RES_X 部分证据型 | 5/10 | 0.50 | RESULT=1.0 | insufficient_evidence：部分证据型，不用于推断 venue 偏好 |
| TCAS-I | RES_A 设置-多结果-解释型 | 2/10 | 0.20 | RESULT=7.5; SETUP=2.0 | minor_pattern：少数样本 |
| TCAS-I | RES_B 结构化实验段型 | 1/10 | 0.10 | RESULT=4.0; SETUP=3.0; NEED=1.0; ORG=1.0 | minor_pattern：少数样本 |
| TCAS-I | RES_C 结果密集型 | 1/10 | 0.10 | RESULT=10.0 | minor_pattern：少数样本 |
| TCAS-I | RES_D 短结果链型 | 2/10 | 0.20 | RESULT=5.0; SETUP=1.0; GAP=0.5 | minor_pattern：少数样本 |
| TCAS-I | RES_X 部分证据型 | 4/10 | 0.40 | RESULT=1.0 | insufficient_evidence：部分证据型，不用于推断 venue 偏好 |
| TCAS-II | RES_X 部分证据型 | 10/10 | 1.00 | RESULT=1.0 | insufficient_evidence：部分证据型，不用于推断 venue 偏好 |
| TCHES/CHES | RES_A 设置-多结果-解释型 | 2/10 | 0.20 | RESULT=6.5; SETUP=3.0; ORG=0.5 | minor_pattern：少数样本 |
| TCHES/CHES | RES_B 结构化实验段型 | 4/10 | 0.40 | RESULT=3.5; PROBLEM=2.2; SETUP=2.0; ORG=1.5; METHOD=0.2 | mixed_preference：混合分布 |
| TCHES/CHES | RES_X 部分证据型 | 4/10 | 0.40 | RESULT=1.0 | insufficient_evidence：部分证据型，不用于推断 venue 偏好 |
| TVLSI | RES_A 设置-多结果-解释型 | 1/10 | 0.10 | RESULT=5.0; SETUP=3.0; ORG=2.0 | minor_pattern：少数样本 |
| TVLSI | RES_X 部分证据型 | 9/10 | 0.90 | RESULT=1.0 | insufficient_evidence：部分证据型，不用于推断 venue 偏好 |

注意：`部分证据型` 多半表示该篇在当前语料中只有局部 Introduction/Results 功能单元，不能把它解读成该 venue 真喜欢短结构。

## Contribution

- 高频主功能：`CONTRIB`（贡献）61 条。
- 数字句：1 条；图引用句：0 条；表引用句：0 条。
- 目标功能链：`CONCEPTUAL CONTRIBUTION -> METHOD CONTRIBUTION -> EMPIRICAL CONTRIBUTION -> ARTIFACT/AUDIT CONTRIBUTION`。
- 这一节为什么这样写：贡献块数量少，是因为它通常集中在引言末尾或摘要末尾；但每条贡献必须可核验，不能只是换个说法重复“本文提出一种方法”。

### 功能拆解

- 概念贡献：重新定义问题、威胁模型、评价边界或解释框架。
- 方法贡献：提出可复现实验设计、变量隔离方法、审计流程或工具链。
- 实证贡献：报告跨平台、跨配置、跨指标的发现。
- artifact/audit 贡献：给出数据、脚本、流程、检查清单或复现实验资产。

### RO-TRNG 仿写规则

- RO-TRNG 贡献建议写成 3-4 条，每条以“我们定义/构造/测量/发布或审计”开头，并能在正文找到对应章节和证据。

### 组织范式总表

这张表回答：全体 60 篇里，有几篇属于这种组织方式；每种功能平均多少句。

| 范式 | 论文数 | 占比 | 平均句数 | 平均功能句数 | 代表论文 |
| --- | --- | --- | --- | --- | --- |
| CON_A 单条贡献块 | 59 | 98% | 1.0 | CONTRIB=1.0 | 01_TCASI:paper_01; 01_TCASI:paper_02; 01_TCASI:paper_03 |
| CON_B 多条贡献块 | 1 | 2% | 2.0 | CONTRIB=2.0 | 04_TC:paper_07 |

### venue 偏好表

这张表回答：某个顶刊类别是不是偏爱某种组织范式。这里的“偏爱”只是当前 10 篇样本内的写法倾向，不是该 venue 的官方规则。

| venue | 范式 | 论文数 | 占比 | 平均功能句数 | 判断 |
| --- | --- | --- | --- | --- | --- |
| TC | CON_A 单条贡献块 | 9/10 | 0.90 | CONTRIB=1.0 | strong_preference：强倾向 |
| TC | CON_B 多条贡献块 | 1/10 | 0.10 | CONTRIB=2.0 | minor_pattern：少数样本 |
| TCAD | CON_A 单条贡献块 | 10/10 | 1.00 | CONTRIB=1.0 | strong_preference：强倾向 |
| TCAS-I | CON_A 单条贡献块 | 10/10 | 1.00 | CONTRIB=1.0 | strong_preference：强倾向 |
| TCAS-II | CON_A 单条贡献块 | 10/10 | 1.00 | CONTRIB=1.0 | strong_preference：强倾向 |
| TCHES/CHES | CON_A 单条贡献块 | 10/10 | 1.00 | CONTRIB=1.0 | strong_preference：强倾向 |
| TVLSI | CON_A 单条贡献块 | 10/10 | 1.00 | CONTRIB=1.0 | strong_preference：强倾向 |

## 分 venue 读法

这些差异是写法倾向，不是硬规则。写 RO-TRNG 时应该按目标 venue 的读者期待调整重心。

- TCAS-I/TCAS-II：强调电路、方法、验证的紧凑链条。本地记录中相关句子约 370 条；可模仿其“模型/电路 -> 验证 -> 应用或解释”的压缩写法。
- TVLSI/TCAD：强调设计约束、工具/流程、实验设置。本地记录中 TVLSI 153 条、TCAD 246 条；RO-TRNG 若强调 FPGA 实现和可复现实验，应多学这类写法。
- TC：强调系统问题、比较基线、实证结果。本地记录中 TC 241 条；适合学习如何把实验发现写成系统层结论。
- TCHES/CHES：强调威胁模型、攻击/防御边界、可复现实验。本地记录中 TCHES/CHES 261 条；适合学习安全评价中如何主动写边界和复现条件。

## 全章节功能模板

- Related Work：`类别 -> 代表性工作 -> 共同能力 -> 共同限制 -> 本文差异`。
- Background：`定义 -> 机制 -> 相关性 -> 限制`。
- Method：`目标 -> 原理 -> 结构 -> 固定变量 -> 改变变量 -> 输出`。
- Experimental Setup：`目的 -> 平台 -> 工具链 -> 控制项 -> 变量 -> 指标 -> 重复次数 -> 处理方法`。
- Discussion：`发现综合 -> 替代解释 -> 限制 -> 含义`。
- Conclusion：`问题回顾 -> 方法回顾 -> 发现 -> 含义 -> 边界/未来工作`。

## 使用提醒

- 先看功能链，再看数字：数字告诉你顶刊常写什么，功能链告诉你应该按什么顺序写。
- 不要把高频功能当配方比例：例如 Introduction 的 `INTERPRET` 很多，不代表要写很多空泛解释，而是每段都要解释“这个事实如何导向本文问题”。
- 仿写时优先检查每段第一句和最后一句：第一句要立问题，最后一句要给解释、边界或转场。
