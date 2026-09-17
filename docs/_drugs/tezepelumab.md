---
layout: default
title: Tezepelumab
parent: AI Predictions (L5)
nav_order: 586
evidence_level: L5
indication_count: 10
---

# Tezepelumab
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

# Tezepelumab: From Asthma to Diabetic Cataract

## One-Sentence Summary

Tezepelumab is a monoclonal antibody that inhibits TSLP, and based on the mechanistic evidence available in this pack it is used for asthma and other respiratory allergic inflammatory diseases. The TxGNN model predicts it may be effective for **Diabetic Cataract**, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction that the evidence pack's own mechanistic review flags as biologically implausible.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma / respiratory allergic inflammatory disease (inferred from mechanistic rationale; no formal labeling data on file) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.40% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed MOA data for Tezepelumab is not on file in this evidence pack (flagged as a High-severity data gap). However, the repurposing rationale attached to each predicted indication consistently describes Tezepelumab as an inhibitor of thymic stromal lymphopoietin (TSLP), an epithelium-derived cytokine that triggers the Th2/inflammatory cascade, and states that the drug is mainly used for asthma and other respiratory allergic inflammatory diseases.

Diabetic cataract, by contrast, is driven by lens protein glycation, oxidative stress, and polyol-pathway dysregulation in the setting of chronic hyperglycemia — none of which have an established connection to the TSLP–Th2 axis. The evidence pack's own analysis attributes this prediction to an indirect knowledge-graph link through the shared "diabetes" node rather than to any genuine shared pathophysiology, and the same caveat applies to the other nine of the top ten predicted indications (mostly cataract subtypes of varying etiology: senile, cortical, nuclear, metabolic, and syndromic).

One partial exception is rank 10, diabetic retinopathy, where the rationale notes emerging (but still preliminary) evidence that TSLP/Th2-related inflammatory mediators may participate in retinal vascular inflammation and neovascularization — a marginally stronger, though still unproven, mechanistic hypothesis. Overall, mechanistic plausibility for this candidate set is low, and the prediction should be treated as hypothesis-generating rather than actionable.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## EU Market Information

Tezepelumab currently has **0 marketing authorizations** on record in this evidence pack, with market status listed as **Not marketed**. No license-level details (authorization number, product name, dosage form, or approved indication text) are available.

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All top-ranked predicted indications, including the leading candidate diabetic cataract, are supported only by TxGNN embedding similarity (L5) with zero clinical trials or literature evidence. The evidence pack's own mechanistic review identifies the shared "diabetes" node as a likely spurious knowledge-graph artifact rather than a genuine TSLP-mediated pathway, so this candidate does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- Authoritative confirmation of the original approved indication and label text (asthma) from EMA/DrugBank
- Formal MOA documentation to replace the current data gap (DG002)
- TFDA/EMA warnings, contraindications, and DDI data — this is currently a Blocking gap (DG001) that prevents any S1 safety assessment
- Preclinical or clinical evidence directly linking TSLP inhibition to lens pathology before this candidate can move beyond hypothesis stage
- If pursued further, prioritize diabetic retinopathy (rank 10) over the cataract cluster, given its comparatively stronger — though still preliminary — inflammatory mechanism rationale, and commission a targeted literature review on TSLP/Th2 involvement in retinal vascular disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

