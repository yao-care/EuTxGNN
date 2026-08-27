---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

# Durvalumab: Toward a New Indication — Prostatic Urethra Urothelial Carcinoma

*(Original approved indication is not documented in this evidence pack — see Data Gap note below)*

## One-Sentence Summary

Durvalumab is an anti-PD-L1 monoclonal antibody (identified from clinical trial descriptions within this evidence pack, e.g. "Anti-PD-L1 Antibody (Durvalumab)" in NCT02812420); its original approved indication and formal mechanism-of-action record are **not available** in the current dataset (flagged as Data Gap DG002). The TxGNN model's top-ranked prediction is **Prostatic Urethra Urothelial Carcinoma** (score 99.98%), but this specific prediction currently has **zero clinical trials and zero publications** supporting it — it is a pure model prediction (L5). Within the same evidence pack, a lower-ranked candidate, **Endocervical Carcinoma** (rank 6), has meaningfully stronger support (2 clinical trials + 1 review, L2).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (Data Gap) |
| Predicted New Indication | Prostatic Urethra Urothelial Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| EU Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action (MOA) data for durvalumab is not available in this evidence pack (Data Gap DG002, severity: High), and the drug's original approved indication is also absent from the dataset. However, clinical trial records elsewhere in this same evidence pack consistently describe durvalumab as an **anti-PD-L1 immune checkpoint inhibitor antibody** (e.g. NCT02812420, NCT03912818, NCT04065269, NCT03452332), which allows a mechanistic interpretation even without a formal MOA field.

For the top-ranked prediction, the model's own rationale notes that prostatic urethra urothelial carcinoma is an anatomical sub-site of urothelial carcinoma, a tumour type in which anti-PD-L1 checkpoint blockade has an established biological rationale (PD-L1 expression driving immune evasion). The mechanistic logic is therefore plausible — the tumour lineage shares immune-microenvironment features with urothelial carcinomas already studied with durvalumab — but **no clinical trial or literature evidence in this pack directly supports this specific sub-type**, so the prediction currently rests entirely on the TxGNN model score (0.9998).

Notably, other candidates in this same evidence pack targeting related urothelial and PD-L1-relevant tumour types (kidney pelvis sarcomatoid transitional cell carcinoma, infiltrating bladder urothelial carcinoma sarcomatoid variant, and endocervical carcinoma) do have supporting trial and/or literature evidence, reinforcing that the underlying checkpoint-inhibition mechanism is being actively tested in adjacent disease areas — see "Other Predicted Indications" below.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Other Predicted Indications (Same Evidence Pack)

This evidence pack tracks 10 TxGNN-predicted indications for durvalumab. Ranked by TxGNN score, but evidence strength varies considerably — the strongest real-world support is found in **Endocervical Carcinoma (rank 6, L2)**, not the top-ranked prediction.

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Supporting Evidence |
|------|-------------------|-------------|-----------------|-----------------|------------------|----------------------|
| 2 | Kidney pelvis sarcomatoid transitional cell carcinoma | 99.98% | L3 | S1 | Research Question | 1 trial: [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) (Early Phase 1, n=54, Grade B) |
| 3 | Infiltrating bladder urothelial carcinoma, sarcomatoid variant | 99.98% | L3 | S1 | Research Question | 2 trials: [NCT03912818](https://clinicaltrials.gov/study/NCT03912818) (Phase 2, terminated, n=7, Grade C), [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) (Grade B) |
| 4 | Renal pelvis papillary urothelial carcinoma | 99.98% | L5 | S0 | Hold | None |
| 5 | Uterine ligament adenocarcinoma | 99.92% | L5 | S0 | Hold | None |
| 6 | Endocervical carcinoma | 99.91% | **L2** | **S2** | **Proceed with Guardrails** | 2 trials: [NCT04065269](https://clinicaltrials.gov/study/NCT04065269) (Phase 2, n=174), [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) (Phase 1, completed, n=20); 1 literature: [PMID 37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) (Review, 2023) |
| 7 | Adenoid cystic carcinoma of the cervix uteri | 99.91% | L5 | S0 | Hold | None |
| 8 | Uterine ligament serous adenocarcinoma | 99.91% | L5 | S0 | Hold | None |
| 9 | Signet ring cell variant cervical mucinous adenocarcinoma | 99.90% | L5 | S0 | Hold | None |
| 10 | Intestinal variant cervical mucinous adenocarcinoma | 99.90% | L5 | S0 | Hold | None |

Note: none of the trials above are durvalumab monotherapy trials — all use durvalumab in combination (with tremelimumab, chemotherapy, radiotherapy, or an ATR inhibitor/olaparib), so even the best-supported candidate (endocervical carcinoma) lacks single-agent efficacy evidence.

## EU Market Information

Durvalumab currently has **0 EU marketing authorization licenses** recorded in this evidence pack; market status is marked as **未上市 (Not Marketed)**. No product name, dosage form, or approved indication text is available to tabulate.

## Cytotoxicity

Durvalumab is an oncology therapeutic (anti-PD-L1 immune checkpoint inhibitor, identified from clinical trial descriptions in this pack) used across multiple carcinoma types, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (Anti-PD-L1 checkpoint inhibitor, per trial descriptions in this evidence pack) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data are all flagged as Blocking Data Gaps (DG001) in this evidence pack — TFDA/SmPC labelling has not yet been retrieved.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Prostatic Urethra Urothelial Carcinoma) has no clinical trial or literature evidence — it is a pure model prediction (L5, decision stage S0). In addition, a **Blocking**-severity data gap (DG001: missing TFDA/SmPC warnings and contraindications) prevents this candidate from even entering the S1 safety pre-screen, regardless of efficacy evidence.

**To proceed, the following is needed:**
- Retrieve TFDA/SmPC warnings, contraindications, and full prescribing information (Blocking gap, DG001)
- Retrieve durvalumab's formal mechanism-of-action and original approved-indication records (High-priority gap, DG002)
- If pursuing a repurposing candidate from this pack, consider re-scoping toward **Endocervical Carcinoma (rank 6)**, which already has L2 evidence (2 trials + 1 review) and a "Proceed with Guardrails" recommendation — a substantially stronger starting point than the top TxGNN-ranked prediction
- Direct clinical trial or literature search specific to prostatic urethra urothelial carcinoma, since none currently exists in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

