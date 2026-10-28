---
layout: default
title: Ritonavir
parent: AI Predictions (L5)
nav_order: 530
evidence_level: L5
indication_count: 3
monitor_inn: "Ritonavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-28
description: "Ritonavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV-1 infection…"
---

# Ritonavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Ritonavir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Ritonavir is an antiretroviral medicine approved in the EU, used together with other antiretroviral agents to treat HIV-1 infection.
The TxGNN model's top-ranked prediction is **feline acquired immunodeficiency syndrome**, a veterinary disease, and there are **0 clinical trials** and **0 publications** that directly study it.
The evidence therefore rests on the model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection, in combination with other antiretroviral agents (adults and children aged 2 years and older) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 2 of 2) |
| Number of Authorizations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ritonavir is known as an HIV-1 protease inhibitor, which blocks the cleavage of viral polyproteins needed to produce mature virus particles. Feline immunodeficiency virus (FIV) is a lentivirus related to HIV, so a general mechanistic rationale exists.

However, FIV protease differs structurally from HIV-1 protease, and HIV-1 protease inhibitors are expected to have limited activity against it. The very high score (0.9992) is nearly identical to that of the other top predictions. It most likely comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. In addition, feline AIDS is a veterinary condition and falls outside the scope of human drug repurposing.

Two other predictions were also reviewed:
- **Simian immunodeficiency virus (SIV) infection** (score 0.9992): Preclinical studies exist, including in vitro work showing ritonavir inhibits SIVmac239 (EC50 about 13 nM, versus about 25 nM for HIV-1). SIV is an animal model of HIV and adds no new human indication. It was not the primary prediction, and its evidence is preclinical and indirect. Because these studies are of SIV, not of feline AIDS, they do not raise the evidence level for the primary prediction.
- **A rare neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 0.9992): No plausible mechanistic link and no studies were found.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

For context, the closest related literature concerns SIV infection (a different disease), and it is preclinical:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro | Antimicrob Agents Chemother | SIVmac239 was inhibited by ritonavir (EC50 about 13 nM), comparable to HIV-1 (about 25 nM) |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antivir Ther | Activity of approved anti-HIV drugs tested against HIV-2, SIV and SHIV strains |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal study | J Virol | Rapid viral decay in SIV-infected macaques given quadruple antiretroviral therapy |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal study | PLoS Pathog | Intensified multidrug ART gave long-term viral suppression in a simian AIDS model |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal study | J Virol Methods | Oral HAART including lopinavir/ritonavir in SHIV-infected macaques; effect on CD8 subset |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004549 | Ritonavir Viatris (previously Ritonavir Mylan) | Not specified | HIV-1 infection, in combination with other antiretroviral agents (adults and children aged 2 years and older) |
| EMEA/H/C/000127 | Norvir | Not specified | HIV-1 infection, in combination with other antiretroviral agents (adults and children aged 2 years and older) |

## Safety Considerations

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC for authoritative safety information.

- **Contraindication relations recorded in the knowledge graph** (these come from a knowledge graph, not from label text): long QT syndrome, torsades de pointes, pancreatitis, liver disease, cirrhosis, gallbladder disease, diabetes mellitus, hyperglycemia, diabetic ketoacidosis, hypertriglyceridemia, hyperbilirubinemia, gout, coronary artery disease, myocardial ischemia, atrioventricular block, cardiomyopathy, sudden cardiac arrest, and hemophilia, among others.
- **Drug Interactions**: 100 interactions were found. Examples of those rated **Major** include loperamide, triamcinolone and budesonide. Many **Moderate** interactions were also listed, for example with metformin, dexamethasone, hydrocortisone, clarithromycin, bupropion, and aprepitant.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is a veterinary disease with no clinical trials and no directly relevant literature, so the evidence level is L5. The high TxGNN score is likely a network artifact, and the closest supporting data (SIV) are preclinical and add no new human indication beyond the approved HIV-1 use.

**To proceed, the following is needed:**
- A decision on whether veterinary indications are in scope for this program
- Direct evidence of ritonavir activity against FIV protease, if the prediction is pursued
- Detailed mechanism of action data
- Label-based warnings and contraindications from the SmPC, which are needed for any safety screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

