---
layout: default
title: Andexanet Alfa
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
---

# Andexanet Alfa
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

# Andexanet Alfa: From Factor Xa Inhibitor Reversal to Glanzmann Thrombasthenia

## One-Sentence Summary

Andexanet alfa (Andexxa/Ondexxya) is a catalytically inactive recombinant Factor Xa decoy protein approved in the US and EU for reversing the anticoagulant effects of direct Factor Xa inhibitors (apixaban, rivaroxaban) in patients with life-threatening or uncontrolled bleeding.
The TxGNN model predicts it may be effective for **Glanzmann Thrombasthenia** (rank #1, score 99.77%),
however **no clinical trials and no supporting publications** exist for this combination, and mechanistic analysis indicates this is a knowledge graph false positive driven by bleeding-phenotype disease cluster overlap rather than a true mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Factor Xa inhibitor (apixaban/rivaroxaban) reversal in acute major bleeding (not registered in Taiwan) |
| Predicted New Indication | Glanzmann Thrombasthenia |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved in this evidence pack. Based on established pharmacological knowledge, andexanet alfa is a modified, catalytically inactive form of human Factor Xa produced via recombinant technology. Its sole pharmacological action is to sequester direct Factor Xa inhibitors (anti-Xa DOACs such as apixaban and rivaroxaban) in the bloodstream, acting as a competitive decoy receptor. It has no intrinsic procoagulant activity and does not directly activate the coagulation cascade — it simply removes the inhibitor that was suppressing endogenous Factor Xa.

Glanzmann thrombasthenia (GT) is a rare autosomal recessive bleeding disorder caused by loss-of-function mutations in the *ITGA2B* or *ITGB3* genes encoding the GPIIb/IIIa (integrin αIIbβ3) complex on platelet surfaces. The result is complete inability of platelets to aggregate in response to any agonist. This is a **primary hemostasis defect** — a platelet-level problem occurring upstream of the coagulation cascade. Andexanet alfa's pharmacological target (neutralizing an exogenous anti-Xa molecule) lies entirely within the **secondary hemostasis** (coagulation cascade) compartment and has no interaction with GPIIb/IIIa signaling, platelet aggregation pathways, or integrin expression.

The high TxGNN score (99.77%) most likely originates from knowledge graph topology: both conditions share the same "hemorrhagic disease" disease cluster in the graph, creating spurious co-proximity. There is no hypothesis by which reversing a Factor Xa inhibitor could compensate for structural absence of functional GPIIb/IIIa. This prediction should be flagged as a **graph-topology false positive** and not pursued without a credible mechanistic rationale.

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
Despite a near-perfect TxGNN prediction score, there is a fundamental mechanistic incompatibility between andexanet alfa's Factor Xa inhibitor–neutralization mechanism and the platelet GPIIb/IIIa aggregation defect that defines Glanzmann thrombasthenia; no clinical trial, observational study, or even preclinical model has explored this combination.

**To proceed, the following would be needed:**
- A credible mechanistic hypothesis connecting Factor Xa decoy activity to GPIIb/IIIa function or platelet aggregation (none currently identified)
- Preclinical data in GPIIb/IIIa-deficient animal models or platelet-function assays demonstrating any signal
- Expert hematology consultation to assess biological plausibility before any clinical exploration
- Resolution of Data Gap DG001 (TFDA/SmPC warnings and contraindications) and DG002 (full MOA data from DrugBank) to complete the safety pre-screening required for any clinical trial consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

