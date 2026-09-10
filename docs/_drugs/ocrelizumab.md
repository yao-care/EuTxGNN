---
layout: default
title: Ocrelizumab
parent: 僅模型預測 (L5)
nav_order: 427
evidence_level: L5
indication_count: 10
---

# Ocrelizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ocrelizumab: From Autoimmune Disease (Multiple Sclerosis) to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Ocrelizumab is an anti-CD20 monoclonal antibody originally approved for multiple sclerosis and related autoimmune conditions, acting through B-cell depletion.
The TxGNN model predicts a possible link to **HER2 Positive Breast Carcinoma**,
but this prediction is currently supported by **0 clinical trials** and **0 relevant publications** — it is a pure model-derived signal with no mechanistic or empirical backing found to date.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the EU licensing dataset (no EU authorizations on file); known clinical use is multiple sclerosis / autoimmune disease per drug class |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | Not marketed (no EU authorization records in this dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known drug-class information, Ocrelizumab is an anti-CD20 monoclonal antibody that depletes B lymphocytes, and its efficacy has been established for multiple sclerosis and other autoimmune conditions. This mechanism has no established biological connection to HER2-driven breast cancer, which is driven by HER2 receptor overexpression and downstream oncogenic signaling — a pathway unrelated to B-cell biology.

The supplied rationale explicitly flags this gap: none of the top-ranked predicted indications (HER2+ breast carcinoma, PR+/PR− breast cancer, luminal A/B subtype, "normal breast-like" subtype) have a known mechanistic link to CD20-mediated B-cell depletion. Notably, the literature retrieved for the rank-4 prediction ("breast tumor luminal A or B") consists entirely of papers about B-cell immunology, B-cell lymphoma, and hepatitis B vaccines — these appear to be **false-positive keyword matches** on the letter "B" (as in "B-cell" vs. "luminal **B**" breast cancer subtype), not genuine clinical evidence. This is an important caveat: the high TxGNN scores across this candidate set likely reflect knowledge-graph embedding proximity rather than plausible pharmacology.

In summary, there is currently no mechanistic, preclinical, or clinical rationale to support repurposing Ocrelizumab for HER2+ breast carcinoma or the other predicted oncology indications.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked predicted indication (HER2 Positive Breast Carcinoma).

*Note: 19 publications were retrieved under a lower-ranked prediction ("breast tumor luminal A or B"), but review confirms these concern B-cell immunology/hepatitis B vaccines and are unrelated to breast cancer — assessed as keyword-collision artifacts, not supporting evidence.*

---

## EU Market Information

This drug currently has no EU marketing authorization records in this dataset (market status: Not Marketed; 0 authorizations on file).

---

## Safety Considerations

Please refer to the SmPC for safety information. No specific warnings, contraindications, or drug interaction data are available in this evidence pack (key warning and contraindication fields are data gaps; DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (HER2 Positive Breast Carcinoma) lacks any mechanistic plausibility, clinical trial evidence, or genuine literature support. The one literature set retrieved under a related prediction appears to be a keyword-matching artifact rather than real evidence. This is a pure L5 (model-prediction-only) signal and does not meet the threshold to advance to safety or clinical evaluation.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for Ocrelizumab (currently a data gap)
- Regulatory label data (warnings/contraindications) — currently a blocking data gap preventing safety screening
- Independent mechanistic or preclinical evidence connecting CD20+ B-cell depletion to HER2+ or hormone-receptor-driven breast cancer pathways
- Re-collection of literature evidence using disease-specific (not single-letter/keyword) search terms to rule out further false-positive matches before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

