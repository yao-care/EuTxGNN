---
layout: default
title: Vandetanib
parent: High Evidence (L1-L2)
nav_order: 632
evidence_level: L2
indication_count: 10
---

# Vandetanib
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

# Vandetanib: From Medullary Thyroid Cancer to Renal Cell Carcinoma

## One-Sentence Summary

> Vandetanib is an oral multi-target tyrosine kinase inhibitor (VEGFR2/3, EGFR, RET), with its established use rooted in medullary thyroid cancer (per literature evidence; not captured in the structured regulatory data provided). The TxGNN model predicts it may be effective for **Renal Cell Carcinoma**, with **4 clinical trials** and **6 publications** currently supporting this direction, though the single relevant randomized trial has not yet reported outcome results.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Medullary Thyroid Cancer (per literature evidence within this pack; no structured license record available — see Data Gaps) |
| Predicted New Indication | Renal Cell Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| EU Market Status | Not Marketed (per structured regulatory data; no license records on file) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Vandetanib is described in the evidence pack's repurposing rationale as a multi-target tyrosine kinase inhibitor acting on VEGFR2/3, EGFR, and RET. Formal DrugBank MOA data was not returned for this candidate (flagged as a High-severity data gap), but this mechanism is consistently corroborated across the literature entries collected for this candidate (e.g., PMID 28477875, PMID 24451769, PMID 30860683), which describe vandetanib alongside other VEGFR/RET-targeting agents such as cabozantinib and lenvatinib.

Vandetanib's established use is in medullary thyroid cancer, where RET-pathway inhibition is the dominant therapeutic rationale. Renal cell carcinoma, by contrast, is classically driven by the VHL–HIF–VEGF axis, making VEGFR inhibition — rather than RET inhibition — the more relevant shared mechanism between the two indications. This is the same pharmacological rationale that underlies the approval of other VEGFR-targeting multi-kinase inhibitors (sunitinib, pazopanib, axitinib) in renal cell carcinoma, lending biological plausibility to the TxGNN prediction even though vandetanib itself has not been approved for this indication.

The clinical trial evidence for vandetanib in RCC is concentrated in rare, VHL-associated and non-clear-cell subtypes rather than common sporadic clear cell RCC, and several trials were terminated early with very small enrollment (n=3–7). Only one trial (NCT01191892) was both randomized and fully enrolled (n=82), but its own design description indicates the efficacy comparison had not been resolved at the time of the summary ("It is not yet known whether... vandetanib" adds benefit). This tempers the mechanistic plausibility with a caution that efficacy in RCC has not been clinically confirmed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | Completed | 82 | Randomized trial of carboplatin + gemcitabine ± vandetanib as first-line therapy in cisplatin-ineligible advanced urothelial/renal pelvis cancer; highest-quality evidence in this set, but efficacy outcome not reported in the summary. |
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | Completed | 37 | Evaluated vandetanib in Von Hippel-Lindau (VHL) disease-associated renal tumors, testing anti-angiogenic and direct anti-tumor activity; completed but non-randomized. |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | Terminated | 7 | Combination of vandetanib + metformin in HLRCC/SDH-associated kidney cancer or sporadic papillary RCC; terminated with very small enrollment, combination design limits attribution to vandetanib alone. |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | Terminated | 3 | Single-agent vandetanib in advanced clear cell renal carcinoma; terminated early with only 3 participants, insufficient for meaningful conclusions. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | RCT (different agent — guadecitabine) | Clinical Cancer Research | Phase 2 trial in SDH-deficient tumors including HLRCC-associated RCC; relevant disease context but tests a different drug, not vandetanib. |
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clinical & Experimental Metastasis | Reviews targeted therapy combinations in fumarate hydratase-deficient RCC, a rare aggressive subtype with no established standard regimen. |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets and Therapy | Positions vandetanib among VEGF/multi-target antiangiogenic agents (alongside sunitinib, sorafenib, pazopanib) approved across solid tumor types. |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Review | Bulletin du Cancer | Describes mechanism of cabozantinib (VEGFR2/c-MET/RET) as comparator, reinforcing the VEGFR/RET dual-targeting rationale shared with vandetanib. |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educational Book | Confirms vandetanib's RET-kinase-targeted approval basis in medullary thyroid cancer, providing the original-indication mechanistic anchor. |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclinical (mouse model) | Molecular Cancer Research | Characterizes TFE3-driven RCC biology and identifies novel therapeutic targets/diagnostic markers, providing background on RCC subtype heterogeneity relevant to mechanistic applicability. |

---

## EU Market Information

No marketing authorization records are present in this Evidence Pack (0 licenses on file, market status recorded as "Not Marketed"). This is notable because literature within the same pack references vandetanib as an EU-authorized product (brand name Caprelsa) for medullary thyroid cancer — this represents a gap in the structured regulatory data rather than a confirmed absence of EU authorization, and should be resolved before any downstream regulatory assessment.

---

## Cytotoxicity

Vandetanib is an oral, RET/VEGFR/EGFR-targeted small-molecule kinase inhibitor used in an oncology indication, meeting the criteria for inclusion of this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor: VEGFR2/3, EGFR, RET) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low relative to conventional cytotoxic chemotherapy; class-characteristic risks reported in the literature are hepatotoxicity (PMID 23981115) and proteinuria (PMID 32105149) rather than bone marrow suppression |
| Emetogenicity Classification | Low (consistent with oral targeted kinase inhibitors as a class) |
| Monitoring Items | Liver function tests, renal function/urine protein, blood pressure; comprehensive cardiac and other monitoring requirements should be confirmed against the SmPC, as full safety labeling data was not available in this pack |
| Handling Protection | As an oral targeted agent, full cytotoxic drug handling protocols required for IV chemotherapy are generally not applicable; confirm classification against institutional hazardous drug handling policy |

---

## Safety Considerations

Please refer to the SmPC for safety information. Structured safety data (key warnings, contraindications, and drug-drug interactions) was not available in this Evidence Pack; this is recorded as a **Blocking** data gap (DG001) that must be resolved before a safety pre-assessment (S1) can be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level L2 is driven by a single completed, randomized Phase 2 trial (NCT01191892) whose efficacy outcome is not confirmed in the available summary, and no marketing authorization or safety labeling data is on file for this candidate. The Blocking safety data gap prevents completion of even a preliminary (S1) safety assessment, so no forward decision beyond Hold is currently supportable.

**To proceed, the following is needed:**
- TFDA/EMA product labeling (warnings, contraindications) to clear the Blocking data gap (DG001) and enable an S1 safety pre-assessment
- Formal DrugBank-sourced mechanism of action confirmation (DG002)
- Outcome/efficacy results from NCT01191892 (or its publication record, if completed)
- Clarification of vandetanib's actual EU/regional marketing authorization status, given the discrepancy between "Not Marketed" regulatory data and literature references to EU authorization for medullary thyroid cancer
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

