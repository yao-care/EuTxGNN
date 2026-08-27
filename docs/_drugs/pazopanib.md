---
layout: default
title: Pazopanib
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 10
---

# Pazopanib
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

# Pazopanib: From Renal Cell Carcinoma to Unclassified Renal Cell Carcinoma

## One-Sentence Summary

Pazopanib is a multi-target tyrosine kinase inhibitor with an established therapeutic background in renal cell carcinoma (RCC) and non-adipocytic soft tissue sarcoma. The TxGNN model predicts it may also be effective for **Unclassified Renal Cell Carcinoma**, a rare RCC subtype, with a prediction score of **99.63%**, currently supported by **1 completed Phase 3 clinical trial** and **6 publications** (mostly real-world/retrospective studies on non-clear-cell RCC). Two data gaps — missing TFDA/EMA label safety information (Blocking) and missing structured mechanism-of-action data (High) — currently prevent a full safety assessment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available as a structured field in this dataset (Data Gap); evidence-pack context repeatedly references pazopanib's existing approved use in advanced/metastatic renal cell carcinoma and non-adipocytic soft tissue sarcoma (e.g., PALETTE trial context) |
| Predicted New Indication | Unclassified renal cell carcinoma |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L3 |
| EU Market Status | Not Marketed (dataset shows 0 licenses — this may reflect an incomplete regulatory record rather than confirmed non-marketing, since MOA/label data is also flagged as missing) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for pazopanib is not available in this dataset (Data Gap DG002). Based on information embedded in the supporting evidence (trial and literature descriptions), pazopanib is described as a multi-target tyrosine kinase inhibitor acting on VEGFR, PDGFR, and c-Kit, with anti-angiogenic and anti-tumor activity. Its efficacy in advanced/metastatic clear-cell renal cell carcinoma is well documented, and it is referenced across multiple trials as a standard treatment option for that broader disease category.

Unclassified renal cell carcinoma falls within the same overarching RCC disease family as pazopanib's established indication, but represents a rarer, histologically distinct subtype outside clear-cell RCC. The mechanistic rationale is that VEGF/PDGF-driven angiogenesis — the pathway pazopanib targets — is not exclusive to clear-cell histology, so activity may extend to non-clear-cell subtypes including the unclassified category. However, the single available Phase 3 trial (NCT01613846) was designed around general advanced/metastatic RCC (a sequencing study, sorafenib vs. pazopanib), not specifically unclassified histology, and its relevance grading in this evidence pack is still marked "pending." The six literature entries similarly focus on the broader "non-clear-cell RCC" category rather than the unclassified subtype in isolation.

Taken together, the prediction is mechanistically plausible and partially supported by real-world/retrospective evidence on the wider non-clear-cell RCC population, but direct, subtype-specific confirmation for unclassified RCC is still limited — hence the conservative L3 evidence-level assignment rather than L1/L2.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01613846](https://clinicaltrials.gov/study/NCT01613846) | Phase 3 | Completed | 544 | Randomized sequential study of sorafenib followed by pazopanib vs. pazopanib followed by sorafenib in advanced/metastatic RCC; evaluates optimal sequencing of TKIs. Population is general advanced/metastatic RCC, not specifically the unclassified subtype — relevance to this indication is not yet confirmed (marked "pending" in source data). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Phase II, single-arm, open-label | Cancer Research and Treatment | Prospective single-arm Phase II study of pazopanib in non-clear-cell RCC (nccRCC); designed to determine efficacy and safety in this broader histology group. |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Retrospective multicenter (PANORAMA study) | Clinical Genitourinary Cancer | Italian multicenter retrospective analysis of first-line pazopanib efficacy and toxicity in nccRCC patients. |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Retrospective cohort | Clinical Genitourinary Cancer | Outcomes of metastatic non-clear-cell RCC patients treated with pazopanib; notes limited outcome data in this setting. |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Real-world retrospective comparative study | Ecancermedicalscience | Compares first-line sunitinib vs. pazopanib in nccRCC and sarcomatoid RCC, questioning whether the two agents are interchangeable in these histologies. |
| [30268423](https://pubmed.ncbi.nlm.nih.gov/30268423/) | 2019 | Retrospective case series / literature review | Clinical Genitourinary Cancer | Describes carcinoma of unknown primary with mRCC histologic features (CUP-mRCC) and reviews VEGF-inhibitor therapy outcomes, including pazopanib, in this rare group. |
| [41558869](https://pubmed.ncbi.nlm.nih.gov/41558869/) | 2026 | Retrospective database study (IMDC) | European Urology Oncology | International database analysis comparing contemporary vs. traditional first-line therapies across nccRCC histologic subtypes, including unclassified RCC, papillary RCC, and chromophobe RCC. |

---

## EU Market Information

No EU marketing authorization records are available in this dataset (Number of Authorizations: 0, Market Status: Not Marketed). This status should be verified directly against the EMA register before being treated as final, since the drug's mechanism-of-action and label data are also flagged as missing (DG001, DG002) — suggesting the regulatory data collection for this candidate may be incomplete rather than confirming an absence of any EU authorization.

---

## Safety Considerations

Please refer to the SmPC for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in this evidence pack (DG001: TFDA/EMA label warnings/contraindications — Blocking severity; DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The safety data gap (DG001) is classified as **Blocking** — it explicitly prevents this candidate from entering the S1 safety initial-screening stage, so no Go or Guardrails decision can responsibly be made yet regardless of the efficacy signal. In addition, the evidence directly supporting *unclassified* renal cell carcinoma specifically (rather than the broader non-clear-cell RCC category) is still indirect: the one Phase 3 trial and six literature items have relevance/classification fields marked "pending" in the source data, supporting an L3 (observational-evidence) rather than a higher evidence level.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/EMA product label (warnings, contraindications) to complete the S1 safety initial assessment
- Resolve DG002: obtain structured mechanism-of-action data from DrugBank to strengthen the mechanistic-link analysis
- Confirm/verify relevance grading for NCT01613846 and the six literature items specifically against the "unclassified RCC" histology (currently marked "pending")
- Verify actual EU marketing authorization status for pazopanib, given the apparent inconsistency between "0 licenses / Not Marketed" and its established global TKI use
- Note: the same evidence pack shows a stronger, more mature signal for **liposarcoma** (rank 4: L2, decision stage S2, 9 clinical trials including multiple completed Phase 2 studies and 20 publications) — this may warrant a separate, higher-priority evaluation track alongside the unclassified RCC candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

