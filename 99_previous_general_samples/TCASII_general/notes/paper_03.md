# paper_03 - Fuzzy Observer-Based Command Filtered Adaptive Control of Flexible Joint Robots

## 一句话定位
这篇面向带时变输出约束和模型不确定性的 flexible joint robot，提出 fuzzy observer 与 command filtered adaptive control 组合方法。

## 摘要写法
摘要先交代 FJR 的应用优势，再指出强耦合、不确定性和 output constraints。随后按“observer 估计状态 -> TVBLF 处理约束 -> command filter 减轻复杂度 -> 仿真验证”排列贡献。

## Introduction 写法
引言用 FJR 的轻量、高顺应和人机安全性开场，然后快速列出现有控制方法。gap 是不确定性、不可测状态、时变输出约束和 explosion of complexity 同时存在。

## 方法/架构写法
方法部分以 Lyapunov 设计为主线：先建模，再设计 fuzzy observer，然后加入 command filter 和误差补偿。每个组件都对应一个具体困难。

## 实验/测量写法
结果主要是仿真轨迹、跟踪误差、控制输入和约束边界。Brief 不会展开大量实验，但要让曲线明确显示输出始终在约束内。

## 图表套路
图表包括参考轨迹/实际轨迹、误差、控制输入和约束区域。控制 brief 的图表目标是让稳定性和约束满足一眼可见。

## 可模仿写法
自适应控制文章要学它的“困难-模块”对应关系：每个新增技术块都解决一个明确定义的问题。
