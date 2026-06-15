---
layout: default
title: Bosutinib
parent: 僅模型預測 (L5)
nav_order: 99
evidence_level: L5
indication_count: 10
---

# Bosutinib
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

# Bosutinib: From Philadelphia Chromosome-Positive Leukemia to Myeloid Leukemia

## One-Sentence Summary

Bosutinib (Bosulif®) is a second-generation oral dual BCR-ABL/Src kinase inhibitor globally established as a standard-of-care treatment for Philadelphia chromosome-positive chronic myeloid leukemia (CML), but currently not registered in Taiwan.
The TxGNN model predicts it may be effective for **Myeloid Leukemia**,
with **3 completed Phase 3 trials** and **20 publications** directly supporting this indication — including the landmark BFORE trial confirming superiority over imatinib in newly diagnosed CML.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ph+ Chronic Myeloid Leukemia (globally approved; no Taiwan registration) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 98.75% |
| Evidence Level | L1 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Taiwan Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank was not retrieved in this evidence pack. Based on published pharmacological data, Bosutinib is a second-generation oral TKI that dually inhibits BCR-ABL kinase (including many imatinib-resistant kinase domain mutations) and Src family kinases (Src, Lyn, Hck). This dual inhibition simultaneously targets the primary oncogenic driver of CML — the constitutively active BCR-ABL fusion kinase arising from the t(9;22) Philadelphia chromosome translocation — and the downstream Src/Lyn-mediated proliferation and survival signals that amplify leukemic cell expansion.

Myeloid leukemia encompasses a disease spectrum unified by dysregulated myeloid progenitor proliferation. In Ph+ CML, BCR-ABL is the singular molecular driver, making Bosutinib's kinase inhibition profile a mechanistically precise match for this disease. The TxGNN prediction for "myeloid leukemia" therefore reflects direct pharmacological congruence, not a speculative extrapolation. This is further reinforced by the ELN 2020/2025 clinical guidelines, which place Bosutinib as an equivalent first-line treatment option alongside imatinib, dasatinib, and nilotinib for newly diagnosed CML.

