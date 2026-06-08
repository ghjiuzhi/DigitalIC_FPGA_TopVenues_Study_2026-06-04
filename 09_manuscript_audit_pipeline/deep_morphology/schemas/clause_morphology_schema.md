# Clause Morphology Schema

Complex sentences are decomposed into clause-like claim units. This is a heuristic audit schema, not a full syntactic parser.

Clause types:

- `main_clause`
- `subordinate_clause`
- `relative_clause`
- `appositive_phrase`
- `parenthetical_phrase`

Each clause record contains:

| Field | Meaning |
| --- | --- |
| `sentence_id` | Parent sentence identifier. |
| `clause_id` | Stable clause identifier, such as `ABS.S6.C2`. |
| `clause_type` | One of the clause types above. |
| `clause_text` | Clause text. |
| `function` | Clause role, such as result interpretation, limitation, implication, or method detail. |
| `claim_type` | Descriptive, causal, novelty, measurement, generalization, limitation, or implication claim. |
| `claim_strength` | `low`, `medium`, `high`, or `very_high`. |
| `evidence_support` | Direct anchor, indirect anchor, or none. |
| `risk_words` | Risk words inside the clause. |
| `recommended_action` | `KEEP`, `SPLIT`, `WEAKEN`, `MOVE`, `ADD_BOUNDARY`, or `ADD_EVIDENCE_ANCHOR`. |

Typical high-risk pattern:

```text
The results demonstrate that X determines Y, which provides a new guideline for Z.
```

Expected decomposition:

- main clause: result interpretation, high claim.
- subordinate clause: causal/generalization claim, very high if using `determines`.
- relative clause: implication claim, high if using `new guideline`.

