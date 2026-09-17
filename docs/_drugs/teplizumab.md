---
layout: default
title: Teplizumab
parent: AI Predictions (L5)
nav_order: 581
evidence_level: L5
indication_count: 10
---

# Teplizumab
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

# Teplizumab: From Type 1 Diabetes (Delay of Onset) to Diabetic Cataract

## One-Sentence Summary

Teplizumab is an anti-CD3 monoclonal antibody, known for its use in delaying the onset of Type 1 diabetes mellitus through immune modulation and regulatory T-cell induction.
The TxGNN model predicts it may be effective for **Diabetic Cataract**,
but this direction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags the mechanistic link as a likely knowledge-graph false positive.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 1 diabetes mellitus (delay of onset) — not yet EU-authorized |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.38% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available from DrugBank for this evaluation. Based on known drug information, Teplizumab is an anti-CD3 monoclonal antibody used to delay the onset of Type 1 diabetes mellitus through an immune-modulatory mechanism (induction of regulatory T-cells).

The top-ranked predicted indications in this evidence pack are largely different forms of cataract (diabetic cataract, mature/immature cataract, senile cataract, cortical/nuclear cataract, tetanic cataract, craniostenosis cataract). However, the repurposing rationale accompanying each prediction explicitly assesses these links as **mechanistically implausible**: cataract pathophysiology is driven by lens protein denaturation, osmotic imbalance, oxidative stress, or accumulation of advanced glycation end-products — none of which are addressed by T-cell-mediated immune modulation. The evidence pack attributes the high TxGNN scores to a shared "diabetes" node in the knowledge graph connecting Teplizumab to multiple cataract subtypes, rather than a genuine causal or biological pathway. One prediction (antithrombin deficiency type 2) is even further removed, being a genetic coagulation disorder with no plausible connection to Teplizumab's mechanism.

Given this explicit self-assessment of low biological plausibility, combined with a complete absence of supporting clinical or literature evidence, none of the top 10 predicted indications currently justify further investment without independent mechanistic validation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

Teplizumab currently has no EU marketing authorization (0 licenses on record; market status: Not marketed).

## Safety Considerations

Please refer to the SmPC for safety information. Detailed warnings, contraindications, and drug-drug interaction data are not yet available for this compound in the current evidence pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All top-ranked predictions are TxGNN model output only (L5, decision stage S0) with no supporting clinical trials or literature, and the evidence pack's own mechanistic review identifies the drug–disease link as a likely knowledge-graph false positive driven by a shared "diabetes" node rather than genuine pharmacological rationale.

**To proceed, the following is needed:**
- TFDA/EMA product label warnings and contraindications (currently a Blocking data gap — required before any S1 safety pre-evaluation can proceed)
- Confirmed mechanism of action (MOA) data from DrugBank to properly assess mechanistic relevance
- Independent literature or preclinical evidence directly linking anti-CD3/immune-modulatory therapy to cataract pathophysiology, given the current rationale suggests none exists
- Re-evaluation of lower-ranked or alternative predicted indications that may have stronger mechanistic grounding (e.g., autoimmune or T-cell-mediated conditions more aligned with Teplizumab's known MOA)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

