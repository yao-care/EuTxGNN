---
layout: default
title: Lopinavir
parent: Medium Evidence (L3-L4)
nav_order: 376
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Lopinavir: predicted new indication Simian immunodeficiency virus infection (evidence level L4). Approved use: HIV-1 infection in adults…"
monitor_inn: "Lopinavir"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "hepatitis B virus infection", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
---

# Lopinavir
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

# Lopinavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Lopinavir is an HIV protease inhibitor, used together with ritonavir and other antiretrovirals to treat HIV-1 infection.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, a primate lentivirus infection.
Support is limited to **3 preclinical macaque publications** and **no registered clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection in adults, adolescents and children (in combination with other antiretrovirals) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (both authorizations cancelled) |
| Number of Authorizations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, lopinavir is an HIV-1 protease inhibitor that blocks cleavage of the Gag-Pol polyprotein, which the virus needs to mature. Its efficacy in HIV-1 infection is established.

Simian immunodeficiency virus (SIV) is a lentivirus closely related to HIV-1. Its protease is similar enough that antiviral activity is plausible. However, the supporting studies are in macaques, where SIV and SHIV infection serve as preclinical models of HIV. They show the drug works in a research model but do not create a new human therapeutic indication beyond the approved HIV-1 use.

Other predictions in the list have weaker support. Feline AIDS is a veterinary condition outside the scope of human repurposing. Several rare tumors and a rare neurodevelopmental disorder have a high model score but no plausible mechanism, no trials and no literature. Some predictions describe conditions already within the approved HIV-1 indication, such as congenital HIV and AIDS-related complex. Hepatitis B virus infection and HPV-related lesions are discussed in the conclusion.

## Clinical Trial Evidence

Currently no related clinical trials are registered for simian immunodeficiency virus infection.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Preclinical (macaque) | J Virol | Rapid viral decay in SIV-infected macaques given quadruple antiretroviral therapy |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Preclinical (SHIV in rhesus macaque) | Microbes Infect | A SHIV carrying the HIV-1 protease gene was built as a tool to test protease inhibitors in vivo |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Preclinical (macaque) | J Virol Methods | Oral HAART including lopinavir/ritonavir and its effect on the CD8 subset in chronically SHIV-infected monkeys |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000368 (cancelled) | Kaletra | Not specified | Treatment of HIV-1 infected adults, adolescents and children aged from 14 days and older, in combination with other antiretrovirals... |
| EMEA/H/C/004025 (cancelled) | Lopinavir/Ritonavir Viatris (previously Ritonavir Mylan) | Not specified | Treatment of HIV-1 infected adults, adolescents and children above the age of 2 years, in combination with other antiretrovirals... |

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC for safety information.

- **Contraindication signals from the knowledge graph (not label text):** long QT syndrome, torsades de pointes, heart conduction disease, atrioventricular block, pancreatitis, liver disease, cirrhosis, chronic hepatitis B and C, hyperglycemia and diabetes, hypertriglyceridemia, hyperbilirubinemia, myocardial ischemia and cardiomyopathy. These need confirmation against the SmPC.
- **Drug interactions:** 65 interactions were recorded. Major ones include dolasetron and papaverine. Moderate ones include levofloxacin, ondansetron, palonosetron, metformin, dapagliflozin, acarbose, famotidine and several laxatives.
- **Literature-reported concerns:** adrenal dysfunction in infants after prenatal or postnatal exposure, and CYP3A-mediated interactions (for example, iatrogenic Cushing syndrome with fluticasone).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for simian immunodeficiency virus infection is three macaque studies. There are no clinical trials, and it offers no human indication beyond the approved HIV-1 use. In the EU, both authorizations are cancelled.

Other predictions in the list were assessed as follows:
- **Congenital HIV and AIDS-related complex:** These are effectively on-label HIV uses (Proceed with Guardrails), not true repurposing.
- **Hepatitis B virus infection:** Lopinavir has no direct anti-HBV activity. The signal reflects HIV/HBV co-infection management (Research Question).
- **HPV-related benign reproductive lesions:** One small single-arm proof-of-concept trial supports a hypothesis only (Research Question).

**To proceed, the following is needed:**
- Mechanism of action data and EMA label warnings and contraindications, to complete safety screening
- Clarification of whether a non-human primate or veterinary prediction has any value for a human development program
- For any HPV-related lesion direction, a controlled trial confirming the single-arm proof-of-concept result
- Confirmation of current EU availability, since both authorizations are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

