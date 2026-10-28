---
layout: default
title: Prasugrel
parent: AI Predictions (L5)
nav_order: 496
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Prasugrel: predicted new indication Pulmonary hypertension (evidence level L5). Approved use: Prevention of atherothrombotic events in acute coronary syndrome (UA/…"
monitor_inn: "Prasugrel"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura", "kyphoscoliotic heart disease", "rheumatoid arthritis", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "leprosy"]
---

# Prasugrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Prasugrel: From Acute Coronary Syndrome to Pulmonary Hypertension
{: .text-alpha }

## One-Sentence Summary

Prasugrel is a P2Y12 platelet inhibitor, originally used with aspirin to prevent atherothrombotic events in acute coronary syndrome patients undergoing PCI.
The TxGNN model's top-ranked prediction is **pulmonary hypertension**, but **no clinical trials** and only **2 publications** were found, and neither studies prasugrel in this condition.
The best-supported alternative direction is **migraine** (especially with patent foramen ovale), with **2 clinical trials** (neither testing prasugrel) and **2 related publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of atherothrombotic events in acute coronary syndrome (UA/NSTEMI/STEMI) patients undergoing primary or delayed PCI, co-administered with aspirin |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Prasugrel is known as a P2Y12 antagonist that inhibits platelet aggregation. Its efficacy in preventing thrombotic events in acute coronary syndrome is established, and mechanistically it may be applicable to conditions in which platelet activation plays a role.

For pulmonary hypertension, platelet activation and in-situ thrombosis are thought to contribute to pulmonary vascular remodeling, so a hypothetical link exists. However, the score is purely a model prediction. The two retrieved papers concern clopidogrel adherence in ACS patients and background therapy in a COVID-19 registry; neither evaluates prasugrel in pulmonary hypertension.

Among the lower-ranked predictions, **migraine** has the most supporting material. Migraine with aura, particularly in patients with patent foramen ovale (PFO), may involve microemboli or platelet-derived mediators bypassing lung filtration, and P2Y12 inhibition could reduce this. Supporting data are small and uncontrolled, and mostly involve other P2Y12 agents (clopidogrel, ticagrelor). Prasugrel-specific evidence is limited. Other predictions (e.g., rheumatoid arthritis, leprosy, brachydactyly-syndactyly syndrome) have no trials or literature and are prediction-only.

## Clinical Trial Evidence

No clinical trials are registered for pulmonary hypertension (the top prediction). The trials below relate to the migraine prediction (rank 2) and do not test prasugrel as the intervention:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07629635](https://clinicaltrials.gov/study/NCT07629635) | Phase 3 | Recruiting | 32 | PFO-directed therapy for migraine cessation; indirect support for the PFO–migraine hypothesis only |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | N/A | Terminated | 7 | GORE CARDIOFORM Septal Occluder (device) for migraine; no prasugrel evidence |

## Literature Evidence

Literature for the top prediction (pulmonary hypertension):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Current Medical Research and Opinion | Factors associated with clopidogrel use and adherence in ACS patients after PCI; not about pulmonary hypertension |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort (registry) | Kardiologiia | Effect of prior background therapy on COVID-19 outcome; not about prasugrel in pulmonary hypertension |

Literature for the migraine predictions (indirect):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospective cohort | Neurology | Off-label thienopyridine therapy in migraineurs with PFO |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label pilot | Neurology | Ticagrelor for refractory migraine with PFO; notes that clopidogrel and prasugrel reduced migraine symptoms in some PFO patients |
| [42722054](https://pubmed.ncbi.nlm.nih.gov/42722054/) | 2026 | Preclinical (mouse) | European Journal of Pharmacology | Prasugrel showed neuroprotection in a pentylenetetrazol kindling (epilepsy) model; not migraine evidence |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000984 | Efient (status: valid) | Not specified | Efient, co-administered with acetylsalicylic acid (ASA), is indicated for the prevention of atherothrombotic events in patients with acute coronary syndrome (i.e. unst... |

## Safety Considerations

- **Contraindications (from knowledge graph, not label text)**: The TxGNN knowledge graph links prasugrel to contraindications in liver failure, hypotensive disorder, blood coagulation disease, stroke disorder, cerebrovascular disorder, susceptibility to ischemic stroke, cerebral infarction, injury, thrombocytopenic purpura, intracranial hemorrhage, transient ischemic attack, and vertebrobasilar insufficiency.
- **Drug Interactions**: 100 interactions were found. Notable ones:
  - **Major**: deferasirox, ibritumomab tiuxetan
  - **Moderate**: acetylsalicylic acid (co-administered by design in the approved indication, so bleeding risk requires monitoring), morphine, opium, fenfluramine, dexfenfluramine, sibutramine
  - **Minor**: H2 blockers (famotidine, ranitidine, cimetidine, nizatidine) and proton pump inhibitors (omeprazole, esomeprazole, pantoprazole, lansoprazole, rabeprazole, dexlansoprazole), bupropion
- Potent P2Y12 inhibition carries bleeding risk, which must be weighed against any benefit in new indications. Please refer to the SmPC for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, pulmonary hypertension, has only a model score with no prasugrel-specific trials or literature (L5). The migraine direction (evidence L3) is more promising as a research question, but its support is small, uncontrolled, and mostly from other P2Y12 agents. Prasugrel's bleeding risk and the lack of a currently valid EU authorization add further caution.

**To proceed, the following is needed:**
- Mechanism of action data and the SmPC warnings and contraindications (currently missing and blocking safety screening)
- Prasugrel-specific preclinical or clinical studies in pulmonary hypertension
- For migraine, a randomized, controlled prasugrel study in PFO-associated migraine, with a bleeding-risk assessment
- Clarification of the EU regulatory status (the sole authorization is cancelled)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

