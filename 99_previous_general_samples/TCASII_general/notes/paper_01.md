# paper_01 - Watermarking-Based Defense Mechanism in LFC of Electricity Grids Compromised by Covert Attacks

## 一句话定位
这篇 brief 针对电网 load frequency control 中 covert attack 难检测的问题，用 multiplicative watermarking 和 Luenberger observer 构造检测与防御机制。

## 摘要写法
摘要直接点明对象、威胁和方法：LFC 被 covert attacks 破坏，本文用 watermark generator filter 加 observer 识别攻击。随后补充 watermark equalization filter 负责抵消注入信号影响，最后用实时仿真和 RMSE/ITAE 改善收束。

## Introduction 写法
引言先说明 AGC/LFC 依赖通信网络，因此暴露在网络攻击下。随后把 stealthy/covert attack 定位为危险场景，并指出常规控制与检测方法不足。Brief 的引言很短，快速到贡献。

## 方法/架构写法
方法部分围绕“注入水印但不破坏控制性能”展开：发送端加入 dummy watermark，接收端抵消，同时 observer 检测异常。结构清楚，公式服务于检测逻辑。

## 实验/测量写法
实验用两区域电力系统和实时仿真说明攻击检测与控制性能恢复。指标选 RMSE、ITAE 等控制系统常用指标，证明方法不只是检测到攻击，也改善动态性能。

## 图表套路
图表重点是系统框图、攻击/防御信号路径、频率响应曲线和对比指标。Brief 里图必须“一图多用”，既说明机制又承载结果。

## 可模仿写法
安全控制 brief 可模仿它的压缩路线：应用风险一句话讲清，检测机制画框图，仿真用 2-3 个指标证明。
