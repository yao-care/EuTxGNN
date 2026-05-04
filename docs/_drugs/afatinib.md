---
layout: default
title: Afatinib
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 10
---

# Afatinib
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

# Afatinib: From Non-Small Cell Lung Cancer to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Afatinib is an irreversible, covalent pan-ErbB kinase inhibitor approved for EGFR mutation-positive non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **HER2 Positive Breast Carcinoma**,
with **10 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | EGFR mutation-positive NSCLC (no Taiwan regulatory record available) |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 98.65% |
| Evidence Level | L1 |
| Market Status | Not marketed (no regulatory record on file) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Afatinib is an irreversible, covalent inhibitor that simultaneously blocks all four members of the ErbB receptor family — EGFR (HER1), HER2 (ErbB2), HER3, and HER4 — by binding covalently to the ATP-binding pocket of their intracellular kinase domains. This pan-ErbB blockade distinguishes afatinib from first-generation reversible EGFR inhibitors (erlotinib, gefitinib), and its mechanism is also broader than trastuzumab, which binds solely to the extracellular domain of HER2. Although detailed MOA data is not yet available from DrugBank for this report, the drug's established clinical activity in NSCLC — a cancer driven by ErbB-family signaling — provides a strong mechanistic foundation.

In HER2-overexpressing breast cancer, amplified HER2 drives cell proliferation primarily through the RAS–MAPK and PI3K–AKT cascades. Afatinib directly suppresses HER2 kinase activity and simultaneously blocks HER2 homo- and heterodimerization with EGFR and HER3 — a key mechanism that may overcome trastuzumab resistance arising from alternative HER-family co-signaling. Furthermore, afatinib's demonstrated ability to penetrate the blood-brain barrier makes it particularly relevant for the subset of HER2-positive patients who develop CNS metastases, a population with very limited treatment options.

