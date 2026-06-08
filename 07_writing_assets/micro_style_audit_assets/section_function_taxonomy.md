# Section Function Taxonomy

这个文件定义顶刊论文每个章节应该承担的功能。审稿时不要只看句子顺不顺，要看每一节是否完成了自己的任务。

## Title / Keywords

标题负责暴露对象、机制、边界和应用场景。Keywords 负责让审稿人和检索系统知道本文属于哪些技术路线。标题中的修饰词必须能回到证据。

## Abstract

摘要负责压缩整篇 claim chain：背景、问题、方法、创新、数字、边界。数字只放能支撑主 claim 的结果。

## Introduction

Introduction 负责把读者从大场景带到具体 gap。顶刊常见顺序是 context -> constraint -> existing work -> gap -> this work -> contributions。

## Related Work / Background

Related Work 不是论文列表，而是 gap map。Background 不是教科书，而是让读者理解本文测量边界需要哪些概念。

## Method / Architecture

方法或架构节负责解释本文如何产生证据。好的写法会先给 overview，再讲设计取舍、实现边界、控制变量和为什么这样能回答问题。

## Experimental Setup

实验设置节负责让结果可复现和可解释。它要说明平台、参数、样本、工具链、测量流程、控制变量和排除项。

## Results / Evaluation

结果节应按 claim 排，不按实验日志顺序排。每个结果块应包含 setup、observation、interpretation、limitation。

## Discussion

Discussion 负责把结果提升到 paper-level implication，同时主动限制 claim。

## Limitations / Future Work

Limitations 负责保护论文可信度。它应该说明平台、PVT、样本、攻击模型、认证边界，而不是一句带过。

## Conclusion

Conclusion 负责收束，不应引入新结果。常见结构是 one-sentence thesis、key evidence、bounded implication、future direction。
