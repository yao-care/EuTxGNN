---
layout: default
title: Empagliflozin
parent: AI Predictions (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Empagliflozin
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

# Empagliflozin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Empagliflozin is an SGLT2 inhibitor originally developed for type 2 diabetes mellitus; detailed mechanism-of-action data for this candidate is currently unavailable (data gap, see below). The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome**, but this prediction currently has **0 supporting clinical trials** and **0 supporting publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (SGLT2 inhibitor class; no EU marketing-authorization record exists in this dataset) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack. Based on general knowledge, Empagliflozin belongs to the SGLT2 (sodium-glucose cotransporter-2) inhibitor class, which lowers blood glucose by blocking renal glucose reabsorption; its efficacy in type 2 diabetes mellitus (and related cardio-renal indications) is well established in the wider literature, even though no such authorization record appears in this dataset.

Classic Stiff Person Syndrome (SPS), however, is an autoimmune neurological disorder driven by anti-GAD65 antibodies that disrupt GABAergic neurotransmission. There is no known pharmacological overlap between GABAergic autoimmune neurotransmission and renal glucose-transporter inhibition.

The evidence pack's own repurposing rationale is explicit about this gap: it states the high TxGNN score for this candidate is most likely driven by knowledge-graph co-occurrence or embedding similarity rather than any genuine mechanistic relationship. In other words, this is a model-artifact-level prediction, not a mechanism-driven hypothesis, and should be treated accordingly.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Empagliflozin has no marketing authorization records in the current EU regulatory dataset (market status: Not Marketed, 0 authorizations on file).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Classic Stiff Person Syndrome) has no clinical trials, no supporting literature, and — per the model's own rationale — no known mechanistic link to Empagliflozin's SGLT2-inhibitory activity. The high TxGNN score most likely reflects graph-embedding similarity rather than biological plausibility, so this candidate does not currently warrant advancement.

**To proceed, the following is needed:**
- TFDA/EMA product labeling (warnings and contraindications) — currently a **Blocking** data gap (DG001), required before any safety pre-screening (S1) can occur
- Confirmed mechanism-of-action data for Empagliflozin — currently a **High**-severity data gap (DG002), needed for mechanistic-relevance analysis
- If this line of research continues, consider prioritizing lower-ranked candidates with at least partial metabolic/mechanistic plausibility instead (e.g., thiamine-responsive dysfunction syndrome, drug-induced/idiopathic lipodystrophy, or pancreatic agenesis — the latter already has 2 tangential PubMed records), rather than the top-ranked but mechanistically unsupported hit
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

