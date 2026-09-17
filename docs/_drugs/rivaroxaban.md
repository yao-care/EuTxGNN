---
layout: default
title: Rivaroxaban
parent: AI Predictions (L5)
nav_order: 514
evidence_level: L5
indication_count: 10
---

# Rivaroxaban
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

# Rivaroxaban: From Anticoagulation (Factor Xa Inhibition) to Rheumatoid Arthritis

## One-Sentence Summary

Rivaroxaban is an oral Factor Xa inhibitor used for anticoagulation in thromboembolic conditions. TxGNN predicts a possible link to **Rheumatoid Arthritis**, but this signal is currently supported only by the model itself (**L5**) — there are **0 clinical trials** and only **3 tangentially related publications**, none of which studied rivaroxaban as an RA treatment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not specified in the structured regulatory data provided; rivaroxaban is pharmacologically an oral anticoagulant (Factor Xa inhibitor) used for thromboembolic disorders |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on known pharmacology, rivaroxaban is a direct Factor Xa inhibitor — its efficacy in preventing and treating thromboembolic disease (e.g., DVT, PE, stroke prevention in atrial fibrillation) is well established, but it has no recognized anti-inflammatory or immunomodulatory activity that would explain a disease-modifying effect in rheumatoid arthritis.

The model-generated rationale for this candidate is explicitly skeptical: it notes that rivaroxaban's only established pharmacology is anticoagulation, and that the high TxGNN score more plausibly reflects a **comorbidity association** in the knowledge graph — RA patients carry an elevated risk of venous thromboembolism and are frequently co-prescribed anticoagulants — rather than a genuine treatment signal for RA itself.

Consistent with this, none of the three retrieved publications describe rivaroxaban being used to treat RA; they cover DVT/PE management, thrombin generation testing in autoimmune disease, and anticoagulant adherence in atrial fibrillation. This pattern (comorbid population overlap without a therapeutic study) is a common source of false-positive signals in knowledge-graph-based repurposing models and should be treated with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | General review of DVT/PE diagnosis and treatment; does not address RA |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Review | La Revue de médecine interne | Discusses thrombin generation assay for assessing hypercoagulability in autoimmune disease (e.g., antiphospholipid syndrome); not an RA treatment study |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PLoS ONE | Compares rivaroxaban vs. apixaban adherence in atrial fibrillation patients; unrelated to RA |

---

## EU Market Information

Rivaroxaban has no EU marketing authorizations recorded in this dataset (market status: Not Marketed, 0 licenses).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction sits at L5 (model prediction only) with no clinical trials and no literature directly studying rivaroxaban for RA. The available evidence itself suggests the signal likely reflects comorbidity confounding (RA patients' elevated thromboembolic risk) rather than a therapeutic mechanism.

**To proceed, the following is needed:**
- TFDA/EMA label warnings and contraindications (currently a blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action data for rivaroxaban (currently a data gap)
- A preclinical or mechanistic study establishing a plausible anti-inflammatory/immunomodulatory pathway, if one exists, before this candidate can move beyond S0
- Epidemiological analysis adjusting for comorbidity confounding to determine whether the TxGNN association reflects treatment effect or population overlap
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

