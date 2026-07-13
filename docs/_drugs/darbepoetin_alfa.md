---
layout: default
title: Darbepoetin Alfa
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 10
---

# Darbepoetin Alfa
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

# Darbepoetin alfa: From Anemia to Amenorrhea

## One-Sentence Summary

Darbepoetin alfa is a long-acting erythropoiesis-stimulating agent (ESA) widely used to treat anemia associated with chronic kidney disease and chemotherapy-induced anemia.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **0 clinical trials** and **0 publications** currently supporting this direction.
This prediction is based entirely on model inference and requires substantial further investigation before any clinical consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anemia (chronic kidney disease; chemotherapy-induced anemia) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 96.73% |
| Evidence Level | L5 |
| Market Status (Taiwan) | Not marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Darbepoetin alfa is a hyperglycosylated analogue of endogenous erythropoietin (EPO), engineered to have a longer serum half-life. It binds to EPO receptors on erythroid progenitor cells in bone marrow, stimulating red blood cell production. Its proven efficacy in treating anemia associated with chronic kidney disease and chemotherapy makes it an anchor point for TxGNN's graph-based inference.

The mechanistic link between Darbepoetin alfa and amenorrhea is indirect and speculative. Severe anemia is known to disrupt the hypothalamic-pituitary-gonadal (HPG) axis, leading to functional hypothalamic amenorrhea — a well-recognized consequence of energy deficit and systemic physiological stress. Correcting anemia with an ESA could theoretically restore the hormonal milieu necessary for normal menstruation. However, this represents a downstream, secondary effect rather than a direct pharmacological action on reproductive endocrinology.

Critically, this theoretical pathway is not supported by any clinical trial or published literature. EPO receptors have not been meaningfully demonstrated in hypothalamic or pituitary gonadotroph cells, and no prospective or observational studies have evaluated Darbepoetin alfa as a treatment for amenorrhea. The high TxGNN score (96.73%) most likely reflects the model capturing a co-morbidity pattern — anemia frequently co-occurs with reproductive dysfunction — rather than a direct causal or mechanistic relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Darbepoetin alfa in amenorrhea.

---

## Literature Evidence

Currently no related literature available for Darbepoetin alfa in amenorrhea.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note for reviewers:** TFDA label warnings and contraindications were not available in this Evidence Pack (Data Gap: DG001). Additionally, a separate safety signal was identified across the full prediction set: the literature for the rank-3 prediction (anaphylaxis) documents a case of Darbepoetin alfa itself *causing* anaphylaxis requiring desensitization (PMID [24129045](https://pubmed.ncbi.nlm.nih.gov/24129045/)). For the rank-10 prediction (HER2+ breast carcinoma), FDA black-box warnings regarding ESA use in cancer patients (increased mortality and tumor progression risk) are relevant context for any oncology-adjacent consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Darbepoetin alfa are rated L5 (model prediction only), with zero supporting clinical trials or peer-reviewed literature for the top-ranked indication (amenorrhea). The mechanistic link is speculative and entirely indirect, and two of the ten predictions (anaphylaxis, HER2+ breast carcinoma) carry active safety signals that would complicate any repurposing pathway.

**To proceed, the following is needed:**

- Retrieve and parse the TFDA SmPC (仿單) to establish baseline safety warnings and contraindications (DG001, Blocking)
- Confirm Darbepoetin alfa's full mechanism of action via DrugBank API (DG002, High)
- Conduct a targeted literature review beyond automated PubMed queries to identify any preclinical studies on EPO signalling in the hypothalamic-pituitary-gonadal axis
- Evaluate whether any of the 10 predicted indications achieves at least L4 evidence before progressing to Stage 1 evaluation
- Given the known ESA safety concerns in oncology (FDA warnings on tumor promotion), explicitly exclude cancer-adjacent indications from repurposing consideration until a full benefit-risk framework is established

---

*⚠️ This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

