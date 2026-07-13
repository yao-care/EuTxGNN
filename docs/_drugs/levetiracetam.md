---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: From Partial Onset Seizures to Visual Epilepsy

## One-Sentence Summary

Levetiracetam (Keppra®) is a second-generation antiseizure medication established globally for the treatment of partial-onset seizures and generalized epilepsy syndromes, though it is currently not licensed in Taiwan.
The TxGNN model predicts it may be effective for **Visual Epilepsy** (photosensitive / visually-triggered reflex epilepsy),
with **9 clinical trials** and **20 publications** currently identified in support of this research direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial onset seizures / generalized epilepsy (global approvals; not licensed in Taiwan) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Taiwan Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank query. Based on known pharmacological information, Levetiracetam binds to synaptic vesicle protein 2A (SV2A) in presynaptic nerve terminals — a mechanism entirely distinct from classical antiepileptic drugs such as sodium channel blockers or GABA modulators. By modulating SV2A, LEV broadly inhibits presynaptic neurotransmitter release, reducing neuronal hyperexcitability across multiple seizure types and cortical networks.

Visual epilepsy (photosensitive reflex epilepsy) is characterized by abnormal occipital cortical sensitivity to flickering lights or visual patterns, expressed on EEG as generalized spike-and-wave discharges, and clinically as myoclonic, absence, or tonic-clonic seizures. The pathophysiological common ground — cortical hyperexcitability and aberrant neuronal synchronization — between partial-onset seizures (the globally established indication) and visual epilepsy makes LEV's SV2A mechanism directly applicable. Both conditions involve the same fundamental substrate that SV2A modulation targets.

There is targeted indirect clinical evidence supporting this direction: literature (PMID 16302877) directly documents LEV's ability to suppress the photoparoxysmal response (PPR) in patients with idiopathic generalized epilepsy, which is the hallmark EEG biomarker of photosensitive epilepsy. Furthermore, LEV is recognized in expert consensus as an effective agent in juvenile myoclonic epilepsy (JME) — a syndrome where photosensitivity is present in approximately one-third of patients. The absence of a dedicated RCT with visual epilepsy as its primary endpoint represents the principal evidence gap preventing a higher evidence classification.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | Prospective observational study assessing new AEDs (including LEV) as first-choice bitherapy in focal epilepsy; real-world efficacy covering multiple seizure subtypes that may include reflex epilepsies |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | Not Yet Recruiting | 1,649 | MAST trial: LEV vs phenytoin for post-TBI seizure prophylaxis; the largest ongoing LEV RCT establishing a safety and efficacy benchmark in high-risk populations |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | Completed | 87 | Placebo-controlled cognitive/neuropsychological safety study of adjunctive LEV in children 4–16 years with refractory partial-onset seizures; confirms acceptable tolerability profile |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | Completed | 62 | LEV modulation of hippocampal hyperactivity in psychosis using visual scene processing fMRI; demonstrates LEV effects on cortical networks engaged during visual stimulation |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | LEV vs phenobarbital for neonatal seizures; comparative efficacy data providing a safety profile across a broad range of seizure types |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completed | 31 | Open-label LEV for migraine prophylaxis with or without visual aura; provides indirect evidence for LEV activity on visually-triggered neurological events |
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | Not Yet Recruiting | 580 | Randomized, double-blind, placebo-controlled Phase 3 trial of prophylactic LEV for acute-phase intracerebral haemorrhage seizure prevention; contributes to LEV safety database |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | Terminated | 1 | Early-terminated study on LEV modulation of hippocampal activity in psychosis using visual-task fMRI; limited data only |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | Enrolling by Invitation | 24 | Gene therapy for Canavan disease with LEV as concomitant seizure management; demonstrates LEV use in rare neurological conditions with structural seizure risk |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT | The Lancet Neurology | Phase 3 PEACH trial: randomized, double-blind, placebo-controlled LEV prophylaxis in intracerebral haemorrhage; pivotal safety and efficacy reference |
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | LEV vs phenobarbital for neonatal seizures; confirms LEV efficacy and superior safety profile across early-onset seizure populations |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | RCT | Seizure | Open-label RCT comparing LEV vs phenytoin for acute symptomatic seizures in children with acute encephalitis syndrome |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic Review | Journal of Neurology | Network meta-analysis comparing antiseizure medications for idiopathic generalized epilepsies; LEV efficacy established in generalized seizure types that overlap with photosensitive epilepsy |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Systematic Review | Epilepsy & Behavior | Meta-analysis of LEV specifically for myoclonic seizures in IGE/JME; directly relevant since photosensitivity co-occurs in ~30% of JME patients |
| [39808752](https://pubmed.ncbi.nlm.nih.gov/39808752/) | 2025 | Systematic Review | Neurology | Network meta-analysis of antiseizure medications for poststroke seizures; reinforces breadth of LEV clinical evidence |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Systematic Review | Neurocritical Care | Systematic review and meta-analysis of LEV for seizure prophylaxis in neurocritical care (ICH, TBI, SAH); clarifies efficacy, optimal dosing, and adverse event profile |
| [36209676](https://pubmed.ncbi.nlm.nih.gov/36209676/) | 2022 | Systematic Review | Seizure | Network meta-analysis of treatments for benzodiazepine-resistant status epilepticus; LEV ranks among the most effective second-line agents |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | Comprehensive spotlight on LEV across all approved indications including adjunctive therapy for myoclonic seizures in JME and primary generalized tonic-clonic seizures — mechanistically linked to photosensitive epilepsy |
| [34260837](https://pubmed.ncbi.nlm.nih.gov/34260837/) | 2021 | Review | NEJM | Initial management of seizures in adults; positions LEV as standard first-line option with broad-spectrum applicability |

---

## Safety Considerations

Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
Levetiracetam's SV2A mechanism provides a biologically plausible basis for efficacy in visual epilepsy, supported by indirect evidence of photoparoxysmal response suppression in IGE (PMID 16302877) and established JME guidelines. However, the absence of any dedicated RCT targeting visually-triggered reflex epilepsy as a primary endpoint limits the evidence classification to L3 — sufficient to formulate a research question but not to advance directly to a clinical development decision.

**To proceed, the following is needed:**
- Dedicated prospective trial with photoparoxysmal response (PPR) abolition as the primary EEG endpoint in patients with photosensitive / visual reflex epilepsy
- Head-to-head comparison with valproate, the current standard of care for photosensitive epilepsy
- MOA data retrieval from DrugBank API to formally confirm SV2A binding kinetics
- Taiwan TFDA safety database review (SmPC / drug insert PDF) to identify contraindications, key warnings, and DDI profile
- Clear patient population definition distinguishing pure photosensitive epilepsy, JME with photosensitivity, and self-induced photosensitive epilepsy (Sunflower syndrome) as separate strata
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

