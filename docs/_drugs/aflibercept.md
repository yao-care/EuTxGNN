---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Aflibercept
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

# Aflibercept: From Neovascular Ocular Disease to Esotropia

## One-Sentence Summary

Aflibercept is a recombinant VEGF Trap biologic, internationally approved for neovascular ocular conditions (wet AMD, diabetic macular edema) and metastatic colorectal cancer, but currently not marketed in Taiwan.
The TxGNN model predicts it may be effective for **Esotropia** (inward eye deviation),
however with **0 clinical trials** and **0 publications** directly supporting this direction, this remains an AI-only prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; internationally approved for wet AMD, DME, and mCRC |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Aflibercept (Eylea / Zaltrap) is a recombinant fusion protein consisting of the extracellular domains of VEGFR1 and VEGFR2 fused to the Fc region of human IgG1. It functions as a high-affinity "VEGF Trap," binding VEGF-A, VEGF-B, and placental growth factor (PlGF), thereby blocking angiogenesis driven by these ligands. This mechanism has been validated in wet AMD, diabetic macular edema, macular edema following retinal vein occlusion, and (as ziv-aflibercept) metastatic colorectal cancer.

Esotropia is a form of strabismus where one or both eyes deviate inward. Its primary etiology is neuromuscular — involving imbalance in extraocular muscle control, refractive error (accommodative esotropia), or cranial nerve palsy — none of which are VEGF-mediated processes. Standard treatments are surgical realignment, optical correction, and prism therapy. While VEGF has been implicated as a secondary factor in retinopathy of prematurity (ROP), which can cause cicatricial strabismus, this represents an indirect, limited connection rather than a direct therapeutic target.

The high TxGNN score (99.38%) most likely reflects Aflibercept's strong graph-network proximity to the ophthalmic disease domain in the knowledge graph, rather than a specific biologically plausible mechanism for esotropia. The mechanistic link, as assessed in the evidence pack's own rationale, is rated as extremely weak, with no direct VEGF-driven pathological pathway identified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Aflibercept in esotropia.

---

## Literature Evidence

Currently no related literature available for Aflibercept in esotropia.

---

## Taiwan Market Information

Aflibercept is currently **not marketed in Taiwan**. No TFDA marketing authorizations are on record for this drug.

> Note: Internationally, Aflibercept is marketed as **Eylea** (ophthalmic, Bayer/Regeneron) for wet AMD and retinal conditions, and as **Zaltrap** (intravenous, Sanofi) for metastatic colorectal cancer. Taiwan-specific regulatory status should be confirmed directly with TFDA.

---

## Safety Considerations

Taiwan TFDA package insert data (warnings and contraindications) was not available at the time of this report generation. Please refer to the internationally approved SmPC / prescribing information for safety guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score, the mechanistic connection between Aflibercept's anti-VEGF action and esotropia is weak — esotropia is primarily a neuromuscular eye alignment disorder without an established VEGF-driven pathological pathway. With zero supporting clinical trials or publications, and no Taiwan regulatory approval, this prediction does not meet the minimum threshold for further development at this time.

**To proceed, the following is needed:**
- Identification of a mechanistically justifiable esotropia subtype (e.g., ROP-associated strabismus with documented VEGF involvement) where anti-VEGF treatment could plausibly modify disease course
- Retrieval of Aflibercept's full MOA data from DrugBank API to confirm receptor binding profile
- Download and parsing of Taiwan TFDA package insert PDF to assess local safety profile and contraindications
- At minimum one published case report or preclinical study demonstrating anti-VEGF effects on ocular alignment before escalating to evidence collection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

