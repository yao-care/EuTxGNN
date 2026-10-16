---
layout: default
title: Osilodrostat
parent: AI Predictions (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Osilodrostat: predicted new indication Familial generalized lentiginosis (evidence level L5). Approved use: Endogenous Cushing's syndrome in adults"
---

# Osilodrostat
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

# Osilodrostat: From Endogenous Cushing's Syndrome to Familial Generalized Lentiginosis

## One-Sentence Summary

Osilodrostat (marketed as Isturisa) was originally used to treat endogenous Cushing's syndrome in adults.
The TxGNN model predicts it may be effective for **familial generalized lentiginosis**, but **no clinical trials and no publications** currently support this direction.
The prediction rests on a network-based score alone, and the available pharmacology argues against benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endogenous Cushing's syndrome in adults |
| Predicted New Indication | Familial generalized lentiginosis |
| TxGNN Prediction Score | 98.19% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, osilodrostat is an inhibitor of 11-beta-hydroxylase (CYP11B1), the enzyme that catalyses the last step of cortisol synthesis. Its efficacy in Cushing's syndrome comes from lowering cortisol. This mechanism description is not verified by the supplied data.

Lowering cortisol removes negative feedback on the pituitary, so ACTH and POMC-derived peptides tend to rise. These peptides stimulate melanocortin-1 receptor (MC1R) signalling and can increase pigmentation. In a lentiginosis phenotype, this could worsen the condition rather than treat it.

The link between Cushing's syndrome and familial generalized lentiginosis is therefore weak. The high score (98.19%, rank 15,522) likely reflects shared annotations in the knowledge graph, not a verified therapeutic rationale. The other nine top predictions (including café-au-lait macule syndrome, acromelanosis, Moynahan syndrome, rhabdoid tumor, and peripheral nerve schwannoma) share the same limitation: network scores only, with no clinical or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004821 (cancelled) | Isturisa | Not specified | Treatment of endogenous Cushing's syndrome in adults |

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records. Most are Moderate, and a few are Major or Minor. Examples from the data compiled for this report:
  - **Major**: Clarithromycin, Dolasetron
  - **Moderate**: Famotidine, Alosetron, Loperamide, Aprepitant, Omeprazole, Dexamethasone, Budesonide, Cimetidine, Levofloxacin, Metreleptin, Palonosetron
  - **Minor**: Naloxegol

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a knowledge-graph score, with no trials or publications. Osilodrostat's expected effect of raising ACTH points against benefit in pigmentary disorders. The EU authorization is also cancelled.

**To proceed, the following is needed:**
- Verified mechanism of action data from DrugBank
- Warnings and contraindications from the EMA product information, required before any safety screening
- Preclinical or clinical evidence showing a plausible benefit in lentiginosis, given the risk of ACTH-driven pigmentation
- Clarification of why the EU authorization was cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

