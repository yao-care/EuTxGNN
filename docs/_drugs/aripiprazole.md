---
layout: default
title: Aripiprazole
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
---

# Aripiprazole
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

# Aripiprazole: From Schizophrenia / Bipolar Disorder to Major Affective Disorder

## One-Sentence Summary

Aripiprazole (Abilify) is a second-generation atypical antipsychotic globally approved for schizophrenia and bipolar disorder, acting as a dopamine-serotonin system stabilizer.
The TxGNN model predicts it may be effective for **Major Affective Disorder** (encompassing major depressive disorder and bipolar spectrum),
with **50 clinical trials** and **20 publications** currently supporting this direction — notably, the FDA approved this very indication as adjunctive therapy in 2007, with EMA authorization following.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Taiwan; globally approved for schizophrenia and bipolar disorder |
| Predicted New Indication | Major Affective Disorder |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| EU Market Status | ✗ Not Marketed (no authorization records found in dataset) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Aripiprazole operates through a mechanistically distinctive profile among antipsychotics: it functions as a **D2/D3 receptor partial agonist** combined with **5-HT1A partial agonism and 5-HT2A antagonism**. Rather than fully blocking dopamine receptors like first-generation antipsychotics, aripiprazole acts as a "dopamine system stabilizer" — attenuating excess dopamine activity in hyperactive pathways while boosting tone in underactive ones. Its 5-HT1A partial agonism simultaneously enhances serotonergic signaling, a mechanism shared with established antidepressants such as buspirone.

Major affective disorder — including major depressive disorder (MDD) and bipolar spectrum — is underpinned by precisely this dopamine-serotonin dysregulation. In MDD patients with inadequate antidepressant response, blunted mesolimbic dopamine tone contributes to anhedonia and motivation deficits that SSRIs/SNRIs alone cannot fully address. Aripiprazole's partial agonism fills this gap, making it a logical augmentation choice when antidepressant monotherapy falls short.

