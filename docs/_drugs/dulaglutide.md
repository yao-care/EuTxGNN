---
layout: default
title: Dulaglutide
parent: AI Predictions (L5)
nav_order: 202
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Dulaglutide: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus (patients 10 years and above) with insuffici…"
monitor_inn: "Dulaglutide"
predicted_indications: ["opsismodysplasia", "focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "autoimmune oophoritis"]
---

# Dulaglutide
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

## Dulaglutide: From Type 2 Diabetes Mellitus to Opsismodysplasia
{: .text-alpha }

## One-Sentence Summary

Dulaglutide is a once-weekly GLP-1 receptor agonist (Trulicity), originally used to improve glycaemic control in type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia,
but **no clinical trials and no publications** currently support this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (patients 10 years and above) with insufficient control, as an adjunct to diet and exercise |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 97.05% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, dulaglutide belongs to the GLP-1 receptor agonist class. Its efficacy in type 2 diabetes is established, and it acts mainly by enhancing glucose-dependent insulin secretion.

Opsismodysplasia is a rare skeletal dysplasia caused by INPPL1 mutations (SHIP2 deficiency) that affects endochondral ossification. SHIP2 is a negative regulator of insulin/PI3K signalling, so a distant pathway-level connection to a diabetes drug is conceivable. However, this link is speculative, and there is no credible mechanistic reason to expect benefit for the skeletal pathology. The high score (0.97) should be read as a computational prediction only.

Other top-ranked predictions show the same pattern. These include focal stiff limb syndrome, classic stiff person syndrome, thiamine-responsive dysfunction syndrome, pancreatic agenesis and several localized lipodystrophies. They most likely reflect network proximity to diabetes or metabolic terms rather than genuine therapeutic rationale. Pancreatic agenesis is mechanistically implausible, because there are no beta cells to stimulate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002825 (cancelled) | Trulicity | Not specified | Treatment of patients 10 years and above with insufficiently controlled type 2 diabetes mellitus as an adjunct to diet and exercise, as monotherapy when metformin is considered inappropriate, or in addition to other diabetes medicines... |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 potential interactions; the first 20 are listed in the compiled data, mostly of Moderate level, with a few Minor ones. Examples of Moderate-level interactions:
  - Sympathomimetics and bronchodilators: phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol
  - Diuretics: furosemide, hydrochlorothiazide, acetazolamide
  - Hormones and corticosteroids: ethinylestradiol, estradiol, norethisterone, hydrocortisone
  - Others: ethanol, alpelisib, aripiprazole, fosphenytoin, fosamprenavir, gemifloxacin

  Minor-level examples are topical hydrocortisone and topical alclometasone.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based solely on a model score. There are no clinical trials or literature, and no credible mechanistic link to opsismodysplasia has been identified. The EU authorization is also listed as cancelled, so no currently valid EU product is recorded.

**To proceed, the following is needed:**
- Mechanism of action data for dulaglutide (for example from DrugBank)
- Warnings and contraindications from the SmPC
- Preclinical or mechanistic studies testing whether GLP-1 receptor signalling or SHIP2/PI3K pathway modulation affects skeletal development
- Clarification of the cancelled EU authorization status (for example, withdrawal versus a data-source issue)
- A review of the other predicted indications to see whether any has a stronger rationale, such as the diabetes component of thiamine-responsive dysfunction syndrome
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

