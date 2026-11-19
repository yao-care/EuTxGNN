---
layout: default
title: Bedaquiline
parent: AI Predictions (L5)
nav_order: 85
evidence_level: L5
indication_count: 4
monitor_inn: "Bedaquiline"
predicted_indications: ["vulvovaginal candidiasis", "fascioliasis", "urea cycle disorder", "esophageal candidiasis"]
last_modified_at: 2026-11-20
description: "Bedaquiline: predicted new indication Vulvovaginal candidiasis (evidence level L5). Approved use: Pulmonary tuberculosis due to Mycobacterium tuberculosis resistant to…"
---

# Bedaquiline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Bedaquiline: From Drug-Resistant Pulmonary Tuberculosis to Vulvovaginal Candidiasis
{: .text-alpha }

## One-Sentence Summary

Bedaquiline (marketed as Sirturo) is used as part of a combination regimen for pulmonary tuberculosis caused by Mycobacterium tuberculosis resistant to at least rifampicin and isoniazid. The TxGNN model predicts it may be effective for **vulvovaginal candidiasis**, but **no clinical trials and no publications** in the data compiled for this report support this direction. The prediction is a computational result only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis due to Mycobacterium tuberculosis resistant to at least rifampicin and isoniazid (as part of a combination regimen, adults and children aged 2 to under 18 years weighing at least 7 kg) |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for bedaquiline: "Bedaquiline is a diarylquinoline antimycobacterial drug. […] SIRTURO is a diarylquinoline antimycobacterial drug that inhibits mycobacterial ATP (adenosine 5'- triphosphate) synthase, by binding to subunit c of the enzyme that is essential for the generation of energy in M. tuberculosis." ([DailyMed: Sirturo (bedaquiline fumarate) prescribing information, Janssen Products, LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1534c9ae-4948-4cf4-9f66-222a99db6d0e), label version 2025-10-17; accessed 2026-11-19.) Bedaquiline is generally understood to act by inhibiting the mycobacterial ATP synthase (subunit c), and its efficacy in drug-resistant tuberculosis forms the basis of its EU authorization.

The link to vulvovaginal candidiasis is not supported by the data provided. Fungal ATP synthase differs structurally from the mycobacterial target, and no antifungal activity is documented here. The high TxGNN score (0.9988) should therefore be read as a computational signal that needs independent preclinical confirmation, not as evidence of efficacy.

Other predictions in the list (fascioliasis 0.9988, urea cycle disorder 0.9978, esophageal candidiasis 0.9968) also scored above 0.99 but likewise have no supporting studies and no plausible mechanistic rationale in the data provided.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/002614 | Sirturo | bedaquiline fumarate | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 recorded interactions. Examples of those rated **Major** include:
  - Dexamethasone
  - Clarithromycin
  - Dolasetron
  - Palonosetron
  - Picosulfuric acid
  - Polyethylene glycol (3350 with electrolytes)
  - Sodium sulfate

  Examples rated **Moderate** include acarbose, famotidine, doxycycline, pioglitazone, loperamide, bupropion, minocycline, tetracycline and naltrexone.

Please refer to the SmPC for warnings and contraindications, as no label-based data were available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No clinical trials or publications study vulvovaginal candidiasis with bedaquiline, and no mechanistic link is supported by the available data. Effective antifungal treatments already exist for this condition.

**To proceed, the following is needed:**
- Preclinical data (for example in vitro activity against Candida species) showing a plausible antifungal effect
- Mechanism of action data for bedaquiline and a comparison with fungal targets
- Safety information from the SmPC (warnings, contraindications), with a review of the interaction profile
- Assessment of route of administration and formulation suitability for a vaginal infection

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Sirturo (bedaquiline fumarate) prescribing information, Janssen Products, LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1534c9ae-4948-4cf4-9f66-222a99db6d0e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

