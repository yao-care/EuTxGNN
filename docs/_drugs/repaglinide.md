---
layout: default
title: Repaglinide
parent: AI Predictions (L5)
nav_order: 500
evidence_level: L5
indication_count: 10
---

# Repaglinide
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

# Repaglinide: From Type 2 Diabetes to Opsismodysplasia

## One-Sentence Summary

Repaglinide is a meglitinide-class oral insulin secretagogue used to manage type 2 diabetes mellitus by stimulating pancreatic β-cell insulin release via K-ATP channel blockade. The TxGNN model's top prediction links it to **Opsismodysplasia**, a rare skeletal dysplasia, but this association is currently supported by **zero clinical trials** and **zero publications**, and the model's own mechanistic rationale finds no known biological connection between the two conditions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (established pharmacological classification; not present in this evidence pack's regulatory dataset) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 98.77% |
| Evidence Level | L5 |
| EU Market Status | Not Marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (DrugBank MOA field marked as a data gap). Based on the mechanistic notes attached to the predictions, Repaglinide acts as a K-ATP channel blocker on pancreatic β-cells, promoting insulin secretion — the pharmacological basis for its established use in type 2 diabetes.

Opsismodysplasia is a rare autosomal-recessive skeletal dysplasia associated with INPPL1 gene mutations, affecting bone growth and development. There is no established biological pathway connecting insulin secretagogue activity to skeletal chondrocyte or growth-plate biology, and the evidence pack itself states this explicitly.

The pack's own repurposing rationale for this candidate concludes that no known biological association exists between opsismodysplasia and repaglinide's K-ATP channel mechanism, and that the high TxGNN score likely reflects an indirect knowledge-graph node connection rather than genuine pharmacological relevance. This should be treated as a low-confidence, likely spurious prediction rather than a genuine repurposing signal.

For context, among the ten top-ranked candidates in this pack, only rank #4 ("thiamine-responsive dysfunction syndrome" / Rogers syndrome, TRMA) shows a theoretically plausible link, since its diabetes component has been reported to respond to insulin secretagogues in some case reports — though it too currently has no direct clinical or literature evidence for repaglinide specifically.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

No EU marketing authorization is currently recorded for Repaglinide in this evidence pack (market status: Not Marketed; 0 authorizations on file).

## Safety Considerations

Please refer to the SmPC for safety information.

A **Blocking** data gap (TFDA/EMA label warnings and contraindications) has been identified and must be resolved before this candidate can enter Stage 1 (S1) safety pre-assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications for Repaglinide in this evidence pack are rated Evidence Level L5 (model prediction only, no clinical trials or literature), and the top-ranked candidate (Opsismodysplasia) is explicitly flagged by its own mechanistic rationale as lacking any known biological connection to the drug's mechanism. Combined with the absence of EU marketing authorization and a Blocking safety data gap, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- DrugBank mechanism of action (MOA) data for Repaglinide
- TFDA/EMA product label warnings, contraindications, and DDI data (Blocking — required before any S1 safety pre-assessment)
- Independent mechanistic or preclinical validation for any of the ten predicted indications, particularly the comparatively more plausible thiamine-responsive dysfunction syndrome (rank #4)
- Continued literature/clinical trial surveillance, as none of the ten candidates currently have supporting registered trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

