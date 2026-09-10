---
layout: default
title: Fluticasone Propionate
parent: 僅模型預測 (L5)
nav_order: 262
evidence_level: L5
indication_count: 10
---

# Fluticasone Propionate
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

# Fluticasone Propionate: From No Taiwan-Registered Indication to Atopic Dermatitis

## One-Sentence Summary

Fluticasone propionate is a topical corticosteroid that currently holds **no marketing authorization in Taiwan** in this dataset, so its original approved indication cannot be extracted from local regulatory records. Among 10 TxGNN-predicted indications, the model's single highest-scoring candidate ("2-hydroxyethyl methacrylate sensitization") has zero supporting studies, so this report instead evaluates the **best-evidenced candidate, Atopic Dermatitis**, which is backed by **11 clinical trials** and **20 publications**, including a completed Phase 3 RCT.

> **Note on selection**: The dataset's top-ranked TxGNN prediction by raw score has no clinical trial or literature support (evidence level L5, "Hold"). Atopic Dermatitis (rank 7 by score, but rank 1 by evidence strength) is presented here because it is the only candidate that reaches an actionable evidence tier (L1) and a "Proceed with Guardrails" recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no marketing authorization on file for this drug in Taiwan |
| Predicted New Indication | Atopic Dermatitis |
| TxGNN Prediction Score | 95.32% |
| Evidence Level | L1 |
| EU/TW Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed original mechanism-of-action data for this drug record is not available (flagged as a High-severity data gap, DG002). Based on the evidence collected for the Atopic Dermatitis prediction itself, fluticasone propionate is a high-potency topical glucocorticoid that acts by activating the glucocorticoid receptor, suppressing pro-inflammatory cytokine expression, and reducing cutaneous inflammation and pruritus — the standard mechanism underlying topical corticosteroid therapy for inflammatory skin disease.

This mechanistic pathway aligns directly with Atopic Dermatitis, a chronic relapsing inflammatory skin condition for which topical corticosteroids are first-line therapy internationally (marketed elsewhere as Cutivate). The evidence pack notes that this indication is already an approved use for fluticasone propionate in multiple other markets; its absence from this local dataset likely reflects a data-collection gap in Taiwan's registry rather than a lack of biological plausibility.

