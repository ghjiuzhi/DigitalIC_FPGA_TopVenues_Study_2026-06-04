# ROTRNG Figure and Table Patterns

ROTRNG 方向图表要让审稿人看见三个东西：物理边界、测量协议、证据链。

## 常见图

1. Entropy-source block diagram  
   画 RO/latch/PLL/source、sampler、conditioning、readout。适合在图上标注 measured boundary。

2. Sampling and restart timing diagram  
   展示 reset、restart、sampling window、clock relationship、counter capture。适合解释为什么 restart 不是普通运行状态。

3. Placement/layout map  
   FPGA 上 RO、sampler、routing 或 region 的位置。适合支撑 implementation sensitivity。

4. Jitter/phase/noise evidence figure  
   TDC、phase drift、edge distribution、frequency spread。适合支撑机制解释。

5. Statistical output figure  
   bias、correlation、min-entropy estimate、restart distribution、NIST summary。适合支撑评估结论，但不能单独当安全证明。

6. Attack/environment table  
   frequency injection、voltage/temperature、aging、EM/clock manipulation。当前稿件如果没做，应写成 limitation 或 related context。

## 常见表

SOTA/coverage table 推荐列：

- Work
- Venue/Year
- Platform
- Source type
- Evaluation method
- Restart evidence
- Sampler boundary considered?
- Attack/environment considered?
- Main limitation
- Relation to this paper

实验设置表推荐列：

- Board/FPGA
- RO count/stage
- Sampler/counter
- Clock/reset
- Placement
- Sample size
- Toolchain
- Measurement script/data path

结果表推荐列：

- Experiment
- Changed factor
- Measured metric
- Observation
- Supported claim
- Limitation

## 审查重点

- 图 1 是否让人一眼看懂本文的 boundary claim？
- 每个结果图是否写明 sample size 和 setup？
- SOTA 表是否比较“有没有覆盖 sampler boundary”，而不是只比吞吐率？
- NIST/min-entropy 表是否没有被写成 certification？
- 是否有一张图或表主动说明 limitation？
