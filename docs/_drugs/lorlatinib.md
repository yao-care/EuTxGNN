---
layout: default
title: Lorlatinib
parent: AI Predictions (L5)
nav_order: 365
evidence_level: L5
indication_count: 10
---

# Lorlatinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Lorlatinib: From ALK-Positive NSCLC to Gingival Fibromatosis

## One-Sentence Summary

Lorlatinib is a third-generation ALK/ROS1 tyrosine kinase inhibitor; per literature evidence in this pack it is used for ALK-positive metastatic non-small cell lung cancer (NSCLC), though the drug's formal original indication and EU authorization status are Data Gaps in this record. The TxGNN model's top-ranked prediction is **Gingival Fibromatosis**, but this pairing has **0 clinical trials** and **0 publications** supporting it — it is a pure AI embedding-similarity signal with no mechanistic basis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this dataset (Data Gap). Literature evidence in this pack consistently describes lorlatinib as a treatment for ALK-positive NSCLC. |
| Predicted New Indication | Gingival Fibromatosis (fibromatosis, gingival) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| EU Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Lorlatinib in this evidence pack (flagged as Blocking/High data gaps DG001–DG002). Based on the literature evidence collected elsewhere in this pack (e.g., PMID 38554546, PMID 33207094), Lorlatinib is a brain-penetrant, third-generation ALK/ROS1 tyrosine kinase inhibitor with demonstrated efficacy in ALK-positive metastatic NSCLC, most notably in the Phase 3 CROWN trial.

Gingival fibromatosis is a benign, non-neoplastic overgrowth of gingival connective tissue, typically driven by fibroblast proliferation and extracellular matrix accumulation — a pathway with no established link to ALK or ROS1 kinase signaling. The evidence pack's own rationale field is explicit on this point: *"無已知機轉關聯...僅為 KG embedding 相似度預測，無支持文獻或試驗"* ("no known mechanistic link; this is a pure knowledge-graph embedding similarity prediction, with no supporting literature or trials"). There is no pharmacological or clinical rationale connecting the original indication to this predicted one — the signal should be treated as model noise rather than a genuine repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

Lorlatinib currently has **0 recorded authorizations** and a market status of "Not marketed" (Not marketed) in this evidence pack's regulatory dataset. No license records are available to summarize.

## Cytotoxicity

*(Included because lorlatinib is an antineoplastic agent per literature evidence in this pack — ALK/ROS1-targeted therapy for NSCLC.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor) — not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Low. Literature in this pack describes lorlatinib's adverse-event profile as dominated by metabolic effects (hypercholesterolemia, hypertriglyceridemia, weight gain) rather than classic myelosuppression (PMID 38554546, PMID 30890623); no formal hematotoxicity data available in this pack |
| Emetogenicity Classification | Low (typical of oral targeted kinase inhibitors; not formally assessed in this pack) |
| Monitoring Items | Fasting lipid panel (cholesterol, triglycerides), body weight, mood/cognitive status, pulmonary symptoms — based on literature signals for hyperlipidemia (PMID 39537504, 33789526), metabolic syndrome (PMID 40157899), and rare pulmonary toxicity/ARDS (PMID 31985497) |
| Handling Protection | Standard oral oncology drug handling applies; this pack contains no formal hazardous-drug classification — confirm against SmPC before establishing handling protocol |

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and DDI data are all marked as Data Gaps in this evidence pack, including a Blocking-severity gap for TFDA/EMA label warnings — DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (gingival fibromatosis) has zero clinical trials, zero literature evidence, and no plausible mechanistic link to lorlatinib's ALK/ROS1 pathway — the pack's own rationale field confirms this is a knowledge-graph artifact, not a scientific hypothesis worth pursuing.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/EMA SmPC warnings and contraindications before any safety review can begin
- Resolve DG002: obtain confirmed MOA and original indication/regulatory status for lorlatinib (currently empty/Data Gap despite being a marketed oncology drug elsewhere)
- If further repurposing signals from this drug are of interest, prioritize disease-ontology QC over raw TxGNN rank: rank 6 ("lung germ cell tumor") appears to be a mislabeled node — its cited literature is entirely about ALK-driven **neuroblastoma** (Phase 1 trial support exists), not germ cell tumors. Ranks 4 ("lung hilum carcinoma") and 5 ("lung benign neoplasm") are populated almost entirely by literature on the *already-approved* ALK+ NSCLC indication, not a genuine new indication
- Do not advance rank 1 (gingival fibromatosis) or the other zero-evidence L5 candidates (ranks 2, 3, 7, 8, 9, 10) without new supporting data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

