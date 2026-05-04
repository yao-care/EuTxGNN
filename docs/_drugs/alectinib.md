---
layout: default
title: Alectinib
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
---

# Alectinib
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

# Alectinib: From ALK-Positive NSCLC to Lung Germ Cell Tumor

---

## One-Sentence Summary

Alectinib is a second-generation ALK tyrosine kinase inhibitor (TKI), approved globally for ALK-positive non-small cell lung cancer (NSCLC), but not yet registered in Taiwan.
The TxGNN model's highest-ranked novel prediction is fibromatosis, gingival (Rank 1, 99.97%), but that prediction — along with Ranks 2–6 and 8–10 — is flagged as mechanistic noise with no supporting evidence and a uniform **Hold** recommendation; the only actionable finding is **Rank 7: Lung Germ Cell Tumor** (99.95%), supported by **2 clinical trials** and **16 publications**.
Note that retrieved evidence maps primarily to **ALK-positive pulmonary neuroendocrine carcinoma (LCNEC/NET)**, suggesting a TxGNN disease-node terminology mismatch rather than true germ cell tumor biology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive NSCLC (globally approved; not registered in Taiwan) |
| Predicted New Indication | Lung Germ Cell Tumor (evidence maps to ALK+ Neuroendocrine Carcinoma of Lung) |
| TxGNN Prediction Score | 99.95% (Rank 7; Ranks 1–6 are mechanistic noise) |
| Evidence Level | L3 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed pharmacological mechanism data was not available via the DrugBank query at the time of this report. Based on clinical literature contained in this evidence pack, Alectinib is a highly selective, CNS-penetrant second-generation inhibitor of Anaplastic Lymphoma Kinase (ALK) and RET tyrosine kinases. Its approved indication in ALK-positive NSCLC is driven by chromosomal rearrangements — most commonly EML4-ALK fusion — found in approximately 3–5% of NSCLC patients. Alectinib suppresses ALK autophosphorylation and downstream oncogenic signaling (RAS/MAPK, PI3K/AKT), and its superior CNS penetration distinguishes it from the first-generation inhibitor crizotinib.

The connection to pulmonary neuroendocrine carcinoma is biologically plausible and mechanistically direct. ALK fusion genes — including EML4-ALK and novel partners such as KIF5B-ALK — have been confirmed in large cell neuroendocrine carcinoma (LCNEC) and atypical carcinoid of the lung across multiple independent case reports from 2018–2023. When an ALK rearrangement is present, inhibition of the same kinase target that drives the approved NSCLC indication can produce clinically meaningful tumor responses. The driver mutation — not the histological origin — determines sensitivity, supporting a tissue-agnostic molecular rationale.

