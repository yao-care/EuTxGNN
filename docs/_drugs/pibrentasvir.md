---
layout: default
title: Pibrentasvir
parent: AI Predictions (L5)
nav_order: 486
evidence_level: L5
indication_count: 10
---

# Pibrentasvir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Pibrentasvir: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

Pibrentasvir is an HCV NS5A inhibitor, used in the glecaprevir/pibrentasvir combination (Maviret) to treat chronic hepatitis C.
The TxGNN model predicts it may be effective for **hepatitis B virus infection**, but **no clinical trials** and **20 publications** have been found, and none of them tests activity against hepatitis B.
The prediction is therefore supported by the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus (HCV) infection in adults and children aged 3 years and older |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. From known pharmacology, pibrentasvir is an inhibitor of HCV NS5A, a viral protein with no counterpart in hepatitis B virus (HBV). Its efficacy in HCV is well established, but that efficacy does not carry over to HBV.

HBV is a DNA virus that replicates through reverse transcription, which is very different from HCV, an RNA virus. The high score (0.998) most likely reflects the closeness of "viral hepatitis" terms in the knowledge graph rather than a shared drug target. The literature retrieved concerns HCV (glecaprevir/pibrentasvir in HCV, paediatric HCV, DAA retreatment), and none of it tests HBV activity. HBV reactivation during HCV antiviral therapy is a safety concern, not a sign of efficacy.

Other predictions in the list were also reviewed. They carry the same weakness: HIV, hepatitis E, hepatitis A, Omsk haemorrhagic fever, Kyasanur forest disease and others all lack a plausible target match. The HIV-related trials enrol HIV/HCV-coinfected patients and measure HCV cure, so they show safe HCV treatment in people living with HIV, not anti-HIV activity.

## Clinical Trial Evidence

Currently no related clinical trials registered for hepatitis B virus infection.

## Literature Evidence

None of the publications below evaluates pibrentasvir against HBV. They concern HCV and are listed as background only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Cohort | J Viral Hepat | Real-world glecaprevir/pibrentasvir use in HCV patients with severe renal impairment (CKD stage 4-5) in Taiwan |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Review | Lancet Gastroenterol Hepatol | HCV infection in children and adolescents; direct-acting antivirals have transformed treatment |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | Management of paediatric viral hepatitis; HBV treatment is described as far from curative |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | Retreatment of HCV patients after DAA failure |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | Diagnosis and treatment of chronic hepatitis C in primary care |
| [42127258](https://pubmed.ncbi.nlm.nih.gov/42127258/) | 2026 | Review | Top Antivir Med | CROI 2026 viral hepatitis overview; general content, no drug-specific data |
| [31129632](https://pubmed.ncbi.nlm.nih.gov/31129632/) | 2019 | Case report | BMJ Case Rep | Glecaprevir/pibrentasvir-associated acute liver injury in a patient with chronic HCV and no HBV co-infection |
| [34344581](https://pubmed.ncbi.nlm.nih.gov/34344581/) | 2021 | Case report | J Infect Chemother | Glecaprevir/pibrentasvir for HCV exacerbation caused by a daratumumab-based regimen |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004430 (cancelled) | Maviret | Not specified | Chronic hepatitis C virus (HCV) infection in adults and children aged 3 years and older. Maviret coated granules is indicated for... |

## Safety Considerations

Please refer to the SmPC for safety information. No drug-interaction records were found in the data compiled for this report.

One signal from the literature is relevant to this prediction: HBV reactivation during HCV direct-acting antiviral therapy is a recognised safety concern, so HBV status should be checked before treatment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Pibrentasvir targets HCV NS5A, which HBV does not have, and no trial or publication tests it against HBV. The high TxGNN score appears to reflect network proximity among viral hepatitis terms and is not enough to justify further investment.

**To proceed, the following is needed:**
- In vitro antiviral testing against HBV, to see whether any activity exists at all
- Mechanism of action data and EMA label warnings and contraindications (currently missing)
- A review of which other predicted indications, if any, warrant a separate assessment; none of the other nine currently show a plausible mechanism or direct evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

