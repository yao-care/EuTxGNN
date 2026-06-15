---
layout: default
title: Atazanavir
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Atazanavir
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

# Atazanavir: From HIV-1 Infection to Congenital Human Immunodeficiency Virus

## One-Sentence Summary

Atazanavir is an established HIV-1 protease inhibitor used as part of combination antiretroviral therapy for treating HIV-1 infection in adults and pediatric patients.
The TxGNN model predicts it may be effective for **Congenital Human Immunodeficiency Virus** (vertically transmitted HIV infection), with **33 clinical trials** and **7 publications** currently supporting this direction.

> **Reporting note**: TxGNN's top-ranked predictions (ranks 1–4) include a veterinary indication (feline AIDS, L5), an animal-model-only finding (simian immunodeficiency, L4), an ultra-rare genetic neurological disorder with no mechanistic link (L5), and an obsolete disease classification (L5). None are actionable for human drug development. This report focuses on **rank 5 — Congenital Human Immunodeficiency Virus** — as the first human HIV indication with substantive clinical trial evidence (L1), and the most clinically meaningful repurposing target.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (established global approval; no EU registration) |
| Predicted New Indication | Congenital Human Immunodeficiency Virus |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| EU Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established clinical pharmacology, Atazanavir is an azapeptide HIV-1 protease inhibitor (brand name Reyataz, Bristol-Myers Squibb) that selectively inhibits the HIV-1 aspartyl protease enzyme. By blocking proteolytic cleavage of the Gag-Pol polyprotein precursor, it prevents maturation of HIV particles into infectious virions. It is administered orally, typically pharmacokinetically boosted with ritonavir or cobicistat to sustain therapeutic plasma concentrations.

Congenital HIV infection results from mother-to-child transmission of the same HIV-1 virus during pregnancy, childbirth, or breastfeeding. Because the viral protease targeted by Atazanavir is identical in congenitally transmitted and adult HIV-1 infection, the mechanism translates directly to this population. Suppressing viral replication in perinatally infected neonates and children prevents progression to AIDS — the same biological goal as in adult treatment. Major regulatory bodies including the WHO, EMA, and US FDA have endorsed protease inhibitor-based regimens for both prevention of mother-to-child transmission (PMTCT) and treatment of perinatally infected children.

The clinical evidence base is substantial across two distinct patient groups. In adults, multiple Phase 3 trials established ATV/ritonavir as non-inferior to lopinavir/ritonavir and comparable to newer integrase inhibitor-based regimens. In children, the dedicated PRINCE I (≥3 months to <6 years) and PRINCE II (3 months to <11 years) studies evaluated Atazanavir oral powder formulation with ritonavir, demonstrating appropriate pharmacokinetic exposure, safety, and antiviral activity covering the full congenital HIV age range. The PHACS SMARTT cohort further provided long-term multi-domain safety surveillance for in utero ARV-exposed children across 22 US sites.

---

## Clinical Trial Evidence

