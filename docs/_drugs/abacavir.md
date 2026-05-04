---
layout: default
title: Abacavir
parent: 僅模型預測 (L5)
nav_order: 11
evidence_level: L5
indication_count: 10
---

# Abacavir
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

# Abacavir: From HIV-1 Infection to Congenital Human Immunodeficiency Virus

## One-Sentence Summary

Abacavir is a nucleoside reverse transcriptase inhibitor (NRTI) used as a core component of combination antiretroviral therapy for HIV-1 infection in adults.
The TxGNN model predicts it may be effective for **Congenital Human Immunodeficiency Virus** (perinatally acquired HIV in infants and children), with **10+ Phase 2/3 clinical trials** and **7 publications** supporting this direction.
TxGNN's two highest-ranked predictions (simian immunodeficiency virus [SIV] and feline immunodeficiency virus [FIV]) are non-human animal models without human repurposing value; congenital HIV is the most clinically actionable indication identified, reaching evidence level L1.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (adult, in combination antiretroviral therapy) |
| Predicted New Indication | Congenital Human Immunodeficiency Virus (perinatally acquired HIV) |
| TxGNN Prediction Score | 92.76% |
| Evidence Level | L1 |
| EU Market Status | Not marketed (per available data) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not included in this evidence pack. Based on established pharmacology, Abacavir is a synthetic carbocyclic nucleoside analogue prodrug. After intracellular phosphorylation to carbovir triphosphate (CBV-TP), it acts as a competitive inhibitor of HIV-1 reverse transcriptase and functions as a DNA chain terminator—directly halting the conversion of viral RNA into proviral DNA that is essential for HIV-1 replication. This places Abacavir in the NRTI class, the backbone of all major combination antiretroviral regimens.

Congenital HIV infection occurs via mother-to-child transmission (MTCT) of HIV-1 during pregnancy, delivery, or breastfeeding. The causative pathogen is biologically identical to the virus responsible for adult HIV-1 infection. This means the viral target (HIV-1 reverse transcriptase), the inhibitory mechanism, and the resistance pathways are fully conserved between adult and pediatric populations. The repurposing rationale here is therefore a **population extension**, not a mechanistic extrapolation—the same NRTI activity that suppresses HIV-1 replication in adults operates identically in infants and children with perinatally acquired infection.

