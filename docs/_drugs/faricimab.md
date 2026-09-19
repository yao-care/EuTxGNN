---
layout: default
title: Faricimab
parent: High Evidence (L1-L2)
nav_order: 246
evidence_level: L1
indication_count: 10
---

# Faricimab
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

# Faricimab: From Diabetic Macular Edema/nAMD to Diabetic Retinopathy

> **Selection note**: In this TxGNN Top-10 original prediction round, the highest-scoring candidates (such as primary release disorder of platelets, pseudo-von Willebrand disease, etc.) are all noise items with unreasonable mechanisms and zero evidence (the model extrapolates based on organ/graph associations; the scoring card also flags these as Hold). This report focuses on the only item in the Top-10 with substantive clinical and literature evidence support—**Diabetic Retinopathy** (original rank 8, score 96.75%), with supplementary mention of mechanistically similar severe nonproliferative diabetic retinopathy (rank 6) as an early signal.

## One-Sentence Summary

Faricimab (Vabysmo) is a bispecific monoclonal antibody that simultaneously neutralizes VEGF-A and Angiopoietin-2 via intravitreal injection and is approved for wet age-related macular degeneration (nAMD) and diabetic macular edema (DME). The TxGNN model predicts its application can extend to the broader spectrum of **Diabetic Retinopathy (DR)**, which is currently supported by **25 clinical trials** and **20 literature reports**, including 4 completed Phase 3 pivotal trials.

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Wet age-related macular degeneration (nAMD), diabetic macular edema (DME) (per literature PMID 35474059 "Faricimab: First Approval" and YOSEMITE/RHINE, TENAYA/LUCERNE trial registration information; no approved indication recorded in Taiwan) |
| Predicted New Indication | Diabetic Retinopathy |
| TxGNN Prediction Score | 96.75% |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed |
| Number of Authorizations (Taiwan) | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Faricimab is a bispecific monoclonal antibody that simultaneously neutralizes VEGF-A and Angiopoietin-2, inhibiting retinal neovascularization and vascular leakage via intravitreal injection. This is the core mechanism verified in nAMD and DME. (The original `original_moa` field is marked as [Data Gap]; the above mechanism description supplements from publicly known drug information, not database-native field evidence.)

Diabetic retinopathy (DR) and DME are essentially part of the same disease spectrum—DME is a macular complication of DR, and both share the core pathophysiology of "retinal ischemia driving VEGF/Ang-2 upregulation." Therefore, extending indication from DME to overall DR (including nonproliferative and proliferative stages) represents natural extrapolation of the same mechanism within the same organ system, not a novel mechanistic hypothesis.

