# ROTRNG 下一步建议

## 近期主线

优先推进 `RO_TRNG_entropy_boundary`，不要先把两篇稿子合并。

理由：
- 它已经有 TIM primary / Access fallback 的明确策略。
- 结构完整，有 manuscript、evidence、notes、venue。
- 它更适合先变成一篇可收敛的稿件。

## 近期 4 个动作

1. 用 `metadata/rotrng_topic_matrix.csv` 选 10-15 篇最相关文献。
2. 更新 `RO_TRNG_entropy_boundary/evidence/related_work_matrix.md`。
3. 更新 `refs/references.bib`，补齐 ROTRNG corpus 中最核心引用。
4. 对照 `ROTRNG_gap_map.md` 重写 Introduction 的 gap 段。

## TVLSI 线怎么处理

`RO_TRNG_tvlsi_sampler_aperture` 暂时不要抢主线。它应该作为后续扩展：
- 补 resource/timing/power。
- 补 route/PIP/net-delay/local-neighborhood evidence。
- 补跨 board/device replication。
- 把 mechanism observation 升级成 design rule。

## 判断是否散乱的标准

如果一个文件不能回答“它服务于哪篇稿子、哪条 claim、哪张图表”，就先不要继续往里面加内容。
