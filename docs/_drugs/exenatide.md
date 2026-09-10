---
layout: default
title: Exenatide
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 10
---

# Exenatide
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

# Exenatide: From Type 2 Diabetes Mellitus to Primary Hereditary Glaucoma

## One-Sentence Summary

Exenatide (DB01276) is a GLP-1 receptor agonist originally developed for type 2 diabetes mellitus. The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, but this pairing currently has **no supporting clinical trials or published literature** — the signal is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (based on known pharmacology; not present in the supplied regulatory record) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 96.21% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate. Based on known information, Exenatide is a GLP-1 receptor agonist (incretin mimetic), and its efficacy in type 2 diabetes mellitus is well established through its effects on insulin secretion and glucose metabolism.

The link between a GLP-1 agonist and primary hereditary glaucoma is not obvious pharmacologically, and the evidence pack contains **no clinical trials, ICTRP records, or literature** connecting exenatide to this specific disease (rank 29,062 out of the full TxGNN candidate list). The high TxGNN score therefore reflects a graph-based similarity signal rather than any observed or mechanistically documented effect, and should be treated as a hypothesis-generating result only, not a validated pharmacological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support, no available mechanism-of-action data, and the drug is not currently marketed in the EU dataset provided — the prediction rests solely on the TxGNN model score (Evidence Level L5).

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- Preclinical/mechanistic evidence linking GLP-1 receptor activity to intraocular pressure or glaucoma pathophysiology
- TFDA/EMA label warnings and contraindications (currently a Blocking data gap per meta.data_gaps DG001)
- Confirmation of EU marketing status and any existing ophthalmic-relevant safety signals before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

