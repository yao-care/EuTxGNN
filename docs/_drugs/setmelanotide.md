---
layout: default
title: Setmelanotide
parent: AI Predictions (L5)
nav_order: 537
evidence_level: L5
indication_count: 10
---

# Setmelanotide
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

# Setmelanotide: From Genetic Obesity Syndromes to Migraine Disorder

## One-Sentence Summary

> Setmelanotide is an MC4R (melanocortin-4 receptor) agonist originally developed for rare genetic obesity syndromes such as Bardet-Biedl syndrome and POMC/PCSK1/LEPR deficiency.
> The TxGNN model predicts it may also be effective for **Migraine Disorder**,
> but this prediction is currently supported by **zero clinical trials** and **zero publications** — it is a pure knowledge-graph inference with no direct mechanistic or clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Genetic obesity syndromes (e.g., Bardet-Biedl syndrome, POMC/PCSK1/LEPR deficiency) — not captured in EU license data since the drug is not yet marketed in the EU |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 92.25% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (`[Data Gap]`). Based on information embedded in the model's rationale, Setmelanotide is an **MC4R agonist** acting on the hypothalamic melanocortin system, primarily regulating energy homeostasis and appetite. Its proven original indications are rare genetic obesity syndromes, several of which (e.g., Bardet-Biedl syndrome) involve broader hypothalamic-pituitary dysfunction beyond simple weight regulation.

The proposed link to migraine rests on the fact that melanocortin receptors (MC1R/MC4R) are expressed in the trigeminovascular system and central pain-modulation pathways — a plausible but indirect anatomical overlap. However, there is **no direct literature support** for a causal relationship between MC4R agonism and migraine, and the theoretical direction of effect is unclear: MC4R activation does not have an established relationship with the vasodilatory mechanisms classically implicated in migraine pathophysiology.

In short, this prediction is best understood as a **knowledge-graph topological association** (shared receptor family / pathway proximity) rather than a mechanistically or clinically validated hypothesis. It should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU marketing authorization data available. Setmelanotide is currently **not marketed** in the EU under this dataset (0 licenses on file).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: Key warnings, contraindications, and DDI data are currently unavailable — flagged as a Blocking data gap (DG001) that must be resolved before any safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-only prediction with no clinical trials, no supporting literature, and no direct mechanistic evidence linking MC4R agonism to migraine. Combined with missing TFDA/SmPC safety data (Blocking gap) and missing formal MOA confirmation (High-severity gap), there is insufficient basis to advance this candidate beyond hypothesis stage.

**To proceed, the following is needed:**
- TFDA/SmPC label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank API — currently a High-severity data gap (DG002)
- Targeted literature search on MC4R/melanocortin system involvement in trigeminovascular pain pathways
- If mechanistic rationale is substantiated, consider preclinical/translational studies before any clinical trial design

*Note: Nine additional low-confidence candidates (migraine with brainstem aura, esophageal disorders, amenorrhea, cauda equina syndrome, neurogenic bladder, hypertrichosis, pituitary dwarfism) were also flagged by TxGNN, all at L5 evidence level with "Hold" recommendations. Several (amenorrhea, hypertrichosis, pituitary dwarfism) show comparatively stronger — though still indirect — mechanistic plausibility via the POMC/melanocortin axis and may warrant lower-priority mechanistic review.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

