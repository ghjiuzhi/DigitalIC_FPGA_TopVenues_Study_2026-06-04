# paper_02 - Resilient Consensus Through Dynamic Event-Triggered Mechanism

## 一句话定位
这篇提出 dynamic event-triggered mean-subsequence-reduced 算法，在存在 malicious agents 时降低通信开销并保证多智能体 resilient consensus。

## 摘要写法
摘要用“In this brief”开头，马上说明问题、攻击条件和动态触发机制。贡献集中在一个算法：引入动态变量调节触发阈值，并证明在非合作节点影响下仍能达成一致。

## Introduction 写法
引言从网络化多智能体系统的开放通信和恶意攻击切入，随后说明 resilient consensus 的基本目标。gap 是既要抗攻击，又要减少事件触发通信开销。

## 方法/架构写法
主体紧凑地定义网络、攻击模型、触发条件和 DE-MSR 更新规则。理论 brief 的方法写法强调条件、定理和证明路径，避免过多应用铺垫。

## 实验/测量写法
实验一般用仿真 case study 展示状态收敛、触发次数和与已有 event-based 方法比较。它证明“少通信”与“抗攻击”两件事同时成立。

## 图表套路
图表通常包括拓扑图、状态轨迹、触发时刻或通信次数对比。几张图足够回答：能收敛吗、攻击下稳吗、通信是否减少。

## 可模仿写法
控制理论 brief 要把模型假设写精确，贡献最好落在一个算法和一个核心定理上，不要试图讲太多系统故事。
