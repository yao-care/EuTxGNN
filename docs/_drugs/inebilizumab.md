---
layout: default
title: Inebilizumab
parent: AI Predictions (L5)
nav_order: 320
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Inebilizumab: predicted new indication Plasma cell myeloma (evidence level L5). Approved use: Monotherapy for adult patients with neuromyelitis optica spectrum dis…"
---

# Inebilizumab
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

# Inebilizumab: From Neuromyelitis Optica Spectrum Disorder to Plasma Cell Myeloma

## One-Sentence Summary

Inebilizumab is an anti-CD19 antibody that was originally authorized in the EU for anti-AQP4 antibody-positive neuromyelitis optica spectrum disorder (NMOSD). The TxGNN model's top-ranked prediction is **drug-induced osteoporosis**, which has no supporting evidence. This report instead focuses on **plasma cell myeloma** (rank 4), the only prediction with any direct clinical signal: **1 Phase 1 study** and **2 indirect reviews**, with no registered clinical trials in the data compiled for this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Monotherapy for adult patients with neuromyelitis optica spectrum disorders (NMOSD) who are anti-aquaporin 4 IgG (AQP4-IgG) seropositive |
| Predicted New Indication | Plasma cell myeloma (rank 4; the rank 1 prediction, drug-induced osteoporosis, has no evidence) |
| TxGNN Prediction Score | 92.75% (plasma cell myeloma); the rank 1 score is 96.44% |
| Evidence Level | L3 (plasma cell myeloma); L5 for the rank 1 prediction |
| EU Market Status | Cancelled only |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold (formal pipeline label for this candidate: Research Question) |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Inebilizumab is known to be a humanized monoclonal antibody against CD19, a surface marker on B cells and on some plasmablasts and plasma cells. By depleting these cells, it reduces the production of pathogenic autoantibodies in NMOSD.

This gives a plausible link to plasma cell malignancy, because myeloma arises from the plasma cell lineage. However, the link is weak. Mature myeloma cells often lose CD19, and expression is heterogeneous and low, so efficacy is uncertain.

The other top-ranked predictions are even less well supported. Several (psoriasis, pityriasis lichenoides, parapsoriasis) are T-cell-driven. Others (congenital hypotrichosis with juvenile macular dystrophy, HER2-positive breast carcinoma, severe nonproliferative diabetic retinopathy) have no plausible CD19-related mechanism. The high scores for these appear to be computational artifacts, and none has clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30915717](https://pubmed.ncbi.nlm.nih.gov/30915717/) | 2019 | Phase 1 clinical trial | Int J Hematol | Multicenter, open-label dose-escalation study (2, 4 or 8 mg/kg IV) of inebilizumab in Japanese patients with relapsed/refractory DLBCL, CLL, FL or multiple myeloma. It assessed safety, tolerability, pharmacokinetics and preliminary anti-tumour activity. |
| [42244451](https://pubmed.ncbi.nlm.nih.gov/42244451/) | 2026 | Review | Clin Pharmacol Ther | Reviews the rationale for B-cell and plasma-cell targeting from oncology to autoimmunity. Indirect context only. |

A third retrieved publication (PMID 38288815, a review of synthetic chemistry for anticancer drugs) is not clinically relevant and is omitted.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005818 (cancelled) | Uplizna | Not specified | Monotherapy for adult patients with neuromyelitis optica spectrum disorders (NMOSD) who are anti-aquaporin 4 immunoglobulin G (AQP4-IgG) s... |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-CD19 monoclonal antibody; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 34 interactions were identified in total. The 20 listed in the compiled data include:
  - **Major**: adalimumab, baricitinib, certolizumab pegol, cladribine, leflunomide, natalizumab, ozanimod
  - **Moderate**: roflumilast, alefacept, alemtuzumab, anakinra, azathioprine, canakinumab, dimethyl fumarate, ocrelizumab, omacetaxine mepesuccinate
  - **Minor**: zinc salts (sulfate, acetate, gluconate, chloride)

  Most of the major and moderate interactions involve other immunosuppressive or immunomodulatory agents, so additive immunosuppression and infection risk should be considered.

Warnings and contraindications from the label are not available. Please refer to the SmPC for the remaining safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only plasma cell myeloma has any direct clinical signal, and it is limited to one Phase 1 safety study. There is no efficacy evidence from Phase 2 or 3 trials, and CD19 expression on myeloma cells is low and heterogeneous. All other predicted indications, including the top-ranked drug-induced osteoporosis, rest on model scores alone (L5). The EU authorization is also cancelled.

**To proceed, the following is needed:**
- The label warnings and contraindications from the EU SmPC, which currently block safety screening
- Mechanism-of-action data from DrugBank
- Data on CD19 expression in myeloma and plasma cell populations
- Efficacy results from the Phase 1 myeloma cohort, followed by a Phase 2 study if signals are encouraging
- Clarification of the current regulatory status, since the EU authorization is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

