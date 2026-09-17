---
layout: default
title: Zonisamide
parent: AI Predictions (L5)
nav_order: 662
evidence_level: L5
indication_count: 10
---

# Zonisamide
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

# Zonisamide: From Epilepsy to Tourette Syndrome

## One-Sentence Summary

> Zonisamide is an antiepileptic drug, with literature in the evidence pack confirming its established use in partial-onset (focal) seizures.
> The TxGNN model's top-ranked prediction suggests it may be effective for **Tourette Syndrome**,
> but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure AI-model prediction with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (partial-onset/refractory seizures) — inferred from literature evidence in this pack; no formal EU marketing-authorization indication text is available |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap requiring a DrugBank API lookup). Based on the literature contained in this evidence pack, zonisamide is a broad-spectrum antiepileptic drug approved for partial and generalized seizures, acting through sodium- and T-type calcium-channel blockade and weak carbonic anhydrase inhibition.

Epilepsy and Tourette syndrome are both neurological conditions rooted in abnormal neuronal excitability and dysregulated neurotransmission, which is the general basis on which anticonvulsants are sometimes explored for tic disorders. The rationale note attached to this prediction states that zonisamide has a weak dopamine-modulating effect that could theoretically benefit tic symptoms, referencing isolated Japanese clinical observations — but this rationale is explicitly described as **theoretical only**, with no clinical trial or peer-reviewed literature in this dataset to support it.

Given the score (99.85%) is a raw TxGNN knowledge-graph output ranked far down the model's overall prediction list (global rank 2081) and is entirely unaccompanied by real-world evidence, this candidate should be treated as a hypothesis-generating signal rather than a validated repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

No EU marketing authorization records are available for this product in the current dataset (0 licenses on file; market status: Not marketed).

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug-drug interaction data are not yet available in this evidence pack; retrieval of the TFDA/EMA product label is flagged as a blocking data gap.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- This is an L5, decision-stage S0 prediction: a high TxGNN score alone, with zero clinical trials and zero literature to corroborate a mechanistic or clinical link to Tourette syndrome.
- Safety pre-assessment (Stage S1) cannot begin because product label warnings and contraindications are a blocking data gap (DG001).

**To proceed, the following is needed:**
- Retrieve the TFDA/EMA product label (SmPC) for warnings, contraindications, and DDI data (DG001, Blocking)
- Confirm mechanism of action via DrugBank API query (DG002, High)
- Identify any preclinical or case-level evidence specifically linking zonisamide to Tourette syndrome or tic disorders
- For comparison, note that this same evidence pack contains two higher-evidence zonisamide candidates worth independent evaluation: **absence epilepsy** (L2, S2, "Proceed with Guardrails" — supported by Phase 3 trials and case-series literature) and **manic bipolar affective disorder** (L2, S2, "Research Question" — supported by an RCT, though underpowered)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

