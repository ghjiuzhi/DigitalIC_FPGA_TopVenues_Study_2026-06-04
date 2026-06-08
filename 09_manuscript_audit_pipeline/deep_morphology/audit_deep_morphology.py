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
    lines = ["# Top-Venue Function Sequence Profiles", ""]
    for section in ["Abstract", "Introduction", "Results", "Contribution"]:
        seq = by_section.get(section, [])
        counts = Counter(seq)
        lines.append(f"## {section}")
        lines.append("")
        lines.append("Observed dominant functions: " + ", ".join(f"`{k}` {v}" for k, v in counts.most_common(8)))
        if section == "Abstract":
            lines.append("")
            lines.append("Target sequence: `BG -> PROBLEM -> GAP -> TASK/METHOD -> SETUP -> RESULT -> INTERPRET/BOUNDARY`.")
        elif section == "Results":
            lines.append("")
            lines.append("Target paragraph sequence: `QUESTION -> FIGURE/TABLE -> OBSERVATION -> QUANTIFICATION -> INTERPRETATION -> BOUNDARY -> TRANSITION`.")
        lines.append("")
    lines.extend(
        [
            "## Full-Section Templates",
            "",
            "- Related Work: `CATEGORY -> REPRESENTATIVE WORKS -> COMMON CAPABILITY -> COMMON LIMITATION -> OUR DIFFERENCE`.",
            "- Background: `DEFINE -> MECHANISM -> RELEVANCE -> LIMIT`.",
            "- Method: `GOAL -> PRINCIPLE -> STRUCTURE -> FIXED VARIABLES -> CHANGED VARIABLES -> OUTPUT`.",
            "- Experimental Setup: `PURPOSE -> PLATFORM -> TOOLCHAIN -> CONTROL -> VARIABLE -> METRIC -> REPEAT -> PROCESSING`.",
            "- Discussion: `FINDING SYNTHESIS -> ALTERNATIVE EXPLANATION -> LIMITATION -> IMPLICATION`.",
            "- Conclusion: `PROBLEM RECAP -> METHOD RECAP -> FINDING -> IMPLICATION -> BOUNDARY/FUTURE`.",
            "",
            "## Corpus-to-Manuscript Coverage",
            "",
            f"- Top-venue sentence records: {len(corpus)}.",
            f"- Manuscript sentence records: {len(manuscript)}.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def report_alignment(manuscript):
    out = MODULE_DIR / "reports" / "deep_morphology_alignment_report.md"
    issues = [row for row in manuscript if row["mismatch_type"] != "none" or row["previous_sentence_relation"] == "jumps"]
    lines = [
        "# Deep Morphology Alignment Report",
        "",
        "This report audits the current manuscript at sentence level. It does not rewrite the manuscript.",
        "",
        "## Summary",
        "",
        f"- Sentence records: {len(manuscript)}.",
        f"- Sentences with mismatch or jump relation: {len(issues)}.",
        "",
        "## Highest-Priority Sentence Records",
        "",
    ]
    for row in issues[:40]:
        lines.extend(
            [
                f"### {row['sentence_id']}",
                "",
                f"Text: {row['sentence_text']}",
                "",
                f"- Dominant function: `{row['dominant_function']}`",
                f"- Expected top-venue role: `{row['expected_topvenue_role']}`",
                f"- Previous relation: `{row['previous_sentence_relation']}`",
                f"- Claim type/strength: `{row['claim_type']}` / `{row['claim_strength']}`",
                f"- Evidence anchor: `{row['evidence_anchor']}`",
                f"- Risk words: `{row['risk_words'] or 'None'}`",
                f"- Punctuation: `{row['punctuation_pattern'] or 'OK'}`",
                f"- Mismatch: `{row['mismatch_type']}`",
                f"- Revision operation: `{row['revision_operation']}`",
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
        "# Abstract Deep Sentence Morphology",
        "",
        "Target sequence: `BG -> PROBLEM -> GAP -> METHOD -> SETUP -> RESULT -> BOUNDARY`.",
        "",
        f"Current sequence: `{seq}`.",
        "",
    ]
    for row in abs_rows:
        lines.extend(
            [
                f"## {row['sentence_id']}",
                "",
                f"Text: {row['sentence_text']}",
                "",
                f"- Function: `{row['dominant_function']}`",
                f"- Expected role: `{row['expected_topvenue_role']}`",
                f"- Claim: `{row['claim_type']}` / `{row['claim_strength']}`",
                f"- Evidence: `{row['evidence_anchor']}`",
                f"- Risk words: `{row['risk_words'] or 'None'}`",
                f"- Operation: `{row['revision_operation']}`",
                "",
            ]
        )
    lines.extend(["## Revised Function Plan Before Rewriting", "", "`BG -> PROBLEM -> GAP -> METHOD -> SETUP -> RESULT -> BOUNDARY`.", ""])
    out.write_text("\n".join(lines), encoding="utf-8")


def report_results(manuscript):
    out = MODULE_DIR / "reports" / "results_deep_paragraph_morphology.md"
    result_rows = [row for row in manuscript if any(token in row["section_id"].lower() for token in ["characterization", "counterfactual", "diagnosis", "result"])]
    by_para = defaultdict(list)
    for row in result_rows:
        by_para[row["paragraph_id"]].append(row)
    lines = [
        "# Results Deep Paragraph Morphology",
        "",
        "Target paragraph sequence: `QUESTION -> FIGURE/TABLE -> OBSERVATION -> QUANTIFICATION -> INTERPRETATION -> BOUNDARY`.",
        "",
    ]
    for para, rows in list(by_para.items())[:40]:
        seq = " -> ".join(row["dominant_function"] for row in rows)
        role = "main result"
        if any("counterfactual" in row["section_id"].lower() for row in rows):
            role = "counterfactual"
        elif any("diagnosis" in row["section_id"].lower() for row in rows):
            role = "mechanism diagnosis"
        lines.extend([f"## {para}", "", f"- Paragraph role: `{role}`", f"- Current sequence: `{seq}`", ""])
        for row in rows:
            lines.append(f"- `{row['sentence_id']}` {row['dominant_function']} | evidence `{row['evidence_anchor']}` | operation `{row['revision_operation']}`")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")


def citation_function(row):
    section = row["section_id"].lower()
    function = row["dominant_function"]
    if row["citation_anchor"] == "None":
        return ""
    if function in {"BG", "PROBLEM"}:
        return "background support"
    if function in {"GAP", "LIMITATION"} or "background" in section:
        return "prior limitation"
    if function == "METHOD":
        return "prior method"
    if function == "SETUP":
        return "standard/test reference"
    if function == "RESULT":
        return "comparison baseline"
    if row["claim_strength"] in {"high", "very_high"}:
        return "claim support"
    return "definition source"


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
