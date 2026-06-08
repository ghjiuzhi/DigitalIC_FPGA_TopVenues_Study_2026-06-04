# paper_09 - FREYA: Event-Driven 8-Channel SoC for Spiking End-to-End Sensing of Time-Sparse Biosignals

## 一句话定位
这篇提出低功耗事件驱动多通道 biomedical SoC，将时间稀疏生物信号采集和 spiking end-to-end sensing 集成在片上。

## 摘要写法
摘要先说明实时生命体征监测需要多通道并行读出和本地低延迟处理，同时传统采样方式对稀疏信号不够高效。随后给出 FREYA 的核心：事件驱动 8 通道 SoC、低功耗/小面积通道指标和 SNN 风格处理。结尾用通道面积、功耗和任务性能收束。

## Introduction 写法
引言把 biomedical wearable/implantable sensing 的能耗瓶颈讲清楚，再指出 time-sparse biosignals 与连续高采样率读出之间的浪费。gap 是“传感、压缩和推理常被分开优化，系统级端到端事件驱动不够”。

## 方法/架构写法
主体围绕感知前端、事件编码、片上处理和多通道集成展开。它的写法不是单纯模拟前端，也不是单纯神经网络，而是展示信号从生物电输入到事件/推理输出的完整路径。

## 实验/测量写法
结果围绕每通道面积、每通道功耗、事件稀疏性、延迟、检测/识别性能和多通道扩展性。TCAS-I biomedical SoC 论文特别强调“真实信号任务”的系统验证。

## 图表套路
图表包括传统系统与 FREYA 架构对比、SoC 框图、通道电路、事件流、芯片照片和任务结果。首图通常就把“为什么事件驱动更省”讲出来。

## 可模仿写法
写智能传感芯片时可模仿它的端到端叙事：把模拟读出、数字处理和算法任务看成一条链，而不是分成互不相干的模块介绍。
