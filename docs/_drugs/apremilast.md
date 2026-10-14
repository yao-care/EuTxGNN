---
layout: default
title: Apremilast
parent: AI Predictions (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Apremilast
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

# Apremilast: From Psoriatic Arthritis to Migraine Disorder

## One-Sentence Summary

Apremilast is an oral PDE4 inhibitor originally authorised in the EU for psoriatic arthritis, plaque psoriasis and oral ulcers of Behçet's disease.
The TxGNN model predicts it may be effective for **migraine disorder** (the top-ranked prediction), but **no clinical trials or publications** currently support this direction.
The only prediction with clinical data is rheumatoid arthritis (rank 3), with **3 registered trials** and one Phase 2 RCT. That evidence is modest and is described below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Active psoriatic arthritis in adults (also moderate to severe plaque psoriasis and oral ulcers associated with Behçet's disease) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 98.66% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 2 (both cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on the literature provided, apremilast is a small-molecule inhibitor of type-4 cyclic nucleotide phosphodiesterase (PDE4). Its efficacy in psoriatic arthritis and psoriasis is established, and it reduces inflammatory signalling by raising intracellular cAMP.

PDE4 is highly expressed in the mammalian brain, and a 2020 review discusses it as a possible target in neurological disorders. This is the only rationale linking apremilast to migraine, and it is speculative. No apremilast-specific study in migraine was found. Headache is also a known adverse event of apremilast, which argues against benefit.

The prediction is therefore driven by the model score alone. The other predictions in the top 10 are also unsupported: migraine with brainstem aura and the migraine susceptibility term are variants of the same idea, and the remaining entries (pulmonary hypertension, kyphoscoliotic heart disease, rare congenital syndromes and rare skin disorders) have no plausible mechanistic link. The one exception is rheumatoid arthritis, which is the best-supported alternative and is covered below.

## Clinical Trial Evidence

There are no registered clinical trials for migraine. For reference, the trials below are for the best-supported alternative prediction, **rheumatoid arthritis** (rank 3, TxGNN score 98.09%).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01285310](https://clinicaltrials.gov/study/NCT01285310) | Phase 2 | Terminated | 237 | Randomised, double-blind, placebo-controlled study of two apremilast doses in RA patients with inadequate response to methotrexate. Reason for termination not stated |
| [NCT01250548](https://clinicaltrials.gov/study/NCT01250548) | Phase 2 | Completed | 34 | Placebo-controlled trial of apremilast in active RA; small sample limits statistical power |
| [NCT01204138](https://clinicaltrials.gov/study/NCT01204138) | Phase 2 | Withdrawn | 0 | Apremilast added to TNF inhibitor plus methotrexate in active RA; no participants enrolled, so no evidence |

## Literature Evidence

There is no literature on apremilast in migraine. The only related publication is a neurological review on PDE4 as a target. The key publications below are for the rheumatoid arthritis prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25779750](https://pubmed.ncbi.nlm.nih.gov/25779750/) | 2015 | RCT | Arthritis & Rheumatology | Phase 2 placebo-controlled study of apremilast in active RA with inadequate response to methotrexate |
| [20525198](https://pubmed.ncbi.nlm.nih.gov/20525198/) | 2010 | Preclinical | Arthritis Research & Therapy | Apremilast inhibited spontaneous TNF-alpha production in human RA synovial cells and improved experimental arthritis |
| [30072998](https://pubmed.ncbi.nlm.nih.gov/30072998/) | 2018 | Preclinical | Frontiers in Immunology | Apremilast ameliorated mouse collagen-induced arthritis by suppressing Th1/Th17 cells and enhancing regulatory T cells |
| [26097790](https://pubmed.ncbi.nlm.nih.gov/26097790/) | 2014 | Pharmacokinetic study | Clin Pharmacol Drug Dev | Co-administration of apremilast and methotrexate in RA and PsA patients |
| [24797159](https://pubmed.ncbi.nlm.nih.gov/24797159/) | 2014 | Review | Drugs | Overview of apremilast's first global approval and development programme |
| [32673703](https://pubmed.ncbi.nlm.nih.gov/32673703/) | 2020 | Review | Pharmacological Research | PDE4 as a therapeutic target in neurological disorders (the only link to migraine, indirect) |
| [40195166](https://pubmed.ncbi.nlm.nih.gov/40195166/) | 2025 | Pharmacovigilance analysis | Arch Dermatol Res | Real-world adverse event analysis of apremilast from the FAERS database |

## EU Market Information

Both authorisations are listed as cancelled. Dosage form was not available.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/006208 | Apremilast Accord | Not available | Psoriatic arthritis Apremilast Accord, alone or in combination with Disease Modifying Antirheumatic Drugs (DMARDs), is indic... |
| EMEA/H/C/003746 | Otezla | Not available | Psoriatic arthritisOtezla, alone or in combination with Disease Modifying Antirheumatic Drugs (DMARDs), is indicated for t... |

## Safety Considerations

- **Drug Interactions**: 75 interactions were identified. Major-level interactions include lumacaftor, fosphenytoin and apalutamide. Many are enzyme inducers that may reduce apremilast exposure. Moderate-level examples include dexamethasone, bexarotene, bosentan, griseofulvin and aminoglutethimide.
- **Adverse events**: Headache is a known adverse event of apremilast, which is relevant when considering a migraine indication.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction has a high model score but no supporting trials or publications (Evidence Level L5). The only mechanistic rationale, PDE4 in neurological disease, is speculative, and headache as a known adverse event argues against benefit. The EU authorisations are also currently cancelled.

**To proceed, the following is needed:**
- Preclinical or mechanistic evidence for PDE4 inhibition in migraine models
- Detailed mechanism of action data and safety label data (warnings and contraindications) from the EU product information
- Clarification of why the EU authorisations were cancelled and of the current regulatory status
- Review of headache incidence in existing apremilast trials as a signal against migraine use
- If a better-supported direction is preferred, evaluation of rheumatoid arthritis, taking into account the terminated Phase 2 trial and the modest efficacy signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

