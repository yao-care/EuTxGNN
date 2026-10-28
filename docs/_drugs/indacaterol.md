---
layout: default
title: Indacaterol
parent: AI Predictions (L5)
nav_order: 319
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Indacaterol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Maintenance bronchodilator treatment of airflow obstruction in adults…"
monitor_inn: "Indacaterol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "trigeminal autonomic cephalalgia", "paratenonitis", "calcific tendinitis", "hypertrichosis (disease)", "bronchial disease", "myositis", "anaphylaxis", "Ambras type hypertrichosis universalis congenita"]
---

# Indacaterol
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

## Indacaterol: From Chronic Obstructive Pulmonary Disease to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Indacaterol is an ultra-long-acting inhaled beta2-agonist, originally authorized in the EU as a maintenance bronchodilator for adults with chronic obstructive pulmonary disease (COPD).
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **no clinical trials and no publications** currently support this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Maintenance bronchodilator treatment of airflow obstruction in adults with COPD |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | Marketed (valid licences: 3 of 3) |
| Number of Authorizations | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Indacaterol is a long-acting beta2-adrenergic agonist. Its efficacy in COPD comes from relaxing airway smooth muscle through cAMP signalling.

The link to NSIAD is weak. A beta2-agonist could theoretically modulate renal water handling through cAMP and vasopressin V2 receptor signalling. However, NSIAD is caused by activating mutations of the V2 receptor (AVPR2), the primary defect. A beta2-agonist is therefore unlikely to correct it. The high score (0.9954) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so the prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001211 | Hirobriz Breezhaler | — | Maintenance bronchodilator treatment of airflow obstruction in adults with COPD (valid) |
| EMEA/H/C/001114 | Onbrez Breezhaler | — | Maintenance bronchodilator treatment of airflow obstruction in adults with COPD (valid) |
| EMEA/H/C/001210 | Oslif Breezhaler | — | Maintenance bronchodilator treatment of airflow obstruction in adults with COPD (valid) |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (drug-disease contraindication links from the TxGNN knowledge graph, not label text): hypertension, long QT syndrome (including familial), sudden cardiac arrest, heart conduction disease, coronary artery disease, epilepsy, diabetes mellitus, hyperglycemia, diabetic ketoacidosis, potassium deficiency, and thyrotoxicosis/hyperthyroidism/Graves disease.
- **Drug Interactions**: 100 interactions were identified. Those shown below are examples.
  - **Moderate:**
    - Antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, saxagliptin, albiglutide, canagliflozin, dapagliflozin, chlorpropamide)
    - Epinephrine
    - Isometheptene
    - Famotidine
    - Clarithromycin
  - **Minor:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, beclomethasone, triamcinolone) and aprepitant.

For warnings and contraindications from the product label, please refer to the SmPC.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone. There are no trials or publications, and the proposed mechanism is implausible given that NSIAD is driven by a V2 receptor defect. The drug is marketed in this country, with 3 valid licences of 3.

Among the other top-10 predictions, only **bronchial disease** (rank 7) has substantive supporting evidence, mainly published asthma Phase 3 data on indacaterol-containing combinations. That is largely an extension of the approved COPD use rather than a novel repurposing. If pursued, it would need to be as a fixed-dose combination with an inhaled corticosteroid, because LABA monotherapy is contraindicated in asthma.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence linking beta2-agonism to NSIAD pathophysiology
- Mechanism of action data and warnings/contraindications from the SmPC
- Verification of current regulatory and availability status, given that the drug is marketed in this country with 3 valid licences of 3
- A cardiovascular, metabolic and electrolyte (potassium) safety assessment for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

