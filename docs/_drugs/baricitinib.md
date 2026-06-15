---
layout: default
title: Baricitinib
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Baricitinib
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

# Baricitinib: From Rheumatoid Arthritis to Myeloid Leukemia (Multi-Indication Analysis)

## One-Sentence Summary

Baricitinib is a selective JAK1/2 inhibitor approved globally for rheumatoid arthritis, atopic dermatitis, and COVID-19, but currently **not registered in Taiwan**.
The TxGNN model generated **10 predicted indications**; the top-ranked prediction is colobomatous microphthalmia-rhizomelic dysplasia syndrome (score 99.94%, L5, no evidence), while **myeloid leukemia** (rank 6) carries the strongest evidence base with **1 active Phase 2/3 clinical trial** and **4 publications** (Evidence Level: L3).
Due to absent Taiwan regulatory data and gaps in MOA and safety documentation, the overall recommendation across all top predictions is **Hold** pending data remediation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally approved for rheumatoid arthritis, atopic dermatitis, COVID-19 |
| Predicted New Indication (Rank 1) | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score (Rank 1) | 99.94% |
| Evidence Level (Rank 1) | L5 — AI prediction only, no clinical studies |
| Taiwan Market Status | ✗ Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (Data Gap DG002). Based on known pharmacological knowledge, Baricitinib is a selective JAK1 and JAK2 inhibitor that blocks downstream STAT phosphorylation triggered by cytokines including IL-6, IL-4, IL-13, and IFN-γ. This broad immunomodulatory effect underpins its approved use in rheumatoid arthritis and atopic dermatitis.

The rank 1 TxGNN prediction — colobomatous microphthalmia-rhizomelic dysplasia syndrome — is an ultra-rare congenital developmental disorder driven by genetic mutations affecting ocular and limb morphogenesis. While the JAK-STAT pathway has some known role in embryonic ocular patterning, the mechanistic connection to JAK1/2 inhibition for this condition is distant extrapolation. The exceptionally high model score (0.999) very likely reflects knowledge graph topological proximity rather than a direct biological or therapeutic relationship, and should be treated with caution.

Among all 10 predicted indications, **myeloid leukemia** (rank 6, score 91.01%) presents the most scientifically plausible repurposing rationale. JAK1/2 inhibition can interrupt IL-3, GM-CSF, and IFN-γ-driven myeloproliferative signaling, and in the allogeneic hematopoietic stem cell transplantation (allo-HSCT) setting, Baricitinib may reduce graft-versus-host disease (GvHD) by suppressing donor T-cell JAK-STAT activation. This is currently being tested in an active Phase 2/3 trial (n=150).

---

## Predicted Indications — Summary Table

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|---------------|----------------|
| 1 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.94% | L5 | Hold |
| 2 | Brachydactyly-syndactyly syndrome | 99.94% | L5 | Hold |
| 3 | Indolent plasma cell myeloma | 93.31% | L5 | Hold |
| 4 | WHIM syndrome | 93.12% | L5 | Hold |
| 5 | Plasma cell myeloma | 91.83% | L4 | Hold |
| 6 | **Myeloid leukemia** | **91.01%** | **L3** | **Research Question** |
| 7 | Meester-Loeys syndrome | 88.21% | L5 | Hold |
| 8 | Ganglioneuroblastoma | 87.59% | L5 | Hold |
| 9 | Heparin cofactor 2 deficiency | 86.31% | L5 | Hold |
| 10 | Vertebral anomalies and variable endocrine and T-cell dysfunction | 84.68% | L5 | Hold |

---

## Clinical Trial Evidence

### Rank 1 — Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

Currently no related clinical trials registered.

---

### Rank 6 — Myeloid Leukemia (Highest-Evidence Prediction)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06475820](https://clinicaltrials.gov/study/NCT06475820) | Phase 2/3 | Active, Not Recruiting | 150 | GvHD prevention using post-transplantation cyclophosphamide combined with abatacept, vedolizumab, and baricitinib in children and young adults with hemoblastosis after HSCT from unrelated or haploidentical donors. Primary endpoint is GvHD prevention; myeloid leukemia is the dominant underlying diagnosis. Completion expected April 2027. |

> **Note:** This trial's primary endpoint is GvHD prevention, not direct anti-leukemic efficacy. Baricitinib's role here is as a HSCT adjunct rather than a primary oncology agent.

---

## Literature Evidence

