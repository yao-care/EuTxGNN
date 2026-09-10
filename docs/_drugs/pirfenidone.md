---
layout: default
title: Pirfenidone
parent: 僅模型預測 (L5)
nav_order: 472
evidence_level: L5
indication_count: 10
---

# Pirfenidone
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

# Pirfenidone: From Idiopathic Pulmonary Fibrosis to Extracutaneous Mastocytoma

## One-Sentence Summary

> Pirfenidone is an antifibrotic agent whose established use is idiopathic pulmonary fibrosis (IPF), acting via inhibition of TGF-β1 signaling and reduction of fibroblast proliferation/collagen synthesis.
> The TxGNN model predicts it may be effective for **Extracutaneous Mastocytoma**,
> but currently **0 clinical trials** and **0 publications** support this specific direction — this is a model prediction only, with a mechanistically weak rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic Pulmonary Fibrosis (IPF) — inferred from mechanistic notes in the evidence pack; no formal indication text is available because the drug carries **no active authorization** in this jurisdiction |
| Predicted New Indication | Extracutaneous Mastocytoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| EU Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action (MOA) data is not currently available for this drug in the record (flagged as a High-severity data gap). Based on information embedded in the evidence pack's rationale notes, Pirfenidone is known to inhibit TGF-β1 signaling and downstream non-SMAD pathways, thereby reducing fibroblast proliferation, myofibroblast activity, and collagen deposition — the pharmacological basis for its established use in idiopathic pulmonary fibrosis.

Extracutaneous mastocytoma, however, is a mast cell proliferative disorder typically driven by **KIT mutations** (e.g., KIT D816V), not by fibrotic tissue remodeling. There is no established biological pathway connecting TGF-β1/collagen-synthesis inhibition to mast cell proliferation control. The evidence pack itself flags this as a **weak mechanistic link**.

Consequently, the very high TxGNN score (99.71%) for this pairing is not corroborated by any clinical trial, real-world evidence, or preclinical literature. This pattern — a high similarity/embedding score with no biological or empirical backing — is consistent with a knowledge-graph artifact (e.g., surface-level lexical/semantic proximity) rather than a genuine repurposing signal, and should be treated with caution.

> **Note on other candidates in this evidence pack:** Among the 10 diseases predicted for Pirfenidone, rank #9 ("fibroblastic neoplasm," score 99.23%) is supported by **L3 evidence** — including a pilot clinical study in FAP-associated desmoid tumors and multiple in-vitro studies in Dupuytren's disease fibroblasts — but also carries a safety signal (two case reports of malignant fibroblastic tumor emergence/aggravation during Pirfenidone use). This candidate has materially stronger evidence than the top-ranked prediction discussed above and may warrant separate evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

This drug currently has **no active marketing authorization** on record in this jurisdiction (market status: 未上市 / Not marketed; total authorizations: 0). No license table can be produced from the evidence pack.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Key warnings, contraindications, and drug-interaction data are marked as data gaps in this evidence pack — notably, TFDA/regulatory label warnings and contraindications are flagged as a **Blocking** severity gap, meaning safety evaluation cannot proceed until this is resolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Extracutaneous Mastocytoma) has a high TxGNN score but zero supporting clinical trials, zero literature, and a mechanistically implausible link (antifibrotic TGF-β1 inhibition vs. KIT-driven mast cell proliferation). This is evidence level L5 — model prediction only — and does not meet the bar to advance past initial screening.

**To proceed, the following is needed:**
- Resolve the **Blocking** data gap: obtain formal regulatory label warnings/contraindications (source: national regulatory agency label PDF) before any safety-stage (S1) evaluation of Pirfenidone can begin, regardless of indication.
- Obtain structured MOA data from DrugBank (High-severity gap) to properly assess mechanistic plausibility across all 10 predicted indications.
- If pursuing repurposing, prioritize re-evaluation of the **fibroblastic neoplasm (Dupuytren's disease / desmoid tumor)** candidate instead, given its stronger L3 evidence base — while also investigating the reported malignant-transformation safety signal before advancing it.
- No further action recommended on the extracutaneous mastocytoma pairing absent new preclinical or clinical data.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

