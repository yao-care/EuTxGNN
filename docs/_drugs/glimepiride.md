---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
---

# Glimepiride
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

# Glimepiride: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Glimepiride is a third-generation sulfonylurea originally developed to treat type 2 diabetes mellitus. The TxGNN model assigns a very high prediction score (**99.75%**) to **Focal Stiff Limb Syndrome** as a potential new indication, but this candidate currently has **zero clinical trials and zero publications** supporting it, and the proposed biological rationale is considered weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (established sulfonylurea use; no formal EU/TW marketing-authorization record on file) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for glimepiride is not available in this evidence pack (flagged as a High-severity data gap — DG002). Based on known pharmacology, glimepiride is part of the sulfonylurea class, and its glucose-lowering efficacy in type 2 diabetes is well established through binding to the SUR1 subunit (ABCC8) of the pancreatic β-cell KATP channel, which triggers insulin release.

Focal Stiff Limb Syndrome, by contrast, belongs to the stiff-person syndrome spectrum, a disease driven by GAD65 autoantibody-mediated autoimmunity and impaired GABAergic neurotransmission in the central nervous system. According to the evidence pack's own rationale, there is **no known biological link** between sulfonylurea-mediated KATP channel closure and GABAergic/autoimmune neurological dysfunction.

The model's high similarity score is therefore assessed as most likely arising from knowledge-graph comorbidity patterns or drug-similarity artifacts rather than a genuine, testable pharmacological mechanism. This candidate should be treated as a low-confidence, exploratory signal rather than a mechanistically grounded hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No marketing authorizations are on file for this jurisdiction — the evidence pack lists 0 licenses and a "Not Marketed" status. This is a Blocking-severity data gap (DG001: TFDA label/warnings and contraindications), which also prevents any Stage 1 safety review for this drug.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no supporting clinical trials or literature (Evidence Level L5, Decision Stage S0), and the proposed mechanistic link to sulfonylurea pharmacology is not biologically plausible — the evidence pack itself flags the prediction as a likely knowledge-graph artifact rather than a genuine signal.

**To proceed, the following is needed:**
- TFDA-approved label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action data from DrugBank (DG002) to properly assess mechanistic plausibility
- Independent preclinical or mechanistic evidence linking sulfonylurea/KATP-channel activity to autoimmune/GABAergic pathology before any further investment

**Note:** Within the same evidence pack, a different candidate for glimepiride — *type 1 diabetes mellitus* (rank 10, score 98.86%) — has materially stronger support (Evidence Level L3, 50 clinical trials, 17 publications, decision stage S1 "Research Question") and may warrant a separate, dedicated evaluation report rather than being pursued under this Hold decision.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

