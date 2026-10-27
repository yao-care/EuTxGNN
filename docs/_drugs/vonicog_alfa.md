---
layout: default
title: Vonicog Alfa
parent: AI Predictions (L5)
nav_order: 675
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Vonicog Alfa: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Prevention and treatment of haemorrhage or surgical bleeding in adult…"
monitor_inn: "Vonicog Alfa"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency"]
---

# Vonicog Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Vonicog Alfa: From von Willebrand Disease to Primary Release Disorder of Platelets
{: .text-alpha }

## One-Sentence Summary

Vonicog alfa is a recombinant von Willebrand factor (rVWF), originally used to prevent and treat bleeding in adults with von Willebrand disease (VWD).
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. The score is a graph-based prediction only, and the mechanism argues against it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention and treatment of haemorrhage or surgical bleeding in adults (18 years and older) with von Willebrand disease, when desmopressin (DDAVP) alone is ineffective or contraindicated |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, vonicog alfa is recombinant von Willebrand factor, which mediates platelet adhesion and aggregation at sites of vascular injury and carries factor VIII. Its efficacy in VWD is established.

For the top-ranked prediction, the mechanism does not fit well. A platelet release (secretion) defect is an intrinsic problem of platelet granules or signalling, so supplying exogenous VWF would not be expected to correct it. The high TxGNN score reflects proximity in the knowledge graph among bleeding disorders, not clinical evidence.

Other predictions fall into three groups:
- **Mechanistically unlikely (platelet-side defects):** Glanzmann thrombasthenia (GPIIb/IIIa defect; standard care is platelet transfusion and recombinant factor VIIa), Scott syndrome, collagen receptor defects and constitutional thrombocytopenia.
- **Plausible but unproven or risky:** Pseudo-von Willebrand disease (VWF could worsen platelet clumping and clearance), acquired coagulation factor deficiency (only acquired VWF deficiency would be relevant), and hemophilia (VWF stabilises factor VIII, but the label states the drug should not be used for haemophilia A).
- **Likely not separate opportunities:** "Von Willebrand disease, X-linked form" is probably an extension of the existing VWD indication, and "flood factor deficiency" does not correspond to a recognised disorder and may be a data artefact.

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted indication.

## Literature Evidence

The only publications retrieved relate to the rank 4 prediction (hemophilia). They concern VWD, not haemophilia, so they support the existing VWD indication and not repurposing.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35439298](https://pubmed.ncbi.nlm.nih.gov/35439298/) | 2022 | RCT (phase 3) | Blood | Efficacy and safety of rVWF prophylaxis in adults with severe VWD, assessing the frequency of treated spontaneous bleeding events |
| [37332615](https://pubmed.ncbi.nlm.nih.gov/37332615/) | 2023 | PK/PD comparison | Journal of Blood Medicine | Pharmacokinetic and pharmacodynamic comparison of recombinant and plasma-derived VWF in type 3 VWD |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Review | Current Pharmaceutical Design | Narrative review of new haemostatic agents and perioperative anaesthetic considerations |
| [37926687](https://pubmed.ncbi.nlm.nih.gov/37926687/) | 2024 | Laboratory field study/survey | Haemophilia | Survey of how haemostasis laboratories measure rVWF versus plasma-derived VWF products |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004454 (cancelled) | Veyvondi | Not specified | Prevention and treatment of haemorrhage or surgical bleeding in adults (age 18 years and older) with von Willebrand disease (VWD), whe... |

## Safety Considerations

Please refer to the SmPC for safety information. No drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on model scores alone (L5 for the top prediction, L4 for hemophilia), with no supporting trials or literature. For most candidates, the mechanism suggests VWF replacement would not correct the underlying defect. The only authorization is cancelled in the EU.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- Warnings and contraindications from the SmPC or package insert
- Clarification of the reason for the EU authorization cancellation
- Confirmation of whether the VWD-related entries (X-linked form, acquired VWF deficiency) are already covered by the existing indication
- Clinical or preclinical evidence for any candidate before reconsidering, with pseudo-von Willebrand disease and acquired von Willebrand syndrome the most mechanistically plausible to examine first
- Review of whether ontology artefacts such as "flood factor deficiency" should be excluded
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

