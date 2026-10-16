---
layout: default
title: Belimumab
parent: AI Predictions (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Belimumab: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Add-on therapy for active…"
monitor_inn: "Belimumab"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "severe nonproliferative diabetic retinopathy", "autosomal dominant macrothrombocytopenia", "granulomatous disease, chronic, autosomal recessive, 5", "anus disease", "inflammatory bowel disease", "granulomatous disease with defect in neutrophil chemotaxis"]
---

# Belimumab
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

# Belimumab: From Systemic Lupus Erythematosus to Primary Release Disorder of Platelets

## One-Sentence Summary

Belimumab is a biologic that inhibits B-cell survival signalling. It was originally used as add-on therapy for active systemic lupus erythematosus (SLE) and lupus nephritis.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Add-on therapy for active, autoantibody-positive systemic lupus erythematosus (SLE) in patients aged 5 years and older, and for active lupus nephritis in adults |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (the single authorization is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Belimumab is known to inhibit soluble BLyS/BAFF and reduce B-cell survival, which is the basis of its use in autoantibody-driven SLE.

Primary release disorder of platelets is an intrinsic defect of platelet granule release. It has no established link to B-cell or BAFF-driven processes. The high prediction score therefore appears to be a statistical artefact of the knowledge-graph model rather than a mechanistically grounded signal. No clinical or literature evidence supports it.

Other top-ranked predictions are similar. Pseudo-von Willebrand disease, Glanzmann thrombasthenia, autosomal dominant macrothrombocytopenia and severe nonproliferative diabetic retinopathy have no plausible BAFF-related rationale. Fetal and neonatal alloimmune thrombocytopenia is biologically plausible in principle because it is antibody-mediated. However, there is no clinical data, and the safety of belimumab in pregnancy is not established.

Of the ten predictions, only **inflammatory bowel disease** (score 97.76%, evidence level L4) has any supporting rationale. BAFF is implicated in IBD pathogenesis, and mucosal BAFF expression is elevated. Direct efficacy data for belimumab in IBD are still lacking.

## Clinical Trial Evidence

Currently no related clinical trials are registered for the primary predicted indication.

## Literature Evidence

Currently no related literature is available for the primary predicted indication.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002015 (cancelled) | Benlysta | Not specified | Add-on therapy in patients aged 5 years and older with active, autoantibody-positive systemic lupus erythematosus (SLE) with a high degree of disease activity (e.g., positive anti‑dsDNA and low complement)... |

## Safety Considerations

- **Drug Interactions**: 69 interactions were identified. The listed examples are the major ones:
  - **Major**: adalimumab, baricitinib, certolizumab pegol, and live BCG vaccine (Tice strain).
  - **Moderate** (examples): azathioprine, alemtuzumab, anakinra, canakinumab, roflumilast, and several vaccines.
  - **Minor**: zinc salts.
  - In general, combining belimumab with other immunosuppressants or biologics, or with live vaccines, calls for caution.
- In patients with chronic granulomatous disease, who are already immunocompromised, immunosuppression with belimumab could add infection risk.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication rests on a model score alone. There are no clinical trials or publications, and there is no plausible mechanistic link between BAFF inhibition and a platelet granule release defect. The EU authorization is also cancelled.

**To proceed, the following is needed:**
- Mechanism of action data confirmed from DrugBank
- Warnings and contraindications from the EMA product information (SmPC)
- A mechanistic rationale and preclinical evidence for the platelet disorder predictions
- If the research focus moves to a more plausible candidate, targeted investigation of belimumab in inflammatory bowel disease (currently a research question at L4) or antibody-mediated conditions such as fetal and neonatal alloimmune thrombocytopenia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

