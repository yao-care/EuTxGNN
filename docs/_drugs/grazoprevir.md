---
layout: default
title: Grazoprevir
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Grazoprevir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Grazoprevir: From Chronic Hepatitis C Virus Infection to HIV Infectious Disease

## One-Sentence Summary

Grazoprevir is an HCV NS3/4A protease inhibitor, originally developed and used as part of the elbasvir/grazoprevir combination (Zepatier) for chronic hepatitis C virus (HCV) genotype 1, 4, and 6 infection.
The TxGNN model predicts it may also be effective for **HIV infectious disease**, with **14 clinical trials** and **20 publications** nominally linked to this pairing —
however, on close review, every one of these studies evaluates HCV treatment outcomes in HIV/HCV co-infected populations, not antiretroviral efficacy, so the supporting evidence for an actual HIV indication is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C Virus (HCV) infection, genotype 1/4/6 (as part of Elbasvir/Grazoprevir, Zepatier) — inferred from trial context; no structured license record is available in this dataset |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.73% (rank 3,468) |
| Evidence Level | L4 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on the information available in the evidence pack, Grazoprevir is a component of the elbasvir/grazoprevir fixed-dose combination, which works by inhibiting the HCV NS3/4A serine protease — an enzyme essential for HCV polyprotein processing and viral replication. This mechanism has proven efficacy in chronic HCV genotype 1, 4, and 6 infection.

HIV and HCV frequently co-occur in the same patient populations (people who inject drugs, men who have sex with men, and other shared-risk groups), so a large number of clinical trials studying HCV treatment specifically enrolled HIV/HCV co-infected participants (e.g., C-EDGE CO-INFECTION, C-WORTHY, the Swiss HCVree Trial). This population overlap is almost certainly why the knowledge graph links Grazoprevir to "HIV infectious disease" — the drug and the disease co-occur frequently in the same study records, not because Grazoprevir has demonstrated antiretroviral activity.

