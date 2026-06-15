---
layout: default
title: Brivaracetam
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Brivaracetam
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

# Brivaracetam: From Focal Onset Seizures to Visual Epilepsy

## One-Sentence Summary

Brivaracetam (BRV) is a third-generation antiseizure medication developed for focal onset seizures, acting as a high-affinity, selective ligand for synaptic vesicle protein 2A (SV2A) with 15- to 30-fold greater binding affinity than its predecessor levetiracetam.
The TxGNN model predicts it may be effective for **Visual Epilepsy** — a reflex epilepsy subtype triggered by visual stimuli —
with **0 clinical trials** and **19 publications** currently identified, though most publications address epilepsy broadly rather than visual epilepsy as a distinct subgroup.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Focal onset seizures (epilepsy) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this evidence pack. Based on information drawn from the referenced literature, Brivaracetam is a propyl analog of levetiracetam engineered through a systematic drug discovery program to maximize SV2A binding selectivity. Its high lipophilicity enables rapid blood-brain barrier penetration — substantially faster than levetiracetam — and its SV2A binding modulates synaptic vesicle exocytosis, effectively suppressing the hypersynchronous neuronal firing that generates seizures.

Visual epilepsy is a reflex epilepsy subtype in which seizures are provoked by specific visual stimuli: flickering light, geometric patterns, or moving images. The photosensitivity model — a well-validated human proof-of-concept paradigm using intermittent photic stimulation (IPS) to elicit photoparoxysmal EEG responses — is mechanistically the closest clinical analog to visual epilepsy. BRV has been evaluated in this model (referenced in the repurposing rationale as PMID 17785672), and a randomized double-blind crossover trial (PMID 32949370) demonstrated that BRV suppresses photoparoxysmal EEG responses more rapidly than levetiracetam, providing direct neurophysiological evidence of BRV activity in visually-triggered epileptiform discharges.

The mechanistic bridge is plausible: BRV's SV2A inhibition is agnostic to seizure trigger, and visual reflex epilepsy differs from other focal epilepsy primarily in its precipitant, not in the downstream synaptic mechanism of seizure propagation. However, no published study has enrolled a visual epilepsy patient cohort specifically, and the 19 identified publications address general focal or generalized epilepsy populations. The current evidence base supports mechanism-driven interest but not clinical readiness.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Brivaracetam in visual epilepsy.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38811492](https://pubmed.ncbi.nlm.nih.gov/38811492/) | 2024 | Narrative Review | Advances in Therapy | Comprehensive review of BRV's preclinical SV2A profile and clinical benefits in epilepsy; includes photosensitivity model data providing mechanistic support for visual reflex epilepsy |
| [40568060](https://pubmed.ncbi.nlm.nih.gov/40568060/) | 2025 | Narrative Review | Journal of Epilepsy Research | Synthesizes BRV pharmacology and real-world efficacy data; highlights rapid BBB penetration and selective SV2A binding as differentiating properties |
| [39664134](https://pubmed.ncbi.nlm.nih.gov/39664134/) | 2024 | Systematic Review | Cureus | Systematic review of BRV efficacy, safety, and reasons for AED switching; evaluates BRV's role across adult and pediatric epilepsy populations |
| [38970892](https://pubmed.ncbi.nlm.nih.gov/38970892/) | 2024 | Prospective Cohort | Epilepsy & Behavior | EXPERIENCE pooled analysis comparing BRV effectiveness and tolerability in older (≥65 years) versus younger adults with epilepsy across Australia, Europe, and the US |
| [38576178](https://pubmed.ncbi.nlm.nih.gov/38576178/) | 2024 | Phase III RCT | Epilepsia Open | Phase III double-blind placebo-controlled trial of adjunctive BRV in adult Asian patients with focal-onset seizures; provides efficacy data from a regional population |
| [37483441](https://pubmed.ncbi.nlm.nih.gov/37483441/) | 2023 | Systematic Review & Meta-analysis | Frontiers in Neurology | Systematic review and meta-analysis of BRV safety and efficacy in childhood epilepsy, addressing a population often excluded from pivotal trials |
| [31937513](https://pubmed.ncbi.nlm.nih.gov/31937513/) | 2020 | Pooled Safety Analysis | Epilepsy & Behavior | In-depth pooled safety analysis of adjunctive BRV across multiple clinical trials; relevant baseline tolerability data for any new indication investigation |
| [32120063](https://pubmed.ncbi.nlm.nih.gov/32120063/) | 2020 | Review | Neuropharmacology | Mechanistic overview of antiseizure drugs including SV2A-mediated pathways; contextualizes BRV's mechanism relative to other agents |
| [31195850](https://pubmed.ncbi.nlm.nih.gov/31195850/) | 2019 | Clinical Study Review | Expert Review of Neurotherapeutics | Reviews BRV clinical trial data and post-marketing experience in focal epilepsy; discusses pharmacological advantages over levetiracetam |
| [26165169](https://pubmed.ncbi.nlm.nih.gov/26165169/) | 2015 | Meta-analysis | Expert Opinion on Pharmacotherapy | Meta-analysis of BRV at multiple doses versus placebo as adjunctive therapy for partial-onset epilepsy; establishes dose-response evidence base |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
BRV's SV2A mechanism and its demonstrated activity in the photosensitivity model provide a biologically plausible basis for investigating visual epilepsy, but no clinical trials or patient-level studies targeting this specific indication exist. The evidence base is mechanistic and indirect, placing this at L4 and insufficient to support direct clinical development without prior targeted research.

**To proceed, the following is needed:**
- Subgroup extraction from existing BRV clinical trial datasets: identify patients with photosensitive or visually-triggered seizures and analyze outcomes separately
- Full review of PMID 17785672 (BRV in the photosensitivity model) to quantify the magnitude of photoparoxysmal response suppression and assess clinical translatability
- Retrieval of TFDA SmPC and DrugBank MOA data to complete safety profiling (currently blocking S1 safety screen)
- Consider a prospective registry study enrolling patients with photosensitive epilepsy (e.g., juvenile myoclonic epilepsy with photosensitivity) as a feasible near-term research step
- Mechanistic literature review of SV2A's role in visual cortex hyperexcitability to strengthen the hypothesis before committing trial resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

