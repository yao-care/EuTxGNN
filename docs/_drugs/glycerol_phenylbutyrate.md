---
layout: default
title: Glycerol Phenylbutyrate
parent: 僅模型預測 (L5)
nav_order: 282
evidence_level: L5
indication_count: 10
---

# Glycerol Phenylbutyrate
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

# Glycerol Phenylbutyrate: From Urea Cycle Disorders to Citrullinemia Type II, Adult-Onset

## One-Sentence Summary

Glycerol phenylbutyrate acts as a nitrogen-scavenging agent, hydrolyzed to phenylbutyrate/phenylacetate which conjugates with glutamine to form phenylacetylglutamine for renal excretion — its established role is chronic ammonia/nitrogen management in **urea cycle disorders (UCDs)**. TxGNN predicts it may also be effective for **Citrullinemia Type II, Adult-Onset (CTLN2)**, a disease with a plausible but not identical mechanistic link to UCDs. Currently **no clinical trials and no literature** support this specific prediction — the evidence rests entirely on the model score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urea cycle disorders (chronic ammonia/nitrogen management) — inferred from mechanistic rationale in the evidence pack; not confirmed by a formal indication label |
| Predicted New Indication | Citrullinemia, Type II, Adult-Onset (CTLN2) |
| TxGNN Prediction Score | 97.13% (rank 22,921) |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, formally sourced MOA data is not available for this drug (flagged as a High-severity data gap). Based on the mechanistic description captured elsewhere in this evidence pack, glycerol phenylbutyrate (GPB) is hydrolyzed to phenylbutyrate/phenylacetate, which conjugates with glutamine to form phenylacetylglutamine and is excreted renally — providing an alternative, urea-cycle-independent route for nitrogen waste disposal. This mechanism is already approved for chronic ammonia/nitrogen management in classic urea cycle disorders.

CTLN2 (adult-onset type II citrullinemia) is caused by citrin deficiency, which secondarily impairs the urea cycle and can trigger hyperammonemic episodes. Directionally, this overlaps with GPB's approved mechanism of action — both involve pathological ammonia accumulation that nitrogen-scavenging therapy could theoretically mitigate.

However, CTLN2's molecular defect (a mitochondrial aspartate-glutamate carrier deficiency) differs from the classic urea cycle enzyme deficiencies GPB is approved for, so the analogy is directional rather than proven. No clinical trials or publications in this dataset test GPB specifically in CTLN2, so this remains a mechanistic hypothesis rather than an evidence-backed indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: retrieval of the TFDA label/warnings for this drug is currently a blocking data gap — see Conclusion.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (CTLN2) has only L5 evidence — a model score with zero supporting clinical trials or literature — and the drug is not currently marketed in Taiwan (0 authorizations).
- Retrieval of TFDA warnings/contraindications is a **Blocking** data gap that prevents any S1 safety screening, so no indication under this candidate can advance regardless of mechanistic plausibility.

**To proceed, the following is needed:**
- TFDA label/SmPC retrieval to resolve the blocking safety data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank or product labeling (DG002)
- Disease-specific (CTLN2) clinical or case-report evidence before advancing past a research-question stage
- Consider prioritizing **hyperammonemic encephalopathy due to carbonic anhydrase VA deficiency** (rank 4) instead — it has a stronger, better-substantiated mechanistic overlap with GPB's approved use, despite a lower TxGNN score
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

