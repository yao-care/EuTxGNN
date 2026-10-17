---
layout: default
title: Romiplostim
parent: AI Predictions (L5)
nav_order: 535
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Romiplostim: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Primary immune thrombocytopenia (ITP) in adults refractory to other t…"
monitor_inn: "Romiplostim"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "platelet-type bleeding disorder", "autosomal dominant macrothrombocytopenia", "Ehlers-Danlos syndrome, fibronectinemic type"]
---

# Romiplostim
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

# Romiplostim: From Immune Thrombocytopenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Romiplostim (Nplate) is a thrombopoietin receptor agonist, originally used to treat primary immune thrombocytopenia (ITP) in patients who do not respond to other treatments.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but there are **0 clinical trials** and only **1 publication**, a mechanistic ITP study that does not directly support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary immune thrombocytopenia (ITP) in adults refractory to other treatments (e.g. corticosteroids, immunoglobulins); chronic primary ITP in children aged 1 year and older refractory to other treatments |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available in the data compiled for this report. From pharmacology data, romiplostim is a peptide agonist of the thrombopoietin receptor (MPL). It stimulates megakaryocyte proliferation and platelet production, which is why it works in ITP, where platelet counts are low.

The link to the predicted indication is weak. Platelet release disorders involve impaired platelet function (secretion defects), not a low platelet count, so raising platelet numbers is unlikely to correct the defect. The only supporting paper concerns ITP autoantibodies that inhibit proplatelet formation. That is the already-approved indication, not a release disorder. The very high TxGNN score most likely reflects network proximity to ITP and platelet biology rather than direct evidence.

Other top-ranked predictions show the same pattern. Pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, and collagen receptor defects are mostly functional platelet disorders with normal or near-normal counts. Of the ten predictions, only fetal and neonatal alloimmune thrombocytopenia (FNAIT, rank 4) has a plausible mechanistic link, because it is an immune-mediated thrombocytopenia related to ITP. It has indirect literature support (evidence level L4, "Research Question") but no direct FNAIT trial data. Some inherited thrombocytopenias may also respond to MPL agonism, depending on the specific genetic defect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Basic/mechanistic study | Haematologica | Serum and IgG autoantibodies from ITP patients inhibit proplatelet formation by megakaryocytes and impair platelet production in vitro. This concerns ITP, not a release disorder. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000942 (cancelled) | Nplate | Not specified | Adults: primary immune thrombocytopenia (ITP) in patients refractory to other treatments (e.g. corticosteroids, immunoglobulins). Paediatrics: chronic primary ITP in patients aged 1 year and older refractory... |

## Safety Considerations

- **Drug Interactions**: A **Major**-level interaction with carfilzomib is recorded. The pharmacology data also confirms the thrombopoietin receptor (MPL) as the drug's target.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only (L5). There are no registered trials, the single publication does not address platelet release disorders, and the mechanism (raising platelet count) does not match a functional platelet defect. The EU authorization is also cancelled.

**To proceed, the following is needed:**
- Mechanistic evidence that increasing platelet number benefits platelet release disorders
- Retrieval and review of the SmPC warnings and contraindications
- Clarification of the EU authorization status (cancelled)
- Consideration of reprioritizing FNAIT, which has the most plausible mechanistic link, and subtype-specific inherited thrombocytopenias, with placental transfer, fetal safety, and neonatal dosing assessed first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

