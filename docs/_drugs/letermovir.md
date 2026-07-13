---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
---

# Letermovir
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

# Letermovir: From CMV Prophylaxis to Vulvovaginal Candidiasis

## One-Sentence Summary

Letermovir is a first-in-class CMV DNA terminase complex inhibitor established for preventing cytomegalovirus (CMV) infection in haematopoietic stem cell transplant (HSCT) recipients.
The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis** with a score of 99.88%, however **no clinical trials or supporting literature** exist for this direction.
This prediction is very likely a model artefact — Letermovir targets a viral enzyme entirely absent in fungi — and the current recommendation is to Hold.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CMV prophylaxis in HSCT recipients (established use; no EU authorization record found in dataset) |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed (0 authorizations in dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally available in the Evidence Pack. Based on established scientific knowledge, Letermovir (brand name Prevymis) belongs to a novel class of antivirals that selectively inhibits the CMV DNA terminase complex — a three-subunit viral enzyme (UL56 / UL89 / UL51) responsible for cleaving and packaging viral DNA into newly assembled capsids. This mechanism of action is entirely specific to the *Herpesviridae* family and has no structural or functional counterpart in any fungal pathogen.

Vulvovaginal candidiasis is caused by *Candida* spp. (predominantly *C. albicans*), which are eukaryotic fungi. All clinically effective antifungal drug classes act through targets unrelated to DNA terminase: azoles disrupt ergosterol biosynthesis, polyenes form pores in the fungal cell membrane, and echinocandins inhibit β-(1,3)-glucan synthase in the cell wall. None of these mechanisms overlap with CMV DNA packaging, and *Candida* spp. do not encode any homologue of the herpesvirus terminase complex.

The TxGNN model's very high prediction score (99.88%) almost certainly reflects spurious signal propagation between "viral infectious disease" and "fungal infectious disease" node clusters in the underlying knowledge graph — both belong to the same broad infection category neighbourhood — rather than any biologically plausible cross-indication mechanism. This prediction should be regarded as a false positive, and no further investigation is warranted for this specific indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU authorization records are present in the current dataset (0 authorizations recorded). This appears to be a data pipeline gap: Letermovir (Prevymis) is externally documented as EMA-approved for CMV prophylaxis in adult CMV-seropositive HSCT recipients. Please verify current authorization status and SmPC directly via the [EMA product database](https://www.ema.europa.eu/en/medicines).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Vulvovaginal candidiasis is a fungal disease, and Letermovir's pharmacological target — the CMV DNA terminase complex — is a viral enzyme with no equivalent in fungi. There is zero mechanistic, preclinical, or clinical evidence to support antifungal activity, and the TxGNN high score is consistent with a graph-neighbourhood artefact rather than a real biological signal.

**To proceed, the following is needed:**

- No further investigation of this specific indication is recommended.
- Resources should be redirected to the higher-priority repurposing hypotheses identified within the same prediction set:
  - **AIDS / HIV co-infection** (Rank 7 — L3, "Research Question"): A completed open-label randomised pilot study (NCT05362916, N=33) assessed Letermovir's effect on gut inflammation in ART-treated, CMV-seropositive people living with HIV; reviewing its published results (linked to PMID 36690406) should be the immediate next step. A second terminated Phase 2 RCT (NCT04840199, N=44) warrants investigation of the termination reason before this direction is advanced further.
  - **Varicella Zoster Infection** (Rank 10 — L4, "Research Question"): A 2024 mutagenesis study (PMID 38517165) directly characterises Letermovir's interaction with the VZV portal protein, providing an early mechanistic hypothesis for cross-herpesvirus activity. In vitro VZV activity confirmation is the critical next step before any clinical study is considered.
  - **Fungal Infectious Disease via indirect immune pathway** (Rank 2 — L4, Hold): PMID 41371495 (2026 cohort) directly examines whether Letermovir prophylaxis reduces invasive fungal infections in HSCT patients through CMV-mediated immune suppression. Reviewing this result is warranted before finalising a blanket "Hold" on any CMV–fungal infection relationship.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

