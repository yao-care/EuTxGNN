---
layout: default
title: Tildrakizumab
parent: AI Predictions (L5)
nav_order: 592
evidence_level: L5
indication_count: 10
---

# Tildrakizumab
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

# Tildrakizumab: From Undocumented Original Indication to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Tildrakizumab (DrugBank ID DB14004) is referenced in the model's rationale as an anti-IL-23p19 monoclonal antibody, but its original approved indication and detailed mechanism of action are not available in the current data source. The TxGNN model predicts potential efficacy in **Severe Nonproliferative Diabetic Retinopathy**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own analysis flags the underlying mechanistic link as speculative rather than established.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current data source (Data Gap) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Tildrakizumab is not available in the current data source (Data Gap, DG002). Based on the drug class information referenced in the model's own rationale text, Tildrakizumab is an anti-IL-23p19 monoclonal antibody, a class typically used to treat IL-23/Th17-driven autoimmune inflammatory conditions.

The predicted new indication, severe nonproliferative diabetic retinopathy, is not a classical autoimmune disease. Chronic inflammation and neovascularization in diabetic retinopathy have been loosely described in the literature as having some relationship with the IL-23/Th17 axis, but this connection is indirect and not supported by direct molecular pathway evidence.

Importantly, the evidence pack itself flags this prediction as likely reflecting structural similarity between inflammation- and cytokine-related nodes in the TxGNN knowledge graph rather than a genuine pharmacological relationship. This concern is reinforced by a notable pattern among this drug's other top-10 predictions: several distinct cataract subtypes (ranks #5–#10) share near-identical or exactly identical scores, which is consistent with an embedding-cluster artifact rather than independent biological signals. Because the original indication and MOA for Tildrakizumab are both undocumented in this data source, no reliable mechanistic chain linking the drug to diabetic retinopathy can currently be established.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

Tildrakizumab currently has no marketing authorization records in this dataset (market status: **Not Marketed**, total authorizations: **0**).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate sits at Evidence Level L5 (AI prediction only, no clinical trials or literature), and the mechanistic rationale supplied for the prediction is explicitly flagged as speculative and possibly an artifact of knowledge-graph node clustering. Combined with the absence of original indication, MOA, and safety data, this candidate does not currently meet the minimum evidence bar to advance beyond S0.

**To proceed, the following is needed:**
- TFDA/EMA product label warnings and contraindications (Blocking gap, DG001)
- Detailed mechanism of action data via DrugBank query (DG002)
- Documentation of Tildrakizumab's original approved indication and regulatory status
- Preclinical or mechanistic studies directly linking IL-23p19 inhibition to diabetic retinopathy pathophysiology
- Any clinical trial or case-report evidence specific to this indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

