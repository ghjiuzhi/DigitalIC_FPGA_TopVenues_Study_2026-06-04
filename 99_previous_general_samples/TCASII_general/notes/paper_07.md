# paper_07 - LLC Resonant Converter With Reconfigurable Secondary-Side

## 一句话定位
这篇提出二次侧可重构 LLC resonant converter，用 center-tapped transformer 和二次侧开关实现固定频率下的输出电压调节。

## 摘要写法
摘要先指出 LLC converter 高效但 DC transformer 模式缺少输出调节。随后说明二次侧 active switch 改变等效 turns ratio，减少电流路径器件且不改 primary side。结尾用 1 kV/4 kW 原型和 97.6% peak efficiency 证明。

## Introduction 写法
引言从 SST、EV charging 等高功率应用切入，说明 LLC 的软开关和高效率优势。gap 是实际系统只需有限调压，但传统方案成本/复杂度较高。

## 方法/架构写法
方法以拓扑变化为中心，解释二次侧整流器如何在不同模式之间切换。它强调 fixed-frequency operation 和 reduced switch count，写法直接服务工程价值。

## 实验/测量写法
实验使用 kW 级样机验证电压步进、模式切换、动态响应和效率。电源 brief 的可信度主要来自原型功率等级和效率曲线。

## 图表套路
图表包括拓扑图、模式等效电路、实验平台、输出电压切换波形和效率曲线。对比表可突出器件数和调压方式。

## 可模仿写法
电源类 brief 可模仿“一个拓扑变化 + 一个硬样机 + 一个高含金量指标”的叙事。
