import csv
import io
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_DIR = Path(__file__).resolve().parent
TOPVENUE_MATRIX = ROOT / "07_writing_assets" / "micro_style_audit_assets" / "topvenue_sentence_function_matrix.csv"
ACTIVE_MANUSCRIPTS = ROOT / "08_topic_layers" / "ROTRNG" / "metadata" / "active_manuscripts.csv"

STRONG_WORDS = {
    "prove",
    "proves",
    "proven",
    "demonstrate",
    "demonstrates",
    "determine",
    "determines",
    "guarantee",
    "guarantees",
    "validate",
    "validates",
    "confirm",
    "confirms",
    "ensure",
    "ensures",
    "always",
    "never",
    "universal",
    "optimal",
    "robust",
    "novel",
    "fundamental",
}
AI_WORDS = {
    "highlight",
    "highlights",
    "underscore",
    "underscores",
    "valuable insight",
    "important implication",
    "it is worth noting",
    "furthermore",
    "moreover",
    "additionally",
    "clearly",
    "obviously",
    "we can see",
}
VAGUE_WORDS = {"some", "many", "various", "several", "good", "better", "large", "small", "high", "low", "significant", "substantial", "effective"}
HEDGE_WORDS = {"may", "might", "can", "could", "suggest", "suggests", "indicate", "indicates", "under", "within", "consistent", "evaluated"}

SENTENCE_FIELDS = [
    "section_id",
    "subsection_id",
    "paragraph_id",
    "sentence_id",
    "sentence_text",
    "sentence_position",
    "dominant_function",
    "secondary_function",
    "previous_sentence_relation",
    "next_sentence_relation",
    "claim_type",
    "claim_strength",
    "evidence_anchor",
    "citation_anchor",
    "figure_table_anchor",
    "technical_terms",
    "hedging_words",
    "risk_words",
    "punctuation_pattern",
    "sentence_skeleton",
    "expected_topvenue_role",
    "mismatch_type",
    "revision_operation",
]

CORPUS_FIELDS = [
    "paper_id",
    "venue",
    "section_type",
    "paragraph_index",
    "sentence_index",
    "sentence_text",
    "sentence_function",
    "sentence_skeleton",
    "claim_type",
    "claim_strength",
    "has_citation",
    "has_number",
    "has_figure_reference",
    "has_table_reference",
    "hedging_pattern",
    "punctuation_pattern",
    "transition_pattern",
]

PAPER_ARCHETYPE_FIELDS = [
    "paper_id",
    "title",
    "venue",
    "year",
    "section_type",
    "sentence_count",
    "exact_sequence",
    "collapsed_sequence",
    "archetype_id",
    "archetype_name",
    "function_counts",
    "evidence_quality",
]

VENUE_ARCHETYPE_FIELDS = [
    "section_type",
    "venue",
    "archetype_id",
    "archetype_name",
    "paper_count",
    "total_papers",
    "share",
    "avg_sentence_count",
    "avg_function_counts",
    "representative_papers",
    "evidence_quality",
    "note",
]

CITATION_FIELDS = [
    "sentence_id",
    "section_id",
    "citation_anchor",
    "citation_function",
    "sentence_function",
    "claim_type",
    "claim_strength",
    "issue",
]

CLAUSE_FIELDS = [
    "sentence_id",
    "clause_index",
    "clause_text",
    "clause_type",
    "function",
    "claim_type",
    "claim_strength",
    "evidence_support",
    "risk_words",
    "issue",
    "recommended_action",
]

FIGURE_TABLE_FIELDS = [
    "id",
    "kind",
    "caption",
    "caption_sentence_count",
    "caption_function_sequence",
    "first_mention_sentence_id",
    "distance_from_first_mention",
    "role",
    "body_claim_linked",
    "body_explains_what_to_look_for",
    "body_quantifies_after_reference",
    "caption_body_consistency",
    "table_note_needed",
    "unit_or_abbreviation_issue",
    "caption_storyline_note",
]

GOLD_LABEL_FIELDS = [
    "sentence_id",
    "sentence_text",
    "model_function",
    "gold_function",
    "model_claim_type",
    "gold_claim_type",
    "model_action",
    "gold_action",
    "notes",
]

CORPUS_QUALITY = {}

FUNCTION_ZH = {
    "BG": "背景",
    "PROBLEM": "问题",
    "GAP": "缺口",
    "NEED": "必要性",
    "METHOD": "方法",
    "SETUP": "实验/平台设置",
    "RESULT": "结果",
    "OBSERVATION": "观察",
    "QUANTIFICATION": "定量结果",
    "INTERPRET": "解释",
    "INTERPRETATION": "解释",
    "BOUNDARY": "边界",
    "CONTRIB": "贡献",
    "CONTRIBUTION": "贡献",
    "ORG": "结构安排",
    "ORGANIZATION": "结构安排",
}

RELATION_ZH = {
    "none": "无上一句",
    "contrasts": "转折/对比上一句",
    "narrows": "收窄上一句",
    "interprets": "解释上一句结果",
    "evidences": "用证据承接上一句",
    "elaborates": "展开上一句",
    "jumps": "跳跃，缺少桥接",
}

CLAIM_ZH = {
    "descriptive": "描述性 claim",
    "causal/generalization": "因果/泛化 claim",
    "comparative": "比较 claim",
    "method": "方法 claim",
    "measurement": "测量/结果 claim",
    "limitation": "限制/边界 claim",
    "novelty": "新颖性 claim",
}

STRENGTH_ZH = {
    "none": "无明显 claim",
    "low": "低",
    "medium": "中",
    "high": "高",
    "very_high": "很高",
}

OPERATION_ZH = {
    "KEEP": "保留",
    "DELETE": "删除",
    "MERGE_WITH_PREVIOUS": "并入上一句",
    "SPLIT_SENTENCE": "拆句",
    "MOVE_BEFORE": "前移",
    "MOVE_AFTER": "后移",
    "REFUNCTION_SENTENCE": "重写句子功能",
    "REORDER_SENTENCE": "调整句子顺序",
    "ADD_BRIDGE": "补桥接句/桥接短语",
    "ADD_EVIDENCE_ANCHOR": "补证据锚点",
    "ADD_CITATION": "补引用",
    "ADD_QUANTIFICATION": "补定量结果",
    "WEAKEN_CLAIM": "削弱 claim",
    "REPLACE_RISK_VERB": "替换高风险动词/泛词",
    "NORMALIZE_TERM": "统一术语",
    "CHANGE_PUNCTUATION": "调整标点",
    "ADD_TABLE_NOTE": "补表格 note",
    "REWRITE_CAPTION": "重写 caption",
    "MOVE_TO_DISCUSSION": "移到 Discussion",
    "MOVE_TO_METHOD": "移到 Method",
    "MOVE_TO_RELATED_WORK": "移到 Related Work",
    "ADD_BOUNDARY": "补边界条件",
    "CHECK_CAPTION_BODY_LINK": "检查 caption 与正文 claim 绑定",
}


def zh_function(value):
    return FUNCTION_ZH.get(value, value)


def zh_relation(value):
    return RELATION_ZH.get(value, value)


def zh_claim(value):
    return CLAIM_ZH.get(value, value)


def zh_strength(value):
    return STRENGTH_ZH.get(value, value)


def zh_operations(value):
    return "；".join(OPERATION_ZH.get(part, part) for part in value.split(";") if part) or "保留"


def zh_evidence(value):
    if not value or value == "None":
        return "无"
    mapping = {
        "Figure": "图",
        "Table": "表",
        "Equation": "公式",
        "Citation": "引用",
        "Experiment setup": "实验设置",
    }
    return "；".join(mapping.get(part, part) for part in value.split(";"))


def read_text(path):
    for encoding in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            return Path(path).read_text(encoding=encoding, errors="ignore")
        except Exception:
            continue
    return ""


