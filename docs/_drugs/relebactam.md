---
layout: default
title: Relebactam
parent: AI Predictions (L5)
nav_order: 497
evidence_level: L5
indication_count: 10
---

# Relebactam
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

Using no additional skill — this is a direct report-generation task per the fully-specified prompt template, not a coding/debugging/brainstorming task.

---

# Relebactam: From Antibacterial Adjunct Therapy to Hyperamylasemia

## One-Sentence Summary

Relebactam is a diazabicyclooctane β-lactamase inhibitor used exclusively as a fixed combination with imipenem/cilastatin (Recarbrio) to restore antibacterial activity against certain resistant gram-negative organisms. The TxGNN model's top prediction points to **Hyperamylasemia**, but this candidate is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags it as likely low-confidence noise due to the absence of any plausible biological mechanism.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antibacterial adjunct (combination with imipenem/cilastatin, as in Recarbrio); no formal approved-indication text on file |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, relebactam is a component of the imipenem/cilastatin/relebactam combination (Recarbrio), where it inhibits class A and C β-lactamases to protect imipenem from enzymatic degradation and restore susceptibility of certain resistant gram-negative pathogens. It has no independent antibacterial activity and is never used as a standalone agent.

There is no established or plausible mechanistic pathway connecting a β-lactamase inhibitor to amylase metabolism or pancreatic/salivary gland function. The evidence pack's own mechanistic rationale explicitly characterizes this top-ranked prediction as biologically implausible ("TxGNN 分數雖高但缺乏生物學合理性，判定為模型雜訊/低可信度預測") — i.e., a high model score without a credible biological basis, most likely statistical noise from the knowledge graph rather than a genuine repurposing signal.

Reviewing the full set of 10 predictions in this pack, all are scored L5 (model prediction only, no supporting trials or literature) and all carry a "Hold" recommendation. Notably, rank 10 (septicemic plague) is the only candidate with an internally noted mechanistic rationale of any substance — theoretical antibacterial activity of imipenem/relebactam against *Yersinia pestis* — though it too lacks any direct clinical or literature support. This further underscores that the current candidate set does not meet the bar for advancement.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## EU Market Information

This drug currently holds no EU marketing authorizations (market status: not marketed; 0 licenses on file).

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or literature support the top-ranked predicted indication, and the mechanistic rationale itself identifies the prediction as likely model noise rather than a genuine signal. Evidence across all 10 ranked candidates in this pack is uniformly L5 with no corroborating data.

**To proceed, the following is needed:**
- TFDA/SmPC warnings and contraindications (currently a **blocking** data gap — required before any S1 safety review)
- Mechanism of action (MOA) detail from DrugBank or the manufacturer (currently a data gap; needed to properly assess mechanistic plausibility)
- Confirmed original approved indication text (imipenem/cilastatin/relebactam combination use is inferred, not sourced from official labeling)
- If reconsidering any candidate from this set, prioritize septicemic plague (rank 10) for a targeted literature/preclinical search given its comparatively stronger — though still unverified — mechanistic rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

