---
layout: default
title: Tiratricol
parent: AI Predictions (L5)
nav_order: 596
evidence_level: L5
indication_count: 10
---

# Tiratricol
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

# Tiratricol: From Undocumented Original Indication to Migraine with Brainstem Aura

## One-Sentence Summary

Tiratricol (TRIAC) is identified in the evidence pack as a thyroid hormone receptor beta (TRβ) agonist; its original approved indication is not documented in this evidence pack, and the compound does not currently hold any EU marketing authorization. The TxGNN model predicts a possible effect on **Migraine with Brainstem Aura**, but this prediction is currently supported by **zero clinical trials** and **zero publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no approved indication on file) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 93.28% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Tiratricol is not available from DrugBank in this evidence pack. Contextual analysis, however, identifies the compound as triiodothyroacetic acid (TRIAC), a thyroid hormone metabolite that acts as a selective agonist of thyroid hormone receptor beta (TRβ).

Because the original indication is undocumented, the relationship between the drug's established use and the predicted new indication cannot be directly evaluated. The rationale offered for the migraine prediction rests on an indirect line of reasoning: thyroid dysfunction (both hyper- and hypothyroidism) is epidemiologically associated with a higher prevalence of migraine, but no direct evidence links TRIAC/TRβ agonism to brainstem excitability or trigeminovascular system activity, the pathways thought to underlie migraine with brainstem aura.

Confidence in this prediction is further weakened by a pattern visible across the drug's full prediction list: several lower-ranked candidates (e.g., polyp of vocal cord, middle ear, frontal sinus, and ureter) cluster together with no plausible shared mechanism, which is a signature of knowledge-graph embedding artifacts rather than genuine pharmacological signal. While the migraine-related predictions score higher and are mechanistically more plausible than the polyp cluster, the complete absence of clinical or literature corroboration means this should still be treated as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

Tiratricol currently holds no marketing authorization in the EU (0 licenses on file). No product name, dosage form, or approved indication text is therefore available.

## Safety Considerations

No verified safety data (key warnings, contraindications, or drug-drug interactions) is currently available for Tiratricol. Because the drug is not marketed in the EU, there is no Summary of Product Characteristics (SmPC) to consult. This absence of foundational safety information has been flagged as a **Blocking** data gap (DG001), which by itself prevents this candidate from advancing to the S1 safety pre-screening stage.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All predicted indications for Tiratricol, including the top-ranked Migraine with Brainstem Aura (93.28%), sit at Evidence Level L5 — model prediction only, with no supporting clinical trials or literature.
- A Blocking data gap on safety labeling (DG001) makes it impossible to complete even a preliminary safety assessment, and the lack of documented mechanism of action (DG002) prevents a rigorous mechanistic-plausibility review.

**To proceed, the following is needed:**
- Documented original indication(s) and a confirmed mechanism of action for Tiratricol (currently a data gap per DrugBank query, DG002)
- Product labeling equivalent to an SmPC (warnings, contraindications) to resolve the Blocking gap DG001
- At least one preclinical or observational study directly linking TRβ agonism to migraine pathophysiology (brainstem excitability, trigeminovascular activation) before advancing beyond decision stage S0
- Independent verification that the migraine and polyp prediction clusters are not artifacts of the TxGNN knowledge-graph embedding structure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

