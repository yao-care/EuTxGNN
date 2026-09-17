---
layout: default
title: Rimegepant
parent: AI Predictions (L5)
nav_order: 506
evidence_level: L5
indication_count: 10
---

# Rimegepant
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

Using the evidence pack as provided — no additional skill applies here since this is a direct content-generation task following an explicit template, not a coding/debugging task.

---

# Rimegepant: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Rimegepant is a calcitonin gene-related peptide (CGRP) receptor antagonist ("gepant") already used internationally for the acute and preventive treatment of migraine, though it is **not yet marketed** in this jurisdiction. The TxGNN model predicts it may also be effective for **Migraine with Brainstem Aura**, a specific migraine subtype, with **0 dedicated clinical trials** for this subtype but **13 supporting publications** on rimegepant's broader migraine efficacy and safety profile.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in structured regulatory data (drug not yet marketed here); per literature, rimegepant is approved elsewhere for acute treatment of migraine with/without aura and preventive treatment of episodic migraine |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% (rank 956) |
| Evidence Level | L1 (based on the broader migraine indication; no subtype-specific RCTs — see rationale below) |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data is currently a data gap in this record. Based on published literature, rimegepant is a small-molecule, highly selective CGRP receptor antagonist, marketed internationally as Nurtec® ODT (USA) and Vydura® (EU), approved for acute treatment of migraine with or without aura and for prevention of episodic migraine in adults.

Migraine with brainstem aura (formerly "basilar-type migraine") is a clinically recognized subtype within the broader migraine spectrum, not a distinct disease with a separate pathophysiology. Since CGRP-mediated neurovascular signaling is considered central to migraine pathophysiology in general — independent of aura subtype — the mechanism plausibly extends to this subtype. However, none of the identified literature (including the pivotal Phase 3 trials referenced in the review by Blair et al., PMID 36739335) report subtype-stratified outcomes for brainstem aura specifically; existing RCTs enrolled general migraine populations. This means the evidence supports the mechanism-level rationale strongly, but subtype-specific clinical confirmation is currently absent.

One additional consideration: a longitudinal MRA study (PMID 41574090) investigated rimegepant's effects on cerebral and extracerebral arteries during migraine attacks, which is directly relevant to aura-related cerebrovascular hemodynamics and may eventually help substantiate (or refute) applicability to the brainstem aura subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41066271](https://pubmed.ncbi.nlm.nih.gov/41066271/) | 2025 | Phase 3 Open-label Long-term Safety | Cephalalgia | Long-term safety/effectiveness of rimegepant 75mg ODT for acute migraine treatment in Chinese adults (single-arm) |
| [35790906](https://pubmed.ncbi.nlm.nih.gov/35790906/) | 2022 | Network Meta-analysis | J Headache Pain | Compares onset of efficacy of rimegepant vs. ubrogepant and lasmiditan for acute migraine treatment |
| [32270407](https://pubmed.ncbi.nlm.nih.gov/32270407/) | 2020 | Regulatory/Drug Profile | Drugs | First approval summary of rimegepant ODT as acute migraine treatment; notes ongoing investigation for prevention and trigeminal neuralgia |
| [36739335](https://pubmed.ncbi.nlm.nih.gov/36739335/) | 2023 | Review | CNS Drugs | Reviews pivotal Phase 3 trial data showing rimegepant superior to placebo for acute and preventive migraine treatment |
| [41366286](https://pubmed.ncbi.nlm.nih.gov/41366286/) | 2025 | Phase 4 Open-label | J Headache Pain | 24-week safety/tolerability of once-daily 75mg rimegepant for episodic migraine prevention |
| [38307667](https://pubmed.ncbi.nlm.nih.gov/38307667/) | 2024 | Review | Handbook Clin Neurol | Overview of CGRP receptor antagonists (gepants), including rimegepant's approval history and class mechanism |
| [41652664](https://pubmed.ncbi.nlm.nih.gov/41652664/) | 2026 | Retrospective Cohort | Headache | Off-label use of rimegepant for acute migraine treatment in adolescents |
| [33550872](https://pubmed.ncbi.nlm.nih.gov/33550872/) | 2021 | Review | Pain Management | Overview of rimegepant within the new wave of acute migraine treatments (vs. lasmiditan, ubrogepant) |
| [36808268](https://pubmed.ncbi.nlm.nih.gov/36808268/) | 2023 | Phase 1 PK/Safety | Clin Pharmacol Drug Dev | PK and safety of single/multiple-dose rimegepant 75mg ODT in healthy Chinese adults |
| [41133671](https://pubmed.ncbi.nlm.nih.gov/41133671/) | 2026 | Phase 1 PK/Safety | Headache | PK, safety, and tolerability of single-dose rimegepant in children (6–<12 years) with migraine history |

---

## EU Market Information

No marketing authorization records are currently available for this jurisdiction. Rimegepant's status is recorded as **Not marketed (Not Marketed)**, with **0 licenses** on file as of the data cutoff (2026-09-16).

---

## Safety Considerations

Please refer to the SmPC for safety information (key warnings, contraindications, and DDI data are currently data gaps for this record).

- **Class-Level Safety Signal (not indication-specific)**: A pharmacovigilance disproportionality analysis of FAERS data (PMID 41706150) identified a potential signal between CGRP antagonists and cardiac adverse event reporting. Because CGRP is an endogenous vasodilator, theoretical concern exists that CGRP receptor blockade could aggravate coronary vasospasm — mechanistically opposite to what would be needed to treat Prinzmetal (vasospastic) angina, a separate low-scoring TxGNN prediction for this drug that should be treated as a **safety monitoring flag, not a repurposing opportunity**. This signal should be tracked as rimegepant's regulatory/safety dossier develops.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Rimegepant's mechanism (CGRP receptor antagonism) is well-established for migraine broadly, and the drug is already approved and marketed elsewhere for migraine with/without aura. However, migraine with brainstem aura specifically lacks dedicated subtype-stratified trial data, and the drug currently has no marketing authorization in this jurisdiction — warranting a cautious, guardrailed path rather than a full "Go."

**To proceed, the following is needed:**
- Official MOA documentation and approved indication text (currently marked as data gaps, DG002 and missing `original_indications`)
- TFDA/local SmPC warnings and contraindications (currently a **Blocking** data gap, DG001) — required before any S1 safety evaluation can proceed
- Subtype-stratified (brainstem aura) analysis from existing Phase 3 migraine trial datasets, or a dedicated prospective study
- Continued monitoring of the CGRP-antagonist cardiac safety signal (FAERS disproportionality analysis) as part of ongoing pharmacovigilance
- Confirmation of local market authorization plans/timeline, given current "Not Marketed" / 0-license status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

