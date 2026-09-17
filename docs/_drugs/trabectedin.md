---
layout: default
title: Trabectedin
parent: High Evidence (L1-L2)
nav_order: 610
evidence_level: L2
indication_count: 10
---

# Trabectedin
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Trabectedin: From Soft Tissue Sarcoma to Breast Carcinoma

## One-Sentence Summary

Trabectedin is a marine-derived, DNA-binding antineoplastic agent historically developed for soft tissue sarcoma and, in combination with pegylated liposomal doxorubicin (PLD), for platinum-sensitive relapsed ovarian cancer — though this dataset records no currently active EU marketing authorization for the drug. The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **2 clinical trials** and **20 publications** — including a completed Phase 2 RCT — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Soft tissue sarcoma; platinum-sensitive relapsed ovarian cancer (with PLD) — per literature evidence; no active EU marketing authorization recorded in this dataset |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| EU Market Status | Not marketed (per this dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The structured mechanism-of-action field for trabectedin is currently a data gap in this dataset. However, the supporting literature and the mechanistic rationale generated for this candidate consistently describe trabectedin as a DNA minor-groove binder that inhibits transcription-coupled nucleotide excision repair (TC-NER) and induces DNA double-strand breaks. This produces selective cytotoxicity in tumors with BRCA1/2 mutations or broader homologous recombination deficiency (HRD), and trabectedin additionally modulates the tumor microenvironment by depleting tumor-associated macrophages (TAM).

Breast and ovarian cancer share substantial mechanistic overlap: up to 25% of sporadic breast tumors carry somatic inactivation of the homologous recombination repair pathway (the "BRCAness" phenotype), a molecular profile closely resembling the BRCA-mutated ovarian cancer population in which trabectedin-PLD is already used. This shared DNA-repair vulnerability is the biological basis for extending trabectedin into breast cancer.

Clinical data support this extrapolation: a Phase 2 trial stratified by XPG mRNA expression evaluated trabectedin in hormone receptor-positive, HER2-negative advanced breast cancer, and a separate international first-in-class Phase II study demonstrated activity specifically in patients with germline BRCA1/2-mutated metastatic breast cancer. Translational work further identified CUL4A as a candidate biomarker of trabectedin sensitivity in breast cancer cell lines, reinforcing that DNA-repair status — not tumor site — may be the key determinant of response.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | Completed | 9 | Evaluated olaparib maintenance after trabectedin-PLD induction in recurrent ovarian carcinoma; population may include BRCA-mutated patients relevant to the breast cancer HRD subgroup, though the primary endpoint is olaparib maintenance rather than trabectedin efficacy itself |
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | Completed | 76 | Single-blind, placebo-controlled study assessing trabectedin's effect on QT/QTc interval in patients with advanced solid tumor malignancies; primarily a cardiac safety study rather than a breast cancer efficacy trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | RCT/Phase 2 | Clinical Breast Cancer | Phase 2 study of trabectedin in HR-positive, HER2-negative advanced breast cancer, stratified by tumor XPG mRNA expression as a predictive biomarker |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Phase 2 | Annals of Oncology | International first-in-class Phase II trial demonstrating trabectedin activity in germline BRCA1/2-mutated metastatic breast cancer |
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | RCT/Phase 2 | Clinical Breast Cancer | Multicenter randomized Phase II study comparing two trabectedin dosing regimens as single-agent therapy in advanced breast cancer after anthracycline and taxane failure |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Review | Cancer Treatment Reviews | Reviews trabectedin's DNA-repair-pathway-selective mechanism and rationale for use in BRCA-deficient tumors, including breast cancer |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Phase 1 | European Journal of Cancer | Phase I PK study of trabectedin plus doxorubicin in soft tissue sarcoma and advanced breast cancer, showing feasibility and antitumor activity |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Review | Expert Opinion on Investigational Drugs | Reviews trabectedin's transcription-inhibiting mechanism and TAM-reducing effect as the rationale for a breast cancer indication |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | Preclinical | Cancer Immunology Research | Shows trabectedin depletes immunosuppressive myeloid cells and enhances IL-12-induced NK-cell cytotoxicity against triple-negative breast cancer |
| [23364677](https://pubmed.ncbi.nlm.nih.gov/23364677/) | 2013 | Biomarker/Translational | Molecular Cancer Therapeutics | Identifies CUL4A as a novel biomarker of trabectedin sensitivity via DNA-repair gene expression analysis in breast cancer cell lines |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | Preclinical | Toxicology Letters | Demonstrates trabectedin induces apoptosis via distinct pathways in HER2-negative/ER-positive and HER2-positive/ER-negative breast cancer cell lines |
| [38366738](https://pubmed.ncbi.nlm.nih.gov/38366738/) | 2024 | Case Report | The Journal of Dermatology | Case report of trabectedin effectiveness in radiation-induced breast angiosarcoma refractory to multiple prior anticancer drugs |

---

## EU Market Information

No active EU marketing authorization is recorded for trabectedin in this dataset (`total_licenses = 0`, `market_status = Not marketed`). Regulatory confirmation should be sought directly from EMA before proceeding further.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — marine-derived DNA minor-groove binding agent, transcription-coupled NER inhibitor |
| Myelosuppression Risk | High — literature reports grade 3–4 neutropenia in approximately 50% and thrombocytopenia in approximately 20% of patients |
| Emetogenicity Classification | Not specified in the available evidence; please refer to the SmPC |
| Monitoring Items | Complete blood count (neutropenia, thrombocytopenia), liver function tests (transaminitis, cholangitis have been reported), renal function |
| Handling Protection | Standard cytotoxic/hazardous drug handling precautions required |

---

## Safety Considerations

Please refer to the SmPC for safety information. No structured warnings, contraindications, or drug interaction data are currently available in this dataset (key warnings and contraindications are flagged as a **Blocking** data gap that prevents an initial safety review).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While a completed Phase 2 RCT and biomarker-driven translational studies suggest trabectedin may have activity in BRCA1/2- or HRD-defined breast carcinoma subgroups, the absence of official safety labeling data (warnings, contraindications, DDI) is a blocking gap that prevents even an initial safety assessment, and no active EU marketing authorization is recorded for this drug in the current dataset.

**To proceed, the following is needed:**
- Official EMA/SmPC safety data (key warnings, contraindications, drug interactions) — currently blocking
- Confirmation of current EU marketing authorization status
- Structured mechanism-of-action documentation (e.g., via DrugBank API)
- A biomarker-based patient selection strategy (BRCA1/2, XPG, HRD status) to define the target breast cancer subpopulation
- Route/dosage form compatibility assessment (currently pending in this dataset)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

