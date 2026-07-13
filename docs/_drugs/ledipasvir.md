---
layout: default
title: Ledipasvir
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Ledipasvir
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

# Ledipasvir: From Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Ledipasvir is an NS5A inhibitor approved as part of the Harvoni® (ledipasvir/sofosbuvir) fixed-dose combination for the treatment of chronic hepatitis C virus (HCV) infection.
The TxGNN model predicts it may be effective for **Hepatitis B Virus Infection**,
with **21 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic hepatitis C virus infection (as part of ledipasvir/sofosbuvir combination; Harvoni®) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| EU Market Status | Not marketed (standalone) |
| Number of Authorizations | 0 (standalone; marketed only as Harvoni® combination) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ledipasvir is a potent NS5A inhibitor designed to target the hepatitis C virus replication complex. Its partner sofosbuvir is a nucleotide analogue that inhibits the NS5B RNA-dependent RNA polymerase. Together, as Harvoni®, the combination achieves sustained virologic response (SVR12) rates exceeding 95% in chronic HCV genotype 1 infection. Detailed standalone MOA data for ledipasvir are not available in the current evidence pack; however, it is well-established pharmacologically that ledipasvir's direct target — HCV NS5A protein — has no sequence homologue in the hepatitis B virus (HBV) genome.

The mechanistic rationale for HBV activity therefore rests primarily on sofosbuvir's component of the LDV/SOF combination. Sofosbuvir, as a chain-terminating nucleotide analogue, has structural potential to cross-inhibit the HBV polymerase reverse transcriptase domain. This hypothesis was directly tested when clinicians observed modest HBsAg reductions in HCV/HBV coinfected patients treated with LDV/SOF — leading to the prospective Phase 2 trial NCT03312023, which enrolled HBV monoinfected subjects and measured HBsAg and HBV DNA decline at Week 12 as primary and secondary endpoints, respectively (PMID 36045503).

