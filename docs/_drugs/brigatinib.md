---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib: From ALK-Positive NSCLC to Lung Benign Neoplasm

## One-Sentence Summary

Brigatinib (ALUNBRIG) is a next-generation ALK/ROS1/EGFR tyrosine kinase inhibitor, globally approved since 2017 for ALK-positive metastatic non-small cell lung cancer (NSCLC), but currently **not registered in Taiwan**.
The TxGNN model predicts it may benefit patients with **Lung Benign Neoplasm** — most plausibly ALK-rearranged inflammatory myofibroblastic tumors (IMTs) —
supported by **0 direct clinical trials** but **20 publications** from ALK+ NSCLC providing indirect mechanistic evidence (Evidence Level L4).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive metastatic NSCLC (global approval; not registered in Taiwan) |
| Predicted New Indication | Lung Benign Neoplasm |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 (indirect mechanistic analogy; no direct clinical trials for this indication) |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Taiwan Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Taiwan drug registry. Based on published clinical and preclinical evidence, Brigatinib is a potent second-generation anaplastic lymphoma kinase (ALK) tyrosine kinase inhibitor that also inhibits ROS1, EGFR (including the T790M resistance mutant), IGF-1R, FLT3, and INSR. It was specifically engineered to overcome crizotinib resistance mutations, and its superior blood-brain barrier penetration gives it a clinically meaningful advantage over first-generation ALK inhibitors.

ALK-positive NSCLC and certain lung "benign neoplasms" share a common molecular driver: constitutive ALK activation driven by chromosomal rearrangement. Inflammatory myofibroblastic tumors (IMTs) — low-grade, borderline mesenchymal tumors arising in the lung — harbor ALK fusions (commonly EML4-ALK or RANBP2-ALK) in approximately 50% of cases. Clinical proof of concept for ALK inhibition in IMT already exists with crizotinib, making Brigatinib a logical next-generation escalation candidate. In ALK-rearranged cells, constitutive kinase activation drives proliferation and survival regardless of whether the tumor is classified as malignant or benign/low-grade.

The critical caveat is that all 20 retrieved publications address ALK+ NSCLC (malignant), not lung benign neoplasm directly. The TxGNN model's high score (99.85%) most likely reflects knowledge-graph topological proximity between lung tumor entities rather than a verified biological link to the full "lung benign neoplasm" category. Whether ALK-rearranged IMTs are coded under "lung benign neoplasm" in the local disease ontology requires pathological and coding verification before this prediction can be advanced.

---

## Literature Evidence