33 clinical trials were identified for the **Congenital Human Immunodeficiency Virus** indication. The 10 most relevant are listed below, prioritised by Phase 3 design and sample size.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00272779](https://clinicaltrials.gov/study/NCT00272779) | Phase 3 | Completed | 1,057 | CASTLE: 96-week head-to-head ATV/RTV vs LPV/RTV, each combined with TDF/FTC, in treatment-naïve HIV-1 adults; largest direct protease inhibitor comparison trial — establishes ATV/RTV as an effective first-line antiretroviral regimen |
| [NCT02269917](https://clinicaltrials.gov/study/NCT02269917) | Phase 3 | Completed | 1,149 | Randomised switch to D/C/F/TAF vs continuation of boosted PI (including ATV) + FTC/TDF in virologically suppressed HIV-1 adults; demonstrates durability of ATV-based viral suppression and supports structured switch decisions |
| [NCT02227238](https://clinicaltrials.gov/study/NCT02227238) | Phase 3 | Completed | 627 | DAWNING: Dolutegravir vs ATV-based regimen in first-line NNRTI failure; defines the comparative efficacy and contemporary role of ATV in WHO-aligned second-line therapy |
| [NCT02422797](https://clinicaltrials.gov/study/NCT02422797) | Phase 3 | Completed | 518 | SWORD-1: DTG + RPV vs current PI/NNRTI/INI regimen (including ATV) in virologically suppressed adults; non-inferiority design confirming sustained suppression on ATV-containing baseline regimens |
| [NCT01910402](https://clinicaltrials.gov/study/NCT01910402) | Phase 3 | Completed | 499 | ARIA: DTG/ABC/3TC vs ATV+RTV + TDF/FTC in ART-naïve women; direct ATV comparator arm providing 48-week gender-specific safety and efficacy data |
| [NCT01335698](https://clinicaltrials.gov/study/NCT01335698) | Phase 3 | Completed | 160 | PRINCE II: ATV oral powder + RTV with optimised NRTI backbone in HIV-infected children aged 3 months to <11 years; key pediatric study covering the primary congenital HIV age group — safety, efficacy, and PK |
| [NCT01099579](https://clinicaltrials.gov/study/NCT01099579) | Phase 3 | Completed | 82 | PRINCE I: ATV oral powder + RTV in HIV-infected children aged 3 months to <6 years; youngest-age pediatric ATV evaluation demonstrating appropriate drug exposure and tolerability in infants and toddlers |
| [NCT01003990](https://clinicaltrials.gov/study/NCT01003990) | Phase 3 | Completed | 710 | Extended access study providing long-term ATV safety surveillance (through 2016) in HIV-infected subjects completing prior BMS-sponsored trials; supports the durability of the long-term safety profile |
| [NCT01691794](https://clinicaltrials.gov/study/NCT01691794) | Phase 4 | Completed | 108 | ATV capsule + RTV in HIV-infected pediatric patients aged 6 to <18 years; prospective international multicenter single-arm safety monitoring study covering the older pediatric congenital HIV population |
| [NCT00207142](https://clinicaltrials.gov/study/NCT00207142) | Phase 4 | Completed | 252 | INDUMA: Randomised maintenance comparison of unboosted vs boosted Reyataz after ATV/RTV induction in treatment-naïve HIV patients; evaluates viral suppression durability with reduced boosting — relevant to long-term paediatric management |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27242802](https://pubmed.ncbi.nlm.nih.gov/27242802/) | 2016 | Prospective Cohort | Frontiers in Immunology | PHACS SMARTT: 22-site US cohort of >3,500 HIV-exposed uninfected children evaluating in utero ARV safety across metabolic, cardiac, neurological, and neurodevelopmental domains; most comprehensive long-term safety evidence for perinatal ARV exposure including ATV |
| [25383770](https://pubmed.ncbi.nlm.nih.gov/25383770/) | 2015 | Cohort Study | JAMA Pediatrics | Congenital anomaly risk in HIV-exposed uninfected infants by prenatal ARV type; overall reassuring findings with agent-level signal detection — ATV included as a key exposure of interest |
| [40011239](https://pubmed.ncbi.nlm.nih.gov/40011239/) | 2025 | Pharmacovigilance | Eur J Clin Pharmacol | European congenital anomaly registry case/non-case study on ARV fetal exposure risk across multiple EU centres; most recent and largest EU-based safety evidence for prenatal ATV exposure |
| [28459118](https://pubmed.ncbi.nlm.nih.gov/28459118/) | 2016 | Prospective Cohort | J AIDS Immune Res | Newborn hearing screening in 1,435 HEU infants from PHACS SMARTT; evaluates association of in utero ATV and other ARV exposures with sensorineural hearing referral risk |
| [24992294](https://pubmed.ncbi.nlm.nih.gov/24992294/) | 2015 | Clinical PK Study | Antiviral Therapy | ATV pharmacokinetics during pregnancy with and without tenofovir co-administration; confirms adequate drug exposure throughout gestation, directly supporting ATV use for PMTCT regardless of NRTI backbone |
| [29859254](https://pubmed.ncbi.nlm.nih.gov/29859254/) | 2018 | In Vitro Study | Reprod Toxicol | ATV and RTV interactions with placental ABC transporters (P-gp/ABCB1, BCRP/ABCG2, MRP2/ABCC2) in rat models; mechanistic basis for transplacental drug transfer — relevant to quantifying fetal exposure in congenital HIV prevention |
| [31595301](https://pubmed.ncbi.nlm.nih.gov/31595301/) | 2020 | Pharmacovigilance | Clin Infect Dis | Pharmacovigilance database analysis for dolutegravir pregnancy safety; ATV cited as reference comparator class, providing indirect comparative safety context for the perinatal HIV setting |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Atazanavir has robust Phase 3 RCT evidence for HIV-1 treatment including dedicated pediatric programmes (PRINCE I and II) covering the congenital HIV age group from 3 months onward, constituting genuine L1 evidence. However, this represents Atazanavir's established therapeutic domain rather than a novel repurposing discovery, the drug carries no current EU registration, and critical safety data gaps (warnings, contraindications, drug interactions) remain unresolved in this evidence pack.

**To proceed, the following is needed:**

- **SmPC/prescribing information retrieval**: Obtain the EMA SmPC or BMS prescribing information to document key warnings, contraindications, and drug interactions — all currently flagged as data gaps (DG001); this is a Blocking item before any clinical safety assessment
- **MOA documentation**: Complete the DrugBank API query (DG002 remediation) to formally confirm the protease inhibitor mechanism of action for inclusion in regulatory submissions
- **EU regulatory status clarification**: Verify whether the EMA marketing authorisation for Reyataz has formally lapsed or been withdrawn, and whether a re-application would be required
- **Paediatric formulation availability**: Confirm that ATV oral powder (for ≥3 months to <6 years) and capsules (≥6 years) remain commercially accessible or manufacturable, given the current EU non-marketing status
- **Neonatal PK gap assessment**: Existing data cover children ≥3 months; a dedicated neonatal PK/safety review is needed for the youngest congenital HIV patients (<3 months of age)
- **Known ATV class-effect monitoring plan**: Structure surveillance for hyperbilirubinemia (UGT1A1 inhibition), nephrolithiasis, QTc prolongation, and lipid effects in the target paediatric population before any clinical implementation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

