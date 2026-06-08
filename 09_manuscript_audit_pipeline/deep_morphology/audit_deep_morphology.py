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
    "ADD_EVIDENCE_ANCHOR": "补证据锚点",
    "WEAKEN_CLAIM": "削弱 claim",
    "REPLACE_RISK_VERB": "替换高风险动词/泛词",
    "CHANGE_PUNCTUATION": "调整标点",
    "ADD_BOUNDARY": "补边界条件",
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
    citations.extend(re.findall(r"\[[0-9,\-\s]+\]|\[[A-Za-z0-9_,:;_\-\s]+\]", sentence))
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


def mismatch_and_operation(function, claim_strength, evidence_anchor, risk_words, punctuation):
    issues = []
    operations = []
    if claim_strength in {"high", "very_high"} and evidence_anchor == "None":
        issues.append("unsupported_claim")
        operations.append("ADD_EVIDENCE_ANCHOR")
    if claim_strength == "very_high":
        issues.append("overstrong_claim")
        operations.append("WEAKEN_CLAIM")
    if risk_words:
        issues.append("risk_word")
        operations.append("REPLACE_RISK_VERB")
    if punctuation.get("em_dash_count", 0) or punctuation.get("question_mark_count", 0):
        issues.append("punctuation_issue")
        operations.append("CHANGE_PUNCTUATION")
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
                mismatch, operation = mismatch_and_operation(function, claim_strength, anchor["evidence_anchor"], risk, punc)
                sentence_id = f"{section_slug}.P{p_index}.S{s_index}" if section_title != "Abstract" else f"ABS.S{s_index}"
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
                        "previous_sentence_relation": relation(previous, clean_sentence),
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
                        "expected_topvenue_role": expected_role(section_title, s_index),
                        "mismatch_type": mismatch,
                        "revision_operation": operation,
                    }
                )
                previous = clean_sentence
    return records


def corpus_records():
    records = []
    with TOPVENUE_MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
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
        if row["dominant_function"] == "RESULT" and cfun != "comparison baseline":
            issue = "result_sentence_citation_check"
        if row["claim_strength"] in {"high", "very_high"} and cfun not in {"claim support", "comparison baseline"}:
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
    manuscript = manuscript_records(active_manuscript_path())
    paper_archetypes = build_paper_sequence_archetypes(corpus)
    venue_archetypes = build_venue_archetype_matrix(paper_archetypes)
    write_csv(MODULE_DIR / "corpus" / "topvenue_sentence_morphology.csv", CORPUS_FIELDS, corpus)
    write_csv(MODULE_DIR / "corpus" / "topvenue_paper_sequence_archetypes.csv", PAPER_ARCHETYPE_FIELDS, paper_archetypes)
    write_csv(MODULE_DIR / "corpus" / "topvenue_venue_archetype_matrix.csv", VENUE_ARCHETYPE_FIELDS, venue_archetypes)
    write_csv(MODULE_DIR / "manuscript" / "manuscript_sentence_morphology.csv", SENTENCE_FIELDS, manuscript)
    write_csv(MODULE_DIR / "manuscript" / "citation_function_matrix.csv", CITATION_FIELDS, citation_records(manuscript))
    write_profiles(corpus, manuscript)
    report_alignment(manuscript)
    report_abstract(manuscript)
    report_results(manuscript)
    print(f"topvenue_records={len(corpus)}")
    print(f"manuscript_records={len(manuscript)}")


if __name__ == "__main__":
    main()
