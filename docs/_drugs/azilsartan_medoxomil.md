---
layout: default
title: Azilsartan Medoxomil
parent: AI Predictions (L5)
nav_order: 79
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Azilsartan Medoxomil: predicted new indication Pulmonary hypertension with unclear multifactorial mechanism (evidence level L5). Approved use: Essential hypertension in adults"
monitor_inn: "Azilsartan medoxomil"
predicted_indications: ["pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "malignant renovascular hypertension", "Braddock syndrome", "cerebrovascular disorder", "obsolete susceptibility to ischemic stroke", "chronic pulmonary heart disease", "brain stem infarction", "hypotrichosis simplex of the scalp"]
---

# Azilsartan Medoxomil
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

# Azilsartan medoxomil: From Essential Hypertension to Pulmonary Hypertension

## One-Sentence Summary

Azilsartan medoxomil is an angiotensin II receptor blocker, originally used to treat essential hypertension in adults.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism**,
but **no clinical trials and no publications** currently support this prediction, so it remains a computational hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Essential hypertension in adults |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 97.78% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, azilsartan medoxomil is an angiotensin II type 1 (AT1) receptor blocker (ARB). It lowers systemic blood pressure, and its efficacy in essential hypertension is the basis of its approval.

A plausible link to pulmonary hypertension is that the renin-angiotensin system may contribute to pulmonary vascular remodeling and hypoxic vasoconstriction, so AT1 blockade is mechanistically conceivable. However, ARBs have not established efficacy in pulmonary arterial hypertension. The prediction rests only on a knowledge-graph score, with no supporting trials or literature.

Other predicted indications fall into three groups:

| Group | Predicted Indications (score) | Assessment |
|------|------|------|
| Pulmonary vascular and heart disease | Pulmonary hypertension owing to lung disease and/or hypoxia (97.78%); chronic pulmonary heart disease (91.79%) | Depends on the unproven pulmonary hypertension link. Systemic vasodilators may worsen ventilation-perfusion matching. |
| Hypertension-related renal disease | Malignant hypertensive renal disease (97.69%); malignant renovascular hypertension (97.69%) | Close to the approved indication, but this likely reflects proximity to the existing indication rather than independent evidence. Malignant hypertension is an emergency usually treated with parenteral agents. ARBs carry a risk of acute renal function decline in bilateral renal artery stenosis or solitary kidney. |
| Cerebrovascular | Cerebrovascular disorder (94.56%); obsolete susceptibility to ischemic stroke (92.74%); brain stem infarction (87.67%) | Any benefit would be indirect, through blood pressure lowering. Lowering blood pressure in acute ischemic stroke may reduce cerebral perfusion and be harmful. The "obsolete" term is a weak target. |
| Unlikely or artifact | Braddock syndrome (97.22%); hypotrichosis simplex of the scalp (85.01%) | No credible mechanistic link; likely knowledge-graph artifacts. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002293 (cancelled) | Edarbi | Not specified | Edarbi is indicated for the treatment of essential hypertension in adults. |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease contraindication edges, not label text): hypotensive disorder, renal artery obstruction, impaired renal function disease.
- **Drug Interactions**: 85 interactions were identified, all of those listed being of Moderate severity. Main examples:
  - Corticosteroids: hydrocortisone, triamcinolone, betamethasone, budesonide, dexamethasone
  - Antidiabetic agents: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, exenatide, and several insulins (human, aspart, degludec, detemir, glargine)
  - Others: bupropion, morphine, acetylsalicylic acid, dronabinol
- Concerns specific to the predicted indications: possible worsening of gas exchange in lung-disease-associated pulmonary hypertension, acute renal function decline in renovascular disease, and reduced cerebral perfusion if blood pressure is lowered in acute stroke.

Please refer to the SmPC for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN score, with no clinical trials or publications (Evidence Level L5). ARBs have not established efficacy in pulmonary hypertension, and the EU authorization is cancelled. The several predicted indications that rank close to hypertension show high scores mainly because of their similarity to the approved indication, not because of independent evidence.

**To proceed, the following is needed:**
- A systematic literature and trial registry search for azilsartan or other ARBs in pulmonary hypertension
- Mechanism of action data to support the mechanistic-link analysis
- Safety information from the SmPC (warnings and contraindications), which is required before any safety screening
- Clarification of why the EU authorization was cancelled, and of the current regulatory pathway
- Preclinical evidence (for example, pulmonary hypertension models) to move beyond model-only prediction
- If any indication is pursued, consider the better-grounded candidates (such as hypertension-related renal disease or stroke prevention) under current disease terms, rather than the obsolete or artifact entries
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

