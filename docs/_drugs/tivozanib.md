---
layout: default
title: Tivozanib
parent: AI Predictions (L5)
nav_order: 622
evidence_level: L5
indication_count: 10
---

# Tivozanib
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

# Tivozanib: From Renal Cell Carcinoma to Endocervical Carcinoma

## One-Sentence Summary

Tivozanib is a VEGF receptor tyrosine kinase inhibitor originally used to treat advanced renal cell carcinoma (RCC).
The TxGNN model predicts it may be effective for **endocervical carcinoma**,
but currently **no clinical trials and no publications** support this direction. The prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | First-line treatment of adult patients with advanced renal cell carcinoma (RCC), and adult patients who are VEGFR and mTOR pathway inhibitor-naïve following disease progression after one prior cytokine therapy for advanced RCC |
| Predicted New Indication | Endocervical carcinoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Tivozanib inhibits all three VEGF receptor tyrosine kinases (VEGFR-1/FLT1, VEGFR-2/KDR and VEGFR-3/FLT4) with equal potency. This blocks VEGF-driven angiogenesis, which is the basis of its use in advanced renal cell carcinoma. Detailed mechanism of action data from the original drug record is not available; the description here comes from target pharmacology data.

Cervical cancers, including endocervical adenocarcinoma, depend in part on VEGF-driven angiogenesis. Anti-angiogenic therapy with bevacizumab has shown benefit in advanced cervical cancer. This gives a plausible but indirect rationale for VEGFR inhibition in this setting.

The very high TxGNN score (0.998) is a computational prediction only. Other highly ranked predictions are closely related rare gynaecological adenocarcinoma subtypes (for example uterine ligament, cervical mucinous and glassy cell variants). This suggests the score may partly reflect ontology proximity between related cervical and uterine cancer terms rather than disease-specific biology.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004131 (status: cancelled) | Fotivda | Not specified | First-line treatment of adult patients with advanced renal cell carcinoma (RCC) and for adult patients who are VEGFR and mTOR pathway inhibitor-naïve following disease progression after one prior treatm... |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 7 records were retrieved. Four are drug-drug interactions and three are target-pharmacology entries (FLT1, KDR, FLT4), which describe binding targets rather than interactions.
  - **Major**: Phenobarbital and St. John's Wort. Both are enzyme inducers, so exposure to tivozanib may fall; avoid combining them or review the need carefully.
  - **Moderate**: Riociguat and medroxyprogesterone acetate.

Other safety information (warnings and contraindications) was not available; please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN score. There are no clinical trials or publications for endocervical carcinoma, and the mechanistic rationale (anti-angiogenesis) is indirect. In addition, the only EU marketing authorization for tivozanib is cancelled.

**To proceed, the following is needed:**
- A systematic search for clinical and preclinical evidence of tivozanib or other VEGFR inhibitors in cervical and endocervical carcinoma
- Preclinical data (cell line or xenograft models) showing VEGFR pathway dependence in endocervical carcinoma
- Detailed mechanism of action data and SmPC safety information (warnings and contraindications)
- Clarification of the reason for the cancelled EU authorization and the current regulatory status
- A review of whether the predicted indication differs meaningfully from related histologies in the list, since the top predictions are closely related rare gynaecological subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

