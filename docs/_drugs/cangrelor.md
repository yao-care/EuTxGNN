---
layout: default
title: Cangrelor
parent: AI Predictions (L5)
nav_order: 123
evidence_level: L5
indication_count: 10
---

# Cangrelor
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

# Cangrelor: From Reduction of Thrombotic Events in PCI to Hemoglobinopathy

## One-Sentence Summary

Cangrelor (Kengrexal) is an intravenous antiplatelet drug, originally used to reduce thrombotic cardiovascular events in adults with coronary artery disease undergoing percutaneous coronary intervention (PCI).
The TxGNN model's top-ranked prediction is **hemoglobinopathy**, with a high score but **no clinical trials and no publications** supporting it. This is a graph-based prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Reduction of thrombotic cardiovascular events in adults with coronary artery disease undergoing PCI who have not received an oral P2Y12 inhibitor beforehand and for whom oral therapy is not feasible or desirable (given with acetylsalicylic acid) |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 98.44% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Cangrelor is a rapid-onset, quickly reversible intravenous P2Y12 platelet inhibitor. Its efficacy in reducing thrombotic events during PCI is the basis of its original approval.

The link to hemoglobinopathy is speculative. Conditions such as sickle cell disease involve platelet activation and a pro-thrombotic state, so P2Y12 inhibition could in principle reduce thrombotic complications. Nothing in the data compiled for this report supports this idea. The high score most likely reflects proximity in the knowledge graph rather than an established pharmacological relationship.

Several other top-ranked predictions are also red-cell or hematologic disorders. These include beta-thalassemia, pyruvate kinase deficiency, glucophosphate isomerase deficiency–related hemolytic anemia, and hereditary pyropoikilocytosis. None has trials or literature. For thalassemia, an intravenous, short-acting agent is also a poor practical fit for a chronic condition.

The prediction with the most real-world evidence is **myocardial infarction** (rank 2, score 98.03%). It is closely related to the original indication and is better described as an extension within the same disease area than as true repurposing. Its evidence is summarized in the Conclusion.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for hemoglobinopathy.

---

## Literature Evidence

Currently no related literature is available for hemoglobinopathy.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003773 (cancelled) | Kengrexal | Not specified | Kengrexal, co-administered with acetylsalicylic acid (ASA), is indicated for the reduction of thrombotic cardiovascular events in adult patients with coronary artery d... |

---

## Safety Considerations

- **Drug Interactions**: The interaction screening completed with 100 interacting drugs identified. Examples from the listed results:
  - **Major**: abciximab, alteplase, fondaparinux, antithrombin III (human), acalabrutinib, deferasirox, trastuzumab emtansine, ibritumomab tiuxetan, tositumomab. Most of these are bleeding-related concerns.
  - **Moderate**: NSAIDs (ibuprofen, ketorolac, celecoxib, topical diclofenac), fluvoxamine, omega-3 fatty acids, fenfluramine, dexfenfluramine, sibutramine.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hemoglobinopathy prediction is supported only by a graph-based score, with no trials, no literature and no clear mechanistic rationale. The only EU authorization is also cancelled, so regional availability would need to be confirmed first.

**Note on the best-supported prediction (myocardial infarction):**
- Evidence is substantial, and the data compiled for this report would rate it L1 with a "Proceed with Guardrails" recommendation. This reflects a large Phase 3 trial (NCT00305162, n=8,882, terminated), several completed Phase 4 trials in STEMI, the PITRI randomized trial (PMID 38742915) and the DAPT-SHOCK-AMI trial (NCT03551964, n=605).
- Most MI studies measure platelet reactivity or infarct-related surrogate endpoints. Evidence for hard clinical outcomes is less certain.
- Guardrails: bleeding risk, transition to oral P2Y12 inhibitors, and the populations studied (e.g., cardiogenic shock).

**To proceed, the following is needed:**
- Any plausible mechanistic or preclinical evidence linking P2Y12 inhibition to hemoglobinopathy, before further investment
- Mechanism of action data (MOA) from DrugBank
- Warnings and contraindications from the SmPC, which are currently missing
- Confirmation of current EU and regional availability, given the cancelled authorization
- If the goal is a near-term development path, re-prioritizing myocardial infarction as the lead indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

