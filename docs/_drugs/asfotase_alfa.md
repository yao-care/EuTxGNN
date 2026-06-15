---
layout: default
title: Asfotase Alfa
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
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

# Asfotase Alfa: From Hypophosphatasia to Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies

## One-Sentence Summary

Asfotase alfa (Strensiq) is a recombinant enzyme replacement therapy targeting tissue-nonspecific alkaline phosphatase (TNSALP), originally developed for hypophosphatasia (HPP) — a rare inherited disorder of bone and mineral metabolism caused by ALPL gene loss-of-function mutations.
The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**, with a near-perfect model confidence score of 99.95%; however, **no clinical trials and no publications** currently support this direction.
The mechanistic rationale is considered weak, and this prediction is most likely attributable to a knowledge graph topological artefact rather than genuine biological relevance.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypophosphatasia (HPP) — bone and mineral metabolism disorder due to TNSALP deficiency |
| Predicted New Indication | Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| EU Market Status | Not marketed (0 authorizations in dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Asfotase alfa is a recombinant fusion protein that directly replaces deficient TNSALP activity. Its core mechanism involves hydrolyzing inorganic pyrophosphate (PPi) — a potent inhibitor of hydroxyapatite crystal formation — thereby unblocking the bone mineralization process. This highly tissue-targeted mechanism (bone, liver, kidney alkaline phosphatase) has proven efficacy in hypophosphatasia, where loss-of-function ALPL mutations cause PPi accumulation and defective skeletal and dental mineralization.

Mitochondrial OXPHOS disorders caused by nuclear DNA anomalies are a heterogeneous group of rare diseases affecting respiratory chain complexes I–V. The underlying pathophysiology centers on impaired ATP synthesis, increased reactive oxygen species, and disrupted mitochondrial membrane potential — mechanisms that are fundamentally distinct from the PPi-excess model of HPP. Although alkaline phosphatase activity appears in some peripheral mitochondrial function literature, the TNSALP isoform's primary substrates and tissue distribution have no established intersection with mitochondrial respiratory chain complex biology or nuclear-encoded subunit defects.

The internal mechanistic assessment for this prediction explicitly rates the connection as a probable false positive, driven by knowledge graph topological proximity: both HPP and mitochondrial OXPHOS disorders occupy adjacent nodes in the rare metabolic disease subgraph of the TxGNN knowledge graph. This is a well-recognized limitation of graph neural network-based prediction, where structural closeness does not imply mechanistic relevance. No supporting preclinical or clinical evidence was identified across ClinicalTrials.gov, ICTRP, and PubMed searches conducted on 2026-03-09.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No European Union marketing authorization records were retrieved for Asfotase alfa in the current dataset (0 licenses found).

> **Data note:** Asfotase alfa is known under the brand name Strensiq and has received regulatory approval in multiple jurisdictions for hypophosphatasia. The absence of authorization records here likely reflects a retrieval gap in the current evidence pack rather than a true absence of approval. Please verify directly against the EMA product database before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications in this evidence pack are at evidence level L5 (model prediction only), with zero supporting clinical trials or publications across all queries. For the top prediction specifically, the mechanistic assessment rates the TNSALP–OXPHOS connection as a likely false positive arising from knowledge graph topology, providing no biological basis to advance this candidate.

**To proceed, the following is needed:**

- **Resolve blocking data gap (DG001):** Retrieve TFDA SmPC warnings and contraindications before any safety assessment can proceed
- **Resolve high-priority data gap (DG002):** Confirm detailed MOA via DrugBank API to formally document the TNSALP/PPi pathway
- **Re-triage predicted indications:** Among the top 10 predictions, the mechanistic rationale is stronger for indications with secondary bone mineralization involvement — specifically **cystinosis** (rank 10, Fanconi syndrome → secondary rickets) and **lysosomal storage disease with skeletal involvement** (rank 6, secondary PPi dysregulation possible); these warrant targeted literature review before the top prediction is prioritized
- **Flag false-positive candidates for model feedback:** Esophageal varices (ranks 8–9) and familial ApoC-II deficiency (rank 7) have explicit "Hold" recommendations and no mechanistic basis; these should be excluded from further evaluation and flagged as potential knowledge graph artefacts for model refinement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

