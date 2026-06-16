---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

# Cabazitaxel: From Metastatic Prostate Cancer to Female Breast Carcinoma

## One-Sentence Summary

Cabazitaxel is a next-generation taxane microtubule stabilizer, initially approved by the FDA for docetaxel-refractory metastatic castration-resistant prostate cancer (mCRPC).
The TxGNN model predicts it may be effective for **female breast carcinoma**,
with **0 registered clinical trials** (in this query set) but **20 publications** — including 1 Phase II RCT and 1 Phase I/II dose-escalation trial — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic castration-resistant prostate cancer (FDA-approved; not marketed in Taiwan) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cabazitaxel belongs to the taxane class of microtubule-stabilizing agents, sharing its core mechanism with paclitaxel and docetaxel — both of which are cornerstones of breast cancer chemotherapy. Its defining pharmacological advantage over docetaxel is a markedly lower affinity for P-glycoprotein (Pgp), the ATP-dependent efflux pump that drives taxane resistance in many tumor types. This property allows cabazitaxel to retain cytotoxic activity in cell lines and tumors where docetaxel has failed.

Breast cancer and prostate cancer, though anatomically distinct, are both hormone-sensitive solid tumors that frequently evolve taxane resistance through overlapping Pgp-mediated mechanisms. High expression of βIII-tubulin — a resistance-conferring isotype — is especially prominent in triple-negative breast cancer (TNBC), and published biochemical data (PMID 28567478) demonstrate that cabazitaxel outperforms docetaxel precisely in this βIII-tubulin-high context, providing direct mechanistic rationale for the TxGNN prediction. Additionally, cabazitaxel has been shown to reprogram tumor-associated macrophages (TAMs), augmenting the efficacy of CD47-targeted immunotherapy in TNBC preclinical models (PMID 33753567), suggesting immunomodulatory activity beyond direct cytotoxicity.

Formal clinical investigation of this repurposing hypothesis has already begun: the Phase II GENEVIEVE trial directly compared cabazitaxel versus weekly paclitaxel as neoadjuvant therapy in HER2-negative breast cancer (PMID 28768217), and a Phase I/II dose-escalation study evaluated cabazitaxel plus capecitabine in taxane- and anthracycline-pretreated metastatic breast cancer (PMID 21339064). These trials confirm the biological plausibility of the TxGNN prediction and provide a foundation for further development.

> **Note on MOA data:** Detailed mechanism of action data (DrugBank) is listed as a data gap in this Evidence Pack. The mechanistic rationale above is derived from published literature included in the evidence set.

---

## Clinical Trial Evidence

