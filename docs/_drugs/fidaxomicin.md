---
layout: default
title: Fidaxomicin
parent: AI Predictions (L5)
nav_order: 260
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
description: "Fidaxomicin: predicted new indication Staphylococcal scalded skin syndrome (evidence level L5). Approved use: Treatment of Clostridioides difficile infections (CDI…"
monitor_inn: "Fidaxomicin"
predicted_indications: ["staphylococcal scalded skin syndrome", "bullous impetigo", "inhalational botulism", "impetigo", "toxin-mediated infectious botulism", "vulvovaginal candidiasis", "hordeolum", "staphylococcus aureus pneumonia", "punctate epithelial keratoconjunctivitis"]
---

# Fidaxomicin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Fidaxomicin: From Clostridioides difficile Infection to Staphylococcal Scalded Skin Syndrome
{: .text-alpha }

## One-Sentence Summary

Fidaxomicin is an oral antibacterial originally used to treat *Clostridioides difficile* infection (CDI).
The TxGNN model predicts it may be effective for **staphylococcal scalded skin syndrome**,
but there are currently **no clinical trials** and **no directly relevant publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of *Clostridioides difficile* infections (CDI, also known as C. difficile-associated diarrhoea) in adults and paediatric patients |
| Predicted New Indication | Staphylococcal scalded skin syndrome |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fidaxomicin is a narrow-spectrum macrocyclic RNA polymerase inhibitor, mainly active against Gram-positive anaerobes such as *C. difficile*. Its efficacy in CDI is established, and it shows some in vitro activity against *Staphylococcus aureus*, the bacterium behind staphylococcal scalded skin syndrome (SSSS).

The link is weak, however. SSSS is a skin disease driven by exfoliative toxins and needs systemic therapy. Oral fidaxomicin is poorly absorbed and stays almost entirely in the gut, so it is unlikely to reach the skin at therapeutic levels. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so it is not a clinically grounded signal.

Other top-ranked predictions are also mostly staphylococcal skin or eye infections (bullous impetigo, impetigo, hordeolum). Several others have no plausible mechanism: inhalational and infectious botulism (toxin-mediated), vulvovaginal candidiasis (fungal), and parasitic skin disease. For *S. aureus* pneumonia, the only literature hit is a general hospital medicine update, not a study of fidaxomicin in this condition. None of these predictions has trial or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no literature directly related to the predicted indication (staphylococcal scalded skin syndrome) is available.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/002087 | Dificlir | fidaxomicin | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 79 interactions were identified in the interaction screening. Examples:
  - **Major**: Vibrio cholerae CVD 103-HgR strain live antigen (live vaccine)
  - **Moderate**: alpelisib, apalutamide, binimetinib, picosulfuric acid
  - **Minor**: nifedipine, amiodarone, clarithromycin, erythromycin, cyclosporine, verapamil, diltiazem, among others

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no clinical trials or relevant publications.

<!-- review:begin eu-lic-20261031-fidaxomicin-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The prediction rests on the model score alone, with no clinical trials or relevant publications. Oral fidaxomicin has minimal systemic absorption, so it is unlikely to reach skin tissue, and the only EU authorization is cancelled." Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-10-31). The EMA data list 1 EU marketing authorisation for this drug, 1 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261031-fidaxomicin-1 -->

**To proceed, the following is needed:**
- Mechanism of action data to support the mechanistic-link analysis
- Warnings and contraindications from the EU product information, so safety screening can proceed
- Preclinical data on fidaxomicin activity against toxin-producing *S. aureus* strains
- Feasibility assessment of a topical or systemic formulation that could reach skin tissue
- Comparison with established treatments for SSSS and related staphylococcal skin infections

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "Oral fidaxomicin has minimal systemic absorption, so it is unlikely to reach skin tissue, and the only EU authorization is cancelled" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

