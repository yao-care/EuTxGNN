---
layout: default
title: Bimekizumab
parent: 僅模型預測 (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
---

# Bimekizumab
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

# Bimekizumab: From Plaque Psoriasis to Diabetic Cataract

## One-Sentence Summary

Bimekizumab is a dual IL-17A and IL-17F inhibitor with demonstrated efficacy in immune-mediated inflammatory conditions such as plaque psoriasis and psoriatic arthritis, though it is not yet marketed in Taiwan.
The TxGNN model predicts it may be effective for **Diabetic Cataract**,
however **no clinical trials** and **no publications** currently support this direction — the prediction rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not marketed in Taiwan; globally approved for plaque psoriasis and related inflammatory conditions |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.23% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bimekizumab is a humanized monoclonal antibody that uniquely inhibits both IL-17A and IL-17F simultaneously, reducing downstream inflammatory signaling more completely than agents targeting IL-17A alone. In diabetic patients, IL-17 is elevated in the systemic circulation and has been associated with oxidative stress in peripheral tissues. Theoretically, suppressing IL-17A/F could reduce inflammatory burden in lens epithelial cells, potentially slowing the progression of diabetic cataract.

In practice, however, the mechanistic chain is tenuous. Bimekizumab is a large-molecule biologic (~145 kDa) with minimal ocular penetration following systemic administration. More critically, diabetic cataract is driven primarily by polyol pathway activation, advanced glycation end-product accumulation, and lens protein oxidative cross-linking — structural processes that are not downstream of IL-17 signaling. The primary treatment for cataract at any stage remains surgical extraction, not pharmacologic intervention.

A particularly telling pattern in this Evidence Pack is that 9 of the top 10 TxGNN-predicted indications are cataract subtypes with near-identical prediction scores (all clustering between 0.9809 and 0.9823). This score clustering is a known artifact of knowledge graph ontology structure — when multiple disease nodes share the same ontology branch (ICD-10: H26 cataract subtypes), the graph neural network propagates similar edge patterns to all sibling nodes, inflating prediction scores without reflecting genuine biological plausibility. This signal should be treated with significant skepticism until validated by independent means.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Bimekizumab in diabetic cataract or any cataract subtype.

---

## Literature Evidence

Currently no related literature available for Bimekizumab in any cataract indication.

---

## Taiwan Market Information

Bimekizumab is not currently authorized for marketing in Taiwan. No license records are available.

---

## Safety Considerations

Please refer to the SmPC for complete safety information.

> Note: Full prescribing information including Taiwan TFDA warnings, contraindications, and drug interaction data was not available in this Evidence Pack (Data Gap DG001). Safety assessment cannot be completed until the SmPC or equivalent labeling document is retrieved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN cataract cluster prediction is almost certainly a knowledge graph ontology artifact rather than a genuine repurposing signal. The near-identical scores across 9 distinct cataract subtypes — including etiologically unrelated types such as tetanic cataract (caused by hypocalcemia) and craniostenosis cataract (caused by genetic developmental abnormality) — are mechanistically inconsistent with IL-17A/F inhibition and indicate that the model is pattern-matching on shared ontology nodes rather than biological mechanism. No supporting clinical trial or literature evidence exists.

**To proceed, the following is needed:**
- Ontology artifact validation: compare Bimekizumab's top predictions against other IL-17 inhibitors (e.g., ixekizumab, secukinumab) in the same TxGNN model to determine whether the cataract cluster is drug-specific or a general graph topology effect
- Preclinical mechanistic evidence demonstrating IL-17 pathway activity in lens epithelial cells or validated animal models of diabetic cataract
- Ocular pharmacokinetic data confirming whether systemic biologic administration achieves any meaningful intraocular drug levels
- Taiwan TFDA SmPC or equivalent labeling document to complete the safety profile (DG001 — Blocking gap)
- DrugBank MOA data retrieval to formally document mechanism of action (DG002 — High severity gap)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

