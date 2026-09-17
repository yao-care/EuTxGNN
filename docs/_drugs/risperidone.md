---
layout: default
title: Risperidone
parent: High Evidence (L1-L2)
nav_order: 511
evidence_level: L1
indication_count: 10
---

# Risperidone
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

Using no additional skills — this is a direct content-generation task with a fully specified template; proceeding straight to the report.

**Note on indication selection:** `predicted_indications[0]` (rank 1, "gaze palsy, familial horizontal, with progressive scoliosis") has an L5 evidence level, zero supporting trials/literature, and its own rationale states "no known relationship" to risperidone's mechanism — it is not reportable. I selected **rank 6, "major affective disorder"**, which has the highest evidence level (L1) and clearest actionable recommendation in this pack, as the report's primary candidate.

---

# Risperidone: From Schizophrenia to Major Affective Disorder

## One-Sentence Summary

> Risperidone is an atypical antipsychotic internationally established for schizophrenia and bipolar mania (5-HT2A/D2 receptor antagonism), though a formal EU authorization record is not present in this dataset.
> The TxGNN model predicts it may be effective for **Major Affective Disorder**, including treatment-resistant depression and bipolar disorder,
> with **34 clinical trials** and **20 publications** currently associated with this direction, including a completed 630-patient Phase 3 RCT.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in EU authorization data on file (no licenses recorded); internationally established use is schizophrenia and bipolar mania |
| Predicted New Indication | Major Affective Disorder |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L1 |
| EU Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not available in this dataset. Based on known pharmacology, risperidone is an atypical antipsychotic acting via combined dopamine D2 and serotonin 5-HT2A receptor antagonism, a mechanism established for schizophrenia and bipolar mania.

This same receptor profile underlies the drug class effect of "second-generation antipsychotic augmentation" in major depressive disorder — a strategy already used clinically when patients fail first-line antidepressants (SSRIs/SNRIs). Other atypical antipsychotics in this class (aripiprazole, quetiapine) already carry regulatory approval for this exact augmentation use, making risperidone's extension to major affective disorder mechanistically consistent rather than a novel biological hypothesis.

