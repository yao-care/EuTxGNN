---
layout: default
title: Abaloparatide
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Abaloparatide
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

# Abaloparatide: From Osteoporosis to Non-Syndromic Esophageal Malformation

## One-Sentence Summary

Abaloparatide is a synthetic analog of parathyroid hormone-related protein (PTHrP), acting as a PTH1R agonist primarily developed for osteoporosis treatment in postmenopausal women at high fracture risk.
The TxGNN model predicts it may be effective for **Non-Syndromic Esophageal Malformation**,
however, with **0 clinical trials** and **0 publications** currently supporting this direction, evidence remains at the model-prediction level only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoporosis (not registered in Taiwan; known global use) |
| Predicted New Indication | Non-Syndromic Esophageal Malformation |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Abaloparatide (brand name Tymlos) is a synthetic PTHrP analog that selectively activates PTH1R (parathyroid hormone receptor type 1), driving anabolic bone formation. Its proven efficacy in osteoporosis rests on stimulating osteoblast activity and increasing bone mineral density.

The mechanistic rationale proposed for the top predicted indication — non-syndromic esophageal malformation — is that PTHrP is expressed in fetal esophageal smooth muscle during embryonic development, where it regulates smooth muscle relaxation and tissue differentiation. In theory, PTH1R signalling could influence the structural development of the esophagus. However, esophageal malformations are congenital structural defects established during organogenesis; there is no pharmacological intervention window after birth, and the post-natal administration of Abaloparatide cannot correct structural anomalies already present at birth. The high TxGNN score is therefore most likely a false positive arising from PTHrP's broad tissue expression creating spurious knowledge-graph edges.

Among the top 10 predicted indications in this pack, two signals carry more biologically coherent (though still unproven) rationales: **migraine disorder** (rank #5, 98.88%), where PTHrP shares calcitonin superfamily membership with CGRP — a validated migraine target — and **amenorrhea** (rank #3, 99.72%), where PTHrP is a known physiological mediator of lactational amenorrhea via GnRH suppression. Both remain at L5 and would require dedicated preclinical studies before any further development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for any of the 10 predicted indications.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-ranked predicted indication (non-syndromic esophageal malformation) represents a congenital structural defect where pharmacological intervention is mechanistically implausible; all 10 predicted indications carry zero supporting clinical or preclinical evidence, placing the entire candidate set at L5. Without Taiwan regulatory data, basic safety parameters are also unverifiable.

**To proceed, the following is needed:**

- Retrieve MOA data from DrugBank (DB05084) to enable mechanistic plausibility scoring
- Download and parse the Taiwan TFDA SmPC (or US FDA label for Tymlos) to assess warnings, contraindications, and known adverse effects before any repurposing evaluation can advance past S0
- If pursuing the **migraine** signal (rank #5): conduct a focused literature review on PTHrP vs. CGRP receptor selectivity overlap and cross-reactivity studies; confirm whether any PTH1R agonist has shown CGRP-R activity
- If pursuing the **amenorrhea** signal (rank #3): clarify whether the intended use case is induction or suppression of menstruation, as the existing PTHrP–GnRH axis literature supports suppression (lactational amenorrhea), not restoration
- Upgrade at least one indication from L5 to L4 through identification of relevant preclinical or mechanistic publications before re-evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

