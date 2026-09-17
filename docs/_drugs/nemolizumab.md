---
layout: default
title: Nemolizumab
parent: AI Predictions (L5)
nav_order: 409
evidence_level: L5
indication_count: 10
---

# Nemolizumab
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

# Nemolizumab: From Pruritus-Related Dermatitis to Diabetic Cataract

## One-Sentence Summary

> Nemolizumab is an anti-IL-31 receptor A (IL-31RA) monoclonal antibody used for pruritus-associated conditions such as atopic dermatitis and prurigo nodularis.
> The TxGNN model predicts it may be effective for **Diabetic Cataract**,
> but **no clinical trials** and **no publications** currently support this direction — this is a model-only prediction with no independent mechanistic evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indications on file) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.55% |
| Evidence Level | L5 |
| EU Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Nemolizumab is an anti-IL-31RA monoclonal antibody that blocks the itch-signaling pathway in sensory neurons and keratinocytes, and is clinically used for pruritic skin conditions such as atopic dermatitis and prurigo nodularis.

There is no established mechanistic link between IL-31/IL-31RA signaling and diabetic cataract pathophysiology, which is driven primarily by hyperglycemia-induced polyol pathway activation, sorbitol accumulation, and oxidative stress in the lens — not by IL-31-dependent inflammation. Notably, this drug's entire top-10 predicted indication list is dominated by cataract subtypes and stages (diabetic, tetanic, immature, mature, nuclear senile, cortical, senile cataract) plus diabetic retinopathy, none of which are independently or mechanistically tied to IL-31RA blockade.

This clustering pattern strongly suggests the TxGNN prediction reflects a **knowledge graph artifact** — likely driven by shared indirect nodes (e.g., diabetes-related comorbidity edges) — rather than a genuine pharmacological signal. No supporting clinical or preclinical evidence currently exists for any of these predicted indications.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No EU marketing authorizations on file — this drug is currently **not marketed** (Not marketed) with 0 registered licenses.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: Warnings, contraindications, and DDI data are currently unavailable — flagged as a Blocking data gap (DG001) that must be resolved before any safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by an L5 TxGNN model score with zero clinical trials, zero literature, and no plausible mechanistic link — the clustering of unrelated cataract subtypes across the top-10 predictions strongly indicates knowledge-graph noise rather than a genuine repurposing signal. Combined with the drug's non-marketed status in the EU and missing safety data, there is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/regulatory label warnings and contraindications) — currently Blocking
- Resolve DG002 (confirmed mechanism of action) to properly assess mechanistic plausibility
- Independent preclinical evidence establishing any IL-31/IL-31RA involvement in lens pathology or diabetic ocular complications
- Re-evaluate once EU marketing authorization status is established, or deprioritize in favor of higher-scoring, mechanistically coherent candidates from this drug's prediction set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

