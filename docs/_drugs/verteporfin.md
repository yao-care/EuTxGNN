---
layout: default
title: Verteporfin
parent: AI Predictions (L5)
nav_order: 641
evidence_level: L5
indication_count: 10
---

# Verteporfin
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

# Verteporfin: From Age-Related Macular Degeneration to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

Verteporfin is a photosensitizing agent developed for photodynamic therapy (PDT) of choroidal neovascularization in wet age-related macular degeneration. The TxGNN model predicts potential efficacy for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**, but this direction is currently supported by **zero clinical trials** and **zero publications** — it is a pure graph-based association with no known mechanistic pathway.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Choroidal neovascularization / wet age-related macular degeneration (photodynamic therapy) — inferred from drug class; not present in the structured `original_indications` field |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.49% (graph rank #5,563) |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured record. Based on known information, Verteporfin is a **photosensitizer / YAP inhibitor**: upon light activation it generates reactive oxygen species that occlude abnormal vasculature (its approved ophthalmic PDT use), and independent of light activation it is also known to inhibit the YAP/TAZ–TEAD transcriptional axis of the Hippo pathway.

For this specific predicted indication, however, the evidence pack's own rationale is explicit that **no known mechanistic pathway connects Verteporfin to nuclear-DNA-related mitochondrial oxidative phosphorylation disorders**. Neither the vascular-occlusion (PDT) mechanism nor the YAP-inhibition mechanism has an established link to nuclear-DNA-encoded OXPHOS complex assembly or mitochondrial bioenergetics. The high TxGNN score therefore reflects a knowledge-graph pattern association rather than a biologically grounded hypothesis, and should be treated as a hypothesis-generation signal only, not as mechanistically supported repurposing evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This predicted indication has no supporting clinical trials or literature, and the mechanistic rationale explicitly notes the absence of any known pathway linking Verteporfin to nuclear-DNA-associated mitochondrial OXPHOS disorders. The evidence level (L5) reflects a model-prediction-only signal, which does not meet the threshold to advance beyond hypothesis stage (S0).

**To proceed, the following is needed:**
- Verteporfin's detailed mechanism of action data (currently flagged as a blocking/high-severity data gap; DrugBank API query pending)
- TFDA/regulatory label warnings and contraindications (currently a blocking data gap for any safety pre-screening; requires SmPC/label retrieval)
- Preclinical or mechanistic studies directly testing Verteporfin's effect on nuclear-DNA-encoded OXPHOS complex function or mitochondrial disease models
- Independent expert review of the TxGNN graph association before any further prioritization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

