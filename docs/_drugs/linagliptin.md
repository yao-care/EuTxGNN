---
layout: default
title: Linagliptin
parent: AI Predictions (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Linagliptin: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus (glycaemic control in adults…"
---

# Linagliptin
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

# Linagliptin: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Linagliptin is a DPP-4 inhibitor originally used to improve glycaemic control in adults with type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia,
but **no clinical trials and no publications** currently support this prediction; it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (glycaemic control in adults, as monotherapy or in combination with metformin, a sulphonylurea and/or insulin) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 94.90% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, linagliptin belongs to the DPP-4 inhibitor class, and its efficacy in type 2 diabetes is established. DPP-4 inhibitors prolong the activity of incretin hormones, which supports glucose-dependent insulin secretion.

Opsismodysplasia is a rare skeletal dysplasia caused by mutations in INPPL1 (SHIP2). The data compiled for this report show no plausible link between DPP-4 inhibition and this disease. The high TxGNN score (0.949) most likely reflects proximity in the model's knowledge graph rather than a demonstrated biological mechanism. The prediction should therefore be treated as a hypothesis-generating signal, not as evidence of benefit.

Other highly ranked predictions for this drug (for example thiamine-responsive dysfunction syndrome, stiff person syndrome, localized lipodystrophies, pancreatic agenesis and homozygous familial hypercholesterolemia) also have no supporting trials, and their mechanistic links are speculative or implausible.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for opsismodysplasia.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002110 (status: cancelled) | Trajenta | Not specified | Type 2 diabetes mellitus to improve glycaemic control in adults: as monotherapy when metformin is inappropriate or contraindicated, and in combination with metformin, a sulphonylurea and metformin, or insulin with or without metformin... |

## Safety Considerations

- **Disease associations from the knowledge graph** (these are model-derived contraindication edges, not label text): hypoglycemia and pancreatitis.
- **Drug Interactions**: The interaction screen returned 100 records; the 20 listed here are mostly Moderate, with a few Minor. Moderate-level interactions include:
  - Sympathomimetics and bronchodilators: phenylephrine, pseudoephedrine, epinephrine, formoterol, salbutamol
  - Corticosteroids: hydrocortisone
  - Hormonal agents: estradiol, levonorgestrel, norethisterone, desogestrel
  - Diuretics and antihypertensives: hydrochlorothiazide, acetazolamide, benazepril
  - Other: ethanol, alpelisib, apalutamide, amobarbital, abametapir (topical)
  - Minor-level interactions: topical hydrocortisone and topical alclometasone

Please refer to the SmPC for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or literature and no plausible mechanistic link between DPP-4 inhibition and opsismodysplasia. In addition, the only EU authorization is cancelled, and label-based safety data are missing.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) and a credible biological hypothesis linking DPP-4 inhibition to INPPL1/SHIP2-related skeletal pathology
- Preclinical or mechanistic studies in relevant disease models
- Label-based warnings and contraindications from the SmPC, to allow safety screening
- Clarification of the current EU regulatory status of linagliptin products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

