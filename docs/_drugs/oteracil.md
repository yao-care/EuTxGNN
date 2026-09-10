---
layout: default
title: Oteracil
parent: 僅模型預測 (L5)
nav_order: 441
evidence_level: L5
indication_count: 10
---

# Oteracil
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

# Oteracil: From Gastric Cancer to Colonic Neoplasm

## One-Sentence Summary

> Oteracil is a component of the S-1 combination, originally used for gastric cancer treatment.
> The TxGNN model predicts it may be effective for **Colonic Neoplasm**,
> with **8 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric cancer (as component of the S-1 combination) |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for oteracil itself (potassium oxonate). Based on known information, oteracil is one of three components of the S-1 combination (tegafur + gimeracil + oteracil). Tegafur is a 5-FU prodrug; gimeracil inhibits dihydropyrimidine dehydrogenase (DPD) to prolong 5-FU exposure; oteracil selectively inhibits orotate phosphoribosyltransferase (OPRT) in the gastrointestinal tract, which reduces phosphorylation of 5-FU locally in the gut and thereby lowers GI toxicity without compromising systemic antitumor activity.

Gastric cancer and colonic neoplasm are both gastrointestinal malignancies with a shared pharmacological rationale for fluoropyrimidine-based chemotherapy. Since oteracil's role is specifically to protect the GI mucosa from 5-FU-related toxicity, this mechanism is directly relevant to colorectal tumors, which arise from the same GI epithelium. This mechanistic plausibility is reinforced by the fact that S-1 (the combination oteracil belongs to) has already been extensively studied and used as adjuvant and metastatic-setting chemotherapy for colon and rectal cancer in Japan and other Asian countries, which is exactly what the clinical trial and literature evidence below confirms.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO trial: S-1 vs capecitabine ± bevacizumab as first-line treatment for metastatic colorectal cancer. |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | UFT+leucovorin vs S-1 (TS-1) as adjuvant treatment for stage III colon cancer, with gene-expression predictive factor analysis. |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1191 | SOX (oxaliplatin + S-1) vs XELOX as adjuvant chemotherapy for stage III colorectal cancer, aiming to reduce hand-foot syndrome. |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | Unknown | 42 | S-1 + oral leucovorin + oxaliplatin (SOL) combination in untreated metastatic colorectal cancer. |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Terminated | 20 | S-1 and capecitabine + oxaliplatin compared for cardiotoxicity (coronary flow) in metastatic GI adenocarcinoma. |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + bevacizumab in unresectable/recurrent colorectal cancer after irinotecan/oxaliplatin failure. |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unknown | 82 | Raltitrexed + S-1 in metastatic colorectal cancer after failure of standard chemotherapy. |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Not yet recruiting | 52 | Fuquinitinib + S-1 (tegafur/gimeracil/oteracil) as third-line treatment for advanced metastatic CRC. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02 phase III trial: SOX superior to UFT/LV as adjuvant chemotherapy in high-risk stage III colon cancer. |
| [27056996](https://pubmed.ncbi.nlm.nih.gov/27056996/) | 2016 | RCT | Ann Oncol | ACTS-RC (JFMC35-C1) phase III trial comparing S-1 vs UFT as adjuvant chemotherapy for stage II/III rectal cancer. |
| [24942277](https://pubmed.ncbi.nlm.nih.gov/24942277/) | 2014 | RCT | Ann Oncol | ACTS-CC phase III trial: S-1 non-inferior to UFT/LV as adjuvant chemotherapy for stage III colon cancer. |
| [22415232](https://pubmed.ncbi.nlm.nih.gov/22415232/) | 2012 | RCT | Br J Cancer | Planned safety analysis of the ACTS-CC phase III trial (S-1 vs UFT/LV) in stage III colon cancer. |
| [32189156](https://pubmed.ncbi.nlm.nih.gov/32189156/) | 2020 | RCT | Int J Clin Oncol | KSCC1303 trial: 3-year disease-free survival results of S-1 + oxaliplatin (C-SOX) in stage III colon cancer. |
| [26036466](https://pubmed.ncbi.nlm.nih.gov/26036466/) | 2015 | RCT | BMC Cancer | Randomized phase II study comparing S-1 dosing schedules for resected colorectal cancer to improve completion rate. |
| [23320901](https://pubmed.ncbi.nlm.nih.gov/23320901/) | 2013 | RCT Protocol | Trials | Study protocol for a randomized trial on optimal adjuvant S-1 dosing schedule in stage III colon cancer. |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review | Clin Colorectal Cancer | Asian consensus adapting international guidelines for metastatic colorectal cancer management. |
| [17496461](https://pubmed.ncbi.nlm.nih.gov/17496461/) | 2007 | Review | Gan To Kagaku Ryoho | Review of adjuvant chemotherapy for colorectal cancer in Japan, including oral fluoropyrimidine use. |
| [12833857](https://pubmed.ncbi.nlm.nih.gov/12833857/) | 2003 | Review | Nihon Shokakibyo Gakkai Zasshi | Review of recent advances in chemotherapy for digestive cancers, including gastric and colonic cancer. |

---

## EU Market Information

Oteracil currently has **no marketing authorization records** in the EU market. The drug is only known internationally as a component of the S-1 combination product; no EU authorization data is available in this evidence pack for it as a standalone or combination entity.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic combination agent — fluoropyrimidine class (component of S-1: tegafur/gimeracil/oteracil) |
| Myelosuppression Risk | Medium — literature reports include neutropenia in phase III safety analyses (PMID 22415232) alongside other class-related toxicities (hand-foot syndrome, erythroderma – PMID 28414195; hypertriglyceridemia – PMID 32936722) |
| Emetogenicity Classification | Low to moderate — oteracil's OPRT-inhibiting action is specifically designed to reduce GI toxicity of 5-FU/tegafur |
| Monitoring Items | CBC with differential, liver and renal function, triglycerides, skin/mucosal assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations, as a component of an antineoplastic combination regimen |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Clinical trial and literature evidence for oteracil (as part of S-1) in colorectal/colonic neoplasm indications is strong (L1: ≥2 completed Phase 3 RCTs plus multiple published Phase III trials such as ACTS-CC, ACTS-CC02, ACTS-RC, KSCC1303). However, a **Blocking** data gap exists — TFDA/EMA label warnings and contraindications are unavailable, which prevents completion of the mandatory S1 safety review, and the drug currently has no EU marketing authorization on record.

**To proceed, the following is needed:**
- Obtain SmPC/label warnings and contraindications (DG001, Blocking)
- Obtain detailed mechanism of action data via DrugBank API (DG002)
- Clarify EU marketing authorization status for S-1 combination products containing oteracil
- Confirm route/dosage form compatibility once regulatory data is available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

