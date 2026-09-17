---
layout: default
title: Sofosbuvir
parent: Medium Evidence (L3-L4)
nav_order: 548
evidence_level: L4
indication_count: 10
---

# Sofosbuvir
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

# Sofosbuvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Sofosbuvir is a nucleotide NS5B RNA-dependent RNA polymerase inhibitor originally developed for hepatitis C virus (HCV) infection. The TxGNN model predicts it may also be effective for **Hepatitis B Virus Infection**, with a very high prediction score, but the supporting evidence consists mainly of trials and literature about HCV/HBV **co-infected** patients rather than direct anti-HBV efficacy — the high score most likely reflects a co-occurrence artifact rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatitis C virus (HCV) infection |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L4 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the structured drug record for this Evidence Pack. Based on the clinical trial and literature evidence collected, Sofosbuvir is well established as a nucleotide analog that inhibits the NS5B RNA-dependent RNA polymerase (RdRp) of hepatitis C virus (HCV), an RNA virus in the Flaviviridae family. This mechanism has been proven highly effective in curing chronic HCV infection.

Hepatitis B virus (HBV), however, is a DNA virus that replicates primarily through a reverse transcriptase, not an RNA-dependent RNA polymerase. There is therefore no direct mechanistic overlap between sofosbuvir's known target and HBV replication. The very high TxGNN score for this prediction is most plausibly explained by a co-occurrence bias in the underlying knowledge graph: many of the clinical trials indexed under this pairing enrolled patients with **HCV/HBV co-infection**, where sofosbuvir was used to treat the HCV component while HBV status was monitored (e.g., for reactivation risk), not treated as the primary target.

For this reason, this candidate should be interpreted with caution. It illustrates a known limitation of graph-based repurposing models — strong co-registration in trial/literature indices can inflate scores even in the absence of a real pharmacological rationale. Rank 2 in the full prediction list (Hepatitis E virus infection) is mechanistically more plausible, since HEV is an RNA virus with in vitro evidence of RdRp inhibition by sofosbuvir, and may warrant separate evaluation.

---

## Clinical Trial Evidence

Of the trials indexed against this prediction, the following are the most directly relevant to hepatitis B (the remainder are HCV-only trials that co-register HBV as a screening/comorbidity variable and were excluded as not relevant):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Open-label study of ledipasvir/sofosbuvir for 12 weeks in patients with HBV monoinfection, evaluating decline in HBsAg and HBV DNA at Week 12; hypothesis based on modest HBsAg reduction observed in HCV/HBV coinfected patients previously treated with LDV/SOF |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of HCV/HBV co-infected patients to determine incidence, morbidity, and predisposing factors for HBV reactivation during direct-acting antiviral treatment of HCV (not an anti-HBV efficacy trial) |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | SOF/VEL regimen combined with prophylactic tenofovir alafenamide (TAF) in HCV/HBV co-infected patients in China, to prevent HBV reactivation during HCV treatment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 open-label | Journal of Medical Virology | Open-label pilot study of ledipasvir/sofosbuvir for 12 weeks in HBV-monoinfected subjects; hypothesis based on modest HBsAg reduction seen in retrospective HCV/HBV coinfection data |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | Cohort follow-up | Clinical Infectious Diseases | LDV/SOF for HCV/HBV co-infected patients in Taiwan; evaluated HBV reactivation during treatment and 108-week posttreatment follow-up (HCV treatment study, HBV monitored as safety outcome) |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case report | Medicine | HBV reactivation after successful HCV treatment with sofosbuvir and ribavirin, with literature review |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohort | Trans R Soc Trop Med Hyg | Sofosbuvir/daclatasvir-based therapy for chronic HCV and HCV/HBV co-infected patients in Egypt (treatment target remains HCV) |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Cohort | Infection and Drug Resistance | Management of HBV reactivation after DAA treatment of HCV in HCV/HBV co-infected patients with pretreatment HBeAg seroconversion |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort | Journal of Clinical Gastroenterology | Risk of HBV reactivation among patients treated with ledipasvir/sofosbuvir for HCV infection |
| [37517414](https://pubmed.ncbi.nlm.nih.gov/37517414/) | 2023 | Modelling study | Lancet Gastroenterology & Hepatology | Global prevalence, cascade of care, and prophylaxis coverage of hepatitis B — background epidemiology, not treatment efficacy data |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Review of antiviral medications for HBV and HCV and their effects on kidney function; HBV and HCV treatments discussed separately (no sofosbuvir anti-HBV mechanism proposed) |
| [25253190](https://pubmed.ncbi.nlm.nih.gov/25253190/) | 2014 | Review | Minerva Pediatrica | Review of hepatitis B and C treatment in children; covers each disease's distinct standard-of-care regimens |

---

## EU Market Information

Sofosbuvir is currently **not marketed** under this Evidence Pack's regulatory dataset (0 recorded authorizations), so no EU marketing authorization table is available. Regulatory status should be verified directly against the EMA product database before any development decision is made.

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score for hepatitis B virus infection is very high, the underlying clinical trial and literature evidence almost entirely derives from HCV/HBV co-infection studies where sofosbuvir was used to treat HCV, not HBV — a classic co-occurrence bias rather than a genuine antiviral signal. Combined with a fundamental mechanistic mismatch (HCV RdRp inhibitor vs. HBV's reverse-transcriptase-dependent replication) and the drug's current unmarketed status in this dataset, this candidate does not currently meet the bar to advance.

**To proceed, the following is needed:**
- Verified mechanism of action (MOA) data for sofosbuvir from DrugBank or the EMA SmPC
- Confirmed EU marketing authorization status (the "not marketed" flag in this pack should be cross-checked against the current EMA database)
- SmPC-sourced safety data (key warnings, contraindications, drug interactions), currently unavailable
- A dedicated pharmacological/virological assessment of whether sofosbuvir or its active metabolite has any direct anti-HBV activity, independent of HCV/HBV coinfection cohorts
- Consideration of the mechanistically stronger hepatitis E virus infection signal (rank 2, L3, in vitro RdRp inhibition demonstrated) as an alternative research question worth separate evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

