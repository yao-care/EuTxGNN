---
layout: default
title: Lonafarnib
parent: 僅模型預測 (L5)
nav_order: 362
evidence_level: L5
indication_count: 10
---

# Lonafarnib
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

# Lonafarnib: From Hutchinson-Gilford Progeria Syndrome to Leprosy

## One-Sentence Summary

Lonafarnib is a farnesyltransferase inhibitor (FTI) originally developed and approved for Hutchinson-Gilford Progeria Syndrome (HGPS), where it blocks Ras protein farnesylation. The TxGNN model predicts it may be effective for **Leprosy**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and no known mechanistic link between the drug and this disease has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hutchinson-Gilford Progeria Syndrome (HGPS) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Lonafarnib is a farnesyltransferase inhibitor (FTI) that blocks post-translational farnesylation of Ras and related proteins. Its approved use is in HGPS, a rare progeroid genetic disorder, where inhibiting farnesylation of defective progerin/lamin A reduces nuclear membrane abnormalities.

For the top-ranked prediction, **leprosy**, no known mechanistic relationship exists. Leprosy pathophysiology is driven by *Mycobacterium leprae* infection, host immune evasion, and granulomatous inflammation — pathways that do not overlap with known farnesyltransferase biology. The high TxGNN score for this pairing is most plausibly explained by indirect, noisy connections within the underlying knowledge graph rather than a genuine pharmacological rationale.

Notably, a lower-ranked candidate in this evidence pack — **rheumatoid arthritis** (rank 2, score 98.82%) — has a more plausible theoretical basis: FTI-mediated blockade of Ras/MEK/ERK signaling could in principle reduce synoviocyte proliferation and inflammation. However, the only literature retrieved for that pairing (PMID 36543278) concerns a traditional Chinese medicine formula acting on the same pathway, not lonafarnib itself, so it remains indirect, pathway-level evidence rather than drug-specific support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

Lonafarnib currently holds no EU marketing authorization (market status: not marketed; 0 authorizations on file), so no product/dosage-form/indication information is available.

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (leprosy) is an L5, model-only prediction with no clinical trials, no literature, and no identifiable mechanistic link — the repurposing rationale itself flags this as likely knowledge-graph noise. There is currently no basis to advance this pairing.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001 (TFDA/regulatory label warnings and contraindications) before any safety pre-screening (S1) can occur
- Resolve high-priority data gap DG002 (confirmed MOA record) to support mechanistic-linkage analysis
- If pursuing repurposing further, prioritize investigation of the rheumatoid arthritis signal (rank 2) instead, since it has a pathway-level rationale (Ras/MEK/ERK), and seek lonafarnib-specific preclinical or clinical evidence for that pathway rather than the leprosy pairing
- DrugBank category and toxicity data to determine whether cytotoxic-drug handling precautions apply
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

