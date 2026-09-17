---
layout: default
title: Florbetapir 18F
parent: AI Predictions (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
---

# Florbetapir 18F
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

# Florbetapir (18F): From Alzheimer's Amyloid PET Imaging to Bronchitis

## One-Sentence Summary

Florbetapir (18F) is not a therapeutic drug — it is an amyloid-beta-binding PET radiotracer used solely to visualize cerebral amyloid plaques as an aid in diagnosing Alzheimer's disease. The TxGNN model predicts it may be effective for **Bronchitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags the link as biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not applicable — diagnostic PET imaging agent (aid in Alzheimer's disease diagnosis), not an approved therapeutic; no marketing licenses on record |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Florbetapir (18F) is not available in DrugBank (flagged as a High-severity data gap in this evidence pack). Based on the information that is available — including the model's own repurposing rationale — Florbetapir (18F) is an ¹⁸F-labeled radiotracer that binds selectively to amyloid-beta plaques in the brain, used exclusively in PET imaging to support Alzheimer's disease diagnosis. It has no cytotoxic, anti-inflammatory, antimicrobial, or bronchodilatory activity and is not designed or dosed for systemic therapeutic effect.

Bronchitis is an infectious/inflammatory airway condition with an entirely different pathophysiology (pathogen-driven or irritant-driven airway inflammation) from cerebral amyloid deposition. The evidence pack's own mechanistic annotation for this candidate states directly that there is "no known pharmacological mechanism to explain a treatment effect on bronchitis" and that the high TxGNN score "lacks biological plausibility support." The same disconnect applies to the other nine top-ranked candidates (rheumatoid arthritis, bronchial neoplasm, two rare congenital syndromes, gout, headache disorder, trigeminal autonomic cephalalgia, laryngotracheitis, and osteoarthritis susceptibility) — each rationale explicitly notes the absence of any plausible pharmacological link to Florbetapir's amyloid-binding, diagnostic-only mode of action.

In short, the high TxGNN score reflects a graph-embedding similarity pattern rather than a grounded pharmacological hypothesis, and should be treated as exploratory model output only, not as a signal warranting further investment at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Florbetapir (18F) is a diagnostic radiotracer, not a therapeutic agent, and the top-ranked TxGNN prediction (bronchitis) has zero supporting clinical trials or literature and no plausible mechanistic link — a pattern that repeats across all ten top-ranked candidates in this evidence pack. Combined with the drug having no marketing licenses and no available label/safety data, this candidate does not meet the bar to advance past model-prediction stage (S0).

**To proceed, the following is needed:**
- DrugBank API query to fill the MOA data gap (DG002)
- TFDA/EMA label (仿單) retrieval to close the safety data gap (DG001), currently blocking S1 entry
- A mechanistic plausibility re-review, given the drug's diagnostic (non-therapeutic) classification, before committing further evidence-collection resources
- If pursued, preclinical/in vitro evidence generation, since no clinical or observational data currently exist for any of the ten predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

