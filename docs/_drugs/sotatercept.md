---
layout: default
title: Sotatercept
parent: AI Predictions (L5)
nav_order: 552
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept: From Unestablished Indication (Not Yet Marketed) to Acute Lymphoblastic Leukemia

## One-Sentence Summary

Sotatercept has no approved indication on file in the current evidence pack — it is not yet marketed in the EU, and its original mechanism of action is not documented in this dataset. The TxGNN model predicts it may be relevant to **Acute Lymphoblastic Leukemia**, but this prediction is currently unsupported by any clinical trials or published literature, and the model's own rationale describes the mechanistic link as unclear.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no EU marketing authorization or documented indication in this dataset |
| Predicted New Indication | Acute Lymphoblastic Leukemia (disease) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured `original_moa` field. However, the model's own rationale notes suggest Sotatercept acts on Activin/GDF ligands and ActRIIA receptor signalling, primarily affecting bone metabolism, erythropoiesis, and vascular remodeling — a profile consistent with the ActRIIA-Fc fusion protein class, but this is not formally confirmed within the evidence pack.

For the top-ranked prediction (Acute Lymphoblastic Leukemia), the model's own assessment explicitly states there is **no clear mechanistic link**: ALL pathogenesis centers on malignant transformation of lymphoid progenitor cells, which has no known intersection with Activin/ActRIIA signalling. The evidence pack suggests this association likely arises from indirect nodes in the knowledge graph (e.g., shared downstream signalling pathways) rather than direct biological evidence.

Notably, a lower-ranked candidate in this dataset — **drug-induced osteoporosis** (rank 4) — carries a substantially stronger mechanistic rationale: Activin A is a known osteoclast-activating factor, and ActRIIA-Fc class molecules (e.g., the related compound ACE-011) have documented effects promoting osteoblast activity while suppressing osteoclast function. This is flagged in the source data as a "Research Question" (decision stage S1) rather than "Hold," and may warrant a separate, dedicated literature review outside the scope of this report's top-ranked candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## EU Market Information

Sotatercept currently has no EU marketing authorization on record (0 licenses, market status: Not marketed). No product, dosage form, or approved indication data is available for this drug in the evidence pack.

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Acute Lymphoblastic Leukemia) is supported only by a TxGNN model score with zero corroborating clinical trials or literature (Evidence Level L5), and the model's own mechanistic rationale explicitly characterizes the biological link as indirect and unsupported. Combined with the fact that Sotatercept is not marketed in the EU and lacks documented original indication or MOA data, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Drug label warnings and contraindications (currently blocking — flagged as a critical data gap; source: regulatory label/SmPC)
- Confirmed mechanism of action data (currently a high-severity gap; source: DrugBank or equivalent regulatory documentation)
- Original approved indication(s) and EU marketing authorization status, to establish a proper repurposing baseline
- If pursuing further investigation, prioritize a targeted literature review of the drug-induced osteoporosis signal (rank 4), which carries a more biologically plausible mechanistic rationale than the top-ranked ALL prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

