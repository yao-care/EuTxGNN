---
layout: default
title: Mannitol
parent: AI Predictions (L5)
nav_order: 386
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mannitol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Cystic fibrosis (CF) in adults aged 18 years and above…"
---

# Mannitol
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

# Mannitol: From Cystic Fibrosis to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is an osmotic agent, authorised in the EU as Bronchitol (inhaled) for adults with cystic fibrosis as an add-on to standard care.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis**, but there are **0 clinical trials** and only **1 general review article**, and the review does not support mannitol use for this condition.
This is a model-only prediction with a Hold recommendation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis (CF) in adults aged 18 years and above, as an add-on therapy to best standard of care |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mannitol is an osmotic diuretic. Its efficacy in cystic fibrosis (as an inhaled product) has been established, and in theory its osmotic action could promote water excretion and affect serum sodium.

However, nephrogenic SIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2). An osmotic agent does not act on this defect. The only linked paper is a general review of pitfalls in evaluating hyponatraemia, and it does not support using mannitol here. The high TxGNN score reflects a network-based prediction only and should not be read as evidence of benefit.

Other top-ranked predictions show the same pattern. Examples are malignant hyperthermia and related RYR1 myopathies, hypokalaemic periodic paralysis, and King-Denborough syndrome. They have no plausible mechanism for mannitol and rest on network proximity or indirect literature. For nephrogenic diabetes insipidus, mannitol's osmotic diuresis would be expected to worsen polyuria, so that direction is potentially harmful.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | Describes common pitfalls in the evaluation of hyponatraemia. It is a general review and does not address mannitol treatment of nephrogenic SIAD. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001252 (cancelled) | Bronchitol | Not specified | Bronchitol is indicated for the treatment of cystic fibrosis (CF) in adults aged 18 years and above as an add-on therapy to best standard of care. |

## Safety Considerations

- **Disease contraindication signals (knowledge graph, not label text)**: The TxGNN knowledge graph links mannitol to contraindication with several conditions. They include liver failure and liver disease, hepatic coma and encephalopathy, anuria, impaired renal function, pulmonary oedema, intracranial haemorrhage, thrombocytopenia, neutropenia, agranulocytosis, anaemia, porphyria, sleep apnoea syndromes, anxiety and dysthymic disorders, and substance-related disorders. These come from a knowledge graph and should be checked against the product label.
- **Drug Interactions**: The interaction query returned 100 records. Most listed ones are Moderate. One Major interaction is listed with **amikacin**. Moderate interactions include formoterol, salbutamol, arformoterol, ACE inhibitors (benazepril, captopril), SGLT2 inhibitors (canagliflozin, dapagliflozin), carbamazepine, citalopram, desvenlafaxine, bisacodyl and contrast agents (iothalamic acid, diatrizoate). Doxycycline is Minor.
- **Indication-specific cautions from the literature**: A 1976 case report describes pulmonary oedema during treatment of water intoxication with hypertonic saline and mannitol. This raises a concern about volume shifts and cardiac strain. Mannitol-based or dextrose-containing infusions have also been noted to risk worsening attacks in periodic paralysis.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials and no supporting literature, and the proposed mechanism is implausible because nephrogenic SIAD is a receptor-level defect that an osmotic agent does not address. The EU authorisation is also cancelled, and label warnings and contraindications were not available for this review.

**To proceed, the following is needed:**
- Mechanistic evidence that an osmotic agent can influence the AVPR2 gain-of-function phenotype, or an alternative rationale
- Mechanism of action data from DrugBank
- EU label (SmPC) warnings and contraindications, which are required for any safety screening
- Preclinical or clinical data in nephrogenic SIAD, none of which currently exists
- Review of other candidate indications. Several of them (such as hypokalaemic periodic paralysis and nephrogenic diabetes insipidus) carry potential harm. Acute pulmonary heart disease has only indirect evidence and a pulmonary oedema safety signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

