---
layout: default
title: Fostamatinib
parent: 僅模型預測 (L5)
nav_order: 265
evidence_level: L5
indication_count: 10
---

# Fostamatinib
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

# Fostamatinib: From Immune Thrombocytopenia to Autosomal Thrombocytopenia with Normal Platelets

## One-Sentence Summary

Fostamatinib is a SYK (spleen tyrosine kinase) inhibitor whose known clinical use is in immune-mediated platelet destruction (its formal original indication is not recorded in this evidence pack — see data gaps below). TxGNN's top-ranked prediction is **Autosomal Thrombocytopenia with Normal Platelets**, but this candidate has **no clinical trials, no literature, and no proposed mechanism the evidence pack itself endorses** — the rationale text explicitly states the pharmacological logic does not hold. This is a **Hold**, not a candidate ready for advancement.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (structured `original_indications` is empty; `original_moa` is a data gap). Rationale text elsewhere in the pack references known SYK-mediated immune thrombocytopenia (ITP) activity. |
| Predicted New Indication | Autosomal Thrombocytopenia with Normal Platelets |
| TxGNN Prediction Score | 99.45% (rank 5888 among all candidates) |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Fostamatinib in this evidence pack (`original_moa` = data gap, severity High). Based on the rationale text attached to the predictions themselves, Fostamatinib's known clinical activity works through SYK inhibition, which reduces Fc-receptor-mediated antibody-dependent platelet destruction — an immune-mediated mechanism relevant to conditions like immune thrombocytopenia (ITP).

The top-ranked candidate, **Autosomal Thrombocytopenia with Normal Platelets**, is a different disease category: it is a congenital/hereditary thrombocytopenia driven by defects in megakaryocyte development or platelet structural genes, not by immune-mediated platelet destruction. The evidence pack's own mechanistic assessment states directly that "the pharmacological logic does not hold" for this pairing, and no clinical trial, ICTRP record, or PubMed literature supports it (0 results across all three sources per the query log).

In short: this is a case where the TxGNN embedding-space score is high, but the domain rationale attached to the same record contradicts it. The prediction should be treated as noise rather than a genuine repurposing hypothesis unless independent mechanistic or clinical signal emerges.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Fostamatinib is currently **not marketed** in Taiwan (0 authorizations on record), so no product/authorization table is available.

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and DDI data are all marked as data gaps in this evidence pack — DG001, severity Blocking, is required before any S1 safety screening can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Autosomal Thrombocytopenia with Normal Platelets) has zero clinical trial or literature support and is explicitly flagged in the evidence pack's own mechanistic assessment as pharmacologically implausible. There is no basis to advance this specific candidate.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any safety screening
- Confirmed mechanism of action (DG002, High) via DrugBank API query
- If repurposing work continues for Fostamatinib, consider redirecting to better-supported candidates from the same evidence pack: **glaucoma** (rank 4, L4, 3 PubMed reviews) and **esophageal disease** (rank 10, L4, 2 PubMed papers on SYK-adjacent signaling) — both still weak (indirect, non-drug-specific literature) but stronger than the top-ranked candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

