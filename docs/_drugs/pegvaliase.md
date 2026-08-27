---
layout: default
title: Pegvaliase
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
---

# Pegvaliase
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

# Pegvaliase: From Phenylketonuria (PKU) to Diabetic Retinopathy

## One-Sentence Summary

Pegvaliase is a PEGylated phenylalanine ammonia-lyase (PAL) enzyme therapy originally used to lower blood phenylalanine levels in **phenylketonuria (PKU)**. The TxGNN model predicts it may be effective for **Diabetic Retinopathy**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure computational signal with no independent evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Phenylketonuria (PKU) — noted in the mechanistic rationale text; the structured `original_indications` and `original_moa` fields are marked as Data Gap in this evidence pack |
| Predicted New Indication | Diabetic Retinopathy |
| TxGNN Prediction Score | 99.17% |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured evidence pack (flagged as a High-severity data gap, DG002). Based on the mechanistic notes attached to this prediction, pegvaliase acts exclusively as an enzyme that clears systemic phenylalanine — its entire pharmacological role is confined to phenylalanine catabolism, which underlies its approval for PKU.

Diabetic retinopathy, by contrast, is driven by a completely different pathway: chronic hyperglycemia activates the polyol pathway, upregulates VEGF, thickens the microvascular basement membrane, and increases oxidative stress. There is no known point of mechanistic overlap between phenylalanine metabolism and these hyperglycemia-driven processes.

The evidence pack's own rationale is explicit on this point: the high TxGNN score (0.9917) is most likely an artifact of semantic proximity within the knowledge graph — both PKU and diabetic retinopathy/diabetic cataract sit in a broadly-labeled "metabolic disease" neighborhood — rather than a genuine pharmacological signal. This same pattern repeats across ranks 2–10 in this evidence pack (severe NPDR, diabetic cataract, nuclear/cortical/mature/immature cataract, etc.), which further suggests the model is picking up a metabolic-disease cluster effect rather than a specific, drug-relevant mechanism. Notably, one historical observation cited in the rationale — that untreated PKU has rarely been associated with cataract as a *disease consequence* — cannot be reversed to imply that treating phenylalanine levels would confer a *therapeutic* benefit in non-PKU cataract or retinopathy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No marketing authorizations are on record for pegvaliase in this dataset (`total_licenses = 0`, market status: 未上市 / Not marketed). No authorization number, product name, or approved indication text is available to tabulate.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: all structured safety fields — key warnings, contraindications, and drug-drug interactions — are marked as Data Gap in this evidence pack. This is flagged as a **Blocking** gap in `meta.data_gaps` (DG001): TFDA label warnings/contraindications have not yet been retrieved, and per the evaluation workflow this candidate cannot proceed to the S1 safety pre-screen until that gap is closed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every predicted indication in this evidence pack (ranks 1–10) sits at Evidence Level L5 — a model score with zero supporting clinical trials or literature — and the accompanying mechanistic analysis argues against, rather than for, biological plausibility. Combined with a Blocking data gap on TFDA label warnings/contraindications, this candidate does not currently meet the bar to advance past initial screening.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for pegvaliase from DrugBank or the SmPC (currently Data Gap, DG002)
- TFDA/EMA label warnings and contraindications to complete the S1 safety pre-screen (currently Blocking gap, DG001)
- Independent preclinical or mechanistic evidence linking phenylalanine metabolism (or PAL enzyme activity) to hyperglycemia-driven retinal/lens pathology, before any further investment in this candidate
- If pursued, re-screening against a broader disease set to determine whether the "metabolic disease cluster" pattern seen across ranks 1–10 reflects a genuine signal or a knowledge-graph artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