def clean_text(text):
    text = re.sub(r"%.*", "", text)
    text = re.sub(r"\\cite\w*\*?(?:\[[^\]]*\])?\{([^{}]*)\}", r"[\1]", text)
    text = re.sub(r"\\ref\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\(?:label|emph|textbf|textit|SI|num)\*?(?:\[[^\]]*\])?\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", " ", text)
    text = text.replace("~", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def punctuation_pattern(sentence):
    return {
        "hyphen_count": sentence.count("-") - sentence.count("--"),
        "en_dash_count": sentence.count("–"),
        "em_dash_count": sentence.count("—") + sentence.count("---"),
        "semicolon_count": sentence.count(";"),
        "colon_count": sentence.count(":"),
        "question_mark_count": sentence.count("?"),
        "parentheses_count": sentence.count("(") + sentence.count(")"),
        "slash_count": sentence.count("/"),
        "comma_count": sentence.count(","),
    }


def punctuation_pattern_text(sentence):
    p = punctuation_pattern(sentence)
    return "; ".join(f"{k}={v}" for k, v in p.items() if v)


def words_present(sentence, vocabulary):
    lower = sentence.lower()
    return sorted(term for term in vocabulary if re.search(rf"\b{re.escape(term)}\b", lower))


def corpus_noise_reason(text, section_type=""):
    raw = text or ""
    clean = clean_text(raw)
    lower = clean.lower()
    tokens = re.findall(r"[A-Za-z0-9]+", clean)
    if not clean or len(clean) < 12:
        return "too_short_or_empty"
    if re.search(r"\bmanuscript\s+(received|revised|accepted)\b", lower):
        return "manuscript_metadata"
    if re.search(r"\b(this work was supported|supported in part|funding|grant|corresponding author)\b", lower):
        return "funding_or_correspondence"
    if re.search(r"\b(e-?mail|email|@|affiliation|department of|school of|university|institute of)\b", lower):
        return "affiliation_or_email"
    if section_type == "Contribution":
        return ""
    if re.search(r"[\u4e00-\u9fff]", clean):
        return ""
    if re.search(r"\bfig(?:ure)?\.?\s*\d+\b", lower) and len(tokens) < 8:
        return "figure_fragment"
    if re.search(r"\b(table|row|column|axis|legend|xlabel|ylabel)\b", lower) and len(tokens) < 10:
        return "table_or_figure_fragment"
    if re.fullmatch(r"[\d\s,.;:+\-/%()]+", clean):
        return "numeric_or_punctuation_fragment"
    if tokens:
        short_tokens = sum(1 for token in tokens if len(token) <= 2)
        digit_tokens = sum(1 for token in tokens if re.fullmatch(r"\d+(?:\.\d+)?", token))
        if digit_tokens / len(tokens) > 0.45:
            return "numeric_or_punctuation_fragment"
        if short_tokens / len(tokens) > 0.70 and len(tokens) >= 5:
            return "single_letter_or_axis_tokens"
    if re.search(r"(?:[A-Za-z]\s){6,}[A-Za-z]", clean):
        return "abnormal_character_spacing"
    if section_type not in {"FigureCaption", "TableCaption"} and re.match(r"(?i)^(fig\.|figure|table)\s+\d+", clean):
        return "caption_or_caption_fragment"
    if len(tokens) < 5 and not re.search(r"[.!?]$", clean):
        return "ocr_fragment"
    return ""


def filter_corpus_units(rows):
    kept = []
    removed = []
    removed_by_reason = Counter()
    retained_by_section = Counter()
    for row in rows:
        reason = corpus_noise_reason(row.get("unit_text_short") or row.get("sentence_text") or "", row.get("section_type", ""))
        if reason:
            removed_row = dict(row)
            removed_row["remove_reason"] = reason
            removed.append(removed_row)
            removed_by_reason[reason] += 1
        else:
            kept.append(row)
            retained_by_section[row.get("section_type", "")] += 1
    stats = {
        "raw_total": len(rows),
        "retained_total": len(kept),
        "removed_total": len(removed),
        "removed_by_reason": dict(removed_by_reason),
        "retained_by_section": dict(retained_by_section),
    }
    return kept, removed, stats


def classify_claim(sentence):
    lower = sentence.lower()
    claim_type = "descriptive"
    if re.search(r"\b(prove|demonstrat|determin|affect|cause|lead|change|influence)\w*\b", lower):
        claim_type = "causal/generalization"
    elif re.search(r"\b(compared|outperform|higher|lower|faster|slower|reduce|improve)\w*\b", lower):
        claim_type = "comparative"
    elif re.search(r"\b(propose|present|design|construct|implement|evaluate|characterize)\w*\b", lower):
        claim_type = "method"
    elif re.search(r"\b(measure|observ|result|show|indicate|suggest)\w*\b", lower):
        claim_type = "measurement"
    elif re.search(r"\b(limit|under|within|scope|condition)\w*\b", lower):
        claim_type = "limitation"
    elif re.search(r"\b(novel|new|first)\b", lower):
        claim_type = "novelty"

    if words_present(sentence, {"prove", "proves", "determine", "determines", "guarantee", "guarantees", "always", "never", "universal"}):
        claim_strength = "very_high"
    elif words_present(sentence, STRONG_WORDS):
        claim_strength = "high"
    elif re.search(r"\b(show|shows|indicate|indicates|suggest|suggests|support|supports|can|may)\b", lower):
        claim_strength = "medium"
    elif len(sentence.split()) > 8:
        claim_strength = "low"
    else:
        claim_strength = "none"
    return claim_type, claim_strength


def sentence_skeleton(sentence):
    s = clean_text(sentence)
    if re.match(r"(?i)^to isolate .+ from .+, we (construct|use|evaluate|compare)", s):
        return "To isolate X from Y, we construct Z."
    if re.match(r"(?i)^although .+, .+ remains .+", s):
        return "Although X, Y remains Z."
    if re.search(r"(?i)prior work .* focused on .* whereas .* remains", s):
        return "Prior work has focused on X, whereas Y remains less characterized."
    if re.match(r"(?i)^fig(?:ure)?\.? \d+ .* shows ", s):
        return "Fig. X shows Y under Z."
    if re.match(r"(?i)^these results (suggest|indicate|show)", s):
        return "These results suggest X under Y."
    if re.search(r"(?i)under .* conditions?", s):
        return "X holds under Y conditions."
    if re.search(r"(?i)we (propose|present|design|evaluate|characterize)", s):
        return "We METHOD X under Y."
    if re.search(r"(?i)(however|nevertheless|whereas)", s):
        return "X, however/whereas Y."
    return re.sub(r"\b[A-Z][A-Za-z0-9\-]*\b", "X", s)[:160]


def dominant_function(sentence, section_type=""):
    lower = sentence.lower()
    if section_type == "Abstract" and re.search(r"\b(however|challenge|problem|limited|bottleneck)\b", lower):
        return "PROBLEM"
    if re.search(r"\b(gap|remain|insufficient|less characterized|not fully|unclear)\b", lower):
        return "GAP"
    if re.search(r"\b(to address|therefore|motivates|need)\b", lower):
        return "NEED"
    if re.search(r"\b(we propose|we present|we design|we construct|we evaluate|we characterize|this paper)\b", lower):
        return "METHOD"
    if re.search(r"\b(fpga|setup|platform|experiment|measurement|benchmark|variant|toolchain|placement|routing)\b", lower):
        return "SETUP"
    if re.search(r"\b(fig\.|figure|table|results?|show|shows|observed|measured|achieves|reduces|increases)\b", lower):
        return "RESULT"
    if re.search(r"\b(indicate|suggest|consistent|imply|because|therefore)\b", lower):
        return "INTERPRETATION"
    if re.search(r"\b(under|within|scope|condition|limitation|future)\b", lower):
        return "BOUNDARY"
    if re.search(r"\b(contribution|contributes)\b", lower):
        return "CONTRIBUTION"
    if re.search(r"\b(section|organized|remainder)\b", lower):
        return "ORGANIZATION"
    return "BG"


def relation(prev_sentence, sentence):
    if not prev_sentence:
        return "none"
    lower = sentence.lower()
    if re.search(r"\b(however|whereas|in contrast|nevertheless)\b", lower):
        return "contrasts"
    if re.search(r"\b(in particular|specifically|to isolate|for this purpose)\b", lower):
        return "narrows"
    if re.search(r"\b(these results|this observation|therefore|thus)\b", lower):
        return "interprets"
    if re.search(r"\b(fig\.|figure|table|results show)\b", lower):
        return "evidences"
    if re.search(r"\b(furthermore|moreover|additionally)\b", lower):
        return "elaborates"
    prev_terms = set(re.findall(r"[A-Za-z][A-Za-z\-]{4,}", prev_sentence.lower()))
    terms = set(re.findall(r"[A-Za-z][A-Za-z\-]{4,}", lower))
    if prev_terms and len(prev_terms & terms) == 0:
        return "jumps"
    return "elaborates"


def anchors(sentence):
    citations = re.findall(r"\\cite\w*\{([^{}]+)\}", sentence)
    bracket_candidates = re.findall(r"\[([A-Za-z0-9_,:;_\-\s]+)\]", sentence)
    citations.extend(candidate for candidate in bracket_candidates if is_citation_bracket(candidate))
    figures = re.findall(r"(?:Fig\.|Figure|Figs\.)\s*~?\\?ref\{[^{}]+\}|(?:Fig\.|Figure|Figs\.)\s*[A-Za-z0-9_:.\-]+", sentence)
    tables = re.findall(r"(?:Table|Tables)\s*~?\\?ref\{[^{}]+\}|(?:Table|Tables)\s*[A-Za-z0-9_:.\-]+", sentence)
    equations = re.findall(r"(?:Eq\.|Equation)\s*~?\\?ref\{[^{}]+\}|(?:Eq\.|Equation)\s*[A-Za-z0-9_:.\-]+", sentence)
    evidence = []
    if figures:
        evidence.append("Figure")
    if tables:
        evidence.append("Table")
    if equations:
        evidence.append("Equation")
    if citations:
        evidence.append("Citation")
    if re.search(r"\bexperiment|measurement|setup|variant|platform\b", sentence, re.I):
        evidence.append("Experiment setup")
    return {
        "citation_anchor": ";".join(c for c in citations if c) or "None",
        "figure_table_anchor": ";".join(figures + tables) or "None",
        "evidence_anchor": ";".join(evidence) if evidence else "None",
        "has_citation": bool(citations),
        "has_figure": bool(figures),
        "has_table": bool(tables),
    }


def is_citation_bracket(value):
    text = value.strip()
    if not text:
        return False
    if text.lower() in {"t", "b", "h", "ht", "htbp", "right", "left", "above", "below", "width", "scale"}:
        return False
    if "=" in text or "\\" in text:
        return False
    if re.fullmatch(r"\d+(?:\s*[-,;]\s*\d+)*", text):
        return False
    if ":" in text or "," in text or re.search(r"\b(?:20\d{2}|19\d{2}|nist|ieee|ches|tcas|tcad|tvlsi)\b", text, re.I):
        return True
    return False


def expected_role_matches(function, expected_role):
    if not expected_role or expected_role == "SECTION_SPECIFIC":
        return True
    norm_function = function.replace("INTERPRETATION", "INTERPRET").replace("CONTRIBUTION", "CONTRIB").replace("ORGANIZATION", "ORG")
    expected_tokens = set(re.findall(r"[A-Z_]+", expected_role.replace("FIGURE_TABLE", "RESULT")))
    if not expected_tokens:
        return True
    if norm_function in expected_tokens:
        return True
    if norm_function == "RESULT" and {"OBSERVATION", "QUANTIFICATION", "FIGURE", "TABLE"} & expected_tokens:
        return True
    return False


def mismatch_and_operation(
    function,
    claim_strength,
    evidence_anchor,
    risk_words,
    punctuation,
    previous_sentence_relation="",
    expected_role="",
    section_type="",
):
    issues = []
    operations = []
    if previous_sentence_relation == "jumps":
        issues.append("sentence_jump")
        operations.append("ADD_BRIDGE")
    if claim_strength in {"medium", "high", "very_high"} and evidence_anchor == "None":
        issues.append("unsupported_claim")
        operations.append("ADD_EVIDENCE_ANCHOR")
        if claim_strength in {"high", "very_high"}:
            operations.append("WEAKEN_CLAIM")
    if claim_strength == "very_high":
        issues.append("overstrong_claim")
        operations.append("WEAKEN_CLAIM")
    if risk_words:
        issues.append("risk_word")
        operations.append("REPLACE_RISK_VERB")
    if (
        punctuation.get("em_dash_count", 0)
        or punctuation.get("question_mark_count", 0)
        or punctuation.get("semicolon_count", 0)
        or punctuation.get("colon_count", 0) > 1
        or punctuation.get("comma_count", 0) > 3
    ):
        issues.append("punctuation_issue")
        operations.append("SPLIT_SENTENCE" if punctuation.get("comma_count", 0) > 3 or punctuation.get("semicolon_count", 0) else "CHANGE_PUNCTUATION")
    if section_type in {"Abstract", "Results"} or re.search(r"(?i)result|characterization|counterfactual|diagnosis", section_type or ""):
        if not expected_role_matches(function, expected_role):
            issues.append("role_mismatch")
            operations.append("REFUNCTION_SENTENCE")
            operations.append("REORDER_SENTENCE")
    if function in {"INTERPRETATION", "BOUNDARY"} and evidence_anchor == "None":
        operations.append("ADD_BOUNDARY")
    return ";".join(dict.fromkeys(issues)) or "none", ";".join(dict.fromkeys(operations)) or "KEEP"


def split_latex_sections(tex_text):
    abstract_match = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex_text, flags=re.S)
    sections = []
    if abstract_match:
        sections.append(("Abstract", abstract_match.group(1)))
    for match in re.finditer(r"\\section\{([^{}]+)\}", tex_text):
        start = match.end()
        next_match = re.search(r"\\section\{[^{}]+\}", tex_text[start:], flags=re.S)
        end = start + next_match.start() if next_match else len(tex_text)
        sections.append((clean_text(match.group(1)), tex_text[start:end]))
    return sections


def split_paragraphs(section_text):
    chunks = re.split(r"\n\s*\n", section_text)
    return [clean_text(chunk) for chunk in chunks if len(clean_text(chunk)) > 40 and not clean_text(chunk).startswith("\\")]


def split_sentences(paragraph):
    paragraph = clean_text(paragraph)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(])", paragraph)
    return [part.strip() for part in parts if len(part.strip()) > 25]


def expected_role(section_type, position):
    if section_type == "Abstract":
        seq = ["BG", "PROBLEM", "GAP", "METHOD", "SETUP", "RESULT", "BOUNDARY"]
        return seq[min(position - 1, len(seq) - 1)]
    lower = section_type.lower()
    if "introduction" in lower:
        return "BG/PROBLEM/GAP/METHOD/CONTRIBUTION"
    if "result" in lower or "characterization" in lower or "counterfactual" in lower:
        return "QUESTION/FIGURE_TABLE/OBSERVATION/QUANTIFICATION/INTERPRETATION/BOUNDARY"
    if "discussion" in lower:
        return "FINDING_SYNTHESIS/ALTERNATIVE_EXPLANATION/LIMITATION/IMPLICATION"
    if "conclusion" in lower:
        return "PROBLEM_RECAP/METHOD_RECAP/FINDING/BOUNDARY"
    return "SECTION_SPECIFIC"


def manuscript_records(manuscript_path):
    tex = read_text(manuscript_path)
    records = []
    for section_title, body in split_latex_sections(tex):
        section_slug = re.sub(r"[^A-Za-z0-9]+", "_", section_title).strip("_").upper() or "SEC"
        for p_index, paragraph in enumerate(split_paragraphs(body), 1):
            sentences = split_sentences(paragraph)
            previous = ""
            for s_index, sentence in enumerate(sentences, 1):
                clean_sentence = clean_text(sentence)
                punc = punctuation_pattern(clean_sentence)
                claim_type, claim_strength = classify_claim(clean_sentence)
                anchor = anchors(sentence)
                risk = sorted(set(words_present(clean_sentence, STRONG_WORDS | AI_WORDS | VAGUE_WORDS)))
                hedge = sorted(set(words_present(clean_sentence, HEDGE_WORDS)))
                function = dominant_function(clean_sentence, section_title)
                sentence_id = f"{section_slug}.P{p_index}.S{s_index}" if section_title != "Abstract" else f"ABS.S{s_index}"
                prev_relation = relation(previous, clean_sentence)
                expected = expected_role(section_title, s_index)
                mismatch, operation = mismatch_and_operation(
                    function,
                    claim_strength,
                    anchor["evidence_anchor"],
                    risk,
                    punc,
                    previous_sentence_relation=prev_relation,
                    expected_role=expected,
                    section_type=section_title,
                )
                records.append(
                    {
                        "section_id": section_title,
                        "subsection_id": "",
                        "paragraph_id": f"{section_slug}.P{p_index}",
                        "sentence_id": sentence_id,
                        "sentence_text": clean_sentence,
                        "sentence_position": s_index,
                        "dominant_function": function,
                        "secondary_function": "",
                        "previous_sentence_relation": prev_relation,
                        "next_sentence_relation": "",
                        "claim_type": claim_type,
                        "claim_strength": claim_strength,
                        "evidence_anchor": anchor["evidence_anchor"],
                        "citation_anchor": anchor["citation_anchor"],
                        "figure_table_anchor": anchor["figure_table_anchor"],
                        "technical_terms": ";".join(sorted(set(re.findall(r"\b(?:FPGA|TRNG|RO|RTL|TDC|LOC|BEL|NIST|restart|sampler|entropy)\b", clean_sentence, re.I)))),
                        "hedging_words": ";".join(hedge),
                        "risk_words": ";".join(risk),
                        "punctuation_pattern": punctuation_pattern_text(clean_sentence),
                        "sentence_skeleton": sentence_skeleton(clean_sentence),
                        "expected_topvenue_role": expected,
                        "mismatch_type": mismatch,
                        "revision_operation": operation,
                    }
                )
                previous = clean_sentence
    return records


