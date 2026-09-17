---
layout: default
title: Velpatasvir
parent: Medium Evidence (L3-L4)
nav_order: 637
evidence_level: L4
indication_count: 10
---

# Velpatasvir
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

# Velpatasvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

Velpatasvir is an NS5A inhibitor used clinically as part of the sofosbuvir/velpatasvir fixed-dose combination for chronic hepatitis C virus (HCV) infection. The TxGNN model predicts it may also be effective for **Hepatitis B Virus Infection**, but the supporting evidence body — **25 clinical trials** and **20 publications** — is almost entirely composed of HCV-focused studies rather than genuine HBV efficacy data, so this prediction currently sits at evidence level **L4** with a **Hold** recommendation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus (HCV) infection (as a component of the sofosbuvir/velpatasvir combination; inferred from the trial/literature evidence in this pack, as no EU marketing authorization record exists for velpatasvir as a standalone product) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| EU Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not recorded at the drug level in this Evidence Pack (flagged as a High-severity data gap, DG002). However, the evidence collected for this candidate consistently describes velpatasvir as an HCV-specific NS5A inhibitor, acting on the NS5A protein within the HCV replication complex. This is the accepted mechanism behind its approved use (as the "VEL" component of sofosbuvir/velpatasvir, marketed as Epclusa) for chronic hepatitis C.

Hepatitis B virus, in contrast, is a partially double-stranded DNA virus that replicates via reverse transcriptase and does not possess an NS5A-homologous protein. There is therefore no direct structural or functional target shared between HCV and HBV that would explain cross-activity of an NS5A inhibitor. Reviewing the clinical trial and literature evidence collected for this pairing confirms this: the overwhelming majority of trials and articles are studies of sofosbuvir/velpatasvir (or related regimens) treating HCV — including in patients who happen to be HBV co-infected — rather than studies evaluating velpatasvir's antiviral activity against HBV itself.

