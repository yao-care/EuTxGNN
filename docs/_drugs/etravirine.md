---
layout: default
title: Etravirine
parent: AI Predictions (L5)
nav_order: 247
evidence_level: L5
indication_count: 8
monitor_inn: "Etravirine"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-10-23
description: "Etravirine: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: HIV-1 infection in antiretroviral-treatment-experienced adults and pa…"
---

# Etravirine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Etravirine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection
{: .text-alpha }

## One-Sentence Summary

Etravirine is an antiretroviral medicine authorized in the EU for treating HIV-1 infection in treatment-experienced patients.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, but the data compiled for this report contain **0 clinical trials** and only **1 indirect publication** (a preclinical study of nanoparticle-based antiretroviral combinations for HIV).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection in antiretroviral-treatment-experienced adults and paediatric patients from 6 years of age (in combination with a boosted protease inhibitor and other antiretrovirals) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Etravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI). Detailed mechanism-of-action data are not available in the compiled data, so this class assignment comes from general knowledge of the drug. It is used against HIV-1 in treatment-experienced patients.

Simian immunodeficiency virus (SIV) is a lentivirus closely related to HIV, which explains why a network-based model would place the two diseases close together. However, SIV (like HIV-2) is generally intrinsically less susceptible to NNRTIs, so the mechanistic link is plausible but uncertain. SIV infection is also mainly relevant as a preclinical animal model rather than as a human indication.

The single retrieved publication studies nanoparticle-based antiretroviral combinations against HIV. It does not study SIV directly, so it is indirect evidence. No cited study directly addresses SIV infection, which caps the evidence level at L5 (model prediction only). The other seven predictions (feline acquired immunodeficiency syndrome, a neurodevelopmental disorder, several benign tumours and an obsolete lipid disorder term) have no trials or literature and no identified mechanistic link. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | Preclinical in vitro study | Molecular Pharmaceutics | Nanoparticle-based antiretroviral drug combinations studied for synergistic inhibition of cell-free and cell-to-cell HIV transmission; indirect evidence, does not address SIV |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000900 | Intelence | Not specified | Intelence, in combination with a boosted protease inhibitor and other antiretroviral medicinal products, is indicated for the treatment of human-immunodeficiency-virus-type-1 (HIV-1)... |

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: The knowledge graph records contraindication relations with chronic hepatitis C virus infection, hepatitis C virus infection, chronic hepatitis B virus infection, peripheral nervous system disease and peripheral neuropathy. These are not taken from the product label and should be checked against the SmPC.
- **Drug Interactions**: The interaction query returned 100 records; the 20 listed are mostly Moderate, with one Minor (ranitidine). Examples of moderate interactions include:
  - Acid-suppressing agents: omeprazole, rabeprazole, cimetidine
  - Corticosteroids: dexamethasone, betamethasone, hydrocortisone, triamcinolone
  - Antidiabetic agents: pioglitazone, saxagliptin, linagliptin, glimepiride, chlorpropamide
  - Others: clarithromycin, metronidazole, aprepitant, eliglustat, dronabinol, naloxegol, naldemedine

Please refer to the SmPC for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score alone. No trial or publication directly studies SIV infection, SIV is intrinsically less susceptible to NNRTIs, and SIV is mainly an animal-model disease rather than a human indication.

**To proceed, the following is needed:**
- Direct preclinical data on etravirine activity against SIV reverse transcriptase or in SIV infection models
- Mechanism-of-action data for etravirine
- Label warnings and contraindications from the SmPC for safety screening
- Clarification of whether a veterinary or animal-model use, rather than a human indication, is the intended goal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