The IMPAACT (International Maternal Pediatric Adolescent AIDS Clinical Trials) network has conducted multiple Phase 3 studies demonstrating the safety and efficacy of ABC/3TC (abacavir/lamivudine) and ABC/DTG/3TC fixed-dose combinations in children and adolescents across diverse settings. Age-appropriate dispersible tablet formulations have been developed and studied in bioavailability trials. The primary risk unique to the pediatric context is the HLA-B\*5701-associated abacavir hypersensitivity reaction, which is well-managed through mandatory pre-treatment genotyping before any patient—including infants—initiates treatment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00102960](https://clinicaltrials.gov/study/NCT00102960) | Phase 3 | Completed | 377 | Compared strategies for initiating ART in HIV-infected infants in resource-limited settings; directly evaluated optimal timing for ABC-containing regimens in neonates |
| [NCT02105987](https://clinicaltrials.gov/study/NCT02105987) | Phase 3 | Completed | 555 | STRIIVING study: switching to ABC/DTG/3TC FDC vs. continuing current ART in virologically suppressed HIV-1 adults; non-inferior antiviral activity confirmed at 24 weeks |
| [NCT01910402](https://clinicaltrials.gov/study/NCT01910402) | Phase 3 | Completed | 499 | DTG/ABC/3TC FDC once daily vs. ATV+RTV+TDF/FTC in ART-naïve HIV-1-infected women; demonstrated non-inferior efficacy with favourable tolerability profile |
| [NCT03016533](https://clinicaltrials.gov/study/NCT03016533) | Phase 3 | Completed | 100 | IMPAACT P1093/P2019 rollover: provided continued access to dolutegravir with ABC/3TC background therapy in HIV-infected children and adolescents |
| [NCT02422797](https://clinicaltrials.gov/study/NCT02422797) | Phase 3 | Completed | 518 | Non-inferiority study: switching from NRTI-based regimen (including ABC) to dolutegravir + rilpivirine in virologically suppressed HIV-1 patients |
| [NCT02429791](https://clinicaltrials.gov/study/NCT02429791) | Phase 3 | Completed | 510 | Parallel non-inferiority study of DTG + RPV vs. continued ABC-based ART in virologically suppressed HIV-1 adults; confirmed durable viral suppression upon switch |
| [NCT02938520](https://clinicaltrials.gov/study/NCT02938520) | Phase 3 | Active, not recruiting | 631 | FLAIR study: long-acting cabotegravir + rilpivirine vs. ABC/DTG/3TC single-tablet regimen in ART-naïve HIV-1 adults; evaluates Abacavir-based STR as the active comparator |
| [NCT03299049](https://clinicaltrials.gov/study/NCT03299049) | Phase 3 | Active, not recruiting | 1,049 | ATLAS-2M: cabotegravir LA + rilpivirine LA every 8 vs. every 4 weeks vs. current ART (including ABC-based regimens); largest ongoing HIV maintenance trial |
| [NCT02893488](https://clinicaltrials.gov/study/NCT02893488) | Phase 1 | Completed | 20 | Relative bioavailability study of dispersible DTG/ABC/3TC tablet under multiple dosing conditions; directly supports development of pediatric-appropriate formulation |
| [NCT00197145](https://clinicaltrials.gov/study/NCT00197145) | Phase 3 | Terminated | 24 | CCR5 antagonist GW873140 + ABC-containing optimized background regimen in treatment-experienced HIV patients; terminated early due to insufficient enrollment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11888583](https://pubmed.ncbi.nlm.nih.gov/11888583/) | 2002 | RCT | Lancet | PENTA 5 trial: compared dual NRTI regimens ± protease inhibitor in treatment-naïve HIV-1-infected children; established efficacy and safety of ABC-containing combinations as a pediatric HIV backbone |
| [39742354](https://pubmed.ncbi.nlm.nih.gov/39742354/) | 2024 | RCT Substudy | J Acquir Immune Defic Syndr | IMPAACT 2010/VESTED substudy: high rates of adverse pregnancy outcomes in women with HIV highlight the critical importance of sustained ART in perinatally infected mothers to prevent vertical transmission |
| [29406430](https://pubmed.ncbi.nlm.nih.gov/29406430/) | 2018 | Cohort | J Acquir Immune Defic Syndr | Italian national observational study comparing ABC/3TC vs. TDF/FTC backbone in HIV-positive pregnant women; relevant to congenital HIV prevention by characterising safety of ABC-based regimens during gestation |
| [31441211](https://pubmed.ncbi.nlm.nih.gov/31441211/) | 2019 | Cohort | J Int AIDS Soc | Multisystem impairment (neurocognitive, cardiovascular, respiratory, renal) in South African adolescents with perinatally acquired HIV on long-term ART; informed ongoing monitoring requirements |
| [24781315](https://pubmed.ncbi.nlm.nih.gov/24781315/) | 2014 | Cohort | PLoS Medicine | French ANRS perinatal cohort (CO1/CO11): estimated prevalence of birth defects by individual ARV drug exposure in utero, including Abacavir; important safety reference for maternal use |
| [34151853](https://pubmed.ncbi.nlm.nih.gov/34151853/) | 2021 | Case Report | J Neuromuscular Dis | Inflammatory myositis in a 5-year-old girl with congenital HIV on ART; illustrates the need for active toxicity monitoring in pediatric patients on Abacavir-containing regimens |
| [28458904](https://pubmed.ncbi.nlm.nih.gov/28458904/) | 2017 | Case Report | Endocrinol Diabetes Metab Case Rep | Iatrogenic Cushing syndrome from fluticasone furoate interaction with lopinavir/ritonavir in a child receiving Abacavir for congenital HIV; highlights the importance of drug-drug interaction surveillance in pediatric co-management |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs—including the IMPAACT series, PENTA 5, and STRIIVING—demonstrate the safety and efficacy of Abacavir-containing regimens in both pediatric and adult HIV-1 populations. The underlying biology is identical between adult HIV-1 and congenital HIV, ABC/3TC fixed-dose tablets with child-appropriate dispersible formulations already exist, and the evidence base reaches L1. The main guardrails are pharmacogenomic screening and pediatric-specific safety monitoring, both of which are implementable.

**To proceed, the following is needed:**

- **HLA-B\*5701 genotyping** mandatory before initiating Abacavir in any patient, including neonates and young infants, to prevent potentially fatal hypersensitivity syndrome
- **Pediatric formulation verification**: confirm dispersible tablet availability and weight-based dosing tables for the target age group (particularly infants under 3 months)
- **Neonatal/infant PK data review**: pharmacokinetic parameters in the youngest age groups differ substantially from older children; dosing must be validated against current WHO and IMPAACT guidelines
- **Long-term safety monitoring plan**: covering neurodevelopmental, metabolic, cardiovascular, and renal outcomes for children on lifelong ART from infancy
- **Drug interaction assessment**: evaluate interactions with common co-medications in the pediatric setting (e.g., corticosteroids, antimicrobials, anti-epileptics)
- **TFDA SmPC review**: confirm local regulatory approval status, approved pediatric age range, and any Taiwan-specific dispensing requirements before clinical deployment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

