---
layout: default
title: Perampanel
parent: AI Predictions (L5)
nav_order: 481
evidence_level: L5
indication_count: 10
---

# Perampanel
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

# Perampanel: From Epilepsy to Visual Epilepsy

## One-Sentence Summary

Perampanel (brand name Fycompa) is an add-on antiseizure medicine, originally used for partial-onset seizures and primary generalised tonic-clonic seizures in patients aged 12 years and older.
The TxGNN model predicts it may be effective for **visual epilepsy**, but **no clinical trials** and only **general epilepsy literature** (none specific to visual or photosensitive epilepsy) currently support this direction.
Among the other predicted indications, **status epilepticus** has the strongest evidence (4 registered trials and about 20 publications).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adjunctive treatment of partial-onset seizures with or without secondarily generalised seizures, and of primary generalised tonic-clonic seizures, in adults and adolescents from 12 years of age |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 (for visual epilepsy; L3 for status epilepticus) |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism data were not available in the data compiled for this report. From the published literature, perampanel is a selective, non-competitive antagonist of the AMPA-type glutamate receptor. It reduces glutamate-driven excitation of postsynaptic neurons, which is the basis of its effect in partial-onset and generalised tonic-clonic seizures.

Visual (photosensitive) epilepsy is a reflex epilepsy in which visual stimuli trigger seizures, and cortical hyperexcitability is thought to be involved. Blocking excitatory AMPA signalling is therefore mechanistically coherent. However, this link is an extrapolation. The retrieved literature consists of general epilepsy reviews, guidelines and network meta-analyses, and none of it studies visual or photosensitive epilepsy directly.

The same pattern holds for most other predicted reflex-type indications (startle, thinking, micturition-induced, eating, orgasm-induced and reading seizures). Evidence for these is absent or indirect. Audiogenic seizures have animal-model support only. Beta-ketothiolase deficiency, a metabolic disorder, has no plausible mechanistic link, and the prediction likely reflects seizure-related graph connections.

The best-supported alternative is **status epilepticus** (score 99.77%). Prolonged seizures involve loss of synaptic GABA-A receptors and increased AMPA receptor expression, which makes AMPA antagonism a rational option when benzodiazepines fail. Systematic reviews and case series report seizure cessation with perampanel in refractory status epilepticus.

---

## Clinical Trial Evidence

No clinical trials are registered for visual epilepsy. Trials for the best-supported alternative indication, status epilepticus, are listed below for reference.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06401707](https://clinicaltrials.gov/study/NCT06401707) | Phase 2 | Recruiting | 52 | Randomized placebo-controlled pilot of perampanel to prevent status epilepticus after cardiac arrest; no results yet |
| [NCT04309721](https://clinicaltrials.gov/study/NCT04309721) | Phase 3 | Terminated | 1 | Add-on enteral perampanel in focal motor status epilepticus; terminated, no usable efficacy data |
| [NCT05684978](https://clinicaltrials.gov/study/NCT05684978) | Phase 4 | Terminated | 1 | Perampanel in refractory status epilepticus; terminated, no usable efficacy data |
| [NCT05756621](https://clinicaltrials.gov/study/NCT05756621) | N/A | Completed | 84 | Retrospective cohort of ketamine plus perampanel in super-refractory status epilepticus after cardiac arrest |

---

## Literature Evidence

No visual-epilepsy-specific publications were found. The table below lists the most relevant publications for status epilepticus (systematic reviews first), followed by general epilepsy evidence that supports perampanel's overall profile.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35151187](https://pubmed.ncbi.nlm.nih.gov/35151187/) | 2022 | Systematic review | Epilepsy Behav | Efficacy and safety of perampanel in achieving cessation of status epilepticus |
| [30076046](https://pubmed.ncbi.nlm.nih.gov/30076046/) | 2018 | Systematic review | Epilepsy Behav | Efficacy and tolerability of perampanel in refractory and super-refractory status epilepticus |
| [33754209](https://pubmed.ncbi.nlm.nih.gov/33754209/) | 2021 | Cohort + review | J Neurol | 81 patients with refractory or super-refractory status epilepticus; dose and efficacy assessed |
| [30613951](https://pubmed.ncbi.nlm.nih.gov/30613951/) | 2019 | Retrospective cohort | Acta Neurol Scand | Multinational cases of perampanel in established, refractory and super-refractory status epilepticus |
| [38872031](https://pubmed.ncbi.nlm.nih.gov/38872031/) | 2024 | Retrospective cohort | Neurocrit Care | Add-on perampanel in refractory status epilepticus with postanoxic encephalopathy |
| [29663350](https://pubmed.ncbi.nlm.nih.gov/29663350/) | 2018 | Review | Epilepsia | Role of AMPA receptors and their antagonists in status epilepticus |
| [35061214](https://pubmed.ncbi.nlm.nih.gov/35061214/) | 2022 | Network meta-analysis | Drugs | Third-generation antiseizure medications, including perampanel, as adjunctive therapy for focal-onset seizures |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Network meta-analysis | J Neurol | Antiseizure medications for idiopathic generalised epilepsies |
| [30092489](https://pubmed.ncbi.nlm.nih.gov/30092489/) | 2018 | Preclinical | Epilepsy Res | Perampanel reduced audiogenic seizures in genetically epilepsy-prone rats without inducing tolerance |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Review | Expert Opin Drug Discov | Discovery and development of perampanel as an AMPA receptor antagonist |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002434 | Fycompa | Not specified | Adjunctive treatment of partial-onset seizures with or without secondarily generalised seizures in adult and adolescent patients from 12 years... (status: cancelled) |

---

## Safety Considerations

- **Drug Interactions**: 56 interactions were identified. The ones listed are mostly moderate, with CNS depressants and sedating drugs being the main concern: opioids (morphine, codeine, hydrocodone, opium, difenoxin, diphenoxylate), ethanol, promethazine, chlorpheniramine, dextromethorphan, dronabinol, nabilone, metoclopramide, chloroquine, hydroxychloroquine, dexamethasone and sibutramine. Clarithromycin is a minor interaction.
- **Other reported concerns from the literature**: Psychiatric and behavioural adverse reactions (aggression, irritability, psychosis) are described, with one report noting a boxed warning for these reactions.

Please refer to the SmPC for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction for visual epilepsy rests on a high model score and a plausible AMPA-antagonist mechanism, but no trial or study addresses it directly, so the evidence is indirect (L4).
- The only EU authorization is cancelled, and safety label data could not be retrieved.
- Status epilepticus is the better-supported candidate (L3) but still has only observational evidence, since the two randomized trials terminated after one participant each.

**To proceed, the following is needed:**
- Visual or photosensitive epilepsy data, such as photoparoxysmal response studies or case series with perampanel
- Mechanism-of-action data in a structured source
- Full warnings and contraindications from the SmPC, and clarification of why the EU authorization was cancelled
- For status epilepticus, results from the ongoing Phase 2 trial (NCT06401707) and an adequately powered randomized trial
- A safety plan covering psychiatric adverse reactions and CNS-depressant interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

