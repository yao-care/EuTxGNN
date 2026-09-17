---
layout: default
title: Roflumilast
parent: AI Predictions (L5)
nav_order: 516
evidence_level: L5
indication_count: 10
---

# Roflumilast
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

# Roflumilast: From COPD to Pulmonary Hypertension

## One-Sentence Summary

> Roflumilast is a selective phosphodiesterase-4 (PDE4) inhibitor used to reduce exacerbations in patients with severe COPD.
> The TxGNN model predicts it may be effective for **Pulmonary Hypertension**,
> but this prediction is currently supported by **no clinical trials** and **no literature**, and the underlying mechanistic link is considered weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Obstructive Pulmonary Disease (COPD), per pharmacovigilance literature in this evidence pack |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 97.24% |
| Evidence Level | L5 (AI prediction only, no supporting studies) |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (blocking data gap). Based on known information, Roflumilast is a selective PDE4 inhibitor that reduces cAMP breakdown, producing anti-inflammatory effects that have proven efficacy in severe COPD.

The proposed link to pulmonary hypertension is mechanistically weak. PDE4 inhibition has some theoretical anti-inflammatory and vascular-remodeling-modulating effects, which could plausibly influence pulmonary vascular remodeling. However, the dominant pharmacology for approved PH therapies (e.g., sildenafil, tadalafil) acts through PDE5 inhibition and the cGMP pathway — a mechanistically distinct target from PDE4/cAMP. This is a pure AI-predicted association with no clinical or preclinical data currently supporting it.

Given this gap between the predicted mechanism and the established PH treatment pathway, this candidate should be treated as a hypothesis-generation signal only, not as a validated repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Roflumilast currently has no marketing authorization on record in this system (market status: **not marketed**, 0 authorizations). No product-level data is available for review.

---

## Safety Considerations

No formal SmPC-level warnings, contraindications, or drug-drug interaction data are available for this drug (blocking data gap — TFDA/EMA label not yet retrieved).

However, evidence collected under a separate predicted-indication entry ("headache disorder," rank 3) flags an important safety signal: clinical trial and real-world pharmacovigilance data consistently identify **headache, weight loss, decreased appetite, insomnia, diarrhea, vomiting, and nausea** as common adverse effects of Roflumilast, occurring mainly early in treatment (trial NCT02018432; pharmacovigilance analyses PMID [41458197](https://pubmed.ncbi.nlm.nih.gov/41458197/) and PMID [41602587](https://pubmed.ncbi.nlm.nih.gov/41602587/)). This is a known class effect of PDE4 inhibitors and should be treated as a **safety consideration for the drug itself**, not as a repurposing opportunity — the TxGNN model's prediction of "headache disorder" as a treatable indication is directionally inconsistent with the actual evidence and should not be pursued.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (pulmonary hypertension) has no clinical trial or literature support and rests on a mechanistically weak link (PDE4 vs. the PDE5-dominant PH treatment pathway). Combined with the absence of basic label-level safety data and the drug's current unmarketed status, there is insufficient evidence to advance this candidate beyond model prediction.

**To proceed, the following is needed:**
- Retrieve TFDA/EMA label safety data (warnings, contraindications) — currently a blocking gap
- Obtain detailed MOA data from DrugBank to properly assess mechanistic plausibility
- Preclinical or mechanistic studies specifically testing PDE4 inhibition in pulmonary vascular remodeling/PH models
- Clarify and separately track the headache/adverse-effect signal so it is not conflated with genuine repurposing candidates
- Consider evaluating higher-evidence candidates in this pack instead — e.g., "female breast carcinoma" (rank 4, L4, in vitro mechanistic data available) offers a more substantive starting hypothesis than the top-ranked PH prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