The one literature record that directly discusses HBV (PMID 31542053, a case report) actually describes HBV **reactivation** occurring during HCV treatment with sofosbuvir/velpatasvir, which is a safety signal, not evidence of therapeutic benefit against HBV. This pattern — where a drug frequently used in HCV/HBV co-infected populations gets flagged by knowledge-graph models as a candidate for HBV itself — is a known artifact of shared clinical contexts rather than a genuine mechanistic signal, and should be interpreted with caution.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03250910](https://clinicaltrials.gov/study/NCT03250910) | Phase 4 | Completed | 228 | Generic velpatasvir + sofosbuvir ± ribavirin for HCV in HIV-coinfected patients; studies HCV outcomes, not HBV (relevance grade C — HCV population only) |
| [NCT02938013](https://clinicaltrials.gov/study/NCT02938013) | Phase 4 | Completed | 15 | Liver/plasma sampling study of HCV viral kinetics during sofosbuvir/velpatasvir(±voxilaprevir) treatment; no HBV endpoint |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | Recruiting | 200 | Cohort study of Vosevi (SOF/VEL/VOX) in patients who failed prior DAA therapy for HCV; not an HBV trial (relevance grade C) |
| [NCT03086044](https://clinicaltrials.gov/study/NCT03086044) | Phase 4 | Unknown | 148 | Pilot trial transplanting organs from HCV-positive donors to HCV-negative recipients with post-transplant antiviral prophylaxis; HCV-specific |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Completed | 33,808 | Large safety comparison of DAA-treated vs. untreated HCV patients; no HBV arm |
| [NCT03570112](https://clinicaltrials.gov/study/NCT03570112) | N/A | Completed | 40 | Natural history and vertical transmission of chronic HCV in pregnancy, with postpartum sofosbuvir/velpatasvir treatment; HCV only |
| [NCT03226717](https://clinicaltrials.gov/study/NCT03226717) | N/A | Unknown | 100 | Evaluates effect of DAAs on HCV-associated arthropathy/extrahepatic manifestations; not HBV-related |
| [NCT04653818](https://clinicaltrials.gov/study/NCT04653818) | Phase 4 | Completed | 84 | RCT on whether DAA use affects HCV-related hepatocellular carcinoma recurrence after ablation; HCV-specific |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Phase 4 | Unknown | 25 | Feasibility study switching HIV-HCV coinfected patients through an antiretroviral regimen sequence including 12 weeks of sofosbuvir/velpatasvir for HCV; not an HBV endpoint |
| [NCT05016609](https://clinicaltrials.gov/study/NCT05016609) | Phase 4 | Unknown | 1,800 | Cluster-randomized trial of same-visit HCV testing/treatment models among people who inject drugs; HCV-focused |

**Note:** None of the trials collected for this candidate directly evaluate velpatasvir as a treatment for hepatitis B. All are HCV treatment or HCV-related studies, several conducted in populations with HIV or HBV co-infection where velpatasvir was used solely for the HCV component.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case Report | J Med Case Rep | HBV reactivation (via an HBsAg immune-escape mutant) in an anti-HBc-positive patient during sofosbuvir/velpatasvir treatment for HCV — a safety signal, not efficacy evidence for HBV |
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | Single-arm trial | Lancet Gastroenterol Hepatol | Sofosbuvir/velpatasvir efficacy and safety in treatment-naive HCV genotype 4 patients in Rwanda; no HBV endpoint |
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Single-arm trial | Lancet Gastroenterol Hepatol | Sofosbuvir/velpatasvir/voxilaprevir retreatment of HCV genotype 4 non-a/d subtypes after prior DAA failure; HCV-specific |
| [38910758](https://pubmed.ncbi.nlm.nih.gov/38910758/) | 2024 | Cross-sectional study | Cureus | Efficacy of sofosbuvir/velpatasvir for HCV in chronic kidney disease patients; no HBV data |
| [33217040](https://pubmed.ncbi.nlm.nih.gov/33217040/) | 2021 | Cohort study | J Gastroenterol Hepatol | Real-world efficacy/safety of sofosbuvir/velpatasvir in HCV genotype 3, including decompensated cirrhosis and HCC patients; HCV only |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | General review of chronic HCV diagnosis and treatment pathway for primary care; does not address HBV |
| [31360020](https://pubmed.ncbi.nlm.nih.gov/31360020/) | 2019 | Real-world study | J Clin Exp Hepatol | Generic pan-genotypic sofosbuvir/velpatasvir experience for chronic HCV in Myanmar; HCV-specific |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | Review of pediatric viral hepatitis management, covering both HBV and HCV therapies broadly, but does not report velpatasvir activity against HBV specifically |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | Cohort study | J Viral Hepat | Simplified HCV treatment strategy in Myanmar; HBV-coinfected participants were treated concurrently with **tenofovir**, not velpatasvir, for their HBV infection |
| [32405174](https://pubmed.ncbi.nlm.nih.gov/32405174/) | 2020 | Case series | J Clin Exp Hepatol | Sofosbuvir/velpatasvir experience in HCV patients with end-stage renal disease/kidney transplant; no HBV outcome reported |

**Note:** Across the full 20-record literature set, only one item (the 2019 case report) directly links velpatasvir to HBV, and it describes a reactivation risk rather than therapeutic benefit. The remainder either study HCV exclusively or mention HBV only in the context of co-infected populations managed with separate HBV-specific antivirals (e.g., tenofovir).

## EU Market Information

Velpatasvir has no standalone EU marketing authorization on record in this dataset (0 licenses, market status: **Not marketed**). It is only available in the EU as part of fixed-dose combination products (e.g., sofosbuvir/velpatasvir, marketed as Epclusa, and sofosbuvir/velpatasvir/voxilaprevir, marketed as Vosevi), which fall outside the scope of the regulatory data captured for this candidate.

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Velpatasvir's mechanism (HCV NS5A inhibition) has no known homologous target in HBV, and virtually all collected trial and literature evidence for this pairing reflects HCV treatment studies or HCV/HBV co-infection contexts rather than genuine anti-HBV activity — the one direct HBV-related report describes a reactivation risk, not efficacy. This pattern indicates the TxGNN signal is likely driven by shared clinical co-occurrence rather than true biological plausibility.

**To proceed, the following is needed:**
- Regulatory label data (warnings/contraindications) from the relevant national/EU authority — currently a blocking data gap that prevents any initial safety assessment (S1)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent source
- Dedicated in vitro or in vivo studies testing velpatasvir activity against HBV replication, to distinguish true mechanistic relevance from co-infection-context contamination in the evidence base
- If any such preclinical signal emerges, monitoring of HBV reactivation risk should be a specific safety focus, given the existing case-report signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

