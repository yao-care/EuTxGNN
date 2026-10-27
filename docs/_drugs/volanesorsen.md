---
layout: default
title: Volanesorsen
parent: AI Predictions (L5)
nav_order: 674
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Volanesorsen: predicted new indication Megaloblastic anemia (evidence level L5). Approved use: Adjunct to diet in adult patients with genetically confirmed familial…"
monitor_inn: "Volanesorsen"
predicted_indications: ["megaloblastic anemia (disease)", "sclerosing cholangitis", "sickle cell disease and related diseases", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin E disease syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-hemoglobin c disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "meningococcal infection", "paroxysmal nocturnal hemoglobinuria"]
---

# Volanesorsen
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

## Volanesorsen: From Familial Chylomicronemia Syndrome to Megaloblastic Anemia
{: .text-alpha }

## One-Sentence Summary

Volanesorsen is an antisense oligonucleotide originally used as an add-on to diet in adults with genetically confirmed familial chylomicronemia syndrome (FCS) who are at high risk of pancreatitis.
The TxGNN model predicts it may be effective for **megaloblastic anemia**, but **no clinical trials and no publications** currently support this prediction, and the EU authorization has been cancelled.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adjunct to diet in adult patients with genetically confirmed familial chylomicronemia syndrome (FCS) and at high risk for pancreatitis, in whom response to diet and triglyceride-lowering therapy has been inadequate |
| Predicted New Indication | Megaloblastic anemia |
| TxGNN Prediction Score | 99.997% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Volanesorsen is known to be an antisense oligonucleotide that targets APOC3 mRNA to lower triglycerides. Its efficacy in FCS relates to lipid metabolism.

Megaloblastic anemia results from vitamin B12 or folate deficiency, which impairs DNA synthesis in blood-cell precursors. There is no known link between this process and APOC3 inhibition, and the data compiled for this report supports no mechanistic connection.

The very high TxGNN score (99.997%) is a model output only. It likely reflects knowledge-graph neighborhood patterns rather than biological rationale. It should not be read as evidence of efficacy. Other top-ranked predictions, such as the sickle cell disease variants, show nearly identical scores and also have no supporting evidence. This suggests the scores are correlated, ontology-driven outputs rather than independent signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004538 (cancelled) | Waylivra | Not specified | Adjunct to diet in adult patients with genetically confirmed familial chylomicronemia syndrome (FCS) and at high risk for pan... |

## Cytotoxicity

Not applicable. Volanesorsen is not an antineoplastic drug, so this section is omitted.

## Safety Considerations

- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph lists **thrombocytopenia** as a contraindication-related disease for this drug. This comes from graph data, not from label text. It is particularly relevant if the drug were considered for hematologic conditions.

Please refer to the SmPC for full safety information, including warnings, contraindications and drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score, with no clinical trials, no literature and no plausible mechanistic link between APOC3 knockdown and megaloblastic anemia. In addition, the EU authorization is cancelled and the thrombocytopenia signal is a concern in hematologic patients.

**To proceed, the following is needed:**
- Mechanism-of-action data from DrugBank, to assess any biological connection
- Warnings and contraindications from the EMA product information (SmPC), to enable safety screening
- Any preclinical or clinical evidence linking APOC3 inhibition to megaloblastic anemia
- A review of the thrombocytopenia risk in the target population
- Clarification of the regulatory and supply status, given that the EU authorization is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

