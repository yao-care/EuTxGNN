---
layout: default
title: Rilpivirine
parent: AI Predictions (L5)
nav_order: 504
evidence_level: L5
indication_count: 10
---

# Rilpivirine
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

# Rilpivirine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Rilpivirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) approved for the treatment of HIV-1 infection in humans, often used as part of two-drug regimens with cabotegravir (long-acting injectable) or dolutegravir (oral).
> The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) infection**, a disease of macaques used as a preclinical model for HIV research — not a naturally occurring human condition.
> Support comes from **0 clinical trials** and **4 publications**, all of which are preclinical macaque studies or a mechanism review, with no evidence of a translatable human indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (per clinical trial documentation in evidence pack) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (preclinical/mechanism studies only) |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the DrugBank record for this drug, but clinical trial documentation confirms Rilpivirine is an NNRTI that inhibits HIV-1 reverse transcriptase, and is approved for HIV-1 infection, frequently as part of a two-drug long-acting injectable regimen with cabotegravir.

SIV is the macaque-infecting relative of HIV, and researchers commonly use SIV or chimeric RT-SHIV (SHIV engineered to carry the HIV-1 reverse transcriptase gene specifically so that HIV drugs remain active) as an animal model to study HIV treatment, prevention, and remission strategies. Because Rilpivirine's target enzyme is homologous between the two viruses, it retains antiviral activity in these models — which is almost certainly why the TxGNN knowledge graph links Rilpivirine to SIV infection with such a high score.

However, this connection reflects **research tool use in an animal model**, not a bona fide new clinical indication: SIV infection is not a disease that occurs or is treated in humans, and none of the supporting literature describes SIV as a target condition for drug approval. This is an important distinction from the drug's approved human indication (HIV-1 infection) and should not be read as evidence of a repurposing opportunity in the conventional sense.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Preclinical (macaque) | Nature Communications | Long-acting cabotegravir/rilpivirine plus immune adjunct tested for SHIV remission in early-treated macaques |
| [41370971](https://pubmed.ncbi.nlm.nih.gov/41370971/) | 2026 | Preclinical (macaque) | EBioMedicine | Single-injection long-acting cabotegravir/rilpivirine evaluated as HIV post-exposure prophylaxis in a macaque model |
| [26438501](https://pubmed.ncbi.nlm.nih.gov/26438501/) | 2015 | Preclinical (macaque) | Antimicrobial Agents and Chemotherapy | Low frequency of drug-resistant variants selected by long-acting rilpivirine in RT-SHIV-infected macaques used for PrEP studies |
| [29746267](https://pubmed.ncbi.nlm.nih.gov/29746267/) | 2018 | Review | Current Opinion in HIV and AIDS | Review of cabotegravir (rilpivirine's regimen partner) for antiretroviral therapy and PrEP; mechanistic background only |

## EU Market Information

No marketing authorizations are recorded for Rilpivirine in the evidence pack (0 licenses; market status: not marketed).

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is a macaque-only disease (SIV infection) used as an HIV research model, not an actual human clinical indication, and all supporting evidence is preclinical (no clinical trials, no RCTs). Combined with a Blocking data gap on regulatory safety warnings (TFDA labeling) and a High-severity gap on mechanism of action, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/EMA SmPC warnings, contraindications, and DDI data (Blocking gap DG001)
- Confirmed mechanism-of-action documentation from DrugBank (High gap DG002)
- Re-evaluation of lower-ranked predictions with genuine human clinical relevance (e.g., rank 4 "congenital HIV" and rank 5 "AIDS related complex" have completed Phase 3 human trials, though both substantially overlap with the existing approved HIV-1 indication rather than representing a true new indication)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

