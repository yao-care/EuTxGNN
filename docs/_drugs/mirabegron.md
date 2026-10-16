---
layout: default
title: Mirabegron
parent: AI Predictions (L5)
nav_order: 411
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mirabegron: predicted new indication Thoracic malformation (evidence level L5). Approved use: Overactive bladder in adults (urgency…"
---

# Mirabegron
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

# Mirabegron: From Overactive Bladder to Thoracic Malformation

## One-Sentence Summary

Mirabegron is a beta-3 adrenergic agonist, originally used to treat overactive bladder in adults and neurogenic detrusor overactivity in children.
The TxGNN model predicts it may be effective for **thoracic malformation**, but **no clinical trials and no publications** currently support this prediction.
It is a graph-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Overactive bladder in adults (urgency, increased micturition frequency and/or urgency incontinence); neurogenic detrusor overactivity in paediatric patients aged 3 to <18 years |
| Predicted New Indication | Thoracic malformation |
| TxGNN Prediction Score | 83.06% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, mirabegron is a beta-3 adrenergic agonist that relaxes the smooth muscle of the bladder detrusor, and its efficacy in overactive bladder has been established.

The review of this prediction found no clinically supported mechanistic link. No known pathway connects beta-3 agonism to the development of thoracic malformations, which are structural developmental conditions. The score of 0.831 comes from the knowledge graph model alone and may reflect indirect graph proximity rather than a therapeutic mechanism.

Other top-ranked predictions are also unsupported. These include renal-hepatic-pancreatic dysplasia, polycystic kidney disease 3, Joubert syndrome with renal defect, esophageal varices, and several rare hair and kidney disorders. None has trials or literature, and all are rated L5 and Hold. For polycystic kidney disease, a speculative cAMP-related concern suggests potential harm rather than benefit, because beta-3 agonism raises cAMP, which drives cyst growth.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002388 (cancelled) | Betmiga | Prolonged-release tablet | Overactive bladder in adults; neurogenic detrusor overactivity in paediatric patients aged 3 to less than 18 years |

## Safety Considerations

- **Knowledge-graph contraindication signals**: hypertensive disorder and hypertension. These come from the TxGNN knowledge graph, not from label text.
- **Drug Interactions**: 70 interactions were identified in total. The main ones are:
  - **Major**: eliglustat
  - **Moderate**: lorcaserin, trospium, metoclopramide, dexfenfluramine, fenfluramine, glycerol phenylbutyrate, promethazine, lusutrombopag, fostamatinib
  - Many others are Minor (for example aprepitant, dexamethasone, cimetidine, clarithromycin, warfarin).

Please refer to the SmPC for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no clinical trials, no literature, and no plausible mechanistic link. The product's only EU authorization is also cancelled. The knowledge-graph hypertension signal adds a further caution.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological rationale linking beta-3 agonism to thoracic malformation
- Preclinical or literature evidence supporting the prediction
- Label warnings and contraindications from the SmPC to complete safety screening
- Clarification of the cancelled EU authorization status
- Review of whether the target condition is a structural malformation that a symptomatic drug could plausibly treat
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

