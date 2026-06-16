---
layout: default
title: Carmustine
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 10
---

# Carmustine
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

# Carmustine: From Malignant Glioma to Lymph Node Cancer

## One-Sentence Summary

Carmustine (BCNU) is a nitrosourea alkylating agent with established use in malignant brain tumor treatment and as the cornerstone of the BEAM conditioning regimen (BCNU + etoposide + cytarabine + melphalan) prior to autologous haematopoietic stem cell transplantation (ASCT).
The TxGNN model predicts it may be effective for **Lymph Node Cancer** (broadly encompassing Hodgkin and non-Hodgkin lymphoma), with **7 clinical trials** and **20 publications** currently supporting this direction.
Notably, this prediction is strongly aligned with existing clinical practice — carmustine is already embedded in standard-of-care lymphoma conditioning protocols worldwide.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant glioma / high-grade brain tumors (Gliadel wafer); BEAM myeloablative conditioning in lymphoma |
| Predicted New Indication | Lymph Node Cancer |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L2 |
| EU Market Status | No EMA authorizations found in current dataset (data gap — Gliadel® is known to hold EMA approval) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Carmustine (BCNU) belongs to the nitrosourea class of alkylating agents. Its primary mechanism involves chloroethylation of DNA at the O6-position of guanine, forming interstrand cross-links that block both DNA replication and RNA transcription. This cytotoxic action is cell-cycle non-specific, making it particularly effective against rapidly dividing malignant cells. Additionally, carmustine's high lipid solubility (log P ≈ 1.5) allows it to penetrate the blood-brain barrier, explaining its dual utility in neuro-oncology and myeloablative conditioning.

Lymph node cancer — broadly encompassing Hodgkin lymphoma (HL) and non-Hodgkin lymphoma (NHL) — involves malignant transformation of lymphoid cells that show documented sensitivity to alkylating agents. The BEAM regimen was specifically designed to exploit carmustine's myeloablative potency, using it to create a tumour-free marrow environment before ASCT. This conditioning approach eliminates residual lymphoma cells that survive conventional induction therapy and allows engraftment of transplanted stem cells to restore haematopoiesis.

