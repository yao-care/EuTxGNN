---
layout: default
title: Propranolol
parent: AI Predictions (L5)
nav_order: 485
evidence_level: L5
indication_count: 10
---

# Propranolol
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

Using superpowers:brainstorming skill check — not applicable here (this is a fully-specified content generation task with an explicit template and evidence pack already supplied, not a design/planning task). Proceeding directly to draft the report per the given v5 prompt spec.

Note before the report: `predicted_indications[0]` in this Evidence Pack is **"distal myopathy, Tateyama type"** — the highest TxGNN score but with **zero clinical trials, zero literature, and an explicit note in the pack's own rationale that there is no known mechanistic link**. Per the template rules I've generated the report strictly around this top-ranked candidate. Rank 6–10 candidates (cardiomyopathy, hemangioma-related indications) have substantially stronger evidence (L2–L3) and are flagged in the Conclusion section for reprioritization.

---

# Propranolol: From Unspecified Original Indication to Distal Myopathy, Tateyama Type

## One-Sentence Summary

> This Evidence Pack does not contain data on propranolol's original approved indication or mechanism of action (both marked as data gaps).
> The TxGNN model's top-ranked prediction is **Distal Myopathy, Tateyama Type**, with a **99.40% prediction score**,
> but currently **0 clinical trials** and **0 publications** support this specific prediction, and the pack's own mechanistic review flags it as biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in Evidence Pack (data gap — `drug.original_indications` and `taiwan_regulatory.licenses` are both empty) |
| Predicted New Indication | Distal myopathy, Tateyama type |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for propranolol in this Evidence Pack (marked as a Blocking/High-severity data gap: DG002). No original indication data is available either, so the relationship between propranolol's known pharmacology and this new prediction cannot be established from the pack itself.

The pack's own mechanistic assessment for this specific prediction is explicitly negative: distal myopathy, Tateyama type is a structural skeletal muscle disease caused by *TTN* (titin) gene mutations. This is a mechanism entirely unrelated to β-adrenergic receptor antagonism, which is propranolol's core pharmacological action. The Evidence Pack states there is "no known overlap" between the two, and that the model's high confidence score likely reflects a lack of biological plausibility rather than a genuine therapeutic signal.

In short: this is a case where a high TxGNN score is **not** corroborated by mechanism, clinical trials, or literature — the textbook profile of an L5 "prediction-only" candidate that should not proceed without independent validation.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## EU Market Information

Currently no EU marketing authorizations recorded in this evidence pack (`taiwan_regulatory.total_licenses = 0`, market status: not marketed).

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction scores highly (99.40%) but has no supporting clinical trials, no supporting literature, and the pack's own mechanistic analysis explicitly finds no biological plausibility linking propranolol's β-blocking action to a TTN-mutation-driven structural myopathy. This meets the L5 threshold ("model prediction only, no actual studies") and does not warrant further evaluation as currently framed.

**To proceed, the following is needed:**
- Resolve DG002 (mechanism of action) via DrugBank API before any mechanistic re-assessment is attempted
- Resolve DG001 (TFDA/EU label warnings and contraindications) — currently blocking, as safety screening (S1) cannot begin without it
- Independent preclinical or genetic-pathway evidence directly linking β-adrenergic signaling to titin-related myopathy, if this candidate is to be reconsidered
- **Reprioritization note**: this same Evidence Pack contains substantially better-supported candidates further down the ranking — notably *breast capillary hemangioma* (L2, includes a completed 500-patient post-marketing study of Hemangiol) and *intramuscular hemangioma* (L2, extensive mechanistic and clinical literature) — which more closely match propranolol's established anti-angiogenic mechanism and may be more productive next steps than this top-ranked candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

