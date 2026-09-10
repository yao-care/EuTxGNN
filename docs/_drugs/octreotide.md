---
layout: default
title: Octreotide
parent: 僅模型預測 (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
---

# Octreotide
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

Using the report template to summarize this Octreotide evidence pack — note upfront: `original_moa`, `original_indications`, and EU licensing data are all empty/`[Data Gap]` in this pack, and the top-ranked prediction itself carries a rationale flagging it as likely a statistical artifact rather than a real biological link. I've represented that honestly rather than smoothing it over.

---

# Octreotide: From Unspecified Indication to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

> Octreotide's original approved indication and mechanism of action are not available in this evidence pack (marked as data gaps).
> The TxGNN model predicts a possible link to **Vulvar Inverted Follicular Keratosis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale suggests no known biological connection exists.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no EU licenses or indication data on record |
| Predicted New Indication | Vulvar Inverted Follicular Keratosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for octreotide is not available in this evidence pack. Based on general pharmacological class knowledge, octreotide is a somatostatin analogue, primarily acting on the GH/glucagon/insulin/gastrin endocrine axes and gastrointestinal secretion — none of which have an established connection to keratinocyte proliferation or differentiation pathways involved in vulvar inverted follicular keratosis.

Importantly, the model-generated rationale for this candidate explicitly notes: *"TxGNN's high score may reflect a statistical association at the embedding level rather than a genuine biological link."* This is a direct signal from the prediction pipeline itself that the association should be treated with caution rather than as a mechanistically grounded hypothesis.

Given the absence of both MOA data and supporting studies, this candidate should currently be regarded as a computational hypothesis only, not a pharmacologically justified repurposing lead.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## EU Market Information

No EU marketing authorizations are currently on record for octreotide in this dataset (market status: Not Marketed, 0 licenses).

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: `key_warnings`, `contraindications`, and DDI data are all recorded as data gaps in this pack — TFDA/EMA label warnings have not yet been retrieved.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support (L5, model prediction only), and the model's own mechanistic rationale suggests the high score likely reflects a statistical artifact rather than a real biological link. Combined with missing MOA and safety data, there is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- TFDA/EMA product label (warnings & contraindications) — currently blocking (DG001), required before any S1 safety screening
- Octreotide mechanism of action data from DrugBank API (DG002)
- Independent mechanistic or preclinical evidence linking somatostatin receptor signaling to keratinocyte pathology
- At minimum, case-report or in-vitro evidence before considering this candidate beyond L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

