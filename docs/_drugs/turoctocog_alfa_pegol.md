---
layout: default
title: Turoctocog Alfa Pegol
parent: AI Predictions (L5)
nav_order: 646
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Turoctocog Alfa Pegol: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Treatment and prophylaxis of bleeding in patients with haemophilia A…"
---

# Turoctocog Alfa Pegol
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

# Turoctocog alfa pegol: From Haemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Turoctocog alfa pegol (marketed as Esperoct) is a PEGylated recombinant factor VIII, originally used to treat and prevent bleeding in haemophilia A.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment and prophylaxis of bleeding in patients with haemophilia A (congenital factor VIII deficiency). Can be used for all age groups. |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, turoctocog alfa pegol is a PEGylated recombinant factor VIII. It replaces the deficient coagulation factor in haemophilia A, and its efficacy in that condition is the basis of its authorisation.

Primary release disorder of platelets is caused by a functional defect in platelets, not by a lack of factor VIII. Replacing FVIII therefore does not address the underlying problem. The very high TxGNN score (99.997%) most likely reflects the fact that both conditions sit in the same "bleeding disorder" neighbourhood of the knowledge graph, rather than a true mechanistic link.

Other top-ranked predictions show the same pattern. Examples are pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, and collagen receptor defects. These are all platelet or platelet-surface disorders in which FVIII replacement does not correct the defect.

Two candidates deserve separate comment:
- **Acquired coagulation factor deficiency** (score 99.974%) is the most biologically plausible, because FVIII replacement makes sense when the deficiency is specifically of FVIII, as in acquired haemophilia A. However, that condition is usually driven by inhibitory autoantibodies that neutralise human-sequence FVIII, so bypassing agents or porcine FVIII are standard. The term is also broad and covers many other factors.
- **Flood factor deficiency** is an unclear term and may be an ontology artefact. The disease identity should be clarified before any evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004883 (cancelled) | Esperoct | Not specified | Treatment and prophylaxis of bleeding in patients with haemophilia A (congenital factor VIII deficiency). Esperoct can be used for all age groups. |

## Safety Considerations

Please refer to the SmPC for safety information.

No drug-drug interaction records were found, and no contraindication edges were found in the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no clinical trials or literature. The mechanism does not fit a platelet disorder, and the only EU authorisation is cancelled. All ten predicted indications are rated L5 and Hold.

**To proceed, the following is needed:**
- Clarify the market status of Esperoct and confirm the reason the EU authorisation was cancelled
- Obtain the product information (warnings and contraindications) from the EMA website, which is a blocking gap for safety screening
- Obtain mechanism of action data from DrugBank
- Systematic literature and trial searches for FVIII use in the predicted conditions
- If any candidate is pursued, start with acquired coagulation factor deficiency restricted to FVIII-specific deficiency, and clarify the identity of "flood factor deficiency"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

