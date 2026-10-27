---
layout: default
title: Temoporfin
parent: AI Predictions (L5)
nav_order: 596
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Temoporfin: predicted new indication Nasopharyngeal teratoma (evidence level L5). Approved use: Palliative treatment of patients with advanced head and neck squamous…"
monitor_inn: "Temoporfin"
predicted_indications: ["nasopharyngeal teratoma", "odontogenic cyst", "pre-malignant neoplasm", "epiglottis neoplasm", "tumor of testis and paratestis", "cystic neoplasm", "benign neoplasm of floor of mouth", "benign neoplasm of tongue", "benign neoplasm of hypopharynx", "cervical neuroblastoma"]
---

# Temoporfin
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

## Temoporfin: From Advanced Head and Neck Squamous Cell Carcinoma to Nasopharyngeal Teratoma
{: .text-alpha }

## One-Sentence Summary

Temoporfin (Foscan) is a photosensitizer used in photodynamic therapy, originally authorized in the EU for palliative treatment of advanced head and neck squamous cell carcinoma.
The TxGNN model predicts it may be effective for **nasopharyngeal teratoma**, but **no clinical trials and no publications** currently support this specific prediction (evidence level L5, model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Palliative treatment of patients with advanced head and neck squamous cell carcinoma failing prior therapies and unsuitable for radiotherapy, surgery or systemic chemotherapy |
| Predicted New Indication | Nasopharyngeal teratoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, temoporfin is a photosensitizer used in photodynamic therapy (PDT). Its efficacy in head and neck squamous cell carcinoma led to its EU authorization, and mechanistically it may act through light-activated local destruction of tumour tissue.

The link to nasopharyngeal teratoma is weak. The nasopharynx is anatomically close to the head and neck region of the approved indication, and PDT acts locally on tumours. However, teratomas are germ-cell tumours with a histology distinct from squamous cell carcinoma, and no supporting data were compiled. The high score (99.78%) may partly reflect generic "neoplasm" associations in the knowledge graph rather than a specific biological rationale.

Other predictions in the top 10 list (all also without direct clinical trial support) are:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Odontogenic cyst | 99.77% | L5 | Benign, usually cured by surgery; weak risk-benefit case |
| 3 | Pre-malignant neoplasm | 99.77% | L5 | PDT is plausible for premalignant upper aerodigestive lesions, but the category is broad |
| 4 | Epiglottis neoplasm | 99.76% | L5 | Closest fit to the original indication, but needs site-specific data |
| 5 | Tumor of testis and paratestis | 99.76% | L5 | No anatomical or clinical rationale; likely a graph artifact |
| 6 | Cystic neoplasm | 99.76% | L4 | One indirect cohort publication |
| 7 | Benign neoplasm of floor of mouth | 99.76% | L5 | Accessible to light, but photosensitivity is unfavorable for benign disease |
| 8 | Benign neoplasm of tongue | 99.76% | L4 | One indirect cohort publication in malignant disease |
| 9 | Benign neoplasm of hypopharynx | 99.76% | L5 | General regional rationale only |
| 10 | Cervical neuroblastoma | 99.76% | L5 | Distinct biology; pediatric safety concern |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (nasopharyngeal teratoma), currently no related literature is available.

Two publications were found for lower-ranked predictions. They offer only indirect support for PDT in the head and neck region:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26179387](https://pubmed.ncbi.nlm.nih.gov/26179387/) | 2015 | Cohort | World J Surg Oncol | Preliminary experience with postoperative temoporfin-mediated PDT as adjuvant treatment after robot-assisted salvage surgery for recurrent squamous cell carcinoma of the base of tongue (linked to the benign neoplasm of tongue prediction) |
| [26072296](https://pubmed.ncbi.nlm.nih.gov/26072296/) | 2015 | Cohort | Photodiagn Photodyn Ther | Feasibility of PDT as adjuvant to surgery in recurrent malignant tumors of the paranasal sinuses (linked to the cystic neoplasm prediction) |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000318 (cancelled) | Foscan | Not specified | Palliative treatment of patients with advanced head and neck squamous cell carcinoma failing prior therapies and unsuitable for radiotherapy, surgery or systemic chemotherapy |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Photosensitizer for photodynamic therapy (light-activated cytotoxicity); not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

Please refer to the SmPC for safety information. No drug interaction records were found in the data compiled for this report. The prolonged photosensitivity typical of photosensitizers has been noted as a risk-benefit concern, particularly for benign conditions and pediatric patients, but it has not been verified against label text here.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for nasopharyngeal teratoma rests on a model score alone, with no trials or publications. The only EU authorization is cancelled, and warnings and contraindications from the label could not be obtained, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Safety information (warnings and contraindications) from the EMA product information
- Mechanism of action data, for example from DrugBank
- Site-specific preclinical or clinical evidence for the predicted indication (the epiglottis neoplasm and pre-malignant neoplasm predictions may be better-aligned candidates to examine first)
- Confirmation of why the EU authorization was cancelled and whether any formulation remains available
- A route and light-delivery feasibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

