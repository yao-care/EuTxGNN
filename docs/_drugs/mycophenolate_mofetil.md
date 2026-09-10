---
layout: default
title: Mycophenolate Mofetil
parent: 僅模型預測 (L5)
nav_order: 404
evidence_level: L5
indication_count: 10
---

# Mycophenolate Mofetil
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

# Mycophenolate Mofetil: From Immunosuppressive Therapy to HIV Infectious Disease

## One-Sentence Summary

> Mycophenolate mofetil (MMF) is an immunosuppressive agent whose formal Taiwan/EU regulatory indication text is not available in this evidence pack.
> The TxGNN model predicts it may be effective for **HIV Infectious Disease**,
> with **10 clinical trials** and **10+ publications** (from a pool of 14) currently supporting this direction, though outcomes are mixed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (regulatory license data unavailable). Supporting literature consistently describes MMF as an **immunosuppressive agent** used to prevent allograft rejection after renal, cardiac, or liver transplant. |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002, High severity). Based on the supporting literature, mycophenolate mofetil is an inosine monophosphate dehydrogenase (IMPDH) inhibitor that blocks de novo purine (guanosine) synthesis, thereby suppressing proliferation of activated T and B lymphocytes. This is the pharmacological basis for its established use as an immunosuppressive agent in solid organ transplantation.

The proposed link to HIV is mechanistic rather than direct antiviral: activated CD4+ T cells are the primary replication targets and reservoir for HIV, so limiting their proliferation could theoretically reduce viral replication capacity. Several pharmacokinetic studies (PMID 15355127, 12352149) further show that MMF depletes intracellular deoxyguanosine triphosphate (dGTP), a mechanism proposed to potentiate the antiviral activity of certain NRTIs such as abacavir and didanosine — an effect distinct from MMF's classic immunosuppressive role.

However, this mechanistic plausibility has not translated into confirmed efficacy. The dedicated MAN2 study (NCT00120419) and its cardiovascular substudy (NCT00247494) remain in "Unknown" status with no reported outcomes, and the only trial designed specifically to test MMF as an antiretroviral adjunct (NCT00021489) was withdrawn with zero enrollment. Despite two decades of small pilot and cohort studies, no confirmatory large-scale trial has established clinical benefit.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | Completed | 27 | Evaluated acute renal graft rejection incidence at 6 months post-transplant in HIV-infected patients on a raltegravir-containing regimen; standard immunosuppression included MMF. |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 1/2 | Completed | 56 | Compared DAPD alone vs. DAPD + MMF added to antiretroviral regimens in treatment-experienced HIV patients. |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | Terminated | 8 | Compared cyclosporine + MMF vs. cyclophosphamide + prednisolone for anti-r-HuEpo associated PRCA; not an HIV-specific trial. |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | Completed | 5 | Allogeneic HSCT with post-transplant cyclosporine + MMF to induce mixed hematopoietic chimerism in HIV-1 infected patients. |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 1/2 | Withdrawn | 0 | Designed to test MMF added to abacavir in heavily ART-experienced patients with treatment failure; withdrawn before any enrollment. |
| [NCT06869265](https://clinicaltrials.gov/study/NCT06869265) | Phase 2 | Recruiting | 56 | Thiotepa/busulfan/fludarabine conditioning for haplo-HSCT in elderly high-risk AML; not HIV-related, MMF not the primary intervention. |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | Unknown | 90 | Substudy of the MAN2 trial evaluating MMF's effect on cardiovascular disease surrogate markers in HIV-1 infected patients. |
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | Unknown | 90 | MAN2 study: MMF vs. control in ART-naive chronic HIV-1 patients, assessing immune hyperactivation, CD4+ count decline, and plasma HIV-1 RNA. |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | Completed | 80 | HLA-mismatched unrelated donor BMT with post-transplant cyclophosphamide, sirolimus, and MMF for GVHD prophylaxis in hematologic malignancies; not HIV-related. |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | Completed | 10 | Renal transplantation safety/efficacy study in HIV-infected ESRD patients, using standard immunosuppression including MMF. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | Randomized pilot study | J Acquir Immune Defic Syndr | MMF added during structured HAART interruption in chronic HIV; assessed immune response and lymphatic tissue viral load during/after ART discontinuation. |
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | Clinical study | AIDS | Investigated whether MMF added to HAART affects plasma HIV-1 RNA decay rate and the latent reservoir in treatment-naive patients. |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | Cohort/Clinical | J Acquir Immune Defic Syndr | MMF added to abacavir-containing ART depleted intracellular dGTP and was associated with decreased plasma HIV-1 RNA in 5 heavily pretreated patients. |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | Pilot study | J Acquir Immune Defic Syndr | Open-label pilot of MMF + ABC/ddI/APV/RTV in 7 patients with multidrug-resistant HIV-1; therapy was well tolerated. |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | Clinical study | AIDS | Evaluated safety, tolerability, and antiretroviral activity of DAPD (amdoxovir) with or without MMF in drug-resistant HIV-1 infection. |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | PK study | Clin Pharmacokinet | Characterized PK/PD of low-dose MMF combined with abacavir, efavirenz, and nelfinavir in HIV-infected patients. |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Cohort | AIDS Res Hum Retroviruses | Found no detrimental immunological effects of adding MMF to HAART in treatment-naive acute/chronic HIV-1 patients. |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | PK study | Clin Pharmacokinet | Examined MMF's effect on antiretroviral drug pharmacokinetics and intracellular nucleoside triphosphate pools. |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | Reviewed immunosuppressive drug strategies, including MMF, targeting chronic immune activation in HIV disease progression. |
| [39515757](https://pubmed.ncbi.nlm.nih.gov/39515757/) | 2025 | Registry analysis | Am J Transplant | Long-term outcomes of induction immunosuppression (tacrolimus/MMF maintenance) in kidney transplant recipients with HIV, comparing r-ATG vs. IL2Ra induction. |

---

## EU Market Information

No marketing authorizations are recorded for mycophenolate mofetil in this evidence pack (market status: **Not Marketed**, 0 authorizations).

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note:** A Blocking-severity data gap (DG001) was identified — TFDA/regulatory label warnings and contraindications could not be retrieved, which means this candidate **cannot currently pass the S1 safety initial screening stage**. This gap must be resolved before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking-severity safety data gap (DG001: warnings/contraindications unavailable) prevents this candidate from entering the S1 safety screening stage, regardless of efficacy evidence.
- Although mechanistic plausibility and several small PK/cohort/pilot studies (early 2000s) suggest MMF may modulate HIV-related immune activation and potentiate certain NRTIs, the two trials designed specifically to test this hypothesis (MAN2 and its substudy) remain in "Unknown" status with no reported results, and the sole targeted efficacy trial (NCT00021489) was withdrawn before enrollment.

**To proceed, the following is needed:**
- Obtain TFDA/EU SmPC warnings, contraindications, and DDI data (resolve DG001, Blocking)
- Obtain confirmed mechanism of action record from DrugBank (resolve DG002, High)
- Determine actual outcomes of the MAN2 study (NCT00120419) and its cardiovascular substudy (NCT00247494), both currently "Unknown" status
- Clarify current regulatory/market status, since this product is listed as "Not Marketed" with zero authorizations in the evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

