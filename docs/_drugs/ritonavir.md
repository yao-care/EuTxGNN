---
layout: default
title: Ritonavir
parent: Medium Evidence (L3-L4)
nav_order: 512
evidence_level: L4
indication_count: 10
---

# Ritonavir
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

Using no special skill here — this is a direct content-generation task per the given report template, not a coding/debugging task.

# Ritonavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Ritonavir is an HIV-1 protease inhibitor originally used to treat HIV-1 infection, most commonly today as a pharmacokinetic booster for other protease inhibitors. The TxGNN model's top-ranked prediction associates it with **Simian Immunodeficiency Virus (SIV) Infection** — an animal disease model, not a human condition — supported only by **0 clinical trials** and **12 preclinical publications**, indicating this is likely an ontology mismatch rather than a genuine human repurposing opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 Infection (established per evidence-pack rationale text; no formal EU/Taiwan license record retrieved) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for ritonavir is not available in this evidence pack (flagged as a High-severity data gap). Based on known information referenced throughout the evidence pack's own repurposing rationales, ritonavir is an HIV-1 protease inhibitor, and its efficacy in HIV-1 infection is well established both as a direct antiviral and as a CYP3A4-mediated booster for co-administered protease inhibitors.

SIV is the simian (macaque) analog of HIV used almost exclusively as a nonhuman primate research model for HIV/AIDS pathogenesis and antiretroviral drug testing — it is not a naturally occurring human disease. The mechanistic link exists at the structural level: SIV protease shares homology with HIV-1 protease, and in vitro data (PMID 12709355) show ritonavir inhibits SIVmac239 with an EC50 of ~13 nM, comparable to its activity against HIV-1 (~25 nM).

However, this mechanistic plausibility does not translate into a viable human repurposing candidate — SIV does not infect humans, and the "indication" itself is a laboratory/animal-model construct. The high TxGNN score most likely reflects the model treating SIV and HIV as closely related graph neighbors (shared drug-target and pathway edges) rather than identifying a novel, clinically actionable indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro/Preclinical | Antimicrob Agents Chemother | Ritonavir inhibits SIVmac239 in vitro (EC50 ≈13 nM), comparable potency to HIV-1 inhibition |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro/Preclinical | Antiviral Therapy | Comparative susceptibility of HIV-2, SIV, and SHIV strains to 16 approved anti-HIV-1 drugs including ritonavir |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal model study | Journal of Virology | Viral decay kinetics in SIV-infected macaques receiving quadruple antiretroviral therapy |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal model study | PLoS ONE | Combination cART plus HDAC inhibitor SAHA in SIV-infected rhesus macaques (viral reservoir study) |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal model study | PLoS Pathogens | Intensified multidrug ART regimen suppresses viremia and restricts viral reservoir in SIV-infected macaques |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | In vitro/Animal model | Microbes and Infection | Construction of chimeric SHIV bearing HIV-1 protease gene, for in vivo protease-inhibitor efficacy testing |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal model study | Journal of Virological Methods | Oral HAART (including lopinavir/ritonavir) impact on CD8 subsets in SHIV-infected monkeys |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | In vitro mechanistic | Journal of Virology | HIV-1 Vif protein processing by viral protease; mechanistic study, not ritonavir-specific efficacy |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Preclinical/mechanistic | mBio | Lentiviral (HIV) persistence in brain tissue despite effective ART; relevance to SIV models discussed |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | In vitro/Preclinical | Antiviral Chemistry & Chemotherapy | Broad-spectrum antiviral fluoroquinolone derivative active against HIV-1, HIV-2, and SIV, including ritonavir-resistant HIV-1 strains |

## EU Market Information

No marketing authorization records are available in this evidence pack (`total_licenses = 0`, `market_status = Not Marketed`). This is inconsistent with ritonavir's known long-standing EU approval (e.g., Norvir) and likely reflects a data collection gap in this specific evidence pull rather than an actual absence of EU authorization.

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication, Simian Immunodeficiency Virus Infection, is an animal research model rather than a human disease, and is supported only by L4 (preclinical/mechanistic) evidence with zero registered clinical trials. It cannot be advanced as a human repurposing candidate.

**To proceed, the following is needed:**
- Resolve the TFDA/EMA label warnings and contraindications data gap (DG001, Blocking) — required before any S1 safety review, per source: TFDA label PDF parsing
- Resolve the mechanism-of-action data gap (DG002, High) via DrugBank API query
- Correct or re-verify the EU marketing-authorization data pull for ritonavir, given the known discrepancy with its established EMA approval
- Review whether the SIV/HIV disease nodes in the underlying knowledge graph should be merged or flagged, since this appears to be an ontology-mapping artifact rather than a novel signal
- If a genuine repurposing signal is sought from this drug's prediction set, evaluate the lower-ranked but more clinically translatable candidates already present in this pack (e.g., hepatitis E virus infection at L4/S1 with a distinct viral-entry-inhibition mechanism, or ritonavir-boosted PI use in perinatal/pediatric HIV at L1/S3) as separate, better-supported candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