Signals supporting this extension have materialized into clinical trials: the MAGIC trial (NCT05681884) is specifically designed as a Phase 2 study targeting nonperfusion areas in nonproliferative DR (NPDR); NCT06790784 compares Faricimab + PRP with conventional vitrectomy treating proliferative DR (PDR) at Phase 3 scale. This shows that the industry has advanced this hypothesis to prospective clinical validation rather than merely model inference.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03622593](https://clinicaltrials.gov/study/NCT03622593) | Phase 3 | Completed | 951 | RHINE: Faricimab vs Aflibercept in DME treatment; efficacy/safety/PK registration trial |
| [NCT03622580](https://clinicaltrials.gov/study/NCT03622580) | Phase 3 | Completed | 940 | YOSEMITE: twin registration trial with RHINE; DME 8-week dosing interval vs Aflibercept |
| [NCT03823300](https://clinicaltrials.gov/study/NCT03823300) | Phase 3 | Completed | 658 | LUCERNE: nAMD indication pivotal trial, same mechanism evidence forming approval basis |
| [NCT03823287](https://clinicaltrials.gov/study/NCT03823287) | Phase 3 | Completed | 671 | TENAYA: nAMD pivotal trial, paired control with LUCERNE |
| [NCT05224102](https://clinicaltrials.gov/study/NCT05224102) | Phase 4 | Active, not recruiting | 218 | Post-marketing study evaluating treatment response in untreated, underrepresented DME populations |
| [NCT05681884](https://clinicaltrials.gov/study/NCT05681884) | Phase 2 | Active, not recruiting | 179 | MAGIC: randomized controlled trial specifically targeting nonperfusion areas in nonproliferative DR (NPDR) |
| [NCT06790784](https://clinicaltrials.gov/study/NCT06790784) | Phase 3 | Recruiting | 426 | Comparison of Faricimab + PRP vs vitrectomy + laser treatment for proliferative DR (PDR) |
| [NCT04597918](https://clinicaltrials.gov/study/NCT04597918) | Phase 2B | Completed | 99 | ALTIMETER: exploratory study of aqueous humor biomarkers and multimodal imaging in DME patients |
| [NCT05476926](https://clinicaltrials.gov/study/NCT05476926) | N/A | Active, not recruiting | 6000 | VOYAGER: multiregional real-world long-term data collection (covering nAMD/DME) |
| [NCT06439576](https://clinicaltrials.gov/study/NCT06439576) | N/A | Recruiting | 1000 | Farseeing: China real-world study covering DME/RVO/nAMD treatment patterns and safety |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38158159](https://pubmed.ncbi.nlm.nih.gov/38158159/) | 2024 | RCT | Ophthalmology | YOSEMITE/RHINE two-year outcomes: efficacy and safety under treat-and-extend dosing |
| [36246184](https://pubmed.ncbi.nlm.nih.gov/36246184/) | 2022 | RCT | Ophthalmology Science | YOSEMITE/RHINE study design and rationale |
| [38852921](https://pubmed.ncbi.nlm.nih.gov/38852921/) | 2024 | RCT | Ophthalmology | Efficacy analysis of Faricimab vs Aflibercept in subgroup with worse baseline vision |
| [36012690](https://pubmed.ncbi.nlm.nih.gov/36012690/) | 2022 | RCT | Int J Mol Sci | Comparative review of Aflibercept and Faricimab in nAMD/DME treatment |
| [35085503](https://pubmed.ncbi.nlm.nih.gov/35085503/) | 2022 | Cohort | Lancet | YOSEMITE/RHINE: efficacy, durability, and safety with 16-week extended dosing |
| [37751021](https://pubmed.ncbi.nlm.nih.gov/37751021/) | 2023 | Review | Advances in Therapy | Systematic literature review and network meta-analysis of DME treatment |
| [35474059](https://pubmed.ncbi.nlm.nih.gov/35474059/) | 2022 | Review | Drugs | Faricimab first approval (nAMD, DME), establishing original indications and mechanism |
| [30905643](https://pubmed.ncbi.nlm.nih.gov/30905643/) | 2019 | Preclinical | Ophthalmology | BOULEVARD Phase 2: Faricimab vs Ranibizumab in DME treatment |
| [38847896](https://pubmed.ncbi.nlm.nih.gov/38847896/) | 2024 | Review | Graefe's Archive | Comprehensive review of Faricimab from preclinical studies to Phase 3 outcomes |
| [35818801](https://pubmed.ncbi.nlm.nih.gov/35818801/) | 2022 | Review | Expert Opin Biol Ther | Review of efficacy and safety of intravitreal anti-VEGF therapy in diabetic retinopathy |

## Taiwan Market Information

Taiwan currently has no marketing approval records for Faricimab (`market_status`: Not marketed, `total_licenses`: 0).

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Faricimab has already completed 4 Phase 3 RCTs (YOSEMITE, RHINE, TENAYA, LUCERNE, meeting L1 standard) under the same neovascularization mechanism (dual VEGF-A/Ang-2 inhibition), and Phase 2 (MAGIC, NPDR) and Phase 3 (NCT06790784, PDR) trials are already specifically targeting broader diabetic retinopathy populations. The mechanistic extrapolation is sound and the evidence chain is complete, but it has not yet obtained Taiwan market approval, and Taiwan prescribing information safety data are lacking.

**To proceed, the following is needed:**
- Complete TFDA prescribing information warnings, contraindications, and drug-drug interactions data (DG001, Blocking)
- Complete formal MOA/DrugBank mechanism data to finalize mechanistic association analysis (DG002, High)
- Track final efficacy readouts from MAGIC (NCT05681884) and NCT06790784 to confirm direct evidence of DR (including NPDR/PDR) indication extension
- Assess regulatory pathway and timeline for Taiwan drug license application/indication expansion

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

