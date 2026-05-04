---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
---

# Adalimumab
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

# Adalimumab: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Adalimumab is a fully human anti-TNF-α monoclonal antibody established globally for rheumatoid arthritis and multiple other inflammatory conditions, though currently not registered in the Taiwan regulatory database.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, with **5 registered clinical trials** (all indirect evidence) and **20 publications** — including 1 systematic review specifically on biological therapy in rheumatoid vasculitis — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Taiwan regulatory database |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the queried dataset. Based on known information, adalimumab is a fully human monoclonal antibody (IgG1 subclass) belonging to the TNF-α inhibitor class. Its efficacy in rheumatoid arthritis has been established through multiple Phase 3 trials worldwide, and mechanistically it works by selectively neutralizing both soluble and membrane-bound TNF-α — thereby interrupting downstream pro-inflammatory cascades.

Rheumatoid vasculitis (RV) is one of the most severe extra-articular manifestations of rheumatoid arthritis, characterized by immune complex deposition in vessel walls, complement activation, and neutrophil-mediated vascular destruction. TNF-α plays a central pathogenic role in this process: it promotes endothelial activation, facilitates immune complex deposition, and sustains neutrophil infiltration into vessel walls. Blocking TNF-α with adalimumab may therefore directly attenuate the vascular inflammatory cascade driving RV, making the mechanistic link biologically coherent rather than merely associative.

The prediction is further supported by the fact that RV occurs almost exclusively in patients with longstanding seropositive RA — the very population for whom adalimumab was originally developed. A 2021 systematic review (PMID 33058033) examined biological agents specifically in RV, and case reports document clinical responses when adalimumab was used directly in RV patients (PMID 25133007). However, no prospective controlled trials have been specifically designed for RV, leaving this a scientifically plausible but clinically unconfirmed repurposing candidate.

---

## Clinical Trial Evidence

No clinical trials specifically designed to evaluate adalimumab in rheumatoid vasculitis were identified. The 5 retrieved trials are all indirect (Grade C relevance).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Observational study of tocilizumab in RA patients with inadequate DMARD or biologic response; provides background on refractory RA management but does not address vasculitis |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large retrospective cohort tracking incident IMID risk in biologics users including adalimumab; not designed to evaluate RV as a treatment endpoint |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Assesses immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty; peripherally relevant to adalimumab dosing decisions in RA |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional study of biological DMARD treatment patterns in Chinese RA patients; no RV-specific endpoints |
| [NCT05111743](https://clinicaltrials.gov/study/NCT05111743) | N/A | Completed | 9,261 | Real-world evaluation of brolucizumab for neovascular AMD; no relationship to adalimumab or rheumatoid vasculitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | PRISMA-based systematic review on biological therapy in rheumatoid vasculitis; examines the therapeutic role of TNF inhibitors and other biologics in RV, providing the strongest available evidence base for this repurposing direction |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort | RMD Open | BSRBR-RA registry analysis comparing drug-specific risk of vasculitis-like events (VLEs) in TNFi-treated RA patients versus those on non-biological DMARDs; directly quantifies the TNFi–vasculitis relationship |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Review | Journal of Clinical Medicine | Overview of RA-associated episcleritis and scleritis; discusses biologics including adalimumab for refractory ocular vascular inflammatory manifestations, an RV-related phenotype |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Case Report | Case Reports in Rheumatology | 42-year-old RA patient with digital vasculitis (necrotizing fingertip ulcers) responded well to adalimumab; direct case-level evidence of adalimumab efficacy in RV |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Case Report | Internal Medicine (Tokyo) | Acute pulmonary hypertension crisis in RV patient following adalimumab dose reduction; highlights that adalimumab withdrawal in active RV can trigger life-threatening decompensation |
| [21385558](https://pubmed.ncbi.nlm.nih.gov/21385558/) | 2011 | Case Report | Clinical and Experimental Rheumatology | Tocilizumab achieved remission in multidrug-refractory, anti-TNF-resistant systemic RV; provides context on treatment sequencing when adalimumab fails |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Case Report | American Journal of Dermatopathology | First reported case of leukocytoclastic vasculitis with perivascular hemophagocytosis associated with adalimumab initiation; important paradoxical safety signal to monitor |
| [38931826](https://pubmed.ncbi.nlm.nih.gov/38931826/) | 2024 | PK Study | Pharmaceutics | Population PK modelling of adalimumab and etanercept biosimilar dosing in RA; supports dose interval optimization strategies relevant to clinical translation |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case Report | Internal Medicine (Tokyo) | ANCA-associated nephritis (pauci-immune glomerulonephritis) developed during combined abatacept and adalimumab therapy in an elderly RA patient; illustrates renal vasculitic complications in this setting |
| [16979537](https://pubmed.ncbi.nlm.nih.gov/16979537/) | 2006 | Review | Best Practice & Research Clinical Rheumatology | Comprehensive review of problems encountered with anti-TNF therapy across >400,000 patients, including autoimmune phenomena and vasculitis as rare but recognized adverse events |

---

## Taiwan Market Information

Adalimumab is currently **not registered** in the Taiwan regulatory database. No authorized products, dosage forms, or approved indications are on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No authorizations found |

---

## Safety Considerations

TFDA product label warnings and contraindications are not available in the current dataset (designated as a blocking data gap). Please refer to the product's Summary of Product Characteristics (SmPC) for complete safety information.

No drug-drug interaction records were returned from the queried database.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
One systematic review and multiple case reports confirm that biological therapy including adalimumab has been used in rheumatoid vasculitis with clinical responses documented, supporting L3 evidence — but the complete absence of prospective controlled trials specifically enrolling RV patients means this remains an investigational use requiring structured evidence generation before clinical adoption.

**To proceed, the following is needed:**
- Design a prospective cohort or registry specifically enrolling RA patients with confirmed active rheumatoid vasculitis (meeting ACR/EULAR classification criteria)
- Retrieve TFDA product label (SmPC) to complete safety profiling — warnings, contraindications, and drug interactions (Blocking data gap DG001)
- Obtain MOA data from DrugBank API to formalize mechanistic analysis (High priority data gap DG002)
- Carefully differentiate patients with primary RV from those with TNFi-induced paradoxical vasculitis before enrollment
- Define primary endpoints (vasculitis remission, organ damage prevention) and establish minimum disease activity thresholds for treatment initiation
- Assess whether adalimumab's SC route and biweekly dosing are compatible with the clinical management of active RV (often requiring rapid disease control)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

