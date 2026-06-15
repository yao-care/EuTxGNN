---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Aprepitant
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

# Aprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Aprepitant is an NK1 (neurokinin 1) receptor antagonist approved in multiple countries for prevention of chemotherapy-induced nausea and vomiting (CINV) and post-operative nausea and vomiting (PONV).
The TxGNN model's top prediction places it as a candidate for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)** with a score of 99.97%,
however **zero clinical trials and zero publications** link Aprepitant to this condition, and no biologically plausible mechanism has been identified.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of chemotherapy-induced nausea and vomiting (CINV) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known information, Aprepitant is an NK1 (neurokinin 1) receptor antagonist that selectively blocks substance P — a neuropeptide involved in the vomiting reflex, neurogenic inflammation, and pain sensitization. Its clinical efficacy in preventing acute and delayed chemotherapy-induced nausea and vomiting is well-established, and it holds marketing authorizations in the US, EU, and Japan, though it is not currently approved in Taiwan.

NSIAD is a rare X-linked condition caused by constitutive gain-of-function mutations in the *AVPR2* gene encoding the V2 vasopressin receptor. This leads to unregulated water retention and persistent dilutional hyponatremia independent of circulating vasopressin levels. Critically, the NK1/substance P signaling pathway has no established biochemical crosstalk with the AVPR2/cAMP/aquaporin-2 (AQP2) axis that underlies this syndrome. There is no known mechanism by which blocking substance P would suppress constitutively active V2 receptor signaling or reduce pathological water reabsorption.

The high TxGNN score (99.97%) most likely reflects indirect topological proximity between Aprepitant-associated nodes and NSIAD-related disease nodes within the biomedical knowledge graph, rather than a true pharmacological relationship. Without a coherent mechanistic pathway and in the complete absence of clinical or preclinical supporting evidence, this prediction is not actionable at this stage.

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
The NK1/substance P pathway has no known interaction with the AVPR2/AQP2 axis responsible for NSIAD, making a pharmacological rationale absent; combined with zero supporting clinical or preclinical evidence, this prediction is not actionable.

**To proceed, the following is needed:**
- Retrieve Aprepitant's detailed MOA data from DrugBank (currently a blocking data gap) to formally complete the mechanistic analysis
- Identify any basic science data — in vitro or animal models — demonstrating NK1 receptor involvement in AVPR2 activity or renal water handling before clinical translation can be considered
- Obtain TFDA prescribing information (仿單) to complete the safety profile, currently flagged as a blocking gap
- Consider prioritizing alternative TxGNN-predicted indications with stronger mechanistic rationale for further investigation:
  - **Subarachnoid hemorrhage** (Rank 9): substance P is released into CSF after SAH and drives neurogenic edema and vasospasm — NK1 antagonism has conceptual support from animal models
  - **Hypertrichosis** (Rank 2): NK1 receptors are functionally expressed in hair follicle dermal papilla and outer root sheath; substance P may influence anagen/catagen cycling

> ⚠️ *This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