Currently no related clinical trials were retrieved via the ClinicalTrials.gov query for this specific drug–disease pair. However, the literature evidence below includes results from Phase I/II and Phase II clinical trials conducted in breast cancer populations.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | Phase II RCT | *European Journal of Cancer* | GENEVIEVE trial: cabazitaxel vs. weekly paclitaxel as neoadjuvant therapy in operable HER2-negative breast cancer (TNBC and luminal B); compared pathological complete response (pCR) rates |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase I/II | *European Journal of Cancer* | Dose-escalation study of cabazitaxel + capecitabine in metastatic breast cancer patients previously treated with taxanes and anthracyclines; assessed MTD, safety, PK, and antitumor activity |
| [29678476](https://pubmed.ncbi.nlm.nih.gov/29678476/) | 2018 | Phase II | *Clinical Breast Cancer* | Cabazitaxel + lapatinib in HER2+ metastatic breast cancer with intracranial metastases; exploited cabazitaxel's blood–brain barrier penetration (NCT01934894) |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclinical | *Journal for Immunotherapy of Cancer* | Cabazitaxel reprograms tumor-associated macrophages (TAMs), enabling synergy with anti-CD47 immunotherapy in TNBC; demonstrates immunomodulatory mechanism beyond cytotoxicity |
| [28567478](https://pubmed.ncbi.nlm.nih.gov/28567478/) | 2017 | Translational | *Cancer Chemotherapy and Pharmacology* | βIII-tubulin overexpression (common in TNBC) confers greater cabazitaxel efficacy vs. docetaxel; provides direct mechanistic support for the breast cancer application |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Preclinical | *Molecular Cancer Therapeutics* | Resistance mechanisms to cabazitaxel studied in MCF-7 breast cancer cells; cabazitaxel showed significantly less cross-resistance than paclitaxel/docetaxel in MDR variants |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclinical | *Journal of Controlled Release* | Cabazitaxel-loaded PEBCA nanoparticles achieved complete remission in 6/8 tumors in a patient-derived basal-like breast cancer xenograft model; free drug gave 2/8 complete remissions |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | Preclinical | *International Journal of Nanomedicine* | PACA nanoparticle variants loaded with cabazitaxel tested in TNBC PDX model; associated with decreased M2 macrophage infiltration in tumor microenvironment |
| [34309357](https://pubmed.ncbi.nlm.nih.gov/34309357/) | 2021 | Preclinical | *Bioconjugate Chemistry* | Cyclic cell-penetrating peptide conjugated to cabazitaxel for targeted delivery in prostate and breast cancer; exploited integrin and fibronectin EDB biomarkers overexpressed in breast tumors |
| [30521787](https://pubmed.ncbi.nlm.nih.gov/30521787/) | 2019 | Preclinical | *Chemistry and Physics of Lipids* | Cabazitaxel + thymoquinone co-loaded lipospheres showed synergistic activity against breast tumor cells via dual inhibition (microtubule + HDAC), with modulation of p53, Bax, BCL-2, and NF-κB |

---

## Taiwan Market Information

Cabazitaxel is currently **not marketed in Taiwan** (market status: 未上市). No drug authorizations are on record with the TFDA. Safety and prescribing information must be sourced from international regulatory documents (e.g., FDA label or EMA SmPC).

---

## Cytotoxicity

Cabazitaxel is a cytotoxic antineoplastic agent (taxane derivative). This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (microtubule-stabilizing agent) |
| Myelosuppression Risk | **High** — Neutropenia is the primary dose-limiting toxicity; febrile neutropenia and neutropenic sepsis have been reported. G-CSF prophylaxis is recommended in high-risk patients |
| Emetogenicity Classification | Low to moderate (consistent with taxane class) |
| Monitoring Items | CBC with differential (before each cycle), liver function tests, renal function, serum electrolytes; monitor for peripheral neuropathy and diarrhea |
| Handling Protection | Must follow cytotoxic drug handling regulations — requires closed-system transfer devices, PPE, and dedicated disposal pathways |

---

## Safety Considerations

Full TFDA package insert data is not available for this drug (Data Gap: DG001). Detailed drug–drug interaction data was not found in this query.

> Please refer to the international SmPC (FDA label or EMA product information) for complete safety information, including warnings on severe neutropenia, hypersensitivity reactions, and renal impairment precautions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong — cabazitaxel's taxane-class activity directly parallels established breast cancer pharmacology, and its unique advantage over paclitaxel/docetaxel (low Pgp affinity, CNS penetration, βIII-tubulin efficacy) addresses clinically meaningful unmet needs in taxane-resistant and TNBC populations. The Phase II GENEVIEVE RCT and Phase I/II capecitabine combination trial provide clinical proof-of-concept, qualifying this as L2 evidence; however, no Phase III breast cancer data yet exists, and Taiwan regulatory dossiers are entirely absent.

**To proceed, the following is needed:**

- **TFDA package insert**: Retrieve and parse the SmPC/FDA label to complete the safety profile (DG001 — Blocking gap)
- **DrugBank MOA data**: Confirm full mechanism of action and target binding details (DG002 — High priority)
- **Phase III trial planning or identification**: Search for ongoing or planned Phase III trials comparing cabazitaxel in HER2-negative or TNBC breast cancer settings (e.g., post-CDX therapy lines)
- **TNBC subgroup analysis**: Prioritize evidence collection specifically for TNBC, where the βIII-tubulin and TAM-reprogramming rationale is strongest
- **Combination strategy evaluation**: Review cabazitaxel + immunotherapy (anti-CD47, anti-PD-L1) synergy data for potential basket trial designs
- **Taiwan/Asia-specific pharmacokinetic data**: Assess whether dose adjustments are needed based on regional body weight and CYP3A4 polymorphism prevalence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

