---
layout: default
title: Dostarlimab
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 10
---

# Dostarlimab
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

# Dostarlimab: From Unknown Original Indication to Acute Megakaryoblastic Leukemia

## One-Sentence Summary

> Dostarlimab's original approved indication and mechanism of action are not recorded in the current evidence pack. The TxGNN model predicts a possible association with **Acute Megakaryoblastic Leukemia**, but this is based purely on a knowledge-graph score of **50%** (rank #1,360,717) with **zero clinical trials** and **zero publications** currently supporting the connection — the model's own rationale explicitly labels the mechanistic link as speculative and indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty and MOA is unconfirmed in the source data |
| Predicted New Indication | Acute Megakaryoblastic Leukemia |
| TxGNN Prediction Score | 50% (score 0.5; rank #1,360,717 — a very low-confidence position despite the mid-range score) |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| EU Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Dostarlimab, and no original indication is recorded in the source data, so its established area of proven efficacy cannot be confirmed from this evidence pack alone. This is a **Blocking** data gap (DG001: missing TFDA label/warnings) and a **High**-severity gap (DG002: missing MOA), both of which materially limit how far this candidate can be evaluated.

The model's own rationale for the top-ranked prediction states: *"Both are hematologic malignancies; theoretically an immune checkpoint inhibitor could produce anti-leukemic activity by activating T cells. However, this is a rare AML subtype, and there is currently no public evidence supporting PD-1 inhibitor efficacy in this subtype — the mechanistic link is speculative and an indirect analogy."* In other words, the association is a topological inference from the knowledge graph rather than a grounded pharmacological hypothesis.

This caution is reinforced by the rest of the top-10 candidate list for this drug: several of the other predicted "indications" (e.g., vasculitis, ovarian dysfunction, Lyell syndrome) are explicitly flagged in the pack's own rationale as likely **reversed-direction signals** — conditions the drug is known to *cause* as an immune-related adverse event, not conditions it treats — or as probable knowledge-graph noise from sparsely connected nodes. Given this pattern, the overall reliability of this prediction batch should be treated as low until independently verified.

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
This candidate sits at Evidence Level L5 with no clinical trials or literature support, an unresolved Blocking data gap on TFDA label warnings/contraindications (DG001), and no confirmed mechanism of action (DG002). The prediction score (50%, rank #1,360,717) and the model's own rationale — which explicitly describes the mechanistic link as speculative — do not support advancing past initial screening.

**To proceed, the following is needed:**
- TFDA label/SmPC (warnings, contraindications) to unblock S1 safety screening (resolves DG001)
- Confirmed mechanism of action from an authoritative source such as DrugBank (resolves DG002)
- Documentation of Dostarlimab's actual original/approved indication(s), which are currently missing entirely from this evidence pack
- Independent clinical trial or literature evidence specifically linking Dostarlimab to acute megakaryoblastic leukemia, since the current score derives purely from graph topology
- Expert review to rule out reversed-direction/immune-related-adverse-event confusion, given that this pattern was flagged in multiple other candidates for this drug in the same batch
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

