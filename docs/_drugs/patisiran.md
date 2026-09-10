---
layout: default
title: Patisiran
parent: 僅模型預測 (L5)
nav_order: 454
evidence_level: L5
indication_count: 10
---

# Patisiran
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

# Patisiran: From Hereditary Transthyretin Amyloidosis to Dermatitis (Low-Confidence Prediction)

## One-Sentence Summary

> Patisiran is an siRNA-lipid nanoparticle (LNP) therapeutic originally developed to silence *TTR* mRNA for the treatment of hereditary transthyretin-mediated (hATTR) amyloidosis.
> The TxGNN model's top-ranked prediction is **Dermatitis**, but this candidate is supported by **0 clinical trials** and **0 publications**,
> and the evidence pack's own mechanistic assessment finds **no known biological link** between TTR gene silencing and inflammatory skin disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary transthyretin (ATTR) amyloidosis (based on drug class context; no formal EU/TW label text available — drug not marketed) |
| Predicted New Indication | Dermatitis |
| TxGNN Prediction Score | 90.65% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a blocking data gap). Based on known drug-class information, Patisiran is an siRNA-LNP therapeutic that silences hepatic *TTR* mRNA production, reducing circulating transthyretin protein and thereby slowing amyloid fibril deposition in peripheral nerves and the heart. Its established clinical role is in hereditary transthyretin amyloidosis with polyneuropathy — an entirely distinct disease category from dermatitis.

The evidence pack's own mechanistic rationale for this prediction is explicit that **no known biological connection exists** between RNA interference-mediated TTR suppression and dermatitis's inflammatory pathways. The TxGNN score of 90.65% most likely reflects an indirect node connection within the knowledge graph (e.g., shared downstream pathways or co-occurring metadata) rather than genuine pharmacological plausibility. Because the model output is unaccompanied by any clinical trial or literature evidence, this candidate should be treated as a hypothesis-generating signal only, not as a validated repurposing lead.

It is worth noting that a lower-ranked candidate in this pack — **overactive bladder (rank 9, score 84.9%)** — has a more coherent (though still indirect) rationale: hATTR amyloidosis itself can cause autonomic neuropathy leading to bladder dysfunction, so improvement in bladder symptoms could theoretically follow from treating the underlying amyloidosis. This represents disease comorbidity rather than a direct new indication, but may warrant closer review before dermatitis in any follow-up evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Patisiran currently has **no marketing authorizations** recorded in this dataset (0 licenses, market status: Not marketed). No product/indication label text is available for cross-reference.

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug-interaction data are currently unavailable — TFDA label retrieval is flagged as a blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure L5 model-only prediction (TxGNN score without corroborating clinical or literature evidence), and the evidence pack's own mechanistic review finds no biological rationale linking TTR-targeted siRNA therapy to dermatitis. Advancing this candidate is not justified at this stage.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank (DG002)
- TFDA/EMA label warnings and contraindications to enable a baseline safety screen (DG001, blocking)
- Independent preclinical or mechanistic evidence connecting TTR silencing to dermatitis pathophysiology, if this candidate is to be pursued further
- Consideration of re-scoping toward higher-plausibility candidates in this pack (e.g., overactive bladder, rank 9) given the disease-comorbidity link to hATTR amyloidosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

