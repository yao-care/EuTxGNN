---
layout: default
title: Tadalafil
parent: AI Predictions (L5)
nav_order: 561
evidence_level: L5
indication_count: 10
---

# Tadalafil
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

# Tadalafil: From PDE5 Inhibitor Therapy to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

> Tadalafil is a phosphodiesterase type 5 (PDE5) inhibitor; detailed original-indication and mechanism-of-action data are not available in this evidence pack, though the pack's own annotations reference its established use in pulmonary arterial hypertension.
> The TxGNN model's top prediction is **Ambras type hypertrichosis universalis congenita**, a rare congenital generalized hypertrichosis syndrome, but this pairing is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic review finds no plausible biological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for tadalafil (DB00820) is not available in this evidence pack (flagged as data gap DG002). Elsewhere in the pack's own rationale notes, tadalafil is repeatedly identified as a PDE5 inhibitor that produces vascular smooth-muscle relaxation via the cGMP pathway, and is noted as already approved for pulmonary arterial hypertension — the only predicted indication in this batch (kyphoscoliotic heart disease, rank 7) where this mechanism offers a coherent, if untested, rationale.

For the top-ranked prediction, Ambras type hypertrichosis universalis congenita, the evidence pack's own assessment concludes there is **no plausible biological link**: this is a rare congenital generalized hair-overgrowth syndrome with no known pathological connection to PDE5/cGMP-mediated vasodilation. The high TxGNN score most likely reflects noise from a sparsely connected knowledge-graph node rather than a genuine biological hypothesis.

Across all 10 predictions reviewed in this evidence pack, none reached a decision stage beyond S1, and every prediction is scored "Hold." Two predictions (migraine with brainstem aura, migraine disorder) are supported by a single case report describing tadalafil-associated migraine aura — this is a potential **adverse effect signal**, not evidence of therapeutic benefit. Overall, this evidence pack does not currently support tadalafil as a viable repurposing candidate for its top-ranked indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU marketing authorization records are currently on file for this drug in this evidence pack (market status: Not Marketed; 0 licenses recorded).

---

## Safety Considerations

Please refer to the SmPC for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack — this is flagged as a **blocking data gap (DG001)** that prevents progression to the initial safety-screening stage (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No predicted indication in this evidence pack — including the top-ranked Ambras type hypertrichosis universalis congenita — is supported by clinical trial or literature evidence directly implicating tadalafil's mechanism. The model's own mechanistic review explicitly finds no plausible biological rationale for the top prediction, and the two predictions with any literature support (migraine-related) point to a possible adverse-effect signal rather than a therapeutic opportunity. Core drug-level data (mechanism of action, label warnings/contraindications) are also missing, which independently blocks safety evaluation.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: obtain EMA/EU SmPC warnings and contraindications
- Resolve DG002: retrieve confirmed mechanism-of-action data from the DrugBank API
- If pursuing the pulmonary-hypertension-related hypothesis (kyphoscoliotic heart disease, rank 7), conduct a targeted literature and trial search, since tadalafil's existing PAH approval provides the only mechanistically coherent lead in this prediction set
- Route the migraine-related findings to pharmacovigilance review as a potential adverse-effect signal rather than a repurposing lead
- Re-run evidence collection once EU marketing authorization and safety data become available, as the current record shows the drug as not marketed with zero licenses on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

