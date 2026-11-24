---
layout: default
title: Entacapone
parent: AI Predictions (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Entacapone: predicted new indication PLA2G6-associated neurodegeneration (evidence level L5). Approved use: Adjunct to standard levodopa/benserazide or levodopa/carbidopa in adu…"
monitor_inn: "Entacapone"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "lethal infantile mitochondrial myopathy", "Lewy body dementia", "fructose-1,6-bisphosphatase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "progressive supranuclear palsy-corticobasal syndrome"]
---

# Entacapone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Entacapone: From Parkinson's Disease (Adjunct Therapy) to PLA2G6-Associated Neurodegeneration
{: .text-alpha }

## One-Sentence Summary

Entacapone is a COMT inhibitor, originally used as an add-on to levodopa in Parkinson's disease patients with end-of-dose motor fluctuations.
The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**,
but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction. It rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Adjunct to standard levodopa/benserazide or levodopa/carbidopa in adult Parkinson's disease patients with end-of-dose motor fluctuations who cannot be stabilised on those combinations |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 0.9976 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 7 of 7) |
| Number of Authorizations | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for entacapone: "Entacapone is a selective and reversible inhibitor of COMT. In mammals, COMT is distributed throughout various organs with the highest activities in the liver and kidney. COMT also occurs in the heart, lung, smooth and skeletal muscles, intestinal tract, reproductive organs, various glands, adipose tissue, skin, blood cells, and neuronal tissues, especially in glial cells." ([DailyMed: entacapone prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ee02a04a-4b42-4cfa-8d9d-b1459c0ee9fd), label version 2026-02-16; accessed 2026-11-19.) Entacapone is known as a catechol-O-methyltransferase (COMT) inhibitor. By slowing levodopa breakdown, it prolongs levodopa's effect in Parkinson's disease.

PLA2G6-associated neurodegeneration includes a dystonia-parkinsonism phenotype with dopaminergic involvement. In theory, COMT inhibition could augment levodopa response in that parkinsonian subtype. This is speculative: there is no direct mechanistic or clinical evidence in the data, and the prediction rests only on the TxGNN score.

For context, the other top-ranked predictions are mostly weak. Several (e.g., Rasmussen encephalitis, myelitis, transaldolase deficiency, fructose-1,6-bisphosphatase deficiency) have no plausible mechanistic link. Two are closer to the approved indication: Lewy body dementia (rank 7, L4, with indirect in vitro and imaging-related material) and juvenile parkinsonism of Hunt (rank 4, supported only by analogy to Parkinson's disease).

## Clinical Trial Evidence

Currently no related clinical trials registered for PLA2G6-associated neurodegeneration.

## Literature Evidence

Currently no related literature available for PLA2G6-associated neurodegeneration.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000170 | Comtess | entacapone | Valid |
| EMEA/H/C/000171 | Comtan | entacapone | Valid |
| EMEA/H/C/002075 | Entacapone Teva | entacapone | Valid |
| EMEA/H/C/002440 | Entacapone Orion | entacapone | Valid |
| EMEA/H/C/000511 | Stalevo | levodopa; carbidopa; entacapone | Valid |
| EMEA/H/C/002441 | Levodopa/Carbidopa/Entacapone Orion | levodopa; carbidopa; entacapone | Valid |
| EMEA/H/C/002785 | Corbilta | levodopa; carbidopa; entacapone | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: The TxGNN knowledge graph links entacapone to contraindications in several areas:
  - Cardiovascular: myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease, orthostatic hypotension
  - Psychiatric: psychotic disorder, schizoaffective disorder, anxiety disorder
  - Organ disease: liver disease, kidney disease, gallbladder disease
  - Neurological: epilepsy, drug-induced dyskinesia
  - Other: glaucoma (open-angle and angle-closure), diabetes mellitus, diabetic ketoacidosis, melanoma, peptic ulcer disease
- **Drug Interactions**: 82 interactions were recorded. Moderate-level interactions include epinephrine (including ophthalmic and topical forms), morphine (including liposomal), dronabinol, opium, nabilone, metoclopramide, and iron. Other interactions with unclassified severity include pantoprazole, omeprazole, lansoprazole, doxycycline, metformin, atropine, lactulose, prednisone, simvastatin, and potassium chloride.
- **Population note**: The label covers adults only. Any use in juvenile or pediatric disorders would be outside the approved population.
- **Safety concern in mitochondrial disease**: The history of hepatotoxicity with the related drug tolcapone raises concern for use in mitochondrial disease populations.

Please refer to the SmPC for full safety information, since label warnings and contraindications were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for PLA2G6-associated neurodegeneration is supported only by a model score (L5), with no trials, no literature, and only a speculative mechanistic link. The drug is marketed.

<!-- review:begin eu-lic-20261106-entacapone-2 -->

> **Review correction (2026-11-24)**: Originally stated: "All four EU authorizations are valid, and the drug is marketed." Removed: the number or status of EU marketing authorisations stated here did not match the EMA data (the EMA medicines data as of 2026-11-06). The current number of EU marketing authorisations for this drug is shown in the Quick Overview and in the table under EU Market Information. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-entacapone-2 -->

**To proceed, the following is needed:**
- Mechanism of action data for entacapone
- EMA label warnings and contraindications
- Preclinical or case-level evidence of benefit in the parkinsonian subtype of PLA2G6-associated neurodegeneration
- Clarification of the current regulatory pathway
- A review of higher-plausibility alternatives, such as Lewy body dementia (L4, "Research Question") and juvenile parkinsonism, before investing in the top-ranked prediction

<!-- review:begin eu-lic-20261106-entacapone-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Clarification of why the EU authorizations were cancelled and of the current regulatory pathway" Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-11-06). The current number of EU marketing authorisations for this drug is shown in the Quick Overview and in the table under EU Market Information. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-entacapone-1 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "of why the EU authorizations were cancelled and" | Corrected (revised 2026-11-24; earlier version kept in the record) | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-24 | Removed: "All four EU authorizations are valid, and t" | Corrected (revised 2026-11-24; earlier version kept in the record) | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: entacapone prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ee02a04a-4b42-4cfa-8d9d-b1459c0ee9fd) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

