---
layout: default
title: Enzalutamide
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
---

# Enzalutamide
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

Using the evidence pack as given — I'll note upfront that `predicted_indications[0]` (rank 1, highest TxGNN score) is the weakest-evidenced candidate in this pack, which the report below reflects honestly (Hold decision) rather than reframing.

---

# Enzalutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Enzalutamide is a second-generation androgen receptor (AR) signaling inhibitor originally developed for prostate cancer. The TxGNN model's top-ranked prediction associates it with **"prostate cancer/brain cancer susceptibility"** — a node that appears to represent a shared genetic susceptibility pathway rather than a treatable disease — with a **99.71% prediction score**, but **zero clinical trials and zero publications** currently support this specific link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (based on established drug knowledge; no TFDA license record available in this evidence pack — Data Gap DG001) |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.71% (rank 3717 of all candidates) |
| Evidence Level | L5 |
| EU Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on known information, enzalutamide is an androgen receptor (AR) signaling inhibitor that blocks testosterone-driven transcriptional activity — its efficacy in prostate cancer, which is largely AR-dependent, is well established.

The predicted new indication, "prostate cancer/brain cancer susceptibility," does not describe a treatable brain tumor. According to the model's own rationale, this node most likely represents a shared genetic susceptibility locus (e.g., HOXB13) that statistically co-associates with both prostate and brain cancer risk in the knowledge graph — not a pharmacological relationship. AR antagonism has no established mechanistic link to brain cancer, so this pairing is best understood as an embedding-similarity artifact rather than a genuine repurposing signal.

For context, this same evidence pack contains other enzalutamide–disease pairs with much stronger support — e.g., "male reproductive organ cancer" (L2) and "prostate neoplasm" (L1, backed by pivotal trials such as PROSPER and PREVAIL) — but those largely reflect enzalutamide's **already-known** prostate cancer indication rather than a novel repurposing opportunity. The rank-1 candidate evaluated here is the one flagged for repurposing consideration, and it currently lacks any clinical or mechanistic support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (androgen receptor signaling inhibitor) — based on established drug classification; detailed DrugBank MOA/toxicity data not available in this evidence pack (Data Gap DG002) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN similarity score, the "prostate cancer/brain cancer susceptibility" prediction has no clinical trials, no literature, and no plausible pharmacological mechanism connecting AR antagonism to brain cancer — it most likely reflects a genetic co-susceptibility artifact in the knowledge graph rather than a treatable repurposing target. Additionally, TFDA label warnings/contraindications are a **Blocking** data gap (DG001), which independently prevents any safety evaluation (S1) from proceeding.

**To proceed, the following is needed:**
- TFDA-approved label warnings and contraindications (resolves Blocking Data Gap DG001)
- Confirmed mechanism of action from DrugBank (resolves Data Gap DG002)
- Mechanistic or preclinical evidence clarifying whether the underlying association is genetic (e.g., HOXB13 susceptibility) rather than pharmacological, before any further investment
- If a genuine repurposing signal is desired, consider evaluating the more directly evidenced prostate-cancer-adjacent candidates in this pack (L1–L2) instead of this L5 node
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

