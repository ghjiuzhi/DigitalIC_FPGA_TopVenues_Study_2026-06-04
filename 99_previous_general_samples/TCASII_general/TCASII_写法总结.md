# TCAS-II Express Briefs 近年论文写法总结

## 样本说明
本目录整理了 10 篇 2024-2025 年 IEEE Transactions on Circuits and Systems II: Express Briefs 的开放版本论文，方向覆盖控制安全、多智能体、机器人控制、无线供能、Cryo-CMOS、ASDM/ADC、电源转换、AI-for-circuits、神经形态自动化和 FHE 硬件加速。

## TCAS-II 和 TCAS-I 写法差异
TCAS-II 的关键词是 **brief**。它不像 TCAS-I 那样完整铺开系统背景和多轮实验，而是集中打一两个技术点。常见结构是：问题一句话、gap 一句话、方法一个核心模块、验证一组最关键图表。它更看重“短、准、可验证”。

## 共同写法规律
1. **标题非常直给。** 通常是“对象 + 技术动作 + 应用/指标”，很少做大而宽的命名。
2. **摘要压缩成四步。** Problem -> proposed idea -> key mechanism -> result。很多摘要第一句就出现 “This brief proposes...”。
3. **Introduction 很短。** 背景通常只够支撑 gap，不追求完整综述。相关工作只选最贴近本文技术点的几类。
4. **贡献集中。** 一篇 brief 最好只有一个主创新：一个触发机制、一个补偿结构、一个拓扑变化、一个生成器或一个预测框架。
5. **实验少但必须尖锐。** 用最能支撑 claim 的曲线或表格，而不是铺很多低信息量图。

## 常见章节模板
```text
Abstract: 问题 -> 方法 -> 机制 -> 关键结果
I. Introduction:
  应用/技术背景
  现有不足
  本文贡献
II. Proposed Method / Circuit / Algorithm:
  一个核心思想
  最必要的公式、拓扑或数据流
III. Analysis / Design Details:
  证明、稳定性、设计取舍或关键参数
IV. Results:
  仿真/测量/原型
  对比表
V. Conclusion:
  重申一个贡献和主要指标
```

## 摘要仿写公式
```text
This brief addresses [specific bottleneck] in [specific circuit/system].
To solve this issue, we propose [one method/topology/algorithm], which [core mechanism].
The proposed design/method is validated by [simulation/prototype/measurement].
It achieves [metric], compared with [baseline/prior works].
```

## Introduction 的压缩技巧
- 第一段只建立“为什么这个问题重要”。
- 第二段只讲“为什么已有方法不够”。
- 第三段直接列本文贡献，通常 2-3 点足够。
- 不要把 TCAS-II 写成小号 TCAS-I；brief 的价值在于把一个局部技术问题讲透。

## 图表组织
- 控制类：系统框图、状态轨迹、触发次数/性能指标。
- 电路类：拓扑图、关键波形/频谱、测量表。
- 电源/RF 类：模式等效电路、效率/传输曲线、原型图。
- 加速器/自动化类：数据流或 flow 图、资源表、SOTA 对比。

## 对投稿最有用的启发
1. 先问自己：本文能不能用一句话说清一个技术点？如果不能，可能更像 TCAS-I。
2. 每个小节都要直接服务主 claim，少写横向铺陈。
3. 对比指标要提前选好，brief 没篇幅补救不聚焦的实验。
4. 结论只回收核心贡献，不新增愿景。
5. 句子可以简单，但 claim 必须非常具体。

## 写 TCAS-II 时的取舍建议
如果准备投 TCAS-II，最重要的是控制论文边界。一个很实用的判断是：你的创新是否可以被一个图、一个公式组或一个核心表格承载。如果需要三个互不相干的模块才能说明贡献，文章很容易显得散。Brief 更适合“局部但锋利”的结果，例如一个 comparator 低温 hysteresis 抑制结构、一个 NTT twiddle factor 生成器、一个二次侧可重构整流方案，或者一个事件触发一致性算法。

实验也要少而硬。不要把所有能跑的仿真都放进去，而是选最能击中审稿问题的结果：控制类看收敛与触发次数，电路类看测量频谱/效率/噪声/功耗，硬件类看资源、吞吐和 SOTA 表。TCAS-II 的好文章不是信息少，而是每个信息点都在支撑同一个核心 claim。
