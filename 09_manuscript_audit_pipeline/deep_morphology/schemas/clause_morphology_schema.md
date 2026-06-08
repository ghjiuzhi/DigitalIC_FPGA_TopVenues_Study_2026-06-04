# 从句形态学 Schema

复杂句往往不是一个 claim，而是多个 claim 挤在一起。这个 schema 用来把复杂句拆成从句级记录。

## 从句类型

- `main_clause`：主句。
- `subordinate_clause`：从属从句。
- `relative_clause`：关系从句。
- `appositive_phrase`：同位语短语。
- `parenthetical_phrase`：括号或插入语。

## 每个从句记录的字段

| 字段 | 中文含义 |
| --- | --- |
| `sentence_id` | 父句编号。 |
| `clause_id` | 从句编号，例如 `ABS.S6.C2`。 |
| `clause_type` | 从句类型。 |
| `clause_text` | 从句文本。 |
| `function` | 从句功能，如结果解释、限制、含义、方法细节。 |
| `claim_type` | claim 类型，如描述、因果、新颖性、测量、泛化、限制、含义。 |
| `claim_strength` | claim 强度。 |
| `evidence_support` | 直接证据、间接证据或无证据。 |
| `risk_words` | 该从句中的高风险词。 |
| `recommended_action` | `KEEP`、`SPLIT`、`WEAKEN`、`MOVE`、`ADD_BOUNDARY`、`ADD_EVIDENCE_ANCHOR`。 |

## 典型高风险句

```text
The results demonstrate that X determines Y, which provides a new guideline for Z.
```

应拆成：

- 主句：结果解释，claim 强。
- that 从句：因果/泛化 claim，如果用 `determines` 则很强。
- which 从句：含义 claim，如果说 `new guideline` 容易自夸和越界。

