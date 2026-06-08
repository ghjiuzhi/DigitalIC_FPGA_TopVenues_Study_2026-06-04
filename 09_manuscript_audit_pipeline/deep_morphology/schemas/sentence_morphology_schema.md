# 逐句形态学 Schema

每一行记录审计一句话。审计目标不是“这句话好不好”，而是判断它在论文结构中承担什么功能、claim 强度是否合适、证据锚点是否足够、上下句是否连贯。

| 字段 | 中文含义 |
| --- | --- |
| `section_id` | 章节名，例如 `Abstract`、`Introduction`、`Results`。 |
| `subsection_id` | 小节名；没有小节时为空。 |
| `paragraph_id` | 段落编号，例如 `INTRODUCTION.P3`。 |
| `sentence_id` | 稳定句子编号，例如 `ABS.S3` 或 `RESULTS.P5.S2`。 |
| `sentence_text` | 原句。 |
| `sentence_position` | 这句话在当前段落或摘要中的位置。 |
| `dominant_function` | 主功能，如 `BG`、`PROBLEM`、`GAP`、`METHOD`、`SETUP`、`RESULT`、`INTERPRETATION`、`BOUNDARY`。 |
| `secondary_function` | 次功能；用于识别一句话承担两个功能的 overload。 |
| `previous_sentence_relation` | 和上一句的关系，如 `elaborates`、`contrasts`、`narrows`、`evidences`、`interprets`、`jumps`。 |
| `next_sentence_relation` | 和下一句的预期关系。 |
| `claim_type` | claim 类型，如描述、比较、因果、新颖性、方法、测量、泛化、限制。 |
| `claim_strength` | claim 强度：`none`、`low`、`medium`、`high`、`very_high`。 |
| `evidence_anchor` | 证据锚点，如 Figure、Table、Equation、Citation、Experiment setup、None。 |
| `citation_anchor` | 该句绑定的引用。 |
| `figure_table_anchor` | 该句绑定的图表。 |
| `technical_terms` | 需要统一的技术术语。 |
| `hedging_words` | 缓和词，如 `may`、`can`、`suggest`、`under`、`within`。 |
| `risk_words` | 过强词、AI 味词或模糊词。 |
| `punctuation_pattern` | 标点统计和异常标点。 |
| `sentence_skeleton` | 句子骨架，例如 `To isolate X from Y, we construct Z.` |
| `expected_topvenue_role` | 顶刊中该位置通常承担的功能。 |
| `mismatch_type` | 问题类型，如缺功能、重复功能、overload、证据不足、顺序错、标点风险。 |
| `revision_operation` | 可执行修订动作，如 `SPLIT_SENTENCE`、`WEAKEN_CLAIM`、`ADD_BOUNDARY`、`ADD_EVIDENCE_ANCHOR`。 |

