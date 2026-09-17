---
layout: default
title: Fluciclovine 18F
parent: AI Predictions (L5)
nav_order: 259
evidence_level: L5
indication_count: 10
---

# Fluciclovine 18F
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

# Fluciclovine (18F): From Oncologic PET Imaging to Trichotillomania

## One-Sentence Summary

Fluciclovine (18F) is a radiolabeled amino acid PET imaging agent used solely for oncologic diagnostic imaging (e.g., prostate cancer detection), not a therapeutic drug with an established pharmacological indication. The TxGNN model predicts a possible association with **Trichotillomania**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own rationale flags it as likely knowledge-graph structural noise rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diagnostic PET imaging agent for oncologic imaging (e.g., prostate cancer) — not an approved therapeutic indication |
| Predicted New Indication | Trichotillomania |
| TxGNN Prediction Score | 97.86% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (MOA: Data Gap). Based on known information, Fluciclovine (18F) is anti-1-amino-3-[18F]fluorocyclobutane-1-carboxylic acid, a synthetic amino acid analog used exclusively as a PET radiotracer for tumor imaging. It is taken up by cells via amino acid transporters (e.g., ASCT2/LAT1) to visualize increased amino acid transport in malignant tissue — it has no established pharmacodynamic or therapeutic mechanism.

Trichotillomania is a neuropsychiatric impulse-control disorder with no known pathophysiological link to amino acid transporter-mediated tumor imaging. The evidence pack's own repurposing rationale explicitly states there is "no mechanistic association" between the drug and this disease, and characterizes the high TxGNN score as "very likely knowledge-graph structural noise."

This pattern repeats across all 10 of the model's top-ranked predictions for this drug (Tourette syndrome, migraine, erectile dysfunction, POTS, various arrhythmias, hyperthyroidism) — none have a plausible mechanistic rationale, and none are supported by real-world clinical or literature evidence. This strongly suggests the high TxGNN scores reflect an artifact of the knowledge graph embedding rather than a credible repurposing signal, likely because a purely diagnostic agent with sparse graph connections receives unstable similarity-based predictions.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Fluciclovine (18F) is a diagnostic PET imaging agent with no established therapeutic mechanism of action, and none of its top 10 TxGNN-predicted indications (all L5, decision stage S0) are supported by clinical trial or literature evidence — the only incidentally matched trial (NCT06064097, for hyperthyroidism) was graded "C" relevance and assessed as database noise, not real evidence. The prediction lacks both mechanistic plausibility and empirical support.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (currently Data Gap, DG002)
- TFDA label warnings/contraindications (currently Data Gap, DG001 — Blocking severity)
- An independent pharmacological plausibility review to determine whether a diagnostic-only agent is a valid repurposing candidate at all
- Continued monitoring for any emerging clinical or literature evidence before revisiting this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

