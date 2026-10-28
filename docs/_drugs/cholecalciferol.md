---
layout: default
title: Cholecalciferol
parent: AI Predictions (L5)
nav_order: 146
evidence_level: L5
indication_count: 4
monitor_inn: "cholecalciferol"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "renal osteodystrophy", "renal tubular acidosis"]
last_modified_at: 2026-10-28
description: "Cholecalciferol: predicted new indication Acromesomelic dysplasia, Campailla Martinelli type (evidence level L5). Approved use: Treatment of postmenopausal osteoporosis in patients at risk of vitam…"
---

# Cholecalciferol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Cholecalciferol: From Postmenopausal Osteoporosis to Acromesomelic Dysplasia, Campailla Martinelli Type
{: .text-alpha }

## One-Sentence Summary

Cholecalciferol (vitamin D3) is authorised in the EU as a component of fixed-dose products for postmenopausal osteoporosis in patients at risk of vitamin D insufficiency.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Campailla Martinelli type**, a rare genetic skeletal disorder.
**No clinical trials and no publications** currently support this prediction, which rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of postmenopausal osteoporosis in patients at risk of vitamin D insufficiency (reduces the risk of vertebral and hip fractures) |
| Predicted New Indication | Acromesomelic dysplasia, Campailla Martinelli type |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 3 of 3) |
| Number of Authorizations | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for cholecalciferol is not available in the data compiled for this report. Cholecalciferol is a vitamin D precursor, and its role in calcium and bone mineral balance is well established. Its efficacy in postmenopausal osteoporosis, where it is used with alendronate in the EU products below, does not extend by itself to a genetic skeletal dysplasia.

The link to the new indication is weak. Acromesomelic dysplasia is a rare inherited skeletal disorder, most likely tied to the NPR2 / C-type natriuretic peptide (CNP) signalling pathway. Cholecalciferol has no established mechanism that would correct this defect. Any connection through general bone mineral metabolism is speculative. The high score (0.9978) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It has not been checked against laboratory, clinical or published evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

All three authorisations are centralised EU products that, judging by their names and indication wording, combine cholecalciferol with alendronate. They show how cholecalciferol is used within these combinations, not how it is approved as a single ingredient.

| Authorization Number | Product Name | Approved Indication |
|---------|------|-----------|
| EMEA/H/C/000759 | Adrovance | Treatment of postmenopausal osteoporosis in patients at risk of vitamin-D insufficiency. Reduces the risk of vertebral and hip fractures. |
| EMEA/H/C/000619 | Fosavance | Treatment of postmenopausal osteoporosis in patients at risk of vitamin-D insufficiency. Reduces the risk of vertebral and hip fractures. |
| EMEA/H/C/001180 | Vantavo (previously Alendronate sodium and colecalciferol, MSD) | Treatment of postmenopausal osteoporosis in patients at risk of vitamin-D insufficiency, including those not receiving vitamin-D supplementation. Reduces the risk of vertebral and hip fractures. |

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The TxGNN knowledge graph records contraindication relations between cholecalciferol and the conditions below. These come from the graph, not from product labelling, and need verification against the SmPC.
  - Cardiovascular and metabolic: hypertension, atrial fibrillation, diabetes mellitus, diabetic ketoacidosis, hyperlipidemia, familial hyperlipidemia.
  - Kidney, liver and gastrointestinal: kidney disease, pyoureter, liver disease, gallbladder disease, gastritis.
  - Calcium, phosphate and parathyroid: hyperparathyroidism, osteitis fibrosa, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, sarcoidosis.
  - Blood and iron: blood coagulation disease, sickle cell anemia, hereditary persistence of fetal hemoglobin, hereditary hemochromatosis, hemosiderosis, iron metabolism disease.
  - Other: primary hyperoxaluria, Wilson disease, female breast carcinoma, prostate cancer (including prostate neoplasm and carcinoma).
- **Drug Interactions:** 56 interactions are recorded in total.
  - **Major:** other vitamin D analogues and metabolites (calcifediol, calcitriol, dihydrotachysterol, doxercalciferol), mainly the risk of additive hypercalcaemia.
  - **Moderate:**
    - Thiazide diuretics (bendroflumethiazide, benzthiazide, chlorothiazide, chlorthalidone)
    - Barbiturates (amobarbital, butabarbital, butalbital)
    - Carbamazepine
    - Bile acid sequestrants (cholestyramine, colesevelam, colestipol)
    - Cardiac glycosides (digoxin, digitoxin)
    - Topical vitamin D analogues (calcipotriol, calcitriol)
  - **Minor:** cimetidine.

Please refer to the SmPC for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score, with no trials or publications on this disease and no plausible mechanism by which vitamin D3 would alter the underlying pathology. Evidence level is L5, so there is no basis to advance.

**To proceed, the following is needed:**
- Any preclinical, mechanistic or clinical evidence that directly links cholecalciferol to acromesomelic dysplasia (Campailla Martinelli type).
- Mechanism of action data for cholecalciferol and an analysis of its relationship to the CNP/NPR2 signalling pathway.
- Label-based warnings and contraindications from the SmPC, so safety can be screened.
- Consideration of other predictions in the data compiled for this report. For example, the prediction for renal osteodystrophy is supported by a Phase 3 trial and a body of CKD-related literature, and may be a better candidate to prioritise.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

