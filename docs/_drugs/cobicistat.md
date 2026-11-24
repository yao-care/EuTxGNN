---
layout: default
title: Cobicistat
parent: AI Predictions (L5)
nav_order: 155
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
description: "Cobicistat: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: Pharmacokinetic enhancer of atazanavir 300 mg or darunavir 800 mg onc…"
monitor_inn: "Cobicistat"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Cobicistat
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

## Cobicistat: From HIV-1 Infection (Pharmacokinetic Boosting) to Simian Immunodeficiency Virus Infection
{: .text-alpha }

## One-Sentence Summary

Cobicistat is a pharmacokinetic enhancer used with atazanavir or darunavir in antiretroviral therapy for HIV-1 infection.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, but **no clinical trials and no publications** currently support this prediction.
The model score appears to reflect similarity to HIV-1 rather than any real antiviral effect of cobicistat.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharmacokinetic enhancer of atazanavir 300 mg or darunavir 800 mg once daily, as part of antiretroviral combination therapy in HIV-1 infected adults and adolescents aged 12 years and older (weighing at least 35 kg with atazanavir, or at least 40 kg with darunavir) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 6 of 6) |
| Number of Authorizations | 6 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for cobicistat: "Cobicistat is a mechanism-based inhibitor of cytochrome P450 3A (CYP3A). Inhibition of CYP3A-mediated metabolism by cobicistat increases the systemic exposure of CYP3A substrates atazanavir and darunavir." ([DailyMed: Tybost (cobicistat) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3784c35c-e87f-410c-900b-8fd6313c6010), label version 2026-02-10; accessed 2026-11-19.) Based on known information, cobicistat is a CYP3A inhibitor that works as a pharmacokinetic booster. It raises blood levels of co-administered antiretrovirals, but it has no antiviral activity of its own.

The high prediction score most likely reflects the closeness of simian immunodeficiency virus (SIV) infection to HIV-1 in the disease network used by the model. SIV is an animal-model disease with no clinical relevance for human repurposing. A direct effect of cobicistat on SIV is not expected. At most, it could act as a booster of a co-administered antiviral.

Other predictions were also reviewed. One of them, a rare neurodevelopmental disorder (0.9991), comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for simian immunodeficiency virus infection.

For context, the closest HIV-related prediction, AIDS related complex, has one directly relevant study:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02503462](https://clinicaltrials.gov/study/NCT02503462) | Phase 4 | Terminated | 7 | Compared cobicistat vs ritonavir boosting on darunavir brain penetration in HIV-infected individuals. Underpowered because it ended early. |

---

## Literature Evidence

Currently no related literature available for simian immunodeficiency virus infection.

<!-- review:begin eu-lic-20261106-cobicistat-1 -->

> **Review correction (2026-11-24)**: Originally stated: "This authorization is recorded as valid, and the drug is marketed in this country (1 valid licence of 1)." Removed: the number or status of EU marketing authorisations stated here did not match the EMA data (the EMA medicines data as of 2026-11-06). The current number of EU marketing authorisations for this drug is shown in the Quick Overview and in the table under EU Market Information. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-cobicistat-1 -->

---

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/002572 | Tybost | cobicistat | Valid |
| EMEA/H/C/002574 | Stribild | elvitegravir; cobicistat; emtricitabine; tenofovir disoproxil fumarate | Valid |
| EMEA/H/C/002819 | Rezolsta | darunavir; cobicistat | Valid |
| EMEA/H/C/003904 | Evotaz | cobicistat; atazanavir | Valid |
| EMEA/H/C/004042 | Genvoya | elvitegravir; cobicistat; emtricitabine; tenofovir alafenamide | Valid |
| EMEA/H/C/004391 | Symtuza | darunavir; cobicistat; emtricitabine; tenofovir alafenamide | Valid |

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database. Examples among those listed:
  - **Major**: loperamide, triamcinolone, cisapride, budesonide
  - **Moderate**: hydrocortisone, aprepitant, betamethasone, dexamethasone, clarithromycin, repaglinide, metoclopramide, clotrimazole, fenfluramine
  - **Minor**: prucalopride

  These stem from CYP3A inhibition. For example, a case report describes iatrogenic Cushing's syndrome from the interaction of cobicistat with glucocorticoids.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support and no plausible mechanism, since cobicistat has no intrinsic antiviral activity. SIV is also an animal-model disease with no human clinical relevance.

**To proceed, the following is needed:**
- Mechanism of action data
- Warnings and contraindications from the EMA product information
- Any repurposing effort should focus on a clinically meaningful question, such as cobicistat's boosting role in HIV regimens, including CNS exposure and use in HIV/HCV or HIV/HBV co-infection. It should not target SIV.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "This authorization is recorded as valid, and the drug is marketed in this country (1 valid licence of 1)" | Corrected (revised 2026-11-24; earlier version kept in the record) | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tybost (cobicistat) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3784c35c-e87f-410c-900b-8fd6313c6010) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