def corpus_records():
    global CORPUS_QUALITY
    raw_rows = []
    with TOPVENUE_MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            raw_rows.append(row)
    clean_rows, removed_rows, stats = filter_corpus_units(raw_rows)
    stats["removed_examples"] = [
        {"text": row.get("unit_text_short", ""), "reason": row.get("remove_reason", ""), "section_type": row.get("section_type", "")}
        for row in removed_rows[:20]
    ]
    stats["retained_examples"] = [
        {"text": row.get("unit_text_short", ""), "section_type": row.get("section_type", "")}
        for row in clean_rows[:20]
    ]
    CORPUS_QUALITY = stats

    records = []
    for row in clean_rows:
            sentence = row["unit_text_short"]
            claim_type, claim_strength = classify_claim(sentence)
            anchor = anchors(sentence)
            records.append(
                {
                    "paper_id": row["paper_id"],
                    "title": row.get("title", ""),
                    "venue": row["venue"],
                    "year": row.get("year", ""),
                    "section_type": row["section_type"],
                    "paragraph_index": "",
                    "sentence_index": row["unit_index"],
                    "sentence_text": sentence,
                    "sentence_function": row["function_label"],
                    "sentence_skeleton": sentence_skeleton(sentence),
                    "claim_type": claim_type,
                    "claim_strength": claim_strength,
                    "has_citation": anchor["has_citation"],
                    "has_number": bool(re.search(r"\d", sentence)),
                    "has_figure_reference": anchor["has_figure"],
                    "has_table_reference": anchor["has_table"],
                    "hedging_pattern": ";".join(words_present(sentence, HEDGE_WORDS)),
                    "punctuation_pattern": punctuation_pattern_text(sentence),
                    "transition_pattern": row["function_chain"],
                    "confidence": row.get("confidence", ""),
                    "evidence_source": row.get("evidence_source", ""),
                }
            )
    return records


def active_manuscript_path():
    with ACTIVE_MANUSCRIPTS.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    main = rows[0]
    base = Path(main["path"]) / "manuscript"
    preferred = base / "main.tex"
    return preferred if preferred.exists() else base / "main_eval_boundary_r23.tex"


def reference_source_candidates(manuscript_path):
    manuscript_path = Path(manuscript_path)
    candidates = [
        manuscript_path.with_suffix(".bbl"),
        manuscript_path.with_suffix(".bib"),
        manuscript_path.parent / "main.bbl",
        manuscript_path.parent / "main.bib",
        manuscript_path.parent.parent / "refs" / "references.bib",
        manuscript_path.parent.parent / "references.bib",
    ]
    seen = set()
    unique = []
    for path in candidates:
        key = str(path).lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(path)
    return unique


def classify_reference_venue(entry):
    text = entry.lower()
    if re.search(r"\btches\b|ches|cryptographic hardware", text):
        return "TCHES/CHES"
    if re.search(r"tcas|circuits and systems", text):
        return "TCAS"
    if re.search(r"tvlsi|very large scale integration|vlsi systems", text):
        return "TVLSI"
    if re.search(r"tcad|computer-aided design", text):
        return "TCAD"
    if re.search(r"\bieee trans|ieee transactions", text):
        return "IEEE Transactions"
    if re.search(r"nist|sp\s*800|special publication", text):
        return "NIST/standard"
    if re.search(r"\bfpga\b|field-programmable", text):
        return "FPGA topic/venue"
    if "arxiv" in text:
        return "arXiv"
    if re.search(r"conference|symposium|workshop", text):
        return "conference/workshop"
    return "other/unknown"


def reference_distribution(manuscript_path):
    source = ""
    text = ""
    for path in reference_source_candidates(manuscript_path):
        if path.exists() and path.stat().st_size > 0:
            source = str(path)
            text = read_text(path)
            break
    if not text:
        return {
            "source": "未定位到可解析 .bbl/.bib",
            "reference_count": 0,
            "year_counts": Counter(),
            "venue_counts": Counter(),
            "missing_core_refs": ["NIST/SP800", "FPGA TRNG", "RO-TRNG", "entropy estimation", "sampler implementation"],
        }
    if source.lower().endswith(".bib"):
        entries = [part for part in re.split(r"\n\s*@", text) if part.strip()]
    else:
        entries = [part for part in re.split(r"\\bibitem(?:\[[^\]]*\])?\{[^{}]*\}", text) if part.strip()]
    year_counts = Counter()
    venue_counts = Counter()
    for entry in entries:
        years = re.findall(r"(?:19|20)\d{2}", entry)
        year_counts[years[-1] if years else "unknown"] += 1
        venue_counts[classify_reference_venue(entry)] += 1
    all_refs = text.lower()
    core_patterns = {
        "NIST/SP800 随机性或熵估计标准": r"nist|sp\s*800|special publication",
        "FPGA TRNG 相关实现": r"\bfpga\b|field-programmable",
        "RO-TRNG / ring oscillator TRNG": r"ring oscillator|ro-?trng|ring-oscillator",
        "entropy estimation / min-entropy": r"entropy|min-entropy",
        "sampler / sampling aperture implementation": r"sampler|sampling aperture|sampling",
    }
    missing = [name for name, pattern in core_patterns.items() if not re.search(pattern, all_refs)]
    return {
        "source": source,
        "reference_count": len(entries),
        "year_counts": year_counts,
        "venue_counts": venue_counts,
        "missing_core_refs": missing,
    }


def render_csv_text(fields, rows):
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = render_csv_text(fields, rows)
    data = text.encode("utf-8-sig")
    if path.exists() and path.read_bytes() == data:
        return
    path.write_bytes(data)


def truthy(value):
    return str(value).strip().lower() == "true"


def count_true(rows, field):
    return sum(1 for row in rows if truthy(row.get(field, "")))


def parse_punctuation_text(text):
    values = defaultdict(int)
    for part in (text or "").split(";"):
        if "=" not in part:
            continue
        key, value = part.strip().split("=", 1)
        try:
            values[key.strip()] = int(value.strip())
        except ValueError:
            values[key.strip()] = 0
    return values


def sentence_needs_clause_audit(row):
    sentence = row.get("sentence_text", "")
    punc = parse_punctuation_text(row.get("punctuation_pattern", ""))
    return (
        ";" in sentence
        or ":" in sentence
        or re.search(r"\b(which|that|while|whereas|although)\b", sentence, re.I)
        or len(sentence.split()) > 35
        or punc.get("comma_count", sentence.count(",")) > 3
        or row.get("claim_strength") in {"medium", "high", "very_high"}
    )


def split_clauses(sentence):
    parts = re.split(r"(?i)(;|:|\balthough\b|\bwhereas\b|\bwhile\b|\bwhich\b|\bthat\b)", sentence)
    clauses = []
    current = ""
    for part in parts:
        if not part:
            continue
        if re.fullmatch(r"(?i);|:|\balthough\b|\bwhereas\b|\bwhile\b|\bwhich\b|\bthat\b", part.strip()):
            if current.strip():
                clauses.append(current.strip())
            current = part.strip() + " "
        else:
            current += part
    if current.strip():
        clauses.append(current.strip())
    return [clause.strip(" ,") for clause in clauses if len(clause.strip()) > 8] or [sentence]


def clause_type(clause, index):
    lower = clause.lower()
    if index == 1:
        return "main_clause"
    if lower.startswith(("which", "that")):
        return "relative_clause"
    if lower.startswith(("although", "while", "whereas")):
        return "subordinate_clause"
    if clause.startswith("(") or clause.endswith(")"):
        return "parenthetical_clause"
    if ":" in clause:
        return "colon_clause"
    return "appositive_or_coordinate_clause"


def clause_records(manuscript):
    records = []
    for row in manuscript:
        if not sentence_needs_clause_audit(row):
            continue
        sentence = row.get("sentence_text", "")
        clauses = split_clauses(sentence)
        multi_claim = len(clauses) > 1 and row.get("claim_strength") in {"medium", "high", "very_high"}
        for index, clause in enumerate(clauses, 1):
            ctype = clause_type(clause, index)
            claim_type, claim_strength = classify_claim(clause)
            anchor = anchors(clause)
            risk = sorted(set(words_present(clause, STRONG_WORDS | AI_WORDS | VAGUE_WORDS)))
            issues = []
            actions = []
            if multi_claim:
                issues.append("multi_claim_sentence")
                actions.append("SPLIT_SENTENCE")
            if claim_strength in {"medium", "high", "very_high"} and anchor["evidence_anchor"] == "None":
                issues.append("implication_without_evidence")
                actions.append("ADD_EVIDENCE_ANCHOR")
            if ctype == "relative_clause" and claim_strength in {"high", "very_high"}:
                issues.append("relative_clause_overclaim")
                actions.append("WEAKEN_CLAIM")
            if re.search(r"\((?:under|within|only|except|condition)", clause, re.I) or re.search(r"\b(under|within|condition)\b", clause, re.I):
                issues.append("hidden_boundary")
                actions.append("ADD_BOUNDARY")
            if ":" in sentence and index > 1:
                issues.append("colon_sentence_split_check")
                actions.append("SPLIT_SENTENCE")
            if risk:
                issues.append("risk_word")
                actions.append("REPLACE_RISK_VERB")
            records.append(
                {
                    "sentence_id": row.get("sentence_id", ""),
                    "clause_index": index,
                    "clause_text": clause,
                    "clause_type": ctype,
                    "function": dominant_function(clause, row.get("section_id", "")),
                    "claim_type": claim_type,
                    "claim_strength": claim_strength,
                    "evidence_support": anchor["evidence_anchor"],
                    "risk_words": ";".join(risk),
                    "issue": ";".join(dict.fromkeys(issues)) or "none",
                    "recommended_action": ";".join(dict.fromkeys(actions)) or "KEEP",
                }
            )
    return records


def caption_function_sequence(caption):
    sentences = split_sentences(caption) or [clean_text(caption)]
    labels = []
    for sentence in sentences:
        lower = sentence.lower()
        labels.append("OBJECT")
        if re.search(r"\b(under|using|across|for each|condition|setup|configuration)\b", lower):
            labels.append("CONDITION")
        if re.search(r"\b(show|shows|compare|comparison|result|entropy|increase|decrease|higher|lower)\b", lower):
            labels.append("TAKEAWAY")
        if re.search(r"\b(note|unit|bold|missing|abbreviation)\b", lower):
            labels.append("NOTE")
    return " -> ".join(collapse_sequence(labels))


def figure_table_role(kind, caption):
    lower = caption.lower()
    if re.search(r"\b(workflow|pipeline|procedure|flow)\b", lower):
        return "workflow"
    if re.search(r"\b(architecture|block diagram|implementation)\b", lower):
        return "architecture"
    if re.search(r"\b(setup|platform|configuration)\b", lower):
        return "setup"
    if re.search(r"\b(result|entropy|comparison|throughput|area|power|latency)\b", lower):
        return "result" if kind == "figure" else "comparison"
    if re.search(r"\b(audit|check|diagnosis)\b", lower):
        return "audit"
    return "concept"


def extract_float_environments(tex_text):
    floats = []
    for kind in ["figure", "table"]:
        pattern = rf"\\begin\{{{kind}\}}(.*?)\\end\{{{kind}\}}"
        for match in re.finditer(pattern, tex_text, flags=re.S | re.I):
            body = match.group(1)
            caption_match = re.search(r"\\caption(?:\[[^\]]*\])?\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", body, flags=re.S)
            label_match = re.search(r"\\label\{([^{}]+)\}", body)
            caption = clean_text(caption_match.group(1)) if caption_match else ""
            label = label_match.group(1) if label_match else f"{kind}:{len(floats)+1}"
            floats.append({"id": label, "kind": kind, "caption": caption, "position": match.start()})
    return sorted(floats, key=lambda row: row["position"])


def figure_table_inventory(tex_text, manuscript):
    floats = extract_float_environments(tex_text)
    inventory = []
    for float_index, item in enumerate(floats, 1):
        label = item["id"]
        first_mention = ""
        first_mention_index = None
        body_sentence = ""
        for index, row in enumerate(manuscript, 1):
            haystack = f"{row.get('figure_table_anchor', '')} {row.get('sentence_text', '')}"
            if label in haystack or label.split(":")[-1] in haystack:
                first_mention = row.get("sentence_id", "")
                first_mention_index = index
                body_sentence = row.get("sentence_text", "")
                break
        caption = item["caption"]
        role = figure_table_role(item["kind"], caption)
        explains = bool(re.search(r"\b(show|shows|indicate|look|observe|compare|summarize)\b", body_sentence, re.I))
        quantifies = bool(re.search(r"\d", body_sentence))
        caption_terms = set(re.findall(r"[A-Za-z][A-Za-z\-]{4,}", caption.lower()))
        body_terms = set(re.findall(r"[A-Za-z][A-Za-z\-]{4,}", body_sentence.lower()))
        consistency = "consistent" if not caption_terms or caption_terms & body_terms else "check_caption_body_takeaway"
        unit_issue = "check_units_or_abbreviations" if re.search(r"\b(ns|MHz|Mbps|LUT|FF|bit|%)\b", caption) and not re.search(r"\b(unit|units|defined|denote)\b", caption, re.I) else "none"
        table_note_needed = "yes" if item["kind"] == "table" and re.search(r"\b(bold|dash|n/a|missing|best)\b", caption, re.I) else "no"
        inventory.append(
            {
                "id": label,
                "kind": item["kind"],
                "caption": caption,
                "caption_sentence_count": len(split_sentences(caption) or ([caption] if caption else [])),
                "caption_function_sequence": caption_function_sequence(caption),
                "first_mention_sentence_id": first_mention or "MISSING",
                "distance_from_first_mention": "" if first_mention_index is None else float_index - first_mention_index,
                "role": role,
                "body_claim_linked": "yes" if first_mention else "no",
                "body_explains_what_to_look_for": "yes" if explains else "no",
                "body_quantifies_after_reference": "yes" if quantifies else "no",
                "caption_body_consistency": consistency,
                "table_note_needed": table_note_needed,
                "unit_or_abbreviation_issue": unit_issue,
                "caption_storyline_note": f"{item['kind']} {label}: {role}; {caption_function_sequence(caption)}",
            }
        )
    return inventory


