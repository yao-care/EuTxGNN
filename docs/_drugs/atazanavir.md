---
layout: default
title: Atazanavir
parent: AI Predictions (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Atazanavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: Treatment of HIV-1 infected adults and paediatric patients 6 years of…"
---

# Atazanavir
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

# Atazanavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Atazanavir is an HIV protease inhibitor, originally used (boosted with low-dose ritonavir) to treat HIV-1 infection in adults and children.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. The prediction rests on model inference alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of HIV-1 infected adults and paediatric patients 6 years of age and older, in combination with other antiretroviral medicinal products (with low-dose ritonavir) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, atazanavir is an HIV-1 protease inhibitor whose efficacy in HIV-1 infection is established, and mechanistically it may be applicable to related lentiviral infections.

Feline immunodeficiency virus (FIV) is a lentivirus whose protease is homologous to HIV-1 protease, so protease inhibition is biologically plausible. However, FIV protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity, and atazanavir activity against it has not been established. The high TxGNN score reflects a graph-based prediction derived from similarity to HIV, not clinical evidence. Feline AIDS is also a veterinary condition, not a human therapeutic indication.

**Other predictions in the list.** The second-ranked prediction, simian immunodeficiency virus (SIV) infection, has one preclinical paper (PMID 20497048), a non-human primate study of combination antiretroviral therapy. It remains indirect evidence, and it is unclear whether atazanavir was part of the regimen. The congenital HIV and AIDS-related complex predictions largely overlap with the existing HIV-1 label and are context extensions rather than true repurposing. Several other predictions (a rare neurodevelopmental disorder, benign prostate and ovarian tumours, and obsolete familial combined hyperlipidemia) have no identified mechanistic link and look like network artifacts. For hyperlipidemia, HIV protease inhibitors are generally associated with dyslipidemia, so therapeutic use would be counterintuitive and potentially harmful.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction (feline acquired immunodeficiency syndrome).

For reference, the closest related prediction (SIV infection) has the following publication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Animal study (non-human primate) | J Infect Dis | SIV-infected macaques on highly active antiretroviral therapy had reduced central nervous system viral replication and inflammation, but viral DNA persisted. Whether atazanavir was part of the regimen is unclear. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004048 (cancelled) | Atazanavir Viatris (previously Atazanavir Mylan) | Not specified | Atazanavir Viatris, co-administered with low dose ritonavir, is indicated for the treatment of HIV 1 infected adults and paediatric pa... |
| EMEA/H/C/000494 (cancelled) | Reyataz | Not specified | Reyataz capsules, co-administered with low dose ritonavir, are indicated for the treatment of HIV-1 infected adults and paediatric pa... |
| EMEA/H/C/004859 (cancelled) | Atazanavir Krka | Not specified | Atazanavir Krka capsules, co-administered with low dose ritonavir, are indicated for the treatment of HIV-1 infected adults and paedi... |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (derived from drug-disease graph edges, not label text): liver failure, liver disease, gallbladder disease, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, chronic hepatitis B and C virus infection, hemophilia, hyperbilirubinemia (including hereditary forms and Gilbert syndrome), nephrolithiasis, acute urate nephropathy, atrioventricular block, and lactic acidosis.
- **Drug Interactions**: 100 interactions were identified in total. Major-level interactions among those listed include:
  - Acid-lowering agents: famotidine, ranitidine, rabeprazole, omeprazole
  - Corticosteroids: triamcinolone, budesonide
  - Loperamide

  Moderate-level interactions include antidiabetic agents (acarbose, alogliptin, albiglutide, metformin, pioglitazone, acetohexamide), antacids (aluminum hydroxide, calcium carbonate), hydrocortisone, betamethasone, alosetron, and aprepitant.

Please refer to the SmPC for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (feline AIDS) is supported only by a graph-based model score, with no clinical trials or literature, and it is a veterinary indication rather than a human one. All three EU authorizations are also cancelled, which further limits near-term development.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank
- Safety information from the SmPC (warnings and contraindications)
- In vitro data on atazanavir activity against FIV protease, and a veterinary regulatory and development assessment
- Clarification of which atazanavir-containing regimens were used in the SIV macaque study
- If a human-relevant direction is preferred, a focused review of neonatal/infant HIV treatment (the label covers ages 3 months and older for the oral powder and 6 years and older for capsules, which leaves a gap for neonates), using the pregnancy pharmacokinetic data (PMID 24992294) as a starting point
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

