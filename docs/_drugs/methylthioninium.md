---
layout: default
title: Methylthioninium
parent: 僅模型預測 (L5)
nav_order: 388
evidence_level: L5
indication_count: 10
---

# Methylthioninium
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

# Methylthioninium: From No Approved Indication to Irritable Bowel Syndrome (Predicted)

## One-Sentence Summary

> Methylthioninium (methylene blue, DrugBank ID DB08167) currently has **no recorded approved indication and is not marketed** under this evidence pack (0 authorizations).
> The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-inference signal with no direct or indirect evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indications on record, drug not currently marketed |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 90.43% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for methylthioninium in this evidence pack, and no approved original indication is on record — the compound is not currently marketed (0 authorizations, decision stage S0).

The only mechanistic rationale accompanying the top prediction states: *"Methylene blue (Methylthioninium) is a guanylate cyclase/NOS inhibitor, theoretically capable of affecting intestinal smooth muscle tone and visceral sensitivity; however, there is no direct or indirect clinical data supporting its use in IBS — this is purely a TxGNN network-inference association with no supporting mechanistic literature."* This is explicitly flagged by the source data as inference-only reasoning, not an established pharmacological link.

Because both the original indication and MOA are undocumented here, the mechanistic plausibility of repurposing toward IBS cannot be independently corroborated, and this prediction should be treated as a hypothesis-generation signal rather than an evidence-backed candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No marketing authorizations are on record for methylthioninium (0 licenses); the compound is not currently marketed in the evaluated jurisdiction.

---

## Safety Considerations

Please refer to the SmPC for safety information.

**Note:** Safety warnings and contraindications for this compound are flagged as a **Blocking data gap** (DG001) — TFDA/regulatory label warnings and contraindications have not yet been retrieved, which prevents progression to the S1 safety pre-screening stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (Irritable Bowel Syndrome, TxGNN score 90.43%) is an L5, S0-stage signal with zero supporting clinical trials or literature, and the drug itself lacks basic regulatory and mechanism-of-action data needed for any safety pre-screening.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (Blocking gap — required before S1 safety evaluation)
- Mechanism of action (MOA) confirmation via DrugBank API (High-priority gap)
- Original/approved indication history for the compound, to establish a baseline for repurposing rationale
- Any preclinical or mechanistic literature specific to gastrointestinal motility/visceral sensitivity to substantiate the IBS hypothesis before further evidence collection is prioritized
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

