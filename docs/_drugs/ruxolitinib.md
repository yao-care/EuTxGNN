---
layout: default
title: Ruxolitinib
parent: AI Predictions (L5)
nav_order: 542
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Ruxolitinib: predicted new indication Uterine corpus perivascular epithelioid cell tumor (evidence level L5). Approved use: Myelofibrosis (disease-related splenomegaly or symptoms)…"
monitor_inn: "Ruxolitinib"
predicted_indications: ["uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lymphangioleiomyomatosis", "liposarcoma", "familial rhabdoid tumor", "lung PEComa", "ovarian myxoid liposarcoma", "hemophagocytic syndrome associated with an infection", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease"]
---

# Ruxolitinib
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

## Ruxolitinib: From Myelofibrosis to Uterine Corpus Perivascular Epithelioid Cell Tumor
{: .text-alpha }

## One-Sentence Summary

Ruxolitinib was originally authorised in the EU for myelofibrosis, polycythaemia vera and graft versus host disease (as Jakavi), and for vitiligo (as the topical product Opzelura).
The TxGNN model predicts it may be effective for **uterine corpus perivascular epithelioid cell tumor (PEComa)**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myelofibrosis (disease-related splenomegaly or symptoms), polycythaemia vera, and acute and chronic graft versus host disease |
| Predicted New Indication | Uterine corpus perivascular epithelioid cell tumor |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 3 of 3) |
| Number of Authorizations | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ruxolitinib: "Ruxolitinib, a kinase inhibitor, inhibits Janus Associated Kinases (JAKs), JAK1 and JAK2, which mediate the signaling of a number of cytokines and growth factors that are important for hematopoiesis and immune function. JAK signaling involves recruitment of STATs (signal transducers and activators of transcription) to cytokine receptors, activation, and subsequent localization of STATs to the nucleus leading to modulation of gene expression." ([DailyMed: Jakafi (ruxolitinib) prescribing information, Incyte Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f1c82580-87ae-11e0-bc84-0002a5d5c51b), label version 2026-07-20; accessed 2026-11-19.) Ruxolitinib is known as a JAK1/2 inhibitor. Its efficacy in myelofibrosis, polycythaemia vera and graft versus host disease is established, and it works by dampening JAK/STAT-driven signalling.

The link to uterine PEComa is weak. PEComa biology is usually driven by mTOR pathway dysregulation (TSC1/TSC2), not JAK/STAT signalling. The high score of 0.9973 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related PEComa-family diseases, not biological evidence. No trials or publications were found to support a rationale for JAK1/2 inhibition in this tumour.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/002464 | Jakavi | ruxolitinib phosphate | Valid |
| EMEA/H/C/005843 | Opzelura | ruxolitinib | Valid |
| EMEA/H/C/006618 | Ruxolitinib Viatris | ruxolitinib hemifumarate | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 100 interactions are recorded in total. The data reviewed for this report list the following main ones:
  - **Major**: clarithromycin, cobicistat, deferasirox, deferiprone, ibritumomab tiuxetan, tositumomab (including I-131 tositumomab), samarium (153Sm) lexidronam
  - **Moderate**: dexamethasone, rosuvastatin, fenfluramine, dexfenfluramine, sibutramine, troglitazone, palifermin, strontium chloride Sr-89

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a TxGNN model (deep learning) score alone, with no trials, no literature, and a mechanism (mTOR-driven PEComa) that does not point to JAK inhibition.

<!-- review:begin eu-lic-20261106-ruxolitinib-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The prediction rests on a TxGNN model (deep learning) score alone, with no trials, no literature, and a mechanism (mTOR-driven PEComa) that does not point to JAK inhibition. Both EU authorisations are currently valid." Removed: the number or status of EU marketing authorisations stated here did not match the EMA data (the EMA medicines data as of 2026-11-06). The current number of EU marketing authorisations for this drug is shown in the Quick Overview and in the table under EU Market Information. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-ruxolitinib-1 -->

**To proceed, the following is needed:**
- Preclinical evidence of JAK/STAT involvement in PEComa, or any clinical report of ruxolitinib use in this tumour
- Mechanism of action data and SmPC warnings and contraindications
- Comparison against the established mTOR-inhibitor approach (e.g., sirolimus) used in related TSC/mTOR-driven diseases

**Alternative candidates:** Among the other predictions for this drug, hemophagocytic syndrome associated with an infection (rank 10) has by far the strongest support (Evidence Level L3). It has murine mechanistic data and several small clinical series and cohorts of ruxolitinib in HLH, including a pediatric response-based stratified treatment study (PMID 35344583). It has no registered trials or RCTs, but it is a more promising research question than uterine PEComa.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "Both EU authorisations are currently valid" | Corrected (revised 2026-11-24; earlier version kept in the record) | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Jakafi (ruxolitinib) prescribing information, Incyte Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f1c82580-87ae-11e0-bc84-0002a5d5c51b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

