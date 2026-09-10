---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 247
evidence_level: L5
indication_count: 10
---

# Febuxostat
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

# Febuxostat: From Gout/Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Febuxostat is a xanthine oxidase (XO) inhibitor whose established pharmacology is to **lower** serum uric acid (used in gout/hyperuricemia management); no formal original-indication record is present in this evidence pack (Taiwan market status: not marketed). The TxGNN model's top-ranked prediction is **Renal Hypouricemia** — a condition of **low** urate — with a 99.99% score, but the evidence pack itself flags this as a likely mechanistic false positive, supported only by **1 low-relevance clinical trial** and **2 tangential review articles**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this pack (no Taiwan licenses on file); pharmacologically an XO inhibitor used for gout/hyperuricemia per rationale notes |
| Predicted New Indication | Renal Hypouricemia (hypouricemia, renal) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| EU Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available as a structured field in this pack (`original_moa: [Data Gap]`). However, the rationale notes attached to the candidate confirm Febuxostat is a xanthine oxidase inhibitor, pharmacologically equivalent in class to allopurinol, whose proven effect is **reducing** uric acid production — the standard treatment direction for hyperuricemia and gout.

Renal hypouricemia is the opposite clinical entity: serum urate is abnormally **low**, typically due to URAT1/GLUT9 transporter defects that cause excessive renal urate wasting. Prescribing a urate-**lowering** drug for a urate-**deficiency** disorder is mechanistically contradictory.

The evidence pack's own rationale explicitly calls this out: it attributes the high TxGNN score to likely embedding confusion between "hypouricemia" and "hyperuricemia," notes that the one linked clinical trial (NCT04398251) is graded relevance **C** (title is an institution name, status Unknown, no demonstrable link to the disease), and that the two literature hits do not support this indication — one is a general review of hypouricemia etiology, the other discusses febuxostat only in the context of *preventing exercise-induced kidney injury*, not treating renal hypouricemia itself. The pack recommends this be manually verified as a possible data-pipeline error rather than acted upon.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Studied uric acid control effects on stone recurrence and renal function in hyperuricemia patients with calculi; title/registry entry does not describe a renal-hypouricemia-specific design. Relevance graded **C** (low) — status unknown, disease link unconfirmed. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Review | Internal Medicine (Tokyo) | Discusses febuxostat as prophylaxis against exercise-induced acute kidney injury in patients who already have renal hypouricemia — not as a treatment for the hypouricemia itself. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | General narrative review of hypouricemia etiology and classification for rheumatologists; does not evaluate febuxostat as a therapeutic option. |

## EU Market Information

No marketing authorizations are currently on file for this candidate (`total_licenses: 0`, market status: 未上市／Not marketed).

## Safety Considerations

No structured safety data (warnings, contraindications, or drug interactions) is available in this evidence pack — DDI query returned no results. Please refer to the SmPC for safety information. Note: the pack flags TFDA label/warning data as a **Blocking** gap (DG001), meaning this candidate cannot proceed to a safety pre-assessment (S1) until that data is obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Renal Hypouricemia) is mechanistically contradictory to the drug's known pharmacology, and both linked evidence items fail to substantiate the indication on inspection — one trial is low-relevance/unconfirmed, and neither publication supports treating renal hypouricemia with febuxostat. This pattern is consistent with a disease-name/embedding artifact rather than a genuine signal.

**To proceed, the following is needed:**
- Manual verification of whether "hypouricemia, renal" was correctly mapped in the underlying TxGNN disease vocabulary (possible hyperuricemia/hypouricemia confusion)
- TFDA label warnings/contraindications (Blocking gap, DG001) before any safety pre-assessment
- Confirmed mechanism-of-action source, e.g., DrugBank API (High-priority gap, DG002)

**Worth noting separately:** two lower-ranked candidates in this same pack — *hypoxanthine guanine phosphoribosyltransferase partial deficiency* (rank 2, L4, decision stage S1) and *Lesch-Nyhan syndrome* (rank 3, L4, S1) — have mechanistically coherent, clinically plausible rationale (XO inhibition addressing purine-salvage-pathway hyperuricemia, mirroring existing off-label allopurinol use) and are flagged internally as "Research Question," making them stronger candidates for follow-up than the rank-1 prediction covered in this report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