### Rank 5 — Plasma Cell Myeloma

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34856779](https://pubmed.ncbi.nlm.nih.gov/34856779/) | 2021 | Case Report | Minerva Medica | Simultaneous treatment of critical COVID-19 and newly diagnosed high-risk multiple myeloma with thalidomide, methylprednisolone, tocilizumab, and baricitinib. Myeloma outcomes were incidental observations during COVID-19 management, not a primary efficacy endpoint. Indirect and opportunistic evidence only. |

### Rank 6 — Myeloid Leukemia

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34730109](https://pubmed.ncbi.nlm.nih.gov/34730109/) | 2021 | Preclinical / Mechanism | Journal of Clinical Investigation | ADC-based conditioning combined with JAK inhibitors enables MHC-mismatched allogeneic HSCT in preclinical models. Supports the concept that JAK inhibition — including baricitinib — reduces immune rejection in the HSCT setting relevant to acute leukemia treatment. |
| [36569952](https://pubmed.ncbi.nlm.nih.gov/36569952/) | 2022 | Review / Hypothesis | Frontiers in Immunology | Review proposing repurposing of BCL-2 and JAK1/2 inhibitors for HIV-1 and viral infection by targeting long-lived infected cells. Indirect mechanistic relevance to immune modulation in hematologic contexts. |
| [35442720](https://pubmed.ncbi.nlm.nih.gov/35442720/) | 2022 | Observational / Diagnostic | JCO Precision Oncology | Nanopore mRNA sequencing for acute leukemia classification in low-resource settings. No baricitinib efficacy data; relevant only to leukemia disease characterization. |
| [31816725](https://pubmed.ncbi.nlm.nih.gov/31816725/) | 2020 | Pharmacokinetic / Analytical | Talanta | LC-MS/MS method for monitoring 11 TKIs including ruxolitinib in CML. Baricitinib is not among monitored drugs; relevance is limited to TDM methodology context. |

---

## Taiwan Market Information

Baricitinib (DB11817) has **no registered products in Taiwan** (0 licenses). Regulatory authorization data cannot be populated.

Globally, Baricitinib is marketed as **Olumiant** (Eli Lilly) and is approved by the US FDA and EMA for:
- Moderate-to-severe rheumatoid arthritis (adults)
- Moderate-to-severe atopic dermatitis (adults and adolescents ≥2 years)
- COVID-19 requiring supplemental oxygen (adults)

Taiwan TFDA prescribing information is unavailable (Data Gap DG001 — Blocking severity).

---

## Safety Considerations

Detailed Taiwan-specific warnings and contraindications are unavailable pending TFDA SmPC retrieval (Data Gap DG001). Based on the drug class profile:

- **Key Class-Level Risks:** JAK inhibitors as a class carry boxed warnings in the US for serious infections, malignancies (including lymphoma), major adverse cardiovascular events (MACE), thrombosis (DVT/PE), and mortality. These are especially relevant when considering oncology repurposing in immunocompromised patients.
- **Heparin Cofactor 2 Deficiency (Rank 9):** Specifically contraindicated conceptually — JAK inhibitors carry a known VTE risk, posing a compounding hazard in patients with pre-existing coagulation defects.
- **Drug Interactions:** No DDI data was returned from the query (query_status: not_found). Please refer to the SmPC for full interaction profile.

---

## Conclusion and Next Steps

**Decision: Hold (all 10 indications)**

**Rationale:**
No predicted indication has reached sufficient evidence quality to advance. The rank 1 prediction (colobomatous microphthalmia-rhizomelic dysplasia syndrome) is almost certainly a knowledge graph artifact with no mechanistic or clinical basis. The most actionable candidate — myeloid leukemia (rank 6, L3) — has only indirect GvHD-context evidence and lacks direct anti-leukemic efficacy data. Combined with blocking data gaps in Taiwan safety documentation, no indication can pass Stage 1 safety screening.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Download and parse TFDA prescribing information PDF to obtain Taiwan-specific warnings and contraindications, enabling entry into S1 safety screening
- **[DG002 — High]** Retrieve MOA data from DrugBank API to enable proper mechanistic linkage analysis for all 10 predicted indications
- For **myeloid leukemia** specifically: identify whether any Phase 1/2 studies directly test Baricitinib for anti-leukemic activity (not just GvHD prevention); monitor NCT06475820 results (completion: April 2027)
- For **plasma cell myeloma** (rank 5): evaluate whether IL-6/JAK2/STAT3 pathway inhibition rationale merits a hypothesis-generating preclinical study, particularly in high-risk or refractory settings
- Reassess all L5 predictions for mechanistic plausibility after MOA data is available — several (ranks 1, 2, 7, 9) appear to be structural false positives that may be deprioritized following manual review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