def gold_label_template_records(manuscript, figure_table_rows, target_count=100):
    selected = []

    def add_from(predicate, limit):
        for row in manuscript:
            if len([item for item in selected if predicate(item)]) >= limit:
                break
            if predicate(row) and row not in selected:
                selected.append(row)

    add_from(lambda row: row.get("section_id") in {"Abstract", "Introduction"}, 30)
    add_from(lambda row: any(token in row.get("section_id", "").lower() for token in ["result", "discussion", "characterization", "diagnosis", "counterfactual"]), 40)
    for fig in figure_table_rows[:20]:
        selected.append(
            {
                "sentence_id": f"CAPTION:{fig.get('id', '')}",
                "section_id": "Caption",
                "sentence_text": fig.get("caption", ""),
                "dominant_function": fig.get("caption_function_sequence", ""),
                "claim_type": "caption",
                "revision_operation": "CHECK_CAPTION_BODY_LINK",
            }
        )
    for row in manuscript:
        if len(selected) >= target_count:
            break
        if row not in selected:
            selected.append(row)
    records = []
    source = selected or manuscript or [{"sentence_id": "CAL.EMPTY", "sentence_text": "", "dominant_function": "", "claim_type": "", "revision_operation": ""}]
    while len(source) < target_count:
        source = source + source
    for index, row in enumerate(source[:target_count], 1):
        records.append(
            {
                "sentence_id": row.get("sentence_id", "") or f"CAL.S{index}",
                "sentence_text": row.get("sentence_text", ""),
                "model_function": row.get("dominant_function", ""),
                "gold_function": "",
                "model_claim_type": row.get("claim_type", ""),
                "gold_claim_type": "",
                "model_action": row.get("revision_operation", ""),
                "gold_action": "",
                "notes": "",
            }
        )
    return records

def function_count_text(counts, limit=8):
    if not counts:
        return "暂无记录"
    return "，".join(f"`{k}`（{zh_function(k)}）{v} 条" for k, v in counts.most_common(limit))


def section_rows(corpus, section):
    return [row for row in corpus if row.get("section_type") == section]


def venue_display_name(venue):
    if venue == "IEEE Transactions on Circuits and Systems II: Express Briefs":
        return "TCAS-II"
    return venue


def sort_key_index(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def collapse_sequence(sequence):
    collapsed = []
    for function in sequence:
        if function and (not collapsed or collapsed[-1] != function):
            collapsed.append(function)
    return collapsed


def format_sequence(sequence):
    return " -> ".join(sequence)


def format_function_counts(counts):
    if not counts:
        return ""
    items = sorted(counts.items(), key=lambda item: (-int(item[1]), item[0]))
    return "; ".join(f"{key}={value}" for key, value in items)


def parse_function_counts(text):
    counts = Counter()
    if not text:
        return counts
    for part in text.split(";"):
        if "=" not in part:
            continue
        key, value = part.strip().split("=", 1)
        try:
            counts[key.strip()] += float(value.strip())
        except ValueError:
            continue
    return counts


def format_avg_function_counts(rows):
    if not rows:
        return ""
    totals = Counter()
    for row in rows:
        totals.update(parse_function_counts(row.get("function_counts", "")))
    averaged = {key: round(value / len(rows), 1) for key, value in totals.items()}
    if not averaged:
        return ""
    items = sorted(averaged.items(), key=lambda item: (-item[1], item[0]))
    return "; ".join(f"{key}={value:.1f}" for key, value in items)


def classify_section_archetype(section_type, sequence, evidence_quality="full_sequence"):
    sequence = [function for function in sequence if function]
    functions = set(sequence)
    sentence_count = len(sequence)
    result_ratio = sequence.count("RESULT") / max(sentence_count, 1)

    archetype_id = "OTHER"
    archetype_name = "其他"

    if section_type == "Abstract":
        if ({"BG", "PROBLEM", "GAP"} & functions) and ({"METHOD", "SETUP"} & functions) and "RESULT" in functions and ({"INTERPRET", "BOUNDARY"} & functions):
            archetype_id, archetype_name = "ABS_A", "完整摘要链"
        elif ({"PROBLEM", "GAP"} & functions) and ({"METHOD", "SETUP"} & functions) and "RESULT" in functions:
            archetype_id, archetype_name = "ABS_B", "问题-方法-结果型"
        elif ({"METHOD", "SETUP"} & functions) and "RESULT" in functions and not ({"PROBLEM", "GAP"} & functions):
            archetype_id, archetype_name = "ABS_C", "方法-验证-结果型"
        elif sequence.count("RESULT") >= 4 or result_ratio >= 0.5:
            archetype_id, archetype_name = "ABS_D", "结果密集型"
        else:
            archetype_id, archetype_name = "ABS_E", "压缩/非典型型"
    elif section_type == "Introduction":
        if sentence_count <= 2 or evidence_quality == "partial/notes-derived":
            archetype_id, archetype_name = "INT_X", "部分证据型"
        elif ({"BG", "PROBLEM", "GAP", "NEED"} & functions) and ({"METHOD", "RESULT", "CONTRIB"} & functions):
            archetype_id, archetype_name = "INT_A", "背景-问题-缺口-任务-贡献型"
        elif "BG" in functions and "INTERPRET" in functions and not ({"GAP", "NEED"} & functions):
            archetype_id, archetype_name = "INT_B", "背景解释型"
        elif {"PROBLEM", "GAP"} & functions:
            archetype_id, archetype_name = "INT_C", "问题缺口驱动型"
        elif {"RESULT", "CONTRIB"} & functions:
            archetype_id, archetype_name = "INT_D", "结果预告型"
        else:
            archetype_id, archetype_name = "INT_E", "非典型引言型"
    elif section_type == "Results":
        if sentence_count <= 2 or evidence_quality == "partial/notes-derived":
            archetype_id, archetype_name = "RES_X", "部分证据型"
        elif "SETUP" in functions and sequence.count("RESULT") >= 5:
            archetype_id, archetype_name = "RES_A", "设置-多结果-解释型"
        elif "ORG" in functions and "SETUP" in functions:
            archetype_id, archetype_name = "RES_B", "结构化实验段型"
        elif sequence.count("RESULT") >= 7:
            archetype_id, archetype_name = "RES_C", "结果密集型"
        else:
            archetype_id, archetype_name = "RES_D", "短结果链型"
    elif section_type == "Contribution":
        if sentence_count <= 1:
            archetype_id, archetype_name = "CON_A", "单条贡献块"
        else:
            archetype_id, archetype_name = "CON_B", "多条贡献块"

    return {"archetype_id": archetype_id, "archetype_name": archetype_name, "evidence_quality": evidence_quality}


def infer_evidence_quality(section_type, rows):
    if section_type in {"Introduction", "Results"}:
        if len(rows) <= 2:
            return "partial/notes-derived"
        sources = " ".join(row.get("evidence_source", "") for row in rows).lower()
        if "notes" in sources:
            return "partial/notes-derived"
        if rows and all(row.get("confidence") == "low" for row in rows):
            return "partial/notes-derived"
    return "full_sequence"


def build_paper_sequence_archetypes(corpus):
    grouped = defaultdict(list)
    for row in corpus:
        key = (row.get("paper_id", ""), row.get("venue", ""), row.get("section_type", ""))
        grouped[key].append(row)

    records = []
    for (paper_id, venue, section_type), rows in sorted(grouped.items()):
        rows = sorted(rows, key=lambda row: sort_key_index(row.get("sentence_index")))
        sequence = [row.get("sentence_function", "") for row in rows if row.get("sentence_function")]
        counts = Counter(sequence)
        evidence_quality = infer_evidence_quality(section_type, rows)
        archetype = classify_section_archetype(section_type, sequence, evidence_quality)
        records.append(
            {
                "paper_id": paper_id,
                "title": rows[0].get("title", ""),
                "venue": venue_display_name(venue),
                "year": rows[0].get("year", ""),
                "section_type": section_type,
                "sentence_count": len(sequence),
                "exact_sequence": format_sequence(sequence),
                "collapsed_sequence": format_sequence(collapse_sequence(sequence)),
                "archetype_id": archetype["archetype_id"],
                "archetype_name": archetype["archetype_name"],
                "function_counts": format_function_counts(counts),
                "evidence_quality": archetype["evidence_quality"],
            }
        )
    return records


def preference_note(total_papers, paper_count, archetype_id, evidence_quality):
    if archetype_id.endswith("_X") or evidence_quality == "partial/notes-derived":
        return "insufficient_evidence：部分证据型，不用于推断 venue 偏好"
    if total_papers and paper_count >= 6:
        return "strong_preference：强倾向"
    if total_papers and 3 <= paper_count <= 5:
        return "mixed_preference：混合分布"
    return "minor_pattern：少数样本"


def build_venue_archetype_matrix(paper_archetypes):
    grouped = defaultdict(list)
    section_venue_totals = Counter((row["section_type"], row["venue"]) for row in paper_archetypes)
    for row in paper_archetypes:
        key = (row["section_type"], row["venue"], row["archetype_id"], row["archetype_name"])
        grouped[key].append(row)

    records = []
    for (section_type, venue, archetype_id, archetype_name), rows in sorted(grouped.items()):
        total = section_venue_totals[(section_type, venue)]
        count = len(rows)
        evidence_values = Counter(row.get("evidence_quality", "") for row in rows)
        evidence_quality = evidence_values.most_common(1)[0][0] if evidence_values else ""
        records.append(
            {
                "section_type": section_type,
                "venue": venue,
                "archetype_id": archetype_id,
                "archetype_name": archetype_name,
                "paper_count": count,
                "total_papers": total,
                "share": f"{count / total:.2f}" if total else "0.00",
                "avg_sentence_count": f"{sum(float(row.get('sentence_count', 0) or 0) for row in rows) / count:.1f}",
                "avg_function_counts": format_avg_function_counts(rows),
                "representative_papers": "; ".join(row["paper_id"] for row in rows[:3]),
                "evidence_quality": evidence_quality,
                "note": preference_note(total, count, archetype_id, evidence_quality),
            }
        )
    return records


def archetype_summary_rows(paper_archetypes, section_type):
    grouped = defaultdict(list)
    for row in paper_archetypes:
        if row["section_type"] == section_type:
            grouped[(row["archetype_id"], row["archetype_name"])].append(row)
    rows = []
    total = sum(len(items) for items in grouped.values())
    for (archetype_id, archetype_name), items in sorted(grouped.items()):
        rows.append(
            {
                "archetype_id": archetype_id,
                "archetype_name": archetype_name,
                "paper_count": len(items),
                "share": f"{len(items) / total:.0%}" if total else "0%",
                "avg_sentence_count": f"{sum(float(row['sentence_count']) for row in items) / len(items):.1f}",
                "avg_function_counts": format_avg_function_counts(items),
                "representative_papers": "; ".join(row["paper_id"] for row in items[:3]),
            }
        )
    return rows


def markdown_table(headers, rows):
    if not rows:
        return ["暂无记录。"]
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(header, "")) for header in headers) + " |")
    return lines


