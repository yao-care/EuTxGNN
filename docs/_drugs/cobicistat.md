---
layout: default
title: Cobicistat
parent: AI Predictions (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cobicistat: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: Pharmacokinetic enhancer of atazanavir 300 mg or darunavir 800 mg onc…"
monitor_inn: "Cobicistat"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "chronic hepatitis C virus infection", "hepatitis C virus infection", "obsolete familial combined hyperlipidemia", "hepatitis B virus infection", "hepatitis E virus infection"]
---

# Cobicistat
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

# Cobicistat: From HIV-1 Infection (Pharmacokinetic Boosting) to Simian Immunodeficiency Virus Infection

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
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, cobicistat is a CYP3A inhibitor that works as a pharmacokinetic booster. It raises blood levels of co-administered antiretrovirals, but it has no antiviral activity of its own.

The high prediction score most likely reflects the closeness of simian immunodeficiency virus (SIV) infection to HIV-1 in the disease network used by the model. SIV is an animal-model disease with no clinical relevance for human repurposing. A direct effect of cobicistat on SIV is not expected. At most, it could act as a booster of a co-administered antiviral.

Other predictions were also reviewed. Most are explained by cobicistat's use inside HIV combination regimens (hepatitis B, hepatitis C, AIDS related complex), and the benefit in those cases comes from the partner drugs, not from cobicistat. A few appear to be graph artifacts (a rare neurodevelopmental disorder, an obsolete hyperlipidaemia term).

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

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002572 | Tybost | Not specified | Pharmacokinetic enhancer of atazanavir 300 mg once daily or darunavir 800 mg once daily as part of antiretroviral combination therapy in HIV-1... |

This authorization is recorded as cancelled, and no currently valid authorization exists.

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

