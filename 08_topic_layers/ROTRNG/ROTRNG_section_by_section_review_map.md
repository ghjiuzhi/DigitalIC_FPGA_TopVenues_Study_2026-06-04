# ROTRNG Section-by-Section Review Map

这个文件把当前稿件每一节映射到顶刊章节功能。它用于审查，不直接改正文。

| Level | Section | Approx. chars | Expected function | Main risk | Review action |
|---|---|---:|---|---|---|
| section | Introduction | 3854 | context -> problem -> gap -> contributions | 数字和证据过早进入时会压住主线 | 保留主线，收紧到 measurement-boundary gap |
| section | Background and Measurement Gap | 3136 | define prior knowledge and measurement gap | 容易变成 related-work 摘要而不是 gap 铺垫 | 每段末尾回到 sampler boundary |
| section | Design and Measurement Workflow | 2 | explain system boundary and evidence chain | 实现细节过多会稀释 claim | 保留 boundary figure 和 workflow figure as core |
| subsection | Implemented Entropy Source | 3288 | supporting section | role unclear | map to a named claim or merge |
| subsection | Evidence Workflow | 1700 | explain system boundary and evidence chain | 实现细节过多会稀释 claim | 保留 boundary figure 和 workflow figure as core |
| section | Experimental Setup and Analysis Rules | 1862 | make measurement contract reproducible | 规则过多但没有说明支撑哪个 claim | 用 setup table + analysis rules 保护可复现性 |
| subsection | Diagnostic Use of Restart Statistics | 2056 | show continuous-stream balance is insufficient | NIST/restart wording像 certification | 标为 diagnostic restart evidence |
| section | Placement-Sensitive Continuous-Stream Characterization | 2171 | context evidence: implementation sensitivity | 被误读成本文唯一 novelty | 明确它只是 counterfactual 前置证据 |
| section | Restart and Warmup Characterization | 2 | show continuous-stream balance is insufficient | NIST/restart wording像 certification | 标为 diagnostic restart evidence |
| subsection | Continuous-Stream Entropy Is Not Enough | 957 | supporting section | role unclear | map to a named claim or merge |
| subsection | Warmup Transition | 1676 | show continuous-stream balance is insufficient | NIST/restart wording像 certification | 标为 diagnostic restart evidence |
| section | Sampler-Side Counterfactuals | 15970 | central boundary test | 表格过密，核心对比被淹没 | 保留代表表，repeat/traceability 可考虑 appendix |
| section | TDC-Assisted Mechanism Diagnosis | 2 | mechanism diagnostic | 被审稿人要求完整物理模型 | 强调 diagnostic, not calibrated physical model |
| subsection | Pairwise TDC Dynamics | 3667 | mechanism diagnostic | 被审稿人要求完整物理模型 | 强调 diagnostic, not calibrated physical model |
| subsection | Code-Density Calibration Boundary | 1278 | supporting section | role unclear | map to a named claim or merge |
| section | Reduced-XOR Counterfactuals | 19251 | central boundary test | 表格过密，核心对比被淹没 | 保留代表表，repeat/traceability 可考虑 appendix |
| section | Entropy-Source Boundary Discussion | 2848 | interpret entropy-source boundary | 结论过大 | 主动写 bounded implication |
| section | Limitations and Future Measurements | 2721 | scope and future measurements | 如果太短会显得回避问题 | 列清 platform/PVT/attack/certification boundaries |
| section | Conclusion | 1577 | bounded claim restatement | 重复摘要或夸大 universal claim | 一句主结论 + 一句边界 + 一句 future direction |
