---
layout: default
title: Selinexor
parent: Medium Evidence (L3-L4)
nav_order: 533
evidence_level: L3
indication_count: 10
---

# Selinexor
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Selinexor: From an Undocumented Original Indication to Progesterone-Receptor Negative (Triple-Negative) Breast Cancer

## One-Sentence Summary

> This Evidence Pack does not record Selinexor's original approved indication (the field is empty), so the original-use context is unknown from this data alone.
> Across **10 TxGNN-predicted oncology indications**, the best-supported candidate is **Progesterone-Receptor Negative Breast Cancer** (incl. triple-negative breast cancer, TNBC), backed by **1 completed investigator-initiated Phase 2 trial (n=10)** and zero conflicting literature.
> The remaining candidates range from weak/indirect (L3–L4) to essentially unsupported model output (L5), and a critical safety data gap currently blocks any drug-level go decision.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack — Selinexor holds 0 EU/Taiwan licenses on file, so no approved-indication text exists to extract |
| Predicted New Indication (lead candidate) | Progesterone-receptor negative breast cancer (incl. triple-negative breast cancer) |
| TxGNN Prediction Score (lead candidate) | 97.20% |
| Evidence Level (lead candidate) | L3 |
| EU Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

*Note: this pack contains 10 ranked predicted indications, not one. See "Predicted Indications — Ranking Overview" below for the full picture.*

---

## Why is This Prediction Reasonable?

**Mechanism.** The dedicated mechanism-of-action field for Selinexor is itself flagged as a data gap in this pack (DG002, High severity). However, the `repurposing_rationale` attached to every predicted indication consistently describes Selinexor as a **Selective Inhibitor of Nuclear Export (SINE)** that blocks **XPO1 (exportin-1)**-mediated nuclear export. This causes tumor-suppressor proteins (e.g., p53, FOXO) to accumulate in the nucleus, triggering apoptosis in malignant cells. This single mechanism is the basis offered for all ten predictions in this pack, spanning multiple unrelated tumor types — a broad, mechanism-first hypothesis rather than a disease-specific one.

**Relationship to original indication.** Because `original_indications` is empty in this pack, we cannot compare disease-relatedness between Selinexor's real approved use and the predicted ones from the data provided here. What can be assessed is internal consistency of the predictions: XPO1 is reported as overexpressed in several aggressive solid tumors, including PR-negative/triple-negative breast cancer, which typically lacks targeted-therapy options — this gives the lead candidate direct mechanistic plausibility, further reinforced by a completed clinical trial that specifically tested Selinexor in this population (NCT02402764).

**A caution on trusting the score alone.** The single highest TxGNN score in this pack (rank 1, "drug-induced osteoporosis," 99.22%) is explicitly flagged in its own rationale as a likely knowledge-graph embedding artifact: the target is a drug-adverse-effect category rather than a treatable oncology indication, has zero supporting trials or literature, and has no known mechanistic link to XPO1 inhibition. We exclude it from further consideration — a clear illustration of why TxGNN score alone must never be the sole decision criterion.

---

## Predicted Indications — Ranking Overview

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Note |
|------|---------|------|------|------|------|------|
| 1 | Drug-induced osteoporosis | 99.22% | L5 | S0 | Hold | Likely embedding noise — not a treatable oncology indication |
| 2 | HER2 positive breast carcinoma | 98.13% | L4 | S0 | Hold | 1 indirect review (endometrial cancer subtypes), no direct evidence |
| **3** | **Progesterone-receptor negative breast cancer (TNBC)** | **97.20%** | **L3** | **S2** | **Research Question** | **1 completed Phase 2 trial, n=10 — lead candidate** |
| 4 | Normal breast-like subtype of breast carcinoma | 97.18% | L5 | S0 | Hold | No trials or literature |
| 5 | Progesterone-receptor positive breast cancer | 97.18% | L5 | S0 | Hold | No trials or literature |
| 6 | Breast tumor luminal A or B | 97.11% | L5 | S0 | Hold | 19 "literature" hits are false positives (B-cell biology, not "luminal B") |
| 7 | Squamous cell lung carcinoma | 96.91% | L3 | S1 | Hold | 2 direct trials, one terminated, one withdrawn — negative/uncertain signal |
| 8 | Gestational trophoblastic neoplasm | 96.54% | L5 | S0 | Hold | No trials or literature |
| 9 | Cervical neuroblastoma | 96.33% | L4 | S0 | Hold | Only an indirect, non-specific review |
| 10 | Schwannoma of jugular foramen | 96.32% | L5 | S0 | Hold | No trials or literature; no plausible mechanistic link (NF2/merlin pathway) |

