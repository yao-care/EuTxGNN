---
layout: default
title: Darolutamide
parent: AI Predictions (L5)
nav_order: 174
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
description: "Darolutamide: predicted new indication Homozygous familial hypercholesterolemia (evidence level L5). Approved use: Non-metastatic castration-resistant prostate cancer (nmCRPC) at high…"
monitor_inn: "Darolutamide"
predicted_indications: ["homozygous familial hypercholesterolemia", "multiple endocrine neoplasia", "HIV infectious disease"]
---

# Darolutamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Darolutamide: From Prostate Cancer to Homozygous Familial Hypercholesterolemia
{: .text-alpha }

## One-Sentence Summary

Darolutamide is a non-steroidal androgen receptor antagonist, originally used to treat prostate cancer (nmCRPC and mHSPC).
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**,
but **no clinical trials** and **no publications** currently support this prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-metastatic castration-resistant prostate cancer (nmCRPC) at high risk of metastatic disease; metastatic hormone-sensitive prostate cancer (mHSPC) with androgen deprivation therapy, with or without docetaxel |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 0.9911 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Darolutamide is a non-steroidal androgen receptor antagonist. Detailed mechanism of action data was not available in the data compiled for this report, so this description relies on its known drug class.

Its established use is in androgen-driven prostate cancer. Homozygous familial hypercholesterolemia is a genetic disorder caused by defects in the LDL receptor pathway. No clear mechanistic link between androgen receptor blockade and this disease was identified. The high score appears to be a TxGNN model (deep learning) artifact rather than a biologically grounded prediction, and it is not supported by any trial or publication.

Other top-ranked predictions show the same pattern. They include multiple endocrine neoplasia, HIV, cytomegalovirus infection and several veterinary viral diseases. None has a plausible mechanistic link or direct clinical evidence. Two prostate cancer trials were retrieved for multiple endocrine neoplasia, but they appear to have been matched by keyword and do not test darolutamide in that condition.

## Clinical Trial Evidence

Currently no related clinical trials registered for homozygous familial hypercholesterolemia.

## Literature Evidence

Currently no related literature available.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/004790 | Nubeqa | darolutamide | Valid |

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/hormonal therapy (androgen receptor antagonist), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs. The 20 shown in the compiled data include:
  - **Major**: dexamethasone, eluxadoline, rosuvastatin
  - **Moderate**: clarithromycin, empagliflozin, glyburide, repaglinide, simvastatin, sulfasalazine, rifaximin, cobicistat, deferasirox, eltrombopag, lusutrombopag, among others
  - **Minor**: aprepitant, cimetidine, miconazole
- The rosuvastatin (Major) and simvastatin (Moderate) interactions matter here. Statins are a mainstay of lipid-lowering therapy, which is the setting of the predicted indication.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and no plausible mechanism linking androgen receptor antagonism to LDL receptor pathway defects. The interaction with rosuvastatin adds a further concern in a lipid-lowering setting.

<!-- review:begin eu-lic-20261031-darolutamide-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The interaction with rosuvastatin adds a further concern in a lipid-lowering setting. The only EU authorization is also cancelled." Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-10-31). The EMA data list 1 EU marketing authorisation for this drug, 1 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261031-darolutamide-1 -->

**To proceed, the following is needed:**
- Mechanistic data (MOA) and a plausible biological rationale linking androgen receptor blockade to LDL metabolism
- Preclinical evidence, such as lipid or LDL receptor models
- Warnings and contraindications from the SmPC, with a safety review of interactions with lipid-lowering drugs

<!-- review:begin eu-lic-20261106-darolutamide-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Warnings and contraindications from the SmPC, with a safety review of interactions with lipid-lowering drugs / Clarification of the cancelled EU authorization status" Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-11-06). The EMA data list 1 EU marketing authorisation for this drug, 1 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-darolutamide-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The only EU authorization is also cancelled" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-06 | Removed: "Clarification of the cancelled EU authorization status" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