def build_topvenue_profile_text(corpus, manuscript):
    paper_archetypes = build_paper_sequence_archetypes(corpus)
    venue_matrix = build_venue_archetype_matrix(paper_archetypes)
    by_section = defaultdict(list)
    for row in corpus:
        by_section[row.get("section_type", "")].append(row.get("sentence_function", ""))
    unique_papers = {row.get("paper_id") for row in corpus if row.get("paper_id")}
    venue_counts = Counter(row.get("venue", "未知 venue") for row in corpus)

    lines = ["# 顶刊句子功能序列画像", ""]
    lines.extend(
        [
            "这个文件把本地 01-06 顶刊语料里的句子功能做成可模仿的序列画像。字段名保持英文是为了脚本稳定，正文说明全部用中文。",
            "",
            "## 这份文档怎么读",
            "",
            "- 它不是论文内容综述，而是写法结构说明：每一句在 Abstract、Introduction、Results、Contribution 里承担什么功能。",
            "- `154 条` 这类数字表示句子/功能单元数量，不是论文数量，也不是实验数量。例如看到 `RESULT 154 条`，意思是语料中有 154 个摘要句子或功能单元被标成结果句。",
            "- 高频功能说明顶刊在该章节最常做什么；它是写作重心提示，不是要求你机械照抄比例。",
            "- 标签名保留英文，便于和 CSV 对照；括号里的中文告诉你它在论文中的实际作用。",
            "",
            "## 数字怎么理解",
            "",
            f"- 当前顶刊语料逐句记录：{len(corpus)} 条。",
            f"- 当前稿件逐句记录：{len(manuscript)} 条。",
            f"- 覆盖论文数量：{len(unique_papers) if unique_papers else '未在样例中提供 paper_id'} 篇。",
            "- `sentence_function`：这句话的主功能，例如背景、问题、缺口、方法、设置、结果、解释、边界。",
            "- `claim_type`：这句话在提出哪类 claim，例如描述、方法、测量、因果、比较、泛化或限制。",
            "- `claim_strength`：claim 的力度。`low/medium` 多用于描述和受限结论；`high/very_high` 需要数字、图表、实验或引用支撑。",
            "- `has_number`：是否含数字。数字多不等于写得好；顶刊通常把数字放在 RESULT 或 SETUP 句里，用来支撑比较和边界。",
            "- `punctuation_pattern`：标点形态，例如逗号过多、分号、破折号。它帮助判断句子是否塞了太多功能。",
            "- `transition_pattern`：句子功能链，例如 `METHOD/SETUP` 或 `RESULT/INTERPRET`，用于判断一句话是在铺方法、给结果，还是从结果转解释。",
            "",
            "## 顶刊怎么写",
            "",
            "顶刊的共同特征不是句子华丽，而是每句话有明确任务：先让读者知道问题为什么重要，再说明已有方法哪里不够，然后交代本文做什么、怎么验证、结果说明什么、边界在哪里。",
            "",
            "- 好的 Abstract 像压缩版论文：背景很短，问题和缺口清楚，方法不展开细节，结果必须有信息量，最后给解释或边界。",
            "- 好的 Introduction 像论证链：背景不是堆知识，而是不断收窄到本文问题；每段都要把读者推向“为什么必须做本文”。",
            "- 好的 Results 段不是堆数字：先说要回答的问题，再给实验设置或图表，再观察现象、量化差异、解释原因，最后说明适用边界。",
            "- 好的 Contribution block 很短但很硬：每条贡献都要能映射到一个概念、方法、实证结果或 artifact/audit 产物。",
            "",
            "## RO-TRNG 仿写",
            "",
            "- 写 Abstract 时，不要一开始讲太多 FPGA/TRNG 常识；先用 1 句背景接住读者，再用 1-2 句指出 sampler-side、placement、restart 或 entropy boundary 的问题。",
            "- 写 Introduction 时，每段只推进一个功能：背景段负责建立任务，问题段负责暴露不确定性，缺口段负责指出现有评价缺什么，方法段负责说明本文如何隔离变量。",
            "- 写 Results 时，每段开头先给问题句，例如“这一组实验检查 X 是否来自 Y”；结果句必须绑定数字、表格或图；解释句要把数字变成机制判断。",
            "- 写边界时要主动：说明结果在哪些 FPGA、seed、placement、restart 条件下成立，避免把受控实验写成普遍定律。",
            "",
            "## 是否统一组织",
            "",
            "先说结论：顶刊不是完全统一按一种逐句顺序组织。逐句精确序列往往每篇都不同，但压缩到高层功能后，会出现少数可复用的组织范式。",
            "",
            "- `exact_sequence` 是每篇论文真实的逐句功能顺序。",
            "- `collapsed_sequence` 会把连续重复功能压缩，方便看高层组织方式。",
            "- `archetype` 是把相近顺序归成一种组织范式，用来回答“有几篇属于这种组织方式”。",
            "- `venue 偏好` 是每个 venue 的 10 篇样本内分布：6/10 以上称为强倾向，3-5/10 称为混合分布，`*_X 部分证据型` 不用于推断偏爱。",
            "",
        ]
    )

    section_guides = {
        "Abstract": {
            "target": "`BG -> PROBLEM -> GAP -> METHOD/SETUP -> RESULT -> INTERPRET/BOUNDARY`",
            "why": "摘要的任务是让读者在很短时间内看懂：领域背景是什么、本文抓住哪个未解决问题、用什么方法隔离或验证、结果给出什么证据、结论边界在哪里。",
            "moves": [
                "`BG`：给读者最小背景，不讲教材。RO-TRNG 可写成“FPGA TRNG 的熵质量受实现细节影响”。",
                "`PROBLEM`：把背景压成具体麻烦。RO-TRNG 可写 sampler、placement、restart 或评价协议会改变可观测熵。",
                "`GAP`：指出现有工作没隔离什么变量，不能只说“研究不足”。",
                "`METHOD/SETUP`：说明本文如何构造对照、平台、指标和审计流程。",
                "`RESULT`：给可验证发现，优先绑定数字、表格或明确比较对象。",
                "`INTERPRET/BOUNDARY`：说明结果意味着什么，以及在哪些条件下成立。",
            ],
            "imitate": "摘要不要把每个技术细节都塞进去；目标是 5-8 句内完成“背景、问题、缺口、方法、设置、结果、边界”。",
        },
        "Introduction": {
            "target": "`BG -> PROBLEM -> GAP -> NEED -> TASK/METHOD -> RESULT/CONTRIB -> ORG`",
            "why": "引言不是加长版摘要。顶刊引言会反复解释为什么这个问题值得做，所以 `INTERPRET` 往往很多：它们负责把背景事实翻译成研究动机、评价缺口和本文设计选择。",
            "moves": [
                "`BG`：建立读者共同知识，但只保留会导向本文问题的背景。",
                "`PROBLEM`：从系统、电路、工具链或安全评价中抽出具体矛盾。",
                "`GAP`：说明已有论文、标准测试或工具流程没有解决哪个判断问题。",
                "`NEED`：把 gap 变成必要性，告诉读者为什么现在必须做这件事。",
                "`TASK/METHOD`：提前给出本文任务和变量隔离思路。",
                "`RESULT/CONTRIB`：用短句预告核心发现和贡献，不展开所有数据。",
                "`ORG`：最后一两句安排论文结构。",
            ],
            "imitate": "RO-TRNG 引言建议用 5-7 段：应用背景、实现敏感性、现有测试/论文限制、本文问题定义、实验设计、贡献、文章结构。",
        },
        "Results": {
            "target": "`QUESTION -> SETUP/FIGURE/TABLE -> OBSERVATION -> QUANTIFICATION -> INTERPRETATION -> BOUNDARY -> TRANSITION`",
            "why": "结果段的核心不是“我们测了很多”，而是“每组实验回答一个问题”。`RESULT` 数量高说明顶刊把观察和量化判断写得很密；`SETUP` 数量也高，说明读者必须先知道比较条件。",
            "moves": [
                "`QUESTION`：段首明确本段回答什么问题。",
                "`SETUP/FIGURE/TABLE`：交代平台、变量、指标、图表或表格。",
                "`OBSERVATION`：描述图表里最明显的趋势。",
                "`QUANTIFICATION`：给数字、差值、比例或排序。",
                "`INTERPRETATION`：解释为什么会这样，连接到机制。",
                "`BOUNDARY`：说明哪些条件下不能外推。",
                "`TRANSITION`：把本段发现导向下一组实验。",
            ],
            "imitate": "RO-TRNG 结果段每段最好只回答一个变量问题，例如 sampler-side、placement、restart、routing 或 seed，不要把多个 claim 混进一句长句。",
        },
        "Contribution": {
            "target": "`CONCEPTUAL CONTRIBUTION -> METHOD CONTRIBUTION -> EMPIRICAL CONTRIBUTION -> ARTIFACT/AUDIT CONTRIBUTION`",
            "why": "贡献块数量少，是因为它通常集中在引言末尾或摘要末尾；但每条贡献必须可核验，不能只是换个说法重复“本文提出一种方法”。",
            "moves": [
                "概念贡献：重新定义问题、威胁模型、评价边界或解释框架。",
                "方法贡献：提出可复现实验设计、变量隔离方法、审计流程或工具链。",
                "实证贡献：报告跨平台、跨配置、跨指标的发现。",
                "artifact/audit 贡献：给出数据、脚本、流程、检查清单或复现实验资产。",
            ],
            "imitate": "RO-TRNG 贡献建议写成 3-4 条，每条以“我们定义/构造/测量/发布或审计”开头，并能在正文找到对应章节和证据。",
        },
    }

    for section in ["Abstract", "Introduction", "Results", "Contribution"]:
        rows = section_rows(corpus, section)
        counts = Counter(row.get("sentence_function", "") for row in rows)
        number_count = count_true(rows, "has_number")
        fig_count = count_true(rows, "has_figure_reference")
        table_count = count_true(rows, "has_table_reference")
        guide = section_guides[section]
        lines.extend(
            [
                f"## {section}",
                "",
                f"- 高频主功能：{function_count_text(counts)}。",
                f"- 数字句：{number_count} 条；图引用句：{fig_count} 条；表引用句：{table_count} 条。",
                f"- 目标功能链：{guide['target']}。",
                f"- 这一节为什么这样写：{guide['why']}",
                "",
                "### 功能拆解",
                "",
            ]
        )
        for move in guide["moves"]:
            lines.append(f"- {move}")
        lines.extend(["", f"### RO-TRNG 仿写规则", "", f"- {guide['imitate']}", ""])
        summary_rows = [
            {
                "范式": f"{row['archetype_id']} {row['archetype_name']}",
                "论文数": row["paper_count"],
                "占比": row["share"],
                "平均句数": row["avg_sentence_count"],
                "平均功能句数": row["avg_function_counts"],
                "代表论文": row["representative_papers"],
            }
            for row in archetype_summary_rows(paper_archetypes, section)
        ]
        lines.extend(
            [
                "### 组织范式总表",
                "",
                "这张表回答：全体 60 篇里，有几篇属于这种组织方式；每种功能平均多少句。",
                "",
            ]
        )
        lines.extend(markdown_table(["范式", "论文数", "占比", "平均句数", "平均功能句数", "代表论文"], summary_rows))
        section_venue_rows = [
            {
                "venue": row["venue"],
                "范式": f"{row['archetype_id']} {row['archetype_name']}",
                "论文数": f"{row['paper_count']}/{row['total_papers']}",
                "占比": row["share"],
                "平均功能句数": row["avg_function_counts"],
                "判断": row["note"],
            }
            for row in venue_matrix
            if row["section_type"] == section
        ]
        lines.extend(
            [
                "",
                "### venue 偏好表",
                "",
                "这张表回答：某个顶刊类别是不是偏爱某种组织范式。这里的“偏爱”只是当前 10 篇样本内的写法倾向，不是该 venue 的官方规则。",
                "",
            ]
        )
        lines.extend(markdown_table(["venue", "范式", "论文数", "占比", "平均功能句数", "判断"], section_venue_rows))
        if section in {"Introduction", "Results"}:
            lines.extend(
                [
                    "",
                    "注意：`部分证据型` 多半表示该篇在当前语料中只有局部 Introduction/Results 功能单元，不能把它解读成该 venue 真喜欢短结构。",
                ]
            )
        lines.append("")

    lines.extend(
        [
            "## 分 venue 读法",
            "",
            "这些差异是写法倾向，不是硬规则。写 RO-TRNG 时应该按目标 venue 的读者期待调整重心。",
            "",
            f"- TCAS-I/TCAS-II：强调电路、方法、验证的紧凑链条。本地记录中相关句子约 {venue_counts.get('TCAS-I', 0) + venue_counts.get('IEEE Transactions on Circuits and Systems II: Express Briefs', 0)} 条；可模仿其“模型/电路 -> 验证 -> 应用或解释”的压缩写法。",
            f"- TVLSI/TCAD：强调设计约束、工具/流程、实验设置。本地记录中 TVLSI {venue_counts.get('TVLSI', 0)} 条、TCAD {venue_counts.get('TCAD', 0)} 条；RO-TRNG 若强调 FPGA 实现和可复现实验，应多学这类写法。",
            f"- TC：强调系统问题、比较基线、实证结果。本地记录中 TC {venue_counts.get('TC', 0)} 条；适合学习如何把实验发现写成系统层结论。",
            f"- TCHES/CHES：强调威胁模型、攻击/防御边界、可复现实验。本地记录中 TCHES/CHES {venue_counts.get('TCHES/CHES', 0)} 条；适合学习安全评价中如何主动写边界和复现条件。",
            "",
            "## 全章节功能模板",
            "",
            "- Related Work：`类别 -> 代表性工作 -> 共同能力 -> 共同限制 -> 本文差异`。",
            "- Background：`定义 -> 机制 -> 相关性 -> 限制`。",
            "- Method：`目标 -> 原理 -> 结构 -> 固定变量 -> 改变变量 -> 输出`。",
            "- Experimental Setup：`目的 -> 平台 -> 工具链 -> 控制项 -> 变量 -> 指标 -> 重复次数 -> 处理方法`。",
            "- Discussion：`发现综合 -> 替代解释 -> 限制 -> 含义`。",
            "- Conclusion：`问题回顾 -> 方法回顾 -> 发现 -> 含义 -> 边界/未来工作`。",
            "",
            "## 使用提醒",
            "",
            "- 先看功能链，再看数字：数字告诉你顶刊常写什么，功能链告诉你应该按什么顺序写。",
            "- 不要把高频功能当配方比例：例如 Introduction 的 `INTERPRET` 很多，不代表要写很多空泛解释，而是每段都要解释“这个事实如何导向本文问题”。",
            "- 仿写时优先检查每段第一句和最后一句：第一句要立问题，最后一句要给解释、边界或转场。",
        ]
    )
    return "\n".join(lines) + "\n"


def write_profiles(corpus, manuscript):
    out = MODULE_DIR / "corpus" / "topvenue_function_sequence_profiles.md"
    text = build_topvenue_profile_text(corpus, manuscript)
    out.write_text(text, encoding="utf-8")


