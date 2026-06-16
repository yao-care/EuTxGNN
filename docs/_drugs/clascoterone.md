---
layout: default
title: Clascoterone
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
---

# Clascoterone
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

# Clascoterone: From Acne Vulgaris to Candidiasis

## One-Sentence Summary

Clascoterone is a topical androgen receptor (AR) antagonist approved in the United States for acne vulgaris, with no current EU marketing authorization on record.
The TxGNN model predicts it may be effective for **Candidiasis**,
with **no clinical trials** and **no publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne Vulgaris |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 94.82% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Clascoterone is a topical androgen receptor (AR) antagonist that competitively binds AR in sebaceous glands and hair follicles, reducing sebum production and the inflammatory cascade that drives acne vulgaris. Structurally, it is a 17α-propionate ester of 11-deoxycortisol — a cortisol precursor — which distinguishes it from systemic AR antagonists and limits its off-target endocrine effects.

The proposed link between acne and candidiasis is highly indirect. Androgen signaling is known to modulate macrophage polarization and innate immune function, and androgen excess has been associated with impaired clearance of certain pathogens in some experimental contexts. The speculative hypothesis is that AR blockade might enhance the host's antifungal immune response. However, no preclinical, in vitro, or clinical studies have examined this connection for Clascoterone specifically.

Critically, Clascoterone is formulated for topical skin application with extremely low systemic absorption — a property that is central to its favourable safety profile in acne, but that also makes meaningful systemic immunomodulation biologically implausible. The high TxGNN score most likely reflects graph propagation through shared immune comorbidity nodes in the knowledge graph, rather than a direct mechanistic pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure L5 prediction (AI model only) with zero supporting clinical trials or literature. The mechanistic bridge between topical AR antagonism and systemic candidiasis is biologically implausible given Clascoterone's topical route and negligible systemic exposure — the drug cannot plausibly reach concentrations needed to modulate the immune microenvironment at mucosal infection sites.

**To proceed, the following is needed:**
- Retrieve full MOA and safety data (TFDA SmPC / EU SmPC) to complete baseline risk assessment
- Commission in vitro studies examining whether AR signalling directly affects *Candida* growth or macrophage antifungal activity
- Consider redirecting discovery effort toward indications with stronger mechanistic plausibility:
  - **Atrophoderma vermiculata** (Rank 6): AR-pathway link through follicular biology is mechanistically closer to the approved acne indication
  - **Adrenal gland hyperfunction / CAH** (Rank 9): Structural homology to cortisol precursors provides a direct biological rationale worth exploring
- Any further pursuit of the candidiasis hypothesis should begin with a formulation feasibility assessment — a mucosally-delivered AR antagonist would be an entirely different product from the approved topical cream
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

