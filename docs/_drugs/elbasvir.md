---
layout: default
title: Elbasvir
parent: Medium Evidence (L3-L4)
nav_order: 214
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Elbasvir: predicted new indication Hepatitis B virus infection (evidence level L4). Approved use: Chronic hepatitis C (CHC) in adults and paediatric patients 12 years…"
monitor_inn: "Elbasvir"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever", "Kyasanur forest disease", "HIV infectious disease", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Elbasvir
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

## Elbasvir: From Chronic Hepatitis C to Hepatitis B Virus Infection
{: .text-alpha }

## One-Sentence Summary

Elbasvir is an HCV NS5A inhibitor, originally used in combination with grazoprevir to treat chronic hepatitis C.
The TxGNN model predicts it may be effective for **hepatitis B virus infection**, but the **2 linked clinical trials** and the published literature all concern hepatitis C, not hepatitis B.
The prediction is therefore supported only by the model score, not by direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C (CHC) in adults and paediatric patients 12 years and older weighing at least 30 kg |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Elbasvir inhibits the HCV NS5A protein, which is involved in viral replication and assembly. Detailed mechanism of action data are not available in the data compiled for this report, so this description relies on the known drug class. It is used together with grazoprevir, an NS3/4A protease inhibitor.

Hepatitis B and hepatitis C are both chronic viral liver infections. However, HBV has no NS5A homolog, so a direct mechanistic link is not established. The high score probably reflects the drug's closeness to other hepatitis viruses in the knowledge network rather than a real shared target.

The other predictions are weaker or different in nature:
- **Hepatitis E virus infection:** a 2026 in vitro study reports that elbasvir inhibits HEV internalization and, with ribavirin, achieves sustained viral suppression. This is the most interesting mechanistic signal, but it is preclinical, and the study design and strength of the result need verification.
- **Hepatitis A, HIV, and others:** the linked trials are HCV or HCV/HIV co-infection studies. They do not show activity against the predicted disease.
- **Flaviviruses (Omsk hemorrhagic fever, Kyasanur forest disease), veterinary conditions, and a rare neurodevelopmental disorder:** computational predictions only, with no supporting data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02940496](https://clinicaltrials.gov/study/NCT02940496) | Phase 2 | Completed | 15 | Pembrolizumab as second-line therapy in HCV-positive and HCV-negative advanced hepatocellular carcinoma. Elbasvir is not the study drug, and there is no HBV endpoint. |
| [NCT02115321](https://clinicaltrials.gov/study/NCT02115321) | Phase 2/3 | Completed | 40 | Grazoprevir + elbasvir in HCV genotype 1, 4 or 6 with Child-Pugh B cirrhosis. It supports the approved HCV indication, not HBV. |

Neither trial provides evidence on hepatitis B.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34902265](https://pubmed.ncbi.nlm.nih.gov/34902265/) | 2022 | Cohort (phase 4, single-arm) | Antimicrob Agents Chemother | Grazoprevir/elbasvir for 12 weeks in liver or kidney transplant recipients with HCV genotype 1b. |
| [32039536](https://pubmed.ncbi.nlm.nih.gov/32039536/) | 2020 | Real-world study | J Viral Hepat | Real-world elbasvir/grazoprevir in Taiwan, focused on liver and renal adverse effects. |
| [32306039](https://pubmed.ncbi.nlm.nih.gov/32306039/) | 2020 | Clinical study | J Antimicrob Chemother | Grazoprevir/elbasvir for recently acquired HCV genotype 1 or 4 in men who have sex with men. |
| [29077864](https://pubmed.ncbi.nlm.nih.gov/29077864/) | 2018 | Randomized study | Clin Infect Dis | Sofosbuvir + grazoprevir/elbasvir + ribavirin retreatment after failure of earlier direct-acting antivirals (ANRS HC34 REVENGE). |
| [26904396](https://pubmed.ncbi.nlm.nih.gov/26904396/) | 2016 | Review | Acta Pharm Sin B | Overview of direct-acting anti-HCV agents. |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | Pharmacokinetic and pharmacodynamic considerations for HCV therapy (2019 update). |
| [25529080](https://pubmed.ncbi.nlm.nih.gov/25529080/) | 2015 | Review | Liver Int | Eradication of HCV and the prospect of a cure for HBV; general viral hepatitis perspective, no elbasvir-specific HBV data. |

The literature is mostly about hepatitis C. No publication shows HBV efficacy of elbasvir.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004126 (cancelled) | Zepatier | Not specified | Chronic hepatitis C (CHC) in adult and paediatric patients 12 years of age and older who weigh at least 30 kg... |

---

## Safety Considerations

- **Drug Interactions:** 15 interactions were identified. One is rated **Major**: ozanimod. The other 14 are rated Moderate, including warfarin, dicoumarol, betrixaban, lusutrombopag, alpelisib, binimetinib, ivosidenib, talazoparib, elagolix, griseofulvin, aminoglutethimide, metreleptin, somatrem, and somatotropin.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TxGNN score for hepatitis B is high, but HBV has no NS5A target and there is no HBV-specific clinical or literature evidence for elbasvir. The linked trials and papers are all about HCV, so this is a model prediction only (L4 at most).
- The product's only EU authorization is cancelled.

**To proceed, the following is needed:**
- In vitro evidence of anti-HBV activity (for example, in HBV replication cell systems).
- Mechanism of action data and a proposed target in HBV biology.
- Safety information from the SmPC (warnings and contraindications).
- Verification of the 2026 hepatitis E study (PMID 42347219). It may be a more promising research question than HBV.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

