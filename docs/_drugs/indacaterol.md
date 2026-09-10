---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 10
---

# Indacaterol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Indacaterol: From Chronic Obstructive Pulmonary Disease to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Indacaterol is a long-acting inhaled β2-adrenergic agonist (LABA), publicly known for its established use in chronic obstructive pulmonary disease (COPD) and asthma maintenance therapy. The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | COPD (chronic obstructive pulmonary disease) — *note: this Evidence Pack contains no Taiwan/EU marketing-authorization or original-indication data; this is based on the drug's publicly known profile, not pack data* |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (flagged as a Blocking/High-severity data gap in the source pack). Based on known information, indacaterol is a long-acting β2-adrenergic receptor agonist, and its efficacy in COPD/asthma bronchodilation is well established; mechanistically, this activity does not have a documented pathway relevant to NSIAD.

NSIAD is caused by a gain-of-function mutation in the vasopressin V2 receptor, leading to inappropriate water retention independent of vasopressin levels. There is no known pharmacological interaction between β2-adrenergic agonism and V2 receptor signaling. The evidence pack's own rationale is explicit on this point: this pairing has **no established mechanistic link**, no clinical trials, and no literature support — it reflects the TxGNN model's statistical prediction score alone.

Given the absence of both mechanistic plausibility and empirical evidence, this specific drug–indication pair should be treated as a low-confidence, exploratory signal rather than a near-term repurposing candidate.

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
This candidate is supported only by a TxGNN model score (L5, no clinical or literature evidence), and the proposed mechanism has no known biological basis connecting β2-agonism to the V2-receptor-driven pathology of NSIAD.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for indacaterol (currently a Blocking data gap)
- Preclinical or mechanistic studies exploring any indirect link between β2-adrenergic signaling and vasopressin V2 receptor activity
- TFDA/EMA label warnings and contraindications (currently a Blocking data gap, required before any S1 safety review)
- Ongoing monitoring for emerging clinical trial or case-report evidence

*Note: within this same Evidence Pack, a separate predicted indication ("bronchial disease," rank 7) shows substantially stronger support — L1 evidence level with multiple completed Phase 3 trials and 20 publications — but reflects indacaterol's already-established core pharmacology (COPD/asthma) rather than a novel repurposing signal. This report follows the pack's designated top-ranked candidate (NSIAD) per the specified extraction rule.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

