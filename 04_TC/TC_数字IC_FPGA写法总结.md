# TC 数字 IC / FPGA 写法总结

## 该 venue 偏好的问题类型
TC 更关心计算机系统、体系结构、可靠性和硬件/软件协同，单纯电路细节不够，要证明系统意义。

## 摘要常见结构
摘要会把问题放在 computing workload 或 system reliability 中，再落到硬件方案。

## Introduction 常见结构
Introduction 强调 why now、workload 重要性、现有系统缺口和可推广性。

## 方法/架构常见结构
方法部分常结合模型、架构、编译/运行时或框架，证明不是孤立模块。

## 实验/测量常见结构
实验覆盖 benchmark、消融、系统级 speedup/efficiency/reliability，baseline 要多。

## 对数字 IC / FPGA 投稿最有用的模仿模板
1. 用具体 workload、算子、单元、攻击模型或设计流程开场。
2. 明确现有方案在 area、power、frequency、latency、throughput、accuracy、security 或 runtime 上的瓶颈。
3. 用一张主架构图承载核心贡献，不让读者在文字里找系统结构。
4. 把结果写成“平台 + 指标 + baseline + 改善幅度”，并说明限制条件。
