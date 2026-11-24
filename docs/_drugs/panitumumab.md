---
layout: default
title: Panitumumab
parent: AI Predictions (L5)
nav_order: 463
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Panitumumab: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Adult patients with wild-type RAS metastatic colorectal cancer (mCRC)…"
monitor_inn: "Panitumumab"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy"]
---

# Panitumumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Panitumumab: From Metastatic Colorectal Cancer to Drug-Induced Osteoporosis
{: .text-alpha }

## One-Sentence Summary

Panitumumab is an anti-EGFR monoclonal antibody, originally used to treat RAS wild-type metastatic colorectal cancer.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction. The prediction is computational only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adult patients with wild-type RAS metastatic colorectal cancer (mCRC): first-line with FOLFOX or FOLFIRI; second-line with FOLFIRI after first-line fluoropyrimidine-based chemotherapy (excluding irinotecan); or as monotherapy after failure of fluoropyrimidine-, oxaliplatin-, and irinotecan-containing regimens |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 0.9913 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for panitumumab: "The EGFR is a transmembrane glycoprotein that is a member of a subfamily of type I receptor tyrosine kinases, including EGFR, HER2, HER3, and HER4. EGFR is constitutively expressed in normal epithelial tissues, including the skin and hair follicle. […] Panitumumab binds specifically to EGFR on both normal and tumor cells, and competitively inhibits the binding of ligands for EGFR." ([DailyMed: Vectibix (panitumumab) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e0fa4bca-f245-4d92-ae29-b0c630a315c2), label version 2026-06-23; accessed 2026-11-19.) Based on known information, panitumumab is an anti-EGFR (epidermal growth factor receptor) monoclonal antibody. Its efficacy in RAS wild-type metastatic colorectal cancer has been established, which is how it came to be authorized.

The link to drug-induced osteoporosis is speculative. In preclinical settings, EGFR signaling has a role in osteoblast differentiation and bone remodeling, so a theoretical connection exists. However, no clinical or literature evidence was provided to support it, and the relationship between a colorectal cancer therapy and a bone-loss condition has not been characterized. The high TxGNN score (0.9913) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000741 | Vectibix | panitumumab | Valid |

<!-- licenses:end -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR monoclonal antibody) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 27 interactions were identified in total (the 20 listed in the data compiled for this report include the following). Major-level interactions include:
  - **Bevacizumab**
  - **Irinotecan** and **liposomal irinotecan**
  - QT-prolonging or antiarrhythmic agents: **amiodarone, dofetilide, dronedarone, droperidol, levacetylmethadol, arsenic trioxide**
  - **Aminolevulinic acid**
- Moderate-level interactions include proton pump inhibitors (rabeprazole, omeprazole, dexlansoprazole, esomeprazole, lansoprazole, pantoprazole), methoxsalen, topical aminolevulinic acid, disopyramide, and idelalisib.
- **Context from the prediction analysis**: Systemic EGFR blockade is known to carry ocular and dermatologic toxicities, and panitumumab can cause hypomagnesemia and hypocalcemia. These are relevant when considering any new use.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score, with no registered clinical trials and no publications. Mechanism of action, warnings, and contraindications are missing.

<!-- review:begin eu-lic-20261106-panitumumab-2 -->

> **Review correction (2026-11-24)**: Originally stated: "The EU authorization in the data is cancelled, and mechanism of action, warnings, and contraindications are missing." Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-11-06). The current number of EU marketing authorisations for this drug is shown in the Quick Overview and in the table under EU Market Information. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-panitumumab-2 -->

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank)
- Warnings and contraindications from the EMA product information, to allow safety screening
- Preclinical or mechanistic studies of EGFR blockade in bone remodeling and osteoporosis models
- A literature and trial search specific to drug-induced osteoporosis
- A risk-benefit assessment, given systemic EGFR-inhibitor toxicity and the availability of established osteoporosis therapies

<!-- review:begin eu-lic-20261031-panitumumab-1 -->

> **Review correction (2026-11-24)**: Originally stated: "A literature and trial search specific to drug-induced osteoporosis / Verification of the current EU marketing status of Vectibix, since only a cancelled authorization is recorded" Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-10-31). The current number of EU marketing authorisations for this drug is shown in the Quick Overview and in the table under EU Market Information. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261031-panitumumab-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "Verification of the current EU marketing status of Vectibix, since only a cancelled authorization is recorded" | Corrected (revised 2026-11-24; earlier version kept in the record) | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-24 | Removed: "The EU authorization in the data is cancelled, and m" | Corrected (revised 2026-11-24; earlier version kept in the record) | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vectibix (panitumumab) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e0fa4bca-f245-4d92-ae29-b0c630a315c2) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

