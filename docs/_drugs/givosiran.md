---
layout: default
title: Givosiran
parent: AI Predictions (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
---

# Givosiran
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

# Givosiran: From Acute Hepatic Porphyria to Porphyria Due to ALA Dehydratase Deficiency

## One-Sentence Summary

Givosiran is a hepatocyte-targeted siRNA originally approved for acute hepatic porphyria (AHP), a group of four inherited disorders of heme biosynthesis. TxGNN's two highest-scoring predictions for this drug (hepatopulmonary syndrome, portal hypertension variants, hepatitis B/C, etc.) are flagged in the evidence pack itself as mechanistically implausible — likely a knowledge-graph embedding artifact around "liver-targeted drugs" rather than a real signal, with zero supporting trials or literature. The one candidate with genuine evidence is **porphyria due to ALA dehydratase deficiency (ADP)**, which is actually one of the four AHP subtypes already covered by Givosiran's approved label; **8 publications** support this pathway, but they include one case report of clinical **non-response**, so this is presented as an evidence review of an existing label subtype rather than a novel repurposing opportunity.

> **Note on candidate selection**: This report deviates from TxGNN's #1-ranked prediction (rank 1, score 99.999%) because the evidence pack's own `repurposing_rationale` explicitly states there is "no mechanistic link" for ranks 1–8 and rank 10 — hepatopulmonary syndrome, portal hypertension/vascular liver diseases, viral hepatitis, and metabolic disorders unrelated to heme biosynthesis. Reporting on that top score would be misleading. Rank 9 (ALA dehydratase deficiency porphyria) is the only candidate with real literature evidence and a coherent mechanism, so it is used here instead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute hepatic porphyria (AHP) — per literature; not present in structured `taiwan_regulatory` data |
| Predicted New Indication | Porphyria due to ALA dehydratase deficiency (ADP) |
| TxGNN Prediction Score | 99.91% (rank 1286 of all predictions) |
| Evidence Level | L3 (observational studies + Phase 3 post-hoc analysis for AHP broadly; only a single case report is specific to ADP) |
| Taiwan Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

`original_moa` is marked as a data gap in the structured record, but the literature evidence retrieved for this candidate independently describes the mechanism: Givosiran is a GalNAc-conjugated siRNA that is taken up by hepatocytes and targets ALAS1 mRNA, silencing hepatic ALA synthase 1. This blocks the upstream, rate-limiting step of heme biosynthesis and prevents accumulation of the neurotoxic intermediates δ-aminolevulinic acid (ALA) and porphobilinogen (PBG) that drive acute porphyria attacks.

Acute hepatic porphyria (AHP) is not a single disease but an umbrella of four enzyme deficiencies in the heme pathway: acute intermittent porphyria, hereditary coproporphyria, variegate porphyria, and ALA dehydratase deficiency porphyria (ADP). Because all four share the same downstream toxic-metabolite mechanism, ADP is already within Givosiran's approved regulatory indication for AHP — this is not really a novel "repurposing" candidate in the TxGNN sense, but an ultra-rare subtype for which disease-specific clinical evidence is sparse.

Critically, one published case report (PMID 35991568) documents a patient with genetically confirmed ADP who did **not** respond clinically to Givosiran despite the shared mechanism, illustrating that mechanistic plausibility does not guarantee subtype-level efficacy. This tempers the otherwise strong mechanistic rationale and is the main reason this evaluation does not support a "Go" recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered specific to porphyria due to ALA dehydratase deficiency. (The evidence pack references the Phase 3 ENVISION trial only indirectly, via a post-hoc literature analysis — see Literature Evidence below — not as a registered trial record for this candidate.)

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36028858](https://pubmed.ncbi.nlm.nih.gov/36028858/) | 2022 | Phase 3 RCT (post-hoc analysis) | Orphanet Journal of Rare Diseases | Post-hoc analysis of the Phase 3 ENVISION trial quantifying AHP disease burden in patients ≥12 years treated with givosiran |
| [40312531](https://pubmed.ncbi.nlm.nih.gov/40312531/) | 2025 | Observational (expanded access study) | Scientific Reports | Open-label, single-arm study in 10 Japanese AHP patients on monthly subcutaneous givosiran (2.5 mg/kg); reports safety/efficacy in expanded access setting |
| [35067977](https://pubmed.ncbi.nlm.nih.gov/35067977/) | 2022 | Observational | Journal of Internal Medicine | RNAi therapy with givosiran significantly reduces attack rates in acute intermittent porphyria |
| [35734365](https://pubmed.ncbi.nlm.nih.gov/35734365/) | 2022 | Review | Drug Design, Development and Therapy | Overview of givosiran's design, development, and therapeutic place for adults with AHP |
| [39313028](https://pubmed.ncbi.nlm.nih.gov/39313028/) | 2024 | Review | Revista Clínica Española | Therapeutic approach to acute crises of hepatic porphyria, covering ALAD deficiency as a subtype triggered by hepatic ALAS1 induction |
| [37027823](https://pubmed.ncbi.nlm.nih.gov/37027823/) | 2023 | Review | Blood | Review of RNA interference therapy mechanism and clinical use across the four AHP subtypes |
| [36883675](https://pubmed.ncbi.nlm.nih.gov/36883675/) | 2023 | PK/PD modeling study | CPT: Pharmacometrics & Systems Pharmacology | Pharmacokinetic-pharmacodynamic model of urinary ALA reduction after givosiran treatment, pooled from Phase I–III trials |
| [35991568](https://pubmed.ncbi.nlm.nih.gov/35991568/) | 2022 | Case report | Frontiers in Genetics | **Disease-specific evidence**: documented lack of clinical response to givosiran in a genetically confirmed case of ALAD porphyria, despite approval covering this subtype |

## Taiwan Market Information

Givosiran currently holds **0 authorizations** in the Taiwan regulatory dataset (`market_status: Not marketed` / not marketed). No license records are available to summarize dosage form or approved indication text.

## Safety Considerations

Please refer to the SmPC for safety information. (Key warnings, contraindications, and DDI data are all unavailable in the current evidence pack — this is flagged as a Blocking data gap, see Conclusion.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic rationale is sound (ADP shares Givosiran's ALAS1-silencing mechanism with the already-approved AHP indication), but the only disease-specific real-world evidence is a single case report showing treatment failure, and no dedicated controlled trial exists for this subtype.
- Taiwan-specific regulatory data (label, warnings, contraindications) is entirely absent — this is a **Blocking** data gap (DG001) that prevents any safety pre-assessment regardless of efficacy evidence.
- TxGNN's higher-scoring predictions for this drug (ranks 1–8, 10) were reviewed and excluded as mechanistically unsupported per the evidence pack's own annotations, leaving no stronger candidate to promote instead.

**To proceed, the following is needed:**
- TFDA/SmPC label data (warnings, contraindications) — currently blocking (DG001)
- Confirmed original MOA documentation from DrugBank (DG002)
- Additional ADP-specific case series or registry data to reconcile the conflicting response signal (one negative case vs. mechanistic plausibility)
- Clarification of whether this candidate should be tracked as "new indication" or "known label subtype with evidence gap," since ADP is not truly outside Givosiran's current approved use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

