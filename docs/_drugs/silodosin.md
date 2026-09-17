---
layout: default
title: Silodosin
parent: AI Predictions (L5)
nav_order: 540
evidence_level: L5
indication_count: 10
---

# Silodosin
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

# Silodosin: From Benign Prostatic Hyperplasia/LUTS to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

> Silodosin is a highly selective alpha-1A adrenergic receptor antagonist, pharmacologically classified for benign prostatic hyperplasia (BPH) and lower urinary tract symptoms (LUTS).
> The TxGNN model predicts a possible association with **Ambras type hypertrichosis universalis congenita**, a rare congenital hair-overgrowth disorder,
> but this prediction is currently supported by **zero clinical trials and zero literature**, and the model's own mechanistic rationale explicitly states there is no known biological pathway connecting the drug to this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the structured data provided; the drug class (alpha-1A antagonist) is typically indicated for BPH/LUTS |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (structured `original_moa` field is a data gap). Based on the mechanistic notes attached to this evidence pack, Silodosin is understood to be a highly selective alpha-1A adrenergic receptor antagonist, a class typically used to relax smooth muscle in the prostate and bladder neck for BPH/LUTS.

For the top-ranked predicted indication, the model's own mechanistic assessment states there is **no known interaction** between alpha-1A receptor antagonism and the genetic pathways implicated in congenital hypertrichosis (e.g., the 8q24 duplication region), and concludes there is **no reasonable mechanistic support** for this repurposing hypothesis. This is a case where the embedding-based similarity score is high, but the accompanying biological rationale explicitly contradicts plausibility.

This pattern repeats across the full candidate list: all 10 predicted indications in this evidence pack (ranks 1–10, covering hair/skin disorders, craniofacial malformation syndromes, and pulmonary/cardiovascular conditions) are scored **L5 (model prediction only)** with **Hold** recommendations, and for 9 of the 10, the rationale text explicitly states "no mechanistic link" (無機轉關聯). The one partial exception, chronic thromboembolic pulmonary hypertension (rank 10), notes a theoretical vascular-tone connection but immediately qualifies it as weak, since Silodosin's high alpha-1A selectivity was specifically designed to minimize systemic vascular effects (to avoid orthostatic hypotension).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

*(Note: literature was returned for the rank-3 candidate, "malformation syndrome with odontal and/or periodontal component," but all 20 records are general periodontitis research that do not mention Silodosin or alpha-1 adrenergic pathways — these appear to be keyword-overlap artifacts rather than drug-specific evidence, and are not included here as they do not pertain to the top-ranked indication.)*

## EU Market Information

No marketing authorizations are recorded for this drug in the provided data (`total_licenses: 0`, market status: **Not marketed**).

## Safety Considerations

Please refer to the SmPC for safety information.

**Important gap:** the drug label (warnings/contraindications) has not yet been retrieved from the regulatory source (severity: Blocking) — this currently prevents any formal safety pre-screening (S1 stage).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All 10 predicted indications are L5 (AI prediction only), with no supporting clinical trials or relevant literature.
- The model's own mechanistic rationale for the top-ranked indication states there is no known biological pathway connecting Silodosin to hair-growth regulation — this is a case of high similarity score without plausibility.
- The drug is not currently marketed in the target jurisdiction (0 authorizations), and core safety data (warnings/contraindications) is a **Blocking** data gap that prevents any downstream safety evaluation.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently Blocking
- Confirmed MOA data from DrugBank (currently a High-severity gap)
- An independent, disease-specific literature search (the current literature for rank 3 is not usable — it lacks any drug-specific relevance)
- If pursuing any candidate further, a documented biological mechanism linking alpha-1A antagonism to the target disease, since none currently exists in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

