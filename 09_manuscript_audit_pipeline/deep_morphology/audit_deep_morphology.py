import csv
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
                    "venue": row["venue"],
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


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_profiles(corpus, manuscript):
    out = MODULE_DIR / "corpus" / "topvenue_function_sequence_profiles.md"
    by_section = defaultdict(list)
    for row in corpus:
        by_section[row["section_type"]].append(row["sentence_function"])
    lines = ["# 顶刊句子功能序列画像", ""]
    lines.append("这个文件把本地顶刊语料里的句子功能做成可模仿的序列画像。字段名保持英文是为了脚本稳定，正文说明全部用中文。")
    lines.append("")
    for section in ["Abstract", "Introduction", "Results", "Contribution"]:
        seq = by_section.get(section, [])
        counts = Counter(seq)
        lines.append(f"## {section}")
        lines.append("")
        lines.append("高频主功能：" + "，".join(f"`{k}`（{zh_function(k)}）{v} 条" for k, v in counts.most_common(8)))
        if section == "Abstract":
            lines.append("")
            lines.append("目标序列：`BG -> PROBLEM -> GAP -> TASK/METHOD -> SETUP -> RESULT -> INTERPRET/BOUNDARY`。")
        elif section == "Results":
            lines.append("")
            lines.append("目标结果段序列：`QUESTION -> FIGURE/TABLE -> OBSERVATION -> QUANTIFICATION -> INTERPRETATION -> BOUNDARY -> TRANSITION`。")
        lines.append("")
    lines.extend(
        [
            "## 全章节功能模板",
            "",
            "- Related Work：`类别 -> 代表性工作 -> 共同能力 -> 共同限制 -> 本文差异`。",
            "- Background：`定义 -> 机制 -> 相关性 -> 限制`。",
            "- Method：`目标 -> 原理 -> 结构 -> 固定变量 -> 改变变量 -> 输出`。",
            "- Experimental Setup：`目的 -> 平台 -> 工具链 -> 控制项 -> 变量 -> 指标 -> 重复次数 -> 处理方法`。",
            "- Discussion：`发现综合 -> 替代解释 -> 限制 -> 含义`。",
            "- Conclusion：`问题回顾 -> 方法回顾 -> 发现 -> 含义 -> 边界/未来工作`。",
            "",
            "## 语料和当前稿件覆盖",
            "",
            f"- 顶刊逐句记录：{len(corpus)} 条。",
            f"- 当前稿件逐句记录：{len(manuscript)} 条。",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


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
    write_csv(MODULE_DIR / "corpus" / "topvenue_sentence_morphology.csv", CORPUS_FIELDS, corpus)
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
