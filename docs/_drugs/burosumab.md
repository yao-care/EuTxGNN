---
layout: default
title: Burosumab
parent: AI Predictions (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Burosumab: predicted new indication Renal osteodystrophy (evidence level L5). Approved use: X-linked hypophosphataemia in children and adolescents aged 1 to 17 y…"
monitor_inn: "Burosumab"
predicted_indications: ["renal osteodystrophy", "impaired renal function disease", "non-renal secondary hyperparathyroidism", "bone remodeling disease", "hyperparathyroidism, transient neonatal", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic cataract", "hypocalcemic rickets", "nuclear senile cataract"]
---

# Burosumab
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

# Burosumab: From X-linked Hypophosphataemia to Renal Osteodystrophy

## One-Sentence Summary

Burosumab is an anti-FGF23 antibody originally used to treat X-linked hypophosphataemia (XLH) and FGF23-related hypophosphataemia in tumour-induced osteomalacia.
The TxGNN model predicts it may be effective for **renal osteodystrophy**, but there are **no registered clinical trials** and only **2 review articles** that give no direct clinical data for this use. Evidence rests on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | X-linked hypophosphataemia in children and adolescents aged 1 to 17 years with radiographic evidence of bone disease, and in adults; FGF23-related hypophosphataemia in tumour-induced osteomalacia |
| Predicted New Indication | Renal osteodystrophy |
| TxGNN Prediction Score | 96.93% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Burosumab is known as a monoclonal antibody that neutralizes FGF23, the hormone that drives renal phosphate wasting in XLH and tumour-induced osteomalacia. By blocking FGF23, it raises serum phosphate and supports bone mineralization.

Renal osteodystrophy is the bone component of chronic kidney disease–mineral and bone disorder (CKD-MBD), where FGF23 is markedly elevated. In principle, anti-FGF23 therapy might improve mineralization. This is the basis of the model's prediction.

There is an important caveat. In CKD, high FGF23 is a compensatory response to phosphate retention. Blocking it could worsen hyperphosphataemia and vascular calcification. The two retrieved publications, a CKD-MBD review and a paediatric metabolic bone disorder review, provide no direct clinical data for burosumab in renal osteodystrophy. The prediction should be treated as a research question, not a treatment hypothesis ready for development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42438722](https://pubmed.ncbi.nlm.nih.gov/42438722/) | 2026 | Review | Kidney International Reports | Reviews CKD-MBD pathophysiology, controversies and gaps, including CKD-associated osteoporosis; no burosumab-specific data |
| [37927073](https://pubmed.ncbi.nlm.nih.gov/37927073/) | 2024 | Review | Current Pediatric Reviews | Diagnosis and new treatments for hypophosphatasia and XLH in children; relevant to the original indication, not renal osteodystrophy |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004275 | Crysvita | Not specified | Crysvita is indicated for the treatment of X-linked hypophosphataemia, in children and adolescents aged 1 to 17 years with radiograph... |

The only authorization is recorded as cancelled, so there is currently no valid EU marketing authorization in the data compiled for this report.

---

## Safety Considerations

- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph links burosumab to a contraindication in kidney failure. This comes from graph edges, not label text, but it is directly relevant to a CKD-related target.
- **Drug Interactions**: 9 interactions were identified.
  - Major: calcium phosphate, calcifediol, calcitriol, dihydrotachysterol, sodium cellulose phosphate, doxercalciferol, paricalcitol
  - Moderate: cinacalcet, etelcalcetide

  Many of these agents are standard in CKD-MBD management, so co-prescription is likely in the proposed population.

Please refer to the SmPC for warnings and contraindications from the product label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by model scoring, with no clinical trials and no direct clinical literature. The mechanism raises a safety concern: blocking compensatory FGF23 in CKD may worsen hyperphosphataemia and vascular calcification. A kidney failure contraindication signal and major interactions with standard CKD-MBD drugs add to this concern. The EU authorization is also recorded as cancelled.

**To proceed, the following is needed:**
- Label warnings and contraindications from the SmPC, which are currently missing
- Detailed mechanism of action data
- Preclinical or mechanistic studies of FGF23 blockade in CKD-MBD, focusing on phosphate and vascular calcification
- Clarification of the cancelled EU authorization status
- If safety allows, a carefully designed early-phase study in a defined CKD population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

