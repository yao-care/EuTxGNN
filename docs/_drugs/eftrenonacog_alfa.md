---
layout: default
title: Eftrenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 10
---

# Eftrenonacog Alfa
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

# Eftrenonacog Alfa: From Factor IX Replacement Therapy to Pseudo-von Willebrand Disease

## One-Sentence Summary

Eftrenonacog alfa is a recombinant coagulation Factor IX–Fc fusion protein whose established mechanism is Factor IX replacement; formal original-indication data is not on file for this evaluation. The TxGNN model's top prediction is **Pseudo-von Willebrand Disease**, but this candidate currently has **no clinical trials** and **no published literature** to support it, and the drug itself is not marketed in Taiwan.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license records or indication text on file (0 licenses) |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Market Status (Taiwan) | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Eftrenonacog alfa is currently a data gap in this evaluation, and no original indication is recorded in the structured data. The only mechanistic information available comes from the model's own rationale notes, which describe Eftrenonacog alfa as a recombinant Factor IX–Fc fusion protein whose known action is supplementing coagulation Factor IX.

Critically, the rationale generated for the top-ranked prediction (Pseudo-von Willebrand Disease) explicitly states that this is a platelet GPIbα-mutation disorder driven by abnormal platelet-VWF affinity — a platelet function defect, not a coagulation factor deficiency — and that it has **no direct physiological relationship** to Factor IX supplementation. This suggests the #1 ranked candidate may reflect knowledge-graph embedding similarity rather than a genuine mechanistic signal.

Of the ten candidates in this pack, the mechanistically strongest link is actually **rank 4, "acquired coagulation factor deficiency"** — the rationale for that candidate notes that if this category includes acquired Factor IX deficiency (e.g., autoimmune inhibitors, hepatic disease, DIC-related consumption), direct FIX supplementation has genuine physiological plausibility, though it is likewise unsupported by any clinical or literature evidence to date.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Market Information (Taiwan)

Currently not marketed in Taiwan; no authorization records available (0 licenses on file).

## Safety Considerations

Please refer to the SmPC for safety information. TFDA label warnings and contraindications for this product have not yet been retrieved for this evaluation (flagged as a blocking data gap).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications are rated L5 (model prediction only) with zero supporting clinical trials or literature, and the pipeline's own scoring independently recommends "Hold" for every candidate. The drug is not currently marketed in Taiwan, and core safety data (warnings, contraindications) is an unresolved blocking gap, so this candidate cannot proceed to safety screening (S1) as-is.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, blocking) — required before any S1 safety screening
- Confirmed original indication and mechanism-of-action data (DG002)
- Clinical or literature evidence for the top candidates, with priority re-evaluation of rank 4 ("acquired coagulation factor deficiency"), which the model's own rationale flags as mechanistically stronger than the current #1-ranked candidate
- Reassessment of whether Pseudo-von Willebrand Disease should remain the lead candidate given the rationale's own note of no direct mechanistic link
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