The relationship between Afatinib's original indication (NSCLC, EGFR-driven) and HER2-positive breast cancer is one of shared oncogenic family membership: both diseases are driven by dysregulated ErbB-receptor kinase activity. The entire LUX-Breast clinical program (Phases 1–3) was designed explicitly to test whether pan-ErbB inhibition translates from lung to breast cancer, validating the TxGNN model's mechanistic reasoning.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01125566](https://clinicaltrials.gov/study/NCT01125566) | Phase 3 | Completed | 508 | LUX-Breast 1: afatinib+vinorelbine vs. trastuzumab+vinorelbine in HER2-overexpressing metastatic BC after one prior trastuzumab regimen; primary PFS endpoint not met vs. comparator, but comprehensive efficacy and safety data generated across a large randomized population |
| [NCT01441596](https://clinicaltrials.gov/study/NCT01441596) | Phase 2 | Completed | 121 | LUX-Breast 3: randomized comparison of afatinib alone or with vinorelbine vs. investigator's choice in HER2+ BC with progressive brain metastases after trastuzumab and/or lapatinib; supports CNS-penetrant activity |
| [NCT01594177](https://clinicaltrials.gov/study/NCT01594177) | Phase 2 | Completed | 65 | Dual HER2 blockade (afatinib+trastuzumab) as neoadjuvant treatment alongside taxane-anthracycline chemotherapy; achieved a pathological complete response (pCR) rate of approximately 49%, supporting combination feasibility |
| [NCT04158947](https://clinicaltrials.gov/study/NCT04158947) | Phase 2 | Unknown | 130 | Randomized afatinib+T-DM1 vs. T-DM1 alone in HER2+ BC patients with active refractory brain metastases; Phase I dose-finding completed, Phase II efficacy results pending |
| [NCT00950742](https://clinicaltrials.gov/study/NCT00950742) | Phase 1 | Completed | 18 | Established the maximum tolerated dose (MTD) of afatinib in combination with trastuzumab in HER2+ advanced BC; foundational pharmacokinetic and safety data underpinning all subsequent combination studies |
| [NCT02438722](https://clinicaltrials.gov/study/NCT02438722) | Phase 2/3 | Active, not recruiting | 174 | Afatinib+cetuximab vs. afatinib alone in EGFR-mutated NSCLC; provides mechanistic data on dual ErbB blockade strategy applicable to breast cancer combination development |
| [NCT00826267](https://clinicaltrials.gov/study/NCT00826267) | Phase 2 | Completed | 29 | Three-arm randomized neoadjuvant study comparing afatinib vs. trastuzumab vs. lapatinib as single agents in HER2+ stage IIIa locally advanced BC; head-to-head pharmacodynamic comparison |
| [NCT00431067](https://clinicaltrials.gov/study/NCT00431067) | Phase 2 | Completed | 41 | Afatinib monotherapy in HER2+ metastatic BC after trastuzumab-containing regimen failure; directly characterizes efficacy in a trastuzumab-refractory population |
| [NCT01320280](https://clinicaltrials.gov/study/NCT01320280) | Phase 2 | Terminated | 29 | Afatinib in HER2+ hormone-refractory prostate cancer after docetaxel failure; terminated early with incomplete efficacy data, but provides cross-tumor HER2-targeted safety reference |
| [NCT01531764](https://clinicaltrials.gov/study/NCT01531764) | Phase 2 | Terminated | 2 | Afatinib+vinorelbine in intermediate HER2-expression (IHC 2+/FISH-negative) metastatic BC; terminated almost immediately (n=2), no meaningful efficacy data available |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [35138529](https://pubmed.ncbi.nlm.nih.gov/35138529/) | 2022 | Phase 2 Trial | Breast Cancer Research and Treatment | LUX-Breast 2: afatinib monotherapy or in combination with vinorelbine/paclitaxel in HER2+ BC after prior trastuzumab/lapatinib failure; evaluates sequential strategy in trastuzumab-refractory advanced disease |
| [38367127](https://pubmed.ncbi.nlm.nih.gov/38367127/) | 2024 | Comparative Study | Clinical & Experimental Metastasis | Established a novel multi-drug-resistant HER2+ BC lung metastasis model; compared T-DM1, T-DXd, and disitamab vedotin, providing the preclinical context for next-line options post-afatinib |
| [35653982](https://pubmed.ncbi.nlm.nih.gov/35653982/) | 2022 | Meta-analysis | ESMO Open | Systematic review and meta-analysis assessing TKI-containing vs. non-TKI-containing regimens in HER2+ MBC with brain metastases; afatinib is a key comparator, supporting CNS-targeted use |
| [33122343](https://pubmed.ncbi.nlm.nih.gov/33122343/) | 2021 | Preclinical/Mechanistic | Clinical Cancer Research | Afatinib enhances antibody-dependent cell-mediated cytotoxicity (ADCC) in HER2-expressing BC in combination with trastuzumab; mechanistic support for the synergy hypothesis |
| [24080156](https://pubmed.ncbi.nlm.nih.gov/24080156/) | 2014 | Systematic Review | Cancer Treatment Reviews | Systematic review of dual HER2 targeting strategies in HER2+ BC; provides the evidence framework within which afatinib combination approaches were developed |
| [29772459](https://pubmed.ncbi.nlm.nih.gov/29772459/) | 2018 | Review | Cancer Treatment Reviews | Reviews TKIs for CNS metastases in HER2+ BC; highlights afatinib's blood-brain barrier penetration and summarizes clinical data from LUX-Breast 3 |
| [24870559](https://pubmed.ncbi.nlm.nih.gov/24870559/) | 2014 | Review | Expert Opinion on Investigational Drugs | Comprehensive review of afatinib's development in breast cancer; contextualizes LUX-Breast program results within the broader anti-HER2 resistance landscape |
| [30350178](https://pubmed.ncbi.nlm.nih.gov/30350178/) | 2018 | Phase 1 Trial | Cancer Chemotherapy and Pharmacology | Phase I trial of afatinib with 3-weekly trastuzumab including optimized anti-diarrheal management; defines feasible dosing for the combination in HER2+ metastatic cancer |
| [29604436](https://pubmed.ncbi.nlm.nih.gov/29604436/) | 2018 | Review | Pharmacological Research | Reviews novel pharmacokinetic strategies for BC brain metastases; positions afatinib among CNS-active investigational agents alongside other small molecules |
| [22305205](https://pubmed.ncbi.nlm.nih.gov/22305205/) | 2012 | Review | Cancer Treatment Reviews | Early landscape review of emerging HER2-targeted therapies; provides historical context for afatinib's clinical development relative to trastuzumab and lapatinib |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — irreversible pan-ErbB/HER family tyrosine kinase inhibitor (not conventional cytotoxic) |
| Myelosuppression Risk | Low (TKI class; myelosuppression is not a primary toxicity compared to conventional chemotherapy) |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function (ALT/AST/bilirubin), renal function, CBC, dermatologic toxicity (acneiform rash, paronychia, dry skin), gastrointestinal toxicity (diarrhea — most common dose-limiting toxicity), pulmonary function (interstitial lung disease risk) |
| Handling Protection | Standard oral antineoplastic handling precautions; full cytotoxic compounding protocols are not required |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Afatinib has been evaluated in one completed Phase 3 RCT (LUX-Breast 1, n=508) and at least five completed Phase 2 trials specifically in HER2-positive breast cancer, generating a robust body of L1-level clinical evidence. Although LUX-Breast 1 did not demonstrate superiority over trastuzumab on the primary PFS endpoint in an unselected population, afatinib showed clinically meaningful activity — particularly in trastuzumab-refractory patients and those with CNS metastases — supporting a precision-indication approach rather than broad-line substitution.

**To proceed, the following is needed:**

- Retrieve full MOA data from DrugBank to complete the mechanistic assessment (Data Gap DG002)
- Review the full SmPC or prescribing information for contraindications, black-box warnings, and drug interactions (Data Gap DG001)
- Define the target subpopulation most likely to benefit: trastuzumab-refractory HER2+ MBC, or HER2+ MBC with active brain metastases (where afatinib's CNS penetration provides differentiated value)
- Benchmark afatinib's positioning against current standard-of-care regimens (T-DM1, trastuzumab deruxtecan/T-DXd, tucatinib-based therapy) to identify a clinically viable niche
- Design a prospective safety monitoring plan covering the major toxicity domains: diarrhea management, hepatotoxicity surveillance, dermatologic toxicity, and ILD monitoring protocols
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

