---
layout: default
title: Etravirine
parent: AI Predictions (L5)
nav_order: 247
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Etravirine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV-1 infection in antiretroviral-treatment-experienced adults and pa…"
monitor_inn: "Etravirine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor", "obsolete familial combined hyperlipidemia"]
---

# Etravirine
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

## Etravirine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Etravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally used to treat HIV-1 infection in treatment-experienced patients.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but **no clinical trials** and **no publications** currently support this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection in antiretroviral-treatment-experienced adults and paediatric patients from 6 years of age (in combination with a boosted protease inhibitor and other antiretrovirals) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, etravirine is an HIV-1 NNRTI, its efficacy in HIV-1 infection in treatment-experienced patients has been established, and mechanistically it may be applicable to other lentiviral infections at the level of class similarity.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV. However, FIV reverse transcriptase is generally less susceptible to NNRTIs, so the link is plausible only on class similarity. The very high TxGNN score appears to reflect network proximity to HIV-related diseases in the knowledge graph, not supporting experimental or clinical data.

Other top-ranked predictions show the same pattern. Simian immunodeficiency virus infection has only one indirect preclinical formulation paper, and SIV and HIV-2 lineages are intrinsically resistant to many NNRTIs. AIDS related complex and congenital HIV largely overlap with the approved HIV-1 indication, so they are not true repurposing. Several other predictions (for example prostate fibroma, Brenner tumor, and a rare neurodevelopmental disorder) have no identifiable mechanistic link and likely reflect knowledge-graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction (feline acquired immunodeficiency syndrome).

For reference, indirectly related publications were found for lower-ranked predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20587860](https://pubmed.ncbi.nlm.nih.gov/20587860/) | 2010 | Cohort/Case series | Antiviral Therapy | Two cases of darunavir and etravirine, with or without raltegravir, used in pregnancy in highly treatment-experienced women (congenital HIV; overlaps with the approved indication) |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | Cohort | AIDS Reviews | Risk factors for gastrointestinal adverse events in HIV treated and untreated patients (AIDS related complex; safety, not efficacy) |
| [27067022](https://pubmed.ncbi.nlm.nih.gov/27067022/) | 2016 | In vitro/Resistance study | AIDS Res Hum Retroviruses | Novel mutations L228I and Y232H cause NNRTI resistance in a combinational pattern (resistance, not efficacy) |
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | Preclinical/Formulation study | Molecular Pharmaceutics | Nanoparticle-based ARV combinations for synergistic inhibition of HIV transmission (SIV infection; indirect) |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000900 (cancelled) | Intelence | Not specified | Intelence, in combination with a boosted protease inhibitor and other antiretroviral medicinal products, is indicated for the treatment of human-immunodeficiency-virus-type-1 (HIV-1)... |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges, not label text): chronic hepatitis C virus infection, hepatitis C virus infection, chronic hepatitis B virus infection, peripheral nervous system disease, and peripheral neuropathy.
- **Drug Interactions**: 100 interactions were identified in the data compiled for this report. Most of those listed are of Moderate severity, with one Minor. Examples include:
  - Acid-suppressing agents: rabeprazole, omeprazole, cimetidine (moderate), ranitidine (minor)
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
  - Antidiabetic agents: pioglitazone, saxagliptin, linagliptin, glimepiride, chlorpropamide
  - Others: clarithromycin, metronidazole, aprepitant, dronabinol, eliglustat, naldemedine, naloxegol

Please refer to the SmPC for complete warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (Evidence Level L5), and its mechanistic basis is weak because FIV and related lentiviruses are generally poorly susceptible to NNRTIs. The very high score likely reflects knowledge-graph proximity to HIV. The one authorization is cancelled, and feline immunodeficiency is a veterinary condition rather than a human therapeutic indication.

**To proceed, the following is needed:**
- In vitro antiviral activity data for etravirine against FIV reverse transcriptase
- Mechanism of action data for etravirine
- Safety information from the current SmPC (warnings and contraindications)
- Clarification of whether a veterinary indication is within the scope of this repurposing programme
- If human repurposing is the goal, review the higher-evidence candidate congenital HIV (L3, observational data in pregnancy). It largely overlaps with the approved indication, and neonatal and infant data are lacking.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

