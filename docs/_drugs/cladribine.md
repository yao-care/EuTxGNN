---
layout: default
title: Cladribine
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
---

# Cladribine
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

# Cladribine: From Hairy Cell Leukemia to Parameningeal Embryonal Rhabdomyosarcoma

## One-Sentence Summary

Cladribine is a purine nucleoside analog with established efficacy in hairy cell leukemia and, more recently, relapsing forms of multiple sclerosis. The TxGNN model predicts it may be effective for **Parameningeal Embryonal Rhabdomyosarcoma**, yet currently **no clinical trials** and **no supporting publications** exist for this indication. Evidence is limited to AI model prediction only (L5), and this prediction — along with all 10 top-ranked indications — clusters around rhabdomyosarcoma subtypes, raising concern for knowledge graph topology artifacts rather than genuine biological signals.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hairy cell leukemia (based on known pharmacology; not captured in regulatory dataset) |
| Predicted New Indication | Parameningeal Embryonal Rhabdomyosarcoma |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| EU Market Status | Not marketed (0 authorizations in dataset — see note below) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Cladribine is a chlorinated deoxyadenosine analog resistant to adenosine deaminase. It is phosphorylated intracellularly by deoxycytidine kinase (dCK) into the active triphosphate form (2-CdATP), which incorporates into DNA and causes irreparable double-strand breaks and apoptosis. This mechanism preferentially targets cells with a high dCK-to-5'-nucleotidase ratio — primarily lymphoid lineage cells — which explains its efficacy in hairy cell leukemia and multiple sclerosis (immune modulation via lymphodepletion).

Parameningeal embryonal rhabdomyosarcoma (RMS) is an aggressive pediatric mesenchymal tumor arising near the meninges (nasal cavity, paranasal sinuses, middle ear). The standard treatment backbone is the VAC regimen (vincristine, actinomycin D, cyclophosphamide) with radiation. The mechanistic gap is significant: RMS cells are of skeletal muscle progenitor origin and their dCK/5'-nucleotidase expression ratio has not been characterized in the literature, meaning selectivity of Cladribine for RMS cannot be assumed.

The TxGNN score of 0.9977 is high, but the pattern across the top 10 predictions — all rhabdomyosarcoma subtypes or rare mesenchymal tumors with tightly clustered scores (0.9977 → 0.9807) and zero supporting evidence — strongly suggests this reflects shared proliferative/oncogenic node connectivity in the knowledge graph rather than a disease-specific biological signal. This prediction should be interpreted with caution as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note on Rank 7 (Liver Sarcoma):** One publication was retrieved (PMID [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/), 2004, Case Report — *Smoldering systemic mastocytosis treated with cladribine*). This is a **false positive** match — the paper describes mastocytosis therapy, not liver sarcoma. After exclusion, all 10 predicted indications have zero supporting evidence.

---

## EU Market Information

No authorizations were captured in this dataset (0 licenses, status: not marketed).

> **Important discrepancy:** Cladribine is known to hold EMA authorization as **Mavenclad®** (oral tablets) for relapsing remitting multiple sclerosis (approved 2017). If this authorization was not captured by the data pipeline, please verify directly at the [EMA Product Catalogue](https://www.ema.europa.eu/en/medicines/find-medicine/european-public-assessment-reports) before making regulatory decisions. This gap does not affect the repurposing evidence assessment for RMS, but it is relevant to the drug's overall safety and SmPC availability.

---

## Cytotoxicity

Cladribine meets the criteria for antineoplastic classification: it is a cytotoxic chemotherapy agent (purine nucleoside analog) with proven efficacy in hematologic malignancy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Purine nucleoside analog (halogenated deoxyadenosine) |
| Myelosuppression Risk | High — profound lymphopenia (CD4+ and CD8+ T-cell depletion) is a class-defining effect; neutropenia and thrombocytopenia also reported |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (especially lymphocyte subsets and CD4+ count), liver function tests, renal function; opportunistic infection surveillance during lymphopenic nadir |
| Handling Protection | Must follow cytotoxic drug handling regulations; teratogenic potential — reproductive precautions required |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> Safety data (key warnings, contraindications, drug interactions) were not available in this Evidence Pack. Given Cladribine's known profound lymphodepletive effects, any repurposing application must conduct a full SmPC review prior to clinical development — including immunosuppression, infection risk, secondary malignancy, and reproductive toxicity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 top-ranked TxGNN predictions for Cladribine cluster around rhabdomyosarcoma subtypes and rare mesenchymal tumors, all at evidence level L5 with zero clinical trials or literature support. The mechanistic basis for Cladribine activity in mesenchymal tumors is absent, and the score clustering pattern across highly specific RMS subtypes is a strong indicator of knowledge graph node bias rather than meaningful biological signal.

**To proceed, the following is needed:**

- **Artifact verification:** Re-evaluate whether the RMS cluster in TxGNN predictions reflects genuine biology or KG topology bias (e.g., by checking edge distribution from Cladribine node to mesenchymal disease nodes)
- **In vitro mechanistic data:** dCK and 5'-nucleotidase expression profiling in RMS cell lines (e.g., RD, A-204, Rh30) to assess whether Cladribine's selective cytotoxicity mechanism applies
- **Full MOA data:** Retrieve complete DrugBank API entry (DB00242) to support mechanistic rationale analysis
- **Safety data:** Obtain TFDA and EMA SmPC for full warnings, contraindications, and DDI profile before any clinical hypothesis development
- **Evidence gap reassessment:** If RMS-specific evidence (even preclinical) emerges from the literature, re-score as L4 and re-evaluate; otherwise this candidate should remain deprioritized relative to indications where Cladribine has established mechanistic logic (e.g., lymphoid malignancies)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

