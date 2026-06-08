# Equation and Algorithm Style Guide

## 公式什么时候需要编号

- 后文会引用：编号。
- 只是一行定义：可以不编号或放 prose。
- 多个表达式构成方法核心：编号并解释变量。

## 公式前后怎么写

公式前：

- 说明为什么需要这个量。
- 定义输入对象。

公式后：

- 解释每个变量。
- 说明这个公式支撑哪个实验或 claim。
- 不要让公式孤立出现。

## 算法/流程怎么呈现

- 如果读者需要复现实验流程，用 workflow figure 或 step list。
- 如果只是数学定义，用 equation。
- 如果是硬件状态机或数据流，用 architecture/dataflow figure。

## 当前 RO-TRNG 稿件审查点

- reduced-XOR 公式必须定义 $s_{r,k}$、data RO index、sampler phase。
- 公式后要说明它为什么能揭示 all64 final output 隐藏内部方向偏置。
- 不把公式写成 proof；它只是 construction/diagnostic definition。
