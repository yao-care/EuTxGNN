---
layout: default
title: Agalsidase Beta
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 10
---

# Agalsidase Beta
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

# Agalsidase Beta: From Fabry Disease to Cervical Neuroblastoma

## One-Sentence Summary

Agalsidase beta (Fabrazyme) is a recombinant enzyme replacement therapy for Fabry disease, a lysosomal storage disorder caused by α-galactosidase A deficiency.
The TxGNN model predicts it may have activity in **cervical neuroblastoma**, with **0 clinical trials** and **0 publications** currently supporting this direction — making this a model-only prediction with no empirical support.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Fabry disease (lysosomal storage disorder; α-galactosidase A deficiency) |
| Predicted New Indication | Cervical Neuroblastoma |
| TxGNN Prediction Score | 98.37% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Agalsidase beta is a recombinant human α-galactosidase A, used as enzyme replacement therapy (ERT) for Fabry disease. It works by substituting the deficient lysosomal enzyme to break down Gb3 (globotriaosylceramide) deposits that accumulate in vascular endothelium, kidney, heart, and peripheral nerves.

The predicted target, cervical neuroblastoma, is an extremely rare pediatric malignancy arising from neural crest cells. Its pathogenesis involves MYCN amplification, ALK mutations, and aberrant sympathetic nervous system development — none of which overlap with lysosomal Gb3 clearance. Although lysosomal dysfunction has been studied in neuroblastoma biology, there is no established evidence that exogenous enzyme replacement therapy could exert anti-tumor effects via this pathway.

A critical analytical concern: the top 10 TxGNN predictions for Agalsidase beta are dominated by rare head-and-neck and skull base tumors (neuroblastoma, schwannoma, meningioma, benign oral neoplasms). Scores for ranks 4–7 differ by less than 0.0001 (0.98308–0.98304), which strongly suggests systematic knowledge graph node clustering — specifically around "head and neck" and "nervous system" anatomical nodes — rather than independent biological signals. Fabry disease's known peripheral neuropathy may have created indirect KG pathways to these nodes, artificially inflating prediction scores across this cluster.

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
Despite a high TxGNN score (98.37%), all 10 top predictions are at evidence level L5 (model prediction only), with zero supporting clinical trials or literature for any indication. The mechanistic connection between lysosomal enzyme replacement and cervical neuroblastoma is not biologically plausible with current evidence, and the scoring pattern across the top-10 list is consistent with systematic model output bias rather than genuine independent repurposing signals.

**To proceed, the following is needed:**
- Retrieve full mechanism of action data (DrugBank API)
- Biological plausibility assessment: Does lysosomal Gb3 accumulation or ERT play any demonstrable role in neural crest tumor development?
- Preclinical evidence (cell line or animal model data) examining any anti-tumor or anti-proliferative effect of Agalsidase beta
- TFDA SmPC download and parsing for safety warnings and contraindications (currently Blocking gap)
- Independent validation to rule out KG clustering artifact — consider whether the head-and-neck tumor cluster reflects true signal or graph topology bias before pursuing any single indication further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

