---
layout: default
title: Ublituximab
parent: AI Predictions (L5)
nav_order: 624
evidence_level: L5
indication_count: 10
---

# Ublituximab
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

# Ublituximab: From CD20+ B-Cell-Targeted Therapy to Diabetic Cataract

## One-Sentence Summary

Ublituximab is a CD20-targeted monoclonal antibody; no original approved indication or EU marketing authorization is on file in this Evidence Pack.
The TxGNN model predicts it may be effective for **Diabetic Cataract**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the accompanying mechanistic review found **no plausible biological link** between B-cell depletion and cataract formation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (no marketing authorization or approved indication text on file) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.57% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Ublituximab is not available in this Evidence Pack, and there is no original approved indication on file — the drug currently holds no EU marketing authorization. The only mechanistic clue available comes from the embedded rationale text, which identifies Ublituximab as a CD20-targeted (anti-CD20) monoclonal antibody that acts by depleting CD20+ B cells.

The TxGNN model's top 10 predictions for this drug are dominated almost entirely by a single disease cluster: various forms of cataract (diabetic cataract, mature cataract, cortical cataract, nuclear senile cataract, immature cataract, tetanic cataract, craniostenosis cataract) plus diabetic retinopathy. All of these are structural or metabolic ophthalmic conditions — driven by lens protein oxidation, glycation, aggregation, age-related degeneration, or VEGF-driven microvascular damage — rather than B-cell-mediated autoimmune processes.

For every one of the top-10 candidates, the domain rationale explicitly concludes there is no plausible mechanistic link between CD20+ B-cell depletion and lens or retinal pathology. A single drug landing on a tight cluster of mechanistically unrelated eye-lens diseases with near-identical, very high scores (98.3%–98.6%) is a classic signature of knowledge-graph embedding noise rather than a genuine biological signal, and is consistent with the "Hold" decision assigned to this candidate at stage S0.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No EU marketing authorization is currently on file for Ublituximab as of the data cutoff (2026-09-17); the drug is not marketed in the EU and no license records are available for review.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> Note: This Evidence Pack flags a **Blocking** data gap (DG001) — no TFDA/EMA label warnings or contraindications are on file — which prevents this candidate from entering the S1 safety pre-screen stage.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (and all top-10 predictions) lack any supporting clinical trial or literature evidence (L5), and the mechanistic review found no credible biological rationale linking CD20+ B-cell depletion to cataract or diabetic retinopathy pathology. A blocking data gap on the drug's safety label also prevents progression to safety pre-screening.

**To proceed, the following is needed:**
- Confirmed mechanism of action and original approved indication(s) from DrugBank/EMA SmPC (High-severity data gap DG002)
- Official EU/TFDA product label with warnings and contraindications (Blocking data gap DG001)
- Independent review of the TxGNN output to rule out an embedding-noise artifact, e.g. by checking whether this drug scores higher for other B-cell/autoimmune-mediated indications outside this ocular cluster
- If pursuing further, preclinical or mechanistic evidence establishing an immune-mediated pathway in lens or retinal disease, which is currently absent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

