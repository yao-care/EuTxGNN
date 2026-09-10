---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 471
evidence_level: L5
indication_count: 10
---

# Pioglitazone
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

# Pioglitazone: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

> Pioglitazone is a thiazolidinedione (TZD)-class PPAR-γ agonist historically used as an insulin sensitizer in type 2 diabetes mellitus.
> The TxGNN model predicts it may be effective for **Opsismodysplasia**, a rare INPPL1-related skeletal dysplasia,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself notes no known biological link between the two conditions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (no EU license text or `original_indications` entries available; Pioglitazone is generally classified as a type 2 diabetes mellitus therapy) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as data gap **DG002**, High severity). Based on general drug classification, Pioglitazone belongs to the thiazolidinedione (TZD) class, acting as a PPAR-γ agonist that improves insulin sensitivity and has been used clinically in type 2 diabetes management.

Opsismodysplasia, however, is a rare autosomal recessive skeletal dysplasia caused by mutations in *INPPL1*, affecting phosphoinositide signaling and bone growth — a pathway with no established connection to PPAR-γ agonism. The evidence pack's own mechanistic assessment is explicit on this point: *"與 PPAR-γ 通路無已知關聯，僅為 TxGNN 圖譜相似性預測，缺乏生物學合理性連結"* (no known association with the PPAR-γ pathway; the prediction reflects only TxGNN graph-similarity output and lacks biological plausibility).

Given the absence of a coherent mechanistic rationale and the complete lack of clinical trials or literature (L5), this candidate should be treated as a preliminary algorithmic signal only — not a validated repurposing hypothesis warranting further investment at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

Pioglitazone currently has no EU marketing authorizations on file in this evidence pack (market status: **not marketed**, 0 licenses recorded).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: a Blocking data gap — DG001, missing TFDA/regulatory drug label warnings and contraindications — prevents this candidate from entering Stage S1 safety review.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (opsismodysplasia, TxGNN score 99.59%) has zero supporting clinical trials or literature (L5), and the evidence pack's own mechanistic review found no biological plausibility linking Pioglitazone's PPAR-γ pathway to this rare skeletal disorder. In addition, a Blocking data gap (missing regulatory safety labeling) prevents entry into Stage S1 safety review.

**To proceed, the following is needed:**
- TFDA/regulatory drug label (warnings, contraindications) — resolves Blocking gap **DG001**
- Verified mechanism of action data via DrugBank API — resolves High-priority gap **DG002**
- Independent mechanistic or preclinical evidence directly connecting Pioglitazone to opsismodysplasia before further investment
- If exploring alternative candidates from this evidence pack, rank 9 (**pancreatic agenesis**, L4) has some literature support, though the rationale notes the cited studies are non-specific reviews of TZDs in general type 2 diabetes rather than disease-specific evidence, and the mechanism (insulin sensitization vs. absolute insulin deficiency) is potentially contradictory
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

