---
layout: default
title: Riluzole
parent: AI Predictions (L5)
nav_order: 505
evidence_level: L5
indication_count: 10
---

# Riluzole
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

# Riluzole: From an Undocumented Original Indication to Bilateral Parasagittal Parieto-Occipital Polymicrogyria

## One-Sentence Summary

Riluzole's original indication is not recorded in this dataset's regulatory data (0 EU authorizations on file), though literature captured elsewhere in this evidence pack confirms it is an established glutamate-modulating therapy for amyotrophic lateral sclerosis (ALS). The TxGNN model's top-ranked prediction is **Bilateral Parasagittal Parieto-Occipital Polymicrogyria**, a rare cortical malformation, but this pairing has **zero clinical trials** and **zero publications** supporting it, and the model's own rationale flags the link as biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in regulatory dataset (this evidence pack's own literature indicates established use in ALS — see note below) |
| Predicted New Indication | Bilateral Parasagittal Parieto-Occipital Polymicrogyria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed (0 authorizations on file) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Riluzole is not available in this evidence pack. What can be reconstructed from the data itself is notable: several lower-ranked predictions in this pack (ranks 3, 5, 6, 7, 8, 10) all fall within the motor neuron disease spectrum, and the literature attached to rank 8 ("amyotrophic lateral sclerosis, susceptibility to") repeatedly identifies Riluzole as *"the only drug... shown to modestly prolong survival"* in ALS via inhibition of glutamatergic neurotransmission. This strongly suggests Riluzole's true, well-established indication is ALS — even though the `original_indications` field in this dataset is empty, which appears to be a data gap rather than a true absence of prior approval.

Against that backdrop, the **rank 1 prediction (Bilateral Parasagittal Parieto-Occipital Polymicrogyria)** does not hold up. This is a neuronal migration/cortical development disorder, not a neurodegenerative motor neuron condition. The model's own repurposing rationale explicitly states there is "no clear pathophysiological connection" to Riluzole's anti-glutamatergic/neuroprotective mechanism, and attributes the high TxGNN score to **knowledge-graph node proximity rather than genuine mechanistic relevance**. No clinical trial or literature evidence exists to counter this concern.

In short: this specific top-ranked candidate should be treated as a low-confidence, model-only signal. If a genuine repurposing opportunity exists in this dataset, it is more plausibly found among the motor-neuron-disease-adjacent candidates further down the ranked list (e.g., lower motor neuron syndrome with late-adult onset, monomelic amyotrophy, Mills syndrome), which share overlapping excitotoxic/motor neuron degeneration mechanisms with Riluzole's known pharmacology — though these too currently lack direct clinical trial or literature support and are marked only as "Research Question."

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

No EU marketing authorization records are available for Riluzole in this dataset. Market status is recorded as **Not Marketed**, with **0 licenses** on file — this itself is likely a data gap given Riluzole's known long-standing EU approval history for ALS, and should be verified against the EMA register before any downstream decision-making.

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: key warnings, contraindications, and DDI data are all recorded as blocking data gaps in this evidence pack — see "To proceed" below.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Bilateral Parasagittal Parieto-Occipital Polymicrogyria) has no clinical trial or literature support, sits at the lowest evidence tier (L5), and the model's own rationale describes the mechanistic link as implausible / likely a graph-topology artifact. There is no basis to advance this specific candidate.

**To proceed, the following is needed:**
- Resolve the `original_indications` / EU licensing data gap for Riluzole — regulatory records show 0 authorizations, which conflicts with literature in this same pack indicating established ALS use; this should be reconciled against the EMA register.
- Obtain TFDA/EMA label warnings and contraindications (currently a **Blocking** gap — DG001) before any safety evaluation (S1) can proceed.
- Obtain confirmed mechanism-of-action data via DrugBank (currently a **High severity** gap — DG002).
- If pursuing repurposing in the motor-neuron-disease space, redirect evaluation toward the mechanistically coherent candidates in this pack (e.g., lower motor neuron syndrome with late-adult onset, monomelic amyotrophy, Mills syndrome, ALS type 22) rather than the rank 1 candidate, and actively source clinical trial/literature evidence for those specific diagnoses.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

