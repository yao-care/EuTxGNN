---
layout: default
title: Enzalutamide
parent: AI Predictions (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Enzalutamide: predicted new indication Prostate neoplasm (evidence level L5). Approved use: Prostate cancer (BCR nmHSPC, mHSPC, nmCRPC and mCRPC)"
monitor_inn: "Enzalutamide"
predicted_indications: ["prostate leiomyoma", "Brenner tumor", "fibroma of prostate", "benign reproductive system neoplasm", "benign prostate phyllodes tumor", "benign neoplasm of prostate", "prostate phyllodes tumor"]
---

# Enzalutamide
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

# Enzalutamide: From Prostate Cancer to Prostate Neoplasm (Benign and Malignant Prostate Tumours)

## One-Sentence Summary

Enzalutamide is an androgen receptor inhibitor, originally used to treat prostate cancer across several disease stages.
The TxGNN model's top-ranked predictions are mostly rare or very broad tumour terms with no supporting studies. The best-supported prediction is **Prostate Neoplasm** (score 98.4%), with **more than 30 registered clinical trials** and **20 publications**. However, this essentially restates the existing approved use rather than a new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (BCR nmHSPC, mHSPC, nmCRPC and mCRPC) |
| Predicted New Indication | Prostate neoplasm (the highest TxGNN-ranked term, "prostate cancer/brain cancer susceptibility", is a genetic susceptibility label and was not used) |
| TxGNN Prediction Score | 98.37% (prostate neoplasm); the top-ranked term scored 99.71% |
| Evidence Level | L1 (for prostate neoplasm, which equals the approved indication) |
| EU Market Status | Cancelled only (all licences cancelled) |
| Number of Authorizations | 3 |
| Recommended Decision | Proceed with Guardrails (confirmation of existing use, not true repurposing) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the retrieved literature, enzalutamide is a second-generation non-steroidal antiandrogen. It blocks androgen binding to the androgen receptor (AR), prevents its nuclear translocation, and prevents its binding to DNA.

"Prostate neoplasm" is a broad category that maps almost entirely onto prostate cancer, which is already the approved indication. The Phase 3 evidence therefore supports existing use. The model's higher-ranked predictions are not credible: prostate leiomyoma, fibroma of prostate, benign prostate phyllodes tumour, and Brenner tumour (an ovarian tumour) have no trials or literature, and no established androgen receptor-driven mechanism. The top term, "prostate cancer/brain cancer susceptibility", is a genetic label rather than a treatable disease.

For "benign neoplasm of prostate", androgen signalling is biologically plausible, but the available literature concerns prostate cancer, and no trials exist for benign disease.

---

## Clinical Trial Evidence

Trials listed are for the prostate neoplasm prediction (the most relevant subset, up to 10).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02446405](https://clinicaltrials.gov/study/NCT02446405) | Phase 3 | Active, not recruiting | 1125 | ENZAMET: enzalutamide vs conventional NSAA with first-line ADT in metastatic prostate cancer |
| [NCT06551324](https://clinicaltrials.gov/study/NCT06551324) | Phase 3 | Active, not recruiting | 600 | MEVPRO-1: mevrometostat plus enzalutamide vs enzalutamide or docetaxel in mCRPC after abiraterone |
| [NCT02987543](https://clinicaltrials.gov/study/NCT02987543) | Phase 3 | Completed | 387 | PROfound: olaparib vs enzalutamide or abiraterone in mCRPC with HRR mutations |
| [NCT03834493](https://clinicaltrials.gov/study/NCT03834493) | Phase 3 | Terminated | 1244 | KEYNOTE-641: pembrolizumab plus enzalutamide vs placebo plus enzalutamide in mCRPC |
| [NCT06136624](https://clinicaltrials.gov/study/NCT06136624) | Phase 3 | Recruiting | 1310 | OMAHA-003: opevesostat vs abiraterone or enzalutamide in heavily pretreated mCRPC |
| [NCT06496581](https://clinicaltrials.gov/study/NCT06496581) | Phase 3 | Recruiting | 500 | Standard of care ± 177Lu-PSMA-617 in poorly responding de novo mHSPC (enzalutamide indirect) |
| [NCT03641560](https://clinicaltrials.gov/study/NCT03641560) | Phase 4 | Completed | 52 | Single-arm safety and efficacy of enzalutamide in Indian mCRPC patients after docetaxel |
| [NCT06059118](https://clinicaltrials.gov/study/NCT06059118) | Phase 2 | Recruiting | 50 | DFMO and high-dose testosterone alternating with enzalutamide in mCRPC |
| [NCT07512076](https://clinicaltrials.gov/study/NCT07512076) | Phase 2 | Not yet recruiting | 26 | Enzalutamide dose optimisation in elderly patients with advanced prostate cancer |
| [NCT06228053](https://clinicaltrials.gov/study/NCT06228053) | Phase 2 | Recruiting | 53 | SX-682 plus enzalutamide in ARPI-resistant mCRPC |

All of these trials are in prostate cancer, the approved indication. None addresses benign prostatic tumours, rare prostate stromal tumours, or other organs' tumours.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31329516](https://pubmed.ncbi.nlm.nih.gov/31329516/) | 2019 | RCT | J Clin Oncol | ARCHES: enzalutamide plus ADT in mHSPC |
| [29949494](https://pubmed.ncbi.nlm.nih.gov/29949494/) | 2018 | RCT | N Engl J Med | Enzalutamide delays metastasis in nmCRPC with rapidly rising PSA |
| [22894553](https://pubmed.ncbi.nlm.nih.gov/22894553/) | 2012 | RCT | N Engl J Med | AFFIRM: increased survival after chemotherapy in CRPC |
| [41124201](https://pubmed.ncbi.nlm.nih.gov/41124201/) | 2026 | RCT | N Engl J Med | EMBARK final analysis: improved survival in biochemically recurrent prostate cancer |
| [42223064](https://pubmed.ncbi.nlm.nih.gov/42223064/) | 2026 | RCT | N Engl J Med | Talazoparib plus enzalutamide plus ADT in metastatic prostate cancer |
| [27477525](https://pubmed.ncbi.nlm.nih.gov/27477525/) | 2017 | RCT (extended) | Eur Urol | PREVAIL extended analysis in chemotherapy-naïve mCRPC |
| [41633900](https://pubmed.ncbi.nlm.nih.gov/41633900/) | 2026 | Post hoc analysis | Eur Urol | ARCHES 5-year survival with enzalutamide plus ADT |
| [39417629](https://pubmed.ncbi.nlm.nih.gov/39417629/) | 2025 | Multicentre comparison | Prostate | Real-world comparison of abiraterone, enzalutamide and apalutamide in mHSPC |
| [32534790](https://pubmed.ncbi.nlm.nih.gov/32534790/) | 2020 | Review | Trends Cancer | Treatment advances in advanced prostate cancer |
| [39275993](https://pubmed.ncbi.nlm.nih.gov/39275993/) | 2024 | Review | Expert Rev Anticancer Ther | Current uses and resistance mechanisms of enzalutamide |

---

## EU Market Information

All three authorisations are recorded as cancelled; there are currently no valid EU licences in the data compiled for this report.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002639 | Xtandi | Not specified | Adult men with BCR nmHSPC unsuitable for salvage radiotherapy, mHSPC, high-risk nmCRPC, and mCRPC (before and after docetaxel)... |
| EMEA/H/C/006299 | Enzalutamide Viatris | Not specified | Adult men with BCR nmHSPC unsuitable for salvage-radiotherapy, mHSPC, high-risk nmCRPC, and mCRPC... |
| EMEA/H/C/006612 | Enzalutamide Accordpharma | Not specified | Treatment of prostate cancer. |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (androgen receptor inhibitor); not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. Of the 20 reviewed, most are Moderate; **Major** interactions include bupropion, dolasetron and eliglustat. Moderate examples include omeprazole, rabeprazole, famotidine, dexamethasone, hydrocortisone, clarithromycin, aprepitant, loperamide, saxagliptin, empagliflozin and linagliptin.
- **Other considerations**: The data compiled for this report flags anti-androgen effects and seizure risk as concerns that would need weighing in any benign indication.

Warnings and contraindications from the label were not available. Please refer to the SmPC for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The only well-supported prediction ("prostate neoplasm") corresponds to prostate cancer, which is already the approved indication, backed by multiple Phase 3 RCTs (ARCHES, PROSPER-type nmCRPC, AFFIRM, PREVAIL, EMBARK). This confirms existing use rather than identifying a new indication. All higher-scoring novel predictions (rare benign prostate tumours, Brenner tumour, the susceptibility label) have no trials or literature and should stay on **Hold**.

**To proceed, the following is needed:**
- Reconcile the "Cancelled only" EU market status with Xtandi's known clinical use, and confirm the current authorisation status
- Mechanism of action data (currently missing)
- Label warnings and contraindications from the SmPC (currently missing)
- Pharmacist review of the Major interactions (bupropion, dolasetron, eliglustat) and CYP-related interactions
- For any benign prostate condition, dedicated studies and a benefit–risk assessment given anti-androgen effects and seizure risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

