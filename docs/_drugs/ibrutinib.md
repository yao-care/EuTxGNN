---
layout: default
title: Ibrutinib
parent: AI Predictions (L5)
nav_order: 304
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ibrutinib: predicted new indication Polyclonal hypergammaglobulinemia (evidence level L5). Approved use: Mantle cell lymphoma (MCL)…"
monitor_inn: "Ibrutinib"
predicted_indications: ["polyclonal hypergammaglobulinemia", "monoclonal paraproteinemia disease", "thyroid gland mucosa-associated lymphoid tissue lymphoma", "small intestinal mucosa-associated lymphoid tissue lymphoma", "small intestinal Burkitt lymphoma", "breast mucosa-associated lymphoid tissue lymphoma", "tonsillar lymphoma", "marginal zone lymphoma", "extracutaneous mastocytoma"]
---

# Ibrutinib
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

# Ibrutinib: From Mantle Cell Lymphoma, Chronic Lymphocytic Leukaemia and Waldenström's Macroglobulinaemia to Polyclonal Hypergammaglobulinemia

## One-Sentence Summary

Ibrutinib is a targeted anticancer drug originally used for B-cell blood cancers: mantle cell lymphoma, chronic lymphocytic leukaemia and Waldenström's macroglobulinaemia.
The TxGNN model predicts it may be effective for **polyclonal hypergammaglobulinemia** with a high score, but **no clinical trials and no publications** currently support this specific prediction, so it rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mantle cell lymphoma (MCL), chronic lymphocytic leukaemia (CLL) and Waldenström's macroglobulinaemia (WM) |
| Predicted New Indication | Polyclonal hypergammaglobulinemia |
| TxGNN Prediction Score | 91.75% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ibrutinib is a Bruton's tyrosine kinase (BTK) inhibitor. Its efficacy in B-cell malignancies has been established, and mechanistically it may be applicable to polyclonal hypergammaglobulinemia.

BTK is a central signalling enzyme in B cells, and B cells are the source of immunoglobulins. Blocking BTK could in principle dampen B-cell activation and reduce immunoglobulin production. Polyclonal hypergammaglobulinemia is a state of excess immunoglobulin from many B-cell clones. This gives a plausible biological link to ibrutinib's original use in B-cell diseases, including Waldenström's macroglobulinaemia, which involves excess IgM.

This link is a theoretical inference only. No study in the compiled data tests ibrutinib in this condition, so the high score should be read as a hypothesis, not as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Status | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003791 | Imbruvica | Cancelled | Previously untreated MCL eligible for ASCT (with R-CHOP/R-DHAP), relapsed or refractory MCL, CLL (untreated and previously treated), W... |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BTK inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 recorded interactions. The first 20 returned include the following.
  - **Major**: aprepitant, acetylsalicylic acid, clarithromycin, cobicistat and deferasirox.
  - **Moderate**: loperamide, dexamethasone, cimetidine, miconazole, clotrimazole, rifaximin, fidaxomicin, and the DPP-4 inhibitors saxagliptin, linagliptin and sitagliptin.
  - **Minor**: prucalopride.
  - Many of these are likely linked to ibrutinib's metabolism, but the compiled data do not state the mechanisms. A full interaction review is needed before any use in a new population.

Warnings and contraindications from the EU label were not available. Please refer to the SmPC for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (91.75%), but it is the only support. There are no trials or publications for polyclonal hypergammaglobulinemia, the mechanism is only a plausible extrapolation, and the sole EU authorization is cancelled. This is not enough to justify moving forward.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and a clearer mechanistic case that BTK inhibition would act on polyclonal (non-malignant) immunoglobulin excess.
- Preclinical or early clinical studies in this condition, or at least a systematic literature review.
- EU label warnings and contraindications, which are currently missing and block safety screening.
- A safety assessment for a non-oncology population, including the large interaction burden.
- Clarification of the regulatory pathway, given the cancelled authorization.

**Note on other predictions:** The same data include better-supported predictions that merit separate evaluation. These are marginal zone lymphoma (Level L1, including the Phase 3 SELENE trial and Phase 2 trials such as MALIBU) and monoclonal paraproteinemia disease (Level L1, mostly overlapping the approved Waldenström's macroglobulinaemia indication). Both were assessed as "Proceed with Guardrails" in the underlying data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

