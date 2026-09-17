---
layout: default
title: Ruxolitinib
parent: High Evidence (L1-L2)
nav_order: 524
evidence_level: L2
indication_count: 10
---

# Ruxolitinib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Ruxolitinib: From Myelofibrosis to Hemophagocytic Lymphohistiocytosis

## One-Sentence Summary

> Ruxolitinib is a JAK1/2 inhibitor internationally indicated for myeloproliferative neoplasms such as myelofibrosis (formal Taiwan/EU regulatory and MOA data for this drug were not available in the current Evidence Pack).
> The TxGNN model, together with mechanistic and clinical evidence, points to **Hemophagocytic Lymphohistiocytosis (HLH)** — particularly infection-associated and malignancy-associated forms — as a strong repurposing candidate,
> supported by **2 registered clinical trials** and **20 publications**, including guideline citations, cohort studies, and murine mechanism studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this Evidence Pack (drug not currently marketed in this jurisdiction). Ruxolitinib is internationally approved for myelofibrosis, polycythemia vera, and steroid‑refractory graft‑versus‑host disease. |
| Predicted New Indication | Hemophagocytic Lymphohistiocytosis (infection-associated; closely related to malignancy-associated HLH, rank 9) |
| TxGNN Prediction Score | 99.32% (rank 6974 of 32,368 pairs) |
| Evidence Level | L2 |
| EU Market Status | Not marketed (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The evidence pack does not include a formal `original_moa` entry (flagged as a High-severity data gap, DG002). However, the repurposing rationale fields attached to multiple predicted indications consistently identify Ruxolitinib as a **JAK1/2 inhibitor**, a mechanism that is well established in the literature for this molecule. JAK1/2 inhibition blocks intracellular signaling downstream of pro-inflammatory cytokines such as IFN-γ and IL-6 — the same cytokines that drive the hyperinflammatory "cytokine storm" central to HLH pathophysiology.

Among the ten TxGNN-predicted indications in this pack, most (PEComa, lymphangioleiomyomatosis, familial rhabdoid tumor, etc.) are mTOR- or chromatin-remodeling-driven tumors with no plausible JAK-STAT connection, and correspondingly carry only L5 (prediction-only) evidence and a "Hold" recommendation. In contrast, the two HLH-related predictions (rank 9: malignancy-associated HLH; rank 10: infection-associated HLH) sit on a biologically coherent axis: HLH is a cytokine-storm syndrome directly downstream of the JAK-STAT pathway that Ruxolitinib targets, and this mechanistic link is corroborated by murine mechanism studies (PMID 31015190, PMID 37228616) and multiple clinical cohorts already using Ruxolitinib off-label or in trials for HLH.

This makes the HLH indication qualitatively different from the other candidates on this list: it is not a pure knowledge-graph inference but a hypothesis already being tested in prospective clinical trials and supported by a substantial body of published clinical experience.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04424056](https://clinicaltrials.gov/study/NCT04424056) | Phase 3 | Unknown | 216 | Randomized trial of Anakinra/Tocilizumab ± Ruxolitinib in severe stage 2b/3 COVID-19-associated hyperinflammatory disease (HLH-spectrum); outcome status not yet reported. |
| [NCT07424222](https://clinicaltrials.gov/study/NCT07424222) | Phase 1 | Not yet recruiting | 16 | Pilot study of oral Ruxolitinib for Immune Effector Cell-Associated HLH-like Syndrome (IEC-HS) after CAR-T therapy; evaluating safety, efficacy, optimal duration, and immunological biomarkers. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34605776](https://pubmed.ncbi.nlm.nih.gov/34605776/) | 2022 | Guideline/Consensus | Critical Care Medicine | Consensus guideline on recognition, diagnosis, and management of HLH in critically ill children and adults. |
| [35344583](https://pubmed.ncbi.nlm.nih.gov/35344583/) | 2022 | Cohort | Blood | Prospective study (ChiCTR2000031702) of Ruxolitinib as first-line, response-stratified therapy in pediatric HLH. |
| [40665481](https://pubmed.ncbi.nlm.nih.gov/40665481/) | 2025 | Cohort | British Journal of Haematology | Retrospective comparison of Ruxolitinib-based regimen (n=53) vs. adjusted HLH-94 chemotherapy (n=42) in pediatric EBV-HLH. |
| [37787838](https://pubmed.ncbi.nlm.nih.gov/37787838/) | 2023 | Cohort | Annals of Hematology | Compassionate-use analysis of sintilimab + Ruxolitinib in 12 adults with EBV-associated HLH. |
| [32732367](https://pubmed.ncbi.nlm.nih.gov/32732367/) | 2021 | Pilot Study | Haematologica | Pilot study of Ruxolitinib as front-line therapy in 12 children with secondary HLH. |
| [31015190](https://pubmed.ncbi.nlm.nih.gov/31015190/) | 2019 | Mechanistic | Blood | Mechanism-of-action study showing Ruxolitinib dampens T-cell/IFN-γ overactivation in murine HLH models. |
| [40360445](https://pubmed.ncbi.nlm.nih.gov/40360445/) | 2025 | Review | Hematology (Amsterdam) | Review of EBV infection triggering HLH in XIAP deficiency. |
| [31943120](https://pubmed.ncbi.nlm.nih.gov/31943120/) | 2020 | Review | QJM | Review of adult HLH diagnosis and treatment. |
| [37702780](https://pubmed.ncbi.nlm.nih.gov/37702780/) | 2023 | Review | Innere Medizin | Review of HLH treatment in ICU patients, including targeted/JAK-based therapy. |
| [34353999](https://pubmed.ncbi.nlm.nih.gov/34353999/) | 2021 | Review | Current Opinion in Critical Care | Review of JAK inhibitors (including Ruxolitinib) in hospitalized COVID-19/hyperinflammatory states. |

---

## EU Market Information

This drug currently has **no marketing authorization on file** in this Evidence Pack (`market_status`: Not marketed / Not marketed; `total_licenses`: 0). No license records are available to summarize.

---

## Safety Considerations

Please refer to the SmPC for safety information.

**Note:** Drug-level TFDA warnings/contraindications data is flagged as a **Blocking** data gap (DG001) in this Evidence Pack — this prevents the candidate from formally entering the S1 safety pre-assessment stage, independent of how strong the efficacy evidence is.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HLH indication is mechanistically coherent and backed by an unusually rich clinical literature (20 publications, including guideline citations and multiple cohort studies) plus 2 registered trials — one Phase 3 (status unknown, outcome unreported) and one Phase 1 (not yet recruiting). However, a **Blocking** data gap on TFDA warnings/contraindications means the entity-level safety assessment cannot begin, and the drug is not currently marketed in this jurisdiction (0 licenses). The recommendation must therefore be Hold until the safety gap is resolved, regardless of the promising efficacy signal.

**To proceed, the following is needed:**
- TFDA/SmPC label (warnings, contraindications, drug interactions) — blocking gap, DG001
- Confirmed outcome/status update for NCT04424056 (Phase 3 RCT)
- Continued monitoring of NCT07424222 (Phase 1 IEC-HS trial) as it opens recruitment
- Formal DrugBank-sourced MOA and original indication data (DG002)
- Assessment of local regulatory pathway, since the drug currently holds no marketing authorization in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

