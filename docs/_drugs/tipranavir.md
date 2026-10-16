---
layout: default
title: Tipranavir
parent: AI Predictions (L5)
nav_order: 617
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tipranavir: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: HIV-1 infection in highly pretreated adults and adolescents aged 12 y…"
---

# Tipranavir
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

# Tipranavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Tipranavir is a non-peptidic HIV-1 protease inhibitor, originally used (together with low-dose ritonavir) to treat HIV-1 infection in highly pretreated patients whose virus is resistant to multiple protease inhibitors.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, but **no clinical trials and no publications** currently support this prediction. The prediction rests on model output only, and the disease is an animal-model condition rather than a human indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection in highly pretreated adults and adolescents aged 12 years and older with virus resistant to multiple protease inhibitors (used with low-dose ritonavir) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, tipranavir is a non-peptidic HIV-1 protease inhibitor. Its efficacy in HIV-1 infection is supported by two phase III studies in highly pretreated adults and one phase II study in adolescents.

Simian immunodeficiency virus (SIV) is a closely related lentivirus with a homologous protease, so activity is biologically plausible. However, SIV infection is a disease of nonhuman primates, used as an animal model, and is not a human clinical indication. The very high TxGNN score most likely reflects how close the term sits to the approved HIV indication in the disease ontology rather than independent evidence.

Other top-ranked predictions are of similar or lower value:
- **Feline acquired immunodeficiency syndrome** (score 99.99%): a veterinary condition. The feline virus protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity, so cross-activity is uncertain.
- **Congenital HIV** and **AIDS related complex** (score 99.83%, Evidence Level L4): essentially the same disease as the approved HIV-1 indication. These are extensions or nomenclature overlaps rather than true repurposing. Evidence for children younger than 12 years is lacking.
- **Obsolete familial combined hyperlipidemia**: protease inhibitors tend to raise triglycerides and cholesterol, so the drug would be expected to worsen this condition. The prediction is likely spurious.
- **Neurodevelopmental disorder, prostate fibroma, Brenner tumor and benign reproductive neoplasms**: no plausible mechanistic link was identified, and these appear to be graph-embedding artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000631 (cancelled) | Aptivus | Not specified | Aptivus, co-administered with low-dose ritonavir, is indicated for combination antiretroviral treatment of HIV-1 infection in highly pretreated adults and adolescents 12 years of age or older with virus resistant to... |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (derived from drug-disease relationships in the TxGNN knowledge graph, not from label text): liver failure, liver disease, hepatitis, chronic hepatitis B and C virus infection, gallbladder disease, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, blood coagulation disease, hemophilia, hypertriglyceridemia, hyperbilirubinemia (including Gilbert syndrome), injury, brain neoplasm, and intracranial hemorrhage.
- **Drug Interactions**: 100 interactions were found in the interaction database. The following are examples from the 20 retrieved:
  - **Major**: acetylsalicylic acid, eluxadoline
  - **Moderate**: antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, linagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, albiglutide, dulaglutide), dexamethasone, clarithromycin, loperamide, eliglustat, cholic acid, magnesium oxide, topical metronidazole

Please refer to the SmPC for the label warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (Evidence Level L5). SIV infection is an animal-model disease with no human indication. In addition, the only EU authorization has been cancelled, and the drug carries significant hepatic and bleeding safety concerns.

**To proceed, the following is needed:**
- Retrieval and review of the SmPC warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data for tipranavir
- Preclinical or literature evidence of tipranavir activity against SIV, if the animal-model direction is of interest
- A decision on whether the human HIV-related predictions (congenital HIV, AIDS related complex) are worth pursuing, since they largely overlap with the existing indication
- Confirmation of the current regulatory and availability status in the EU
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