def report_alignment(manuscript):
    out = MODULE_DIR / "reports" / "deep_morphology_alignment_report.md"
    issues = [row for row in manuscript if row["mismatch_type"] != "none" or row["previous_sentence_relation"] == "jumps"]
    lines = [
        "# 深度形态学对齐报告",
        "",
        "这个报告按句子级审计当前稿件。它只指出位置、功能、风险和修订动作，不直接改写原稿。",
        "",
        "## 总览",
        "",
        f"- 逐句记录：{len(manuscript)} 条。",
        f"- 存在 mismatch 或上下句跳跃的句子：{len(issues)} 条。",
        "",
        "## 优先检查的句子记录",
        "",
    ]
    for row in issues[:40]:
        lines.extend(
            [
                f"### {row['sentence_id']}",
                "",
                f"原句：{row['sentence_text']}",
                "",
                f"- 主功能：`{row['dominant_function']}`（{zh_function(row['dominant_function'])}）",
                f"- 顶刊期望角色：`{row['expected_topvenue_role']}`",
                f"- 和上一句关系：`{row['previous_sentence_relation']}`（{zh_relation(row['previous_sentence_relation'])}）",
                f"- claim 类型/强度：`{row['claim_type']}`（{zh_claim(row['claim_type'])}） / `{row['claim_strength']}`（{zh_strength(row['claim_strength'])}）",
                f"- 证据锚点：`{row['evidence_anchor']}`（{zh_evidence(row['evidence_anchor'])}）",
                f"- 风险词：`{row['risk_words'] or '无'}`",
                f"- 标点模式：`{row['punctuation_pattern'] or 'OK'}`",
                f"- 问题类型：`{row['mismatch_type']}`",
                f"- 建议动作：`{row['revision_operation']}`（{zh_operations(row['revision_operation'])}）",
                "",
            ]
        )
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")


def report_abstract(manuscript):
    out = MODULE_DIR / "reports" / "abstract_deep_sentence_morphology.md"
    abs_rows = [row for row in manuscript if row["section_id"] == "Abstract"]
    seq = " -> ".join(row["dominant_function"] for row in abs_rows)
    lines = [
        "# 摘要逐句深度形态学报告",
        "",
        "顶刊目标序列：`BG -> PROBLEM -> GAP -> METHOD -> SETUP -> RESULT -> BOUNDARY`。",
        "",
        f"当前摘要序列：`{seq}`。",
        "",
    ]
    for row in abs_rows:
        lines.extend(
            [
                f"## {row['sentence_id']}",
                "",
                f"原句：{row['sentence_text']}",
                "",
                f"- 当前功能：`{row['dominant_function']}`（{zh_function(row['dominant_function'])}）",
                f"- 该位置期望功能：`{row['expected_topvenue_role']}`",
                f"- claim：`{row['claim_type']}`（{zh_claim(row['claim_type'])}） / `{row['claim_strength']}`（{zh_strength(row['claim_strength'])}）",
                f"- 证据锚点：`{row['evidence_anchor']}`（{zh_evidence(row['evidence_anchor'])}）",
                f"- 风险词：`{row['risk_words'] or '无'}`",
                f"- 建议动作：`{row['revision_operation']}`（{zh_operations(row['revision_operation'])}）",
                "",
            ]
        )
    lines.extend(["## 改写前的功能计划", "", "`BG -> PROBLEM -> GAP -> METHOD -> SETUP -> RESULT -> BOUNDARY`。", ""])
    out.write_text("\n".join(lines), encoding="utf-8")


def report_results(manuscript):
    out = MODULE_DIR / "reports" / "results_deep_paragraph_morphology.md"
    result_rows = [row for row in manuscript if any(token in row["section_id"].lower() for token in ["characterization", "counterfactual", "diagnosis", "result"])]
    by_para = defaultdict(list)
    for row in result_rows:
        by_para[row["paragraph_id"]].append(row)
    lines = [
        "# Results 段落深度形态学报告",
        "",
        "顶刊成熟实验段落的目标序列：`QUESTION -> FIGURE/TABLE -> OBSERVATION -> QUANTIFICATION -> INTERPRETATION -> BOUNDARY`。",
        "",
    ]
    for para, rows in list(by_para.items())[:40]:
        seq = " -> ".join(row["dominant_function"] for row in rows)
        role = "主结果"
        if any("counterfactual" in row["section_id"].lower() for row in rows):
            role = "反事实实验"
        elif any("diagnosis" in row["section_id"].lower() for row in rows):
            role = "机制诊断"
        lines.extend([f"## {para}", "", f"- 段落角色：`{role}`", f"- 当前句子功能序列：`{seq}`", ""])
        for row in rows:
            lines.append(
                f"- `{row['sentence_id']}` {row['dominant_function']}（{zh_function(row['dominant_function'])}）"
                f" | 证据 `{zh_evidence(row['evidence_anchor'])}`"
                f" | 动作 `{zh_operations(row['revision_operation'])}`"
            )
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")


def report_corpus_quality():
    out = MODULE_DIR / "reports" / "corpus_extraction_quality_report.md"
    stats = CORPUS_QUALITY or {}
    lines = [
        "# 顶刊语料抽取质量报告",
        "",
        "这个报告用于判断顶刊 corpus 是否干净。它统计抽取后删除了哪些非论文正文噪声，并给出人工抽查样例。",
        "",
        "## 总览",
        "",
        f"- 原始抽取句子/功能单元：{stats.get('raw_total', 0)} 条。",
        f"- 删除噪声：{stats.get('removed_total', 0)} 条。",
        f"- 保留进入 corpus：{stats.get('retained_total', 0)} 条。",
        "",
        "## 删除原因统计",
        "",
    ]
    removed_by_reason = stats.get("removed_by_reason", {})
    if removed_by_reason:
        for reason, count in sorted(removed_by_reason.items(), key=lambda item: (-item[1], item[0])):
            lines.append(f"- `{reason}`：{count} 条。")
    else:
        lines.append("- 未删除任何记录。")
    lines.extend(["", "## 保留记录按 section 统计", ""])
    retained_by_section = stats.get("retained_by_section", {})
    if retained_by_section:
        for section, count in sorted(retained_by_section.items()):
            lines.append(f"- `{section}`：{count} 条。")
    else:
        lines.append("- 暂无保留记录。")
    lines.extend(["", "## 删除样例（最多 20 条）", ""])
    for row in stats.get("removed_examples", [])[:20]:
        lines.append(f"- `{row.get('remove_reason') or row.get('reason')}` / `{row.get('section_type', '')}`：{row.get('text', '')[:180]}")
    lines.extend(["", "## 保留样例（最多 20 条）", ""])
    for row in stats.get("retained_examples", [])[:20]:
        lines.append(f"- `{row.get('section_type', '')}`：{row.get('text', '')[:180]}")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def report_clause_claim_risk(clauses):
    out = MODULE_DIR / "reports" / "clause_claim_risk_report.md"
    risky = [row for row in clauses if row.get("recommended_action") != "KEEP"]
    issue_counts = Counter()
    for row in risky:
        for issue in row.get("issue", "").split(";"):
            if issue and issue != "none":
                issue_counts[issue] += 1
    lines = [
        "# 从句级 claim 风险报告",
        "",
        "这个报告只检查需要从句级审计的句子：长句、冒号/分号句、relative clause、条件从句、多逗号句或中高强度 claim。",
        "",
        "## 总览",
        "",
        f"- 从句记录：{len(clauses)} 条。",
        f"- 需要动作的从句：{len(risky)} 条。",
        "",
        "## issue 统计",
        "",
    ]
    if issue_counts:
        for issue, count in issue_counts.most_common():
            lines.append(f"- `{issue}`：{count} 条。")
    else:
        lines.append("- 暂无从句级 issue。")
    lines.extend(["", "## 优先检查样例", ""])
    for row in risky[:60]:
        lines.extend(
            [
                f"### {row['sentence_id']} C{row['clause_index']}",
                "",
                f"从句：{row['clause_text']}",
                "",
                f"- 从句类型：`{row['clause_type']}`",
                f"- 功能：`{row['function']}`（{zh_function(row['function'])}）",
                f"- claim：`{row['claim_type']}` / `{row['claim_strength']}`",
                f"- 证据：`{row['evidence_support']}`（{zh_evidence(row['evidence_support'])}）",
                f"- issue：`{row['issue']}`",
                f"- 建议动作：`{row['recommended_action']}`（{zh_operations(row['recommended_action'])}）",
                "",
            ]
        )
    out.write_text("\n".join(lines), encoding="utf-8")


def report_figure_table_elements(inventory):
    out = MODULE_DIR / "reports" / "figure_table_element_morphology_report.md"
    lines = [
        "# 图表元素级形态报告",
        "",
        "这个报告检查图表是否承担清楚的论文叙事功能：caption 是否有对象/条件/结论/备注，正文是否先引用再解释，caption 和正文 claim 是否一致。",
        "",
        "## 总览",
        "",
        f"- 图表记录：{len(inventory)} 个。",
        f"- 缺少正文 first mention：{sum(1 for row in inventory if row['first_mention_sentence_id'] == 'MISSING')} 个。",
        f"- caption/body 需要核对：{sum(1 for row in inventory if row['caption_body_consistency'] != 'consistent')} 个。",
        "",
        "## 图表逐项审计",
        "",
    ]
    for row in inventory:
        lines.extend(
            [
                f"### {row['kind']} `{row['id']}`",
                "",
                f"caption：{row['caption']}",
                "",
                f"- caption 功能序列：`{row['caption_function_sequence']}`",
                f"- 角色：`{row['role']}`",
                f"- first mention：`{row['first_mention_sentence_id']}`",
                f"- 正文是否解释看什么：`{row['body_explains_what_to_look_for']}`",
                f"- 正文是否给定量：`{row['body_quantifies_after_reference']}`",
                f"- caption/body 一致性：`{row['caption_body_consistency']}`",
                f"- 表格 note 需求：`{row['table_note_needed']}`",
                f"- 单位/缩写问题：`{row['unit_or_abbreviation_issue']}`",
                "",
            ]
        )
    lines.extend(["## caption-only storyline", ""])
    if inventory:
        for row in inventory:
            lines.append(f"- `{row['id']}`：{row['caption_storyline_note']}")
    else:
        lines.append("- 未抽取到 figure/table 环境。")
    out.write_text("\n".join(lines), encoding="utf-8")


def annotation_accuracy_rows(gold_rows):
    filled = [row for row in gold_rows if row.get("gold_function") or row.get("gold_claim_type") or row.get("gold_action")]
    if not filled:
        return {
            "filled": 0,
            "function_accuracy": "待标注",
            "claim_type_accuracy": "待标注",
            "false_keep_cases": 0,
            "confusions": Counter(),
        }
    function_total = sum(1 for row in filled if row.get("gold_function"))
    function_match = sum(1 for row in filled if row.get("gold_function") and row.get("gold_function") == row.get("model_function"))
    claim_total = sum(1 for row in filled if row.get("gold_claim_type"))
    claim_match = sum(1 for row in filled if row.get("gold_claim_type") and row.get("gold_claim_type") == row.get("model_claim_type"))
    false_keep = sum(1 for row in filled if row.get("model_action") == "KEEP" and row.get("gold_action") and row.get("gold_action") != "KEEP")
    confusions = Counter(
        f"{row.get('model_function')} -> {row.get('gold_function')}"
        for row in filled
        if row.get("gold_function") and row.get("gold_function") != row.get("model_function")
    )
    return {
        "filled": len(filled),
        "function_accuracy": f"{function_match / function_total:.2f}" if function_total else "待标注",
        "claim_type_accuracy": f"{claim_match / claim_total:.2f}" if claim_total else "待标注",
        "false_keep_cases": false_keep,
        "confusions": confusions,
    }


