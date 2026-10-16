---
layout: default
title: Micafungin
parent: Medium Evidence (L3-L4)
nav_order: 405
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-15
description: "Micafungin: predicted new indication Urinary tract infection (disease) (evidence level L3). Approved use: Invasive candidiasis"
---

# Micafungin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Micafungin: From Invasive Candidiasis to Urinary Tract Infection

## One-Sentence Summary

Micafungin is an echinocandin antifungal, originally used to treat invasive candidiasis and to prevent Candida infection in high-risk transplant and neutropenic patients.
The TxGNN model predicts it may be effective for **urinary tract infection** (mainly Candida UTI/candiduria), with **no registered clinical trials** and **12 publications** (mostly case reports, case series and small cohorts) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Invasive candidiasis; oesophageal candidiasis; prophylaxis of Candida infection in allogeneic haematopoietic stem-cell transplantation or prolonged neutropenia |
| Predicted New Indication | Urinary tract infection (disease) |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L3 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, micafungin is an echinocandin that inhibits fungal 1,3-beta-D-glucan synthase and is fungicidal against most Candida species. Its efficacy in invasive candidiasis is established.

Candida UTI (candiduria) is a fungal infection within the drug's spectrum, so the prediction is mechanistically plausible. Echinocandins have traditionally been considered poor options for urinary infections because little drug is excreted in urine. However, reports suggest urinary micafungin levels can exceed the MICs of many Candida species (PMID 27424599). This is especially relevant for fluconazole-resistant organisms such as *C. krusei* and *C. glabrata*, and for patients in whom amphotericin B or flucytosine is undesirable, such as transplant recipients.

The other predicted indications are not supported. Bacterial urethritis (Ureaplasma, gonococcal), urogenital tuberculosis, xanthogranulomatous pyelonephritis and uterine inflammatory disease are bacterial, and bacteria lack the drug's target. The mesothelioma and pleural tumour predictions have no mechanistic or clinical basis and are likely artifacts of knowledge-graph clustering. This report therefore focuses on the top-ranked prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35146837](https://pubmed.ncbi.nlm.nih.gov/35146837/) | 2022 | Cohort | Pediatr Int | Outcomes of micafungin for hospital-acquired Candida UTI in critically ill children, including success rates by Candida species |
| [27587066](https://pubmed.ncbi.nlm.nih.gov/27587066/) | 2016 | Cohort | Int Urol Nephrol | Rates of candiduria elimination in hospitalized patients treated with micafungin |
| [27424599](https://pubmed.ncbi.nlm.nih.gov/27424599/) | 2016 | PK study / case series | Int J Antimicrob Agents | Six UTI cases treated successfully, four with fluconazole-resistant Candida; urinary micafungin levels were sufficient |
| [26937340](https://pubmed.ncbi.nlm.nih.gov/26937340/) | 2016 | Case series | Med Mycol Case Rep | Five candiduria cases; fungal clearance within 30 days of completing treatment |
| [31111613](https://pubmed.ncbi.nlm.nih.gov/31111613/) | 2019 | Case report + review | Transpl Infect Dis | Chronic *C. krusei* UTI eradicated with increased-dose micafungin in a liver and kidney transplant recipient |
| [38827222](https://pubmed.ncbi.nlm.nih.gov/38827222/) | 2024 | Case report | Front Pediatr | *C. glabrata* urinary infection in a premature neonate treated with micafungin |
| [40765059](https://pubmed.ncbi.nlm.nih.gov/40765059/) | 2025 | Case report | J Pharm Health Care Sci | *C. glabrata* pyelonephritis and bacteraemia in a patient on an SGLT2 inhibitor, treated successfully with micafungin |
| [38681664](https://pubmed.ncbi.nlm.nih.gov/38681664/) | 2024 | Case report | Med Mycol Case Rep | Renal fungus ball caused by *C. glabrata* (micafungin-sensitive), managed with antifungal therapy plus endoscopic extraction |
| [29109159](https://pubmed.ncbi.nlm.nih.gov/29109159/) | 2018 | Cohort | Antimicrob Agents Chemother | Overtreatment of asymptomatic candiduria is common; guidelines do not recommend antifungals for it |

These studies are small and non-randomized. No prospective randomized evidence is available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000734 (cancelled) | Mycamine | Not specified | Invasive candidiasis, oesophageal candidiasis, and prophylaxis of Candida infection in allogeneic HSCT or prolonged neutropenia (adults, adolescents, children, neonates)... |

## Safety Considerations

- **Label warning on liver tumours**: The approved indication text states that the decision to use micafungin should consider a potential risk of liver tumours, so it should be used only when other antifungals are not appropriate.
- **Knowledge-graph contraindication signals** (not label text): kidney disease and pyoureter. These deserve attention given the urinary-tract setting.
- **Drug interactions** (5 moderate-level interactions): amphotericin B, nitisinone, everolimus, ribociclib, sirolimus.

Please refer to the SmPC for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link for Candida UTI is plausible, and small case series and cohorts report successful treatment, including in fluconazole-resistant infections. However, the evidence is limited to observational data with no registered trials or randomized evidence. The only EU authorization is cancelled, and the label's liver-tumour warning and the kidney-related contraindication signals require careful weighing. The other nine predictions have no mechanistic or clinical support.

**To proceed, the following is needed:**
- The SmPC warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism-of-action data
- A systematic review of the candiduria and Candida UTI literature, followed by a prospective study comparing micafungin with standard therapy
- Pharmacokinetic data on urinary concentrations to define dosing, especially in renal impairment
- Clarification of the regulatory status given the cancelled EU authorization
- A defined patient population (for example, fluconazole-resistant symptomatic Candida UTI) to avoid overtreating asymptomatic candiduria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

