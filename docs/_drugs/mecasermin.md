---
layout: default
title: Mecasermin
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
---

# Mecasermin
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

# Mecasermin: From Severe Primary IGF-1 Deficiency to Monosomy X (Turner Syndrome)

## One-Sentence Summary

> Mecasermin (recombinant human IGF-1) was originally developed for severe primary IGF-1 deficiency, a condition characterized by growth hormone insensitivity.
> The TxGNN model predicts it may be effective for **Monosomy X (Turner Syndrome)**,
> but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure AI-model prediction that has not yet been independently verified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe primary IGF-1 deficiency (growth hormone insensitivity, e.g., Laron syndrome) — no formal MOA/indication record in this evidence pack |
| Predicted New Indication | Monosomy X (Turner Syndrome) |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for mecasermin in this evidence pack (flagged as a High-severity data gap). Based on the contextual information embedded in the model's own rationale outputs, mecasermin is a recombinant human IGF-1 analogue, and its established use domain is severe primary IGF-1 deficiency — conditions marked by growth hormone insensitivity at the receptor/signaling level. This mechanistic anchor point is the basis on which TxGNN evaluates related growth-disorder phenotypes.

Monosomy X (Turner syndrome) commonly presents with short stature and a component of partial growth hormone resistance, which provides a plausible physiological rationale for IGF-1 supplementation — this is likely why it received the highest TxGNN score among the 10 candidates in this pack. Notably, a mechanistically *more direct* candidate also appears in this dataset at rank 3 ("growth hormone insensitivity syndrome with immune dysregulation 2"), since GH insensitivity is essentially mecasermin's core approved use-case. However, neither candidate — including the top-ranked Monosomy X — is accompanied by any clinical trial or literature evidence in this pack.

Given the complete absence of supporting clinical or literature evidence, this prediction should be treated as a hypothesis-generating signal only. An independent search for any existing off-label use of IGF-1 in Turner syndrome (a population that already sometimes receives growth hormone therapy) is needed before this candidate can be meaningfully advanced.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## EU Market Information

No EU marketing authorizations are recorded for mecasermin in this evidence pack (market status: **Not marketed**, 0 total licenses). No product/authorization table can be generated at this time.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: key warnings, contraindications, and drug interaction data are currently unavailable in this evidence pack. Retrieval of TFDA/EMA label warnings and contraindications is flagged as a **blocking** data gap for any safety review.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by a TxGNN model score (Evidence Level L5), with zero clinical trials and zero publications identified. In addition, the drug is not currently marketed in the EU, and mechanism-of-action and safety label data are both missing — including a blocking-severity gap on warnings/contraindications. There is insufficient evidence to move beyond model prediction at this stage.

**To proceed, the following is needed:**
- Retrieve TFDA/EMA label warnings and contraindications for mecasermin (blocking gap — required before any safety screening can begin)
- Retrieve formal mechanism-of-action documentation from DrugBank or equivalent source (high-severity gap)
- Conduct an independent literature/registry search for off-label IGF-1 use in Turner syndrome, since this pack contains no such evidence
- Re-evaluate the mechanistically closer candidate (growth hormone insensitivity syndrome, rank 3) in parallel, as it aligns more directly with mecasermin's known pharmacology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

