# BibTeX Quality Checklist

## 必查字段

- `@article`：author、title、journal、year、volume/number、pages、doi。
- `@inproceedings`：author、title、booktitle、year、pages、doi、publisher。
- `@techreport`：author、title、institution、type、number、year、doi。

## IEEE 风格细节

- 期刊名保持统一，不要同一刊物一会儿缩写、一会儿全称，除非模板自动处理。
- 标题中的专有名词要保护大小写：`{FPGA}`、`{TRNG}`、`{PUF}`、`{NIST}`、`{RO}`。
- DOI 字段保留 DOI 本体，不要混入 `https://doi.org/`，除非项目已有统一风格。
- 作者名含重音符号时保持 BibTeX 可编译写法。

## 未引用文献处理

未引用文献只有三种去向：

- 明确补到 related work。
- 留在 notes，不进 `references.bib`。
- 删除，避免 bibliography 膨胀。

## 审稿风险

- 引用不存在或 DOI 错误会直接伤可信度。
- 标准或安全论文引用错用途，会让审稿人质疑 claim 纪律。
- 只列 bibliography 但正文没引用，说明 related work 没消化。
