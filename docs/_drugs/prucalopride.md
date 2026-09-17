---
layout: default
title: Prucalopride
parent: AI Predictions (L5)
nav_order: 486
evidence_level: L5
indication_count: 10
---

# Prucalopride
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

# Prucalopride: From Gastrointestinal Motility Disorder to Hypoalphalipoproteinemia

## One-Sentence Summary

> Prucalopride is a selective 5-HT4 receptor agonist known for its prokinetic effect on gastrointestinal smooth muscle, used clinically to promote bowel motility.
> The TxGNN model predicts it may be effective for **Hypoalphalipoproteinemia** (low HDL cholesterol) with a score of **99.82%**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the drug's own known mechanism has no established link to lipid metabolism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in source data (drug not marketed in the EU); pharmacologically known as a GI prokinetic agent |
| Predicted New Indication | Hypoalphalipoproteinemia (low HDL cholesterol) |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (`original_moa` is marked as a data gap). However, the evidence pack's own rationale identifies prucalopride as a selective 5-HT4 receptor agonist whose established pharmacology acts on gastrointestinal smooth muscle to promote motility (prokinetic effect) — consistent with its known clinical use for bowel motility disorders such as chronic constipation.

There is no known biological pathway connecting 5-HT4 receptor agonism to HDL/lipoprotein metabolism, which is the pathophysiological basis of hypoalphalipoproteinemia. The evidence pack itself explicitly states that this top-ranked prediction "likely reflects a knowledge-graph co-occurrence pattern rather than genuine biological plausibility." In other words, the high TxGNN score is not corroborated by a credible mechanistic story, and no clinical trials or literature currently exist to support it.

Notably, several lower-ranked predictions in this same output (amyloidosis and primary amyloidosis, ranks 6 and 9) have a mechanistically coherent rationale — amyloid deposition can affect the enteric autonomic nervous system and cause GI motility impairment, which is plausibly addressable by a prokinetic agent — and are backed by preliminary literature. These may warrant separate evaluation, but they are not the top-ranked candidate covered by this report.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note:** A blocking data gap exists — TFDA/EU label warnings and contraindications have not yet been retrieved, which prevents progression to the S1 safety review stage for any candidate indication of this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (hypoalphalipoproteinemia) has no clinical trial or literature support (Evidence Level L5) and lacks a credible mechanistic link to the drug's known pharmacology. In addition, a blocking data gap in label safety information prevents any candidate from advancing to formal safety review.

**To proceed, the following is needed:**
- Retrieve TFDA/EU label warnings and contraindications (blocking gap, DG001)
- Confirm mechanism of action via DrugBank API (DG002)
- If pursuing repurposing further, prioritize mechanistically plausible candidates from this prediction set (e.g., amyloidosis-associated GI motility disorders) over the top TxGNN-ranked but mechanistically unsupported hypoalphalipoproteinemia indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

