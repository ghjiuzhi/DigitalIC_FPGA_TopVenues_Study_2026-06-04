# TCHES/CHES 数字 IC / FPGA 写法总结

## 该 venue 偏好的问题类型
TCHES/CHES 重视密码硬件的安全性与可验证性，性能只是其中一半，攻击模型和安全证据同样关键。

## 摘要常见结构
摘要常按“威胁/密码瓶颈-方法-攻击或实现结果-安全含义”组织。

## Introduction 常见结构
Introduction 会先明确 adversary model 或 cryptographic workload，再定位现有防护/加速器不足。

## 方法/架构常见结构
方法必须把算法、硬件、泄漏/故障路径和安全假设写清楚。

## 实验/测量常见结构
实验既要有硬件指标，也要有攻击评估、泄漏测试、参数敏感性或安全证明。

## 对数字 IC / FPGA 投稿最有用的模仿模板
1. 用具体 workload、算子、单元、攻击模型或设计流程开场。
2. 明确现有方案在 area、power、frequency、latency、throughput、accuracy、security 或 runtime 上的瓶颈。
3. 用一张主架构图承载核心贡献，不让读者在文字里找系统结构。
4. 把结果写成“平台 + 指标 + baseline + 改善幅度”，并说明限制条件。
