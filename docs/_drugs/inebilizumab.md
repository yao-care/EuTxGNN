---
layout: default
title: Inebilizumab
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
---

# Inebilizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Inebilizumab (DB12530): From Anti-CD19 B-Cell Therapy to Plasma Cell Myeloma

## One-Sentence Summary

> Inebilizumab is an anti-CD19 monoclonal antibody; its original approved indication is not recorded in this evidence pack, and it is currently **not marketed in Taiwan**.
> Among 10 TxGNN-predicted indications, **plasma cell myeloma (multiple myeloma)** is the only one supported by actual data — **1 completed clinical trial** and **2 publications** — making it the sole candidate worth active follow-up; the remaining 9 predictions are AI-score-only with no clinical or literature backing.

*Note on indication selection: TxGNN's top-ranked prediction by score alone is "drug-induced osteoporosis" (96.4%), but the evidence pack itself flags it as mechanistically unsupported and evidence-free. This report instead highlights the highest-evidence candidate, plasma cell myeloma, as the actionable finding; all 10 predictions are listed in the appendix table below.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No data available (drug not TFDA-approved; no license or indication record) |
| Predicted New Indication | Plasma Cell Myeloma (Multiple Myeloma) |
| TxGNN Prediction Score | 92.75% (rank 50,530 of all predictions) |
| Evidence Level | L3 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question (S1 — further validation needed before Go/Hold decision) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Inebilizumab is not currently available in this evidence pack, and no original approved indication is on record (the drug is not marketed in Taiwan). Based on the information that is available, Inebilizumab is an anti-CD19 monoclonal antibody (previously coded MEDI-551) that depletes CD19-expressing B-lineage cells.

The rationale for exploring plasma cell myeloma is target biology: unlike CD20, which is lost early as B cells differentiate into plasma cells, CD19 remains expressed on clonotypic B cells and a subset of malignant plasma cell precursors in multiple myeloma. This gives the CD19-targeting mechanism a plausible biological rationale in this disease, distinct from the other 9 predicted indications in this pack (e.g., psoriasis, diabetic retinopathy), where the evidence text explicitly states no meaningful mechanistic link to B-cell/CD19 biology exists.

Critically, this is not a purely computational hypothesis — inebilizumab was actually tested clinically under its original development code (MEDI-551) in multiple myeloma patients, which is reflected in the trial and literature evidence below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01861340](https://clinicaltrials.gov/study/NCT01861340) | Early Phase 1 | Completed | 20 | Pilot study combining MEDI-551 (inebilizumab) with lenalidomide and dexamethasone in previously untreated multiple myeloma patients, aiming to reduce myeloma cancer stem cells |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30915717](https://pubmed.ncbi.nlm.nih.gov/30915717/) | 2019 | Phase 1 trial | International Journal of Hematology | Multicenter Phase 1 dose-escalation study of inebilizumab in Japanese patients with relapsed/refractory B-cell lymphoma and multiple myeloma (2, 4, or 8 mg/kg IV, days 1 and 8 of a 28-day cycle); evaluated safety, tolerability, PK, and preliminary anti-tumor activity |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Review | Anti-Cancer Agents in Medicinal Chemistry | Broad review of synthetic methodology for FDA-approved anticancer drugs (2018–2021); tangential coverage, not myeloma-specific |

---

## Taiwan Market Information

Inebilizumab is **not marketed in Taiwan** — there are 0 registered marketing authorizations and no license records in this evidence pack.

---

## Safety Considerations

Please refer to the SmPC for safety information. (No key warnings, contraindications, or drug-interaction data are currently available for Inebilizumab; a TFDA label review is flagged as a **blocking data gap** — see Conclusion below.)

---

## Conclusion and Next Steps

**Decision: Research Question** (decision stage S1)

**Rationale:**
Plasma cell myeloma is the only one of 10 TxGNN-predicted indications for Inebilizumab backed by actual clinical and literature evidence — a completed Early Phase 1 trial and a Phase 1 publication testing the drug (as MEDI-551) directly in this disease. Evidence level L3 reflects early-phase/exploratory data rather than confirmatory trials, so a Go/Hold call is premature; this warrants a structured research question rather than a final decision.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently a **blocking** data gap — required before any S1 safety screening can proceed)
- Mechanism of action (MOA) documentation from DrugBank (currently a **high-severity** data gap affecting mechanistic assessment)
- Follow-up on trial NCT01861340 outcomes (efficacy/safety results beyond the pilot stage)
- Confirmation of Taiwan/regional regulatory pathway, since the drug currently holds no Taiwan marketing authorization

---

### Appendix: Other TxGNN-Predicted Indications (Score-Only, No Supporting Evidence)

The following 9 predictions scored highly by TxGNN but have **no clinical trials or literature evidence**, and in several cases the model's own mechanistic rationale text notes a weak or contradictory biological link. All are at decision stage S0 with a **Hold** recommendation.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|
| 1 | Drug-induced osteoporosis | 96.44% | L5 | Hold |
| 2 | Psoriasis | 95.75% | L5 | Hold |
| 3 | Pityriasis lichenoides | 94.03% | L5 | Hold |
| 5 | Indolent plasma cell myeloma | 92.65% | L4 | Hold |
| 6 | Ulcerative colitis | 92.38% | L5 | Hold |
| 7 | Congenital hypotrichosis with juvenile macular dystrophy | 91.59% | L5 | Hold |
| 8 | HER2-positive breast carcinoma | 91.55% | L5 | Hold |
| 9 | Parapsoriasis | 91.49% | L5 | Hold |
| 10 | Severe nonproliferative diabetic retinopathy | 90.60% | L5 | Hold |

*Rank 5 (indolent plasma cell myeloma) borrows indirect mechanistic support from rank 4's evidence (same CD19+ plasma cell precursor population) but has no direct trial or literature data of its own.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

