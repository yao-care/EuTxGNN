---
layout: default
title: Sargramostim
parent: AI Predictions (L5)
nav_order: 547
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sargramostim: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Treatment of patients of all ages acutely exposed to myelosuppressive…"
---

# Sargramostim
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

# Sargramostim: From Haematopoietic Sub-syndrome of Acute Radiation Syndrome to Drug-Induced Osteoporosis

## One-Sentence Summary

Sargramostim is a myeloid growth factor (GM-CSF) that was authorised in the EU for patients acutely exposed to myelosuppressive doses of radiation (Haematopoietic Sub-syndrome of Acute Radiation Syndrome, H-ARS).
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but **no clinical trials and no publications** currently support this direction, so it rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of patients of all ages acutely exposed to myelosuppressive doses of radiation with Haematopoietic Sub-syndrome of Acute Radiation Syndrome (H-ARS) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 98.99% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sargramostim is a recombinant GM-CSF, a growth factor acting on myeloid lineage cells. Its efficacy in restoring blood-cell production after radiation-induced myelosuppression underlies its original indication, and mechanistically it may be relevant to other conditions involving myeloid cells.

For drug-induced osteoporosis, the only conceivable link is that GM-CSF acts on myeloid cells, including osteoclast precursors, so a biological connection to bone remodelling is possible. However, the direction of the effect (bone-resorptive versus protective) is not established, and no supporting data were compiled for this report. The high TxGNN score (0.990) should therefore be treated as a hypothesis, not as evidence of benefit. The original indication (acute radiation haematopoietic injury) and the predicted indication (bone loss caused by medicines) are clinically unrelated.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/006411 (cancelled) | Imreplys | Not specified | Treatment of patients of all ages acutely exposed to myelosuppressive doses of radiation with Haematopoietic Sub-syndrome of Acute Radiation Syndrome (H-ARS)... |

---

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interactions in total (the first 20 were reviewed here), all rated **Moderate**. Examples include:
  - Radiopharmaceuticals and radioimmunotherapies: iobenguane (I-131), fludeoxyglucose (18F), ibritumomab tiuxetan, tositumomab, tositumomab (I-131)
  - Cytotoxic and antineoplastic agents: paclitaxel, mercaptopurine, azacitidine, bendamustine, arsenic trioxide, trimetrexate, altretamine, asparaginase (E. coli)
  - Targeted and immune-modulating agents: abemaciclib, acalabrutinib, avapritinib, aldesleukin, alemtuzumab, belantamab mafodotin, levamisole

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for drug-induced osteoporosis is supported only by the model score, with no clinical trials, no literature and no established mechanism. In addition, the only EU authorisation is cancelled, which limits near-term development in the EU.

**To proceed, the following is needed:**
- A systematic literature search on GM-CSF/sargramostim and bone metabolism, including the direction of effect on osteoclasts
- Preclinical studies in models of drug-induced bone loss
- Mechanism of action data and warnings/contraindications from the product information
- Clarification of route and formulation availability, given the cancelled authorisation
- A review of the other predicted indications; none currently has stronger support. Cervical neuroblastoma (score 96.2%) is linked to two trials, but both test GM-CSF in different settings (a Ras-peptide vaccine in adult solid tumours, and mouthwash for mucositis) and do not address the predicted disease.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

