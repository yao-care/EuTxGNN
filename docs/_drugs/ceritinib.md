---
layout: default
title: Ceritinib
parent: 僅模型預測 (L5)
nav_order: 138
evidence_level: L5
indication_count: 10
---

# Ceritinib
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

# Ceritinib: From ALK+ Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Ceritinib (Zykadia®) is a second-generation, oral anaplastic lymphoma kinase (ALK) inhibitor originally developed and approved for the treatment of ALK-rearranged non-small cell lung cancer (NSCLC).
The TxGNN model predicts it may be effective for **Gingival Fibromatosis** with a prediction score of 99.86%, yet **no clinical trials** and **no supporting publications** exist for this indication.
The mechanistic link between ALK inhibition and gingival fibromatosis is not established; this prediction likely reflects a knowledge graph generalization artifact rather than a true biological relationship.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive non-small cell lung cancer (NSCLC) |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| EU Market Status | Not found in dataset (0 authorizations recorded) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Ceritinib is a potent and selective second-generation ALK tyrosine kinase inhibitor — approximately 20-fold more potent than the first-generation inhibitor crizotinib. It competitively blocks the ATP-binding site of the ALK kinase domain, suppressing downstream proliferative and survival signaling in tumors driven by ALK fusion genes (most commonly EML4-ALK in NSCLC). Ceritinib also inhibits IGF-1R and FAK at clinically relevant concentrations.

Gingival fibromatosis is a rare benign condition characterized by progressive fibrous overgrowth of gingival connective tissue. Its primary pathophysiological drivers are TGF-β/SMAD pathway activation and excessive gingival fibroblast proliferation — mechanisms entirely distinct from ALK-driven oncogenesis. ALK has no established expression, mutation, or functional role in gingival fibromatosis in the published literature.

The high TxGNN prediction score (99.86%) for this pairing is most likely attributable to a knowledge graph topology effect: "fibromatosis" disease nodes cluster near other fibrotic or proliferative conditions (such as ALK-positive inflammatory myofibroblastic tumors) within the graph, creating proximity-based score inflation that does not reflect biological plausibility. Without any mechanistic evidence or supporting literature, this prediction does not support further development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EU marketing authorizations are recorded for Ceritinib in the current dataset.

> **Dataset note:** Ceritinib (Zykadia®, Novartis) received EMA marketing authorization in May 2015 for ALK-positive NSCLC. The absence of records here may indicate a data gap or a subsequent regulatory change. Please verify current EU authorization status directly via the [EMA product page](https://www.ema.europa.eu/en/medicines/human/EPAR/zykadia).

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Second-generation ALK tyrosine kinase inhibitor (small molecule, oral) |
| Myelosuppression Risk | Low (ALK inhibitors have minimal direct myelotoxicity; hematological toxicity is not a primary concern) |
| Emetogenicity Classification | Low to moderate (GI adverse effects including nausea, diarrhea, and vomiting are common at standard doses) |
| Monitoring Items | Liver function (ALT/AST/bilirubin), serum amylase and lipase (pancreatitis risk), fasting blood glucose, ECG (QTc prolongation), CBC |
| Handling Protection | Standard oral cytotoxic handling precautions apply per institutional policy |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No mechanistic basis links ceritinib's ALK inhibition to gingival fibromatosis — the condition is driven by TGF-β/SMAD fibroblast hyperactivation, not ALK signaling — and the evidence level is L5 (model prediction only, zero clinical or pre-clinical studies). The high TxGNN score is assessed as a knowledge graph generalization artifact.

**To proceed, the following would be needed:**
- Evidence of ALK expression or constitutive activation in gingival fibroblasts or gingival fibromatosis biopsy tissue
- Mechanistic studies demonstrating ALK pathway crosstalk with TGF-β/SMAD-driven fibrosis
- Resolution of the MOA data gap (DrugBank query recommended)
- Complete safety profile from the EMA SmPC, including key warnings and contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

