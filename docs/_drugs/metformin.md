---
layout: default
title: Metformin
parent: AI Predictions (L5)
nav_order: 383
evidence_level: L5
indication_count: 10
---

# Metformin
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

# Metformin: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Metformin is a globally established first-line biguanide agent for Type 2 Diabetes Mellitus. The TxGNN model predicts a possible new application in **Focal Stiff Limb Syndrome**, but the current Evidence Pack contains **only a model prediction score (99.45%)** — no clinical trials and no supporting literature exist for this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this Evidence Pack (no Taiwan/EU license data available); Metformin is globally recognized as a first-line treatment for Type 2 Diabetes Mellitus |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on general background knowledge, Metformin belongs to the biguanide class of antidiabetic agents, acting primarily by reducing hepatic glucose production, decreasing intestinal glucose absorption, and improving peripheral insulin sensitivity. Its efficacy in Type 2 Diabetes Mellitus is well established.

There is, however, no known pharmacological or mechanistic rationale connecting Metformin to Focal Stiff Limb Syndrome, a rare neuromuscular/autoimmune disorder. The prediction rests solely on the TxGNN knowledge-graph score (0.994); no mechanistic literature or clinical evidence supports this link. The same holds for the other top-ranked candidates in this pack (e.g., Classic Stiff Person Syndrome, Opsismodysplasia), which also lack any biological rationale beyond the model score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Candidate Indications Reviewed (Ranks 2–10)

For context, nine additional TxGNN-predicted indications were reviewed in this pack. All were assessed as **Hold**, either due to a complete absence of supporting evidence (L5) or only weak, indirect preclinical/case-report evidence (L4):

| Rank | Predicted Indication | Score | Evidence Level | Note |
|------|----------------------|-------|-----------------|------|
| 2 | Classic Stiff Person Syndrome | 99.45% | L5 | No mechanistic link; autoimmune disorder unrelated to known glucose-lowering action |
| 3 | Opsismodysplasia | 99.40% | L5 | Rare skeletal dysplasia, no mechanistic link |
| 4 | Thiamine-Responsive Dysfunction Syndrome | 99.40% | L5 | Metformin is known to *interfere* with B12/thiamine metabolism — a potential risk signal, not a therapeutic rationale |
| 5 | Drug-Induced Localized Lipodystrophy | 99.06% | L5 | No supporting evidence |
| 6 | Centrifugal Lipodystrophy | 98.99% | L5 | No supporting evidence |
| 7 | Pressure-Induced Localized Lipoatrophy | 98.96% | L5 | No supporting evidence |
| 8 | Pancreatic Agenesis | 98.91% | L4 | 20 papers reviewed; only 1 indirect case report (Alström syndrome), not disease-specific |
| 9 | Idiopathic Localized Lipodystrophy | 98.90% | L5 | No supporting evidence |
| 10 | Homozygous Familial Hypercholesterolemia | 92.30% | L4 | Only 2 papers; 1988 in-vitro fibroblast study showing indirect cholesterol-lowering effect, not clinically validated |

None of these candidates currently meet a threshold for further development.

---

## Safety Considerations

Please refer to the SmPC for safety information. **Note:** TFDA label warnings/contraindications (DG001) are flagged as a **Blocking** data gap in this Evidence Pack — safety evaluation (S1 stage) cannot proceed until this data is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications in this Evidence Pack are supported only by the TxGNN model score (L5) or minimal indirect preclinical/case-report evidence (L4), with no clinical trials confirming human efficacy for any of them. Additionally, a **Blocking** data gap (missing TFDA warnings/contraindications) prevents even a preliminary safety assessment.

**To proceed, the following is needed:**
- TFDA label PDF (warnings, contraindications) — resolves Blocking gap DG001
- DrugBank MOA data — resolves High-severity gap DG002
- Targeted literature/mechanistic search specifically on Focal Stiff Limb Syndrome and Metformin (none currently exists)
- If pursuing rank 8 (Pancreatic Agenesis) or rank 10 (HoFH), dedicated mechanistic studies to confirm the preliminary preclinical signals before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

