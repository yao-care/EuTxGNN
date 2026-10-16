---
layout: default
title: Levodopa
parent: AI Predictions (L5)
nav_order: 365
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Levodopa: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Intermittent treatment of episodic motor fluctuations (OFF episodes)…"
monitor_inn: "Levodopa"
predicted_indications: ["Rasmussen subacute encephalitis", "PLA2G6-associated neurodegeneration", "myelitis", "transaldolase deficiency", "paralysis agitans, juvenile, of Hunt", "fructose-1,6-bisphosphatase deficiency", "progressive supranuclear palsy-corticobasal syndrome", "Lewy body dementia", "multiple system atrophy, parkinsonian type", "X-linked intellectual disability-ataxia-apraxia syndrome"]
---

# Levodopa
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

# Levodopa: From Parkinson's Disease OFF Episodes to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Levodopa is a dopamine precursor, originally used (as inhaled Inbrija) for intermittent treatment of OFF episodes in adults with Parkinson's disease who are on a levodopa/dopa-decarboxylase inhibitor.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**, its top-ranked prediction, but **no clinical trials and no publications** were found for this indication. The prediction is purely computational.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Intermittent treatment of episodic motor fluctuations (OFF episodes) in adult patients with Parkinson's disease treated with a levodopa/dopa-decarboxylase inhibitor |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, levodopa is converted in the brain to dopamine and replaces the dopamine lost in Parkinson's disease, which is why it is effective for motor symptoms in that condition.

Rasmussen encephalitis is a unilateral inflammatory epileptic encephalopathy. There is no clear dopaminergic-deficit rationale linking it to levodopa, so the model's high score is not supported by an evident mechanism. This is a purely computational prediction, and the high score alone should not be taken as evidence of benefit.

**Other predictions worth noting.** Several lower-ranked TxGNN predictions have a more plausible link to levodopa, and they may be better candidates for follow-up:

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Multiple system atrophy, parkinsonian type | 97.02% | L2 | Levodopa is standard symptomatic therapy with partial or transient benefit. One recruiting Phase 1/2 trial (NCT06831500) has been found, but its intervention is not confirmed as levodopa. |
| PLA2G6-associated neurodegeneration | 98.75% | L3 | Several case series report levodopa-responsive parkinsonism, often transient, with dyskinesia reported. |
| Lewy body dementia | 97.25% | L3 | Levodopa may help motor symptoms but risks worsening psychosis or hallucinations. Direct RCT evidence is limited. |
| Paralysis agitans, juvenile, of Hunt | 98.03% | L5 | Archaic term for juvenile-onset parkinsonism. It needs mapping to a modern disease entity before reassessment. |
| X-linked intellectual disability-ataxia-apraxia syndrome | 96.46% | L4 | Reports in MCT8 deficiency describe a levodopa/carbidopa response. Disease mapping needs verification. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Rasmussen subacute encephalitis.

---

## Literature Evidence

Currently no related literature available for Rasmussen subacute encephalitis.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication | Status |
|---------|------|------|-----------|------|
| EMEA/H/C/004786 | Inbrija | Not specified | Intermittent treatment of episodic motor fluctuations (OFF episodes) in adult patients with Parkinson's disease (PD) treated with a levodopa/dopa-decarboxylase inhibitor. | Cancelled |

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (derived from drug-disease relationships in the TxGNN knowledge graph, not from label text, and to be confirmed against the SmPC). Listed conditions include:
- Neurological and autonomic: multiple system atrophy, orthostatic hypotension, postural orthostatic tachycardia syndrome, drug-induced dyskinesia, epilepsy
- Psychiatric: psychotic disorder, schizoaffective disorder, schizophreniform disorder, anxiety disorder, mental disorder
- Cardiovascular: myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease
- Eye: open-angle glaucoma, angle-closure glaucoma
- Other: kidney disease, liver disease, peptic and gastric ulcer, diabetes mellitus, diabetic ketoacidosis, melanoma

Epilepsy appears on this list and is relevant to a seizure-driven condition such as Rasmussen encephalitis.

**Drug Interactions** (100 interactions identified; examples):
- Moderate: epinephrine, ephedrine, bupropion, metoclopramide, metronidazole, pyridoxine, iron, and anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine, methscopolamine, clidinium, mepenzolate)
- Minor: antacids (aluminum hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide, magnesium oxide)

Label-based warnings and contraindications were not available. Please refer to the SmPC for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Rasmussen encephalitis prediction has a high model score but no trials, no literature, and no plausible mechanism. The evidence level is L5. In addition, the only EU authorization has been cancelled, and the knowledge graph flags epilepsy as a contraindication signal.

**To proceed, the following is needed:**
- Mechanism of action data for levodopa
- SmPC warnings and contraindications, which are required before any safety screening
- A mechanistic rationale or preclinical data for Rasmussen encephalitis, if this indication is to be pursued
- Consideration of re-prioritizing to better-supported candidates, particularly MSA-P (verify the intervention in NCT06831500), PLA2G6-associated neurodegeneration, and MCT8 deficiency
- Mapping of "paralysis agitans, juvenile, of Hunt" to a modern disease entity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