Critically, none of the 14 identified trials use an HIV-related endpoint. Their primary endpoint is uniformly Sustained Virologic Response for HCV (SVR12), and the population-level relevance grading in the evidence pack rates all of them "C" (low relevance to an HIV indication). Grazoprevir has no reported affinity for HIV protease, reverse transcriptase, or integrase. Mechanistically, this prediction should be treated as a population co-occurrence artifact rather than a genuine repurposing signal — consistent with why the evidence pack's own scoring assigns this candidate "Hold" rather than a stronger recommendation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03098121](https://clinicaltrials.gov/study/NCT03098121) | Phase 4 | Completed | 40 | Grazoprevir/elbasvir in peginterferon/ribavirin-experienced PWID and MSM with genotype 1 HCV/HIV co-infection; endpoint is HCV efficacy/tolerability, not HIV outcome |
| [NCT02105662](https://clinicaltrials.gov/study/NCT02105662) | Phase 3 | Completed | 218 | Grazoprevir + elbasvir in treatment-naïve HCV genotype 1/4/6 patients co-infected with HIV; primary hypothesis was HCV SVR12 >70%, not an HIV endpoint |
| [NCT02897596](https://clinicaltrials.gov/study/NCT02897596) | Phase 3 | Unknown | 62 | 8 vs 12 weeks of grazoprevir/elbasvir for early chronic HCV genotype 1/4 in HIV co-infected patients; HCV clearance is the endpoint |
| [NCT04048850](https://clinicaltrials.gov/study/NCT04048850) | N/A | Completed | 25 | Cohort study of Zepatier in HCV mono- and HIV/HCV co-infected, treatment-naïve/experienced patients with substance use; assesses HCV treatment, not HIV |
| [NCT03037151](https://clinicaltrials.gov/study/NCT03037151) | Phase 4 | Unknown | 100 | Safety/fibrosis improvement with grazoprevir + elbasvir in compensated cirrhotic HCV GT1/GT6 patients with or without HIV; HIV status is a stratification variable, not the treatment target |
| [NCT03221582](https://clinicaltrials.gov/study/NCT03221582) | Phase 4 | Terminated (n=6) | 6 | Impact of HCV therapy on cardiovascular risk and bone health in HCV mono- and HIV/HCV co-infected patients; terminated early, not an HIV efficacy trial |
| [NCT02785666](https://clinicaltrials.gov/study/NCT02785666) | Phase 3 | Completed | 150 | Swiss HCVree Trial: "treat, counsel, cure" strategy with grazoprevir/elbasvir ± ribavirin in HIV-positive MSM within the Swiss HIV Cohort Study; endpoint is HCV cure rate |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | Completed | 87 | Cardiovascular risk outcomes after HCV eradication in HIV co-infected vs HIV mono-infected controls; evaluates cardiovascular endpoints post-HCV-cure, not antiretroviral effect |
| [NCT02252016](https://clinicaltrials.gov/study/NCT02252016) | Phase 3 | Completed | 159 | Double-blind, placebo-controlled trial of grazoprevir + elbasvir in HCV GT1/4/6 patients with inherited blood disorders, with and without HIV co-infection; SVR12 is the primary hypothesis |
| [NCT02600325](https://clinicaltrials.gov/study/NCT02600325) | Phase 3 | Completed | 80 | DAHHS-2: grazoprevir + elbasvir for acute HCV genotype 1/4 in HIV-positive individuals; assesses acute HCV cure, not HIV control |

*Note: 4 additional trials were identified for this pairing but are omitted here for brevity (all similarly HCV-endpoint focused). Across all 14 trials, HIV serostatus functions only as a co-infection/stratification variable — none measure an antiretroviral or HIV virologic outcome.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26423374](https://pubmed.ncbi.nlm.nih.gov/26423374/) | 2015 | RCT (HCV, non-randomised open-label) | The Lancet HIV | C-EDGE CO-INFECTION study: efficacy, safety and tolerability of grazoprevir + elbasvir in HCV/HIV co-infected patients — endpoint is HCV response, HIV status is inclusion criterion only |
| [25467560](https://pubmed.ncbi.nlm.nih.gov/25467560/) | 2015 | RCT (Phase 2) | Lancet | C-WORTHY trial: 8 vs 12 weeks of grazoprevir + elbasvir ± ribavirin in HCV GT1 mono-infected and HIV/HCV co-infected patients; primary outcome is HCV SVR |
| [26849059](https://pubmed.ncbi.nlm.nih.gov/26849059/) | 2016 | Review (PK/PD) | Expert Opinion on Drug Metabolism & Toxicology | Reviews pharmacodynamics/pharmacokinetics of elbasvir/grazoprevir specifically for HCV treatment |
| [27603877](https://pubmed.ncbi.nlm.nih.gov/27603877/) | 2016 | Review | Expert Review of Clinical Pharmacology | Covers mechanism, PK/PD, clinical use, safety and efficacy of elbasvir/grazoprevir for chronic HCV genotypes 1 and 4 |
| [27091555](https://pubmed.ncbi.nlm.nih.gov/27091555/) | 2016 | Review | Expert Opinion on Drug Safety | Safety and efficacy review of elbasvir/grazoprevir for HCV genotypes 1, 4, and 6 |
| [28417245](https://pubmed.ncbi.nlm.nih.gov/28417245/) | 2017 | Review | Drugs | Comprehensive review of elbasvir/grazoprevir (Zepatier) approval and efficacy for chronic HCV genotype 1 and 4 |
| [28947524](https://pubmed.ncbi.nlm.nih.gov/28947524/) | 2017 | Review | American Journal of Health-System Pharmacy | Chemistry, pharmacology, PK/PD, efficacy, safety and dosing of elbasvir-grazoprevir for HCV |
| [30233138](https://pubmed.ncbi.nlm.nih.gov/30233138/) | 2018 | Review | Drug Design, Development and Therapy | Current evidence on safety and efficacy of elbasvir/grazoprevir for chronic HCV |
| [26933896](https://pubmed.ncbi.nlm.nih.gov/26933896/) | 2016 | Review | Expert Opinion on Pharmacotherapy | Overview of grazoprevir + elbasvir for HCV treatment |
| [30745392](https://pubmed.ncbi.nlm.nih.gov/30745392/) | 2019 | PK Interaction Study | Antimicrobial Agents and Chemotherapy | Pharmacokinetic drug-drug interactions between elbasvir/grazoprevir and HIV protease inhibitors (ritonavir, atazanavir, lopinavir, darunavir) in healthy volunteers — relevant to co-administration safety, not to anti-HIV efficacy of grazoprevir itself |

*Note: 10 additional publications were identified but omitted for brevity; nearly all are HCV-focused reviews or DDI studies involving concomitant antiretroviral therapy, reinforcing that no literature demonstrates direct anti-HIV activity for grazoprevir.*

---

## EU Market Information

No EU marketing authorization records are available for Grazoprevir in this dataset (market status: **Not Marketed**, 0 licenses on record). No authorization number, product name, or approved indication text could be extracted.

---

## Safety Considerations

Please refer to the SmPC for safety information. *(Key warnings, contraindications, and drug-drug interaction data are all marked as data gaps in this evidence pack — including a Blocking-severity gap (DG001) for TFDA/label warnings and contraindications, which must be resolved before any S1 safety screening can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The apparent evidence base (14 trials, 20 publications) is a population-overlap artifact: every study enrolls HIV/HCV co-infected patients but measures HCV virologic response, not an HIV/antiretroviral endpoint, and Grazoprevir has no known mechanistic activity against HIV targets.
- This pattern is consistent across the broader prediction set for this drug: multiple other high-scoring TxGNN predictions for Grazoprevir (hepatitis B, hepatitis E, hepatitis A, and several animal/veterinary viral diseases) show the same lack of genuine mechanistic or clinical support, suggesting the knowledge graph is picking up co-occurrence noise around "hepatitis/viral infection" nodes rather than a specific repurposing signal.
- Foundational safety data (MOA, TFDA/EMA warnings, contraindications, DDI) are entirely missing, which independently blocks any further evaluation regardless of the indication's plausibility.

**To proceed, the following is needed:**
- Resolve Blocking data gap DG001 (TFDA/EMA label warnings and contraindications) before any safety screening
- Resolve High-severity data gap DG002 (verified mechanism of action from DrugBank/EMA SmPC) to formally confirm the absence of anti-HIV pharmacological plausibility
- Drug-drug interaction data (current DDI query returned no results)
- If this candidate is still pursued despite low mechanistic plausibility, require in vitro antiviral activity data against HIV protease/reverse transcriptase/integrase as a gating step before any clinical consideration
- Consider refining the TxGNN/evidence pipeline to flag and downweight co-infection-cohort trials that do not report a disease-specific efficacy endpoint, to reduce false-positive repurposing signals of this type
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

