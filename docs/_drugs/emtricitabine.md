---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Emtricitabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Emtricitabine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Emtricitabine is a nucleoside reverse transcriptase inhibitor (NRTI) whose established use is HIV-1 treatment and pre-exposure prophylaxis (PrEP).
> The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection**,
> supported by **2 clinical trials** and **20 publications** — but SIV is a macaque/animal-model analog of HIV, not a human disease, so this specific prediction is not directly actionable as a human indication (see rationale below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection treatment / pre-exposure prophylaxis (PrEP) — inferred from repurposing rationale text; no structured `original_indications` or licence record available |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L3 |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Emtricitabine is not available in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, Emtricitabine is a cytidine-analog NRTI, part of the same drug class used in Truvada/Descovy-type combinations; its efficacy against HIV-1 reverse transcriptase is well established, and mechanistically this activity may extend to closely related retroviruses.

SIV shares high homology with HIV-1 at the reverse transcriptase level, which is why TxGNN links Emtricitabine to SIV infection with a very high score. A large body of macaque PrEP/PEP challenge studies (rectal, vaginal, and oral exposure models) confirms that Emtricitabine, usually combined with tenofovir, prevents SIV/SHIV acquisition and suppresses replication in these animal models — mechanistically consistent with its known NRTI action.

However, SIV infection is a disease of non-human primates used as a research model for HIV — **it is not a human disease and cannot itself be filed as a human clinical indication.** The evidentiary strength here reflects the quality of the animal-model literature, not clinical applicability. Two other TxGNN-ranked candidates in this evidence pack are more directly actionable because they sit within Emtricitabine's actual human indication space: "AIDS related complex" (rank 5, L2, includes a Phase 1b trial directly testing Emtricitabine) and "congenital human immunodeficiency virus" (rank 6, L1, extensive perinatal/PMTCT and PrEP-in-pregnancy trial evidence). These represent label-extension opportunities rather than a genuinely novel indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab + ART in ART-naïve HIV-infected humans aiming for virological remission; human HIV study, not an SIV/animal model — weak relevance (Grade C) |
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | Withdrawn | 0 | Decay kinetics of HIV with raltegravir; references comparable SIV-macaque decay kinetics but trial itself was withdrawn with zero enrollment (Grade C) |

*Both trials study human HIV populations, not SIV; neither directly supports an SIV indication.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | RCT/Review (Human PrEP) | Pharmacotherapy | Reviews systemic PrEP for HIV prevention; basis for extrapolating FTC/TDF efficacy |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | Animal Model (Macaque) | J Infect Dis | Oral TAF/FTC or TAF alone prevented vaginal SHIV infection in macaques |
| [29788316](https://pubmed.ncbi.nlm.nih.gov/29788316/) | 2018 | Animal Model (Macaque) | J Infect Dis | Vaginal FTC/tenofovir gel protected macaques against repeated rectal SHIV exposure |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Animal Model (Macaque) | J Infect Dis | Oral FTC/TAF chemoprophylaxis protected macaques from rectal SHIV infection |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Animal Model (Macaque) | J Infect Dis | FTC/TDF prevented vaginal SHIV infection even with concurrent chlamydia/trichomonas coinfection |
| [24914761](https://pubmed.ncbi.nlm.nih.gov/24914761/) | 2014 | Animal Model (Macaque) | AIDS Res Hum Retroviruses | HIV VLP vaccine + partial oral PrEP (Truvada) prevented SHIV infection in macaques |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Animal Model (Macaque) | Nature Communications | Oral FTC/TAF + long-acting cabotegravir/rilpivirine tested for SHIV remission in macaques |
| [29466356](https://pubmed.ncbi.nlm.nih.gov/29466356/) | 2018 | Animal Model | PLoS One | Resistance mutations emerged in SIV-infected macaques on non-suppressive tenofovir/emtricitabine + raltegravir |
| [12021341](https://pubmed.ncbi.nlm.nih.gov/12021341/) | 2002 | Mechanistic (In Vivo) | J Virology | M184V resistance mutation emerged in SIV-infected macaques treated with emtricitabine, mirroring HIV resistance patterns |
| [18216122](https://pubmed.ncbi.nlm.nih.gov/18216122/) | 2008 | Natural History Study | J Virology | SIVagm-infected African green monkeys treated with tenofovir/emtricitabine ART to study viral dynamics |

*10 most relevant publications shown (10 additional lower-priority/unclassified macaque studies exist in the source pack but are omitted here).*

---

## EU Market Information

Emtricitabine currently has **no marketing authorization records** in this dataset (market status: Not Marketed; 0 authorizations on file). No EU licence table can be generated.

---

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and DDI data are all currently unavailable — TFDA/EMA label data was flagged as a Blocking data gap, `DG001`, and could not be retrieved for this evidence pack.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, SIV infection, is a non-human primate disease used as an HIV research model — it cannot be filed as a human clinical indication regardless of the strong TxGNN score and supportive animal literature. This candidate is a research/mechanistic curiosity, not a repurposing opportunity. The evidence pack does contain more clinically actionable candidates within Emtricitabine's real indication space — "AIDS related complex" (rank 5, L2, Proceed with Guardrails) and "congenital human immunodeficiency virus" (rank 6, L1, Proceed with Guardrails) — which should be evaluated as separate, higher-priority reports.

**To proceed, the following is needed:**
- TFDA/EMA label warnings and contraindications (blocking data gap `DG001`) before any safety-stage (S1) evaluation can proceed
- Confirmed mechanism-of-action data via DrugBank API (`DG002`)
- Re-scope the repurposing evaluation toward rank 5 (AIDS related complex) and rank 6 (congenital HIV/PMTCT) candidates, which carry direct clinical and regulatory relevance
- Market authorization records, since none are currently on file for this drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

