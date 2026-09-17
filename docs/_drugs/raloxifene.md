---
layout: default
title: Raloxifene
parent: AI Predictions (L5)
nav_order: 487
evidence_level: L5
indication_count: 10
---

# Raloxifene
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

# Raloxifene: From Postmenopausal Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

Raloxifene is a selective estrogen receptor modulator (SERM) established for postmenopausal osteoporosis. The TxGNN model's top-ranked prediction for this drug is **Duodenal Ulcer**, but currently **no clinical trials** and **no literature** support this direction — the evidence pack itself flags this as a likely knowledge-graph noise artifact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Postmenopausal osteoporosis / prevention of vertebral fractures (not present in EU license registry data — see Data Gap DG001; sourced from supporting literature in this pack) |
| Predicted New Indication | Duodenal Ulcer (disease) |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on information available in this evidence pack, Raloxifene is a nonsteroidal selective estrogen receptor modulator (SERM), and its efficacy in postmenopausal osteoporosis / prevention of non-traumatic vertebral fractures has been established in the literature associated with this dataset.

However, for the top-ranked predicted indication — duodenal ulcer — the evidence pack's own mechanistic assessment concludes there is **no known relationship** between SERM pharmacology and duodenal ulcer pathophysiology (which is primarily driven by *H. pylori* infection and gastric acid secretion). The rationale explicitly characterizes this as a "graph noise-type prediction" from TxGNN, meaning the high similarity score likely reflects structural proximity in the knowledge graph rather than a biologically plausible therapeutic link. No supporting clinical or literature evidence exists to counter this assessment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No marketing authorizations are recorded for this drug in the current dataset. Market status is listed as **Not marketed (Not marketed)**, with **0 total licenses** — this itself is flagged as a data gap requiring verification against the official EU/EMA registry (see DG001).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: This evidence pack marks TFDA/label warnings and contraindications (DG001, Blocking severity) as unresolved, and mechanism-of-action data (DG002, High severity) as unresolved. These gaps currently prevent progression to a full safety review (Stage S1).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (duodenal ulcer) has zero supporting clinical trials or literature (Evidence Level L5, Decision Stage S0), and the pack's own mechanistic rationale identifies it as a likely spurious knowledge-graph prediction with no plausible pharmacological basis. Combined with a Blocking-severity gap in safety/label data, there is currently insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Resolve DG001: Obtain TFDA/EMA label warnings and contraindications (required before any Stage S1 safety evaluation)
- Resolve DG002: Retrieve confirmed mechanism of action via DrugBank API
- Verify EU marketing authorization status directly against EMA registry, as "0 licenses / not marketed" is inconsistent with Raloxifene's known market history and should be confirmed rather than assumed accurate
- Conduct a targeted literature/clinical trial search specific to "duodenal ulcer" to confirm the absence of a genuine signal before closing this candidate
- If repurposing potential is still of interest, consider re-examining lower-ranked candidates with clearer mechanistic coherence (e.g., rank 8, pregnancy-associated osteoporosis, which reached L3/S1 but carries a conflicting teratogenicity contraindication) rather than pursuing the top-ranked but noise-flagged prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

