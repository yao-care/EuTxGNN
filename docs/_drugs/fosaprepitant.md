---
layout: default
title: Fosaprepitant
parent: 僅模型預測 (L5)
nav_order: 264
evidence_level: L5
indication_count: 10
---

# Fosaprepitant
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

# Fosaprepitant: From Chemotherapy-Induced Nausea/Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fosaprepitant is the intravenous prodrug of aprepitant, an NK1 (Substance P) receptor antagonist historically used for chemotherapy-induced nausea and vomiting (CINV) prevention. The TxGNN model's top-ranked prediction for this drug is **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this candidate currently has **no supporting clinical trials, no supporting literature, and no established mechanistic link** — it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy-induced nausea and vomiting (CINV) prevention — not formally authorized in this jurisdiction (0 licenses on file) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.92% (rank 1,227 among all predictions) |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fosaprepitant is the water-soluble intravenous prodrug of aprepitant, an NK1 (Substance P) receptor antagonist. Its established clinical use is antiemetic — blocking Substance P/NK1 signaling to suppress chemotherapy-induced nausea and vomiting, as reflected in the multiple oncology antiemetic trials associated with this drug in the evidence pack.

NSIAD, however, is a distinct rare genetic disorder caused by gain-of-function mutations in the AVPR2 (vasopressin V2) receptor, leading to inappropriate water retention independent of vasopressin levels. There is currently **no known mechanistic link** between NK1/Substance P receptor antagonism and AVPR2 receptor signaling. The evidence pack itself states explicitly: "此為 AVPR2 受體功能獲得性突變導致之罕見疾病，與 NK1/Substance P 路徑無已知機轉關聯，亦無任何臨床或臨床前證據支持" (a rare disease driven by AVPR2 gain-of-function mutation, with no known mechanistic connection to the NK1/Substance P pathway, and no clinical or preclinical evidence).

In short, this ranks as a pure knowledge-graph statistical signal (TxGNN score) without biological plausibility or empirical support. It should be treated as hypothesis-generating only, not as a basis for further development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

Fosaprepitant currently has no marketing authorization on file in this jurisdiction (0 licenses; market status: not marketed).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Key warnings, contraindications, and drug-interaction data were queried but not found in TFDA/DrugBank sources at this time — this is flagged as a blocking data gap (DG001) for any future safety evaluation of this drug.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (NSIAD) has no clinical trials, no literature, and no established mechanistic rationale — it is an L5, model-prediction-only signal with an explicit absence of biological plausibility. This does not meet the threshold to advance beyond S0.

**To proceed, the following is needed:**
- TFDA/regional label warnings and contraindications (currently a blocking data gap, DG001)
- Confirmed mechanism of action data for fosaprepitant (currently a high-severity data gap, DG002)
- If pursuing repurposing for this drug at all, consider re-screening lower-score candidates with actual mechanistic support instead — e.g., within this same evidence pack, retinitis (rank 7) has L4 preclinical evidence (PMID 32058829) showing fosaprepitant blocks UVR-induced NK1 receptor expression in ocular tissue, which is a more biologically grounded starting point than NSIAD
- Note: the multiple endocrine neoplasia (rank 5) candidate should also be disregarded — its cited trials are CINV antiemetic-support studies in oncology patients, not treatment trials for MEN itself, and are flagged in the pack as a likely co-occurrence false positive
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

