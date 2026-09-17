---
layout: default
title: Tenecteplase
parent: AI Predictions (L5)
nav_order: 578
evidence_level: L5
indication_count: 10
---

# Tenecteplase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tenecteplase: From Acute Myocardial Infarction (Thrombolysis) to Posterolateral Myocardial Infarction

## One-Sentence Summary

Tenecteplase is a fibrin-specific plasminogen activator (thrombolytic agent); formal original-indication text and detailed mechanism-of-action data are not available in this dataset, but contextual evidence points to use in acute myocardial infarction/thrombosis. The TxGNN model predicts it may be effective for **Posterolateral Myocardial Infarction**, but this specific prediction is currently **not supported by any clinical trial or literature** — it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current dataset (regulatory record shows 0 EU licenses; see Data Gap DG001) — contextually implied to be acute myocardial infarction / arterial thrombosis based on thrombolytic mechanism |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only — no clinical trials, no literature) |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not directly available for tenecteplase (marked as a Data Gap, DG002). However, other entries within this Evidence Pack consistently describe tenecteplase as acting through **plasminogen activation** (fibrinolysis), i.e. it is a thrombolytic agent that breaks down blood clots. Literature retrieved for related predictions in this pack (e.g. PMID 18183355, PMID 23975441) confirm real-world use of tenecteplase for thrombus-related acute myocardial infarction and pulmonary embolism, which is consistent with this mechanistic class.

Posterolateral myocardial infarction is an anatomical subtype of myocardial infarction, distinguished by the coronary territory involved (posterolateral wall) rather than by a distinct underlying pathology. Since thrombolytic therapy targets the culprit coronary thrombus itself rather than a specific infarct location, the same biological rationale that supports tenecteplase in myocardial infarction generally would be expected to extend to this anatomical subtype.

This mechanistic plausibility is indirectly reinforced elsewhere in the Evidence Pack: other TxGNN-predicted MI subtypes for this drug (e.g. septal MI, coronary stenosis) are backed by actual clinical trial and literature evidence, including a completed Phase 2 trial (NCT00604695) and multiple studies on intracoronary tenecteplase during PCI for STEMI. This suggests the underlying knowledge-graph signal for "tenecteplase → myocardial infarction subtypes" reflects a real pharmacological relationship, even though the specific posterolateral subtype itself has not yet been directly studied.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU marketing authorization records are present in this dataset (0 licenses on file). This should be verified against the EMA product database, as tenecteplase-containing products are known to be marketed in the EU under other names; the absence of records here likely reflects a data gap rather than confirmed non-authorization.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (posterolateral myocardial infarction, TxGNN score 99.87%) has no supporting clinical trials or literature (Evidence Level L5), and critical safety inputs — warnings, contraindications, and regulatory/market data — are all marked as data gaps, including a **blocking** gap (DG001) that prevents even an initial safety screen (S1).

**To proceed, the following is needed:**
- TFDA/EMA product label (SmPC) — warnings and contraindications (DG001, blocking)
- Confirmed mechanism-of-action source from DrugBank (DG002)
- Verification of EU marketing authorization status for tenecteplase (current record shows 0 licenses, which should be cross-checked against EMA's product register)
- Indication-specific evidence for posterolateral MI; alternatively, consider evaluating the related "coronary stenosis" prediction (rank 5), which already has completed Phase 2 trial data (NCT00604695) and multiple supporting publications, as a stronger near-term repurposing candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

