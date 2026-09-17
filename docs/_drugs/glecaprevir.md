---
layout: default
title: Glecaprevir
parent: Medium Evidence (L3-L4)
nav_order: 278
evidence_level: L4
indication_count: 10
---

# Glecaprevir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Glecaprevir: From Hepatitis C to HIV Infectious Disease

## One-Sentence Summary

Glecaprevir is an NS3/4A protease inhibitor, originally developed as part of the glecaprevir/pibrentasvir (Mavyret/Maviret) combination for chronic hepatitis C virus (HCV) infection. The TxGNN model predicts it may also be effective for **HIV infectious disease**, with **15 clinical trials** and **20 publications** currently linked to this pairing — but a closer read of that evidence shows it almost entirely describes HCV treatment in HIV/HCV co-infected patients, not a direct antiviral effect against HIV itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus (HCV) infection, genotypes 1–6 (as the glecaprevir/pibrentasvir combination). No formal EMA/TFDA label text is available in this evidence pack — this is inferred from the clinical trial and literature content itself. |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| EU Market Status | ✗ Not marketed (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for glecaprevir is not available in this pack (flagged as a High-severity data gap). Based on the clinical trial and literature content collected, glecaprevir is an NS3/4A serine protease inhibitor, co-formulated with the NS5A inhibitor pibrentasvir, and its efficacy against chronic HCV genotypes 1–6 is well established through a large Phase 3 program (ENDURANCE, EXPEDITION, SURVEYOR, CERTAIN series, etc.).

HCV and HIV are frequently co-transmitted (roughly 25–30% of HIV-positive individuals in Europe and the US are HCV co-infected), so a substantial share of glecaprevir's clinical trial population — and much of the surrounding literature — consists of HIV/HCV co-infected patients (e.g., EXPEDITION-2, MAGELLAN-3, PURGE-C). This shared-population overlap plausibly explains why a knowledge-graph model like TxGNN would place "HIV infectious disease" close to glecaprevir in embedding space.

However, none of the trials or publications in this pack measure an antiviral effect of glecaprevir against HIV itself — the endpoints are uniformly HCV sustained virologic response (SVR), with HIV status treated as a covariate or safety consideration (e.g., drug-drug interactions with antiretrovirals). Glecaprevir's target, the HCV NS3/4A protease, has no structural homology to the HIV protease, reverse transcriptase, or integrase, so there is no known mechanistic basis for direct anti-HIV activity. The most likely explanation is that this is a co-occurrence artifact of the knowledge graph rather than a genuine pharmacological signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) | Phase 3 | Completed | 153 | EXPEDITION-2: efficacy/safety of glecaprevir/pibrentasvir in HCV GT1–6 adults with HIV-1 co-infection (HCV endpoint, not HIV endpoint) |
| [NCT02939989](https://clinicaltrials.gov/study/NCT02939989) | Phase 3 | Completed | 33 | MAGELLAN-3: G/P + sofosbuvir + ribavirin in HCV patients (some HIV/HCV co-infected) with prior virologic failure; endpoint is HCV SVR |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Phase 3 | Completed | 546 | G/P in Asian adults with chronic HCV GT1–6, with or without HIV co-infection; HCV SVR endpoint |
| [NCT04189627](https://clinicaltrials.gov/study/NCT04189627) | N/A (real-world) | Completed | 99 | DETI-2: real-world G/P effectiveness in adolescents with chronic HCV, including HIV/HCV co-infected subgroup |
| [NCT04042740](https://clinicaltrials.gov/study/NCT04042740) | Phase 2 | Completed | 45 | PURGE-C: 4-week G/P fixed-dose combination for acute HCV, with or without HIV-1 co-infection |
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Phase 3 | Completed | 83 | Pilot study of DAA regimens (incl. G/P) for recently acquired HCV, with or without HIV co-infection |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes after HCV eradication in HIV/HCV co-infected vs HIV mono-infected patients |
| [NCT05108935](https://clinicaltrials.gov/study/NCT05108935) | N/A | Completed | 17 | Telemedicine program combining HIV PrEP, MOUD, and hepatitis C treatment at syringe service sites — not a G/P-HIV efficacy trial |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Phase 1/2 | Not yet recruiting | 30 | PK and safety of G/P initiated in pregnancy in women with HCV, with or without HIV |
| [NCT03235349](https://clinicaltrials.gov/study/NCT03235349) | Phase 3 | Completed | 160 | G/P in Asian adults with HCV GT1–6 and compensated cirrhosis, with or without HIV co-infection |

*Note: all trials above use HCV virologic response as the primary endpoint. None report an HIV-specific efficacy outcome for glecaprevir.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39697370](https://pubmed.ncbi.nlm.nih.gov/39697370/) | 2024 | Cohort | Clinical and experimental hepatology | Real-life efficacy/safety of G/P in HIV/HCV-positive patients treated with bictegravir/emtricitabine/tenofovir alafenamide |
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | Cohort | J Antimicrob Chemother | Response to G/P in HIV/HCV-coinfected patients in real-world clinical practice |
| [31284039](https://pubmed.ncbi.nlm.nih.gov/31284039/) | 2019 | Systematic Review/Meta-analysis | Int J Antimicrob Agents | Pooled SVR12 of 97.8% for G/P across HCV GT1–6 (13 studies, 3082 patients) |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | Review | Expert Opin Pharmacother | Protease inhibitor therapy for HCV; notes ~25–30% HIV co-infection rate in treated populations |
| [30671330](https://pubmed.ncbi.nlm.nih.gov/30671330/) | 2017 | Review | GMS Infectious Diseases | Overview of HCV protease inhibitors, including use in HIV co-infected populations |
| [31537106](https://pubmed.ncbi.nlm.nih.gov/31537106/) | 2020 | Review | The Annals of Pharmacotherapy | Pharmacology/efficacy/safety review of G/P as an 8-week pangenotypic HCV regimen |
| [30499343](https://pubmed.ncbi.nlm.nih.gov/30499343/) | 2019 | Review | Future Microbiology | Overview of G/P for treatment of chronic HCV infection |
| [35877601](https://pubmed.ncbi.nlm.nih.gov/35877601/) | 2022 | Review | PLoS One | Comparative analysis of drug approval evidence for TB, HIV, and HCV — contextual, not a G/P-HIV efficacy study |
| [34664197](https://pubmed.ncbi.nlm.nih.gov/34664197/) | 2021 | Case Report | Clinical Journal of Gastroenterology | Successful G/P treatment of a hemophilia patient co-infected with HIV and HCV genotype 4a |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference Report | AIDS Reviews | Report from the 2017 International Conference on Viral Hepatitis, covering HCV/HIV treatment landscape |

## EU Market Information

Glecaprevir currently has no EU marketing authorization on record in this pack — market status is **Not marketed (Not Marketed)** with **0 licenses**. No product name, dosage form, or approved indication text is available to tabulate.

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug-drug interaction data are not available in this evidence pack — DDI lookup returned no results, and TFDA label warnings/contraindications are recorded as a Blocking-severity data gap.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All 15 clinical trials and the majority of the 20 publications describe glecaprevir/pibrentasvir treating HCV in HIV/HCV co-infected patients — none measure a direct antiviral effect against HIV, and there is no structural or mechanistic basis (NS3/4A protease vs. HIV protease/reverse transcriptase/integrase) for cross-activity. The evidence strongly suggests the TxGNN score reflects a co-occurrence artifact rather than a real pharmacological signal.

**To proceed, the following is needed:**
- Confirmed mechanism-of-action data for glecaprevir (currently a data gap)
- TFDA/EMA label warnings and contraindications (currently a Blocking data gap)
- Any in vitro or preclinical evidence of direct anti-HIV activity, if it exists, to distinguish a real signal from a knowledge-graph artifact
- Drug-drug interaction data, particularly against antiretroviral regimens, before any further safety evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

