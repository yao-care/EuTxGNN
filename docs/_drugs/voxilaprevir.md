---
layout: default
title: Voxilaprevir
parent: Medium Evidence (L3-L4)
nav_order: 679
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Voxilaprevir: predicted new indication Hepatitis B virus infection (evidence level L4). Approved use: Chronic hepatitis C virus (HCV) infection in patients aged 12 years a…"
monitor_inn: "voxilaprevir"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection", "Omsk hemorrhagic fever", "Kyasanur forest disease", "HIV infectious disease", "chronic hepatitis B virus infection", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome"]
---

# Voxilaprevir
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

## Voxilaprevir: From Chronic Hepatitis C to Hepatitis B Virus Infection
{: .text-alpha }

## One-Sentence Summary

Voxilaprevir is an HCV NS3/4A protease inhibitor, originally used (as part of the Vosevi combination) to treat chronic hepatitis C virus infection.
The TxGNN model predicts it may be effective for **hepatitis B virus infection**, but **no clinical trials** and **9 publications** are linked to this prediction, and none of those publications studies anti-HBV activity. The evidence is indirect only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus (HCV) infection in patients aged 12 years and older and weighing at least 30 kg |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, voxilaprevir is an HCV NS3/4A protease inhibitor used in the Vosevi combination, and its efficacy in chronic hepatitis C is well established.

The prediction is not mechanistically supported. HBV has no NS3/4A protease. It replicates through a reverse transcriptase/polymerase and a different replication cycle, so there is no plausible direct target overlap. The high TxGNN score most likely reflects network proximity between hepatitis C and other hepatotropic viral diseases in the knowledge graph, not a shared drug target.

The retrieved literature concerns HCV retreatment, and HBV appears only incidentally (drug pricing, dental bloodborne-infection markers, a conference report). There is no direct evidence of anti-HBV activity. The other top-ranked predictions (hepatitis E, hepatitis A, flavivirus diseases, HIV and related) are similarly weak: none has a clear mechanistic link, and the trials linked to them are HCV or HIV/HCV studies.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for hepatitis B virus infection.

---

## Literature Evidence

None of these publications evaluates voxilaprevir against HBV. They describe HCV treatment, and HBV is mentioned only incidentally.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | Single-arm trial (cohort) | Lancet Gastroenterol Hepatol | Sofosbuvir-velpatasvir-voxilaprevir re-treatment of HCV after prior DAA failure in Rwanda (SHARED-3) |
| [36535062](https://pubmed.ncbi.nlm.nih.gov/36535062/) | 2022 | Cohort | J Gastrointestin Liver Dis | Real-world efficacy and safety of sofosbuvir-velpatasvir-voxilaprevir in Romanian genotype 1b patients who did not respond to prior DAAs |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | Retreatment of HCV patients after DAA failure |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | Pharmacokinetic and pharmacodynamic considerations of HCV therapy, 2019 update |
| [40611935](https://pubmed.ncbi.nlm.nih.gov/40611935/) | 2025 | Cohort | J Clin Exp Hepatol | Resistance-associated substitutions and predictors of DAA treatment failure in an HCV elimination programme |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | Preclinical/Virology | Hepatology | Evolution and persistence of HCV protease inhibitor resistance variants |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Conference report | AIDS Rev | International Conference on Viral Hepatitis 2017; HBV and HCV burden and treatment discussed |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Economic analysis | Ann Hepatol | Global comparison of HBV and HCV drug pricing |
| [41570233](https://pubmed.ncbi.nlm.nih.gov/41570233/) | 2025 | Cross-sectional | Vopr Virusol | Prevalence of HIV, HBV and HCV markers among dental patients |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004350 | Vosevi | Not specified | Treatment of chronic hepatitis C virus (HCV) infection in patients aged 12 years and older and weighing at least 30 kg. (see sections 4.2, 4.4 and 5.1). |

The authorization is cancelled, so there is currently no valid EU marketing authorization.

---

## Safety Considerations

- **Drug Interactions**: 19 interactions were identified in DDInter. Major-level interactions are:
  - Rosuvastatin
  - Edoxaban
  - Cyclosporine

  The remaining 16 are Moderate level, including cobicistat, apixaban, eltrombopag, ethinylestradiol, obeticholic acid, eluxadoline, artesunate, afatinib, bosutinib, cobimetinib, idelalisib, lapatinib, lenvatinib, olaparib, pazopanib and teriflunomide.
- **Other**: HBV reactivation is a known risk during HCV direct-acting antiviral therapy. This matters for any use of the drug in patients with HBV.

Please refer to the SmPC for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there is no plausible mechanism (HBV lacks an NS3/4A protease target), no clinical trials and no literature showing anti-HBV activity. The evidence is indirect only. The EU authorization is also cancelled.

**To proceed, the following is needed:**
- Mechanism of action data for voxilaprevir
- In vitro evidence of anti-HBV activity, for example in HBV replication cell models, to establish any biological basis
- SmPC safety information (warnings and contraindications), especially on HBV reactivation
- A review of whether the other predicted indications (e.g., the HIV/HCV co-infection evidence) offer a more tractable path, since those results concern HCV treatment, not new activity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

