---
layout: default
title: Teprotumumab
parent: AI Predictions (L5)
nav_order: 582
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab: From Undocumented Original Indication to Monosomy X

## One-Sentence Summary

Teprotumumab's originally approved indication and mechanism of action are not documented in this Evidence Pack, and the drug currently has no marketing authorization in the EU.
The TxGNN model predicts a possible association with **Monosomy X** (the karyotype underlying Turner syndrome),
but this candidate is currently supported by **0 clinical trials** and **0 publications**, and its mechanistic rationale has not yet been assessed.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (drug not authorized in the EU) |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Teprotumumab is not available in this Evidence Pack, and no original indication has been recorded. Based on general knowledge of the drug class, Teprotumumab is an IGF-1 receptor (IGF-1R) monoclonal antibody antagonist, but this Evidence Pack does not document a confirmed original indication or approved use, so no direct comparison between an "original indication" and "Monosomy X" can be made at this time.

For the top-ranked prediction (Monosomy X), the mechanistic-link and similarity-to-original-indication fields in the Evidence Pack are explicitly marked as **pending** — meaning the biological rationale has not yet been reviewed or validated by the pipeline. This is notable because several other predictions for this same drug (esophageal varices, mitochondrial OXPHOS disorders, varicose disease) were reviewed and flagged with **Hold** recommendations, with reviewers noting only weak or indirect mechanistic links (e.g., IGF-1's general association with metabolic/hepatic pathways) and no evidence of a causal pharmacological pathway supporting repurposing. This pattern suggests the TxGNN signal for this drug may reflect knowledge-graph co-occurrence rather than a validated mechanism, and the Monosomy X prediction should be treated with similar caution until a dedicated mechanistic review is completed.

It is also worth noting that several of the top 10 predictions for this drug (ranks 1, 4, 6, 7, 8, 10) cluster around sex-chromosome disorders and Turner-syndrome-related karyotypes (monosomy X, mosaic monosomy X, Turner syndrome due to structural X anomalies, mixed gonadal dysgenesis, sex chromosome disorder of sex development). This clustering may indicate a shared knowledge-graph neighborhood (e.g., growth-related or endocrine nodes) rather than independent, mechanism-driven signals for each condition — a pattern that warrants scrutiny before any of these candidates advance.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## EU Market Information

Teprotumumab currently has no EU marketing authorization (market status: **not marketed**, 0 authorizations on file). No dosage forms, brand names, or approved indication text are available for the EU market.

## Safety Considerations

Please refer to the SmPC for safety information.

> Note: This Evidence Pack flags the absence of TFDA/label warnings and contraindications as a **Blocking** data gap (DG001), meaning a formal safety pre-screen (S1) cannot be completed until this information is obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Monosomy X) has zero supporting clinical trials or literature, and its mechanistic rationale is explicitly unassessed ("pending") in the Evidence Pack. Combined with the absence of the drug's original indication, mechanism of action, and any EU marketing authorization, there is currently insufficient basis to advance this candidate beyond an AI-prediction-only stage.

**To proceed, the following is needed:**
- Confirm Teprotumumab's original approved indication and mechanism of action (query DrugBank API, per DG002)
- Obtain TFDA/SmPC warnings and contraindications to complete the S1 safety pre-screen (per DG001, Blocking)
- Complete mechanistic-link and similarity-to-original-indication review for the Monosomy X prediction (currently marked "pending")
- Conduct a targeted literature/clinical-trial search for IGF-1R pathway involvement in Turner syndrome or monosomy X-related growth/endocrine phenotypes
- Clarify EU regulatory status and any prior submission history, given the current "not marketed" designation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

