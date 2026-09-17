---
layout: default
title: Simoctocog Alfa
parent: AI Predictions (L5)
nav_order: 542
evidence_level: L5
indication_count: 10
---

# Simoctocog Alfa
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

# Simoctocog Alfa: From Hemophilia A to Pseudo-von Willebrand Disease

## One-Sentence Summary

Simoctocog alfa is a recombinant, B-domain-deleted Factor VIII (FVIII) product used for the prevention and treatment of bleeding in Hemophilia A. The TxGNN model predicts it may be effective for **Pseudo-von Willebrand Disease**, but this is currently a **model prediction only** — there are **0 clinical trials** and **0 publications** supporting this direction, and the accompanying mechanistic review flags the biological rationale as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia A — bleeding prophylaxis/treatment and surgical hemostasis (no approved-label text available; inferred from evidence-pack rationale, not from regulatory license data) |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 (no clinical trials, no literature) |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on information embedded elsewhere in this pack's own rationale text, simoctocog alfa is a recombinant B-domain-deleted FVIII product approved for Hemophilia A, where it replaces deficient circulating Factor VIII to restore the intrinsic coagulation cascade.

For the top-ranked prediction, however, this mechanism does **not** transfer well. Pseudo-von Willebrand Disease is caused by a gain-of-function defect in the platelet GPIb receptor, which leads to excessive platelet binding and clearance of von Willebrand Factor. The underlying problem is on the **platelet side**, not a deficiency of coagulation factor concentration — supplementing FVIII does not correct this platelet–VWF interaction defect. The evidence pack's own repurposing rationale explicitly notes that the very high TxGNN score for this candidate likely reflects **graph-level proximity of "bleeding disorder" nodes** in the knowledge graph, rather than a genuine pharmacological relationship.

Notably, two lower-ranked candidates in this pack show more plausible mechanistic links and have been advanced to decision stage S1 ("Research Question") rather than held at S0: **acquired coagulation factor deficiency** (rank 5) and **Hemophilia A with vascular abnormality** (rank 9). The latter in particular remains within the FVIII-deficiency disease spectrum and is closer to an indication extension than a true repurposing signal, though it still lacks any supporting trial or literature evidence. These may warrant closer attention than the current rank-1 candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

No EMA marketing authorization is recorded for this product in the current dataset (0 licenses; market status: not marketed).

---

## Safety Considerations

Please refer to the SmPC for safety information. All key warnings, contraindications, and drug-interaction data for this product are currently unavailable in this evidence pack (DG001, flagged Blocking severity — this gap alone prevents progression to the S1 safety review stage).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Pseudo-von Willebrand Disease) has no supporting clinical trials or literature and is accompanied by an internal mechanistic assessment indicating the pharmacology is unlikely to apply. Combined with a blocking safety data gap (no SmPC warnings/contraindications available) and the product's current lack of EU marketing authorization in this dataset, there is insufficient basis to proceed.

**To proceed, the following is needed:**
- TFDA/EMA product label (SmPC) with warnings and contraindications, to close the blocking safety gap (DG001)
- Confirmed mechanism-of-action data via DrugBank API (DG002)
- If pursuing repurposing further, prioritize the mechanistically closer, S1-stage candidates — **acquired coagulation factor deficiency** and **Hemophilia A with vascular abnormality** — over the current rank-1 candidate, and conduct a targeted literature/trial search for FVIII use in acquired hemophilia A (noting that inhibitor-positive patients typically require bypassing agents rather than direct FVIII replacement)
- Confirmation of EU marketing authorization status, since the dataset currently shows 0 licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

