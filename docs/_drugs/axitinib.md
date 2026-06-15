---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib: From Advanced Renal Cell Carcinoma to Renal Cell Carcinoma Associated with Neuroblastoma

## One-Sentence Summary

Axitinib (Inlyta) is a potent and selective VEGFR-1/2/3 tyrosine kinase inhibitor globally approved for advanced renal cell carcinoma (mRCC), though it is not currently registered in Taiwan.
The TxGNN model's top-ranked prediction is **Renal Cell Carcinoma Associated with Neuroblastoma** (rank #1, score 99.90%), a rare composite malignancy — however, **no clinical trials or publications** currently support this specific direction.
The model concurrently predicts Axitinib for multiple RCC subtypes (ranks #2–6, #9), several of which carry Phase 2–3 clinical trial evidence; the most evidence-rich prediction is **Renal Carcinoma** (rank #6, L1, 50+ clinical trials, 20+ publications).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Advanced renal cell carcinoma (globally approved; not registered in Taiwan) |
| Predicted New Indication | Renal Cell Carcinoma Associated with Neuroblastoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (rank #1 target) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (rank #1) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacology, Axitinib is a second-generation oral VEGFR tyrosine kinase inhibitor that selectively targets VEGFR-1, VEGFR-2, and VEGFR-3 with an IC₅₀ approximately 10-fold lower than earlier-generation TKIs. In conventional clear-cell RCC, VHL gene loss stabilizes HIF-1α/2α, driving VEGF/VEGFR overexpression and tumor neovascularization — the mechanism Axitinib directly disrupts.

For the rank #1 predicted indication — **renal cell carcinoma associated with neuroblastoma** — the RCC component, if VHL-deficient, would theoretically retain VEGF/VEGFR pathway dependence, offering a mechanistic rationale for VEGFR inhibition. However, the neuroblastoma component is primarily driven by MYCN amplification and ALK mutations, pathways not targeted by Axitinib. This mechanistic mismatch, combined with the ultra-rare and heterogeneous nature of this composite malignancy, substantially weakens the prediction's actionability.

The TxGNN model likely derives this high score from the shared "renal cell carcinoma" node in the knowledge graph. The model's broader predictions across related RCC subtypes — including Xp11.2/TFE3 translocation RCC, unclassified RCC, and collecting duct carcinoma — are mechanistically more coherent and carry actual clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for renal cell carcinoma associated with neuroblastoma.

**Related evidence from other high-ranked RCC subtype predictions (for context):**

**Renal Carcinoma (Rank #6, L1 — strongest evidence)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00678392](https://clinicaltrials.gov/study/NCT00678392) | Phase 3 | Completed | 723 | AXIS trial: Axitinib vs. sorafenib as 2nd-line mRCC; established PFS/OS benefit and is the FDA/EMA approval basis |
| [NCT05738694](https://clinicaltrials.gov/study/NCT05738694) | Phase 2 | Recruiting | 298 | Multicenter RCT: neoadjuvant Axitinib + PD-1 inhibitor vs. surgery alone in high-risk RCC (T2G3-4/T3-4/N1) |
| [NCT00835978](https://clinicaltrials.gov/study/NCT00835978) | Phase 2 | Completed | 213 | Randomized double-blind study of Axitinib dose titration strategy in mRCC; supports dosing optimization |
| [NCT05817903](https://clinicaltrials.gov/study/NCT05817903) | Phase 2 | Recruiting | 118 | AxIn Study: Axitinib intensification + nivolumab vs. nivolumab alone after nivolumab + ipilimumab induction |
| [NCT02133742](https://clinicaltrials.gov/study/NCT02133742) | Phase 1 | Completed | 52 | Phase 1b PK/PD study of Axitinib + pembrolizumab combination; established recommended Phase 2 dose |
| [NCT05808608](https://clinicaltrials.gov/study/NCT05808608) | Phase 1/2 | Recruiting | 33 | AK104 (PD-1/CTLA-4 bispecific antibody) + Axitinib in special pathological RCC subtypes |
| [NCT04385654](https://clinicaltrials.gov/study/NCT04385654) | Phase 2 | Unknown | 40 | Toripalimab + Axitinib as neoadjuvant therapy for advanced/metastatic non-clear cell RCC |
| [NCT03494816](https://clinicaltrials.gov/study/NCT03494816) | Phase 2 | Completed | 24 | NAXIVA: Axitinib for reducing venous tumour thrombus extent in clear cell RCC with venous invasion |
| [NCT01441414](https://clinicaltrials.gov/study/NCT01441414) | Phase 2 | Terminated | 18 | Axitinib + CVX-060 (ANG-2 inhibitor) vs. axitinib alone in previously treated mRCC; terminated early |
| [NCT00700258](https://clinicaltrials.gov/study/NCT00700258) | N/A (Registry) | Completed | 1,520 | STAR-TOR registry: safety, tolerability and efficacy of Axitinib in advanced mRCC in routine practice |

**Xp11.2/TFE3 Translocation RCC (Rank #3, L2) and Childhood Kidney Cell Carcinoma (Rank #4, L2)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | Active, not recruiting | 15 | Randomized Phase 2: Axitinib + nivolumab vs. nivolumab alone for TFE/translocation RCC across all age groups (including pediatric) |
| [NCT04510597](https://clinicaltrials.gov/study/NCT04510597) | Phase 3 | Recruiting | 364 | PROBE Trial: ICI-based combination ± cytoreductive nephrectomy for metastatic RCC; large Phase 3 providing indirect evidence |
| [NCT02164838](https://clinicaltrials.gov/study/NCT02164838) | Phase 1 | Completed | 51 | First-ever pediatric Phase 1 trial of Axitinib in children and adolescents with refractory solid tumors; established MTD/RP2D |

**Collecting Duct Carcinoma (Rank #9, L3)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06211114](https://clinicaltrials.gov/study/NCT06211114) | Phase 2 | Recruiting | 30 | ICI + Axitinib combination for previously treated advanced collecting duct carcinoma; most direct prospective evidence for this rare subtype |

---

## Literature Evidence

Currently no related literature available for renal cell carcinoma associated with neuroblastoma.

**Related evidence from high-ranked RCC predictions (for context):**

**Renal Carcinoma (Rank #6, L1)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30779529](https://pubmed.ncbi.nlm.nih.gov/30779529/) | 2019 | RCT | N Engl J Med | KEYNOTE-426: Pembrolizumab + Axitinib superior to sunitinib in 1st-line advanced RCC (OS, PFS, ORR all improved) |
| [40750932](https://pubmed.ncbi.nlm.nih.gov/40750932/) | 2025 | RCT Follow-up | Nature Med | KEYNOTE-426 5-year analysis: sustained OS/PFS superiority with biomarker characterization |
| [30779531](https://pubmed.ncbi.nlm.nih.gov/30779531/) | 2019 | RCT | N Engl J Med | JAVELIN Renal 101: Avelumab + Axitinib vs. sunitinib; significantly improved PFS as 1st-line mRCC treatment |
| [39706335](https://pubmed.ncbi.nlm.nih.gov/39706335/) | 2025 | RCT | Ann Oncol | JAVELIN Renal 101 final analysis: overall survival results for avelumab + axitinib vs. sunitinib |
| [37872020](https://pubmed.ncbi.nlm.nih.gov/37872020/) | 2024 | RCT | Ann Oncol | RENOTORCH Phase 3: Toripalimab + Axitinib vs. sunitinib in intermediate/poor-risk advanced RCC |
| [37500340](https://pubmed.ncbi.nlm.nih.gov/37500340/) | 2023 | RCT Follow-up | Eur Urol | KEYNOTE-426 43-month protocol-specified final analysis; durable survival benefit confirmed |
| [39362847](https://pubmed.ncbi.nlm.nih.gov/39362847/) | 2024 | Cohort | Signal Transduct Target Ther | NEOTAX Phase 2: Neoadjuvant toripalimab + axitinib in ccRCC with IVC tumor thrombus; 35% down-staging rate |
| [28276433](https://pubmed.ncbi.nlm.nih.gov/28276433/) | 2017 | Review | Nat Rev Dis Primers | Comprehensive RCC biology review: subtypes, VHL/HIF/VEGF pathway, treatment landscape |
| [29033542](https://pubmed.ncbi.nlm.nih.gov/29033542/) | 2017 | Review | Drug Des Devel Ther | Axitinib mechanism, clinical development, and role in RCC treatment |
| [32895571](https://pubmed.ncbi.nlm.nih.gov/32895571/) | 2020 | Biomarker Analysis | Nature Med | JAVELIN Renal 101 biomarker analysis: PD-L1 and TMB do not predict PFS; FcγR polymorphisms explored |

**Childhood Kidney Cell Carcinoma (Rank #4, L2)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39326645](https://pubmed.ncbi.nlm.nih.gov/39326645/) | 2024 | Review | Crit Rev Oncol Hematol | Narrative review of Axitinib outcomes across children, young adults, and adults with RCC |
| [31012542](https://pubmed.ncbi.nlm.nih.gov/31012542/) | 2019 | Review | Pediatr Blood Cancer | Advanced pediatric RCC treatment review; discusses VEGFR-TKI as a treatment option given limited alternatives |
| [26279736](https://pubmed.ncbi.nlm.nih.gov/26279736/) | 2015 | Case Report | Can Urol Assoc J | First reported pediatric use of Axitinib (12-year-old with malignant EAML); adult protocols applied safely |

**Liposarcoma (Rank #5, L4)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27822137](https://pubmed.ncbi.nlm.nih.gov/27822137/) | 2016 | Preclinical | Sarcoma | Axitinib demonstrates antiangiogenic and antitumor activity in myxoid liposarcoma cell lines (FUS-CHOP translocation drives VEGF overexpression) |

---

## Taiwan Market Information

Axitinib is currently **not registered in Taiwan**. No TFDA-authorized product licenses are on record.

| Item | Status |
|------|--------|
| Market Status | Not marketed in Taiwan |
| Total Authorizations | 0 |
| Regulatory Note | Axitinib (Inlyta®) is approved by the FDA (2012) and EMA for advanced/metastatic RCC, but Taiwan registration has not been obtained. TFDA SmPC data is unavailable (Data Gap DG001 — blocking for safety evaluation). |

---

## Cytotoxicity

Axitinib is a targeted antineoplastic agent used in oncology (VEGFR tyrosine kinase inhibitor).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — VEGFR-1/2/3 tyrosine kinase inhibitor (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Low to moderate; thrombocytopenia and neutropenia reported less frequently than with cytotoxic agents; monitor CBC |
| Emetogenicity Classification | Low |
| Monitoring Items | Blood pressure (hypertension very common, often used as pharmacodynamic marker), liver function (ALT/AST), thyroid function (hypothyroidism), CBC, renal function, hand-foot skin reaction assessment |
| Handling Protection | Oral solid dosage form; standard cytotoxic drug handling precautions apply per institutional protocols |

---

## Safety Considerations

Please refer to the SmPC for safety information.

TFDA-specific prescribing information (SmPC warnings and contraindications) was not retrievable for this report (Data Gap DG001, severity: Blocking). Known class-effect concerns for VEGFR-TKIs include hypertension, hand-foot skin reaction (palmar-plantar erythrodysesthesia), hepatotoxicity, thyroid dysfunction, arterial thromboembolic events, and wound healing complications. These should be reviewed against the full SmPC before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold** (for rank #1 prediction: renal cell carcinoma associated with neuroblastoma)

**Rationale:**
The composite RCC-neuroblastoma entity is ultra-rare with no clinical or preclinical data supporting Axitinib use, and the neuroblastoma component is driven by MYCN/ALK pathways that are mechanistically unrelated to VEGFR inhibition — the Hold recommendation is appropriate regardless of TxGNN's high computational score.

**To proceed for rank #1, the following is needed:**
- Preclinical studies characterizing VEGFR pathway activity in RCC-neuroblastoma composite tumors
- Case series or expert consensus establishing treatment paradigms for this entity
- TFDA SmPC safety data (DG001: Blocking — required before any S1 safety evaluation)
- DrugBank MOA data confirmation (DG002: High priority)

---

**Summary across all 10 predicted indications:**

| Rank | Predicted Indication | Evidence Level | Recommendation |
|------|---------------------|----------------|----------------|
| #6 | Renal carcinoma | L1 | Proceed with Guardrails |
| #3 | Xp11.2/TFE3 translocation RCC | L2 | Proceed with Guardrails |
| #4 | Childhood kidney cell carcinoma | L2 | Proceed with Guardrails |
| #9 | Collecting duct carcinoma | L3 | Proceed with Guardrails |
| #2 | Unclassified renal cell carcinoma | L3 | Research Question |
| #5 | Liposarcoma | L4 | Research Question |
| #1 | RCC associated with neuroblastoma | L5 | **Hold** |
| #7 | Ovarian myxoid liposarcoma | L5 | Hold |
| #8 | Angiolipoma | L5 | Hold |
| #10 | Familial spontaneous pneumothorax | L5 | Hold |

The near-term opportunity for Axitinib in Taiwan lies in pursuing TFDA registration for established indications (advanced mRCC, ICI combination regimens) and exploring compassionate use frameworks for rare RCC subtypes with Phase 2 evidence — not the rank #1 TxGNN prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

