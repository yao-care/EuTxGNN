---
layout: default
title: Lumacaftor
parent: AI Predictions (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Lumacaftor: predicted new indication Leprosy (evidence level L5). Approved use: Cystic fibrosis (CF) in patients aged 6 years and older (tablets) or…"
monitor_inn: "Lumacaftor"
predicted_indications: ["leprosy", "migraine with or without aura, susceptibility to", "migraine disorder", "rheumatoid arthritis", "pulmonary hypertension", "kyphoscoliotic heart disease", "migraine with brainstem aura", "multiple endocrine neoplasia", "brachydactyly-syndactyly syndrome", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Lumacaftor
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

# Lumacaftor: From Cystic Fibrosis to Leprosy

## One-Sentence Summary

Lumacaftor is a CFTR corrector, originally used (in the Orkambi combination) to treat cystic fibrosis in patients homozygous for the F508del mutation.
The TxGNN model predicts it may be effective for **leprosy**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. The prediction is based on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic fibrosis (CF) in patients aged 6 years and older (tablets) or 1 year and older (granules) who are homozygous for the F508del mutation in the CFTR gene |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known information, lumacaftor is a CFTR corrector that improves the folding and trafficking of the F508del-CFTR protein. Its use in cystic fibrosis is established.

No plausible link between CFTR correction and leprosy (a *Mycobacterium leprae* infection with associated neuropathy) is supported by the available data. The high score (0.994) comes from a graph-based prediction and does not reflect a validated biological rationale. This prediction should be treated as a hypothesis only.

Other top-ranked predictions are also model-only signals without supporting studies. Three of the ten are migraine entries (migraine with or without aura susceptibility, migraine disorder, migraine with brainstem aura). They overlap and should be read as one signal, not independent evidence. The remaining predictions are rheumatoid arthritis, pulmonary hypertension, kyphoscoliotic heart disease, multiple endocrine neoplasia, brachydactyly-syndactyly syndrome, and nephrogenic syndrome of inappropriate antidiuresis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003954 (status: cancelled) | Orkambi | Not specified | Orkambi tablets are indicated for the treatment of cystic fibrosis (CF) in patients aged 6 years and older who are homozygous for the F508del... |

## Safety Considerations

- **Drug Interactions**: The interaction screening returned 100 interacting drugs in total. Lumacaftor is a strong CYP3A inducer, which is consistent with this high count. The first 20 entries reviewed include:
  - **Major**: eliglustat, naldemedine, naloxegol, rolapitant
  - **Moderate**: proton pump inhibitors and H2 blockers (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole, ranitidine), antidiabetic agents (acetohexamide, glimepiride, linagliptin, pioglitazone, repaglinide), corticosteroids (betamethasone, prednisone), bupropion, and nitisinone
- **Pulmonary hypertension note**: If this indication were pursued, the CYP3A induction would complicate co-therapy with common pulmonary hypertension drugs and should be assessed first.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The leprosy prediction has a high model score but no clinical trials, no literature, and no supported mechanistic link (Evidence Level L5). The only EU authorization is cancelled, and warning and contraindication data are missing, so the candidate cannot yet proceed to safety screening.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to test any plausible link between CFTR correction and leprosy
- EU SmPC warnings and contraindications for safety screening
- Independent preclinical or literature support for the leprosy hypothesis
- A review of whether the other predicted indications (especially the overlapping migraine entries) offer a stronger rationale
- A drug-interaction assessment given strong CYP3A induction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

