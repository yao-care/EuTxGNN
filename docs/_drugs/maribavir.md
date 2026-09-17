---
layout: default
title: Maribavir
parent: AI Predictions (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
---

# Maribavir
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

# Maribavir: From CMV-Targeted Antiviral Therapy to Bronchitis (Predicted)

## One-Sentence Summary

> Maribavir is a UL97 kinase inhibitor developed to block cytomegalovirus (CMV) replication; it is not currently marketed in this jurisdiction and no approved indication is on file.
> The TxGNN model predicts a possible link to **Bronchitis**, but this ranks among the model's lowest-confidence outputs, with **0 clinical trials** and **0 publications** currently supporting the direction — and the evidence pack's own rationale notes no known biological connection between CMV suppression and bronchitis pathology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (drug not marketed; no approved indication text available) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 87.79% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation is a flagged data gap (DG002, High severity). However, the evidence pack's repurposing rationale indicates Maribavir is a **UL97 kinase inhibitor**, acting specifically against cytomegalovirus (CMV) replication — a narrow, virus-specific mechanism rather than a broad antimicrobial or anti-inflammatory action.

The rationale explicitly states there is **no known mechanistic link** between CMV replication inhibition and bronchitis, which is typically driven by bacterial/viral respiratory pathogens (often unrelated to CMV) or allergic inflammation. The evidence pack attributes the TxGNN score to likely indirect associations between viral-disease and respiratory-disease nodes within the knowledge graph, rather than a substantiated biological hypothesis.

This same pattern holds across all ten ranked predictions in this candidate set (bronchitis, diabetic retinopathy variants, filariasis, and several GI neoplasms) — each rationale independently notes the absence of a plausible mechanistic connection to Maribavir's CMV-targeted activity. This is a strong signal that the current prediction batch reflects model-level associations rather than biologically grounded repurposing candidates.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## EU Market Information

Maribavir is **not currently marketed** in this jurisdiction (0 authorizations on file), so no marketing authorization details are available for review.

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: TFDA/regulatory label warnings and contraindications (DG001) are flagged as a **Blocking** data gap — safety data cannot currently support a formal S1 safety screen.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All ten TxGNN-predicted indications for Maribavir are Evidence Level L5 (model prediction only) with zero supporting clinical trials or literature, and the model's own mechanistic rationale for the top candidate (bronchitis) states no known biological plausibility exists.
- A Blocking data gap (DG001 — missing TFDA warnings/contraindications) independently prevents progression to the S1 safety review stage regardless of indication-level evidence.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA (or applicable regulatory) label warnings and contraindications
- Resolve DG002: confirm detailed mechanism-of-action documentation via DrugBank API
- Generate or identify preclinical/mechanistic literature specifically linking CMV/UL97 pathway modulation to bronchitis (or a higher-ranked, mechanistically plausible indication) before advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

