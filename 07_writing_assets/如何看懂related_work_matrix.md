# 如何看懂 related_work_matrix

`related_work_matrix.csv` 是这个资产库的主表。你不需要一次看完 60 行。它的作用是帮你筛选“我现在该重点看哪几篇论文”。

## 最常用的筛选顺序

1. 先筛 `topic`
2. 再看 `contribution_type`
3. 再看 `evidence_type`
4. 最后看 `paper_role`

## 字段解释

### topic

这篇论文属于什么方向。

例子：
- `FPGA accelerator`
- `RISC-V / SoC / processor`
- `cryptographic hardware / hardware security`
- `CIM / memory / emerging devices`
- `EDA / CAD / design automation`

怎么用：
如果你做 FPGA 加速器，就先筛 topic 里含 `FPGA accelerator` 的论文。

### problem

这篇论文要解决的核心问题。

看法：
不要只看题目，要看 problem 里写的是哪类瓶颈：资源、时延、功耗、带宽、安全、可靠性、工具效率。

### method

这篇论文用什么方法解决问题。

看法：
method 不是让你复制方案，而是让你学“方法怎么被说清楚”。例如：数据流优化、存储 banking、ISA 扩展、攻击模型、防护机制。

### platform

论文的实现或评估平台。

常见值：
- FPGA
- ASIC / CMOS
- RISC-V / SoC
- EDA benchmark
- security evaluation platform

怎么用：
写 SOTA 表时，platform 不一样不能随便横比。FPGA 和 ASIC 要分开，或者解释归一化方式。

### metrics

论文用哪些指标证明贡献。

常见指标：
- area/resource
- frequency
- latency
- throughput
- power/energy
- accuracy
- security/leakage/fault metric
- runtime/QoR

怎么用：
你的 claim 里说“更快”，实验就必须有 latency 或 throughput；说“更省”，就必须有 area/resource 或 power/energy。

### contribution_type

贡献属于哪一类。

常见值：
- architecture
- circuit
- EDA/tool
- security
- CIM/memory
- processor
- measurement

怎么用：
如果你的贡献是 architecture，就不要用 circuit 论文的写法硬套；如果你的贡献是 tool，就要学 TCAD 的 benchmark 和 ablation 写法。

### evidence_type

论文靠什么证据支撑 claim。

常见值：
- FPGA implementation
- ASIC measurement
- simulation/model analysis
- formal/security evaluation
- benchmark/tool evaluation

怎么用：
这是判断你论文证据够不够的关键。只有 simulation，就不要写得像已经 silicon proven。

### limitation

这篇论文可能的适用边界或投稿时容易被审稿人追问的点。

怎么用：
找 gap 时重点看 limitation。多个论文的 limitation 重复出现，就可能是你的选题机会。

### what_to_learn

这篇论文最值得你学什么。

例子：
- 学摘要压缩方式。
- 学方法图。
- 学 SOTA 表。
- 学安全评估。
- 学 benchmark 组织。

### paper_role

这篇论文在你写作时最适合扮演什么角色。

例子：
- 适合模仿摘要
- 适合模仿方法图
- 适合模仿实验表
- 适合模仿 related work
- 适合模仿 SOTA 对比

## 一个完整筛选例子

你做 FPGA crypto accelerator：

1. `topic` 筛 `FPGA accelerator` 和 `cryptographic hardware`。
2. `paper_role` 找 `适合模仿实验表`、`适合模仿 SOTA 对比`。
3. 重点看 TCAS-II 的 NTT FPGA accelerator 和 TCHES/CHES 的 FHE/PQC hardware。
4. 输出 8-12 篇 related work，再按 NTT、FHE/PQC、FPGA architecture 分组。
