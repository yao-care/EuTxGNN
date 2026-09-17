---
layout: default
title: Tafamidis
parent: AI Predictions (L5)
nav_order: 562
evidence_level: L5
indication_count: 10
---

# Tafamidis
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

# Tafamidis: From Transthyretin Amyloidosis to Primary Release Disorder of Platelets

## One-Sentence Summary

Tafamidis is a transthyretin (TTR) tetramer stabilizer whose established clinical use, as reflected throughout the Evidence Pack's literature and trial data, is transthyretin amyloidosis (ATTR-CM/ATTR-PN). The TxGNN model's top-ranked prediction in this pack is **Primary Release Disorder of Platelets**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure knowledge-graph similarity output with no mechanistic or clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in structured regulatory data (see Data Gap DG002); literature/trial evidence elsewhere in this pack (e.g., NEJM 2018, PMID 30145929) indicates the established use is transthyretin (ATTR) amyloidosis/cardiomyopathy |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 89.27% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Tafamidis is not available as a structured field (Data Gap DG002, High severity). However, the evidence pack's own literature and trial titles consistently identify Tafamidis as a small-molecule TTR tetramer stabilizer that prevents dissociation and misfolding of transthyretin into amyloid fibrils — this is the mechanism underlying its established use in transthyretin amyloidosis.

There is no known biological pathway connecting TTR tetramer stabilization to primary platelet release disorders. Platelet release defects arise from abnormalities in platelet granule content or secretion machinery, a biological domain unrelated to hepatic protein misfolding. The repurposing rationale attached to this candidate explicitly states that the prediction reflects only TxGNN knowledge-graph embedding similarity, without any clinical or mechanistic basis.

Notably, this Evidence Pack also contains several other predicted indications for Tafamidis (e.g., "primary amyloidosis," rank 5, and "acquired amyloid peripheral neuropathy," rank 6) that are strongly supported by Phase 3/4 trials and RCTs — but these correspond mechanistically to the drug's known/approved ATTR indications rather than genuine repurposing candidates. By contrast, the rank-1 candidate reviewed here (platelet release disorder) has neither mechanistic plausibility nor supporting evidence and should be treated as a low-confidence, exploratory hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No EU marketing authorizations are currently on file for Tafamidis in this Evidence Pack (market status: **Not Marketed**, total licenses: 0).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: Safety warning and contraindication fields in this Evidence Pack are flagged as a Blocking data gap — DG001 — meaning safety review cannot proceed to initial S1 assessment until TFDA/EMA label data is retrieved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (primary release disorder of platelets) has no clinical trials, no literature, and no plausible mechanistic link to Tafamidis's known TTR-stabilizing activity — it sits at Evidence Level L5 / Decision Stage S0, the lowest confidence tier in this framework.

**To proceed, the following is needed:**
- Resolve Data Gap DG001 (TFDA/EMA label warnings and contraindications) — currently blocking any safety assessment (S1)
- Resolve Data Gap DG002 (confirmed mechanism of action) to properly evaluate mechanistic plausibility
- Obtain confirmed original indication and regulatory licensing data (currently absent from `taiwan_regulatory`)
- If repurposing is still of interest, consider redirecting evaluation toward the pack's higher-evidence candidates (e.g., rank 5 "primary amyloidosis" [L1] and rank 6 "acquired amyloid peripheral neuropathy" [L2]) after confirming with a domain expert whether these represent genuine new indications or already-approved uses mislabeled due to disease-ontology mapping noise (as flagged for the "dermis disease" entry, rank 8)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

