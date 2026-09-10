---
layout: default
title: Glasdegib
parent: 僅模型預測 (L5)
nav_order: 277
evidence_level: L5
indication_count: 10
---

# Glasdegib
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

# Glasdegib: From Acute Myeloid Leukemia to Myelodysplastic/Myeloproliferative Disease

## One-Sentence Summary

> Glasdegib is a Smoothened (SMO) / Hedgehog pathway inhibitor originally developed and approved (in combination with low-dose cytarabine) for acute myeloid leukemia (AML).
> The TxGNN model predicts it may also be effective for **myelodysplastic/myeloproliferative disease (MDS/MPN)**,
> with **3 clinical trials** and **1 publication** currently supporting this direction.

*(Note: The single highest-scoring TxGNN hit, "bulbar polio," and several other top-ranked outputs were flagged by the evidence engine itself as biologically implausible / likely model noise — see "Why is This Prediction Reasonable?" below for how the MDS/MPN candidate was selected instead.)*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Myeloid Leukemia (AML), in combination with low-dose cytarabine (not TFDA-approved / not marketed in Taiwan) |
| Predicted New Indication | Myelodysplastic/Myeloproliferative Disease (MDS/MPN) |
| TxGNN Prediction Score | 96.76% |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation is not yet available for this evidence pack (marked as a High-severity data gap). Based on information embedded in the evidence itself, glasdegib (PF-04449913) is a Smoothened (SMO) receptor antagonist that inhibits Hedgehog pathway signaling — a pathway implicated in the self-renewal and chemoresistance of leukemic stem cells. It is already approved (in combination with low-dose cytarabine) for AML.

MDS/MPN and AML sit on the same myeloid stem-cell malignancy spectrum, sharing overlapping pathobiology (clonal hematopoietic stem/progenitor cell disorders with Hedgehog-pathway involvement in leukemic stem cell survival). This mechanistic continuity is why glasdegib's known AML activity plausibly extends to MDS/MPN, and it is reflected in real clinical development: glasdegib has been directly studied — alone and combined with azacitidine — in MDS and CMML populations.

By contrast, several other high-TxGNN-score outputs (bulbar polio, 5q35 microduplication syndrome, neuralgic/amyotrophic neuralgia, ganglioneuroblastoma) were assessed by the evidence pack's own rationale as having no known biological link to SMO/Hedgehog inhibition and are treated as likely model noise (Hold). Two AML/MDS subtypes related to prior alkylating-agent or radiation exposure, plus acute panmyelosis with myelofibrosis and bilineal AML, are mechanistically consistent with glasdegib's known biology but currently lack any subtype-specific trial or literature evidence (Research Question stage) — these are worth monitoring but are not yet actionable.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01842646](https://clinicaltrials.gov/study/NCT01842646) | Phase 2 | Completed | 35 | Single-arm study of oral SMO inhibitor glasdegib (PF-04449913) in relapsed/refractory MDS or CMML; evaluates safety and efficacy. |
| [NCT04842604](https://clinicaltrials.gov/study/NCT04842604) | Phase 3 | Completed | 14 | Open-label continuation study of azacitidine with or without glasdegib in previously untreated AML, MDS, or CMML patients continuing from prior studies. |
| [NCT02367456](https://clinicaltrials.gov/study/NCT02367456) | Phase 1 | Completed | 73 | Phase 1b study of glasdegib combined with azacitidine in previously untreated higher-risk MDS, AML, or CMML; evaluates safety, efficacy, PK and PD via a safety lead-in and expansion cohorts. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31030089](https://pubmed.ncbi.nlm.nih.gov/31030089/) | 2019 | Phase 2 Trial | Leukemia Research | Phase 2 trial of glasdegib in HMA-failure MDS (n=35, median age 73); Hedgehog pathway upregulation implicated in leukemic stem cell survival, with 54–77% of patients classified high-risk by IPSS/MD Anderson Global Risk Model. |

---

## EU Market Information

Glasdegib is currently **not marketed in Taiwan** (0 authorizations, market status: 未上市). No license or approved-indication data is available to tabulate.

---

## Cytotoxicity

Glasdegib is an antineoplastic agent (approved for AML, a hematologic malignancy).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (SMO/Hedgehog pathway inhibitor); typically administered with a conventional cytotoxic backbone (e.g., low-dose cytarabine or azacitidine) |
| Myelosuppression Risk | High — expected when combined with cytotoxic backbone therapy in myeloid malignancies; please refer to the SmPC for confirmed grading |
| Emetogenicity Classification | Low (oral small-molecule targeted agent); please refer to the SmPC for confirmed classification |
| Monitoring Items | CBC with differential, liver and renal function; ECG/QTc monitoring is a class consideration for SMO inhibitors and should be confirmed against the SmPC |
| Handling Protection | As an antineoplastic agent, handling should follow institutional hazardous-drug protocols; refer to SmPC/safety data sheet for specifics |

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack; the DDI query returned no results.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Glasdegib's approved AML mechanism (SMO/Hedgehog inhibition targeting leukemic stem cells) extends plausibly to MDS/MPN, and this is supported by three completed early-phase trials and one published Phase 2 study — but none are confirmatory randomized Phase 2/3 trials, and safety/label data remain unavailable.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently a Blocking data gap — required before any S1 safety assessment)
- Verified mechanism-of-action documentation (High-severity data gap)
- A confirmatory randomized trial in MDS/MPN specifically (existing trials are single-arm or small continuation studies)
- Drug-drug interaction data (current DDI query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

