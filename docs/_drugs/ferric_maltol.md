---
layout: default
title: Ferric Maltol
parent: AI Predictions (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ferric Maltol: predicted new indication Plummer-Vinson syndrome (evidence level L5). Approved use: Treatment of iron deficiency in adults"
monitor_inn: "Ferric maltol"
predicted_indications: ["Plummer-Vinson syndrome", "vitamin B12- and folate-independent constitutional megaloblastic anemia", "IRIDA syndrome", "biotin metabolic disease", "severe nonproliferative diabetic retinopathy", "ariboflavinosis", "Keshan disease", "non-syndromic esophageal malformation", "protein-energy malnutrition"]
---

# Ferric Maltol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ferric Maltol: From Iron Deficiency to Plummer-Vinson Syndrome
{: .text-alpha }

## One-Sentence Summary

Ferric maltol is an oral iron replacement, originally used to treat iron deficiency in adults. The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome**, but **no clinical trials and no publications** were found, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of iron deficiency in adults |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, ferric maltol is an oral iron replacement. Its efficacy in iron deficiency is the basis of its approval, and mechanistically it may be applicable to conditions in which iron deficiency is a key feature.

Plummer-Vinson syndrome is characterized by iron deficiency anemia, dysphagia and esophageal webs. Correcting the iron deficiency is therefore a plausible link, and the high score probably reflects the overlap with the approved indication. However, iron repletion alone is not expected to resolve the esophageal web component, and no trials or literature support the prediction.

Other predictions (ranks 2–10) are also unsupported by any clinical evidence:
- **Somewhat plausible, as adjunctive use only:** folic acid deficiency anemia (mixed deficiency), protein-energy malnutrition (supportive iron repletion, with caution regarding infection risk).
- **Likely limited by biology:** IRIDA syndrome. Elevated hepcidin blocks intestinal iron absorption, so oral iron is characteristically poorly effective, and parenteral iron is the usual approach.
- **Weak or no mechanistic link, probably graph artifacts:** B12- and folate-independent megaloblastic anemia, biotin metabolic disease, severe nonproliferative diabetic retinopathy, ariboflavinosis, Keshan disease, non-syndromic esophageal malformation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002733 (cancelled) | Feraccru | Not specified | Treatment of iron deficiency in adults |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease contraindication edges, not label text): hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease. These are consistent with the general caution against iron supplementation in iron-overload states.
- **Additional caution from the prediction analysis:** Excess iron may contribute to oxidative stress in diabetic complications, and iron supplementation in malnourished patients at risk of infection requires caution.

No drug interaction records were found. Please refer to the SmPC for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model (L5). The only mechanistically plausible candidate, Plummer-Vinson syndrome, largely overlaps with the already approved indication of iron deficiency. The EU authorization is cancelled, and label safety information could not be obtained.

**To proceed, the following is needed:**
- Label warnings and contraindications from the EMA documentation, which are required before safety screening
- Mechanism of action data (for example from DrugBank)
- A literature and trial search specific to iron therapy in Plummer-Vinson syndrome and mixed deficiency anemia
- Clarification of why the EU authorization was cancelled and whether the product is available in any form
- Assessment of whether any benefit is distinct from the existing iron deficiency indication, since the esophageal web component is not expected to respond to iron alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

