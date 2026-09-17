---
layout: default
title: Eculizumab
parent: AI Predictions (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: From Complement-Mediated Diseases to Cyclic Hematopoiesis

## One-Sentence Summary

Eculizumab is a complement C5 inhibitor whose evidence pack references established use in paroxysmal nocturnal hemoglobinuria (PNH), atypical hemolytic uremic syndrome (aHUS), and generalized myasthenia gravis. The TxGNN model's top prediction is **Cyclic Hematopoiesis**, but this candidate has **0 clinical trials** and **0 publications** supporting it, and the mechanistic review flags it as a likely knowledge-graph artifact rather than a genuine pharmacological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Taiwan regulatory data (no marketing authorization on file); literature in this evidence pack references PNH, atypical HUS, and generalized myasthenia gravis as existing approved uses |
| Predicted New Indication | Cyclic Hematopoiesis |
| TxGNN Prediction Score | 99.97% (rank 595) |
| Evidence Level | L5 |
| EU/TW Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data is marked as a data gap in the formal drug record. However, the evidence pack's own mechanistic annotations consistently describe Eculizumab as a **terminal complement (C5) inhibitor**, consistent with its known role in complement-mediated hemolytic and neuromuscular disorders (PNH, aHUS, generalized myasthenia gravis).

Cyclic hematopoiesis, by contrast, is caused by **ELANE gene mutations** that disrupt neutrophil elastase regulation and the cyclical timing of granulopoiesis — a bone marrow production defect with no established connection to complement activation or terminal complement complex formation.

The rationale text attached to this prediction explicitly states that the high TxGNN score likely reflects **node clustering** in the knowledge graph (neutropenia/bone marrow failure diseases sharing graph proximity to complement-related disease nodes) rather than a real pharmacological relationship. No clinical trial or literature evidence was found to support a mechanistic bridge between C5 inhibition and neutrophil cyclical production defects.

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
The top-ranked prediction (Cyclic Hematopoiesis) has no clinical trial or literature support, and the drug's own evidence annotations identify it as a probable false-positive graph association rather than a mechanistically plausible repurposing candidate. None of the 10 ranked predictions in this evidence pack reach beyond L5 (AI prediction only), and two candidates with retrieved literature (ranks 4 and 10) were reviewed and found to reference only Eculizumab's *existing* approved indications (PNH, aHUS, myasthenia gravis), not the predicted disease itself.

**To proceed, the following is needed:**
- TFDA/EMA label data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- A pharmacology-driven hypothesis connecting complement C5 inhibition to neutrophil cyclical production, if this candidate is to be pursued further
- If no such hypothesis can be established, deprioritize this candidate in favor of predictions with retrievable, disease-specific evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

