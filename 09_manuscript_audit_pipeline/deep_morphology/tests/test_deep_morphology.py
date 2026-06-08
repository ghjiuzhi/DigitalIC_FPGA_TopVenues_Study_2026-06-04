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


if __name__ == "__main__":
    unittest.main()