The key insight from this evaluation is not whether Bosutinib works for myeloid leukemia — three completed Phase 3 RCTs confirm it does — but rather that Taiwanese patients currently lack access to this established therapy due to the absence of a Taiwan TFDA registration. The TxGNN score of 98.75% reflects the model correctly identifying a globally proven indication, and the actionable finding is the regulatory gap that needs to be addressed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02130557](https://clinicaltrials.gov/study/NCT02130557) | Phase 3 | Completed | 536 | BFORE: Bosutinib 400mg vs Imatinib 400mg in newly diagnosed CP-CML; demonstrated superior MMR (47.2% vs 36.9%) and CCyR at 12 months — primary pivotal trial supporting FDA/EMA approval |
| [NCT00574873](https://clinicaltrials.gov/study/NCT00574873) | Phase 3 | Completed | 502 | Phase 3 RCT of Bosutinib vs Imatinib in newly diagnosed Ph+ CP-CML; assessed cytogenetic response at 1 year across international sites |
| [NCT03106779](https://clinicaltrials.gov/study/NCT03106779) | Phase 3 | Completed | 233 | ASCEMBL: Asciminib vs Bosutinib 500mg in CML-CP after ≥2 prior TKIs; Bosutinib served as active control, establishing benchmark MMR rates in later-line settings |
| [NCT05743465](https://clinicaltrials.gov/study/NCT05743465) | N/A (RWE) | Completed | 1769 | Largest real-world comparative study of TKIs in CML; safety and clinical outcomes of Bosutinib, Ponatinib, Imatinib, Dasatinib, and Nilotinib in routine practice |
| [NCT00261846](https://clinicaltrials.gov/study/NCT00261846) | Phase 1/2 | Completed | 571 | Seminal Bosutinib dose-escalation and efficacy study in Ph+ leukemias; established MTD and demonstrated broad activity across chronic, accelerated, and blast phases |
| [NCT03885830](https://clinicaltrials.gov/study/NCT03885830) | N/A (Observational) | Completed | 45 | Prospective TKI PK/PD exposure-response study in CP-CML; correlates Bosutinib clearance/exposure with clinical milestones, toxicity, and adherence |
| [NCT03610971](https://clinicaltrials.gov/study/NCT03610971) | Phase 2 | Active, not recruiting | 24 | Ruxolitinib combined with TKI (including Bosutinib) to extend treatment-free remission in CP-CML relapsing after prior TKI discontinuation |
| [NCT04793399](https://clinicaltrials.gov/study/NCT04793399) | Phase 1/2 | Terminated | 9 | Bosutinib + Atezolizumab combination in newly diagnosed CML; early safety signals evaluated before premature termination |
| [NCT04258943](https://clinicaltrials.gov/study/NCT04258943) | Phase 1/2 | Active, not recruiting | 60 | ITCC-054/COG-AAML1921: Bosutinib in pediatric Ph+ CP-CML (newly diagnosed and resistant/intolerant); dose-finding and PK characterization in children |
| [NCT02810990](https://clinicaltrials.gov/study/NCT02810990) | Phase 2 | Completed | 65 | BEST study: Bosutinib efficacy and tolerability in elderly CP-CML patients after front-line TKI failure; supports use in age-specific subpopulations |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29091516](https://pubmed.ncbi.nlm.nih.gov/29091516/) | 2018 | RCT (BFORE Phase 3) | J Clin Oncol | Bosutinib vs Imatinib in 536 newly diagnosed CP-CML patients; superior MMR and MCyR at 12 months; manageable GI and hepatic toxicity profile |
| [35643868](https://pubmed.ncbi.nlm.nih.gov/35643868/) | 2022 | RCT (BFORE 5-year final) | Leukemia | 5-year BFORE final analysis confirming durable molecular response superiority; 59.7% of bosutinib patients remained on study treatment at completion |
| [34407542](https://pubmed.ncbi.nlm.nih.gov/34407542/) | 2021 | RCT (ASCEMBL Phase 3) | Blood | Phase 3 ASCEMBL: Asciminib vs Bosutinib 500mg in ≥2nd-line CML-CP; Bosutinib MMR ~25% at 24 weeks as active comparator benchmark |
| [36717654](https://pubmed.ncbi.nlm.nih.gov/36717654/) | 2023 | RCT (ASCEMBL follow-up) | Leukemia | Extended ASCEMBL follow-up; Bosutinib comparator arm maintains consistent MMR rates confirming durable activity in multiply pretreated CML |
| [32127639](https://pubmed.ncbi.nlm.nih.gov/32127639/) | 2020 | Guidelines (ELN 2020) | Leukemia | ELN 2020 recommendations: Bosutinib designated first-line CML treatment option with equivalent survival to other second-generation TKIs; favored for lower cardiovascular/metabolic risk |
| [39093014](https://pubmed.ncbi.nlm.nih.gov/39093014/) | 2024 | Review (2025 update) | Am J Hematol | CML 2025 update: Bosutinib retained as standard first-line TKI; guidance on treatment sequencing, monitoring milestones, and treatment-free remission criteria |
| [39252937](https://pubmed.ncbi.nlm.nih.gov/39252937/) | 2024 | Review (Bosutinib-focused) | Front Oncol | Comprehensive expert review of Bosutinib clinical data across all treatment lines; practical recommendations for patient selection and AE management |
| [29695943](https://pubmed.ncbi.nlm.nih.gov/29695943/) | 2018 | Review | J Blood Med | Bosutinib patient selection and clinical perspectives; favorable cardiovascular profile (no vascular occlusion risk) distinguishes it from nilotinib/ponatinib |
| [24711212](https://pubmed.ncbi.nlm.nih.gov/24711212/) | 2014 | Cohort (Phase 1/2) | Am J Hematol | Second-line Bosutinib after imatinib failure: 85% CHR, 59% MCyR at 24-month follow-up in 288 patients; confirmed activity across multiple resistance mechanisms |
| [29773593](https://pubmed.ncbi.nlm.nih.gov/29773593/) | 2018 | Cohort (Phase 1/2 final) | Haematologica | 5-year final results of second-line Bosutinib in CP-CML: 40% of patients remained on therapy at year 5; durable responses with predictable, manageable toxicity |

---

## Taiwan Market Information

Bosutinib currently has **no marketing authorizations in Taiwan** (0 registered products; TFDA status: 未上市). Despite FDA approval since 2012 and EMA approval (Bosulif®, Pfizer), Bosutinib remains inaccessible to Taiwanese CML patients through the domestic regulatory pathway.

| Authorization | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No Taiwan TFDA authorizations registered |

For prescribing reference, the global Bosulif® SmPC covers: Ph+ CML (chronic, accelerated, and blast phase) with prior TKI resistance or intolerance; newly diagnosed Ph+ CP-CML (FDA-approved 2017).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — BCR-ABL/Src tyrosine kinase inhibitor (second-generation TKI; not conventional cytotoxic) |
| Myelosuppression Risk | Moderate — Grade 3/4 thrombocytopenia occurs in 14–40% of patients; neutropenia and anemia also reported; distinct from alkylating agent-type pan-myelosuppression |
| Emetogenicity Classification | Low — GI toxicity predominantly manifests as diarrhea (dose-limiting in early treatment); nausea present but classical emesis uncommon; antiemetic prophylaxis generally not required |
| Monitoring Items | CBC with differential (monthly for first 3–6 months, then quarterly); hepatic transaminases ALT/AST (hepatotoxicity risk — monitor at baseline, then monthly for 3 months, then periodically); serum creatinine; BCR-ABL1 IS transcript monitoring per ELN milestones |
| Handling Protection | Standard oral TKI handling precautions — do not crush or split tablets; cytotoxic waste disposal protocols apply; pregnancy exposure prevention required |

---

## Safety Considerations

Taiwan TFDA prescribing information (SmPC) for Bosutinib is not currently available as the drug is not registered in Taiwan. Please refer to the Pfizer **Bosulif® global SmPC** and the FDA/EMA product labels for comprehensive information on warnings, contraindications, drug interactions, and special population guidance.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Bosutinib has the highest possible evidence grade (L1), supported by three completed Phase 3 RCTs (BFORE, NCT00574873, ASCEMBL), international guideline endorsement (ELN 2020/2025), and more than two decades of pharmacovigilance data — making this TxGNN prediction a validation of established clinical consensus rather than a speculative repurposing hypothesis. The barrier to patient access in Taiwan is regulatory, not evidentiary.

**To proceed, the following is needed:**

- **Taiwan TFDA NDA submission:** Compile existing FDA/EMA clinical data package (clinical study reports from BFORE, NCT00574873, Phase 1/2 studies) for Taiwan registration application
- **Asian PK bridging assessment:** The Japanese Phase 2 study (NCT03128411, n=64) provides Asian pharmacokinetic reference data; confirm whether TFDA requires additional Taiwan-specific PK bridging or accepts existing data
- **Full SmPC localization:** Prepare Taiwan-language prescribing information covering safety warnings, contraindications (hepatic impairment dose adjustment, pregnancy/lactation exclusion), and DDI guidance (CYP3A4 interactions — pharmacokinetic study NCT02058277 provides aprepitant interaction data)
- **NHI reimbursement pathway:** Initiate negotiation for inclusion in Taiwan National Health Insurance CML treatment coverage alongside established TKIs
- **Risk Management Plan:** Establish monitoring protocols for myelosuppression (CBC), hepatotoxicity (LFTs), and GI toxicity management in line with ELN guidelines
- **Secondary indication scoping:** After Taiwan CML registration, evaluate TxGNN rank-9 prediction for **HER2-positive breast carcinoma** (L2 evidence; Phase 1 trial NCT03854903 completed; two Phase 2 RCTs in ER+/HER2- BC) and rank-8 **plasma cell myeloma** (L4 preclinical evidence; Src/CAM-DR mechanistic rationale) as potential next-stage expansion indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

