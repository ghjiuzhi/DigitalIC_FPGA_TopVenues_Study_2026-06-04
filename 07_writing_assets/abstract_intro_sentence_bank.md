# 摘要、Introduction 与贡献句式库

这些句式是可迁移模板，不是论文原文复制。使用时把方括号内容替换成你自己的对象、平台和指标。

## Abstract 模板

### Regular Paper 型
1. `[Task/Workload] has become a critical bottleneck in [system/application] because [specific hardware constraint].`
2. `This paper presents [architecture/circuit/method], which [core mechanism] to improve [metric].`
3. `The proposed design is implemented/evaluated on [FPGA/ASIC/process/toolflow] under [setup].`
4. `Compared with [baseline/SOTA], it achieves [quantitative result] in [area/power/latency/throughput/security].`
5. `These results indicate that [main technical claim] under [scope/constraint].`

### Brief 型
1. `[Existing solution] suffers from [single clear bottleneck] when [condition].`
2. `We propose [compact technique] for [target module/operator].`
3. `[Implementation/evaluation] shows [two strongest metrics], making it suitable for [use case].`

### Security Hardware 型
1. `[Cryptographic primitive/implementation] is vulnerable/expensive under [attack model or workload].`
2. `We introduce [countermeasure/accelerator/evaluation method] that [mechanism].`
3. `Experiments on [platform/dataset/traces] show [security evidence] with [hardware overhead].`

## Introduction Gap 模板

- `Although [prior direction] has improved [metric], it still assumes [condition] and therefore does not address [your constraint].`
- `Existing FPGA/ASIC implementations mainly optimize [metric A], while [metric B or deployment constraint] remains underexplored.`
- `For [target workload], the dominant cost is no longer [old bottleneck] but [new bottleneck], motivating a different architecture.`
- `Most prior studies evaluate [module-level metric], but few report [system-level metric] under [realistic setup].`

## Contribution List 模板

1. `We propose [architecture/method], a [brief descriptor] that [main mechanism].`
2. `We implement [module/system] on [platform] and quantify [metrics] under [setup].`
3. `We compare against [baseline group] and show [bounded claim], while discussing [limitation].`

## 写作提醒

- 摘要最后一句不要写空泛意义，要写“结果证明了什么边界内的 claim”。
- Introduction 的 gap 要能被实验表验证。
- 贡献列表每条都要能映射到一个 figure/table/result。
