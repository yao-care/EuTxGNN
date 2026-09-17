---
layout: default
title: Telmisartan
parent: AI Predictions (L5)
nav_order: 574
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan is an angiotensin II receptor blocker (ARB), and its original indication in this evidence pack is described in the context of hypertension management via AT1 receptor blockade. The TxGNN model predicts it may be effective for **Prinzmetal Angina**, but currently this prediction is supported only by the model's score, with **no clinical trials** and **no published literature** in the evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (inferred from ARB/AT1-blockade mechanism referenced in the evidence pack; no formal indication label data available) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in the evidence pack (flagged as a data gap). Based on the information that is available, Telmisartan is an angiotensin II receptor blocker (ARB) that works primarily by blocking the AT1 receptor to lower blood pressure and inhibit vascular remodeling.

Prinzmetal (variant) angina, however, is pathophysiologically driven by coronary artery smooth muscle spasm and is conventionally managed with calcium channel blockers or nitrates — pathways with no established mechanistic link to the renin-angiotensin-aldosterone system (RAAS). The evidence pack's own rationale explicitly notes that this candidate is a high-scoring model prediction **without substantive mechanistic support**.

In other words, this is a case where TxGNN generated a numerically high score, but the underlying pharmacology does not provide a plausible biological rationale for repurposing. This should be treated as a low-confidence, exploratory signal rather than a clinically actionable hypothesis.

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
This prediction is based solely on the TxGNN model score, with zero supporting clinical trials or literature, and the proposed mechanism (RAAS/AT1 blockade) has no established link to the pathophysiology of Prinzmetal angina (coronary vasospasm), which is conventionally treated via calcium channel blockers or nitrates.

**To proceed, the following is needed:**
- TFDA/EMA-approved label warnings and contraindications (currently a **Blocking** data gap — required before any Stage 1 safety screening can begin)
- Confirmed mechanism of action (MOA) data via DrugBank API (currently a **High**-severity data gap)
- Independent mechanistic or preclinical evidence specifically linking ARB pharmacology to coronary vasospasm before considering further investment in this indication
- Note: within this same prediction batch, **cerebral artery occlusion** and **intracerebral hemorrhage** show substantially stronger evidence (L2, "Proceed with Guardrails," supported by completed Phase 3/4 trials such as NCT01075698 and NCT02699645/TRIDENT). These may warrant separate, higher-priority evaluation ahead of the Prinzmetal angina candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

