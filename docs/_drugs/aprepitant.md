---
layout: default
title: Aprepitant
parent: AI Predictions (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Aprepitant: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Prevention of postoperative nausea and vomiting (PONV) in adults"
monitor_inn: "Aprepitant"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "hypertrichosis (disease)", "pulmonary hypertension", "leprosy", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "kyphoscoliotic heart disease", "syndrome with a Dandy-Walker malformation as major feature", "subarachnoid hemorrhage (disease)", "isolated genetic hair shaft abnormality"]
---

# Aprepitant
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

# Aprepitant: From Postoperative and Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Aprepitant is a substance P/NK1 receptor antagonist, originally used to prevent nausea and vomiting after surgery and during cancer chemotherapy.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of postoperative nausea and vomiting (PONV) in adults; prevention of nausea and vomiting associated with chemotherapy (other strengths and formulations) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Aprepitant blocks the NK1 receptor, the target of substance P. This is the basis of its antiemetic effect. Detailed mechanism of action data is not available in the data compiled for this report, so this description relies on its known drug class.

The link between the original and predicted indications is weak. Nephrogenic SIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2). These act downstream of any effect NK1 signalling might have on neuroendocrine or fluid regulation. The connection is speculative, and no clinical or literature evidence supports it.

The very high TxGNN score (99.97%) is a computational prediction from a knowledge graph. It is not evidence of efficacy and should be treated as a hypothesis only.

Other predicted indications in the data (hypertrichosis, pulmonary hypertension, leprosy, subarachnoid haemorrhage and others) also score above 99.8%. All are at evidence level L5 with a Hold recommendation. Subarachnoid haemorrhage has the most plausible biological rationale, based on preclinical work on substance P/NK1 signalling in blood-brain barrier disruption and cerebral oedema, but it remains hypothetical.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000527 (cancelled) | Emend | Not specified | Emend 40 mg hard capsules is indicated for the prevention of postoperative nausea and vomiting (PONV) in adults. Emend is also available as 80 mg and 125 m... |

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: The TxGNN knowledge graph lists liver failure as a drug-disease contraindication.
- **Drug Interactions**: 100 interactions were found in the DDInter database. Examples:
  - **Major**: fentanyl, alfentanil, acalabrutinib
  - **Moderate**: paclitaxel, abemaciclib, nifedipine, ibuprofen, hydrocortisone, levonorgestrel, fluvoxamine, fosphenytoin, gefitinib, rabeprazole, lidocaine
  - **Minor**: dolutegravir

  Many of these likely reflect aprepitant's metabolism through CYP3A4. Please refer to the SmPC for full details.

Please refer to the SmPC for warnings and precautions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (evidence level L5). The proposed mechanism is speculative, because the cause of nephrogenic SIAD lies downstream of NK1 signalling. The EU authorization is also cancelled.

**To proceed, the following is needed:**
- Detailed mechanism of action data for aprepitant
- Preclinical or mechanistic studies testing whether NK1 antagonism affects V2 receptor-mediated water handling
- Label warnings and contraindications from the current SmPC, to allow safety screening
- Clarification of the cancelled EU authorization status and available dosage forms
- Comparison with other predicted indications, such as subarachnoid haemorrhage, where the biological rationale is more plausible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

