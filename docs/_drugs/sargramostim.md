---
layout: default
title: Sargramostim
parent: AI Predictions (L5)
nav_order: 527
evidence_level: L5
indication_count: 10
---

# Sargramostim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Sargramostim: From No EU-Authorized Indication to Drug-Induced Osteoporosis

## One-Sentence Summary

Sargramostim (recombinant GM-CSF, DrugBank DB00020) currently holds **no marketing authorization in the EU**, and no established original indication is recorded in this evidence pack.
The TxGNN model's top-ranked prediction is **Drug-Induced Osteoporosis**, but this association is supported by **0 clinical trials** and **0 publications**, and the accompanying mechanistic review argues the biology may actually run in the opposite direction.
Evidence level is **L5** (model prediction only) with a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no EU marketing authorization on record for this drug |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 98.99% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for sargramostim is not available in this evidence pack. Based on general pharmacology, sargramostim is a recombinant human GM-CSF that stimulates proliferation and differentiation of granulocyte and macrophage precursor cells in the bone marrow, primarily to accelerate neutrophil recovery.

The TxGNN-generated mechanistic rationale for this specific prediction is **not supportive**: GM-CSF's known biology acts on the granulocyte/macrophage lineage and has only an indirect, directionally uncertain relationship to osteoclast differentiation (the RANKL/OPG axis). Some published evidence actually suggests GM-CSF may **promote** osteoclastic bone resorption rather than protect against it — the opposite of what would be needed to treat drug-induced osteoporosis.

Given the absence of a clear mechanistic basis, plus zero supporting clinical trials or literature, this candidate appears to be a low-confidence association generated purely from knowledge-graph embeddings rather than a biologically grounded repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Sargramostim currently has no EU marketing authorization on record (0 licenses). No product, dosage form, or approved indication data is available in this dataset.

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: TFDA-equivalent warnings/contraindications and detailed MOA are flagged as data gaps in this evidence pack — see Next Steps.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for this indication consists of a single TxGNN embedding score with no supporting clinical trials or literature, and the drug's own mechanistic rationale argues against biological plausibility. Additionally, sargramostim is not currently authorized in the EU, so no regulatory or real-world use data exists to cross-validate the hypothesis.

**To proceed, the following is needed:**
- Original indication and mechanism of action (MOA) data for sargramostim (currently flagged as data gaps: DG001, DG002)
- Preclinical or mechanistic studies specifically addressing GM-CSF's effect on osteoclast/osteoblast balance, given conflicting directionality in existing literature
- TFDA/SmPC-equivalent safety labeling (warnings, contraindications) before any S1 safety pre-assessment can proceed
- If pursuing repurposing work on this drug, consider prioritizing the **cervical neuroblastoma** candidate (rank 6) instead — it has an L3 evidence level with two completed clinical trials (including a completed Phase 3 GM-CSF mucositis trial) and a coherent mechanistic link to established GM-CSF/dinutuximab immunotherapy protocols in neuroblastoma.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

