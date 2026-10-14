---
layout: default
title: Buprenorphine
parent: Medium Evidence (L3-L4)
nav_order: 113
evidence_level: L4
indication_count: 10
---

# Buprenorphine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Buprenorphine: From Opioid Dependence to Acute Intermittent Porphyria

## One-Sentence Summary

Buprenorphine is an opioid medicine originally authorised in the EU for substitution treatment of opioid dependence.
The TxGNN model predicts it may be effective for **acute intermittent porphyria**, but the prediction is supported by **0 clinical trials** and **1 publication** (a 1993 anaesthetic case report that shows no therapeutic benefit).
This is essentially a model-only prediction, and it should not be treated as a credible repurposing lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of opioid dependence within a framework of medical, social and psychological treatment (adults and adolescents aged 16 years or over) |
| Predicted New Indication | Acute intermittent porphyria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| EU Market Status | ✗ Cancelled only (no currently valid authorisation) |
| Number of Authorizations | 2 (both cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data are not available in the data compiled for this report. Buprenorphine is an opioid used for opioid dependence, and its efficacy in that setting is established. No mechanistic route to acute intermittent porphyria has been identified.

The only publication retrieved is a 1993 Japanese case report on anaesthetic management of a patient with suspected acute intermittent porphyria undergoing gynaecological cancer surgery. It describes perioperative care and does not show that buprenorphine treats the disease. The very high TxGNN score is therefore not supported by clinical or mechanistic evidence. It likely reflects network proximity in the knowledge graph rather than a true therapeutic link.

Safety of buprenorphine in porphyria has also not been addressed in the available evidence. This matters because porphyria patients are sensitive to many drugs.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case report | Masui (Japanese Journal of Anesthesiology) | Anaesthetic management of a 40-year-old woman with suspected acute intermittent porphyria undergoing hysterectomy. It concerns perioperative care, not treatment benefit. |

---

## EU Market Information

Both authorisations are cancelled, so no product is currently authorised under these licences.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004651 | Buvidal | Not specified | Treatment of opioid dependence within a framework of medical, social and psychological treatment. Tr... |
| EMEA/H/C/006188 | Buprenorphine Neuraxpharm | Not specified | Substitution treatment of opioid drug dependence, within a comprehensive therapeutic monitoring fram... |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease links in the TxGNN knowledge graph, not label text):
  - Cardiovascular: long QT syndrome (including familial), torsades de pointes, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy.
  - Respiratory: COPD, respiratory failure.
  - Liver: liver disease, chronic hepatitis B and C virus infection, gallbladder disease.
  - Endocrine: adrenocortical insufficiency (Addison disease), hypothyroidism.
  - Gastrointestinal and urinary: paralytic ileus, intestinal obstruction, benign prostatic hyperplasia, urethral stricture.
  - Neurological: intracranial hypertension, pseudotumor cerebri.
  - Substance use: drug dependence and substance-related disorders.
  - Porphyria is not among the listed conditions, and this absence does not establish safety.
- **Drug Interactions**: 100 interactions are recorded. Major-level examples include morphine, bupropion, alvimopan, cisapride and dolasetron. Moderate-level examples include famotidine, loperamide, atropine, dexamethasone and clarithromycin.

For label warnings and contraindications, please refer to the SmPC.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no clinical trials and one unrelated case report. Both EU authorisations are cancelled, and safety in porphyria has not been addressed.

Among the other predictions for this drug, **schizophrenia** has the strongest evidence. It has one ongoing Phase 2 trial (NCT05778591, low-dose buprenorphine for social motivation, n=40, recruiting) and a plausible kappa-opioid mechanism. It is a more reasonable focus for any further work than acute intermittent porphyria.

**To proceed, the following is needed:**
- Mechanism of action data and a documented mechanistic link to acute intermittent porphyria
- A porphyria-specific safety review (porphyrinogenic potential), including the SmPC warnings and contraindications
- Any controlled or observational clinical data in porphyria
- Clarification of the regulatory status, since both EU licences are cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

