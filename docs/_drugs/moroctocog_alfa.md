---
layout: default
title: Moroctocog Alfa
parent: AI Predictions (L5)
nav_order: 417
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Moroctocog Alfa: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Treatment and prophylaxis of bleeding in patients with haemophilia A…"
---

# Moroctocog Alfa
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

# Moroctocog alfa: From Haemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

Moroctocog alfa is a recombinant B-domain-deleted factor VIII, originally used to treat and prevent bleeding in patients with haemophilia A.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**,
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment and prophylaxis of bleeding in patients with haemophilia A (congenital factor VIII deficiency) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, moroctocog alfa is a recombinant B-domain-deleted factor VIII. It replaces the missing FVIII activity in the intrinsic coagulation pathway, which is why it works in haemophilia A.

The predicted disease is a different kind of problem. Primary release disorder of platelets is a defect in platelet granule content or secretion, not a lack of FVIII. Replacing FVIII would not be expected to correct that defect. The high TxGNN score most likely reflects how close these conditions sit to one another in the knowledge graph (all are bleeding disorders), not a real mechanistic rationale.

The other nine predictions show the same pattern. Most involve platelet or vascular defects with normal FVIII levels:

- **Pseudo-von Willebrand disease (99.97%)**: The primary defect lies in the platelets (GP1BA gain-of-function). The product label states that moroctocog alfa contains no von Willebrand factor and is not indicated in von Willebrand disease.
- **Glanzmann thrombasthenia (99.96%)**: This is an integrin αIIbβ3 defect with normal coagulation factors. Established management uses platelet transfusion and recombinant factor VIIa.
- **Acquired coagulation factor deficiency (99.88%)**: This is the most plausible of the predictions, since acquired FVIII deficiency could in principle be treated with FVIII replacement. However, the category is heterogeneous. Acquired haemophilia A is autoantibody-mediated and usually needs bypassing agents and immunosuppression. This is classed as a research question, not a treatment candidate.
- **Scott syndrome, collagen receptor defect bleeding diathesis, constitutional thrombocytopenia**: These are platelet-intrinsic defects with no direct link to FVIII.
- **"Flood factor deficiency"**: The term is ambiguous and may be a nomenclature artifact. It needs to be checked against a standard ontology.
- **Hereditary thrombocytosis with transverse limb defect, familial thrombomodulin anomalies**: The clinical risk may be thrombotic, so giving a procoagulant factor concentrate could be harmful.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000232 (cancelled) | ReFacto AF | Not specified | Treatment and prophylaxis of bleeding in patients with haemophilia A (congenital factor-VIII deficiency). ReFacto AF is appropriate for use in adults and children of all ages, inc... |

## Safety Considerations

Please refer to the SmPC for safety information.

Note from the label: moroctocog alfa contains no von Willebrand factor and is not indicated in von Willebrand's disease.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no clinical or published support (evidence level L5), and the mechanism does not fit. The disease is a platelet secretion defect, whereas the drug replaces FVIII. The only EU authorization is cancelled, and the safety data needed for screening are missing.

**To proceed, the following is needed:**
- Safety information (warnings and contraindications) from the EMA product information, which is currently a blocking gap
- Mechanism of action data from DrugBank
- Evidence that FVIII replacement can correct the platelet secretion defect, such as preclinical or mechanistic studies
- Disambiguation of "flood factor deficiency" against a standard disease ontology
- If any prediction is pursued further, "acquired coagulation factor deficiency" is the most reasonable candidate for a focused research question. It would need a defined patient subgroup, such as acquired FVIII deficiency without inhibitors.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