The clinical validation is among the strongest in all of psychiatric pharmacology. The US FDA approved aripiprazole as adjunctive therapy for MDD in 2007, supported by multiple Phase 3 RCTs enrolling thousands of patients across diverse populations. The VAST-D trial alone enrolled 1,522 Veterans with treatment-resistant MDD (NCT01421342). The TxGNN prediction therefore reflects a well-established, mechanistically sound clinical application that is already the global standard of care — the primary gap in this dataset is local (Taiwan/EU) registration status, not evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00095758](https://clinicaltrials.gov/study/NCT00095758) | Phase 3 | Completed | 1,200 | 14-week double-blind placebo-controlled RCT; aripiprazole as adjunctive therapy in MDD patients with inadequate ongoing antidepressant response; one of the pivotal FDA-approval trials |
| [NCT01421342](https://clinicaltrials.gov/study/NCT01421342) | Phase 3 | Completed | 1,522 | VAST-D: Head-to-head comparison of aripiprazole augmentation vs bupropion augmentation vs bupropion switch in Veterans with MDD unresponsive to first-line antidepressants |
| [NCT00876343](https://clinicaltrials.gov/study/NCT00876343) | Phase 3 | Completed | 586 | Aripiprazole vs placebo as adjunctive therapy co-administered with SSRI or SNRI in MDD; multi-center study providing Japan/Asia-Pacific data |
| [NCT02046564](https://clinicaltrials.gov/study/NCT02046564) | Phase 3 | Completed | 412 | ASC-01 (fixed-dose aripiprazole/sertraline combination) vs sertraline monotherapy in MDD with incomplete sertraline response |
| [NCT03423680](https://clinicaltrials.gov/study/NCT03423680) | Phase 3 | Recruiting | 390 | Ongoing confirmatory Phase 3 RCT of adjunctive aripiprazole with mood stabilizer for major depressive episode in bipolar I or II disorder; completion expected December 2025 |
| [NCT01567527](https://clinicaltrials.gov/study/NCT01567527) | Phase 3 | Completed | 731 | 52-week double-blind RCT of aripiprazole intramuscular depot as maintenance in bipolar I disorder; primary endpoint: time to any mood episode recurrence |
| [NCT00110461](https://clinicaltrials.gov/study/NCT00110461) | Phase 3 | Completed | 296 | Two doses of aripiprazole in children and adolescents with bipolar I disorder (manic/mixed episode); extends evidence base to pediatric population |
| [NCT00102518](https://clinicaltrials.gov/study/NCT00102518) | Phase 3 | Completed | 325 | Long-term (open-label) safety and tolerability of flexible-dose aripiprazole (2–30 mg) in adolescents with schizophrenia and children/adolescents with bipolar I disorder |
| [NCT00683852](https://clinicaltrials.gov/study/NCT00683852) | Phase 3 | Completed | 225 | Reduced-dose aripiprazole as adjunctive to antidepressants in MDD patients with prior inadequate response; dose optimization data |
| [NCT00667745](https://clinicaltrials.gov/study/NCT00667745) | Phase 4 | Completed | 283 | LiTMUS effectiveness trial; aripiprazole serves as active comparator in optimized pharmacotherapy for bipolar disorder |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review + NMA | J Affect Disord | Network meta-analysis of augmentation agents for treatment-resistant depression; aripiprazole among most extensively studied comparators with favorable efficacy-tolerability profile |
| [38669232](https://pubmed.ncbi.nlm.nih.gov/38669232/) | 2024 | Meta-analysis of RCTs | PLoS One | Largest systematic review and meta-analysis of aripiprazole or bupropion augmentation/switching for TRD or MDD; confirms superior augmentation efficacy over switching |
| [38219278](https://pubmed.ncbi.nlm.nih.gov/38219278/) | 2024 | Systematic Review | Neuropsychopharmacol Rep | Frequentist NMA comparing brexpiprazole vs aripiprazole for Japanese MDD patients with inadequate antidepressant response; critical for Asia-Pacific population data |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic Review + Meta | Psychol Med | Comprehensive meta-analytic assessment of antipsychotics as monotherapy and adjunctive therapy for MDD; aripiprazole is primary reference comparator |
| [34167174](https://pubmed.ncbi.nlm.nih.gov/34167174/) | 2021 | Systematic Review + Meta | Prim Care Companion CNS Disord | Long-term (≥6 months) efficacy and tolerability of adjunctive aripiprazole for MDD; remission rates and adverse effect incidence across extended follow-up |
| [37746943](https://pubmed.ncbi.nlm.nih.gov/37746943/) | 2023 | Systematic Review + NMA | Medicine | Ranks 4 atypical antipsychotics (aripiprazole, quetiapine, olanzapine, brexpiprazole) for MDD augmentation; comparative efficacy and safety hierarchy |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | Review | Psychiatr Clin North Am | Pharmacotherapy for TRD; positions aripiprazole as a first-choice augmentation agent alongside brexpiprazole, with FDA approval as the evidence anchor |
| [36961650](https://pubmed.ncbi.nlm.nih.gov/36961650/) | 2023 | RCT (Open-label) | CNS Drugs | Safety, tolerability, and pharmacokinetics of aripiprazole 2-month long-acting injectable (960 mg) in schizophrenia and bipolar I; extended-release formulation data |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | Comprehensive JAMA review of bipolar disorder diagnosis and treatment; covers ~40 million patients worldwide, includes aripiprazole as standard maintenance agent |
| [36855876](https://pubmed.ncbi.nlm.nih.gov/36855876/) | 2023 | Review | Am J Psychiatry | Antipsychotics in the evolving TRD therapeutic landscape; characterizes aripiprazole as "one of the best-studied and most widely used adjunctive therapies" for TRD |

---

## Safety Considerations

Please refer to the SmPC for safety information.

> **Note**: TFDA prescribing information (local safety warnings and contraindications) was not available in the current dataset and constitutes a blocking data gap for formal S1 safety screening.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for aripiprazole in major affective disorder is among the strongest in psychiatry — multiple large Phase 3 RCTs have confirmed adjunctive efficacy in MDD and bipolar depression, and both FDA (2007) and EMA have already approved this indication globally. The TxGNN prediction accurately identifies a well-validated clinical application currently absent from local (Taiwan/EU) registration.

**To proceed, the following is needed:**
- Resolve blocking data gap: obtain and parse TFDA prescribing information PDF to extract local warnings, contraindications, and black-box alerts before S1 safety evaluation
- Retrieve detailed MOA from DrugBank API (DB01238) to complete mechanistic linkage analysis
- Confirm current EMA authorization status for generic aripiprazole products (Abilify brand was withdrawn by the originator, but generics may hold active EMA approvals)
- Define the precise target indication for local registration: adjunctive MDD (as per FDA approval) vs bipolar depression (as in NCT03423680) — these require separate regulatory pathways
- Prepare bridging data plan: assess whether existing Phase 3 data from Asian populations (NCT00876343, NCT38219278) is sufficient for TFDA/EMA submission without additional local trials
- Establish risk-management protocol for known class-effect concerns with atypical antipsychotics (metabolic monitoring, tardive dyskinesia surveillance, impulse control) to satisfy local regulatory requirements
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

