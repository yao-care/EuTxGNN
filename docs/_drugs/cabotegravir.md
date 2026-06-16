---
layout: default
title: Cabotegravir
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Cabotegravir
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

# Cabotegravir: From HIV Infection to Rheumatoid Arthritis

## One-Sentence Summary

Cabotegravir is an HIV integrase strand transfer inhibitor (INSTI), approved internationally for HIV-1 prevention (PrEP) and treatment, but not currently registered in Taiwan.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with a high model confidence score of 99.45%.
However, **no clinical trials or supporting publications** have been identified for this indication, leaving the prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 Infection (Prevention / Treatment) — based on drug class (INSTI); not registered in Taiwan |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known information, Cabotegravir belongs to the integrase strand transfer inhibitor (INSTI) class of antiretroviral agents. It works by blocking the HIV-1 integrase enzyme, preventing viral DNA from being inserted into the host cell genome — an entirely virally-targeted mechanism with no known direct interaction with mammalian inflammatory pathways.

Rheumatoid arthritis (RA) is a chronic autoimmune disease driven by dysregulated T-cell and B-cell activity, pro-inflammatory cytokines (particularly TNF-α, IL-6, and IL-17), and synovial fibroblast proliferation. There is no established biological bridge between HIV integrase inhibition and these RA pathways. Some INSTI-class drugs have been observed to produce weak interactions with the NF-κB signalling pathway in vitro, but no studies have extended this observation to inflammatory arthritis models, and this remains speculative.

The TxGNN high score (0.9945) most likely reflects indirect knowledge graph connections — for example, shared protein network neighbors between HIV-related immune activation nodes and RA-associated inflammatory nodes — rather than a direct, biologically validated pharmacological link. Without mechanistic validation or any clinical signal, this prediction should be treated as a hypothesis-generating output only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Cabotegravir in Rheumatoid Arthritis.

> **Note:** 18 PubMed records were retrieved under the rank-10 prediction (Brain Small Vessel Disease 1 with or without Ocular Anomalies), but systematic review confirms all 18 are **disease background reviews** covering congenital ocular anomalies, syndromic disorders, and developmental genetics — none involve Cabotegravir as an intervention. These papers are therefore not cited as supporting evidence.

---

## Taiwan Market Information

Cabotegravir has no registered marketing authorizations in Taiwan. No product license data is available.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) and current prescribing information for safety data. Taiwan-specific label warnings and contraindications were not available in this evidence pack.

> From the known drug class profile: INSTI-class agents (including Cabotegravir) are generally well tolerated but carry class considerations including hypersensitivity reactions, hepatotoxicity in patients with underlying liver disease, and immune reconstitution inflammatory syndrome (IRIS). Long-acting injectable Cabotegravir (cabotegravir LA) has additional injection-site reaction considerations. These are not confirmed from this evidence pack and should be verified against the official SmPC.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high confidence score to this pairing, but no clinical trials, no intervention-focused literature, and no plausible mechanistic basis have been identified to support Cabotegravir as a candidate for rheumatoid arthritis. The evidence level is L5 (AI prediction only), which does not meet the threshold for further investment without additional mechanistic grounding.

**To proceed, the following is needed:**

- **MOA clarification**: Confirm whether any INSTI-class mechanism (e.g., NF-κB modulation, innate immune crosstalk) has been observed in inflammatory disease models; if so, quantify the magnitude and biological relevance
- **Knowledge graph path analysis**: Identify the specific protein–disease nodes driving the TxGNN score to assess whether the indirect link is biologically interpretable or an artefact of graph topology
- **Preclinical signal search**: Conduct a broader PubMed/EMBASE search for any in vitro or animal model data linking Cabotegravir (or the broader INSTI class) to arthritis, inflammation, or autoimmune modulation
- **Safety data retrieval**: Obtain Taiwan TFDA SmPC and international label (FDA/EMA) to complete the safety profile before any further evaluation
- **Market context**: Clarify Cabotegravir's current regulatory status in Taiwan and potential pathway for any new indication development, given zero existing local authorizations

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

