---
layout: default
title: Selumetinib
parent: AI Predictions (L5)
nav_order: 535
evidence_level: L5
indication_count: 10
---

# Selumetinib
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

# Selumetinib: From NF1-Related Plexiform Neurofibroma to Familial Generalized Lentiginosis

## One-Sentence Summary

Selumetinib is a MEK1/2 inhibitor whose established use is in neurofibromatosis type 1 (NF1)-related plexiform neurofibromas, acting by blocking the RAS-MAPK signaling pathway.
The TxGNN model predicts it may be effective for **Familial Generalized Lentiginosis**,
but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — it is an AI-inference-only candidate with no direct evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | NF1-related plexiform neurofibroma (referenced in the drug's own repurposing rationale; not formally recorded as a local marketing authorization) |
| Predicted New Indication | Familial generalized lentiginosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| EU Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank for this evidence pack (High-severity data gap, DG002). Based on the information embedded in the evidence itself, Selumetinib is consistently described across multiple predicted-indication rationales as a **MEK1/2 inhibitor** that blocks the downstream RAS-MAPK signaling pathway — the same pathway already targeted in its known use for NF1-related plexiform neurofibromas.

Familial generalized lentiginosis sits within the broader RASopathy spectrum: related conditions such as LEOPARD syndrome / Noonan syndrome with multiple lentigines are caused by germline mutations in RAS-MAPK pathway genes (PTPN11, RAF1, BRAF). This creates a plausible, but indirect, mechanistic bridge between an MEK inhibitor and a lentiginosis phenotype.

However, the evidence pack's own rationale explicitly flags this link as "**僅為 TxGNN embedding 推論，無實際機轉驗證資料**" (an embedding-similarity inference only, without any actual mechanistic validation). No preclinical or clinical data connect selumetinib specifically to familial generalized lentiginosis — the prediction should be treated as a hypothesis-generating signal, not a validated pharmacological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

This drug currently has no marketing authorization on record in this evidence pack (market status: Not marketed / Not marketed; total licenses: 0).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK1/2 inhibitor; non-cytotoxic mechanism) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (familial generalized lentiginosis, TxGNN score 99.96%) has zero supporting clinical trials or literature — it is an L5, decision-stage S0 candidate based purely on knowledge-graph embedding similarity, with no mechanistic validation.
- Two Blocking/High-severity data gaps (label warnings/contraindications, and mechanism of action) currently prevent any safety pre-assessment (S1) for this drug in general.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official product label warnings/contraindications before any S1 safety screening.
- Resolve DG002 (High): obtain formal DrugBank/SmPC mechanism-of-action data to properly assess mechanistic relevance.
- Generate at least preclinical mechanistic evidence directly linking selumetinib to familial generalized lentiginosis before advancing past S0.
- **Note for portfolio consideration:** within this same prediction set, *peripheral nerve schwannoma* (rank 9, L2, decision-stage S2) is supported by a selumetinib-specific NF2 Phase 2 trial (NCT03095248) and 7 relevant publications, and shares the same NF2/merlin–MAPK mechanistic logic as the drug's established NF1 indication. This is a substantially stronger repurposing candidate and may warrant prioritized evaluation over the rank-1 prediction discussed here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

