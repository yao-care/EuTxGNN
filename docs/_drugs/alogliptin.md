---
layout: default
title: Alogliptin
parent: AI Predictions (L5)
nav_order: 39
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Alogliptin: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus in adults aged 18 years and older…"
monitor_inn: "Alogliptin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "autoimmune oophoritis"]
---

# Alogliptin
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

# Alogliptin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Alogliptin is a DPP-4 inhibitor originally used to improve glycaemic control in adults with type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**,
but **no clinical trials** and **no publications** currently support this direction, so the prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus in adults aged 18 years and older, to improve glycaemic control in combination with other glucose-lowering medicinal products including insulin |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 98.01% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no valid authorisation) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, alogliptin is a dipeptidyl peptidase-4 (DPP-4) inhibitor. Its efficacy in type 2 diabetes has been established, and mechanistically it may have some relevance to stiff person syndrome.

Stiff person syndrome is an autoimmune neurological disorder, typically associated with anti-GAD65 antibodies, and it frequently co-occurs with type 2 diabetes. This shared autoimmune and metabolic background is the most plausible link. DPP-4 (CD26) also has reported immunomodulatory effects, which could in theory matter in an autoimmune condition.

However, no direct mechanism for relieving stiffness, spasms or the GABAergic dysfunction of the disease has been established. The high score is a computational prediction, likely reflecting network similarity, and should be read with caution. Focal stiff limb syndrome (rank 2, same score) is a localised variant of the same spectrum and shares the same speculative rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

For context, the lower-ranked candidate pancreatic agenesis (score 96.5%) had three indirect papers (a 2010 review of pioglitazone plus alogliptin, a 2011 tolerability review of DPP-4 inhibitors, and a 2011 mouse study of beta-cell function). None of them address pancreatic agenesis itself, and DPP-4 inhibition is unlikely to work without functioning beta cells.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002182 (cancelled) | Vipidia | Not specified | Vipidia is indicated in adults aged 18 years and older with type 2 diabetes mellitus to improve glycaemic control in comb... |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 potential interactions. Most of the 20 listed are of Moderate severity and a few are Minor. Examples include:
  - Sympathomimetics and bronchodilators: phenylephrine, pseudoephedrine, epinephrine, formoterol, salbutamol
  - Diuretics: furosemide, hydrochlorothiazide, acetazolamide
  - Corticosteroids: hydrocortisone (Moderate), topical hydrocortisone and alclometasone (Minor)
  - Other glucose-lowering agents: acetohexamide
  - Others: ethinylestradiol, ethanol, fosinopril, fosphenytoin, fosamprenavir, gemifloxacin, alpelisib, aloe vera leaf

  Many of these can affect blood glucose, which matters for people on a glucose-lowering drug.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5), with no registered trials or publications. The EU authorisation for the only product is cancelled, and the mechanistic link to stiff person syndrome is speculative. The other nine candidates, mostly lipodystrophies and rare genetic syndromes, are also at L5 (pancreatic agenesis at L4 with only indirect evidence), so none is ready to advance.

**To proceed, the following is needed:**
- Mechanism of action data for alogliptin from DrugBank
- Warnings and contraindications from the SmPC (the EMA product information has not yet been obtained, which blocks safety screening)
- A literature search for DPP-4 inhibitors or CD26 modulation in stiff person syndrome and related autoimmune neurological disorders
- Preclinical or case-based evidence of benefit before any trial is considered
- Clarification of the regulatory situation, since the only EU authorisation is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

