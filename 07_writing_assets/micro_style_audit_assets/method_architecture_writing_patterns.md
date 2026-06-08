# Method and Architecture Writing Patterns

## 顶刊常见方法节顺序

1. 先给 system/architecture overview，让读者知道模块边界。
2. 再讲关键机制，而不是先堆实现细节。
3. 说明 design choice：为什么这个模块、参数、流程是必要的。
4. 说明 controlled variables：哪些因素被固定，哪些被改变。
5. 说明 scope：这个方法能证明什么，不能证明什么。

## 数字 IC / FPGA 常见写法

- Architecture figure 放在方法节早期，支撑读者理解模块。
- Parameter/setup table 紧跟方法或实验设置，避免正文反复解释。
- 如果是 accelerator，方法节通常讲 dataflow、memory、parallelism、pipeline。
- 如果是 security/measurement paper，方法节通常讲 threat/measurement model、evidence chain、controls。

## RO-TRNG 当前稿件审查点

- Boundary figure 和 evidence workflow 是核心方法图。
- `Implemented Entropy Source` 不应变成新架构宣称，而应服务 measurement boundary。
- `Evidence Workflow` 要让读者看懂 placement、restart、counterfactual、TDC、reduced-XOR 的证据关系。
- 每个控制变量都要说明它排除了哪类替代解释。