The mechanistic rationale is therefore exceptionally strong: carmustine is not merely predicted to have activity against lymphoma — it is already the active backbone of a standard clinical pathway for relapsed/refractory HL and aggressive NHL. BEAM conditioning prior to ASCT is endorsed by ESMO and NCCN guidelines. The TxGNN score of 98.49% reflects the model's recognition of this well-established biological and clinical convergence. The only reason this appears as a "repurposing" prediction is that the current Evidence Pack does not record lymphoma as a formally registered original indication — an artefact of the data collection gap rather than a genuine mechanistic novelty.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01141712](https://clinicaltrials.gov/study/NCT01141712) | Phase 2 | Completed | 43 | Multicenter trial: BEAM conditioning (carmustine, etoposide, cytarabine, melphalan) + ASCT for aggressive B-cell lymphoma and Hodgkin lymphoma in HIV-infected patients; assessed overall survival and transplant-related mortality |
| [NCT00345865](https://clinicaltrials.gov/study/NCT00345865) | Phase 2 | Completed | 473 | Large-scale PBSC transplant programme for lymphoma patients; carmustine-containing conditioning evaluated across disease subtypes for disease control and long-term outcome |
| [NCT01702961](https://clinicaltrials.gov/study/NCT01702961) | N/A | Completed | 75 | Real-world observational study of Rituximab + BEAM conditioning for relapsed lymphoma and Hodgkin's disease after first relapse; provides registry-level efficacy and safety data |
| [NCT01008462](https://clinicaltrials.gov/study/NCT01008462) | Phase 2 | Completed | 16 | Sequential auto HCT followed by non-myeloablative allogeneic HCT for high-risk HL, NHL, multiple myeloma, and CLL; BEAM-like conditioning with carmustine as part of sequential intensification strategy |
| [NCT01468311](https://clinicaltrials.gov/study/NCT01468311) | Phase 1/2 | Terminated | 6 | Y-90-labeled daclizumab (anti-CD25) radioimmunotherapy combined with high-dose BEAM for recurrent/refractory Hodgkin's lymphoma; terminated early due to accrual; provides safety signal for BEAM + RIT combination |
| [NCT00002772](https://clinicaltrials.gov/study/NCT00002772) | Phase 3 | Terminated | 602 | Phase 3 comparison of intensive sequential chemotherapy including carmustine-class alkylators for high-risk breast cancer with axillary lymph node involvement; terminated — provides high-dose alkylator pharmacology and toxicity context |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18988286](https://pubmed.ncbi.nlm.nih.gov/18988286/) | 2008 | RCT | Cancer | Randomized Phase 2 (GOELAMS Group, 158 patients): early intensification with myeloablative chemotherapy + ASCT vs. ABVD for high-risk stage IIB–IV Hodgkin lymphoma; 5-year FFTF rates compared, supports role of myeloablative conditioning in refractory HL |
| [2642573](https://pubmed.ncbi.nlm.nih.gov/2642573/) | 1989 | Clinical Study | Leukemia | 23 Hodgkin's disease patients directly treated with BCNU (450–600 mg/m²) + etoposide + cyclophosphamide with bone marrow rescue; demonstrates carmustine's direct anti-lymphoma myeloablative activity; median age 28, 19/23 had progressive disease on prior therapy |
| [10473086](https://pubmed.ncbi.nlm.nih.gov/10473086/) | 1999 | Clinical Study | Clin Cancer Res | O6-alkylguanine-DNA alkyltransferase (AGT) activity in cutaneous T-cell lymphoma (mycosis fungoides); topical carmustine is standard early treatment; Phase 1 data on temozolomide in mycosis fungoides provides mechanistic context for carmustine resistance via MGMT |
| [7577204](https://pubmed.ncbi.nlm.nih.gov/7577204/) | 1995 | RCT | JNCI Monographs | CALGB 9082: high-dose vs. low-dose cyclophosphamide/cisplatin/carmustine with ABMT for high-risk breast cancer (≥10 axillary nodes); establishes carmustine PK and toxicity profile in high-dose myeloablative context relevant to lymphoma conditioning |
| [1639635](https://pubmed.ncbi.nlm.nih.gov/1639635/) | 1992 | Clinical Study | Int J Radiat Oncol Biol Phys | 49 patients with primary breast cancer (≥10 axillary nodes) treated with high-dose cyclophosphamide/cisplatin/carmustine (HDCT) + ABMT followed by post-mastectomy radiotherapy; characterises locoregional disease control after carmustine-based myeloablation |

> **Note:** The 20 publications retrieved for this query include a large proportion of breast cancer high-dose chemotherapy studies where carmustine was a component of myeloablative regimens. Lymphoma-specific publications are limited (3 of 20); stronger lymphoma evidence is available under the Rank 5 indication (Reticulum Cell Sarcoma / DLBCL), where 20 publications with higher specificity were retrieved.

---

## EU Market Information

No EMA marketing authorizations were found in the current dataset for Carmustine (INN) as of 2026-06-15. This is likely a data gap: carmustine wafer (Gliadel®) is documented in the clinical literature and regulatory sources as holding EMA approval for high-grade glioma. Independent verification via the EMA product database is recommended before drawing conclusions about EU market availability.

---

## Cytotoxicity

Carmustine belongs to the alkylating agent / nitrosourea class and meets all criteria for antineoplastic cytotoxic classification.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Nitrosourea alkylating agent (bifunctional chloroethylating agent) |
| Myelosuppression Risk | **High** — onset typically delayed 4–6 weeks post-administration; cumulative toxicity with repeat dosing; both neutropenia and thrombocytopenia expected; haematological nadir later than most alkylating agents |
| Emetogenicity Classification | **Moderate to High** — particularly at high doses used in BEAM conditioning (BCNU 300 mg/m²); prophylactic antiemetics required |
| Monitoring Items | Full blood count with differential (weekly during and 6 weeks post-treatment), liver function tests, renal function, pulmonary function tests (risk of pulmonary fibrosis, especially with cumulative doses > 1,400 mg/m²) |
| Handling Protection | Must follow cytotoxic drug handling regulations — preparation in certified laminar flow hood, closed-system drug transfer devices, PPE (gloves, gown, eye protection) required |

---

## Safety Considerations

Safety data was not available for this drug in the current Evidence Pack. Please refer to the SmPC (Summary of Product Characteristics) for complete safety information, including key warnings, contraindications, and drug interactions.

> **Known class-level concerns** based on published literature evidence within this report: pulmonary fibrosis (particularly with cumulative dosing), delayed myelosuppression (nadir at 4–6 weeks), hepatotoxicity, and secondary malignancy risk (therapy-related AML/MDS). These should be formally verified against the current SmPC before clinical application.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Carmustine's role in the BEAM regimen for lymphoma conditioning is already well-established in international clinical guidelines, and Phase 2 trial evidence (NCT01141712, NCT00345865) directly supports its use in lymph node cancer. However, the EU regulatory data gap and missing MOA/safety data require resolution before a complete evaluation can be filed.

**To proceed, the following is needed:**

- **Regulatory verification**: Confirm EMA market status for carmustine (Gliadel® wafer and IV BCNU) by direct EMA database query — current dataset shows 0 authorizations, inconsistent with published approval records
- **MOA data**: Obtain complete mechanism of action data from DrugBank API (DG002) to support mechanistic linkage analysis
- **Safety dossier**: Download and parse SmPC from EMA to populate key warnings, contraindications, and drug interaction profile (DG001)
- **Evidence specificity**: Retrieve lymphoma-specific clinical trial publications (the current PubMed set for "lymph node cancer" is heavily contaminated with breast cancer papers; a targeted NHL/HL search is recommended to strengthen evidence quality assessment)
- **MGMT resistance assessment**: Review whether target patient population has high MGMT expression (a known resistance mechanism to carmustine), and whether O6-benzylguanine sensitisation strategy is applicable in the lymphoma context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

