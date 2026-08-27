---
layout: default
title: Drospirenone
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 10
---

# Drospirenone
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

# Drospirenone: From Hormonal Contraception to Elevated Plasma Zinc

## One-Sentence Summary

> Drospirenone is a spironolactone-derived progestin used in combined oral contraceptives and hormone replacement therapy, valued for its antimineralocorticoid and antiandrogenic activity.
> The TxGNN model's top-ranked prediction suggests a possible association with **elevated plasma zinc**,
> but this candidate currently has **no supporting clinical trials and no supporting literature** — the score reflects a knowledge-graph pattern only, not observed clinical or mechanistic evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack; based on supporting literature, drospirenone is used as the progestin component of combined oral contraceptives and menopausal hormone therapy |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 98.74% |
| Evidence Level | L5 (model prediction only, no clinical or literature evidence) |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for drospirenone is flagged as a data gap in this evidence pack. Based on the supporting literature that is available, drospirenone is a 17α-spirolactone derivative structurally related to spironolactone. It acts as a progestin with additional **antimineralocorticoid (anti-aldosterone)** and **antiandrogenic** activity, which is why it is combined with ethinyl estradiol or estetrol in oral contraceptive and hormone-therapy products — its antimineralocorticoid effect promotes sodium excretion and potassium retention, and its antiandrogenic effect is used clinically to manage acne and hirsutism in conditions such as PCOS.

There is no established or literature-supported pharmacological pathway linking antimineralocorticoid/antiandrogenic progestin activity to **plasma zinc regulation**. Zinc homeostasis is governed primarily by intestinal absorption/transporter proteins (ZIP/ZnT families), renal handling, and metallothionein binding — none of which are known targets or downstream effects of drospirenone's aldosterone-receptor antagonism. The complete absence of clinical trials or publications connecting these two entities is consistent with this being a **knowledge-graph embedding artifact** rather than a biologically grounded signal: the high TxGNN score likely reflects proximity in the model's learned representation space rather than a real pharmacological relationship.

Given this, the prediction should be treated as a hypothesis-generation output only, not as a candidate with mechanistic or clinical support at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No marketing authorizations are currently recorded for drospirenone in this dataset (market status: Not Marketed; 0 authorizations on file).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*Note: Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this evidence pack (DG001, severity: Blocking) — this must be resolved with official labeling data before any safety assessment can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (elevated plasma zinc) has a high model score but zero supporting clinical trials or literature, and no plausible pharmacological mechanism connects drospirenone's known antimineralocorticoid/antiandrogenic activity to zinc homeostasis. This meets the criteria for **L5 — model prediction only**, and per the model's own scoring output the recommendation is already Hold.

It is also worth flagging for data-quality purposes: among the other candidates in this batch, the literature sets returned for "dyschondrosteosis-nephritis syndrome" and "thyrocerebrorenal syndrome" (both rare congenital syndromes) consist entirely of PMS/PMDD/PCOS/oral-contraceptive publications with no relevance to those disease labels. This suggests a possible disease-label–to-literature mapping error in the underlying evidence retrieval pipeline for this drug's candidate set, and the full batch may warrant a QA re-run before any candidate from it is advanced.

**To proceed, the following is needed:**
- Official mechanism of action (MOA) data from DrugBank or the approved product labeling
- TFDA/EMA labeling data — key warnings, contraindications, and drug interactions (currently a Blocking data gap, DG001)
- Confirmed original indication and licensing history for this drug in the target market
- A biological/mechanistic hypothesis or preclinical signal connecting drospirenone to zinc metabolism before this candidate is escalated beyond S0
- Re-validation of the literature-to-disease mapping pipeline for this candidate batch, given the mismatches observed in ranks 2 and 7
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