By contrast, the model's numerically highest-scoring prediction (contact sensitization to 2-hydroxyethyl methacrylate) and several other candidates (vulvar inverted follicular keratosis, alopecia mucinosa, telogen effluvium, hereditary hypotrichosis) have mechanistic links rated as weak or purely speculative by the source rationale text, with no corroborating trials or literature — these remain at "Hold" status.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01772056](https://clinicaltrials.gov/study/NCT01772056) | Phase 3 | Terminated | 54 | Twice-weekly fluticasone propionate 0.05% cream as maintenance therapy to reduce AD relapse in children after acute flare stabilization |
| [NCT00690105](https://clinicaltrials.gov/study/NCT00690105) | Phase 4 | Completed | 577 | Head-to-head tacrolimus 0.1% vs. fluticasone 0.005% ointment in adults with moderate-severe facial AD ("red face" lesions) |
| [NCT00689832](https://clinicaltrials.gov/study/NCT00689832) | Phase 4 | Completed | 487 | Tacrolimus 0.03% vs. fluticasone 0.005% ointment in children ≥2 years with moderate-severe AD |
| [NCT01915914](https://clinicaltrials.gov/study/NCT01915914) | Phase 4 | Completed | 107 | Intermittent (twice-weekly) fluticasone 0.05% cream added to daily moisturizer to reduce relapse risk in stabilized pediatric AD |
| [NCT00119158](https://clinicaltrials.gov/study/NCT00119158) | Phase 4 | Completed | 90 | Combined pimecrolimus + fluticasone (Cutivate) cream in severe AD lesions |
| [NCT00616538](https://clinicaltrials.gov/study/NCT00616538) | Phase 4 | Completed | 121 | Fluticasone 0.05% vs. EpiCeram barrier-repair cream in pediatric AD |
| [NCT00546000](https://clinicaltrials.gov/study/NCT00546000) | Phase 4 | Completed | 56 | Open-label HPA-axis safety study of fluticasone lotion 0.05% in pediatric AD |
| [NCT03742414](https://clinicaltrials.gov/study/NCT03742414) | Phase 2 | Active, not recruiting | 398 | Proactive fluticasone + skin barrier cream vs. reactive therapy in infants to prevent AD progression and food allergy |
| [NCT04706559](https://clinicaltrials.gov/study/NCT04706559) | N/A | Completed | 98 | Probiotic supplementation trial in pediatric AD (fluticasone not the primary intervention) |
| [NCT00426283](https://clinicaltrials.gov/study/NCT00426283) | Phase 2 | Completed | 42 | High-dose swallowed fluticasone vs. placebo for eosinophilic esophagitis (different indication, included for completeness) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29373242](https://pubmed.ncbi.nlm.nih.gov/29373242/) | 2018 | RCT | Allergologia et Immunopathologia | Intermittent fluticasone 0.05% cream vs. vehicle reduces relapse risk in stabilized pediatric AD |
| [33150035](https://pubmed.ncbi.nlm.nih.gov/33150035/) | 2020 | Open-label comparative study | Dermatology Practical & Conceptual | Compares proactive topical fluticasone vs. tacrolimus for efficacy and safety in AD |
| [11862174](https://pubmed.ncbi.nlm.nih.gov/11862174/) | 2002 | Cohort/Safety study | J Am Acad Dermatol | Fluticasone 0.05% cream shown safe in severe/extensive AD in infants as young as 3 months |
| [27543211](https://pubmed.ncbi.nlm.nih.gov/27543211/) | 2016 | Cohort | J Am Acad Dermatol | Fluticasone cream plus bleach baths alters cutaneous microbiome in childhood AD |
| [21977914](https://pubmed.ncbi.nlm.nih.gov/21977914/) | 2012 | Review | JEADV | Reviews fluticasone's high therapeutic index for intervention and maintenance treatment of AD |
| [15608497](https://pubmed.ncbi.nlm.nih.gov/15608497/) | 2005 | Review | Skin Pharmacology and Physiology | Reviews safety and efficacy of fluticasone across dermatological disorders including AD |
| [12207596](https://pubmed.ncbi.nlm.nih.gov/12207596/) | 2002 | Clinical study | British Journal of Dermatology | Intermittent dosing of fluticasone cream reduces long-term AD relapse risk |
| [14522623](https://pubmed.ncbi.nlm.nih.gov/14522623/) | 2003 | Comparative study | J Dermatological Treatment | Two multicentre RCTs of fluticasone 0.05% cream for acute and maintenance AD treatment in children |
| [17225720](https://pubmed.ncbi.nlm.nih.gov/17225720/) | 2007 | Comparative study | Annals of Allergy, Asthma & Immunology | Fluticasone reduces Staphylococcus colonization in AD, with or without antibiotics |
| [24655575](https://pubmed.ncbi.nlm.nih.gov/24655575/) | 2014 | Review | J Allergy and Clinical Immunology | Discusses induction of remission and subclinical inflammation treatment concepts in AD |

---

## EU Market Information

No marketing authorizations are on file for this drug (market status: Not Marketed; total authorizations: 0).

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The Atopic Dermatitis prediction is supported by an L1 evidence base — including a completed Phase 3 RCT and multiple Phase 4 comparative trials — and topical corticosteroids are an established standard of care for this condition elsewhere, making the mechanistic rationale strong. However, this drug currently has no Taiwan marketing authorization and two Blocking/High-severity data gaps remain unresolved.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any safety pre-assessment (S1) can proceed
- Confirmed mechanism-of-action documentation from DrugBank (DG002, High)
- Local regulatory pathway assessment given the current "Not Marketed" status in Taiwan
- Drug-drug interaction data (current DDI query returned no results)
- Anatomical/indication-fit clarification if the lower-evidence candidate "Polyp of Middle Ear" (L3, nasal-polyp evidence extrapolated to a different anatomical site) is also to be pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

