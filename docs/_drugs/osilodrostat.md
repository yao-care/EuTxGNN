---
layout: default
title: Osilodrostat
parent: 僅模型預測 (L5)
nav_order: 439
evidence_level: L5
indication_count: 10
---

# Osilodrostat
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

# Osilodrostat: From Cushing's Disease to Rare Dermatologic and Genetic Syndromes

## One-Sentence Summary

Osilodrostat (DrugBank DB11837) is a CYP11B1 (11β-hydroxylase) inhibitor that blocks cortisol synthesis, originally developed for Cushing's disease/syndrome. The TxGNN model's top 10 predictions for this drug are a mix of rare pigmentary skin disorders, congenital chromosomal syndromes, and unrelated tumor types (e.g., rhabdoid tumor, schwannoma), none of which have any known mechanistic link to cortisol synthesis inhibition. **No clinical trials or literature currently support any of these predictions.**

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indications on file) |
| Predicted New Indication | Familial generalized lentiginosis |
| TxGNN Prediction Score | 98.19% |
| Evidence Level | L5 |
| EU Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not fully available. Based on known information, Osilodrostat is a CYP11B1 (11β-hydroxylase) inhibitor that suppresses adrenal cortisol synthesis, and its established use is in Cushing's disease/syndrome.

All 10 top-ranked predictions from TxGNN are rare dermatologic pigmentation disorders (e.g., familial generalized lentiginosis, acromelanosis, Moynahan syndrome), congenital chromosomal instability syndromes, or unrelated oncologic conditions (rhabdoid tumor, peripheral nerve schwannoma). None of these has an established or plausible pathophysiological connection to cortisol synthesis inhibition. The model's own rationale notes for every candidate explicitly flag "no known mechanistic link" and attribute the high scores to likely noise from indirect node associations in the knowledge graph (e.g., shared pigmentation-related or genetic-syndrome nodes), rather than genuine biological plausibility.

Given the absence of any supporting mechanism, clinical trial, or literature evidence across the entire top-10 list, these predictions should be treated as low-confidence, exploratory signals only — not as candidates warranting near-term clinical investigation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

No EU marketing authorizations on file (market status: 未上市 / Not marketed; total licenses: 0).

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications are rated L5 (AI prediction only) with no clinical trials, no literature, and no plausible mechanistic rationale — the drug's own rationale notes describe several candidates as likely knowledge-graph noise. There is no basis to proceed to safety or clinical evaluation at this time.

**To proceed, the following is needed:**
- TFDA/EMA label warnings and contraindications (currently a blocking data gap, DG001)
- Confirmed mechanism of action detail from DrugBank (DG002)
- Independent mechanistic or preclinical rationale connecting CYP11B1 inhibition to any of the predicted conditions before further evidence collection is warranted
- Re-screening of lower-ranked TxGNN candidates that may have stronger biological plausibility (e.g., other cortisol/steroidogenesis-related conditions), since the current top 10 appear dominated by graph-topology artifacts rather than true signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

