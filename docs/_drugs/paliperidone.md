---
layout: default
title: Paliperidone
parent: AI Predictions (L5)
nav_order: 460
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-12
description: "Paliperidone: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Schizophrenia in adults and adolescents 15 years and older"
monitor_inn: "Paliperidone"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "myopia X-linked", "syndromic myopia", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia 26, X-linked, female-limited", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "atypical glycine encephalopathy"]
---

# Paliperidone
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

## Paliperidone: From Schizophrenia to Retinal dystrophy with or without extraocular anomalies
{: .text-alpha }

## One-Sentence Summary

Paliperidone is an antipsychotic originally used to treat schizophrenia and schizoaffective disorder.
The TxGNN model ranks **retinal dystrophy with or without extraocular anomalies** as its top predicted new indication, but **no clinical trials and no publications** currently support this direction.
The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia in adults and adolescents 15 years and older; schizoaffective disorder in adults |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 5 of 5) |
| Number of Authorizations | 5 (valid: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Paliperidone is generally known as a dopamine D2 and serotonin 5-HT2A receptor antagonist. Its efficacy in schizophrenia and schizoaffective disorder is established.

The data compiled for this report does not establish a mechanistic link between this receptor activity and inherited retinal degeneration. The high score (0.9992) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological or clinical evidence. Retinal dystrophies are genetically driven degenerative conditions, and a symptomatic antipsychotic is not expected to modify them.

The other top predictions share this problem: X-linked and syndromic myopia, hydranencephaly, a congenital glycosylation disorder, polymicrogyria, Charcot-Marie-Tooth type 1G and atypical glycine encephalopathy all lack trials or literature. Dopamine signalling in eye growth gives the myopia entries only a speculative rationale. The one prediction with any registered studies is treatment-refractory schizophrenia (rank 10). That is a subgroup of the approved indication rather than a true repurposing target, and the available trials do not show paliperidone efficacy there. Clozapine remains the standard for refractory cases.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for retinal dystrophy.

---

## Literature Evidence

Currently no related literature available for retinal dystrophy.

---

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000746 | Invega | paliperidone | Valid |
| EMEA/H/C/002105 | Xeplion | paliperidone palmitate | Valid |
| EMEA/H/C/004066 | Trevicta | paliperidone palmitate | Valid |
| EMEA/H/C/005486 | Byannli | paliperidone palmitate | Valid |
| EMEA/H/C/006185 | Niapelf | paliperidone palmitate | Valid |

<!-- licenses:end -->

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these are graph-derived drug-disease edges, not label text). They include:
  - Cardiovascular and rhythm: long QT syndrome (including familial), torsades de pointes, orthostatic hypotension, postural orthostatic tachycardia syndrome, hypotensive disorder, myocardial infarction, coronary thrombosis
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hyperlipidaemia (including familial), obesity (including monogenic), potassium deficiency
  - Haematological: neutropenia, agranulocytosis, haemoglobinopathy
  - Neurological: epilepsy, multiple system atrophy, basal ganglia disease, focal hand dystonia, blepharospasm
  - Other: Crohn disease and inflammatory bowel disease, female breast carcinoma, impaired renal function
- **Drug Interactions**: 100 interactions were recorded. Two are rated Major: **bupropion** and **morphine**. The Moderate-level examples shown include:
  - Antidiabetic agents (metformin, pioglitazone, alogliptin, albiglutide, canagliflozin, chlorpropamide, acarbose)
  - Anticholinergic agents (atropine, hyoscyamine, glycopyrronium)
  - Others (famotidine, epinephrine, hydrocortisone, amphotericin B, loperamide, lorcaserin, bisacodyl)

Please refer to the SmPC for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. The extensive safety signals (QT prolongation, metabolic effects, neutropenia) would also need justification in a non-psychiatric population.

<!-- review:begin eu-lic-20261031-paliperidone-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The prediction is supported only by a model score. There are no trials or publications, no plausible mechanistic link, and the only EU authorization is cancelled." Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-10-31). The EMA data list 5 EU marketing authorisations for this drug, 5 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261031-paliperidone-1 -->

**To proceed, the following is needed:**
- Mechanism of action data and a testable biological hypothesis linking paliperidone to retinal degeneration
- Preclinical evidence in retinal dystrophy models
- Label warnings and contraindications from the EU product information
- A benefit-risk rationale for a non-psychiatric population, given the safety signals above

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "There are no trials or publications, no plausible mechanistic link, and the only EU authorization is cancelled" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

