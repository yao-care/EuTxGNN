---
layout: default
title: Cholecalciferol
parent: AI Predictions (L5)
nav_order: 146
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Cholecalciferol: predicted new indication Familial isolated hypoparathyroidism due to impaired PTH secretion (evidence level L5). Approved use: Treatment of postmenopausal osteoporosis in patients at…"
monitor_inn: "cholecalciferol"
predicted_indications: ["familial isolated hypoparathyroidism due to impaired PTH secretion", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hypophosphatemic rickets", "renal osteodystrophy", "renal tubular acidosis"]
---

# Cholecalciferol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Cholecalciferol: From Postmenopausal Osteoporosis to Familial Isolated Hypoparathyroidism Due to Impaired PTH Secretion

## One-Sentence Summary

Cholecalciferol (vitamin D3) was originally authorized in the EU as a component of combination products for postmenopausal osteoporosis in patients at risk of vitamin D insufficiency.
The TxGNN model predicts it may be useful for **familial isolated hypoparathyroidism due to impaired PTH secretion**, but **0 clinical trials** and **0 publications** currently support this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of postmenopausal osteoporosis in patients at risk of vitamin D insufficiency (reduces the risk of vertebral and hip fractures) |
| Predicted New Indication | Familial isolated hypoparathyroidism due to impaired PTH secretion |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| EU Market Status | ✗ Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 3 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Cholecalciferol is a vitamin D prohormone. In the EU it was authorized only as a component of combination products, and its role in osteoporosis is to correct vitamin D insufficiency so that calcium and bone metabolism can work properly.

In hypoparathyroidism, parathyroid hormone (PTH) is deficient. This reduces 1-alpha-hydroxylation of vitamin D in the kidney, so less active vitamin D is produced. In principle, vitamin D3 could therefore serve as an adjunct. However, cholecalciferol is itself inactive and must be converted to its active form. Active analogs such as calcitriol and alfacalcidol are the usual therapy in this condition. The high TxGNN score reflects a connection within the model's knowledge graph (vitamin D, calcium and bone metabolism). It is not backed by any trial or publication specific to this disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

All three authorizations are for alendronate and cholecalciferol combination products and have been cancelled.

| Authorization Number | Product Name | Approved Indication |
|---------|------|-----------|
| EMEA/H/C/000759 | Adrovance | Treatment of postmenopausal osteoporosis in patients at risk of vitamin-D insufficiency. Adrovance reduces the risk of vertebral and hip fractures. |
| EMEA/H/C/000619 | Fosavance | Treatment of postmenopausal osteoporosis in patients at risk of vitamin-D insufficiency. Fosavance reduces the risk of vertebral and hip fractures. |
| EMEA/H/C/001180 | Vantavo (previously Alendronate sodium and colecalciferol, MSD) | Treatment of postmenopausal osteoporosis in patients at risk of vitamin-D insufficiency, including those not receiving vitamin-D supplementation. Vantavo reduces the risk of vertebral and hip fractures. |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease edges in the TxGNN knowledge graph, not product label text): hypercalcemia, hyperparathyroidism, nephrocalcinosis, kidney disease, liver disease, sarcoidosis, phosphorus metabolism disease, hypertension, diabetes mellitus, atrial fibrillation, and others. Several of these (hypercalcemia, nephrocalcinosis, calcium and phosphate disorders) are directly relevant to a calcium-handling disorder such as hypoparathyroidism.
- **Drug Interactions** (56 interactions recorded; the 20 listed in the data include):
  - **Major:** other vitamin D agents (calcifediol, calcitriol, dihydrotachysterol, doxercalciferol), which add to the risk of excess vitamin D effect.
  - **Moderate:** thiazide diuretics (bendroflumethiazide, benzthiazide, chlorothiazide, chlorthalidone), barbiturates (amobarbital, butabarbital, butalbital), carbamazepine, bile acid sequestrants (cholestyramine, colesevelam, colestipol), digoxin and digitoxin, and topical vitamin D analogs.
  - **Minor:** cimetidine.

Please refer to the SmPC for label warnings, as no label warning data were available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model scoring alone, with no clinical trials or publications for this disease. Active vitamin D analogs, not cholecalciferol, are the usual therapy for hypoparathyroidism, and all EU authorizations containing cholecalciferol have been cancelled.

**To proceed, the following is needed:**
- Disease-specific literature or trial evidence showing a role for cholecalciferol in PTH-deficient hypoparathyroidism, beyond correcting vitamin D deficiency
- Mechanism of action data and EU label warnings and contraindications
- A safety plan for calcium, phosphate and PTH monitoring, and for hypercalcemia risk
- Consideration of other predictions for this drug that have stronger support. **Renal osteodystrophy** (TxGNN score 99.11%) reaches Evidence Level L1 (one Phase 3 randomized trial, NCT00752401, in vitamin D-deficient kidney transplant recipients, plus a completed trial in secondary hyperparathyroidism). However, that trial's status is unknown and no results were available, so this grade reflects trial design rather than confirmed outcomes. It is assessed as "Proceed with Guardrails" and is the more promising direction for further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

