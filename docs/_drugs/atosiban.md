---
layout: default
title: Atosiban
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
---

# Atosiban
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

# Atosiban: From Threatened Preterm Labor to Primary Hereditary Glaucoma

## One-Sentence Summary

Atosiban is an oxytocin and vasopressin V1A receptor antagonist, approved in Europe (as Tractocile) as a tocolytic to delay threatened preterm labor, but not registered in Taiwan.
The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, ranking this indication first among all candidates with a score of **99.92%**.
However, there are currently **no clinical trials** and **no publications** directly supporting this direction, making this an entirely model-driven prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Threatened preterm labor (tocolytic) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Atosiban is a competitive antagonist of oxytocin (OT) receptors and vasopressin V1A receptors. Its established clinical role is as a uterine relaxant — it inhibits oxytocin-driven myometrial contractions to delay preterm delivery before 37 weeks of gestation. The drug is approved in the European Union (marketed as Tractocile by Ferring Pharmaceuticals) but has not been registered by Taiwan's TFDA.

The predicted connection to primary hereditary glaucoma — a genetic disorder in which trabecular meshwork dysfunction leads to impaired aqueous humor outflow, raised intraocular pressure, and progressive optic nerve damage — is not immediately obvious from classical receptor pharmacology. However, oxytocin receptors are expressed in tissues well beyond the uterus, including in trabecular meshwork cells, ciliary body epithelium, and retinal ganglion cells. Emerging preclinical data suggests the oxytocin-vasopressin signaling axis may influence aqueous humor dynamics and intraocular pressure regulation, providing a plausible biological substrate for the model's prediction.

The TxGNN model's high score most likely reflects shared network topology in the biomedical knowledge graph — overlapping signaling nodes between OT/V1A receptor biology and glaucoma-associated pathways — rather than direct empirical evidence. This prediction is best interpreted as a hypothesis-generating signal that warrants dedicated ocular pharmacology investigation before any translational commitment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Primary Hereditary Glaucoma.

---

## Literature Evidence

Currently no related literature available for Primary Hereditary Glaucoma.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note:** Taiwan TFDA SmPC warnings and contraindications are currently unavailable (identified data gap). DDI query returned no interactions. Refer to the EU SmPC for Tractocile (Ferring) for full safety characterization until Taiwan label is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Primary hereditary glaucoma has no supporting clinical or preclinical literature linking it to Atosiban, placing this prediction squarely at Evidence Level L5 (model prediction only). The pharmacological mechanism connecting oxytocin receptor antagonism to hereditary glaucoma pathophysiology remains unvalidated and requires foundational investigation before any forward steps.

**To proceed, the following is needed:**
- Targeted literature review on oxytocin/V1A receptor expression and function in trabecular meshwork and aqueous humor dynamics
- Preclinical validation in cell-based or animal models of hereditary glaucoma using OT receptor modulators
- Obtain Taiwan TFDA SmPC or EU SmPC (Tractocile) to fully characterize warnings, contraindications, and population exclusions
- Retrieve DrugBank MOA data (currently a data gap) to complete mechanistic analysis
- Consider reprioritizing the evaluation pipeline toward the **vascular disease** indication (rank #6), which has 17 associated publications exploring OT receptor biology in cardiac ischemia — these provide substantially more mechanistic context and may represent a more actionable near-term candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

