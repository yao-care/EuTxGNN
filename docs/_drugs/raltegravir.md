---
layout: default
title: Raltegravir
parent: Medium Evidence (L3-L4)
nav_order: 488
evidence_level: L4
indication_count: 10
---

# Raltegravir
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Raltegravir: From HIV-1 Infection to Simian Immunodeficiency Virus (SIV) Infection

## One-Sentence Summary

Raltegravir is an HIV-1 integrase strand transfer inhibitor; its established indication is HIV-1 infection, though this evidence pack contains no formal licensing/MOA data confirming this (both flagged as data gaps). The TxGNN model's **top-ranked** prediction is **Simian Immunodeficiency Virus (SIV) Infection**, which the evidence pack's own analysis flags as a species/entity-mapping artifact rather than a translatable human indication — it is supported by only **1 withdrawn clinical trial** (zero enrollment) and **19 mostly preclinical/animal-model publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not currently marketed/licensed in this jurisdiction (no license records); publicly known indication is HIV-1 infection |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a data gap, DG002). Based on known public drug information, Raltegravir is an HIV-1 integrase strand transfer inhibitor, and its efficacy in HIV-1 infection is well established in clinical practice.

SIV is a primate lentivirus that shares the same genus (Lentivirus) as HIV and a homologous integrase domain, so the drug's integrase-inhibition mechanism is plausible in nonhuman primate models — several preclinical studies in this pack do use raltegravir-based ART in SIV-infected rhesus macaques as a research tool. However, **SIV infection is a veterinary/research-model disease, not a human disease**, and does not constitute a clinically translatable repurposing indication. This top-ranked prediction most likely reflects a knowledge-graph entity mapping artifact (HIV/SIV structural similarity in the graph) rather than a genuine repurposing opportunity.

Notably, two lower-ranked but far more clinically credible signals exist further down this evidence pack: **congenital HIV infection** (rank 4, L2, "Proceed with Guardrails") and **AIDS related complex** (rank 5, L2, "Proceed with Guardrails"). Both represent legitimate extensions of raltegravir's existing HIV indication into specific populations (neonatal/pregnancy PMTCT, pediatric use) and disease staging, backed by real Phase 1–4 trials and cohort/pharmacovigilance literature — unlike the SIV prediction, these are not novel repurposing hypotheses but confirmatory extensions of known use, and may warrant a separate evaluation as their own candidates.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | Withdrawn | 0 | Intended to study HIV/SIV viral decay kinetics under integrase-inhibitor ART; trial was withdrawn with zero enrollment, yielding no usable data. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20233398](https://pubmed.ncbi.nlm.nih.gov/20233398/) | 2010 | Preclinical (animal model) | Retrovirology | Established a raltegravir-based ART regimen in SIVmac251-infected macaques, creating an animal model for lentiviral persistence research. |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | Preclinical (mechanistic) | Clin Infect Dis | Raltegravir and dolutegravir shown to exert proadipogenic/profibrotic effects and induce insulin resistance in human/simian adipose tissue models. |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | Preclinical (animal model) | J Virol | Characterized integrase strand-transfer inhibitor resistance mutation profiles in SIVmac239. |
| [24622515](https://pubmed.ncbi.nlm.nih.gov/24622515/) | 2014 | Preclinical (animal model, PrEP) | Sci Transl Med | Topical integrase inhibitors tested for postexposure protection against vaginal SHIV infection in macaques. |
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | Preclinical (in vitro/animal) | Antimicrob Agents Chemother | Evaluated antiviral activity of newer integrase inhibitors against raltegravir-resistant SIVmac239 and HIV-1. |
| [29643246](https://pubmed.ncbi.nlm.nih.gov/29643246/) | 2018 | Preclinical (animal model) | J Virol | Assessed 2-LTR circle dynamics in raltegravir-treated, SIV-infected macaques to study CD8+ cell-mediated viral control. |
| [29466356](https://pubmed.ncbi.nlm.nih.gov/29466356/) | 2018 | Preclinical (animal model) | PLoS One | Documented emergence of resistance mutations in SIV-infected macaques receiving raltegravir-intensified non-suppressive ART. |
| [31597776](https://pubmed.ncbi.nlm.nih.gov/31597776/) | 2019 | Preclinical (animal model) | J Virol | Evaluated persistence of intact viral genomes in SIV-infected macaques after early raltegravir-based ART initiation. |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Preclinical (animal model) | mBio | Investigated CNS lentiviral persistence despite effective ART (including raltegravir) in SIV brain infection models. |
| [23365453](https://pubmed.ncbi.nlm.nih.gov/23365453/) | 2013 | Preclinical (in vitro) | J Virol | In vitro susceptibility analysis of simian retrovirus type 4 to antiretroviral agents including raltegravir. |

## EU Market Information

Raltegravir currently has no marketing authorization on record in this dataset (market status: **not marketed**, 0 licenses). No product/authorization table is available.

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and drug-drug interaction data are all marked as data gaps in this evidence pack — TFDA/regulatory label warnings are flagged as a Blocking data gap, DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, SIV infection, is not a human disease and does not constitute a clinically actionable repurposing candidate — the evidence pack's own rationale identifies it as a likely entity-mapping artifact from HIV/SIV mechanistic homology. Supporting evidence is limited to one withdrawn trial (zero enrollment) and preclinical animal-model literature (L4), insufficient to justify progression.

**To proceed, the following is needed:**
- Resolve the Blocking data gap (DG001): retrieve official label warnings/contraindications before any safety pre-screening (S1) can occur
- Resolve the mechanism-of-action data gap (DG002) via DrugBank API
- If pursuing repurposing signals from this pack, redirect evaluation toward the human-relevant candidates — **congenital HIV infection** and **AIDS related complex** (both L2, "Proceed with Guardrails") — as separate, better-supported candidates rather than the SIV signal
- Confirm/obtain formal original-indication licensing text, since no EU authorization record currently exists for this drug in this dataset
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

