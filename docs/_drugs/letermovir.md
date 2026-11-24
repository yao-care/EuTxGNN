---
layout: default
title: Letermovir
parent: AI Predictions (L5)
nav_order: 363
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Letermovir: predicted new indication Vulvovaginal candidiasis (evidence level L5). Approved use: Prophylaxis of CMV reactivation and disease in CMV-seropositive allog…"
monitor_inn: "Letermovir"
predicted_indications: ["vulvovaginal candidiasis"]
---

# Letermovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Letermovir: From CMV Prophylaxis in Transplant Recipients to Vulvovaginal Candidiasis
{: .text-alpha }

## One-Sentence Summary

Letermovir (Prevymis) is an antiviral originally used to prevent cytomegalovirus (CMV) reactivation and disease in transplant recipients.
The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
The very high score appears to be a TxGNN model (deep learning) artifact of the drug's anti-infective class rather than a real mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prophylaxis of CMV reactivation and disease in CMV-seropositive allogeneic haematopoietic stem cell transplant (HSCT) recipients, and prophylaxis of CMV disease in CMV-seronegative kidney transplant recipients receiving a graft from a CMV-seropositive donor |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for letermovir: "PREVYMIS is an antiviral drug against CMV. […] Letermovir inhibits the CMV DNA terminase complex (pUL51, pUL56, and pUL89) which is required for viral DNA processing and packaging. Biochemical characterization and electron microscopy demonstrated that letermovir affects the production of proper unit length genomes and interferes with virion maturation." ([DailyMed: Prevymis (letermovir) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1b49df80-be4f-47e0-a0b7-123f3e69395b), label version 2026-01-14; accessed 2026-11-19.) Based on known information, letermovir is a CMV-specific antiviral that inhibits the viral terminase complex (pUL56/UL51/UL89), which is needed to cut and package viral DNA.

That target has no known counterpart in fungi. *Candida*, the cause of vulvovaginal candidiasis, is a fungus and does not use a herpesvirus-type terminase. There is therefore no plausible mechanistic link between the original indication and the predicted one. The 0.9988 score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

In short, this prediction should be treated as a model artifact. It should not be treated as a repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for vulvovaginal candidiasis.

---

## Literature Evidence

Currently no related literature available for vulvovaginal candidiasis.

---

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/004536 | Prevymis | Letermovir | Valid |

<!-- licenses:end -->

This authorization is recorded as valid: the drug is marketed in this country, with 1 valid licence out of 1.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction database. The 20 shown here include:
  - **Major**: eliglustat, naloxegol, cisapride
  - **Moderate**: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, pioglitazone, glimepiride, saxagliptin, chlorpropamide, acetohexamide, aprepitant, omeprazole, lansoprazole, clarithromycin, naldemedine, nitisinone

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trials or literature support letermovir for vulvovaginal candidiasis. The drug's target, a viral terminase, is absent in fungi, so the high TxGNN score is not backed by mechanism or evidence.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis for antifungal activity, with in vitro data against *Candida* species
- Mechanism of action data from DrugBank
- Safety information (warnings and contraindications) from the EMA product information

<!-- review:begin eu-lic-20261106-letermovir-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Safety information (warnings and contraindications) from the EMA product information / Clarification of the cancelled EU authorization status" Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-11-06). The current number of EU marketing authorisations for this drug is shown in the Quick Overview and in the table under EU Market Information. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-letermovir-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "Clarification of the cancelled EU authorization status" | Corrected (revised 2026-11-24; earlier version kept in the record) | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Prevymis (letermovir) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1b49df80-be4f-47e0-a0b7-123f3e69395b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

