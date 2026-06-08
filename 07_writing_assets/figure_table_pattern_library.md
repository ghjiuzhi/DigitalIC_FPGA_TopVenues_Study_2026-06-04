# 图表套路库

## Architecture Figure
- 功能：让读者在 30 秒内看懂系统边界、数据路径和核心创新模块。
- 适用：FPGA accelerator、RISC-V SoC、CIM、crypto hardware。
- 写法：图注必须说明输入、输出、关键模块和本文新增部分。

## Dataflow Figure
- 功能：解释并行度、数据复用、memory banking、pipeline 或 scheduling。
- 适用：TVLSI、TC、TCAS-I 的架构论文。
- 写法：不要只画模块，要画数据移动方向和瓶颈被消除的位置。

## System Overview
- 功能：把 workload、硬件、软件/控制和实验设置放到同一个视图。
- 适用：TC、TCAS-I、TCHES/CHES。
- 写法：适合放在方法开头，帮助审稿人判断 scope。

## SOTA Comparison Table
- 功能：证明你的 claim 在同类工作中的位置。
- 必备列：work、venue/year、platform/process、area/resource、frequency、latency/throughput、power/energy、normalized metric、limitation。
- 避坑：不要混用 FPGA 与 ASIC 指标而不解释归一化口径。

## Ablation Table
- 功能：证明每个设计选择都有贡献。
- 适用：EDA/tool、accelerator、security countermeasure。
- 写法：至少包含 baseline、+component A、+component B、full design。

## Security Evaluation Table
- 功能：同时交代攻击模型、安全证据和硬件开销。
- 必备列：attack/fault model、trace/sample count、success rate、leakage metric、area/power overhead、remaining risk。

## Limitation / Boundary Table
- 功能：主动说明适用边界，减少审稿人对泛化 claim 的攻击。
- 适用：所有投稿，尤其是 TCAD、TCHES/CHES、TC。
