---
layout: default
title: Fenfluramine
parent: AI Predictions (L5)
nav_order: 248
evidence_level: L5
indication_count: 10
---

# Fenfluramine
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

# Fenfluramine: From Obesity (Historical, Withdrawn Use) to Proximal 16p11.2 Microdeletion Syndrome

## One-Sentence Summary

Fenfluramine is a serotonin-releasing agent historically used as an appetite suppressant (as part of the "fen-phen" combination) and later repurposed for treatment-resistant genetic epilepsies such as Dravet and Lennox-Gastaut syndrome. The TxGNN model's top-ranked prediction for this drug is **Proximal 16p11.2 Microdeletion Syndrome**, but this candidate currently has **no clinical trials and no supporting literature** — the model's own rationale text describes the mechanistic link as pure speculation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no Taiwan license record exists for this drug (0 authorizations); `drug.original_indications` is empty in this evidence pack |
| Predicted New Indication | Proximal 16p11.2 Microdeletion Syndrome |
| TxGNN Prediction Score | 99.93% (rank 1082 of all candidates) |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Taiwan Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this drug in the current evidence pack (flagged as data gap DG002, High severity). Based on information embedded elsewhere in this same evidence pack, Fenfluramine is known to act as a serotonin-releasing agent — historically used for appetite suppression, and more recently repurposed (outside the scope of this pack's structured data) for genetic epilepsy syndromes via serotonergic modulation.

For the top-ranked candidate, **Proximal 16p11.2 Microdeletion Syndrome**, the model's own rationale is explicit that no molecular pathway or clinical data supports the link: some patients with this syndrome present with an obesity/metabolic phenotype, which offers a loose conceptual bridge to fenfluramine's serotonergic appetite-suppressant activity — but this is characterized in the evidence pack itself as speculation ("屬臆測"), not a validated mechanistic hypothesis.

Notably, other lower-ranked candidates in this pack have somewhat stronger — though still unproven — rationale (e.g., fatty liver disease at rank 9, supported by obesity-pathophysiology reviews; and a seizure-associated neuronal migration disorder at rank 10, where an analogy to fenfluramine's approved epilepsy use is drawn). None of these reach a level of evidence sufficient to support the top-ranked indication being carried forward.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Fenfluramine currently holds **0 marketing authorizations** in Taiwan (market status: Not marketed / Not marketed). No license records, product names, dosage forms, or approved-indication text are available in this evidence pack.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this pack. Data gap DG001 — TFDA label warnings/contraindications — is rated **Blocking**, meaning this candidate cannot formally enter the S1 safety-review stage until resolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Proximal 16p11.2 Microdeletion Syndrome) has zero clinical trials, zero literature support, and is explicitly labeled speculative in the model's own rationale (L5, decision stage S0). Separately, a Blocking data gap on TFDA safety labeling (DG001) prevents any candidate for this drug from proceeding to formal safety evaluation regardless of indication-level evidence.

**To proceed, the following is needed:**
- TFDA label (仿單) warnings and contraindications for Fenfluramine (resolves Blocking gap DG001)
- Mechanism-of-action data via DrugBank API (resolves High-severity gap DG002)
- Any clinical trial or literature evidence directly linking fenfluramine to 16p11.2 microdeletion syndrome, beyond the current speculative metabolic-phenotype rationale
- If pursuing this drug further, consider evaluating the fatty liver disease (rank 9, L4) or epilepsy-adjacent (rank 10) candidates instead, which carry marginally more mechanistic plausibility — though both are also currently at Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