The evidence base reflects this: a large, completed Phase 3 double-blind RCT (n=630) directly tested risperidone augmentation in antidepressant-refractory MDD, and multiple additional Phase 3/4 RCTs and network meta-analyses support its role in bipolar depression, bipolar mania relapse prevention, and treatment-resistant unipolar depression.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) | Phase 3 | Completed | 630 | Double-blind adjunctive risperidone vs. placebo in MDD with sub-optimal response to antidepressant therapy |
| [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) | Phase 3 | Completed | 258 | Risperidone augmentation of SSRI monotherapy in unipolar treatment-resistant depression, including long-term maintenance effect |
| [NCT00391222](https://clinicaltrials.gov/study/NCT00391222) | Phase 3 | Completed | 585 | Risperidone long-acting injectable (LAI) monotherapy vs. placebo for prevention of mood episodes in bipolar I disorder |
| [NCT00277654](https://clinicaltrials.gov/study/NCT00277654) | Phase 3 | Completed | 111 | Risperidone monotherapy vs. placebo in bipolar disorder with comorbid panic/generalized anxiety disorder |
| [NCT00667745](https://clinicaltrials.gov/study/NCT00667745) | Phase 4 | Completed | 283 | LiTMUS effectiveness trial; lithium-optimized regimens vs. comparators (including risperidone) in bipolar disorder |
| [NCT00174577](https://clinicaltrials.gov/study/NCT00174577) | Phase 3 | Unknown | 84 | Risperidone augmentation in antidepressant partial/non-responders |
| [NCT00203723](https://clinicaltrials.gov/study/NCT00203723) | Phase 4 | Terminated | 45 | Combined ECT + risperidone vs. ECT alone for treatment-resistant depression |
| [NCT01282632](https://clinicaltrials.gov/study/NCT01282632) | Phase 1/2 | Completed | 42 | Pilot RCT: risperidone vs. olanzapine as add-on to SSRIs in treatment-resistant depression |
| [NCT00167479](https://clinicaltrials.gov/study/NCT00167479) | Phase 4 | Completed | 60 | Risperidone monotherapy in ambulatory bipolar disorder with comorbid anxiety disorder |
| [NCT00571688](https://clinicaltrials.gov/study/NCT00571688) | Phase 4 | Completed | 50 | Risperidone Consta (LAI) vs. treatment-as-usual for relapse/rehospitalization prevention in bipolar disorder |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic review/Network meta-analysis | J Affect Disord | Compared efficacy/discontinuation of augmentation agents (incl. risperidone) in treatment-resistant depression |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Systematic review/Meta-analysis | J Psychopharmacol | Evaluated adjunctive/combination treatments for early-stage treatment-resistant depression |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Cochrane Review | Cochrane Database Syst Rev | Second-generation antipsychotics (incl. risperidone) for MDD and dysthymia |
| [17975181](https://pubmed.ncbi.nlm.nih.gov/17975181/) | 2007 | RCT | Ann Intern Med | Randomized trial of risperidone for treatment-refractory major depressive disorder |
| [20486830](https://pubmed.ncbi.nlm.nih.gov/20486830/) | 2010 | RCT/Open-label extension | Expert Opin Pharmacother | Risperidone LAI as monotherapy and adjunctive therapy in maintenance treatment of bipolar I disorder |
| [23554581](https://pubmed.ncbi.nlm.nih.gov/23554581/) | 2013 | Meta-analysis | PLoS Medicine | Adjunctive atypical antipsychotic treatment for MDD: depression, quality of life, and safety outcomes |
| [24919175](https://pubmed.ncbi.nlm.nih.gov/24919175/) | 2014 | Meta-analysis | Braz J Med Biol Res | Efficacy/tolerability of atypical antipsychotic (incl. risperidone) augmentation of antidepressants, 17 trials, n=3807 |
| [25295435](https://pubmed.ncbi.nlm.nih.gov/25295435/) | 2014 | Nationwide population-based study | J Clin Psychiatry | Effectiveness of SGA augmentation (incl. risperidone) for MDD in a national cohort |
| [15291687](https://pubmed.ncbi.nlm.nih.gov/15291687/) | 2004 | Case series/Cohort | J Clin Psychiatry | Effectiveness of olanzapine, risperidone, quetiapine, ziprasidone as augmentation in treatment-resistant MDD |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Review | J Psychopharmacol | Efficacy/tolerability of combination treatments for MDD: antidepressants + second-generation antipsychotics vs. esketamine vs. lithium |

## EU Market Information

No active EU marketing authorization is currently on file for risperidone in this dataset (`market_status: Not Marketed`, 0 licenses recorded). This may reflect the absence of a centralized EMA procedure rather than true unavailability, since risperidone is a long-genericized molecule typically authorized via national/decentralized procedures across EU member states — this should be verified against national regulatory registries before final decision-making.

## Safety Considerations

Please refer to the SmPC for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two or more completed Phase 3 RCTs (n=630 and n=258) directly support risperidone augmentation in treatment-resistant/unipolar depression, reinforced by multiple systematic reviews and network meta-analyses and additional Phase 3/4 RCTs in bipolar disorder — meeting the L1 evidence bar. However, the absence of confirmed EU marketing status and safety/label data prevents unconditional "Go."

**To proceed, the following is needed:**
- TFDA/EMA-equivalent product label warnings and contraindications (DG001 — currently blocking S1 safety screening)
- Confirmed DrugBank mechanism-of-action documentation (DG002)
- Verification of EU marketing authorization status via national registries (current record shows "Not Marketed")
- Drug-drug interaction data (current DDI query returned no results)
- Population-specific dosing/monitoring protocol for augmentation use in major affective disorder (e.g., metabolic and prolactin monitoring given antipsychotic class effects)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

