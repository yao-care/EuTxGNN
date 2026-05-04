---
layout: default
title: Amifampridine Phosphate
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 0
---

# Amifampridine Phosphate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Amifampridine Phosphate: Evaluation Pending — Prediction Pipeline Incomplete

## One-Sentence Summary

Amifampridine phosphate is a small-molecule drug with no original indications or approved status recorded in the current Evidence Pack.
The TxGNN model did not generate any predicted new indications for this compound, most likely due to a failed DrugBank ID mapping that prevented the drug from entering the prediction pipeline.
As a result, this candidate **cannot be evaluated for repurposing potential** until the underlying data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in current dataset |
| Predicted New Indication | No prediction generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction only (pipeline incomplete) |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The query log reveals a critical upstream failure: a DrugBank search for amifampridine phosphate returned **1 result**, yet the `drugbank_id` field in the Evidence Pack remains `null`. This indicates the match was found but not successfully linked to the candidate record.

Without a valid DrugBank ID, TxGNN's knowledge graph and deep learning models have no anchor node to traverse the drug–disease network. The entire prediction pipeline — from KG-based candidate generation to DL scoring — depends on this mapping as its entry point. A missing DrugBank ID means zero predictions, regardless of the drug's actual repurposing potential.

Compounding this, the mechanism of action (MOA) is also unavailable. Even if predictions were recovered, the mechanistic rationale section could not be constructed without MOA data. Both gaps need to be resolved in tandem.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack for amifampridine phosphate is structurally incomplete — the DrugBank ID mapping failed, no TxGNN predictions were generated, and no safety or regulatory data is available. Repurposing evaluation cannot proceed in the current state.

**To proceed, the following is needed:**

- **Resolve DrugBank ID mapping** — The query log confirms a DrugBank result was found. Manually verify the correct DrugBank ID (likely `DB09117` for amifampridine phosphate / Firdapse) and re-populate the Evidence Pack
- **Re-run the TxGNN prediction pipeline** after successful DrugBank ID linkage to generate drug–disease scores
- **Retrieve MOA data from DrugBank** — Needed for mechanistic rationale analysis once predictions are available
- **Obtain Taiwan TFDA package insert** — Required for safety warnings, contraindications, and S1 safety screening (currently Blocking severity per DG001)
- **Confirm original approved indication(s)** from international regulatory sources (e.g., FDA/EMA approval for Lambert–Eaton Myasthenic Syndrome) to populate the `original_indications` field
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

