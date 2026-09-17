---
layout: default
title: Delamanid
parent: Medium Evidence (L3-L4)
nav_order: 176
evidence_level: L4
indication_count: 10
---

# Delamanid
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

# Delamanid: From Multidrug-Resistant Tuberculosis to Bovine Tuberculosis

## One-Sentence Summary

Delamanid is a nitroimidazole antimycobacterial originally used for multidrug-resistant pulmonary tuberculosis (MDR-TB). The TxGNN model predicts it may also be effective for **Bovine Tuberculosis** (zoonotic *Mycobacterium bovis* infection), but this direction is currently supported only by a prediction score and **1 indirect publication** (a pathogen genomics study, not a drug-efficacy study) — **no clinical trials exist** for this specific pairing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multidrug-resistant tuberculosis (MDR-TB) — noted in evidence-pack rationale; no EU/TFDA label text available in this pack |
| Predicted New Indication | Tuberculosis, Bovine |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (`original_moa`) is not available for delamanid in this evidence pack. Based on the repurposing rationale associated with this prediction, delamanid is a nitro-dihydro-imidazooxazole prodrug that is activated by the mycobacterial Ddn nitroreductase system and subsequently inhibits mycolic acid (cell wall) synthesis — a mechanism it shares with its approved indication of MDR pulmonary tuberculosis caused by *Mycobacterium tuberculosis*.

*Mycobacterium bovis*, the causative agent of bovine tuberculosis, belongs to the same *Mycobacterium tuberculosis* complex and shares the mycolic acid synthesis pathway and Ddn activation system. This provides a plausible mechanistic bridge: in theory, delamanid should retain activity against *M. bovis*.

However, this extrapolation carries important caveats noted directly in the evidence pack: *M. bovis* has intrinsic resistance to pyrazinamide, and drug-susceptibility data for other anti-TB agents (including delamanid specifically) against *M. bovis* is scarce. Zoonotic TB is effectively an orphan indication here, and no delamanid-specific in vitro or clinical susceptibility data currently exists.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Cohort/Epidemiology | BMC Genomics | Whole-genome sequencing study characterizing genetic diversity and drug-resistance patterns of *M. bovis* isolates from zoonotic human TB cases; this is a pathogen genomics study and does not evaluate delamanid efficacy directly |

## EU Market Information

Delamanid currently has no EU marketing authorizations recorded in this evidence pack (0 licenses; market status: Not Marketed).

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence for this specific prediction is the TxGNN score plus a single pathogen-genomics publication that does not test delamanid; there are no clinical trials, no drug-specific susceptibility data against *M. bovis*, and no EU marketing authorization to anchor a safety/regulatory pathway. This falls short of the threshold to proceed even under guardrails.

**To proceed, the following is needed:**
- TFDA/EMA product label (SmPC) with warnings and contraindications — currently a **blocking** data gap (DG001) that prevents any S1 safety screening
- Confirmed mechanism of action via DrugBank API (DG002)
- In vitro/preclinical susceptibility data of delamanid specifically against *M. bovis*
- Any clinical or case-series evidence of delamanid use in human zoonotic/bovine TB

**Note:** Within this same evidence pack, a related candidate indication — *inactive tuberculosis* (latent/non-active TB, rank 3) — has substantially stronger evidence (L2, including an ongoing Phase 3 trial, NCT03568383, PHOENIx MDR-TB, n=5,832, and 20 supporting publications). If the goal is to identify the most defensible repurposing direction for delamanid, that candidate warrants prioritized evaluation over bovine tuberculosis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

