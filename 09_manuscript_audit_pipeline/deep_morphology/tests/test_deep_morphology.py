import importlib.util
import os
import stat
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "audit_deep_morphology.py"


def load_module():
    spec = importlib.util.spec_from_file_location("audit_deep_morphology", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DeepMorphologyTests(unittest.TestCase):
    def test_punctuation_pattern_counts_sentence_marks(self):
        module = load_module()
        pattern = module.punctuation_pattern(
            "Fig. 3 shows sampler-side effects under W4-W5; however, this does not prove universality."
        )
        self.assertEqual(pattern["hyphen_count"], 2)
        self.assertEqual(pattern["semicolon_count"], 1)
        self.assertEqual(pattern["em_dash_count"], 0)

    def test_claim_strength_detects_risky_verb(self):
        module = load_module()
        claim_type, claim_strength = module.classify_claim(
            "These results prove that sampler-side implementation determines the entropy boundary."
        )
        self.assertIn("causal", claim_type)
        self.assertEqual(claim_strength, "very_high")

    def test_sentence_skeleton_masks_entities(self):
        module = load_module()
        skeleton = module.sentence_skeleton(
            "To isolate sampler-side routing from data-RO placement, we construct controlled variants."
        )
        self.assertIn("To isolate X from Y", skeleton)

    def test_topvenue_profile_explains_counts_and_imitation_rules(self):
        module = load_module()
        corpus = [
            {
                "venue": "TCAS-I",
                "section_type": "Abstract",
                "sentence_function": "RESULT",
                "claim_type": "measurement",
                "claim_strength": "medium",
                "has_number": "True",
                "has_figure_reference": "False",
                "has_table_reference": "False",
                "punctuation_pattern": "comma_count=1",
                "transition_pattern": "RESULT/INTERPRET",
            },
            {
                "venue": "TCHES/CHES",
                "section_type": "Results",
                "sentence_function": "SETUP",
                "claim_type": "method",
                "claim_strength": "low",
                "has_number": "False",
                "has_figure_reference": "True",
                "has_table_reference": "False",
                "punctuation_pattern": "",
                "transition_pattern": "METHOD/SETUP",
            },
        ]
        manuscript = [{"dummy": "row"}]

        text = module.build_topvenue_profile_text(corpus, manuscript)

        self.assertIn("句子/功能单元数量", text)
        self.assertIn("不是论文数量", text)
        self.assertIn("顶刊怎么写", text)
        self.assertIn("RO-TRNG 仿写", text)
        self.assertIn("RESULT 154 条", text)
        self.assertIn("TCAS-I/TCAS-II", text)
        self.assertIn("TCHES/CHES", text)

    def test_write_csv_skips_unchanged_readonly_file(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "records.csv"
            fields = ["name", "value"]
            rows = [{"name": "RESULT", "value": "154"}]
            path.write_bytes(module.render_csv_text(fields, rows).encode("utf-8-sig"))
            os.chmod(path, stat.S_IREAD)
            try:
                module.write_csv(path, fields, rows)
            finally:
                os.chmod(path, stat.S_IWRITE | stat.S_IREAD)

    def test_abstract_complete_chain_classifies_as_abs_a(self):
        module = load_module()
        result = module.classify_section_archetype(
            "Abstract",
            ["BG", "PROBLEM", "GAP", "METHOD", "SETUP", "RESULT", "INTERPRET"],
            "full_sequence",
        )
        self.assertEqual(result["archetype_id"], "ABS_A")
        self.assertIn("完整摘要链", result["archetype_name"])

    def test_results_single_sentence_is_partial_evidence(self):
        module = load_module()
        result = module.classify_section_archetype("Results", ["RESULT"], "partial/notes-derived")
        self.assertEqual(result["archetype_id"], "RES_X")
        self.assertIn("部分证据", result["archetype_name"])
        self.assertEqual(result["evidence_quality"], "partial/notes-derived")

    def test_function_counts_are_formatted_for_reading(self):
        module = load_module()
        text = module.format_function_counts({"RESULT": 3, "SETUP": 1})
        self.assertEqual(text, "RESULT=3; SETUP=1")

    def test_venue_preference_labels_strong_and_mixed(self):
        module = load_module()
        strong_rows = [
            {"venue": "TCAS-I", "section_type": "Abstract", "archetype_id": "ABS_A", "archetype_name": "完整摘要链", "sentence_count": "7", "function_counts": "RESULT=2", "paper_id": f"p{i}", "evidence_quality": "full_sequence"}
            for i in range(6)
        ] + [
            {"venue": "TCAS-I", "section_type": "Abstract", "archetype_id": "ABS_C", "archetype_name": "方法-验证-结果型", "sentence_count": "6", "function_counts": "RESULT=3", "paper_id": f"q{i}", "evidence_quality": "full_sequence"}
            for i in range(4)
        ]
        mixed_rows = [
            {"venue": "TC", "section_type": "Abstract", "archetype_id": "ABS_A", "archetype_name": "完整摘要链", "sentence_count": "7", "function_counts": "RESULT=2", "paper_id": f"a{i}", "evidence_quality": "full_sequence"}
            for i in range(4)
        ] + [
            {"venue": "TC", "section_type": "Abstract", "archetype_id": "ABS_C", "archetype_name": "方法-验证-结果型", "sentence_count": "6", "function_counts": "RESULT=3", "paper_id": f"b{i}", "evidence_quality": "full_sequence"}
            for i in range(3)
        ] + [
            {"venue": "TC", "section_type": "Abstract", "archetype_id": "ABS_D", "archetype_name": "结果密集型", "sentence_count": "6", "function_counts": "RESULT=4", "paper_id": f"c{i}", "evidence_quality": "full_sequence"}
            for i in range(3)
        ]

        matrix = module.build_venue_archetype_matrix(strong_rows + mixed_rows)
        notes = {(row["venue"], row["archetype_id"]): row["note"] for row in matrix}

        self.assertIn("strong_preference", notes[("TCAS-I", "ABS_A")])
        self.assertIn("mixed_preference", notes[("TC", "ABS_A")])

    def test_profile_includes_venue_archetype_language(self):
        module = load_module()
        corpus = []
        for i in range(6):
            for j, function in enumerate(["BG", "PROBLEM", "GAP", "METHOD", "RESULT", "INTERPRET"], start=1):
                corpus.append(
                    {
                        "paper_id": f"p{i}",
                        "title": f"Paper {i}",
                        "venue": "TCAS-I",
                        "year": "2026",
                        "section_type": "Abstract",
                        "sentence_index": str(j),
                        "sentence_function": function,
                        "has_number": "False",
                        "has_figure_reference": "False",
                        "has_table_reference": "False",
                        "confidence": "high",
                    }
                )
        text = module.build_topvenue_profile_text(corpus, [])
        self.assertIn("不是完全统一", text)
        self.assertIn("venue 偏好", text)
        self.assertIn("强倾向", text)
        self.assertIn("有几篇属于这种组织方式", text)

    def test_corpus_noise_filter_removes_metadata_and_fragments(self):
        module = load_module()
        noisy = [
            "Manuscript received 1 January 2024; revised 2 March 2024.",
            "This work was supported in part by the National Science Foundation.",
            "E-mail: author@example.com",
            "0 0.2 0.4 0.6 0.8",
            "Voltage Time Entropy Restart",
            "The proposed TRNG is evaluated on FPGA devices under controlled placement.",
        ]

        kept, removed, stats = module.filter_corpus_units(
            [{"unit_text_short": text, "section_type": "Introduction"} for text in noisy]
        )

        self.assertEqual(len(kept), 1)
        self.assertIn("controlled placement", kept[0]["unit_text_short"])
        self.assertGreaterEqual(stats["removed_total"], 5)
        self.assertIn("manuscript_metadata", stats["removed_by_reason"])

    def test_revision_operation_blocks_false_keep_for_jumps_and_missing_evidence(self):
        module = load_module()
        mismatch, operation = module.mismatch_and_operation(
            "RESULT",
            "medium",
            "None",
            [],
            {},
            previous_sentence_relation="jumps",
            expected_role="METHOD",
            section_type="Abstract",
        )

        self.assertNotEqual(operation, "KEEP")
        self.assertIn("ADD_BRIDGE", operation)
        self.assertIn("ADD_EVIDENCE_ANCHOR", operation)
        self.assertIn("REFUNCTION_SENTENCE", operation)

    def test_anchor_extraction_ignores_latex_position_brackets(self):
        module = load_module()
        anchor = module.anchors(r"\begin{figure}[t]\includegraphics[width=.9\linewidth]{x}\end{figure}")
        self.assertFalse(anchor["has_citation"])
        self.assertEqual(anchor["citation_anchor"], "None")

    def test_clause_records_flag_overloaded_sentence(self):
        module = load_module()
        sentence = {
            "sentence_id": "RESULTS.P1.S1",
            "section_id": "Results",
            "sentence_text": "Although the design passes NIST tests, the sampler-side placement changes the entropy estimate, which suggests a boundary condition, and the result should not be generalized.",
            "claim_strength": "medium",
            "dominant_function": "RESULT",
            "evidence_anchor": "None",
            "risk_words": "generalized",
            "punctuation_pattern": "comma_count=4",
        }

        clauses = module.clause_records([sentence])

        self.assertGreaterEqual(len(clauses), 2)
        self.assertTrue(any(row["recommended_action"] != "KEEP" for row in clauses))
        self.assertTrue(any("multi_claim" in row["issue"] or "hidden_boundary" in row["issue"] for row in clauses))

    def test_figure_table_inventory_extracts_caption_and_first_mention(self):
        module = load_module()
        tex = r"""
        Figure~\ref{fig:flow} shows the audit workflow and the body explains the takeaway.
        \begin{figure}
        \caption{Audit workflow under controlled restart conditions.}
        \label{fig:flow}
        \end{figure}
        \begin{table}
        \caption{Entropy comparison across placements.}
        \label{tab:entropy}
        \end{table}
        """
        manuscript = [
            {
                "sentence_id": "INTRO.P1.S1",
                "sentence_text": "Figure fig:flow shows the audit workflow and the body explains the takeaway.",
                "figure_table_anchor": "Figure fig:flow",
            }
        ]

        inventory = module.figure_table_inventory(tex, manuscript)

        ids = {row["id"] for row in inventory}
        self.assertIn("fig:flow", ids)
        self.assertIn("tab:entropy", ids)
        fig = next(row for row in inventory if row["id"] == "fig:flow")
        self.assertEqual(fig["first_mention_sentence_id"], "INTRO.P1.S1")
        self.assertIn("OBJECT", fig["caption_function_sequence"])

    def test_gold_label_template_samples_50_sentences(self):
        module = load_module()
        manuscript = [
            {
                "sentence_id": f"ABS.S{i}",
                "section_id": "Abstract" if i < 20 else "Results",
                "sentence_text": f"Sentence {i} reports a controlled result.",
                "dominant_function": "RESULT",
                "claim_type": "measurement",
                "revision_operation": "ADD_EVIDENCE_ANCHOR",
            }
            for i in range(60)
        ]

        rows = module.gold_label_template_records(manuscript, [])

        self.assertEqual(len(rows), 50)
        self.assertIn("gold_function", rows[0])
        self.assertEqual(rows[0]["gold_action"], "")


if __name__ == "__main__":
    unittest.main()
