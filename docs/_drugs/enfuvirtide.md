---
layout: default
title: Enfuvirtide
parent: AI Predictions (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Enfuvirtide: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: HIV-1 infection in treatment-experienced patients who failed or are i…"
---

# Enfuvirtide
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

# Enfuvirtide: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Enfuvirtide is a peptide fusion inhibitor originally used, together with other antiretrovirals, to treat HIV-1 infection in patients whose earlier regimens have failed.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, but there are **0 clinical trials** and only **10 publications**, mostly preclinical studies of next-generation lipopeptide inhibitors rather than enfuvirtide itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection in treatment-experienced patients who failed or are intolerant to protease inhibitor, NNRTI and NRTI regimens |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 98.18% |
| Evidence Level | L3 (class-level preclinical and review literature; no human trials) |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for enfuvirtide is not available in the data compiled for this report. Based on the literature, enfuvirtide (T-20) is a peptide derived from the gp41 HR2 (C-terminal heptad repeat) region. It blocks formation of the six-helix bundle and so prevents fusion of the viral and cell membranes in HIV-1.

SIV is closely related to HIV and uses a similar gp41-mediated fusion mechanism, so a mechanistic rationale exists. There are important caveats, though. Enfuvirtide's sequence is specific to HIV-1, and its activity against SIV and HIV-2 is reduced (PMID 15040537). Most of the supporting studies test next-generation lipopeptide fusion inhibitors (for example LP-52 and cholesterylated peptides) in rhesus macaque and SIV/SHIV models, not enfuvirtide itself. This is class-level preclinical evidence. SIV infection is also an animal-virus indication with no direct human clinical relevance.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32404526](https://pubmed.ncbi.nlm.nih.gov/32404526/) | 2020 | Preclinical (non-human primate) | J Virol | Lipopeptide LP-52 evaluated in SIVmac239-infected rhesus macaques; low-dose monotherapy rapidly reduced plasma viral load. Resistance selection was also assessed |
| [30716118](https://pubmed.ncbi.nlm.nih.gov/30716118/) | 2019 | Preclinical (non-human primate) | PLoS Pathog | Low-dose lipopeptide monotherapy maintained long-term viral suppression in rhesus macaques |
| [29899103](https://pubmed.ncbi.nlm.nih.gov/29899103/) | 2018 | Preclinical (non-human primate) | J Virol | LP-50 and LP-51, designed from T-20-based LP-40, showed high therapeutic efficacy in rhesus monkey models |
| [30867304](https://pubmed.ncbi.nlm.nih.gov/30867304/) | 2019 | Preclinical (in vitro/in vivo) | J Virol | Cholesterol-modified T-20-based fusion inhibitors with extremely potent, long-lasting anti-HIV-1/2 activity |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | Preclinical (in vitro) | Antivir Ther | Susceptibility of HIV-2, SIV and SHIV to approved anti-HIV-1 drugs; relevant to the reduced activity of enfuvirtide against SIV |
| [26450803](https://pubmed.ncbi.nlm.nih.gov/26450803/) | 2015 | Review | AIDS Rev | Review of HIV-1 group O origin, evolution, pathogenesis and treatment |
| [28356533](https://pubmed.ncbi.nlm.nih.gov/28356533/) | 2017 | Preclinical | J Virol | Lipopeptide LP-19 with potent in vitro, ex vivo and in vivo activity against HIV-1/2 |
| [27795437](https://pubmed.ncbi.nlm.nih.gov/27795437/) | 2017 | Preclinical (in vitro) | J Virol | Helical short-peptide fusion inhibitor with potent activity against HIV-1, HIV-2 and SIV |
| [30089693](https://pubmed.ncbi.nlm.nih.gov/30089693/) | 2018 | Preclinical (in vitro/structural) | J Virol | Structural and functional characterization of fusion inhibitors with extremely potent activity against HIV-1, HIV-2 and SIV |
| [31462566](https://pubmed.ncbi.nlm.nih.gov/31462566/) | 2019 | Preclinical (in vitro) | J Virol | Membrane-anchored short-peptide fusion inhibitor protected target cells from HIV-1, HIV-2 and SIV infection |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000514 (cancelled) | Fuzeon | Not specified | Fuzeon is indicated in combination with other antiretroviral medicinal products for the treatment of HIV-1-infected patients who have... |

## Safety Considerations

- **Drug Interactions**: One moderate-level interaction is recorded, with cobicistat (DDInter).
- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph lists pneumonia as a drug-disease contraindication edge. This comes from graph data, not from the product label, and should be verified against the SmPC.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is an animal-virus infection, and the supporting studies mostly concern next-generation lipopeptide inhibitors rather than enfuvirtide. Enfuvirtide's activity against SIV is reduced, and no clinical trials exist. The only EU authorization is cancelled. The other nine predicted indications (for example feline immunodeficiency, vulvar conditions, oral conditions) have no supporting evidence and no plausible mechanism, so they do not change this decision.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- Safety information (warnings and contraindications) from the Fuzeon SmPC
- Direct data on enfuvirtide itself (not lipopeptide analogues) in SIV models
- Clarification of the research purpose, since SIV has no direct human clinical use, and of whether a research question or a human indication is intended
- Confirmation of the regulatory and supply status of enfuvirtide in the EU, given the cancelled authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

