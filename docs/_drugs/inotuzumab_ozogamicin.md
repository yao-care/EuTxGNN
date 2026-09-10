---
layout: default
title: Inotuzumab Ozogamicin
parent: 僅模型預測 (L5)
nav_order: 312
evidence_level: L5
indication_count: 10
---

# Inotuzumab Ozogamicin
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

# Inotuzumab Ozogamicin: From CD22+ B-Cell Malignancy (Original Indication Data Pending) to Drug-Induced Osteoporosis

## One-Sentence Summary

Inotuzumab ozogamicin is a CD22-targeted antibody-drug conjugate (ADC); its confirmed original indication is not yet available in this evidence pack (label/TFDA data pending). The TxGNN model's top-ranked association is with **drug-induced osteoporosis** (score 98.24%), but this is supported by **zero clinical trials and zero literature**, and the model's own mechanistic annotation suggests the link — if real — more likely reflects a known adverse-reaction pathway (chemotherapy-related bone effects) rather than a genuine treatment indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (original_indications empty; TFDA label data pending — see Data Gap DG001) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 98.24% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this drug (Data Gap DG002). Based on information present elsewhere in the evidence pack, inotuzumab ozogamicin is described as an anti-CD22 antibody-drug conjugate (ADC) — CD22 is a B-lymphocyte lineage marker, indicating this drug's known biology is centered on B-cell malignancies rather than bone or connective tissue disease.

For the top-ranked prediction, "drug-induced osteoporosis," the model's own rationale states there is **no positive treatment mechanism** connecting a CD22-targeted ADC to bone density preservation. If any real-world association exists, it more plausibly reflects a chemotherapy-associated adverse effect on bone metabolism (an adverse-reaction signal) rather than a therapeutic opportunity — and no clinical trial or publication currently supports either interpretation.

It is also worth noting a pattern across this candidate set: several lower-ranked breast-cancer-related predictions (HER2-positive, luminal A/B, PR-positive/negative) carry no plausible mechanistic link to a CD22-targeted ADC, and the one candidate that did return literature ("breast tumor luminal A or B") retrieved papers about generic B-cell immunology and hepatitis B vaccines — consistent with a keyword/embedding collision on "B" rather than a genuine disease association. This raises the possibility that the ranking for this drug is affected by systematic noise, and reinforces caution in interpreting the top prediction at face value.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Inotuzumab ozogamicin is not currently marketed in Taiwan (0 authorizations on record); no license data is available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Antibody-drug conjugate, anti-CD22) |
| Myelosuppression Risk | Medium–High — the evidence pack notes known hematologic toxicity signals (e.g., thrombocytopenia, platelet/von Willebrand factor interaction) associated with this drug |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | CBC with platelet count; please refer to the SmPC for full monitoring requirements |
| Handling Protection | As an ADC-class antineoplastic agent, cytotoxic drug handling precautions should apply pending confirmation via SmPC |

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for this drug are rated L5 (model prediction only, decision stage S0) with a system-generated Hold recommendation. The top-ranked candidate lacks any supporting clinical trial or literature evidence, and the model's own rationale suggests it may represent an adverse-reaction signal rather than a treatable indication; several other candidates show signs of embedding-level keyword confusion (e.g., "B" collisions with B-cell biology).

**To proceed, the following is needed:**
- TFDA label / original indication and contraindication data (Data Gap DG001, blocking)
- Confirmed mechanism of action from DrugBank (Data Gap DG002)
- Independent pharmacological review of the drug-induced osteoporosis hypothesis to distinguish adverse-effect signal from therapeutic potential
- Re-evaluation of the breast-cancer-related candidates for possible embedding/keyword artifacts before further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

