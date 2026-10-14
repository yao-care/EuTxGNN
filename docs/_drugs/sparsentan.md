---
layout: default
title: Sparsentan
parent: AI Predictions (L5)
nav_order: 574
evidence_level: L5
indication_count: 10
---

# Sparsentan
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

# Sparsentan: From IgA Nephropathy to Alopecia

## One-Sentence Summary

Sparsentan is a dual endothelin type A and angiotensin II type 1 receptor antagonist, originally used to treat primary IgA nephropathy (IgAN) with significant proteinuria.
The TxGNN model predicts it may be effective for **alopecia**, but **no clinical trials and no publications** currently support this direction. The prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of adults with primary IgA nephropathy (IgAN) with urine protein excretion > 1.0 g/day (or urine protein-to-creatinine ratio > 0.75 g/g) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 94.52% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Sparsentan blocks two receptors at once: the endothelin type A receptor (ETA) and the angiotensin II type 1 receptor (AT1). In IgA nephropathy this dual blockade is used to reduce proteinuria. Detailed mechanism of action data is not available in the data compiled for this report, so the analysis below relies on the known targets only.

The link between kidney disease and alopecia is weak. No established connection between endothelin or angiotensin II receptor blockade and hair follicle biology was identified. One speculative route is vasoactive or fibrotic signaling in the scalp microvasculature, but this has not been tested. The high TxGNN score (0.945) is a computational prediction and should not be read as evidence of efficacy.

Other top-ranked predictions are also mostly in hair and skin disorders (congenital hypotrichosis milia, hypotrichosis simplex of the scalp, diffuse alopecia areata, lichen disease, dermatitis). For several of them the plausible mechanism points away from benefit. For example, alopecia areata is driven by autoimmune JAK/STAT and T-cell pathways, which sparsentan does not target. This clustering suggests the model may be picking up a pattern unrelated to sparsentan's actual pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005783 | Filspari | Not specified | Treatment of adults with primary immunoglobulin A nephropathy (IgAN) with a urine protein excretion > 1.0 g/day (or urine protein-to-creatinine ratio > 0.75 g/g, see section 5.1). (Status: cancelled) |

---

## Safety Considerations

- **Drug Interactions**: The interaction query completed and returned only pharmacological target records, not drug-drug interactions. The targets are the angiotensin II type 1 receptor (AGTR1) and the endothelin type A receptor (EDNRA).
- **Class-related concerns from the prediction analysis**: Endothelin and angiotensin receptor antagonists carry embryo-fetal toxicity warnings, so use in pregnancy is a concern. Angiotensin receptor blockade also tends to raise serum potassium (hyperkalemia risk). These points come from general class knowledge, not from the label data compiled for this report.

Please refer to the SmPC for full safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for alopecia is supported only by a model score (L5), with no registered trials or publications and no plausible mechanistic link. The only EU authorization is also listed as cancelled, which adds regulatory uncertainty.

**To proceed, the following is needed:**
- Parse the EU product information to obtain warnings and contraindications. This is a blocking gap for safety screening.
- Obtain detailed mechanism of action data (for example from DrugBank).
- Preclinical or mechanistic studies testing whether ETA/AT1 blockade affects hair follicle biology.
- Clarification of why the EU authorization was cancelled, and of the available routes of administration (for example, whether a topical formulation would be feasible for a scalp condition).
- A review of the other top-ranked predictions, since several show no plausible benefit or point toward risk (for example angioedema and potassium deficiency).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

