---
layout: default
title: Sarilumab
parent: AI Predictions (L5)
nav_order: 528
evidence_level: L5
indication_count: 10
---

# Sarilumab
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

Using no additional skill — this is a direct content-generation task with a fully specified template; I'll follow the Evidence Pack extraction rules exactly.

# Sarilumab: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

> Sarilumab is a human monoclonal antibody blocking the IL-6 receptor alpha (IL-6Rα), originally developed for rheumatoid arthritis (per literature on file; the drug currently holds no formal marketing authorization in this dataset).
> The TxGNN model's top-ranked prediction is **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**,
> but this candidate currently has **0 clinical trials** and **0 publications** supporting it, and has been flagged by evidence review as a likely knowledge-graph noise signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (identified from literature evidence in this pack; no formal EU/Taiwan marketing authorization on file) |
| Predicted New Indication | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN Prediction Score | 98.50% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not directly recorded in the drug-level fields of this evidence pack. However, literature captured elsewhere in the pack (PMID 32451909) confirms that sarilumab is a human monoclonal antibody blocking the interleukin-6 receptor alpha (IL-6Rα), approved for moderately to severely active rheumatoid arthritis in adults with inadequate response or intolerance to conventional DMARDs.

Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a rare congenital disorder involving ocular coloboma/microphthalmia and skeletal (rhizomelic) dysplasia, driven by developmental gene abnormalities rather than cytokine-mediated inflammation. There is no known biological pathway connecting IL-6/IL-6R signaling to this developmental syndrome.

The evidence review explicitly concludes this is a knowledge-graph noise prediction: the TxGNN embedding score is high, but there is no mechanistic plausibility, no clinical trial activity, and no literature support. This prediction should not be interpreted as a genuine repurposing signal for sarilumab.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

Sarilumab currently holds no recorded marketing authorization in this dataset (market status: **Not marketed**; 0 authorizations on file).

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (colobomatous microphthalmia-rhizomelic dysplasia syndrome) has no supporting clinical trials, no supporting literature, and no plausible mechanistic link to IL-6Rα blockade — it is assessed as a model noise artifact rather than a genuine repurposing signal.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for sarilumab (currently a data gap, DG002)
- TFDA/EU label warnings and contraindications (currently a data gap, DG001; blocking for any safety pre-assessment)
- If repurposing exploration for sarilumab continues, evaluation should instead focus on the pack's mechanistically stronger candidates with existing L4 evidence — **inflammatory bowel disease** and **plasma cell myeloma** — both currently at decision stage S1 ("Research Question") rather than this noise-flagged L5 prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

