# Figure Role Taxonomy

## 图的常见角色

- System overview：第一时间解释系统和边界。
- Architecture：解释模块、数据通路、控制路径。
- Workflow：解释实验或算法流程。
- Timing：解释时钟、reset、restart、采样窗口。
- Dataflow：解释数据如何移动和并行。
- Mechanism：解释为什么结果会出现。
- Result：展示测量曲线、分布、柱状图。
- Ablation/control：说明替代解释被排除。
- Comparison：和 baseline 或 SOTA 比较。
- Limitation：说明边界或失败 case。

## 审查动作

- 保留：支撑主 claim 或让读者理解方法的图。
- 合并：多张图讲同一变量或同一趋势。
- 移到附录：traceability、repeat、archive 细节图。
- 补充：缺少 boundary overview、workflow、核心机制解释图。

## Caption 必须回答

这张图测/画什么，在什么条件下，支撑哪个 claim，不支撑什么更大的 claim。
