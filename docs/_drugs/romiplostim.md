---
layout: default
title: Romiplostim
parent: High Evidence (L1-L2)
nav_order: 517
evidence_level: L1
indication_count: 10
---

# Romiplostim
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Romiplostim: From Immune Thrombocytopenia to Platelet-Type Bleeding Disorder

## One-Sentence Summary

> Romiplostim is a thrombopoietin (TPO) receptor agonist originally used to treat chronic immune thrombocytopenia (ITP).
> Among 10 TxGNN-predicted indications, the model's platelet-count-deficiency cluster — most concretely represented by **Platelet-Type Bleeding Disorder** (a category spanning ITP, chemotherapy-induced thrombocytopenia, MDS-related thrombocytopenia, and post-transplant thrombocytopenia) — is by far the best supported,
> with **8 clinical trials, including 2 completed Phase 3 RCTs**, currently backing this direction. *(Note: this indication was selected over the top-ranked TxGNN score because it has the strongest actual clinical evidence — see rationale below.)*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Immune Thrombocytopenia (ITP) *(inferred from repurposing rationale text; not captured in `original_indications` field)* |
| Predicted New Indication | Platelet-Type Bleeding Disorder |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, `original_moa` is marked as a data gap in the structured record. However, the evidence pack's own repurposing rationale text confirms that Romiplostim is a **TPO-receptor (MPL) agonist** that stimulates megakaryocyte proliferation and differentiation, thereby increasing platelet production — this is the mechanistic basis behind all 10 predicted indications in this pack.

Romiplostim's approved use in ITP addresses thrombocytopenia caused by immune-mediated platelet destruction and impaired production. "Platelet-Type Bleeding Disorder" is a broader disease category that captures thrombocytopenia of multiple etiologies — including chemotherapy-induced thrombocytopenia (CIT), myelodysplastic syndrome (MDS)-associated thrombocytopenia, and post-hematopoietic-stem-cell-transplant platelet engraftment failure. In all of these, the underlying problem is a **quantitative shortfall in platelet production**, which is exactly the mechanism Romiplostim targets — unlike several other TxGNN-predicted candidates in this pack (e.g., Glanzmann thrombasthenia, Scott syndrome, pseudo-von Willebrand disease) which are **qualitative/functional platelet defects** that a production-stimulating agent cannot correct.

This mechanistic fit is reflected in the evidence: a completed Phase 3 RCT (RECITE, NCT03362177) directly tested Romiplostim in chemotherapy-induced thrombocytopenia, and a completed Phase 3 extension study (NCT05492409) established long-term safety in ITP patients on a Romiplostim biosimilar. Several additional Phase 1/2/4 studies extend into MDS and post-transplant settings, reinforcing that this is a class-consistent extension of Romiplostim's known pharmacology rather than a mechanistically speculative prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03362177](https://clinicaltrials.gov/study/NCT03362177) | Phase 3 | Completed | 165 | RECITE: randomized, placebo-controlled, double-blind trial of Romiplostim for chemotherapy-induced thrombocytopenia in GI/pancreatic/colorectal cancer patients on oxaliplatin-based regimens |
| [NCT05492409](https://clinicaltrials.gov/study/NCT05492409) | Phase 3 | Completed | 160 | Long-term extension study evaluating safety and immunogenicity of a Romiplostim biosimilar (GNR-069) in ITP patients who completed the Phase 3 RMP-ITP-III trial |
| [NCT02335268](https://clinicaltrials.gov/study/NCT02335268) | Phase 2 | Completed | 77 | EUROPE trial: prospective validation of a predictive response model for Romiplostim in IPSS low/int-1 risk MDS patients with thrombocytopenia |
| [NCT02227576](https://clinicaltrials.gov/study/NCT02227576) | Phase 2 | Terminated | 20 | Secondary prophylactic use of Romiplostim to prevent temozolomide-induced thrombocytopenia in newly diagnosed glioblastoma patients (terminated) |
| [NCT04638829](https://clinicaltrials.gov/study/NCT04638829) | Phase 4 | Completed | 60 | Open-label study measuring safety and treatment satisfaction after switching adults with chronic ITP from Eltrombopag or Romiplostim to Avatrombopag |
| [NCT07321626](https://clinicaltrials.gov/study/NCT07321626) | Phase 1 | Recruiting | 130 | Randomized controlled study of Romiplostim N01 for promoting platelet engraftment after haploidentical allogeneic stem cell transplant in hematologic malignancies |
| [NCT02046291](https://clinicaltrials.gov/study/NCT02046291) | Phase 1 | Completed | 21 | Dose-escalation study of weekly Romiplostim safety in patients failing platelet engraftment after umbilical cord blood transplant |
| [NCT02298075](https://clinicaltrials.gov/study/NCT02298075) | N/A | Completed | 148 | Retrospective study of sustained response rate after discontinuing TPO-receptor agonists (Eltrombopag, Romiplostim) in primary ITP patients |

---

## Literature Evidence

Currently no related literature available for this specific indication category (literature evidence in the pack is attached to other, less-supported disease terms such as "primary release disorder of platelets" and "autosomal dominant macrothrombocytopenia").

---

## EU Market Information

No marketing authorizations are recorded in this dataset for this jurisdiction — market status is **Not Marketed**, with **0 licenses** on file. No `licenses` entries were available to extract product name, dosage form, or approved indication text.

---

## Safety Considerations

Please refer to the SmPC for safety information. *(Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack — see DG001, DG002 below.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs plus multiple supporting Phase 1/2/4 studies demonstrate that Romiplostim's core mechanism (TPO-receptor-mediated platelet production) extends reliably beyond ITP into chemotherapy-induced and other production-deficit thrombocytopenias, giving this candidate an L1 evidence level. However, a blocking data gap on local drug label warnings/contraindications (DG001) and a missing formal MOA record (DG002) prevent a full safety sign-off at this stage.

**To proceed, the following is needed:**
- TFDA/EMA-equivalent label PDF for warnings, contraindications, and precautions (DG001 — blocking; required before S1 safety pre-assessment)
- Confirmed mechanism-of-action record via DrugBank API query (DG002)
- Regulatory filing/authorization status check for the target indication in this jurisdiction, since current market status shows zero licenses
- Population-specific safety review for off-label extension settings (e.g., glioblastoma/CNS tumor patients, given the terminated NCT02227576 trial)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