All 20 retrieved publications address ALK+ NSCLC (malignant) and provide strong evidence of Brigatinib's ALK-inhibiting mechanism — the shared biological driver for this repurposing hypothesis — but are **indirect** evidence for lung benign neoplasm.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34537440](https://pubmed.ncbi.nlm.nih.gov/34537440/) | 2021 | Phase 3 RCT | J Thorac Oncol | ALTA-1L final results: Brigatinib vs crizotinib in first-line ALK+ NSCLC; superior PFS and emerging OS trend confirmed at final analysis |
| [30280657](https://pubmed.ncbi.nlm.nih.gov/30280657/) | 2018 | Phase 3 RCT | N Engl J Med | ALTA-1L primary analysis: Brigatinib significantly superior to crizotinib in ALK inhibitor-naive advanced ALK+ NSCLC |
| [37574132](https://pubmed.ncbi.nlm.nih.gov/37574132/) | 2023 | Phase 3 RCT | J Thorac Oncol | ALTA-3: Brigatinib vs alectinib post-crizotinib progression; first head-to-head Phase 3 comparison between second-generation ALK TKIs |
| [32780660](https://pubmed.ncbi.nlm.nih.gov/32780660/) | 2020 | Phase 3 RCT | J Clin Oncol | ALTA-1L 2nd interim: continued PFS benefit and improved health-related quality of life vs crizotinib confirmed |
| [28475456](https://pubmed.ncbi.nlm.nih.gov/28475456/) | 2017 | Phase 2 RCT | J Clin Oncol | ALTA Phase 2: two Brigatinib regimens in crizotinib-refractory ALK+ NSCLC; 90 mg × 7 days → 180 mg QD regimen preferred |
| [39923717](https://pubmed.ncbi.nlm.nih.gov/39923717/) | 2025 | Integrated Analysis | Lung Cancer | Pooled ALTA-1L + J-ALTA data: larger global dataset confirms first-line Brigatinib efficacy and safety consistency across populations |
| [38331773](https://pubmed.ncbi.nlm.nih.gov/38331773/) | 2024 | Systematic Review / NMA | BMC Cancer | Network meta-analysis of all ALK TKIs in first-line ALK+ NSCLC; Brigatinib ranked among top options for PFS |
| [36038416](https://pubmed.ncbi.nlm.nih.gov/36038416/) | 2022 | Phase 3 Subgroup | Clin Lung Cancer | ALTA-1L Asian vs non-Asian subgroup: consistent Brigatinib efficacy and safety benefit across ethnic populations |
| [39232917](https://pubmed.ncbi.nlm.nih.gov/39232917/) | 2024 | Indirect Comparison / NMA | Clin Lung Cancer | Matching-adjusted indirect comparison of lorlatinib vs Brigatinib as first-line therapy; comparative PFS and safety quantified |
| [37597303](https://pubmed.ncbi.nlm.nih.gov/37597303/) | 2023 | Safety Review / NMA | Lung Cancer | Comparative toxicity profiles of ALK TKIs; quantifies myelosuppression, hepatotoxicity, and pulmonary risk by agent to guide clinical decisions |

> ⚠️ **Evidence level is L4** because all publications address ALK+ NSCLC (malignant), not lung benign neoplasm directly. Mechanistic analogy to ALK-rearranged inflammatory myofibroblastic tumors is biologically plausible but unvalidated in clinical trials.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (second-generation ALK/ROS1/EGFR tyrosine kinase inhibitor; oral small molecule antineoplastic) |
| Myelosuppression Risk | Low (targeted TKI; clinically significant myelosuppression is uncommon; anaemia reported in ~25% but Grade 3+ rare) |
| Emetogenicity Classification | Low to moderate (oral TKI; nausea reported in ~33% of patients, severe events rare) |
| Monitoring Items | Liver function (ALT/AST), pulmonary function (ILD/pneumonitis), blood pressure, heart rate (bradycardia), QTc interval, fasting blood glucose (hyperglycaemia), CPK (myopathy), visual acuity |
| Handling Protection | Standard oral targeted therapy precautions; cytotoxic handling regulations apply per institutional SOP |

---

## Safety Considerations

Please refer to the SmPC for complete safety information.

Based on published Phase 3 trial data, the following class-related risks are clinically important:

- **Early-onset pulmonary toxicity**: ILD/pneumonitis has been reported within the first 7 days of initiation. The dose escalation protocol (90 mg QD × 7 days, then 180 mg QD) significantly reduces this risk and is mandatory.
- **Cardiovascular**: Hypertension, bradycardia, and QTc prolongation — baseline cardiovascular assessment and ongoing monitoring required.
- **Visual disturbances**: Blurred vision, diplopia, and photosensitivity reported; ophthalmic evaluation if symptomatic.
- **Metabolic**: Hyperglycaemia (particularly in patients with pre-existing diabetes) and elevated CPK with myalgia; routine metabolic monitoring recommended.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Brigatinib has robust Phase 3 evidence for ALK+ NSCLC and a biologically plausible mechanistic link to ALK-rearranged lung benign tumors (particularly IMTs). However, no direct clinical trials or publications address "lung benign neoplasm" as an indication, all evidence is indirect (L4), and the drug is not registered in Taiwan — making any clinical application premature without further validation.

**To proceed, the following is needed:**

- Pathological confirmation that the target patient population harbours ALK rearrangements (EML4-ALK, RANBP2-ALK, or other ALK fusions) in the relevant tumour type
- Clarify disease coding: verify whether ALK-rearranged inflammatory myofibroblastic tumors (IMTs) are classified as "lung benign neoplasm" in the local disease ontology
- Download and parse the TFDA SmPC PDF to complete safety and contraindication assessment (currently Blocking data gap)
- Retrieve full MOA documentation from DrugBank (DB12267) to support mechanistic analysis
- Identify whether an ongoing basket trial (e.g., ALK+ solid tumours) could enrol patients with ALK+ IMTs as a sub-cohort
- Consult Taiwan regulatory pathway for compassionate use or off-label access in ALK+ IMT if pathological confirmation is obtained
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

