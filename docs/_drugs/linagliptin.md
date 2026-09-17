---
layout: default
title: Linagliptin
parent: AI Predictions (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
---

# Linagliptin
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

# Linagliptin: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

> Linagliptin is a DPP-4 inhibitor used to regulate blood glucose in type 2 diabetes mellitus (as referenced in the drug's own evidence base).
> The TxGNN model's top-ranked prediction is **Opsismodysplasia**, a rare skeletal dysplasia, but this candidate is currently supported by **0 clinical trials** and **0 publications** — the score reflects knowledge-graph embedding similarity only, with no identified biological mechanism connecting the two.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (DPP-4 inhibitor; not present in a structured license record — see note below) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 94.90% |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

*Note: No `taiwan_regulatory.licenses` records exist for this drug, so the original indication above is inferred from the mechanistic descriptions embedded in the evidence pack's rationale and literature fields, not from a formal license text.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Linagliptin is not available (flagged as a High-severity data gap). Based on the information present in the evidence pack, Linagliptin acts through DPP-4 inhibition on the incretin/GLP-1 pathway to regulate blood glucose in type 2 diabetes.

The evidence pack's own rationale for this candidate is explicit that **no known biological connection exists** between this mechanism and opsismodysplasia. Opsismodysplasia is a skeletal developmental disorder caused by *INPPL1* gene mutations — a structural/genetic bone condition unrelated to glucose or incretin regulation. The high TxGNN score (94.90%, rank 37,382 of the full prediction set) reflects similarity in the model's learned embedding space rather than a pharmacologically plausible mechanism.

Given this, the prediction should be treated as a hypothesis-generating signal only, not as evidence of therapeutic potential.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (opsismodysplasia) has no clinical trial or literature support, and the evidence pack's own mechanistic analysis finds no biological plausibility linking DPP-4 inhibition to this rare skeletal disorder. This is an L5, model-only signal.

**To proceed, the following is needed:**
- TFDA/EMA-equivalent label warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action (MOA) data from DrugBank or another authoritative source (currently a High-severity data gap)
- A biologically grounded hypothesis connecting Linagliptin's pharmacology to opsismodysplasia (or reconsideration of lower-ranked candidates, e.g. rank 8, pancreatic agenesis, which at least returned related literature, though still lacking direct mechanistic support)
- DDI data (current query returned "not_found") before any combination-therapy consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