There is an important additional layer of evidence: a well-documented safety signal of HBV reactivation during DAA-based HCV treatment. Multiple cohort studies (PMIDs 29334502, 28585404, 29194858) and Phase 3b data from Taiwan (NCT02613871, n=111) document that suppression of HCV with LDV/SOF in coinfected patients can unmask or amplify HBV replication. While this reactivation phenomenon represents a safety risk, it simultaneously confirms that HBV is biologically reactive to the antiviral environment created by LDV/SOF — supporting the TxGNN prediction that HBV is a physiologically plausible target. Clinically, any use of LDV/SOF in HBV-infected patients must include mandatory concurrent monitoring of HBV DNA and liver function, and prophylactic antiviral therapy (e.g., entecavir or tenofovir) should be considered.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Direct pilot study of LDV/SOF for 12 weeks in HBV monoinfected subjects; primary endpoint was HBsAg decline from baseline; secondary endpoint was HBV DNA reduction at Week 12 |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3b | Completed | 111 | LDV/SOF fixed-dose combination in adults with chronic genotype 1 or 2 HCV and HBV coinfection in Taiwan; assessed antiviral efficacy, safety, and HBV reactivation over 108-week follow-up |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of DAA treatment in chronic HCV/HBV coinfected patients; determined incidence, morbidity, mortality and predisposing factors for HBV reactivation during direct anti-HCV treatment |
| [NCT02219685](https://clinicaltrials.gov/study/NCT02219685) | Phase 2 | Completed | 40 | Double-blind, placebo-controlled RCT evaluating LDV/SOF effects on cerebral metabolism and neurocognition in chronic HCV; highest-quality study design with ledipasvir as direct investigational agent |
| [NCT03261349](https://clinicaltrials.gov/study/NCT03261349) | Phase 2 | Unknown | 21 | Pilot study of HARVONI® (LDV/SOF) for HCV genotype 1 or 2-associated indolent B-cell Non-Hodgkin's Lymphoma; sustained virologic response correlated with lymphoma regression |
| [NCT02836925](https://clinicaltrials.gov/study/NCT02836925) | Phase 2 | Completed | 40 | Multicenter single-arm study evaluating antiviral activity of interferon-free LDV/SOF (genotype 1 and 4) in HCV-associated indolent B-cell lymphomas |
| [NCT03423641](https://clinicaltrials.gov/study/NCT03423641) | N/A | Completed | 33,808 | Large-scale real-world DAA safety surveillance study; systematically recorded adverse events including HBV reactivation during HCV treatment, providing critical safety background |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 Clinical Study | Journal of Medical Virology | The only direct Phase 2 pilot trial testing LDV/SOF in HBV monoinfected subjects; observed modest HBsAg reduction based on retrospective HBV/HCV coinfection data |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | Cohort | Clinical Infectious Diseases | 108-week post-treatment follow-up of HBV dynamics in LDV/SOF-treated HCV/HBV coinfected patients; characterised long-term HBV reactivation pattern |
| [29174546](https://pubmed.ncbi.nlm.nih.gov/29174546/) | 2018 | Retrospective Cohort | Gastroenterology | Prospective study of LDV/SOF efficacy and HBV reactivation risk in HBV-coinfected patients; established clinical risk profile for HBV reactivation during HCV cure |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort/Safety | Journal of Clinical Gastroenterology | Risk of HBV reactivation in actively infected or previously exposed patients during or after HCV treatment with DAAs including LDV/SOF |
| [27486112](https://pubmed.ncbi.nlm.nih.gov/27486112/) | 2016 | Cohort/Safety | Clinical Infectious Diseases | Analysis of 173 patients in Taiwan/Korea LDV/SOF clinical trial; 103 patients (60%) had prior HBV infection; none showed evidence of HBV reactivation during treatment |
| [27367295](https://pubmed.ncbi.nlm.nih.gov/27367295/) | 2016 | Cohort | Antiviral Therapy | Pilot study of LDV/SOF in HCV patients coinfected with HBV; demonstrated HCV SVR with concurrent HBV monitoring |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Cohort | Journal of Viral Hepatitis | Prospective study of HBV reactivation risk during DAA treatment for HCV infection in cancer patients with HBV/HCV coinfection |
| [28585404](https://pubmed.ncbi.nlm.nih.gov/28585404/) | 2017 | Cohort | Hepatology Research | Japanese prospective cohort (790 patients) analysing frequency and risk factors for HBV reactivation during all-oral DAA treatment including SOF/LDV |
| [29194858](https://pubmed.ncbi.nlm.nih.gov/29194858/) | 2018 | Cohort | Journal of Viral Hepatitis | 25 HBV coinfected and 765 resolved-HBV patients monitored during DAA therapy including SOF/LDV; low incidence of clinically significant HBV reactivation reported |
| [37254310](https://pubmed.ncbi.nlm.nih.gov/37254310/) | 2024 | In Silico | Journal of Biomolecular Structure & Dynamics | Molecular docking, dynamics simulation and MM/GBSA analysis screening antiviral compounds including ledipasvir against HBV X protein as a therapeutic target |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note from evidence review:** Although formal safety data are not available in the current evidence pack, multiple studies identified in the evidence collection document a clinically important safety signal — **HBV reactivation during LDV/SOF therapy** — including at least one case of acute fulminant hepatitis B in an HIV/HBV/HCV triply-infected patient receiving DAAs. Any use of LDV/SOF for HBV indication must include mandatory HBV DNA and liver function monitoring, and prophylactic HBV antiviral therapy should be considered in high-risk patients.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 open-label study (NCT03312023; PMID 36045503) provides the highest-quality direct evidence, having enrolled HBV monoinfected subjects and measuring HBsAg decline as the primary endpoint. Complementary Phase 3b data from Taiwan (NCT02613871, n=111) and Phase 2/3 coinfection data (NCT02555943, n=23) provide supporting clinical context. However, the mechanistic contribution of ledipasvir itself — as opposed to sofosbuvir — to anti-HBV activity remains unresolved, and observed HBsAg reductions were modest rather than curative, limiting clinical translation without further optimisation.

**To proceed, the following is needed:**

- **Mechanistic clarification:** Define whether ledipasvir contributes any direct anti-HBV activity, or whether observed effects are entirely attributable to sofosbuvir — this is essential for rational repurposing decisions
- **Dedicated Phase 2b/3 RCT:** Design a randomised controlled trial with HBV functional cure (HBsAg seroconversion) as the primary endpoint in HBV monoinfected patients, powered sufficiently beyond the 21-patient pilot study
- **Safety monitoring protocol:** Mandatory pre-treatment HBV DNA screening, on-treatment HBV DNA and ALT monitoring at Weeks 4, 8, 12, and 24 post-treatment; prophylactic entecavir or tenofovir co-administration protocol for HBV-active patients
- **Combination optimisation:** Evaluate whether LDV/SOF alone or LDV/SOF plus standard HBV antivirals (entecavir, tenofovir) provides superior HBsAg decline
- **EU regulatory pathway:** Clarify whether a new indication extension for Harvoni® (ledipasvir/sofosbuvir) in HBV is feasible under EMA framework, given the existing Harvoni® marketing authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

