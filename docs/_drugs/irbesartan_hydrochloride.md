---
layout: default
title: Irbesartan Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 62
evidence_level: L5
indication_count: 0
---

# Irbesartan Hydrochloride
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

# Irbesartan Hydrochloride: Repurposing Evaluation — Data Insufficient to Proceed

## One-Sentence Summary

Irbesartan hydrochloride is a salt formulation of irbesartan, a well-characterized angiotensin II receptor blocker (ARB) class antihypertensive. The TxGNN pipeline returned **no predicted new indications** for this drug entry, and the drug is not currently registered in Taiwan under this specific formulation name. A repurposing evaluation cannot be completed until the drug identifier is resolved and the prediction pipeline is re-run.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Insufficient data (original indications not captured in this Evidence Pack) |
| Predicted New Indication | None available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — pipeline output absent; no actual studies |
| Taiwan Market Status | Not marketed (0 licenses) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The predicted indications list is empty for this entry. This is most likely a **drug identifier resolution problem**, not a true absence of repurposing candidates. Two specific issues are suspected:

**1. Atypical salt name may have blocked DrugBank mapping.**
Standard irbesartan is listed in DrugBank as a free base (DB00522), not as a hydrochloride salt. When the pipeline queries "irbesartan hydrochloride," the name normalizer may have failed to resolve it to DB00522, resulting in a null `drugbank_id` and no knowledge graph traversal — and therefore no TxGNN score.

**2. Downstream pipeline skipped due to missing DrugBank ID.**
The query log confirms a DrugBank search returned one result (`result_status: success`, `result_count: 1`), yet no `drugbank_id` was written into the Evidence Pack. This suggests a parsing or field-mapping failure in the DrugBank collector, not a true data absence.

Until the identifier is correctly resolved to DB00522 (or an equivalent), the TxGNN repurposing score cannot be generated and no evidence sections can be populated.

---

## Taiwan Market Information

No authorizations were found in Taiwan for the name "irbesartan hydrochloride." Standard irbesartan (free base) is widely marketed globally under brand names such as Aprovel and Avapro, but this specific salt formulation does not appear in the current TFDA license database.

> **Note:** If the intent was to evaluate standard irbesartan, a separate Evidence Pack should be generated using the INN "irbesartan" to ensure correct TFDA license retrieval.

---

## Safety Considerations

Please refer to the SmPC or TFDA prescribing information for safety data. No DDI, warnings, or contraindications were captured in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — no DrugBank ID was resolved, no TxGNN predictions were generated, and no original indication or safety data was captured. Proceeding with a repurposing evaluation under these conditions would have no evidence basis.

**To proceed, the following is needed:**

- **Fix drug identifier:** Confirm whether "irbesartan hydrochloride" should be normalized and mapped to DrugBank DB00522 (irbesartan). Update the name normalization dictionary in `normalizer.py` if needed.
- **Re-run evidence pipeline:** After resolving the DrugBank ID, re-run `collect_evidence.py` to generate TxGNN scores and fetch clinical trial / PubMed evidence.
- **Retrieve MOA data:** Query DrugBank API for DB00522 to obtain mechanism of action (ARB, AT₁ receptor antagonist) and populate the `original_moa` field.
- **Retrieve TFDA safety data:** Download the TFDA prescribing information PDF for irbesartan and parse warnings, contraindications, and key DDIs.
- **Consider re-querying under INN "irbesartan":** If the intent is to evaluate the standard free-base formulation, a clean Evidence Pack should be generated using the normalized INN.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

