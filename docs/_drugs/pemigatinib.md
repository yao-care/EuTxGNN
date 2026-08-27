---
layout: default
title: Pemigatinib
parent: 僅模型預測 (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

# Pemigatinib: From FGFR2 Fusion-Positive Cholangiocarcinoma to Multiple Endocrine Neoplasia

## One-Sentence Summary

Pemigatinib is a selective FGFR1/2/3 tyrosine kinase inhibitor originally approved for FGFR2 fusion-positive cholangiocarcinoma (bile duct cancer). The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia**, but currently **0 clinical trials** and **0 publications** support this specific prediction — the mechanistic rationale itself flags this as likely knowledge-graph noise rather than a real biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | FGFR2 fusion-positive cholangiocarcinoma *(from general drug knowledge; not confirmed via EU marketing authorization data, as no EU license record exists for this product)* |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in structured form. Based on general drug knowledge, Pemigatinib belongs to the FGFR1/2/3 kinase inhibitor class, and its efficacy in FGFR2 fusion-positive cholangiocarcinoma has been clinically established. Whether this mechanism extends to multiple endocrine neoplasia (MEN) is the key question this prediction raises.

The relationship between the original indication and the predicted new indication is weak. MEN1 and MEN2 syndromes are driven primarily by MEN1 gene mutations or RET proto-oncogene mutations respectively — neither has an established direct connection to FGFR1/2/3 signaling. The high TxGNN score most likely reflects the proximity of "endocrine neoplasia" and "FGFR-related tumour" nodes within the knowledge graph's embedding space, rather than a genuine shared pharmacological mechanism.

Given this, the mechanism is **not well supported** as applicable to MEN. This is one of several candidates in the current prediction set (alongside veterinary-disease entries such as infectious bovine rhinotracheitis and malignant catarrh appearing at similar score ranges) that illustrate a known limitation of pure embedding-similarity predictions: high TxGNN scores do not by themselves indicate biological plausibility. Without any supporting trial or literature evidence, this prediction should be treated as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Pemigatinib currently has no EU marketing authorization on record (0 authorizations; market status: not marketed). No product/dosage-form/indication data is available to tabulate.

---

## Cytotoxicity

*(Included because the original indication, cholangiocarcinoma, is an oncology indication and Pemigatinib is a targeted anticancer kinase inhibitor.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR1/2/3 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score, there is no clinical trial or literature evidence supporting Pemigatinib for multiple endocrine neoplasia, and the mechanistic rationale itself indicates the prediction likely reflects knowledge-graph embedding noise rather than a real drug-disease relationship. In addition, safety data (warnings/contraindications) are a **blocking** data gap (DG001), which prevents even a preliminary safety evaluation (S1 stage).

**To proceed, the following is needed:**
- TFDA/EMA label warnings and contraindications (DG001, blocking — required before any safety pre-screening)
- Detailed mechanism of action (MOA) data (DG002)
- Preclinical or mechanistic studies establishing a credible FGFR–MEN pathway link, if one is to be pursued
- At minimum, one exploratory clinical or case-level report before advancing this candidate beyond hypothesis stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

