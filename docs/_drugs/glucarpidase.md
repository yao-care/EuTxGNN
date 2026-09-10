---
layout: default
title: Glucarpidase
parent: 僅模型預測 (L5)
nav_order: 281
evidence_level: L5
indication_count: 10
---

# Glucarpidase
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

# Glucarpidase: From Methotrexate Toxicity to Diabetic Cataract

## One-Sentence Summary

Glucarpidase (carboxypeptidase G2) is a recombinant bacterial enzyme used to rapidly clear toxic plasma methotrexate concentrations in patients with impaired renal clearance. The TxGNN model predicts it may be effective for **Diabetic Cataract**, but currently **no clinical trials** and **no published literature** support this direction, and the model's own mechanistic rationale flags the prediction as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Methotrexate toxicity (rescue therapy for elevated plasma methotrexate levels) — not derived from a formal license record in this evidence pack |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| EU Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Glucarpidase's only established pharmacological action is hydrolyzing the glutamate residue on folate/methotrexate molecules to rapidly eliminate circulating methotrexate — it is used as an emergency detoxification enzyme, not a disease-modifying therapeutic. This action has no known relationship to lens protein metabolism, the polyol (aldose reductase) pathway, oxidative stress, or any other mechanism implicated in diabetic cataract formation.

The evidence pack's own mechanistic analysis for this candidate explicitly states there is no known biological pathway connecting glucarpidase to cataract pathophysiology, and suggests the prediction likely reflects a knowledge-graph embedding artifact ("false positive") caused by data sparsity for this rare indication pairing, rather than a genuine pharmacological signal. This same "no mechanistic link" conclusion is repeated across all 10 top-ranked predicted indications for this drug (diabetic retinopathy, tetanic cataract, senile cataract, etc.), all clustered at similar TxGNN scores — a pattern consistent with a systematic embedding-space artifact rather than a specific, credible signal for any one disease.

Given this, the high TxGNN score should be interpreted as a statistical association within the model's latent space, not as evidence of therapeutic plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Glucarpidase currently holds no EU marketing authorizations (market status: 未上市, 0 licenses on file in this evidence pack).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: TFDA label warnings/contraindications and formal MOA data are flagged as blocking/high-severity data gaps in this evidence pack — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no mechanistic rationale, no clinical trial evidence, and no published literature connecting glucarpidase to diabetic cataract or any of its other top-ranked predicted indications. The evidence pack's own analysis identifies this as a likely false-positive prediction driven by embedding-space sparsity rather than genuine pharmacology. Combined with the drug having no EU marketing presence and missing safety documentation, this candidate does not meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA label (仿單) warnings and contraindications — currently a blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank API — currently a high-severity data gap (DG002)
- Independent pharmacological or preclinical rationale linking glucarpidase to any diabetic ophthalmic pathway, before further evidence collection is warranted
- Re-evaluation of whether this candidate should remain in the pipeline given the model's own rationale disputing biological plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

