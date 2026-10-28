---
layout: default
title: Mannitol
parent: AI Predictions (L5)
nav_order: 386
evidence_level: L5
indication_count: 9
monitor_inn: "Mannitol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "nephrogenic diabetes insipidus", "central core myopathy"]
last_modified_at: 2026-10-28
description: "Mannitol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Cystic fibrosis (CF) in adults aged 18 years and above…"
---

# Mannitol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Mannitol: From Cystic Fibrosis to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Mannitol (marketed in the EU as the inhaled product Bronchitol) is originally used as add-on therapy for cystic fibrosis in adults.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis**, but there are **0 clinical trials** and only **1 general review** in the data compiled for this report, and that review does not study this disease directly. This is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis (CF) in adults aged 18 years and above, as add-on therapy to best standard of care |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Mannitol is an osmotic agent. In theory, an osmotic agent could promote water excretion through osmotic diuresis, which is the only mechanistic link to this condition.

Nephrogenic syndrome of inappropriate antidiuresis is a gain-of-function disorder of the vasopressin V2 receptor that causes hyponatremia. The only retrieved paper is a general review of pitfalls in evaluating hyponatremia. It does not support the use of mannitol in this disorder. Osmotic diuresis could also worsen sodium balance. The original indication (inhaled mannitol for cystic fibrosis) has a different mechanism and route from this prediction, so the high score should be treated as a model output rather than supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | General review of common pitfalls in evaluating hyponatremia; does not address mannitol use in this disorder |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001252 | Bronchitol | Not specified | Treatment of cystic fibrosis (CF) in adults aged 18 years and above as an add-on therapy to best standard of care. |

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The TxGNN knowledge graph records contraindication relations between mannitol and conditions including liver failure, hepatic encephalopathy, anuria, impaired renal function, pulmonary edema, intracranial hemorrhage, thrombocytopenia, neutropenia, anemia, porphyria and sleep apnea syndromes. These come from the graph and have not been checked against the product label.
- **Drug Interactions:** 100 interactions were found in total. Examples include a Major interaction with amikacin, and Moderate interactions with formoterol, salbutamol, arformoterol, carbamazepine, citalopram, captopril, benazepril, dapagliflozin, canagliflozin and bisacodyl.
- **Prediction-specific concern:** Osmotic diuresis may worsen sodium balance in a patient with hyponatremia.

Please refer to the SmPC for the full label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no study that directly addresses nephrogenic syndrome of inappropriate antidiuresis. The only literature is a general hyponatremia review, so the evidence level is L5. The proposed mechanism is also questionable, since osmotic diuresis could worsen sodium balance.

**To proceed, the following is needed:**
- Mechanism of action data for mannitol
- Label warnings and contraindications from the EMA product information (SmPC)
- Preclinical or case-level evidence that mannitol has a benefit in this V2 receptor gain-of-function disorder
- A safety assessment of osmotic diuresis and sodium balance in hyponatremic patients
- Assessment of route compatibility, since the licensed product is an inhaled formulation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

