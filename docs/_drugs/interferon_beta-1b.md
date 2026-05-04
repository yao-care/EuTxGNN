---
layout: default
title: Interferon Beta-1B
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 10
---

# Interferon Beta-1B
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

# Interferon beta-1b: From Multiple Sclerosis to Hairy Cell Leukemia

## One-Sentence Summary

Interferon beta-1b (IFN-β-1b) is a recombinant Type I interferon approved in many countries for relapsing forms of multiple sclerosis, though it currently holds no marketing authorization in Taiwan.
The TxGNN model predicts it may be effective for **Hairy Cell Leukemia (HCL)**, supported by **5 publications** (predominantly small-series studies from 1987–1990) and no registered clinical trials.
The prediction is mechanistically grounded: IFN-β-1b and the already-established IFN-α therapy for HCL share the same IFNAR1/IFNAR2 receptor complex, making a class-level antiproliferative effect biologically plausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsing multiple sclerosis (globally approved; not marketed in Taiwan) |
| Predicted New Indication | Hairy Cell Leukemia |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for IFN-β-1b is not available from the Taiwan regulatory source. Based on known pharmacology, IFN-β-1b is a non-glycosylated recombinant Type I interferon that binds to the shared IFNAR1/IFNAR2 receptor complex, activating the JAK-STAT signaling pathway to produce antiproliferative, antiviral, and immunomodulatory effects. Its efficacy in relapsing multiple sclerosis has been established through large randomized trials spanning several decades.

The mechanistic rationale for hairy cell leukemia rests on receptor-level convergence: IFN-α — already a proven therapy for HCL — and IFN-β-1b bind to identical receptor subunits. Hairy cells characteristically overexpress IFNAR, rendering them highly sensitive to Type I interferon antiproliferative signaling. While IFN-β-1b and IFN-α differ in amino acid sequence and glycosylation status, they engage overlapping JAK-STAT cascades and stimulate similar ADCC-enhancing effects. This shared receptor biology directly supports the TxGNN prediction.

Historical clinical data from 1987–1990 provides early proof-of-concept: prospective and case-series studies of beta-serine interferon (the precursor form of IFN-β-1b) demonstrated meaningful hematologic responses in HCL patients, including peripheral blood count normalization in the majority of evaluable cases. However, since cladribine and pentostatin now achieve high complete remission rates as first-line treatments, IFN-β therapy for HCL would currently occupy a second-line or refractory-disease niche. The prediction is historically validated but must be interpreted in the context of substantially evolved treatment standards.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Interferon beta-1b in hairy cell leukemia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3312839](https://pubmed.ncbi.nlm.nih.gov/3312839/) | 1987 | Case Series | Leukemia | UCLA experience with Type I interferons in 51 HCL patients; recombinant beta-serine-IFN produced hematologic improvement in 71% of treated patients; responses occurred within 6–12 months, similar in pattern to IFN-α |
| [2736487](https://pubmed.ncbi.nlm.nih.gov/2736487/) | 1989 | Prospective Comparative | Cancer | rIFN-β-ser (90 × 10⁶ IU SC TIW) prospectively compared to rIFN-α in HCL (n=8 evaluable): 63% achieved normalization of peripheral blood counts; additional 25% showed partial improvement; persistent bone marrow hairy cells detected in all patients |
| [2082943](https://pubmed.ncbi.nlm.nih.gov/2082943/) | 1990 | Case Series | American Journal of Hematology | 12 heavily pre-treated HCL patients (median 8.5 months from diagnosis) received beta-ser IFN 90 MU IV three times weekly; bone marrow involvement 90–100% hairy cells at baseline; antiproliferative activity demonstrated |
| [1702309](https://pubmed.ncbi.nlm.nih.gov/1702309/) | 1990 | Biomarker Study | British Journal of Haematology | Panel of monoclonal antibodies used to identify residual hairy cells after IFN-α or IFN-β therapy (n=20); hairy cells retained characteristic CD22/CD11c/CD25/CD32 phenotype post-treatment, informing minimal residual disease monitoring |
| [2198792](https://pubmed.ncbi.nlm.nih.gov/2198792/) | 1990 | Case Report | American Journal of Clinical Oncology | 2'-deoxycoformycin (DCF) achieved complete response in 3 patients who had failed prior IFN-α (n=2) or IFN-β-ser (n=1), confirming IFN-β as an active prior-line therapy and establishing DCF as a salvage option |

---

## Taiwan Market Information

Interferon beta-1b is not approved in Taiwan and holds no TFDA marketing authorization. No product licenses are currently registered.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Available evidence is limited to small observational studies and case series from over 30 years ago (L3), predating modern HCL treatment standards. While the mechanistic link via shared IFNAR receptors with IFN-α — an established HCL therapy — is compelling, no prospective controlled trials with IFN-β-1b in HCL have been registered, and current standard-of-care (cladribine/pentostatin) has substantially superseded interferon-based approaches.

**To proceed, the following is needed:**
- Mechanism of action data confirming IFNAR1/IFNAR2 expression density in hairy cells and comparative receptor binding affinity of IFN-β-1b versus IFN-α subtypes
- Taiwan TFDA prescribing information (仿單) for complete safety, warning, and contraindication data (currently unavailable — Data Gap DG001)
- Pharmacokinetic/pharmacodynamic assessment comparing IFN-β-1b dosing regimens used in MS with beta-serine-IFN doses used historically in HCL trials
- Evaluation of whether IFN-β-1b offers a meaningful niche in HCL patients refractory to purine analogues, particularly BRAF V600E–negative or vemurafenib-ineligible cases
- Updated literature search to determine whether any contemporary evidence on IFN-β in HCL has emerged beyond the 1987–1990 publications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

