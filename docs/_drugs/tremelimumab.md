---
layout: default
title: Tremelimumab
parent: AI Predictions (L5)
nav_order: 617
evidence_level: L5
indication_count: 10
---

# Tremelimumab
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

# Tremelimumab: From Anti-CTLA-4 Immunotherapy to Diabetic Cataract

## One-Sentence Summary

Tremelimumab is an anti-CTLA-4 immune checkpoint inhibitor; detailed data on its original approved indication and mechanism of action are not available in this Evidence Pack. The TxGNN model's top-ranked predicted indication is **Diabetic Cataract**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the model's own rationale text explicitly flags the mechanistic link as biologically implausible — most likely an artifact of shared knowledge-graph embeddings rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this Evidence Pack (`original_indications` is empty; MOA recorded as a data gap) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Tremelimumab is not available from DrugBank in this Evidence Pack (flagged as data gap DG002). However, the model's own rationale text identifies it as an **anti-CTLA-4 immune checkpoint inhibitor**, whose pharmacology centers on activating T cells and blocking immune tolerance — a mechanism used to enhance anti-tumour immune responses.

This mechanism has **no established biological connection** to diabetic cataract, whose pathophysiology is driven by metabolic and osmotic stress (e.g., sorbitol accumulation via the polyol pathway) and oxidative damage to lens proteins — processes unrelated to T-cell checkpoint signalling. Notably, all top 10 TxGNN predictions for this drug are cataract subtypes (diabetic, mature, immature, senile, nuclear, cortical, tetanic, craniostenosis-associated) clustered within a very narrow and nearly identical score range (98.2%–98.5%), which strongly suggests the model is picking up a shared knowledge-graph node (e.g., diabetes-related genes/phenotypes) rather than an independent, indication-specific mechanistic signal.

More importantly, the directionality of this prediction runs **counter to known pharmacology**: CTLA-4 checkpoint inhibitors are well-documented to *cause* immune-related ocular adverse events (e.g., uveitis) and can trigger autoimmune (type 1-like) diabetes as an immune-related adverse event (irAE). This means Tremelimumab is more plausibly a **risk factor** for ocular and metabolic complications than a candidate therapy for cataract or diabetic retinopathy. Based on the evidence available, this prediction should be treated as a modelling artifact rather than a credible repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 top-ranked predicted indications for Tremelimumab are cataract-related conditions with near-identical scores, zero supporting clinical trials, zero supporting literature (Evidence Level L5), and an explicit mechanistic rationale indicating the link is likely a knowledge-graph embedding artifact rather than a true signal. Furthermore, the drug's known immune-activating mechanism is more consistent with causing ocular/metabolic adverse events than treating them, so this candidate should not advance past initial screening.

**To proceed, the following is needed:**
- Original mechanism of action (MOA) data from DrugBank (data gap DG002)
- TFDA/EMA product label warnings and contraindications (data gap DG001, blocking for S1 safety pre-screening)
- Independent preclinical or mechanistic validation to rule out this being a KG embedding artifact before any further evaluation
- Review of TxGNN embedding quality for this drug, given the anomalous clustering of near-identical scores across multiple cataract subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

