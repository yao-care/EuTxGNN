---
layout: default
title: Belatacept
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
---

# Belatacept
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

# Belatacept: From Kidney Transplant Rejection Prevention to Plasma Cell Myeloma

## One-Sentence Summary

Belatacept (Nulojix®) is a CTLA-4-Ig fusion protein originally developed to prevent acute rejection in kidney transplant recipients by blocking the CD28 T cell costimulatory pathway.
The TxGNN model predicts it may be effective for **Plasma Cell Myeloma**, with **2 clinical trials** and **7 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Kidney transplant rejection prevention (not registered in Taiwan; based on clinical trial context) |
| Predicted New Indication | Plasma Cell Myeloma |
| TxGNN Prediction Score | 97.03% |
| Evidence Level | L3 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Belatacept is a selective T cell costimulation blocker — a fusion protein composed of the extracellular domain of CTLA-4 fused to the Fc region of human IgG1. It works by competitively binding to CD80 (B7.1) and CD86 (B7.2) on antigen-presenting cells with higher affinity than native CD28, effectively blocking the "second activation signal" required for full T cell activation. Without this costimulatory signal, antigen-reactive T cells fall into anergy rather than becoming activated — an immunosuppressive mechanism originally exploited to prevent transplant rejection.

This same mechanism has direct biological relevance in plasma cell myeloma. Malignant plasma cells in multiple myeloma aberrantly overexpress CD86, making them structurally susceptible to CTLA-4-Ig engagement. Crucially, CD28 signaling in the myeloma context serves a dual function: it governs immune surveillance but also directly drives the proliferation of CD28-positive myeloma cells themselves (PMID 38562904). This raises the possibility that Belatacept could suppress myeloma cell growth by disrupting this proliferative signal — rather than acting solely as an immunosuppressant.

Preliminary clinical evidence supports this mechanistic reasoning. A 2019 Phase 1/2 pilot study (PMID 31129111) directly applied a CTLA4Ig-based reduced-intensity conditioning regimen combined with donor lymphocyte infusions for refractory myeloma following haploidentical transplantation, explicitly targeting the CD28-CD86 axis. Two currently active trials (NCT04827979, NCT05017545) pair belatacept with established anti-plasma cell agents (daratumumab and carfilzomib) to deplete plasma cells in highly sensitized transplant candidates, demonstrating mechanistic cross-over — though their primary endpoint remains transplant desensitization rather than myeloma treatment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04827979](https://clinicaltrials.gov/study/NCT04827979) | Phase 1/2 | Active, Not Recruiting | 19 | Daratumumab (anti-CD38) + Belatacept for highly sensitized kidney transplant candidates: anti-CD38 depletes plasma cells while Belatacept blocks B cell costimulation to reduce anti-HLA antibodies; mechanistically targets plasma cell biology shared with myeloma |
| [NCT05017545](https://clinicaltrials.gov/study/NCT05017545) | Phase 1/2 | Active, Not Recruiting | 21 | Carfilzomib (approved myeloma proteasome inhibitor) + Belatacept for transplant desensitization; Carfilzomib's established myeloma indication gives this combination cross-disease mechanistic significance in plasma cell elimination |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31129111](https://pubmed.ncbi.nlm.nih.gov/31129111/) | 2019 | Phase 1/2 Pilot | Clin Lymphoma Myeloma Leuk | CTLA4Ig-based reduced-intensity conditioning + donor lymphocyte infusions after haploidentical transplantation for refractory myeloma — the most direct evidence for targeting the CD28-CD86 pathway in myeloma treatment |
| [38562904](https://pubmed.ncbi.nlm.nih.gov/38562904/) | 2024 | Translational | bioRxiv | Endogenous CD28 drives CAR T cell responses in multiple myeloma; CD28 costimulation plays a critical dual role in both myeloma cell proliferation and anti-myeloma immune effector function — inhibition may have complex bidirectional effects |
| [9869202](https://pubmed.ncbi.nlm.nih.gov/9869202/) | 1998 | Observational | Leuk Lymphoma | B7 family costimulatory molecules (CD80/CD86) expressed on malignant plasma cells; altered CD28/CTLA-4 expression found on T cells of MM patients — foundational evidence for pathway dysregulation in myeloma |
| [15370258](https://pubmed.ncbi.nlm.nih.gov/15370258/) | 2004 | Observational | Leuk Lymphoma | Elevated soluble CD80 detected in multiple myeloma patients vs. normal donors, suggesting active shedding of costimulatory ligands in MM microenvironment — supports CD80/CD86 axis involvement |
| [11167807](https://pubmed.ncbi.nlm.nih.gov/11167807/) | 2001 | Genetic Association | Br J Haematol | CTLA-4 microsatellite polymorphism associated with MM susceptibility — genetic-level evidence linking the CTLA-4 pathway to myeloma disease predisposition |
| [11981425](https://pubmed.ncbi.nlm.nih.gov/11981425/) | 2002 | Observational | Transplantation | Anti-CTLA-4 antibodies detected in ATG/TMG preparations used in leukemia treatment; CTLA-4 targeting may contribute to immunosuppressive effects in hematological malignancy contexts |
| [40398621](https://pubmed.ncbi.nlm.nih.gov/40398621/) | 2025 | Review/Registry | Transplant Cell Ther | CIBMTR annual report on HCT and cellular therapy trends including multiple myeloma (2013–2023); provides treatment landscape context for positioning Belatacept among existing myeloma therapies |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Key safety signals relevant to potential myeloma use:** Published literature identifies **post-transplant lymphoproliferative disorder (PTLD)** — especially in EBV-seronegative recipients — and **serious opportunistic infections** as class-level risks for Belatacept. These risks require careful benefit-risk assessment before any use in myeloma patients, who are frequently immunocompromised. Taiwan TFDA package insert data (DG001) and DrugBank MOA data (DG002) were not available in this evidence pack; both must be retrieved before proceeding to clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A biologically plausible mechanistic link exists between Belatacept's CD28-CD86 blockade and plasma cell myeloma biology, anchored by one Phase 1/2 pilot study directly targeting this pathway in refractory myeloma (PMID 31129111). However, no dedicated clinical trial has evaluated Belatacept as a primary myeloma treatment, and the dual role of CD28 — simultaneously supporting anti-tumor T cell immunity and driving myeloma cell proliferation — creates a fundamental mechanistic tension that must be resolved before investment is warranted.

**To proceed, the following is needed:**
- Resolve the mechanistic paradox: determine whether Belatacept's CD28 blockade primarily suppresses myeloma cell proliferation (beneficial) or suppresses anti-myeloma T cell surveillance (harmful) — preclinical models distinguishing these effects are needed first
- Dedicated Phase 1/2 clinical trial evaluating Belatacept in relapsed/refractory multiple myeloma, building on the CTLA4Ig + haploidentical transplant concept established in PMID 31129111
- Outcome data from NCT05017545 regarding plasma cell depletion depth and durability, which may provide proof-of-concept for plasma cell targeting
- Complete safety data retrieval: Taiwan TFDA package insert (DG001) and DrugBank MOA (DG002)
- PTLD risk stratification strategy for myeloma patients, particularly those who are EBV-seronegative or heavily pre-treated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

