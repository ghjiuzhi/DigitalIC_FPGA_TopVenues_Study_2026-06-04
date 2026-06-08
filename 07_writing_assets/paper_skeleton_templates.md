# 数字 IC / FPGA 论文骨架模板

## Brief 型（TCAS-II）
1. Abstract：问题、方案、两个最硬指标。
2. Introduction：短背景、窄 gap、贡献。
3. Proposed Method：一张主框图、关键公式/操作、设计取舍。
4. Results：资源/延迟/功耗/误差表，SOTA 对比。
5. Conclusion：重申适用场景和限制。

## Regular Paper 型（TCAS-I / TVLSI）
1. Abstract：完整 problem-method-result-claim。
2. Introduction：应用背景、硬件瓶颈、现有不足、贡献列表。
3. Background / Related Work：按技术路线比较，不按年份堆叠。
4. Architecture / Circuit Design：系统框图、模块、数据流、关键电路。
5. Implementation：平台、工艺/FPGA、工具、参数。
6. Evaluation：主结果、SOTA 表、消融、敏感性/限制。
7. Conclusion：强调经证据支持的 bounded claim。

## EDA / Tool 型（TCAD）
1. Problem Formulation：输入、输出、约束、优化目标。
2. Method：算法流程、模型、复杂度、工具链接口。
3. Benchmarks：数据集、baseline、运行环境。
4. Results：QoR、runtime、ablation、scalability。
5. Discussion：失败 case 和适用边界。

## Security Hardware 型（TCHES/CHES）
1. Threat Model / Workload：攻击者能力或密码算子参数。
2. Design / Attack / Countermeasure：硬件结构和安全机制。
3. Security Evaluation：trace、fault、leakage、success rate。
4. Hardware Evaluation：area、frequency、latency、throughput、power。
5. Tradeoff：安全性与开销的边界。

## FPGA Accelerator 型
1. Workload Analysis：瓶颈算子、数据规模、并行机会。
2. Architecture：PE、pipeline、memory、scheduler。
3. Mapping：定点/量化、资源复用、banking、timing closure。
4. Evaluation：resource、frequency、latency、throughput、energy、SOTA。
