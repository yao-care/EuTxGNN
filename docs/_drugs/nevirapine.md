---
layout: default
title: Nevirapine
parent: AI Predictions (L5)
nav_order: 428
evidence_level: L5
indication_count: 3
monitor_inn: "Nevirapine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-23
description: "Nevirapine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L4). Approved use: HIV-1 infection (in combination with other antiretroviral medicines)…"
---

# Nevirapine
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

## Nevirapine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally used, in combination with other antiretrovirals, to treat HIV-1 infection.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are **0 clinical trials** and only **1 preclinical publication** directly studying this disease.
This is a veterinary condition, so it falls outside the scope of human drug repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (in combination with other antiretroviral medicines) in adults, adolescents and children |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, nevirapine is an HIV-1 NNRTI that binds directly to the viral reverse transcriptase (RT) and blocks viral DNA synthesis. Its efficacy in HIV-1 infection is established and it is marketed in the EU.

Feline immunodeficiency virus (FIV) is also a lentivirus that depends on a reverse transcriptase, which is the basis for the prediction. However, FIV RT differs structurally from HIV-1 RT, and NNRTIs bind a pocket specific to HIV-1 RT. The one directly relevant study (2023, PMID 38031646) compared nevirapine, efavirenz and rilpivirine against feline and human immunodeficiency virus RT using biochemical and structural methods. Its abstract, as provided, does not state the result, so whether nevirapine actually inhibits FIV RT cannot be concluded here.

The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not clinical validation. A feline disease is also not a human indication, so this prediction has little direct value for human drug repurposing.

Two other predictions were returned. **Simian immunodeficiency virus infection** (score 0.9985) is supported only by indirect, preclinical work. This literature suggests that SIV and HIV-2 are generally poorly inhibited by NNRTIs, while RT-SHIV chimeras carrying HIV-1 RT are sensitive, so nevirapine acts there as a research tool rather than a treatment. A **rare neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter** (score 0.9982) has no trials, no literature and no evident mechanistic link, and should be treated as a model artifact.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Only one publication directly studies the predicted disease:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Preclinical biochemical/structural study | Journal of Veterinary Science | Compares nevirapine, efavirenz and rilpivirine against feline and human immunodeficiency virus RT to assess NNRTI potential for FIV. The abstract provided does not report the outcome. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000183 | Viramune | Not specified (oral suspension, tablets and prolonged-release tablets per indication text) | In combination with other antiretroviral medicines for HIV-1 infected adults, adolescents and children... |

## Safety Considerations

Label warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC for safety information.

**Relations recorded in the knowledge graph (not label text):** the knowledge graph lists nevirapine alongside the following conditions, which suggests caution and should be checked against the SmPC: liver failure, liver disease, drug-induced liver injury, gallbladder disease, chronic hepatitis B and C virus infection, rash (exanthem), Stevens-Johnson syndrome, toxic epidermal necrolysis (Lyell syndrome), rhabdomyolysis, and nodular fasciitis.

**Drug interactions:** 100 interactions were found. The first 20 listed are all of Moderate level. Examples include:
- Rabeprazole
- Bupropion
- Aprepitant
- Clarithromycin
- Dexamethasone
- Prednisolone
- Budesonide
- Ondansetron
- Naltrexone
- Cisapride

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct evidence is a single preclinical structural study, with no clinical trials. FIV RT is structurally different from HIV-1 RT, so nevirapine's activity is uncertain. The indication is also veterinary and outside human drug repurposing. The high TxGNN score alone is not enough to justify advancing.

**To proceed, the following is needed:**
- The full result of the FIV RT study (PMID 38031646) to confirm whether nevirapine inhibits FIV RT
- A decision on whether veterinary indications are in scope for this programme
- Mechanism of action data and SmPC warnings and contraindications for nevirapine
- For human repurposing, a re-run focused on human diseases with a plausible biological link
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

