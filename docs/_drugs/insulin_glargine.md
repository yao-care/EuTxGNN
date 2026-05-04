---
layout: default
title: Insulin Glargine
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Insulin Glargine
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

# Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin glargine is a long-acting basal insulin analog, internationally established for the management of Type 1 and Type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **Autoimmune Oophoritis**, with **0 clinical trials** and **0 publications** currently supporting this direction.
At this stage, the prediction rests entirely on AI model inference from the underlying biomedical knowledge graph, with no independent clinical evidence to corroborate it.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diabetes Mellitus (Type 1 and Type 2) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed (0 authorizations) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, insulin glargine is a recombinant long-acting insulin analog that differs from human insulin by two amino acid substitutions (Arg-Arg at B-chain C-terminus) and replacement of Asn with Gly at A21. These modifications shift its isoelectric point, causing micro-precipitation at the subcutaneous injection site and enabling a slow, peakless release that approximates physiological basal insulin secretion.

Ovarian cells express functional insulin receptors, and insulin signaling — via the IR/IRS-1/PI3K/Akt axis — plays a recognized role in follicular development, oocyte maturation, and gonadal steroidogenesis. This biological overlap between insulin's metabolic targets and ovarian physiology provides the conceptual bridge that the TxGNN model is likely exploiting.

However, the core pathology of autoimmune oophoritis is immune-mediated destruction of ovarian tissue, driven by autoantibodies (notably anti-steroidogenic cell antibodies) and dysregulated T-cell responses — a mechanism entirely outside insulin glargine's established pharmacological footprint. Insulin glargine has no known immunomodulatory targets. The high TxGNN score most plausibly reflects the broad connectivity of insulin-related metabolic nodes within the knowledge graph, rather than a direct pathophysiologically relevant pathway. This prediction should be interpreted with considerable caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Insulin glargine currently holds no Taiwan Food and Drug Administration (TFDA) marketing authorization. No registered products, approved indications, or dosage form data were found in the Taiwan regulatory database at the time of data collection (2026-04-20).

> **Note:** This finding may reflect a data collection gap rather than a true absence from the Taiwan market. Insulin glargine (e.g., Lantus®, Toujeo®) is approved in numerous major jurisdictions globally. TFDA SmPC verification is recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the SmPC for safety information.

> Safety data (key warnings, contraindications, drug-drug interactions) were not available in this Evidence Pack. Retrieval from the TFDA official website or equivalent regulatory source is listed as a **Blocking** data gap requiring resolution before any safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.88%), the mechanistic link between insulin glargine and autoimmune oophoritis is tenuous — the disease is driven by autoimmune tissue destruction, a process that insulin has no established ability to modulate. With zero supporting clinical trials or publications, this prediction does not currently meet the minimum evidence threshold for further investment.

**To proceed, the following is needed:**

- **Resolve Blocking data gap:** Obtain TFDA SmPC (or EMA/FDA equivalent) to complete safety screening (warnings, contraindications, interactions)
- **Resolve MOA data gap:** Confirm insulin glargine's full pharmacological profile via DrugBank API to enable mechanistic linkage analysis
- **Mechanistic validation:** Identify whether insulin receptor signaling in ovarian immune cells has any documented effect on autoimmune cascades (e.g., regulatory T-cell modulation, cytokine suppression)
- **Broader prediction review:** Note that rank 6 prediction — **Pancreatic Agenesis** (score 99.43%, L4 evidence, 6 publications) — has a substantially more direct mechanistic rationale (absolute insulin deficiency requiring exogenous replacement) and may warrant prioritization over this rank-1 prediction for near-term follow-up
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