The critical constraint is rarity: ALK rearrangements in pulmonary NET/LCNEC are substantially less frequent than in NSCLC adenocarcinoma, making conventional prospective trials difficult to execute and explaining why evidence remains at the case report level. The ongoing UK-based DETERMINE platform trial (NCT05770037, Phase 2/3, recruiting) is specifically designed to generate prospective data in patients with ALK-positive rare and molecularly-defined cancers through a basket design, and represents the most important near-term evidence-generating study for this research question.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04644315](https://clinicaltrials.gov/study/NCT04644315) | Phase 2 | Terminated | 1 | Single-arm, home-based decentralized study of alectinib in ALK+ locally advanced or metastatic solid tumors other than lung cancer; terminated after enrolling only 1 patient — no efficacy or safety conclusions can be drawn |
| [NCT05770037](https://clinicaltrials.gov/study/NCT05770037) | Phase 2/3 | Recruiting | 30 | DETERMINE platform trial (UK, MHRA-approved): alectinib Treatment Arm 01 in adult, paediatric, and TYA patients with ALK-positive rare or molecularly defined cancers; completion expected October 2029 — the most relevant ongoing trial for this indication |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [36690569](https://pubmed.ncbi.nlm.nih.gov/36690569/) | 2023 | Case report | Clinical Lung Cancer | ALK-positive neuroendocrine tumor of the lung showed favorable response to alectinib; supports routine ALK testing in pulmonary NET |
| [37031440](https://pubmed.ncbi.nlm.nih.gov/37031440/) | 2023 | Case report | Orvosi Hetilap | Mixed large cell neuroendocrine carcinoma with ALK fusion treated with alectinib; highlights ALK-driven LCNEC as a distinct therapeutic entity |
| [35200571](https://pubmed.ncbi.nlm.nih.gov/35200571/) | 2022 | Case report | Current Oncology | Stage IV combined LCNEC + adenocarcinoma with ALK rearrangement demonstrated partial response to alectinib following recurrence with bony metastases |
| [34994612](https://pubmed.ncbi.nlm.nih.gov/34994612/) | 2021 | Case report | JCO Precision Oncology | Metastatic LCNEC with ALK fusion oncogene showed partial response to alectinib — extends ALK inhibitor utility to neuroendocrine histology |
| [29151522](https://pubmed.ncbi.nlm.nih.gov/29151522/) | 2018 | Case report | Internal Medicine (Tokyo) | LCNEC with ALK rearrangement and multiple liver/bone metastases responded to alectinib after failure of cytotoxic chemotherapy |
| [30591488](https://pubmed.ncbi.nlm.nih.gov/30591488/) | 2019 | Clinical study | Anticancer Research | ALK immunohistochemistry applied to pulmonary LCNEC series; identified novel KIF5B-ALK fusion oncokinase — supports routine ALK screening in LCNEC |
| [31559892](https://pubmed.ncbi.nlm.nih.gov/31559892/) | 2020 | Case report | Cancer Biology & Therapy | Pulmonary atypical carcinoid with EML4-ALK rearrangement — extends the ALK fusion spectrum into the lower-grade neuroendocrine carcinoid category |
| [37561984](https://pubmed.ncbi.nlm.nih.gov/37561984/) | 2023 | Review | JCO Precision Oncology | ALK inhibitors including alectinib and crizotinib reviewed for adult-onset neuroblastoma enriched for somatic ALK mutations — broadens the concept of ALK-driven neuroendocrine tumors beyond the lung |
| [39667359](https://pubmed.ncbi.nlm.nih.gov/39667359/) | 2024 | Case report | Clinical Respiratory Journal | Ensartinib (ALK-TKI) in NET with novel CEP44-ALK fusion; alectinib and crizotinib discussed as viable options in ALK-rearranged NET — expands the fusion partner landscape |
| [36965191](https://pubmed.ncbi.nlm.nih.gov/36965191/) | 2023 | Case report | Pediatric Blood & Cancer | Alectinib produced significant response in pediatric intramedullary high-grade glioma harboring ALK fusion — illustrates tissue-agnostic efficacy of ALK inhibition when the driver is present |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation ALK/RET tyrosine kinase inhibitor (not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Low — anemia and neutropenia reported but typically mild to moderate and less frequent than with platinum-based regimens |
| Emetogenicity Classification | Low — oral agent; nausea and vomiting are uncommon adverse events |
| Monitoring Items | Liver function tests (AST/ALT — hepatotoxicity is the primary class concern), complete blood count, heart rate (bradycardia observed), body weight (clinically significant weight gain in approximately 10% of patients), renal function |
| Handling Protection | Standard oral hazardous drug precautions apply; full cytotoxic chemotherapy handling protocols (such as those for platinum or taxane infusions) are not required |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Alectinib in ALK-positive pulmonary neuroendocrine carcinoma (LCNEC/NET) is mechanistically credible and supported by at least five independent case reports demonstrating objective responses, but no completed prospective trial exists. The only ongoing prospective study (DETERMINE, NCT05770037) is still recruiting and will not report until 2029. Additionally, Taiwan has no registered license for Alectinib, and both the TFDA safety data (warnings, contraindications) and DrugBank MOA record are missing, blocking a formal S1 safety pre-assessment.

**To proceed, the following is needed:**
- Mature results from the DETERMINE platform trial (NCT05770037), expected October 2029
- Formal multi-institutional ALK testing protocol (IHC + confirmatory FISH or NGS) standardized for pulmonary NET/LCNEC at diagnosis, to enable patient selection
- Retrieval and parsing of the TFDA SmPC PDF to complete the S1 safety and contraindication review
- DrugBank API query to obtain complete MOA, category, and toxicity profile (currently blocking mechanistic analysis)
- Retrospective case series or registry study aggregating existing ALK+ LCNEC cases treated with ALK-TKIs to estimate response rate, progression-free survival, and safety profile prior to any prospective development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

