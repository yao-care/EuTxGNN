---
layout: default
title: Lixisenatide
parent: AI Predictions (L5)
nav_order: 360
evidence_level: L5
indication_count: 10
---

# Lixisenatide
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

# Lixisenatide: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Lixisenatide is a GLP-1 receptor agonist established for type 2 diabetes mellitus (formal regulatory indication text not available in this jurisdiction, where the drug is currently unmarketed). The TxGNN model's top prediction is **Opsismodysplasia**, a rare skeletal dysplasia, but this is supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags the link as a knowledge-graph proximity artifact rather than a mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from regulatory licenses (drug not marketed in this jurisdiction); known class use is Type 2 Diabetes Mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 97.56% |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on known information, Lixisenatide is a GLP-1 receptor agonist that increases insulin secretion and reduces insulin resistance, with established use in type 2 diabetes mellitus.

Opsismodysplasia is a rare skeletal dysplasia caused by INPPL1 gene mutations. There is no known physiological connection between GLP-1 receptor signaling and this bone development pathway. The evidence pack's own repurposing rationale explicitly states the high TxGNN score likely reflects graph-proximity clustering rather than a mechanistic inference, and no preclinical or clinical data exist to substantiate the link.

Across all 10 TxGNN-ranked candidates for this drug, only one (rank 6, pancreatic agenesis) has any supporting literature, and even that single preclinical study (a tumor-cachexia rat model) addresses a different biological question than the predicted indication. This pattern — high model scores with consistently absent or mismatched external evidence — indicates the current signal is exploratory only and not yet actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked prediction (Opsismodysplasia).

*Note: One tangentially related preclinical study exists for a lower-ranked candidate (rank 6, pancreatic agenesis) — [Quintilhano et al., 2021, PMID 32911572](https://pubmed.ncbi.nlm.nih.gov/32911572/), Cell Biochemistry and Function — examining lixisenatide's effect on cachexia in tumor-bearing rats. This does not directly support pancreatic agenesis (a congenital PDX1/PTF1A-related disorder) and is not evidence for the top-ranked indication.*

---

## EU Market Information

Not currently marketed in this jurisdiction — 0 marketing authorizations on record.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: TFDA/label warnings and contraindications data are marked as a Blocking-severity gap (DG001) — this evaluation cannot proceed past initial safety screening (S1) without this data.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (Opsismodysplasia) has no clinical, preclinical, or literature support, and the mechanistic rationale is explicitly assessed as non-biological (graph-proximity artifact). Combined with a Blocking data gap on safety labeling and a High-severity gap on mechanism of action, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism of action data via DrugBank or equivalent source (DG002)
- Any preclinical or in vitro evidence directly linking GLP-1 receptor activity to skeletal/connective tissue pathways relevant to opsismodysplasia
- Re-screening of lower-ranked candidates (e.g., lipodystrophy-related indications) where a plausible metabolic mechanism exists, even though direct evidence is currently absent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

