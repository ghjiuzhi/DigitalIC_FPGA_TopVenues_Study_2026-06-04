import importlib.util
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


if __name__ == "__main__":
    unittest.main()