---

## Clinical Trial Evidence

| Trial Number | Predicted Indication | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|------|---------|
| [NCT02402764](https://clinicaltrials.gov/study/NCT02402764) | PR-negative breast cancer (TNBC) | Phase 2 | Completed | 10 | Investigator-initiated single-arm trial of Selinexor in metastatic triple-negative breast cancer; directly tested drug + population, but very small sample limits strength of conclusion |
| [NCT02213133](https://clinicaltrials.gov/study/NCT02213133) | Squamous cell lung carcinoma | Phase 2 | **Terminated** | 45 | Open-label study of oral Selinexor in relapsed/metastatic squamous cell carcinoma of head & neck, lung, or esophagus; terminated before full completion — reason not captured in this pack |
| [NCT02536495](https://clinicaltrials.gov/study/NCT02536495) | Squamous cell lung carcinoma | Phase 1/2 | **Withdrawn** | 0 | Investigator-sponsored trial of Selinexor + docetaxel in relapsed squamous cell lung cancer; withdrawn before any enrollment, no usable data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36943683](https://pubmed.ncbi.nlm.nih.gov/36943683/) | 2023 | Review | Current Opinion in Obstetrics & Gynecology | Review of endometrial cancer treatment by molecular subtype; mentions HER2-directed strategies but does not directly discuss Selinexor in HER2+ breast cancer — indirect relevance only |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Review | Anti-Cancer Agents in Medicinal Chemistry | Broad synthetic-methodology review of 56 FDA-approved anticancer drugs (2018–2021) including Selinexor; not specific to squamous lung carcinoma or neuroblastoma, cited under both indications |

*Note: 19 additional "literature" records were returned under rank 6 ("breast tumor luminal A or B"). On review, all 19 concern B-cell immunology or hepatitis B vaccination — a keyword false-match ("B" ≠ "luminal B") — and are excluded here as noise, not evidence.*

---

## Cytotoxicity

Selinexor's predicted indications in this pack are exclusively oncologic (multiple breast cancer subtypes, lung carcinoma, gestational trophoblastic neoplasm, neuroblastoma, schwannoma), and its stated mechanism (inducing nuclear retention of tumor-suppressor proteins to kill malignant cells) is an antineoplastic mechanism. This section is therefore included.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Selective Inhibitor of Nuclear Export (SINE), XPO1/exportin-1 inhibitor (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

Please refer to the SmPC for safety information.

**Critical data gap:** this Evidence Pack flags TFDA label warnings/contraindications as a **Blocking**-severity gap (DG001) — safety data is entirely absent (key warnings, contraindications, and DDI records are all unpopulated), which by itself prevents this candidate from entering the S1 safety-screening stage regardless of predicted-indication strength.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking-severity safety data gap (DG001 — no TFDA/SmPC warnings, contraindications, or DDI data) prevents S1 safety screening for the drug at all, independent of which indication is pursued.
- Even the best-supported predicted indication (PR-negative/triple-negative breast cancer, rank 3, L3) rests on a single completed Phase 2 trial with only 10 patients — informative but not sufficient to justify progression past a research-question stage.
- Two other candidates with real trial data (squamous cell lung carcinoma) show a negative/uncertain signal (one terminated, one withdrawn), and the remaining seven candidates are either weakly indirect (L4) or unsupported model output (L5), including one likely embedding-noise prediction (drug-induced osteoporosis) despite its top TxGNN score.

**To proceed, the following is needed:**
- Resolve DG001: obtain the Selinexor SmPC/label (warnings, contraindications, DDI) from TFDA/EMA to complete S1 safety screening
- Resolve DG002: obtain confirmed mechanism-of-action documentation from DrugBank to formally populate `original_moa`
- For PR-negative/TNBC breast cancer: seek additional or larger trial data beyond the n=10 pilot before advancing past "Research Question"
- Determine the termination reason for NCT02213133 (squamous cell lung carcinoma) before considering that indication further
- Re-run literature retrieval for "breast tumor luminal A or B" with corrected search terms — current results are false positives
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

