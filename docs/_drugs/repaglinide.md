---
layout: default
title: Repaglinide
parent: AI Predictions (L5)
nav_order: 518
evidence_level: L5
indication_count: 10
---

# Repaglinide
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

# Repaglinide: From Type 2 Diabetes to Opsismodysplasia

## One-Sentence Summary

Repaglinide is an insulin secretagogue originally used to lower blood glucose in adults with type 2 diabetes.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia, but **no clinical trials and no directly relevant publications** currently support this prediction. It is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (NIDDM) whose hyperglycaemia can no longer be controlled satisfactorily by diet, weight reduction and exercise; also in combination with metformin |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 98.77% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 6 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, repaglinide is a short-acting insulin secretagogue that blocks K-ATP channels (SUR1/Kir6.2) in pancreatic beta cells, which stimulates insulin release around meals. Its efficacy in type 2 diabetes is established.

For opsismodysplasia, no mechanistic link can be identified. This condition is a skeletal dysplasia caused by mutations in INPPL1 (SHIP2). Nothing known about repaglinide's action on beta-cell K-ATP channels connects to this pathway. The high TxGNN score appears to reflect network-based associations in the knowledge graph rather than biological or clinical support.

The other top-ranked predictions show the same pattern. Stiff person spectrum disorders, localized lipodystrophies, and autoimmune oophoritis have no established mechanistic connection. Pancreatic agenesis is mechanistically implausible, because repaglinide needs functional beta cells to work.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for opsismodysplasia.

## EU Market Information

All six EU authorizations have been cancelled, and no valid authorization remains.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000187 | NovoNorm | Not specified | Type 2 diabetes (NIDDM) not controlled by diet, weight reduction and exercise; also in combination with metformin... |
| EMEA/H/C/000362 | Prandin | Not specified | Type 2 diabetes (NIDDM) not controlled by diet, weight reduction and exercise; also in combination with metformin... |
| EMEA/H/C/001065 | Enyglid | Not specified | Type 2 diabetes (NIDDM) not controlled by diet, weight reduction and exercise; also in combination with metformin... |
| EMEA/H/C/001067 | Repaglinide Teva | Not specified | Type 2 diabetes (NIDDM) not controlled by diet, weight reduction and exercise; also in combination with metformin... |
| EMEA/H/C/001066 | Repaglinide Krka | Not specified | Type 2 diabetes (NIDDM) not controlled by diet, weight reduction and exercise. Treatment should be initiated as an... |

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** kidney disease, liver disease, gallbladder disease, pituitary hormone deficiencies (including hypopituitarism and Sheehan syndrome), adrenal insufficiency/Addison disease, hypogonadotropic hypogonadism/Kallmann syndrome, thymus gland disease, pyoureter, and infectious disease. These come from model-derived graph links and need confirmation against the official product information.
- **Drug Interactions:** 100 interactions were recorded. The ones shown are mostly Moderate, with a few Minor (topical corticosteroids):
  - Moderate: ethanol, ibuprofen, ketorolac, nifedipine, hydrochlorothiazide, acetazolamide, hydrocortisone, ethinylestradiol, epinephrine, phenylephrine, pseudoephedrine, salbutamol, formoterol, acebutolol, abiraterone, abametapir (topical), and the antidiabetics albiglutide and alogliptin.
  - Minor: topical hydrocortisone and topical alclometasone.

Please refer to the SmPC for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a network-based model score. There are no clinical trials, no relevant publications, and no plausible mechanism linking repaglinide to opsismodysplasia. All EU authorizations are also cancelled.

**To proceed, the following is needed:**
- A plausible biological rationale connecting K-ATP channel blockade or insulin secretion to INPPL1/SHIP2-related skeletal dysplasia, backed by preclinical data
- Mechanism of action data to support mechanistic analysis
- Warnings and contraindications from the official EU product information, for a formal safety screen
- Current market and availability status, given that all EU licences are cancelled
- Reassessment of other predictions with some biological plausibility, such as diabetes-associated thiamine-responsive syndromes, where repaglinide would only be symptomatic treatment of hyperglycaemia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

