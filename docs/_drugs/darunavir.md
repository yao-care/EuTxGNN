---
layout: default
title: Darunavir
parent: AI Predictions (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Darunavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV-1 infection…"
monitor_inn: "Darunavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
---

# Darunavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Darunavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Darunavir is an HIV-1 protease inhibitor, originally used (boosted with ritonavir or cobicistat) in combination with other antiretrovirals to treat HIV-1 infection.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but **no clinical trials and no publications** currently support this specific prediction (evidence level L5, model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection, in combination with other antiretroviral medicinal products (adults and paediatric patients aged 3 years and over) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, darunavir is a protease inhibitor used against HIV-1, and its efficacy in HIV-1 infection is established.

Feline immunodeficiency virus (FIV) is a lentivirus whose protease is related to HIV-1 protease, so a protease inhibitor could plausibly act on it. However, darunavir was optimized against HIV-1 protease, and no cross-activity data against FIV protease are available. The high score (0.9997) is a model prediction only and should not be read as evidence of efficacy.

The same score level is shared by a closely related prediction, **simian immunodeficiency virus (SIV) infection**. It has four preclinical macaque studies of combination antiretroviral regimens, but darunavir's individual contribution cannot be determined from them. SIV is not a human disease, so this is mainly useful as a translational model.

Other predictions with human-relevant literature (congenital HIV, AIDS related complex) fall within or close to the already approved HIV-1 indication, so they are extensions of use rather than true repurposing. Several other high-scoring predictions (a rare neurodevelopmental disorder, benign prostate and ovarian tumors) have no plausible mechanistic link and appear to be knowledge-graph artifacts. "Obsolete familial combined hyperlipidemia" is also unsupported, because protease inhibitors tend to worsen lipid profiles rather than treat them.

## Clinical Trial Evidence

Currently no related clinical trials registered for feline acquired immunodeficiency syndrome.

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

For the closely related SIV infection prediction (indirect, preclinical only):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Preclinical (animal) | PLoS Pathogens | Highly intensified multidrug ART induced long-term viral suppression and restricted the viral reservoir in SIV-infected macaques |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Preclinical (animal) | AIDS Res Hum Retroviruses | Comparison of coformulated injectable ART regimens in SIV-infected rhesus macaques |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Preclinical (animal) | PLoS One | Suppressive ART plus the HDAC inhibitor SAHA in SIV-infected Chinese rhesus macaques |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Preclinical (animal) | AIDS | Auranofin restricted the viral reservoir in a monkey AIDS model |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004068 | Darunavir Viatris (previously Darunavir Mylan) | Not specified | Darunavir co-administered with low dose ritonavir, in combination with other antiretrovirals, for HIV-1 infection... (cancelled) |
| EMEA/H/C/000707 | Prezista | Not specified | Prezista co-administered with low dose ritonavir or cobicistat, in combination with other antiretrovirals, for HIV-1... (cancelled) |
| EMEA/H/C/004273 | Darunavir Krka | Not specified | Darunavir Krka 400 mg and 800 mg co-administered with low dose ritonavir, in combination with other antiretrovirals... (cancelled) |

## Safety Considerations

- **Disease-related cautions (from the knowledge graph, not label text)**: Contraindication links were recorded for liver failure, liver disease, cirrhosis, gallbladder disease, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, chronic hepatitis B and C infection, hypertriglyceridemia, and hemophilia.
- **Drug Interactions**: 100 interactions were identified. Most listed are moderate, including antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, saxagliptin, canagliflozin, dapagliflozin, chlorpropamide, acetohexamide), corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), aprepitant, and clarithromycin. **Cisapride is a major interaction.**

Please refer to the SmPC for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no trials or publications for feline AIDS, no cross-activity data against FIV protease, and no valid EU marketing authorization for darunavir at present. The SIV macaque studies are indirect and do not isolate darunavir's effect.

**To proceed, the following is needed:**
- In vitro data on darunavir activity against FIV protease and replication
- Veterinary pharmacokinetic and safety data in cats (the compiled data cover human use only)
- Mechanism of action data, which is currently unavailable
- Label warnings and contraindications from the current SmPC, which are missing from the compiled data
- Clarification of the cancelled EU status, for any human-use extension such as CNS penetration or perinatal HIV-1 treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

