---
layout: default
title: Mifamurtide
parent: 僅模型預測 (L5)
nav_order: 394
evidence_level: L5
indication_count: 10
---

# Mifamurtide
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

# Mifamurtide: From Osteosarcoma (Unconfirmed) to Filariasis

## One-Sentence Summary

> Mifamurtide is a liposomal formulation of muramyl tripeptide phosphatidylethanolamine (MTP-PE), though its original indication is not confirmed in this evidence pack.
> The TxGNN model predicts it may be effective for **Filariasis**,
> but currently **no clinical trials** and **no supporting literature** exist for this specific pairing — the prediction rests solely on an indirect, low-confidence mechanistic inference.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no license data or original indication text in this evidence pack) |
| Predicted New Indication | Filariasis |
| TxGNN Prediction Score | 93.06% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on the repurposing rationale provided, Mifamurtide is a liposomal MTP-PE (muramyl tripeptide phosphatidylethanolamine) that activates NOD2 signaling in monocytes/macrophages, inducing pro-inflammatory cytokines (TNF-α, IL-1, IL-6). This is a general macrophage-activating immunostimulant mechanism rather than a disease-specific one.

The proposed link to filariasis is that enhanced macrophage activation might theoretically improve host immune clearance of filarial parasites. However, this is explicitly flagged in the rationale as a weak, indirect inference — there is no direct literature or trial evidence connecting Mifamurtide to filariasis, and the established first-line treatment for filariasis is antiparasitic chemotherapy, not immune stimulation. The biological plausibility here is low.

Notably, several other top-10 predictions for this drug (autoimmune oophoritis, type 1 diabetes mellitus, diabetic nephropathy) show **mechanistically contradictory** rationale — Mifamurtide's pro-inflammatory action could plausibly *worsen* these autoimmune/inflammatory conditions rather than treat them. This pattern across the candidate set suggests the model is picking up on the drug's general immunostimulant signature rather than disease-specific therapeutic relevance, which should temper confidence in the top-ranked prediction as well.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No EU marketing authorizations are currently on record for this drug in the evidence pack (market status: not marketed, 0 licenses).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: Mechanism of action, key warnings, and contraindications are flagged as a Blocking data gap (DG001) in this evidence pack — TFDA/EMA label data has not yet been retrieved, which prevents a preliminary safety (S1) assessment.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (filariasis) has no clinical trial or literature support and rests on a single, explicitly weak mechanistic inference (L5, S0). Several lower-ranked candidates for this same drug show mechanistically contradictory rationale, suggesting the model's overall signal for Mifamurtide reflects generic immunostimulant activity rather than indication-specific therapeutic relevance. Combined with the absence of EU marketing status and a Blocking-severity safety data gap, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmed original indication and mechanism of action (DrugBank API query, per DG002)
- TFDA/EMA label warnings, contraindications, and DDI data (per DG001, Blocking — required before any S1 safety evaluation)
- Direct clinical or preclinical evidence specifically linking Mifamurtide to filariasis (or reconsideration of lower-scoring but mechanistically coherent candidates)
- Clarification of "not marketed" status in this evidence pack, given inconsistency with the drug's known regulatory history
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

