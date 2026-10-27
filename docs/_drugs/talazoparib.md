---
layout: default
title: Talazoparib
parent: AI Predictions (L5)
nav_order: 586
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Talazoparib: predicted new indication HER2 positive breast carcinoma (evidence level L5). Approved use: Germline BRCA-mutated breast cancer"
monitor_inn: "Talazoparib"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "primary release disorder of platelets", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection"]
---

# Talazoparib
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

## Talazoparib: From BRCA-Mutated Breast Cancer and Prostate Cancer to HER2-Positive Breast Carcinoma
{: .text-alpha }

## One-Sentence Summary

Talazoparib is a PARP inhibitor originally authorised in the EU for germline BRCA-mutated breast cancer and metastatic castration-resistant prostate cancer (mCRPC).
The TxGNN model predicts it may be effective for **HER2-positive breast carcinoma**,
but no trial in the data compiled for this report directly tests talazoparib in HER2-positive disease. The data include **6 clinical trials** (all Phase 1/2, mostly HER2-negative or tumour-agnostic) and **15 publications** (mostly reviews, retrospective studies and HER2-negative or triple-negative breast cancer work).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Germline BRCA-mutated breast cancer; mCRPC (EU label) |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 98.98% |
| Evidence Level | L2 (as scored in the compiled data; see the caveat below) |
| EU Market Status | Cancelled only (the single EU authorisation is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank are not available for this report. Talazoparib is a PARP1/2 inhibitor with strong PARP-trapping activity. It causes synthetic lethality in tumours with homologous recombination deficiency, such as those with BRCA1/2 mutations.

Its approved breast cancer use is in germline BRCA-mutated, HER2-negative disease. For HER2-positive disease the link is indirect. It applies only to the BRCA-mutated or HRD subset, and HER2 status itself is not the target. The high TxGNN score most likely reflects the close network proximity of breast cancer subtypes, not HER2-specific biology.

The L2 evidence level comes from the compiled scoring and should be read cautiously. The supporting trials are not HER2-positive-specific, and none is a completed Phase 2/3 RCT in this population.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03499353](https://clinicaltrials.gov/study/NCT03499353) | Phase 2 | Terminated | 61 | Single-arm neoadjuvant talazoparib in germline BRCA1/2 early HER2-negative breast cancer |
| [NCT03911973](https://clinicaltrials.gov/study/NCT03911973) | Phase 1/2 | Active, not recruiting | 37 | Gedatolisib plus talazoparib in triple-negative or BRCA1/2-positive, HER2-negative breast cancer |
| [NCT05826964](https://clinicaltrials.gov/study/NCT05826964) | Phase 2 | Active, not recruiting | 24 | Randomised study using ctDNA to guide early treatment switching in metastatic breast cancer; talazoparib's role and HER2 relevance not confirmed |
| [NCT04550494](https://clinicaltrials.gov/study/NCT04550494) | Phase 2 | Active, not recruiting | 29 | Talazoparib in advanced solid tumours with DNA damage response gene aberrations (tumour-agnostic) |
| [NCT04134884](https://clinicaltrials.gov/study/NCT04134884) | Phase 1 | Completed | 34 | ASTX727 plus talazoparib in triple-negative or HER2-negative metastatic breast cancer; early safety and dose data |
| [NCT01042379](https://clinicaltrials.gov/study/NCT01042379) | Phase 2 | Recruiting | 5000 | I-SPY2 adaptive platform trial in neoadjuvant breast cancer; talazoparib-specific HER2-positive evidence not established |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36379199](https://pubmed.ncbi.nlm.nih.gov/36379199/) | 2022 | Meta-analysis | Breast | PARP inhibitors (olaparib, talazoparib) in BRCA1/2-related advanced HER2-negative breast cancer; GRADE recommendations |
| [36202026](https://pubmed.ncbi.nlm.nih.gov/36202026/) | 2022 | Meta-analysis | Cancer Treat Rev | Bayesian network meta-analyses of therapeutic algorithms in metastatic triple-negative breast cancer |
| [36045677](https://pubmed.ncbi.nlm.nih.gov/36045677/) | 2022 | Retrospective cohort | Front Immunol | Talazoparib versus conventional chemotherapy; the abstract refers to HER2-negative advanced breast cancer, despite the title mentioning HER2-positive |
| [36952230](https://pubmed.ncbi.nlm.nih.gov/36952230/) | 2023 | Retrospective cohort | Oncologist | Real-world talazoparib use in germline BRCA-mutated, HER2-negative advanced breast cancer |
| [39516069](https://pubmed.ncbi.nlm.nih.gov/39516069/) | 2025 | Retrospective cohort | Clin Breast Cancer | Real-world outcomes, toxicities and prescribing patterns of PARP inhibitors in metastatic breast cancer (Mayo Clinic) |
| [40192953](https://pubmed.ncbi.nlm.nih.gov/40192953/) | 2025 | Retrospective cohort | Mol Diagn Ther | Clinical actionability of molecular targets, including PARP inhibitors, in multi-ethnic breast cancer patients |
| [40471518](https://pubmed.ncbi.nlm.nih.gov/40471518/) | 2025 | Phase I/II trial | Breast Cancer Res Treat | Gedatolisib plus talazoparib in advanced triple-negative or BRCA1/2-positive, HER2-negative breast cancer |
| [34324367](https://pubmed.ncbi.nlm.nih.gov/34324367/) | 2021 | Guideline review | J Clin Oncol | ASCO guideline update for HR-positive, HER2-negative metastatic breast cancer |
| [33983696](https://pubmed.ncbi.nlm.nih.gov/33983696/) | 2021 | Review | Oncology (Williston Park) | Novel therapies for metastatic triple-negative breast cancer |
| [28958991](https://pubmed.ncbi.nlm.nih.gov/28958991/) | 2017 | Preclinical | Mol Cancer Ther | Gene signature linked to 53BP1 response to PARP inhibitors (including talazoparib) in triple-negative breast cancer cell lines |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004674 (cancelled) | Talzenna | Not specified | Breast cancer with deleterious or suspected deleterious germline BRCA mutations (patient selection by validated test); mCRPC (no tumour mutation testing required) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor) with cytotoxic effects |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions (anaemia, neutropenia and thrombocytopenia are expected class effects) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Complete blood count; liver and renal function |
| Handling Protection | Follow local regulations for handling cytotoxic or antineoplastic medicines |

## Safety Considerations

- **Drug Interactions**: The interaction query found 100 potential interactions. Major-level interactions in the listed results include **clarithromycin, deferiprone and samarium (153Sm) lexidronam**. Moderate-level interactions include eliglustat, eluxadoline, rolapitant, simvastatin, fidaxomicin, cobicistat, palifermin, strontium chloride Sr-89, eltrombopag, fostamatinib, ticagrelor, quinine, ivacaftor, roflumilast, chloramphenicol and erythromycin.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trial or publication tests talazoparib specifically in HER2-positive breast cancer. The available evidence concerns germline BRCA-mutated, HER2-negative or triple-negative disease, which is largely already covered by the existing label. The high TxGNN score likely reflects network proximity rather than HER2-specific biology. The only EU authorisation is also cancelled.

**To proceed, the following is needed:**
- Clinical data in HER2-positive breast cancer, ideally restricted to BRCA-mutated or HRD tumours
- Mechanism-of-action data and a clearer rationale for combining PARP inhibition with HER2-directed therapy
- Warnings and contraindications from the SmPC, which are missing from the compiled data
- Clarification of the EU regulatory status, since the single authorisation is cancelled
- A myelosuppression monitoring plan and a review of the major drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

