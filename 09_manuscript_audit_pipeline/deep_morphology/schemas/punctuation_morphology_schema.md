# Punctuation Morphology Schema

Punctuation is audited per sentence because punctuation changes claim structure and technical register.

| Mark | Field | Correct IEEE-style use | Suspicious use | Replacement rule |
| --- | --- | --- | --- | --- |
| `-` | `hyphen_count` | Compound modifier, e.g. `sampler-side`, `restart-based`. | Hyphen used as dash or over-stacked modifiers. | Keep technical compounds; replace dash use with comma, colon, or en dash. |
| `–` | `en_dash_count` | Range or relation, e.g. `W4-W5` if normalized to en dash in final typesetting. | Used as decorative interruption. | Use only for ranges/relations. |
| `—` | `em_dash_count` | Rare explanatory insertion. | AI-like aside or dramatic contrast. | Replace with comma, parentheses, or a separate sentence. |
| `:` | `colon_count` | Introduce list, definition, or explicit explanation. | Repeated template-like setup. | Use once when it sharpens structure. |
| `;` | `semicolon_count` | Join closely related independent clauses. | Long sentence hiding two claims. | Split if both sides carry separate claims. |
| `?` | `question_mark_count` | Rare research-question framing. | Rhetorical question in technical body. | Convert to declarative task sentence. |
| `()` | `parentheses_count` | Abbreviation, condition, or short clarification. | Hiding important constraints. | Move important conditions into main sentence. |
| `/` | `slash_count` | Compact alternatives or units. | Rough pairing such as `method/result`. | Replace with explicit conjunction when meaning matters. |
| `,` | `comma_count` | Clause separation and lists. | Overloaded sentence with too many clauses. | Split or simplify when comma count is high. |

