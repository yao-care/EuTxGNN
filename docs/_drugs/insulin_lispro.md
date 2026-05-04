---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Insulin Lispro
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analog used for the treatment of Type 1 and Type 2 diabetes mellitus, designed to mimic the body's natural mealtime insulin response.
The TxGNN model predicts it may be effective for **Autoimmune Oophoritis**, with **0 clinical trials** and **0 publications** currently supporting this direction.
Overall evidence remains at the AI model prediction level only (L5); the mechanistic connection reflects a knowledge graph comorbidity association rather than a direct therapeutic rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diabetes Mellitus (Type 1 and Type 2) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, insulin lispro is a rapid-acting insulin analog in which lysine and proline residues at positions B28–B29 are reversed, reducing self-aggregation and enabling faster subcutaneous absorption. It acts by binding to the insulin receptor on target tissues (liver, muscle, adipose) to promote glucose uptake and suppress hepatic glucose production.

The TxGNN model's prediction appears to be driven by a **knowledge graph comorbidity association** rather than a direct therapeutic mechanism. Both Type 1 Diabetes Mellitus (T1DM) and autoimmune oophoritis are organ-specific autoimmune diseases that may share an autoimmune predisposition — anti-islet cell antibodies can co-occur with other organ-specific autoimmune conditions, and the insulin/IGF-1R signaling pathway is present in ovarian granulosa cells, creating a topological connection within the knowledge graph.

However, this mechanistic link does **not** support insulin lispro as a treatment for autoimmune oophoritis. Insulin supplementation corrects hormonal deficiency arising from beta-cell destruction; it does not modulate the underlying autoimmune process targeting ovarian tissue. The established treatment approach for autoimmune oophoritis involves immunomodulation (corticosteroids, hormone replacement therapy). This prediction almost certainly reflects co-occurrence patterns within the knowledge graph rather than actionable therapeutic potential, and should be interpreted accordingly.

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
There is no clinical trial or published literature evidence supporting insulin lispro for autoimmune oophoritis, and the mechanistic rationale reflects a knowledge graph comorbidity association (shared autoimmune background between T1DM and autoimmune oophoritis) rather than a plausible therapeutic pathway — insulin supplementation cannot modulate ovarian autoimmune destruction.

**To proceed, the following is needed:**
- Detailed mechanism of action data from DrugBank (Data Gap DG002) to complete mechanistic link analysis
- TFDA product insert (仿單) for warnings and contraindications (Data Gap DG001, currently blocking the S1 safety evaluation)
- Preclinical evidence (in vitro or animal model) demonstrating any direct immunomodulatory effect on ovarian autoimmunity before this indication can be elevated beyond L5
- A formal review of whether the TxGNN knowledge graph is conflating "comorbidity co-occurrence" with "repurposable therapeutic mechanism" for this drug-disease pair, particularly given the similar Hold recommendations across all 10 predicted indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

