---
layout: default
title: Colesevelam
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 10
---

# Colesevelam
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

# Colesevelam: From Hyperlipidemia/Type 2 Diabetes to Gout

## One-Sentence Summary

Colesevelam is a bile acid sequestrant approved internationally for primary hypercholesterolemia and as an adjunct therapy to improve glycemic control in type 2 diabetes mellitus (T2DM), though it is not currently marketed in Taiwan.
The TxGNN model predicts it may be effective for **Gout**, with a prediction score of **93.37%** — however, **no clinical trials** and **no published literature** currently support this specific indication.
Among all 10 predicted indications analyzed, evidence remains limited to model prediction only, making the overall repurposing portfolio a low-priority exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Primary hypercholesterolemia; type 2 diabetes mellitus (glycemic control adjunct) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 93.37% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank query. Based on known information, Colesevelam is a non-absorbed polymeric bile acid sequestrant that works exclusively within the gastrointestinal lumen. It binds bile acids in the small intestine, preventing their enterohepatic reabsorption, which forces the liver to convert more cholesterol into bile acids — thereby reducing circulating LDL-cholesterol. A secondary effect, likely mediated through gut FXR (farnesoid X receptor) and TGR5 signaling modulation, results in improved incretin secretion and glycemic control in T2DM patients.

The connection between Colesevelam and gout is speculative. Bile acid sequestration and uric acid metabolism are not directly linked through any established pharmacological pathway. One theorized indirect route involves the gut microbiome: altered bile acid composition can shift intestinal microbial populations, which may modulate purine catabolism and thus influence serum uric acid levels. However, this chain of reasoning lacks any supporting clinical or animal study data.

The high TxGNN prediction score (0.934) most likely reflects indirect knowledge graph proximity — specifically, the well-documented associations among hypercholesterolemia, metabolic syndrome, and gout — rather than a direct pharmacological mechanism. Gout and dyslipidemia frequently co-occur in the context of metabolic syndrome, which may have inflated the model's confidence via shared graph nodes rather than a causal drug–disease pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Colesevelam is not currently approved or marketed in Taiwan. No regulatory authorizations are on record from the Taiwan Food and Drug Administration (TFDA).

> **Note:** Colesevelam is commercially available in other markets under brand names such as Welchol (US) and Cholestagel (EU) for hypercholesterolemia and T2DM indications. Taiwan-specific regulatory and safety label data (TFDA package insert) has not been retrieved and represents a blocking data gap for formal safety review.

---

## Safety Considerations

Please refer to the SmPC (Summary of Product Characteristics) or equivalent prescribing information for full safety details. Taiwan-specific warning and contraindication data (TFDA package insert) is currently unavailable.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence and no published literature supporting the use of Colesevelam specifically for gout. The mechanistic connection between bile acid sequestration and uric acid metabolism is indirect and highly speculative, and the high TxGNN score appears to reflect metabolic syndrome co-morbidity clustering in the knowledge graph rather than a true pharmacological signal.

**To proceed, the following is needed:**
- Retrieve TFDA package insert (SmPC equivalent) to complete the safety review — this is currently a **blocking data gap**
- Obtain detailed MOA data from DrugBank API to enable mechanistic plausibility assessment
- Conduct a targeted literature search for any observational evidence of gout incidence change in patients on Colesevelam for hyperlipidemia or T2DM
- Consider preclinical exploration of bile acid–gut microbiome–purine metabolism interactions before committing to clinical evaluation

> **Reviewer Note — Higher-Priority Repurposing Candidates:**
> Among the 10 predicted indications analyzed, **diabetic nephropathy** (Rank 7, TxGNN score 86.16%, Evidence Level L4, Stage S1) is the most mechanistically supported candidate. Colesevelam's approved glycemic benefit in T2DM directly addresses the primary driver of diabetic nephropathy, and a related bile acid sequestrant polymer (SAR442357, PMID [33203659](https://pubmed.ncbi.nlm.nih.gov/33203659/)) demonstrated disease-progression delay in a rat nephropathy model. Clarifying whether the renal-protective effect in that study is attributable to the bile acid axis (supporting Colesevelam extrapolation) or to the phosphate-sequestering component (not applicable to Colesevelam) is the key mechanistic question to resolve before designing any clinical study.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

