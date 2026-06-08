# 人工校准准确率报告

这个报告等待人工填写 `calibration/gold_sentence_labels_template.csv` 中的 gold 字段后再产生真实准确率。当前先提供模板覆盖和待标注状态。

## 总览

- 模板句子数：50 条。
- 已填写 gold 的句子数：0 条。
- function accuracy：待标注
- claim_type accuracy：待标注
- false KEEP cases：0

## 系统性混淆模式

- gold labels 尚未填写，暂无混淆统计。

## 使用方法

- 请人工填写 `gold_function`、`gold_claim_type`、`gold_action`。
- 重点观察 `SETUP vs RESULT`、`BG vs INTERPRETATION`、false KEEP、overclaim 漏检。
- 填完后重新运行 pipeline，即可更新准确率报告。
