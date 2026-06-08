# Sentence Morphology Schema

Each record audits one sentence as a functional unit, not as generic prose quality.

| Field | Meaning |
| --- | --- |
| `section_id` | Normalized section label, such as `Abstract`, `Introduction`, or `Results`. |
| `subsection_id` | Optional subsection title or empty when absent. |
| `paragraph_id` | Section-local paragraph identifier. |
| `sentence_id` | Stable location, such as `ABS.S3` or `RESULTS.P5.S2`. |
| `sentence_text` | Source sentence text. |
| `sentence_position` | Sentence position inside the paragraph or abstract. |
| `dominant_function` | Main role: `BG`, `PROBLEM`, `GAP`, `NEED`, `TASK`, `METHOD`, `SETUP`, `CONTROL`, `VARIABLE`, `RESULT`, `OBSERVATION`, `QUANTIFICATION`, `INTERPRETATION`, `BOUNDARY`, `LIMITATION`, `CONTRIBUTION`, `TRANSITION`, or `ORGANIZATION`. |
| `secondary_function` | Secondary role if the sentence is overloaded. |
| `previous_sentence_relation` | Relation to previous sentence: `elaborates`, `contrasts`, `narrows`, `generalizes`, `motivates`, `specifies`, `evidences`, `interprets`, `transitions`, `duplicates`, `jumps`, or `none`. |
| `next_sentence_relation` | Expected relation to next sentence, using the same vocabulary. |
| `claim_type` | `descriptive`, `comparative`, `causal`, `novelty`, `method`, `measurement`, `generalization`, `limitation`, or `bounded empirical interpretation`. |
| `claim_strength` | `none`, `low`, `medium`, `high`, or `very_high`. |
| `evidence_anchor` | `Fig. X`, `Table X`, `Equation X`, `Citation [X]`, `Experiment setup`, `Prior definition`, or `None`. |
| `citation_anchor` | Citation keys or citation cluster if present. |
| `figure_table_anchor` | Figure/table references if present. |
| `technical_terms` | Domain terms worth normalizing. |
| `hedging_words` | Words such as `may`, `can`, `suggest`, `under`, `within`. |
| `risk_words` | Strong, vague, or AI-like words that may overstate the claim. |
| `punctuation_pattern` | Counts and notable punctuation marks. |
| `sentence_skeleton` | Reusable rhetorical skeleton, such as `To isolate X from Y, we construct Z.` |
| `expected_topvenue_role` | Corpus-supported role expected at this position. |
| `mismatch_type` | Missing, repeated, overloaded, unsupported, order, punctuation, AI-like, or none. |
| `revision_operation` | Operation such as `SPLIT_SENTENCE`, `WEAKEN_CLAIM`, `ADD_BOUNDARY`, or `ADD_EVIDENCE_ANCHOR`. |

