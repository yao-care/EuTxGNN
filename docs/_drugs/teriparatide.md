---
layout: default
title: Teriparatide
parent: AI Predictions (L5)
nav_order: 584
evidence_level: L5
indication_count: 10
---

# Teriparatide
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

# Teriparatide: From Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

Teriparatide, the active 1-34 fragment of recombinant human parathyroid hormone, is an osteoanabolic agent long used for the treatment of osteoporosis. The TxGNN model's top-ranked prediction is **Duodenal Ulcer**, with a very high similarity score, but this candidate is currently supported by **zero clinical trials** and **zero publications**, and the evidence pack's own repurposing rationale flags it as likely model noise rather than a genuine biological signal. Overall evidence for this specific prediction is essentially absent, and the drug itself has no recorded EU marketing authorization in this dataset.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (inferred from supporting literature in this evidence pack; not present in structured license data) |
| Predicted New Indication | Duodenal Ulcer |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for teriparatide is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, teriparatide is a PTH(1-34) analogue that stimulates osteoblast activity and bone formation, and it is used clinically for osteoporosis and related bone-fragility conditions.

Duodenal ulcer is a mucosal, acid-peptic gastrointestinal disease with no established relationship to PTH-mediated bone anabolism. The repurposing rationale accompanying this specific prediction explicitly states that there is **no known mechanistic link** between PTH-class drugs and peptic ulcer pathology, and that no clinical or literature evidence supports this association. It characterizes the prediction as likely representing noise in the TxGNN embedding space rather than a validated signal for repositioning.

By contrast, other lower-ranked candidates in this same evidence pack are mechanistically coherent and empirically supported — most notably **pregnancy- and lactation-associated osteoporosis** (rank 8), where teriparatide's bone-anabolic mechanism directly applies and is already documented in real-world clinical use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU marketing authorizations are recorded for Teriparatide in this evidence pack (market status: Not marketed; 0 authorizations on file).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: TFDA/EMA label warnings and contraindications are marked as a Blocking data gap in this evidence pack and must be obtained before any safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Duodenal Ulcer) has no supporting clinical trials, no supporting literature, and no identified mechanistic plausibility — the evidence pack itself characterizes it as likely model noise. Combined with the absence of any EU marketing authorization and a Blocking safety data gap, this candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- TFDA/EMA-approved label warnings and contraindications (Blocking gap — required before any safety screening can occur)
- Verified mechanism-of-action documentation for Teriparatide (High-severity gap)
- If pursuing this candidate at all, independent confirmation of a plausible PTH–peptic ulcer mechanism, since none currently exists in the available evidence
- Consider re-prioritizing evaluation toward **pregnancy- and lactation-associated osteoporosis** (rank 8 in this same evidence pack), which is supported by 2 clinical trials and roughly 20 publications documenting real-world teriparatide use and offers a substantially stronger evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

