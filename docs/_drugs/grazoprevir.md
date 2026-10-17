---
layout: default
title: Grazoprevir
parent: Medium Evidence (L3-L4)
nav_order: 296
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Grazoprevir: predicted new indication HIV infectious disease (evidence level L4). Approved use: Chronic hepatitis C (CHC) in adults and paediatric patients 12 years…"
monitor_inn: "Grazoprevir"
predicted_indications: ["HIV infectious disease", "hepatitis B virus infection", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever", "Kyasanur forest disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Grazoprevir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Grazoprevir: From Chronic Hepatitis C to HIV Infectious Disease

## One-Sentence Summary

Grazoprevir is an HCV NS3/4A protease inhibitor, marketed in combination with elbasvir (Zepatier) for chronic hepatitis C.
The TxGNN model predicts it may be effective for **HIV infectious disease**, but the **10 listed clinical trials** and **20 publications** all concern treating hepatitis C, including in patients co-infected with HIV. None tests anti-HIV activity, so the prediction is not supported by indication-specific evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C (CHC) in adults and paediatric patients 12 years and older weighing at least 30 kg |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on published literature, grazoprevir is an inhibitor of the HCV NS3/4A serine protease and is used with elbasvir, an NS5A inhibitor, as a fixed-dose combination.

The high TxGNN score most likely reflects network proximity to antiviral drugs and HIV-related annotations, not a real mechanistic link. HIV uses a different protease, and grazoprevir has no established direct anti-HIV activity. The trials involving HIV are in HIV/HCV co-infected patients, and their endpoint is HCV cure. This is a population overlap, not a repurposing signal. The co-infection data show that grazoprevir/elbasvir can treat HCV safely and effectively in people with HIV, which is already within the original indication.

Other top-ranked predictions are also weakly supported. For hepatitis B, hepatitis E and hepatitis A, the viruses lack an NS3/4A-type protease. The hepatitis A prediction is linked to 43 trials, but they are HCV trials mapped through the generic term "hepatitis". The flavivirus predictions (Omsk hemorrhagic fever, Kyasanur forest disease) have some theoretical plausibility because their NS2B/NS3 protease is related to HCV NS3, but they remain untested. Kyasanur forest disease has only one in silico study.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02897596](https://clinicaltrials.gov/study/NCT02897596) | Phase 3 | Unknown | 62 | Grazoprevir/elbasvir for 8 or 12 weeks in early chronic HCV (GT1/4) in HIV/HCV co-infected patients; HCV endpoint |
| [NCT02105662](https://clinicaltrials.gov/study/NCT02105662) | Phase 3 | Completed | 218 | Grazoprevir + elbasvir in treatment-naïve HCV (GT1/4/6) patients co-infected with HIV; endpoint SVR12 |
| [NCT02252016](https://clinicaltrials.gov/study/NCT02252016) | Phase 3 | Completed | 159 | Placebo-controlled trial in HCV with inherited blood disorders, with and without HIV co-infection |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Phase 3 | Completed | 80 | Acute HCV GT1/4 in HIV-positive patients (Dutch DAHHS-2 study) |
| [NCT02785666](https://clinicaltrials.gov/study/NCT02785666) | Phase 3 | Completed | 150 | Treat, counsel and cure strategy for HCV in HIV-positive men who have sex with men (Swiss cohort) |
| [NCT03098121](https://clinicaltrials.gov/study/NCT03098121) | Phase 4 | Completed | 40 | Grazoprevir/elbasvir in peginterferon/ribavirin-experienced HCV GT1 with HIV co-infection |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes after HCV eradication in HCV mono-infected and HIV/HCV co-infected individuals |
| [NCT04048850](https://clinicaltrials.gov/study/NCT04048850) | N/A | Completed | 25 | Cohort study of Zepatier in HCV patients with substance use, including HIV co-infection |
| [NCT03407703](https://clinicaltrials.gov/study/NCT03407703) | N/A | Unknown | 50 | Effect of HCV treatment on kidney function in patients with and without HIV |
| [NCT02057003](https://clinicaltrials.gov/study/NCT02057003) | N/A | Unknown | 1000 | Real-life DAA-based regimens for HCV in HIV-coinfected patients (HEPAVIR cohort) |

All listed trials evaluate HCV treatment. None assesses HIV efficacy.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32246857](https://pubmed.ncbi.nlm.nih.gov/32246857/) | 2020 | Systematic review / network meta-analysis | J Gastroenterol Hepatol | Comparative efficacy and safety of DAA regimens in HCV/HIV co-infection |
| [26423374](https://pubmed.ncbi.nlm.nih.gov/26423374/) | 2015 | Non-randomised open-label trial | Lancet HIV | C-EDGE CO-INFECTION: efficacy and safety of grazoprevir plus elbasvir in HCV/HIV co-infection |
| [28417245](https://pubmed.ncbi.nlm.nih.gov/28417245/) | 2017 | Review | Drugs | Elbasvir/grazoprevir in chronic HCV genotypes 1 and 4; high sustained virologic response in phase III trials |
| [27603877](https://pubmed.ncbi.nlm.nih.gov/27603877/) | 2016 | Review | Expert Rev Clin Pharmacol | Mechanism, pharmacokinetics, efficacy and safety of elbasvir/grazoprevir |
| [27091555](https://pubmed.ncbi.nlm.nih.gov/27091555/) | 2016 | Review | Expert Opin Drug Saf | Safety and efficacy of elbasvir and grazoprevir for hepatitis C |
| [28689442](https://pubmed.ncbi.nlm.nih.gov/28689442/) | 2017 | Review | Expert Opin Drug Metab Toxicol | Drug interactions between DAAs and antiretrovirals in HIV-infected patients treated for hepatitis C |
| [30541077](https://pubmed.ncbi.nlm.nih.gov/30541077/) | 2019 | Pharmacokinetic study | J Antimicrob Chemother | Low interaction potential between elbasvir/grazoprevir and the HIV integrase inhibitors raltegravir and dolutegravir |
| [29344726](https://pubmed.ncbi.nlm.nih.gov/29344726/) | 2018 | Integrated analysis | J Gastroenterol | Safety and efficacy in 1070 participants with HCV genotype 1b |
| [30233138](https://pubmed.ncbi.nlm.nih.gov/30233138/) | 2018 | Review | Drug Des Devel Ther | Current evidence on elbasvir/grazoprevir for chronic hepatitis C |
| [37731164](https://pubmed.ncbi.nlm.nih.gov/37731164/) | 2023 | Review | Clin Pharmacokinet | Mechanisms and clinical significance of pharmacokinetic interactions of approved HCV DAAs |

The literature covers HCV treatment and HCV/HIV drug interactions. No publication reports anti-HIV activity of grazoprevir.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004126 | Zepatier | Not specified | Chronic hepatitis C (CHC) in adult and paediatric patients 12 years of age and older who weigh at least 30 kg... (status: cancelled) |

---

## Safety Considerations

- **Drug Interactions**: 53 interactions were recorded in the interaction database. Those graded Major include:
  - clarithromycin
  - dexamethasone
  - eluxadoline
  - obeticholic acid
  - rosuvastatin
  - simvastatin
  - cobicistat
  - eltrombopag
  - artesunate

  Those graded Moderate include:
  - aprepitant
  - cimetidine
  - clotrimazole
  - miconazole
  - troglitazone
  - deferasirox
  - ticagrelor
  - ivacaftor
  - zafirlukast
  - chloramphenicol
  - erythromycin

  Cobicistat, a booster used in some antiretroviral regimens, is a Major interaction, which is relevant for HIV-treated patients. Literature reports a low interaction potential with raltegravir and dolutegravir.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV prediction rests on population overlap, not on activity against HIV. All trials and publications test HCV treatment in HIV/HCV co-infected patients, which is already covered by the original indication. Grazoprevir targets the HCV NS3/4A protease and has no established mechanism against HIV. The EU authorization is also cancelled. The other top predictions (hepatitis B, E, A, animal viral hepatitis, Omsk hemorrhagic fever, Kyasanur forest disease, SIV, feline immunodeficiency, and a rare neurodevelopmental disorder) have no indication-specific supporting evidence either.

**To proceed, the following is needed:**
- Mechanism of action data and in vitro antiviral assays against HIV (and, as a separate research question, against flavivirus NS2B/NS3 proteases)
- Safety information from the SmPC (warnings and contraindications), including the reason for the cancelled EU authorization
- Interaction review with antiretroviral regimens, especially cobicistat-boosted ones
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

