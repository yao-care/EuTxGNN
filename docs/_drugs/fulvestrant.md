---
layout: default
title: Fulvestrant
parent: 僅模型預測 (L5)
nav_order: 267
evidence_level: L5
indication_count: 10
---

# Fulvestrant
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

# Fulvestrant: From ER+/HER2- Metastatic Breast Cancer to HIV Infectious Disease

## One-Sentence Summary

Fulvestrant is a selective estrogen receptor degrader (SERD) whose established use is ER+/HER2- metastatic breast cancer; it is not currently marketed or licensed in this jurisdiction. The TxGNN model predicts it may be effective for **HIV Infectious Disease**, but this direction is currently supported by **0 clinical trials** and only **1 publication that does not actually address HIV**. Evidence strength is minimal and the mechanistic rationale is largely absent.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ER+/HER2- Metastatic Breast Cancer (drug classification cited in evidence pack; no formal license record in this jurisdiction) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is flagged as a data gap in this evidence pack (DG002). Based on information available elsewhere in the pack's own evidence annotations, Fulvestrant acts as a pure estrogen receptor (ER) antagonist/degrader (SERD class), with proven efficacy in ER+/HER2- metastatic breast cancer.

Estrogen receptor signaling has no established direct role in HIV viral replication or host antiviral immune defense. The pathophysiology of HIV infection (retroviral entry, reverse transcription, immune evasion, CD4+ T-cell depletion) does not intersect with the ER pathway that Fulvestrant targets.

The only literature returned for this pairing (PMID 40343334) is a cross-omics mechanism study of HTLV-1-associated myelopathy — a different retrovirus and a different disease — and does not mention Fulvestrant or ER signaling in the context of HIV treatment. Taken together, this prediction appears to be a high-scoring knowledge-graph output without a corroborating mechanistic or clinical basis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Mechanistic/cross-omics study | Research Square | Cross-omics analysis of HTLV-1-associated myelopathy (HAM), not HIV; does not evaluate Fulvestrant or ER-pathway involvement in HIV — low direct relevance to this predicted indication |

## EU Market Information

Fulvestrant is not currently marketed or licensed in this jurisdiction (0 authorizations on record).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (endocrine/hormonal — SERD class), not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials support Fulvestrant for HIV infection, the single available publication addresses an unrelated retroviral disease (HTLV-1, not HIV), and there is no established mechanistic link between ER antagonism and HIV pathophysiology. The TxGNN score alone (L5, model prediction only) is insufficient to justify advancing this candidate.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (currently a High-severity gap, DG002)
- TFDA/EMA label warnings and contraindications (currently a Blocking gap, DG001) before any safety pre-assessment (S1) can begin
- A dedicated mechanistic or preclinical study directly evaluating ER-pathway involvement in HIV infection
- Re-evaluation against higher-evidence candidates in this same drug's prediction set (e.g., rheumatoid arthritis, rank 6, which already reached decision stage S1 with L4 evidence and a "Research Question" recommendation) before committing resources to this rank-1 pairing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

