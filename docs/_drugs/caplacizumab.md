---
layout: default
title: Caplacizumab
parent: AI Predictions (L5)
nav_order: 126
evidence_level: L5
indication_count: 9
monitor_inn: "Caplacizumab"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "hemophilia", "platelet-type bleeding disorder"]
last_modified_at: 2026-10-27
description: "Caplacizumab: predicted new indication primary release disorder of platelets (evidence level L5). Approved use: Cablivi is indicated for the treatment of adults experiencing an epis…"
---

# Caplacizumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Caplacizumab: anti-von Willebrand factor (vWF) nanobody → primary release disorder of platelets
{: .text-alpha }

## One-Sentence Summary

Caplacizumab is an anti-vWF nanobody that blocks the interaction between vWF and platelets.
The TxGNN model predicts it for **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this direction.
The mechanistic reasoning also argues against it, because blocking platelet adhesion would likely worsen bleeding.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cablivi is indicated for the treatment of adults experiencing an episode of acquired thrombotic thrombocytopenic purpura (aTTP), in conjunction with plasma exchange and immunosuppression. |
| Predicted New Indication | primary release disorder of platelets |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From the known pharmacology, caplacizumab binds the A1 domain of vWF and blocks its binding to the platelet GPIb-IX-V receptor. This stops vWF-driven platelet adhesion and microthrombus formation.

Primary release disorders of platelets are intrinsic defects of platelet granule content or secretion. They are not driven by vWF-mediated adhesion. The model score therefore rests on statistical association alone, and there is no biological support for it.

The mechanism points the other way. Further inhibition of platelet adhesion would be expected to add to the bleeding tendency of a patient who already has a platelet function defect. The score should not be read as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the predicted disease.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004426 | Cablivi | Not recorded | Treatment of adults experiencing an episode of acquired thrombotic thrombocytopenic purpura (aTTP), in conjunction with plasma exchange and immunosuppression. |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 records. Examples of Major-level interactions include acetylsalicylic acid, abciximab, alteplase, fondaparinux, acalabrutinib, anagrelide, deferasirox, trastuzumab emtansine, ibritumomab tiuxetan and tositumomab. Most of these involve antiplatelet, anticoagulant or thrombolytic agents, so additive bleeding risk is the main concern. Moderate-level examples include ibuprofen, ketorolac, celecoxib, fluvoxamine, fenfluramine, dexfenfluramine and sibutramine.
- Bleeding risk is the central concern for this prediction, since caplacizumab inhibits vWF-dependent platelet adhesion and the predicted disease already involves impaired platelet function.

Please also refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials, no publications on this disease, and a mechanism that suggests added bleeding risk rather than benefit. The evidence level is L5.

**To proceed, the following is needed:**
- Preclinical or mechanistic evidence that vWF-GPIb blockade could help in platelet release disorders
- A bleeding-risk assessment for patients with existing platelet function defects
- Complete SmPC warnings and contraindications for caplacizumab
- Detailed mechanism of action data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

