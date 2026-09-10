---
layout: default
title: Methylnaltrexone
parent: 僅模型預測 (L5)
nav_order: 386
evidence_level: L5
indication_count: 10
---

# Methylnaltrexone
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

# Methylnaltrexone: From Opioid-Induced Constipation to Congenital Hypotrichosis Milia

## One-Sentence Summary

> Methylnaltrexone is a peripherally-restricted mu-opioid receptor antagonist internationally used to treat opioid-induced constipation; no local marketing authorization or original-indication record exists in this evidence pack.
> The TxGNN model's top-ranked prediction is **Congenital Hypotrichosis Milia**, but this pairing has **no supporting clinical trials or literature (0/0)**, and the model's own rationale explicitly flags it as likely knowledge-graph noise rather than a genuine mechanistic link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (drug not locally marketed); internationally recognized use is opioid-induced constipation (OIC) |
| Predicted New Indication | Congenital Hypotrichosis Milia |
| TxGNN Prediction Score | 78.35% |
| Evidence Level | L5 |
| EU Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on general drug classification knowledge, methylnaltrexone (DB06800) belongs to the peripherally-acting mu-opioid receptor antagonist (PAMORA) class, which blocks opioid effects on gastrointestinal mu-receptors without crossing the blood-brain barrier — the basis for its recognized use in opioid-induced constipation. No local (Taiwan) approved-indication text or license record is present to confirm this against the evidence pack itself.

For the top-ranked candidate, however, the evidence pack's own repurposing rationale states there is **no known pathophysiological connection** between peripheral mu-opioid receptor antagonism and congenital hypotrichosis milia, a rare congenital hair/skin disorder. The rationale explicitly attributes this pairing to likely noise from rare-disease node connections within the TxGNN knowledge graph, rather than a biologically plausible mechanism.

Notably, among the 10 candidates in this evidence pack, only two show any literature-level engagement: **respiratory failure** (rank 7, L4) has mechanistic literature on opioid receptors and cardiorespiratory control — though the rationale itself argues methylnaltrexone's peripheral restriction likely makes it *ineffective* against central respiratory depression; and **alopecia/alopecia areata** (ranks 5–6) have a plausible but unproven hypothesis involving mu-opioid receptor expression in hair follicle keratinocytes. Neither has any clinical trial or case-report evidence. The rank-1 candidate reported here has weaker rationale support than either of these.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No marketing authorizations are recorded for this drug in this jurisdiction (market status: 未上市 / Not marketed; total licenses: 0).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted pairing (methylnaltrexone → congenital hypotrichosis milia) has zero clinical trial or literature evidence, and the model's own mechanistic rationale identifies it as probable knowledge-graph noise rather than a credible hypothesis. Combined with a **blocking** data gap on TFDA warnings/contraindications (DG001) and a **high-severity** gap on mechanism of action (DG002), the candidate cannot proceed past initial safety screening (S0).

**To proceed, the following is needed:**
- TFDA label (warnings, contraindications) — required to clear Blocking gap DG001 before any S1 safety assessment
- Confirmed mechanism of action via DrugBank API — required to clear High-severity gap DG002
- Confirmation of original approved indication and local market status (currently absent from evidence pack)
- If pursuing a biologically more plausible direction, consider re-evaluating the alopecia/alopecia areata candidates (ranks 5–6), which at least have a stated (if unproven) mechanistic hypothesis — but note these also currently lack any clinical trial or literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

