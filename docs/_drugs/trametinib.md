---
layout: default
title: Trametinib
parent: AI Predictions (L5)
nav_order: 634
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Trametinib: predicted new indication Choroideremia (evidence level L5). Approved use: Unresectable or metastatic BRAF V600-mutant melanoma"
monitor_inn: "Trametinib"
predicted_indications: ["choroideremia"]
---

# Trametinib
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

## Trametinib: From BRAF V600-Mutant Melanoma to Choroideremia
{: .text-alpha }

## One-Sentence Summary

Trametinib is a MEK1/2 inhibitor, originally used for BRAF V600-mutant melanoma (alone or with dabrafenib) and BRAF V600-mutant non-small cell lung cancer.
The TxGNN model predicts it may be effective for **choroideremia**, but **no clinical trials and no publications** currently support this prediction, so it is a computational signal only.
Many of the other top-ranked predictions are melanoma subtypes, where evidence is stronger (see the note below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unresectable or metastatic BRAF V600-mutant melanoma; adjuvant treatment of Stage III BRAF V600-mutant melanoma; advanced BRAF V600-mutant non-small cell lung cancer |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, trametinib is a MEK1/2 inhibitor (pharmacology data lists MAP2K1 and MAP2K2 as targets) that acts downstream of BRAF in the MAPK pathway, and its efficacy in BRAF V600-mutant melanoma is established.

For choroideremia, the link is weak. Choroideremia is an inherited retinal degeneration caused by loss of function of the CHM gene (REP1), and it is not a MAPK-driven disease. The data compiled for this report show no clear reason why MEK inhibition would help. The high score may reflect proximity in the knowledge network rather than a real biological mechanism.

**Note on other predictions:** Most of the other top-ranked predictions are melanoma subtypes, which are mechanistically more plausible when a BRAF V600 mutation is present. The most developed is **non-cutaneous melanoma** (score 99.30%, Evidence Level L2, "Proceed with Guardrails"). Mucosal melanoma has preclinical support (MEK-based combinations, BRAF fusions). Epithelioid cell, eyelid, lentigo maligna, superficial spreading and amelanotic melanoma are supported only by reviews and case reports. Scrotum and balloon cell melanoma have no evidence beyond the prediction. Choroideremia is the top-ranked prediction by score, so it is the focus of this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for choroideremia.

---

## Literature Evidence

Currently no related literature available for choroideremia.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002643 (cancelled) | Mekinist | Not specified | Melanoma (BRAF V600), alone or with dabrafenib; adjuvant Stage III melanoma with dabrafenib; advanced BRAF V600 NSCLC with dabrafenib... |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 17 records were retrieved, of which 15 are drug-drug interactions rated Moderate and 2 are target pharmacology entries (MAP2K1, MAP2K2). Moderate-level interacting drugs include dabrafenib, encorafenib, enzalutamide, apalutamide, brigatinib, erdafitinib, gilteritinib, idelalisib, tucatinib, midostaurin, fostamatinib, elagolix, isavuconazonium, lasmiditan and sarecycline.

For warnings and contraindications, please refer to the SmPC.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The choroideremia prediction rests on a computational score alone. There are no trials or publications, and choroideremia is caused by CHM loss of function rather than MAPK signalling, so a mechanism for MEK inhibition is not apparent. The EU authorization is also cancelled.

**To proceed, the following is needed:**
- A biological rationale linking MEK/MAPK inhibition to choroideremia, tested in preclinical models (for example, retinal pigment epithelium or patient-derived cells)
- Mechanism of action data and safety label information (warnings and contraindications) from the SmPC
- Assessment of ocular safety, since MEK inhibitors can cause retinal toxicity (this should be verified in the SmPC) and the target population already has retinal degeneration
- If the team wants a more actionable direction, consider re-prioritizing the melanoma subtype predictions (especially non-cutaneous melanoma with genotype selection) for further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

