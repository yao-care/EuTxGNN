---
layout: default
title: Miglustat
parent: AI Predictions (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
---

# Miglustat
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

# Miglustat: From Gaucher Disease to Tay-Sachs Disease (GM2 Gangliosidosis)

## One-Sentence Summary

> Miglustat is an oral glucosylceramide synthase inhibitor (substrate reduction therapy) originally developed and approved for **type 1 Gaucher disease**.
> Among the 10 indications predicted by the TxGNN model for this drug, **Tay-Sachs disease (GM2 gangliosidosis)** is the only one supported by substantive real-world evidence,
> with **5 clinical trials** (including 2 completed Phase 3 studies) and **20 publications**, including one completed randomized controlled trial and one systematic review.
> The other 9 higher- or similarly-scored TxGNN predictions (e.g. autosomal ichthyosis, cholesteryl ester storage disease, Krabbe disease) currently have **zero supporting trials or literature** and remain pure AI-model hypotheses.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 1 Gaucher disease (per literature evidence in this pack; no formal marketing-authorization record available) |
| Predicted New Indication | Tay-Sachs disease (GM2 gangliosidosis) |
| TxGNN Prediction Score | 99.75% (rank 3216 of all drug–disease pairs) |
| Evidence Level | L2 (1 completed randomized controlled clinical study) |
| EU Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed structured MOA data for miglustat is marked as a data gap in this pack, but the literature evidence collected alongside the prediction fills in the picture: miglustat (N-butyldeoxynojirimycin) is an iminosugar that inhibits **glucosylceramide synthase**, the first committed enzyme in glycosphingolipid (GSL) biosynthesis. By slowing GSL production ("substrate reduction therapy"), it was originally approved for type 1 Gaucher disease, where excess glucosylceramide accumulates in macrophages (PMID 12808890).

Tay-Sachs disease is caused by deficiency of β-hexosaminidase A, leading to accumulation of **GM2 ganglioside** — itself a glycosphingolipid — predominantly in neurons. Because GM2 sits downstream of the same glycosphingolipid biosynthetic pathway that miglustat inhibits upstream, reducing precursor flux can, in principle, lower the substrate load presented to the deficient enzyme, potentially slowing disease progression (PMID 9103204, PMID 11227045, PMID 16763917).

This mechanistic logic has already been tested clinically rather than remaining purely theoretical: miglustat has been studied as substrate reduction therapy in both late-onset and infantile forms of GM2 gangliosidosis (Tay-Sachs and Sandhoff disease), including a completed randomized controlled trial in late-onset disease (PMID 19346952) and a 2023 systematic review (PMID 37209042). This places the Tay-Sachs prediction on considerably firmer ground than the other TxGNN candidates in this pack, most of which (e.g. cholesteryl ester storage disease, adrenal gland neoplasm) have no mechanistic or clinical support at all.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Phase 3 | Completed | 10 | Single and steady-state dosing PK/safety/tolerability of miglustat (Zavesca) in infantile-onset GM2 gangliosidosis (Tay-Sachs/Sandhoff); rationale that miglustat inhibits GM2 ganglioside formation and may delay symptom onset |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Phase 2 | Completed | 5 | PK of single and multiple oral doses of miglustat in juvenile GM2 gangliosidosis |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Phase 3 | Terminated | 30 | Miglustat therapeutic effects on neurological/systemic symptoms in infantile Sandhoff and Tay-Sachs disease |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Phase 4 | Terminated | 16 | Synergistic combination of miglustat + ketogenic diet in infantile/juvenile gangliosidoses (Syner-G), hypothesized to improve survival and neurodevelopmental outcomes |
| [NCT07399704](https://clinicaltrials.gov/study/NCT07399704) | Phase 2 | Recruiting | 21 | Long-term safety/PK/efficacy of nizubaglustat (a next-generation substrate reduction agent) in GM2 gangliosidosis and NPC patients, including a cohort transitioning from stable, full-dose miglustat |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | RCT | Genetics in Medicine | 12-month randomized, controlled trial of miglustat in late-onset Tay-Sachs disease, plus 24 months of extended treatment |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Systematic Review | European Journal of Neurology | Systematic review of efficacy and safety of miglustat in GM2 gangliosidosis; notes prior inconsistent results across studies |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Case Series | Neurology | Substrate reduction therapy (miglustat) in 2 patients with infantile Tay-Sachs; did not arrest neurologic deterioration but achieved measurable CSF drug levels and prevented macrocephaly |
| [16151419](https://pubmed.ncbi.nlm.nih.gov/16151419/) | 2005 | Case Report | Bone Marrow Transplantation | Allogeneic BMT followed by miglustat substrate reduction therapy in subacute Tay-Sachs disease |
| [32867370](https://pubmed.ncbi.nlm.nih.gov/32867370/) | 2020 | Review | International Journal of Molecular Sciences | Clinical features, pathophysiology, and current therapies (including substrate reduction) for GM2 gangliosidoses |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Review | Frontiers in Physiology | New therapeutic approaches to Tay-Sachs disease |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Natural History Study | Molecular Genetics and Metabolism | Timeline of clinical changes in infantile gangliosidoses; notes substrate reduction therapy with miglustat has been tried but limited by GI side effects |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Review | Current Opinion in Investigational Drugs | Miglustat drug profile: approved for type 1 Gaucher disease in EU (2002), also in development for Tay-Sachs, Fabry, and Niemann-Pick type C |
| [30743792](https://pubmed.ncbi.nlm.nih.gov/30743792/) | 2009 | Review | Expert Review of Endocrinology & Metabolism | Substrate reduction therapy with miglustat for glycosphingolipid storage disorders affecting the brain |
| [9103204](https://pubmed.ncbi.nlm.nih.gov/9103204/) | 1997 | Preclinical Study | Science | Foundational mouse study: N-butyldeoxynojirimycin (miglustat precursor compound) prevented GM2 accumulation and reduced neuronal storage in a Tay-Sachs mouse model |

---

## EU Market Information

No marketing authorizations for miglustat are recorded in this dataset (market status: **Not marketed**, 0 licenses on file). This may reflect an incomplete regulatory dataset rather than actual absence of the drug from the market — miglustat is marketed elsewhere as Zavesca® for type 1 Gaucher disease and Niemann-Pick type C disease. This should be confirmed against the primary regulatory source before proceeding.

---

## Safety Considerations

Please refer to the SmPC for safety information. Key warnings, contraindications, and drug-drug interaction data are not available in this evidence pack (flagged as a **Blocking** data gap — see Conclusion below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic rationale and clinical evidence base for miglustat in Tay-Sachs disease is meaningfully stronger than for any of the other 9 TxGNN-predicted indications in this pack — it includes a completed RCT, a 2023 systematic review, and 5 registered trials (2 completed Phase 3 studies), with an active successor-molecule trial (NCT07399704) still recruiting.
- However, the absence of TFDA/local label data (key warnings, contraindications, DDI) is flagged as a **Blocking** data gap (DG001) that prevents this candidate from entering the S1 safety pre-assessment stage, regardless of the efficacy signal.
- Efficacy results to date are also mixed: the infantile-onset trial (NCT03822013) was terminated, and case-series data (PMID 16434676) showed drug exposure in CSF but no arrest of neurologic deterioration, suggesting benefit may be restricted to late-onset/juvenile phenotypes.

**To proceed, the following is needed:**
- Retrieve and analyze the official SmPC/label (warnings, contraindications, DDI) to unblock the S1 safety pre-assessment (DG001).
- Confirm detailed MOA and PK/PD data via DrugBank API to strengthen the mechanistic-link analysis (DG002).
- Clarify actual EU/local marketing-authorization status, since "0 licenses" appears inconsistent with miglustat's known approval history for Gaucher disease and NPC.
- Monitor results from the ongoing NCT07399704 study, which directly compares outcomes in patients transitioning from full-dose miglustat.
- Stratify any future indication-expansion analysis by disease subtype (late-onset vs. infantile Tay-Sachs), given the divergent efficacy signals observed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

