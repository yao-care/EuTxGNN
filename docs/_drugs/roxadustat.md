---
layout: default
title: Roxadustat
parent: AI Predictions (L5)
nav_order: 539
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Roxadustat: predicted new indication Dry eye syndrome (evidence level L5). Approved use: Treatment of adult patients with symptomatic anaemia associated with…"
monitor_inn: "Roxadustat"
predicted_indications: ["dry eye syndrome", "bone Paget disease", "dentinogenesis imperfecta", "squamous cell carcinoma", "dental pulp calcification", "dentin dysplasia", "Sjogren syndrome", "adenosquamous breast carcinoma", "acantholytic variant squamous cell breast carcinoma", "metaplastic breast carcinoma"]
---

# Roxadustat
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

## Roxadustat: From Anaemia of Chronic Kidney Disease to Dry Eye Syndrome
{: .text-alpha }

## One-Sentence Summary

Roxadustat was originally used to treat symptomatic anaemia associated with chronic kidney disease (CKD).
The TxGNN model predicts it may be effective for **dry eye syndrome**,
but **no clinical trials and no publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of adult patients with symptomatic anaemia associated with chronic kidney disease (CKD) |
| Predicted New Indication | Dry eye syndrome |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Roxadustat is a hypoxia-inducible factor prolyl hydroxylase (HIF-PH) inhibitor. By blocking these enzymes, it stabilizes HIF-1α and HIF-2α and raises erythropoietin levels, which is how it treats anaemia in CKD. The compiled data list EGLN2 as one of its pharmacological targets. Detailed mechanism of action data from DrugBank are not currently available.

The link between CKD anaemia and dry eye is indirect. HIF activation could plausibly influence corneal epithelial repair, angiogenesis and inflammatory signaling at the ocular surface. However, the direction of the effect is uncertain, because HIF-1α is also linked to ocular surface inflammation. The prediction comes from the TxGNN model alone and has no supporting clinical or literature data.

The second-ranked prediction, Sjogren syndrome, is related to dry eye through sicca symptoms, but it also has no supporting evidence. Other top predictions include bone Paget disease, dental disorders (dentinogenesis imperfecta, dental pulp calcification, dentin dysplasia) and several squamous and breast carcinoma subtypes. For the cancers, HIF stabilization could theoretically promote tumor progression, so they raise a safety concern rather than a therapeutic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004871 (status: cancelled) | Evrenzo | Not specified | Treatment of adult patients with symptomatic anaemia associated with chronic kidney disease (CKD). |

## Safety Considerations

- **Drug Interactions**: One pharmacological entry was found, in which roxadustat acts on its target, egl-9 family hypoxia inducible factor 2 (EGLN2). This is its mechanism of action rather than a clinical drug-drug interaction. No interaction severity level is available.
- **Theoretical concern**: HIF stabilization may promote tumor progression, angiogenesis and therapy resistance. This matters especially for the cancer-related predictions, and it could also affect bone turnover.

For warnings and contraindications, please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The dry eye prediction is supported only by the TxGNN model, with no clinical trials or publications (Evidence Level L5). The effect direction is uncertain, and the only EU authorization has been cancelled.

**To proceed, the following is needed:**
- Preclinical evidence (for example, ocular surface or corneal epithelial models) showing a beneficial effect of HIF-PH inhibition on dry eye
- A literature review of HIF-1α/2α roles in ocular surface inflammation
- Detailed mechanism of action data and the SmPC warnings and contraindications
- Assessment of the route of administration, since a topical ocular formulation may be needed rather than the oral systemic form
- A safety assessment of long-term HIF stabilization, particularly regarding tumor promotion
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

