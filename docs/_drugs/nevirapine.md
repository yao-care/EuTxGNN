---
layout: default
title: Nevirapine
parent: Medium Evidence (L3-L4)
nav_order: 414
evidence_level: L4
indication_count: 10
---

# Nevirapine
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

# Nevirapine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI), established in the literature for treating HIV-1 infection.
> The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**,
> but this is supported only by **0 clinical trials** and **16 preclinical/mechanistic publications** — and several of those publications indicate wild-type SIV is naturally resistant to NNRTIs, weakening the case.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this EU regulatory data pack (0 authorizations on file); per literature context, Nevirapine is used as an antiretroviral (NNRTI) for HIV-1 infection |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| EU Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the supporting literature, Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) used against HIV-1. Mechanistically, the rationale for extending it to SIV infection rests on the fact that HIV and SIV are both lentiviruses with structurally related reverse transcriptase enzymes.

However, the collected evidence actually undercuts this rationale rather than supporting it. Multiple in vitro/preclinical papers (e.g. PMID 7541200, 15040537) report that **wild-type SIV reverse transcriptase has a structurally divergent NNRTI binding pocket and is naturally resistant to nevirapine and other NNRTIs**. Sensitivity is only observed in engineered chimeric viruses (SHIV/RT-SHIV) that have been genetically modified to carry HIV-1's reverse transcriptase gene, purely as a laboratory tool for studying drug-resistance evolution in non-human primate models — not as a therapeutic target in naturally occurring SIV infection.

In short, the biological similarity that TxGNN is picking up on (HIV vs. SIV as related lentiviruses) does not translate into real antiviral activity against native SIV, and there is no human clinical relevance here — SIV does not infect humans. This candidate is best understood as identifying nevirapine's established role as a *research tool* in NNRTI-resistance animal models, not a genuine drug-repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In vitro/Preclinical | Journal of Virology | Constructed an SIV-HIV chimera expressing HIV-1 reverse transcriptase to study NNRTI resistance in pigtail macaques, since NNRTIs do not effectively inhibit native SIV RT |
| [19195672](https://pubmed.ncbi.nlm.nih.gov/19195672/) | 2009 | Preclinical (animal model) | Virology | Characterized vaginal transmission of an RT-SHIV (HIV-1 RT inserted into SIV backbone) in rhesus macaques as a model system, not a treatment study |
| [7541200](https://pubmed.ncbi.nlm.nih.gov/7541200/) | 1995 | In vitro susceptibility | Biochem Biophys Res Commun | Built a hybrid SIV/HIV-1 RT chimera (RT-SHIV) specifically because native SIV is not sensitive to HIV-1-specific NNRTIs; chimera was sensitive to both NRTIs and NNRTIs |
| [11375059](https://pubmed.ncbi.nlm.nih.gov/11375059/) | 2001 | In vivo animal model | AIDS Res Hum Retroviruses | Cynomolgus monkeys infected with RT-SHIV used as an in vivo model to study emergence and reversal of NNRTI drug resistance |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro susceptibility comparison | Antiviral Therapy | Evaluated 16 approved anti-HIV-1 drugs (including presumably nevirapine-class NNRTIs) against HIV-2, SIV, and SHIV strains to guide treatment/PEP use — relevant to differential species susceptibility |
| [12234864](https://pubmed.ncbi.nlm.nih.gov/12234864/) | 2002 | Pending | Antimicrob Agents Chemother | Tested integrase inhibitor L-708,906 combined with zidovudine, **nevirapine**, or nelfinavir against SIV(MAC251); combinations with nevirapine were subsynergistic |
| [27748043](https://pubmed.ncbi.nlm.nih.gov/27748043/) | 2017 | Pending | Chem Biol Drug Des | Small molecule 3G11 inhibits HIV-1 RT specifically but does NOT block SIVmac or other retroviruses — illustrates species-specific RT inhibitor activity |
| [11020686](https://pubmed.ncbi.nlm.nih.gov/11020686/) | 2000 | Pending | Ann Emerg Med | Reviews postexposure prophylaxis rationale, citing animal (SIV) studies showing antiretrovirals can reduce SIV transmission as indirect support for human PEP |
| [1283296](https://pubmed.ncbi.nlm.nih.gov/1283296/) | 1992 | Pending | Antimicrob Agents Chemother | FTC (an NRTI, not nevirapine) shown active against HIV-1, HIV-2, SIV, and FIV in cell culture systems |
| [16859727](https://pubmed.ncbi.nlm.nih.gov/16859727/) | 2006 | Pending | Virology | Tested NRTIs and NNRTIs against HIV-1 and SIV virions for inhibiting endogenous reverse transcription, exploring potential as topical "lentivirucides" |

---

## EU Market Information

No EU marketing authorizations are currently on file for Nevirapine in this data pack (market status: **Not marketed / Not marketed**, 0 authorizations recorded).

---

## Safety Considerations

Please refer to the SmPC for safety information.

*(Note: `safety.key_warnings` and `safety.contraindications` are both flagged as data gaps in this evidence pack, and no drug interaction records were found. TFDA/EMA label warnings are listed as a Blocking data gap — DG001 — required before any safety (S1) assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L4 (preclinical/mechanistic only, no clinical trials), and the literature itself indicates wild-type SIV is naturally resistant to nevirapine — sensitivity has only been demonstrated in artificially engineered chimeric viruses used as laboratory research tools. There is also no human clinical relevance, as SIV does not infect humans. The mechanistic and clinical case for repurposing is weak.

**To proceed, the following is needed:**
- Nevirapine mechanism-of-action data (DG002, High severity) to properly assess mechanistic plausibility
- TFDA/EMA product label warnings and contraindications (DG001, Blocking — required before any S1 safety assessment)
- Clarification of the clinical/translational rationale, since the target organism (SIV) is non-human and the existing evidence describes a research-tool use case rather than a therapeutic indication
- If a genuine human-relevant indication is intended, re-examine other candidates in this evidence pack — e.g., "AIDS related complex" (rank 10, L2/S3, Proceed with Guardrails) is better supported but falls within nevirapine's original approved use rather than representing a novel repurposing opportunity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