def report_annotation_accuracy(gold_rows):
    out = MODULE_DIR / "reports" / "annotation_accuracy_report.md"
    stats = annotation_accuracy_rows(gold_rows)
    lines = [
        "# 人工校准准确率报告",
        "",
        "这个报告等待人工填写 `calibration/gold_sentence_labels_template.csv` 中的 gold 字段后再产生真实准确率。当前先提供模板覆盖和待标注状态。",
        "",
        "## 总览",
        "",
        f"- 模板句子数：{len(gold_rows)} 条。",
        f"- 已填写 gold 的句子数：{stats['filled']} 条。",
        f"- function accuracy：{stats['function_accuracy']}",
        f"- claim_type accuracy：{stats['claim_type_accuracy']}",
        f"- false KEEP cases：{stats['false_keep_cases']}",
        "",
        "## 系统性混淆模式",
        "",
    ]
    if stats["confusions"]:
        for confusion, count in stats["confusions"].most_common():
            lines.append(f"- `{confusion}`：{count} 条。")
    else:
        lines.append("- gold labels 尚未填写，暂无混淆统计。")
    lines.extend(
        [
            "",
            "## 使用方法",
            "",
            "- 请人工填写 `gold_function`、`gold_claim_type`、`gold_action`。",
            "- 重点观察 `SETUP vs RESULT`、`BG vs INTERPRETATION`、false KEEP、overclaim 漏检。",
            "- 填完后重新运行 pipeline，即可更新准确率报告。",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def operation_explanation(row_or_operation):
    if isinstance(row_or_operation, dict):
        operation = row_or_operation.get("revision_operation") or row_or_operation.get("recommended_action") or "KEEP"
        sentence_id = row_or_operation.get("sentence_id", "")
        function = row_or_operation.get("dominant_function") or row_or_operation.get("function", "")
        expected = row_or_operation.get("expected_topvenue_role", "")
        evidence = row_or_operation.get("evidence_anchor") or row_or_operation.get("evidence_support", "")
        strength = row_or_operation.get("claim_strength", "")
    else:
        operation = row_or_operation
        sentence_id = ""
        function = ""
        expected = ""
        evidence = ""
        strength = ""
    parts = []
    for op in [part for part in operation.split(";") if part]:
        zh = OPERATION_ZH.get(op, op)
        if op == "ADD_BOUNDARY":
            reason = "需要补充适用条件、实验边界或不可外推范围。"
        elif op == "ADD_EVIDENCE_ANCHOR":
            reason = f"该位置存在 `{strength}` 强度 claim，但证据锚点为 `{evidence or 'None'}`。"
        elif op == "ADD_BRIDGE":
            reason = "上下句关系跳跃，需要桥接前后论证。"
        elif op == "REFUNCTION_SENTENCE":
            reason = f"当前功能 `{function}` 与顶刊期望 `{expected}` 不一致。"
        elif op == "REORDER_SENTENCE":
            reason = "句子顺序不符合目标功能链，需要前移、后移或并入相邻句。"
        elif op == "SPLIT_SENTENCE":
            reason = "一句话承载多个 claim 或从句过载，建议拆分。"
        elif op == "WEAKEN_CLAIM":
            reason = "claim 语气过强，需要改成受证据约束的表达。"
        elif op == "REPLACE_RISK_VERB":
            reason = "存在高风险动词、泛词或 AI 味表达，需要替换成可证实表述。"
        elif op == "CHANGE_PUNCTUATION":
            reason = "标点形态影响技术论文语气或句子清晰度。"
        elif op == "REWRITE_CAPTION":
            reason = "caption 未清楚承担对象、条件、结论或备注功能。"
        elif op == "ADD_TABLE_NOTE":
            reason = "表格中的单位、缩写、bold rule、缺失值或精度规则需要 note。"
        else:
            reason = "该操作用于让句子/段落回到顶刊常见功能链。"
        prefix = f"{sentence_id}: " if sentence_id else ""
        parts.append(f"{prefix}{op}（{zh}）：{reason}")
    return "；".join(parts) if parts else "KEEP（保留）：当前记录没有触发强制 revision operation。"


def issue_rows(manuscript, clauses, figures, citations):
    rows = []
    for row in manuscript:
        if row.get("revision_operation") and row["revision_operation"] != "KEEP":
            severity = "must_fix" if any(op in row["revision_operation"] for op in ["ADD_EVIDENCE_ANCHOR", "ADD_BRIDGE", "REFUNCTION_SENTENCE", "WEAKEN_CLAIM"]) else "should_fix"
            rows.append(
                {
                    "id": row["sentence_id"],
                    "level": "sentence",
                    "section": row.get("section_id", ""),
                    "severity": severity,
                    "issue": row.get("mismatch_type", ""),
                    "operation": row.get("revision_operation", ""),
                    "explanation": operation_explanation(row),
                }
            )
    for row in clauses:
        if row.get("recommended_action") and row["recommended_action"] != "KEEP":
            rows.append(
                {
                    "id": f"{row['sentence_id']}.C{row['clause_index']}",
                    "level": "clause",
                    "section": "",
                    "severity": "must_fix" if "ADD_EVIDENCE_ANCHOR" in row["recommended_action"] else "should_fix",
                    "issue": row.get("issue", ""),
                    "operation": row.get("recommended_action", ""),
                    "explanation": operation_explanation(row),
                }
            )
    for row in figures:
        ops = []
        if row.get("first_mention_sentence_id") == "MISSING":
            ops.append("ADD_BRIDGE")
        if row.get("body_explains_what_to_look_for") == "no" or row.get("caption_body_consistency") != "consistent":
            ops.append("REWRITE_CAPTION")
        if row.get("table_note_needed") == "yes" or row.get("unit_or_abbreviation_issue") != "none":
            ops.append("ADD_TABLE_NOTE")
        if ops:
            operation = ";".join(dict.fromkeys(ops))
            rows.append(
                {
                    "id": row["id"],
                    "level": row.get("kind", "figure_table"),
                    "section": "figure/table",
                    "severity": "should_fix",
                    "issue": "figure_table_storyline_issue",
                    "operation": operation,
                    "explanation": operation_explanation(operation),
                }
            )
    for index, row in enumerate(citations, 1):
        if row.get("issue") and row["issue"] != "none":
            rows.append(
                {
                    "id": f"CIT.{index}:{row.get('sentence_id', '')}",
                    "level": "citation",
                    "section": row.get("section_id", ""),
                    "severity": "should_fix",
                    "issue": row.get("issue", ""),
                    "operation": "ADD_CITATION",
                    "explanation": "ADD_CITATION（补引用）：该 citation 的功能与句子 claim 类型不完全匹配，需要补充或调整引用支撑。",
                }
            )
    return rows


def packet_matrix_csv(manuscript, clauses):
    fields = [
        "sentence_id",
        "section_id",
        "paragraph_id",
        "clause_id",
        "unit_type",
        "unit_text",
        "dominant_function",
        "secondary_function",
        "expected_function",
        "previous_sentence_relation",
        "next_sentence_relation",
        "claim_type",
        "claim_strength",
        "evidence_anchor",
        "citation_anchor",
        "figure_table_anchor",
        "risk_words",
        "punctuation_pattern",
        "issue",
        "revision_operation",
        "chinese_explanation",
    ]
    rows = []
    for row in manuscript:
        rows.append(
            {
                "sentence_id": row.get("sentence_id", ""),
                "section_id": row.get("section_id", ""),
                "paragraph_id": row.get("paragraph_id", ""),
                "clause_id": "",
                "unit_type": "sentence",
                "unit_text": row.get("sentence_text", ""),
                "dominant_function": row.get("dominant_function", ""),
                "secondary_function": row.get("secondary_function", ""),
                "expected_function": row.get("expected_topvenue_role", ""),
                "previous_sentence_relation": row.get("previous_sentence_relation", ""),
                "next_sentence_relation": row.get("next_sentence_relation", ""),
                "claim_type": row.get("claim_type", ""),
                "claim_strength": row.get("claim_strength", ""),
                "evidence_anchor": row.get("evidence_anchor", ""),
                "citation_anchor": row.get("citation_anchor", ""),
                "figure_table_anchor": row.get("figure_table_anchor", ""),
                "risk_words": row.get("risk_words", ""),
                "punctuation_pattern": row.get("punctuation_pattern", ""),
                "issue": row.get("mismatch_type", ""),
                "revision_operation": row.get("revision_operation", ""),
                "chinese_explanation": operation_explanation(row),
            }
        )
    sentence_lookup = {row.get("sentence_id"): row for row in manuscript}
    for row in clauses:
        parent = sentence_lookup.get(row.get("sentence_id"), {})
        rows.append(
            {
                "sentence_id": row.get("sentence_id", ""),
                "section_id": parent.get("section_id", ""),
                "paragraph_id": parent.get("paragraph_id", ""),
                "clause_id": f"{row.get('sentence_id')}.C{row.get('clause_index')}",
                "unit_type": "clause",
                "unit_text": row.get("clause_text", ""),
                "dominant_function": row.get("function", ""),
                "secondary_function": "",
                "expected_function": parent.get("expected_topvenue_role", ""),
                "previous_sentence_relation": parent.get("previous_sentence_relation", ""),
                "next_sentence_relation": "",
                "claim_type": row.get("claim_type", ""),
                "claim_strength": row.get("claim_strength", ""),
                "evidence_anchor": row.get("evidence_support", ""),
                "citation_anchor": parent.get("citation_anchor", ""),
                "figure_table_anchor": parent.get("figure_table_anchor", ""),
                "risk_words": row.get("risk_words", ""),
                "punctuation_pattern": parent.get("punctuation_pattern", ""),
                "issue": row.get("issue", ""),
                "revision_operation": row.get("recommended_action", ""),
                "chinese_explanation": operation_explanation(row),
            }
        )
    return render_csv_text(fields, rows)


def section_counts(manuscript):
    counts = Counter(row.get("section_id", "") for row in manuscript)
    total = sum(counts.values()) or 1
    return [(section, count, count / total) for section, count in counts.most_common()]


def build_packet_gold_labels(manuscript, clauses, figures):
    rows = gold_label_template_records(manuscript, figures, target_count=100)
    used = len(rows)
    for clause in clauses:
        if used >= 100:
            break
        rows.append(
            {
                "sentence_id": f"{clause.get('sentence_id')}.C{clause.get('clause_index')}",
                "sentence_text": clause.get("clause_text", ""),
                "model_function": clause.get("function", ""),
                "gold_function": "",
                "model_claim_type": clause.get("claim_type", ""),
                "gold_claim_type": "",
                "model_action": clause.get("recommended_action", ""),
                "gold_action": "",
                "notes": "",
            }
        )
        used += 1
    return rows[:100]


def build_submission_packet_files(corpus, manuscript, clauses, figures, citations, gold_rows, corpus_quality, reference_meta=None):
    issues = issue_rows(manuscript, clauses, figures, citations)
    must = [row for row in issues if row["severity"] == "must_fix"]
    should = [row for row in issues if row["severity"] == "should_fix"]
    optional = [row for row in issues if row["severity"] not in {"must_fix", "should_fix"}]
    section_summary = section_counts(manuscript)
    function_counts = Counter(row.get("dominant_function", "") for row in manuscript)
    punctuation_issues = [row for row in manuscript if row.get("punctuation_pattern") and row.get("revision_operation") != "KEEP"]
    packet_gold = gold_rows if len(gold_rows) >= 100 else build_packet_gold_labels(manuscript, clauses, figures)
    corpus_quality = corpus_quality or CORPUS_QUALITY or {}
    reference_meta = reference_meta or {
        "source": "未提供参考文献源",
        "reference_count": 0,
        "year_counts": Counter(),
        "venue_counts": Counter(),
        "missing_core_refs": ["NIST/SP800", "FPGA TRNG", "RO-TRNG", "entropy estimation", "sampler implementation"],
    }

    dashboard_lines = [
        "# 投稿形态学对齐总览",
        "",
        "这个总览汇总当前 manuscript 在全文（paper）、章节（section）、段落（paragraph）、句子（sentence）、从句（clause）、图（figure）、表（table）、引用（citation）和标点（punctuation）层面的顶刊形态偏离。报告只生成 revision packet，不直接重写 manuscript。",
        "",
        "## 总体状态",
        "",
        f"- 顶刊清洗后 corpus：{len(corpus)} 条功能单元。",
        f"- manuscript 逐句记录：{len(manuscript)} 条。",
        f"- 从句记录：{len(clauses)} 条。",
        f"- 图表记录：{len(figures)} 个。",
        f"- citation 记录：{len(citations)} 条。",
        f"- 必须修改：{len(must)} 项；建议修改：{len(should)} 项；可选修改：{len(optional)} 项。",
        "",
        "## 必须修改",
        "",
    ]
    for row in must[:20]:
        dashboard_lines.append(f"- `{row['id']}`：`{row['operation']}`（{zh_operations(row['operation'])}）。{row['explanation']}")
    if not must:
        dashboard_lines.append("- 当前没有 must fix 项。")
    dashboard_lines.extend(["", "## 建议修改", ""])
    for row in should[:20]:
        dashboard_lines.append(f"- `{row['id']}`：`{row['operation']}`（{zh_operations(row['operation'])}）。{row['explanation']}")
    if not should:
        dashboard_lines.append("- 当前没有 should fix 项。")
    dashboard_lines.extend(["", "## 可选修改", ""])
    dashboard_lines.append("- 低风险术语统一、图表微调和局部标点微调可在 must/should 完成后处理。")

    corpus_lines = [
        "# 顶刊 corpus 风格指纹",
        "",
        "本报告来自清洗后的顶刊 corpus，不使用未清洗噪声作为风格依据。",
        "",
        "## 清洗质量",
        "",
        f"- 原始功能单元：{corpus_quality.get('raw_total', len(corpus))} 条。",
        f"- 删除噪声：{corpus_quality.get('removed_total', 0)} 条。",
        f"- 保留功能单元：{corpus_quality.get('retained_total', len(corpus))} 条。",
        "",
        "## 顶刊高频功能",
        "",
    ]
    for function, count in Counter(row.get("sentence_function", "") for row in corpus).most_common(12):
        corpus_lines.append(f"- `{function}`（{zh_function(function)}）：{count} 条。")

    whole_lines = [
        "# 全文形态报告",
        "",
        "本报告检查全文层级形态（paper-level morphology）：章节顺序（section order）、章节长度比例（section length ratios）、图表密度（figure/table density）、贡献数量（contribution count）、视觉节奏（visual rhythm）和参考文献分布（reference distribution）。",
        "",
        "## 章节顺序与长度比例",
        "",
    ]
    for section, count, ratio in section_summary:
        whole_lines.append(f"- `{section}`：{count} 句，占 {ratio:.1%}。")
    whole_lines.extend(
        [
            "",
            "## 图表密度与视觉节奏",
            "",
            f"- 图表数量：{len(figures)} 个；约每 {max(len(manuscript) / max(len(figures), 1), 1):.1f} 句出现一个图表对象。",
            f"- 图：{sum(1 for row in figures if row.get('kind') == 'figure')} 个；表：{sum(1 for row in figures if row.get('kind') == 'table')} 个。",
            "",
            "## 参考文献分布",
            "",
            f"- citation anchor 记录：{len(citations)} 条。",
            f"- 可解析参考文献源：{reference_meta.get('source', '未定位')}。",
            f"- 可解析参考文献条目：{reference_meta.get('reference_count', 0)} 条。",
            "- 年份分布：" + ("；".join(f"{year}={count}" for year, count in reference_meta.get("year_counts", Counter()).most_common()) or "未解析到年份。"),
            "- venue/来源分布：" + ("；".join(f"{venue}={count}" for venue, count in reference_meta.get("venue_counts", Counter()).most_common()) or "未解析到 venue/来源。"),
        ]
    )

    section_lines = ["# Section 功能对齐报告", "", "本报告按 section 汇总 dominant function，并判断是否接近顶刊目标功能链。", ""]
    by_section = defaultdict(list)
    for row in manuscript:
        by_section[row.get("section_id", "")].append(row)
    for section, rows in by_section.items():
        seq = " -> ".join(row.get("dominant_function", "") for row in rows[:20])
        mismatches = sum(1 for row in rows if row.get("revision_operation") != "KEEP")
        section_lines.extend(
            [
                f"## {section}",
                "",
                f"- 句子数：{len(rows)}。",
                f"- 前 20 句功能序列：`{seq}`。",
                f"- 需要 revision operation 的句子：{mismatches}。",
                "",
            ]
        )

    abstract_intro = [row for row in manuscript if row.get("section_id") in {"Abstract", "Introduction"}]
    abstract_intro_lines = ["# Abstract / Introduction 深度报告", "", "这一部分检查摘要和引言是否按顶刊功能链展开。", ""]
    for row in abstract_intro:
        if row.get("revision_operation") != "KEEP":
            abstract_intro_lines.append(f"- `{row['sentence_id']}` `{row['dominant_function']}`（{zh_function(row['dominant_function'])}）→ `{row['revision_operation']}`（{zh_operations(row['revision_operation'])}）：{operation_explanation(row)}")

    result_discussion = [row for row in manuscript if any(token in row.get("section_id", "").lower() for token in ["result", "discussion", "characterization", "diagnosis", "counterfactual"])]
    result_lines = ["# Results / Discussion 深度报告", "", "这一部分检查结果段是否具备 QUESTION / FIGURE-TABLE / OBSERVATION / QUANTIFICATION / INTERPRETATION / BOUNDARY 链条。", ""]
    for row in result_discussion:
        if row.get("revision_operation") != "KEEP":
            result_lines.append(f"- `{row['sentence_id']}`：`{row['revision_operation']}`（{zh_operations(row['revision_operation'])}）。{operation_explanation(row)}")

    fig_lines = ["# 图表叙事报告", "", "本报告检查图表的角色、题注功能序列、首次正文提及、正文解释、定量支撑、题注与正文一致性和表格 note 状态。", ""]
    for row in figures:
        fig_lines.extend(
            [
                f"## {row.get('kind')} `{row.get('id')}`",
                "",
                f"- 角色：`{row.get('role')}`。",
                f"- 题注功能序列：`{row.get('caption_function_sequence')}`。",
                f"- 首次正文提及：`{row.get('first_mention_sentence_id')}`。",
                f"- 正文解释：`{row.get('body_explains_what_to_look_for')}`；定量支撑：`{row.get('body_quantifies_after_reference')}`。",
                f"- 题注与正文一致性：`{row.get('caption_body_consistency')}`。",
                f"- 表格 note：`{row.get('table_note_needed')}`；单位/缩写/加粗规则：`{row.get('unit_or_abbreviation_issue')}`。",
                "",
            ]
        )

    citation_lines = [
        "# 引用与参考文献支撑报告",
        "",
        "本报告检查 citation（文中引用）在句子里的功能：background（背景支撑）、prior limitation（前人限制）、gap support（缺口支撑）、method support（方法支撑）、standard（标准依据）、comparison（比较基线）、definition（定义来源）、claim support（主张支撑）。",
        "",
        "## 文中 citation 功能",
        "",
    ]
    for index, row in enumerate(citations, 1):
        citation_lines.append(f"- `CIT.{index}` `{row.get('sentence_id')}`：`{row.get('citation_anchor')}` → {row.get('citation_function')}；issue=`{row.get('issue')}`。")
    citation_lines.extend(
        [
            "",
            "## 参考文献年份与来源分布",
            "",
            f"- 解析来源：{reference_meta.get('source', '未定位')}。",
            f"- 参考文献条目数：{reference_meta.get('reference_count', 0)}。",
            "- 年份分布：" + ("；".join(f"{year}={count}" for year, count in reference_meta.get("year_counts", Counter()).most_common()) or "未解析到年份。"),
            "- venue/来源分布：" + ("；".join(f"{venue}={count}" for venue, count in reference_meta.get("venue_counts", Counter()).most_common()) or "未解析到 venue/来源。"),
            "",
            "## 缺失核心引用提醒",
            "",
        ]
    )
    missing_refs = reference_meta.get("missing_core_refs", [])
    if missing_refs:
        for item in missing_refs:
            citation_lines.append(f"- 需要人工确认是否补充：{item}。")
    else:
        citation_lines.append("- 自动检查未发现核心引用类别明显缺口；仍需人工结合目标 venue 和 gold labels 复核。")

    micro_lines = ["# 微观风格检查报告", "", "本报告审计 hyphen（连字符）/ en dash（范围连接号）/ em dash（破折号）、问号、分号、冒号、图表引用格式、数字单位、缩写、术语一致性和 AI-like（模板化）表达。", ""]
    micro_lines.append(f"- 触发标点或风险词 revision 的句子：{len(punctuation_issues)} 条。")
    for row in punctuation_issues[:80]:
        micro_lines.append(f"- `{row['sentence_id']}` 标点 `{row.get('punctuation_pattern')}`，风险词 `{row.get('risk_words') or '无'}`，操作 `{row.get('revision_operation')}`（{zh_operations(row.get('revision_operation'))}）。")

    priority_lines = ["# Revision 优先级计划", "", "先处理 must fix，再处理 should fix，最后处理 optional。不要在完成 packet 审计前直接重写 manuscript。", "", "## Must fix", ""]
    for row in must:
        priority_lines.append(f"- `{row['id']}`：`{row['operation']}`（{zh_operations(row['operation'])}）。{row['explanation']}")
    priority_lines.extend(["", "## Should fix", ""])
    for row in should:
        priority_lines.append(f"- `{row['id']}`：`{row['operation']}`（{zh_operations(row['operation'])}）。{row['explanation']}")

    patch_lines = ["# 最小差异补丁计划", "", "这是最小改动计划，不直接改写 manuscript。论文正文和 LaTeX patch 仍应保持英文；这里用中文说明每个 patch 应做什么。", ""]
    for row in (must + should)[:120]:
        patch_lines.append(f"- 定位 `{row['id']}`：执行 `{row['operation']}`（{zh_operations(row['operation'])}）。中文理由：{row['explanation']}")

    annotation_report = "\n".join(
        [
            "# 人工校准报告",
            "",
            "请先填写 `gold_labels.csv` 中的 gold 字段，再重新运行 pipeline。没有 gold labels 时，不宣称分类器可靠。",
            "",
            f"- gold-label 样本数：{len(packet_gold)} 条。",
            "- function accuracy：待标注。",
            "- claim_type accuracy：待标注。",
            "- confusion patterns：待标注后生成。",
            "",
        ]
    )

    files = {
        "00_dashboard.md": "\n".join(dashboard_lines) + "\n",
        "01_corpus_style_fingerprint.md": "\n".join(corpus_lines) + "\n",
        "02_whole_paper_shape_report.md": "\n".join(whole_lines) + "\n",
        "03_section_function_alignment.md": "\n".join(section_lines) + "\n",
        "04_sentence_clause_morphology_matrix.csv": packet_matrix_csv(manuscript, clauses),
        "05_abstract_intro_deep_report.md": "\n".join(abstract_intro_lines) + "\n",
        "06_results_discussion_deep_report.md": "\n".join(result_lines) + "\n",
        "07_figure_table_storyline_report.md": "\n".join(fig_lines) + "\n",
        "08_citation_reference_support_report.md": "\n".join(citation_lines) + "\n",
        "09_micro_style_lint_report.md": "\n".join(micro_lines) + "\n",
        "10_revision_priority_plan.md": "\n".join(priority_lines) + "\n",
        "11_patch_plan_minimal_diff.md": "\n".join(patch_lines) + "\n",
        "calibration/gold_labels.csv": render_csv_text(GOLD_LABEL_FIELDS, packet_gold),
        "calibration/annotation_accuracy_report.md": annotation_report,
    }
    return files


def write_submission_packet(corpus, manuscript, clauses, figures, citations, gold_rows, corpus_quality, reference_meta=None):
    packet_dir = MODULE_DIR / "submission_morphology_packet"
    files = build_submission_packet_files(corpus, manuscript, clauses, figures, citations, gold_rows, corpus_quality, reference_meta)
    for rel_path, content in files.items():
        path = packet_dir / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if rel_path.endswith(".csv"):
            path.write_bytes(content.encode("utf-8-sig"))
        else:
            path.write_text(content, encoding="utf-8")
    return packet_dir


def citation_function(row):
    section = row["section_id"].lower()
    function = row["dominant_function"]
    if row["citation_anchor"] == "None":
        return ""
    if function in {"BG", "PROBLEM"}:
        return "背景支撑"
    if function in {"GAP", "LIMITATION"} or "background" in section:
        return "前人限制"
    if function == "METHOD":
        return "前人方法"
    if function == "SETUP":
        return "标准/测试依据"
    if function == "RESULT":
        return "比较基线"
    if row["claim_strength"] in {"high", "very_high"}:
        return "claim 支撑"
    return "定义来源"


def citation_records(manuscript):
    records = []
    for row in manuscript:
        if row["citation_anchor"] == "None":
            continue
        cfun = citation_function(row)
        issue = "none"
        if row["dominant_function"] == "RESULT" and cfun != "比较基线":
            issue = "result_sentence_citation_check"
        if row["claim_strength"] in {"high", "very_high"} and cfun not in {"claim 支撑", "比较基线"}:
            issue = "high_claim_citation_role_check"
        records.append(
            {
                "sentence_id": row["sentence_id"],
                "section_id": row["section_id"],
                "citation_anchor": row["citation_anchor"],
                "citation_function": cfun,
                "sentence_function": row["dominant_function"],
                "claim_type": row["claim_type"],
                "claim_strength": row["claim_strength"],
                "issue": issue,
            }
        )
    return records


def main():
    corpus = corpus_records()
    manuscript_path = active_manuscript_path()
    manuscript_tex = read_text(manuscript_path)
    manuscript = manuscript_records(manuscript_path)
    ref_meta = reference_distribution(manuscript_path)
    clauses = clause_records(manuscript)
    figure_tables = figure_table_inventory(manuscript_tex, manuscript)
    gold_rows = gold_label_template_records(manuscript, figure_tables)
    paper_archetypes = build_paper_sequence_archetypes(corpus)
    venue_archetypes = build_venue_archetype_matrix(paper_archetypes)
    write_csv(MODULE_DIR / "corpus" / "topvenue_sentence_morphology.csv", CORPUS_FIELDS, corpus)
    write_csv(MODULE_DIR / "corpus" / "topvenue_paper_sequence_archetypes.csv", PAPER_ARCHETYPE_FIELDS, paper_archetypes)
    write_csv(MODULE_DIR / "corpus" / "topvenue_venue_archetype_matrix.csv", VENUE_ARCHETYPE_FIELDS, venue_archetypes)
    write_csv(MODULE_DIR / "manuscript" / "manuscript_sentence_morphology.csv", SENTENCE_FIELDS, manuscript)
    write_csv(MODULE_DIR / "manuscript" / "manuscript_clause_morphology.csv", CLAUSE_FIELDS, clauses)
    write_csv(MODULE_DIR / "manuscript" / "figure_table_inventory.csv", FIGURE_TABLE_FIELDS, figure_tables)
    write_csv(MODULE_DIR / "manuscript" / "citation_function_matrix.csv", CITATION_FIELDS, citation_records(manuscript))
    write_csv(MODULE_DIR / "calibration" / "gold_sentence_labels_template.csv", GOLD_LABEL_FIELDS, gold_rows)
    write_profiles(corpus, manuscript)
    report_corpus_quality()
    report_alignment(manuscript)
    report_abstract(manuscript)
    report_results(manuscript)
    report_clause_claim_risk(clauses)
    report_figure_table_elements(figure_tables)
    report_annotation_accuracy(gold_rows)
    write_submission_packet(corpus, manuscript, clauses, figure_tables, citation_records(manuscript), gold_rows, CORPUS_QUALITY, ref_meta)
    print(f"topvenue_records={len(corpus)}")
    print(f"manuscript_records={len(manuscript)}")


if __name__ == "__main__":
    main()
