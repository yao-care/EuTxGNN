---
layout: default
title: Varenicline
parent: AI Predictions (L5)
nav_order: 658
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Varenicline: predicted new indication Migraine disorder (evidence level L5). Approved use: Smoking cessation in adults"
monitor_inn: "Varenicline"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "alopecia", "open-angle glaucoma", "primary hereditary glaucoma", "headache disorder", "pulmonary hypertension"]
---

# Varenicline
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

# Varenicline: From Smoking Cessation to Migraine Disorder

## One-Sentence Summary

Varenicline is a prescription medicine originally used to help adults stop smoking.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 clinical trials** and only **1 linked publication** (a case report of a safety event, not evidence of benefit), so this prediction rests on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Smoking cessation in adults |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Varenicline acts on nicotinic acetylcholine receptors. It is a partial agonist at the alpha4beta2 receptor and a full agonist at the alpha7 receptor. Its benefit in smoking cessation comes from easing cravings and withdrawal while reducing the reward from smoking. The mechanism of action data compiled for this report is not available in structured form, so this description comes from the mechanistic rationale in the prediction data.

The link to migraine is speculative. Nicotinic cholinergic signalling may play a role in modulating pain pathways involving the trigeminal nerve and blood vessels, but no clinical data support this. The TxGNN score is very high, yet it is a computational prediction only.

The one linked publication is a case report of cardiac arrest in a patient taking varenicline. It is a safety signal rather than evidence of migraine efficacy, and it raises a cardiovascular concern. For headache more broadly, the linked literature (13 papers) mostly reports headache as a common side effect of varenicline in smoking cessation studies, which is the opposite of a repurposing signal.

Other predictions in the list (all L5, all Hold) include migraine with brainstem aura, alopecia-related conditions, glaucoma, headache disorder and pulmonary hypertension. None has clinical trials, and several have no plausible mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | Case report | Therapie | Cardiac arrest in a patient taking varenicline; an adverse event report, not evidence of migraine benefit |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000699 | Champix | Not specified | Smoking cessation in adults (status: cancelled) |

## Safety Considerations

- **Possible contraindication signals from the knowledge graph** (drug-disease links in the TxGNN knowledge graph, not taken from product label text): anxiety disorder, neurotic disorder, dysthymic disorder, bipolar disorder, major affective disorder, substance abuse/dependence, schizophrenia, acute coronary syndrome, peripheral vascular disease, intermittent claudication, and peripheral arterial disease. These flag psychiatric and cardiovascular cautions that need verification against the official label.
- **Cardiovascular concern**: the only linked publication for the predicted indication reports cardiac arrest with varenicline.
- **Drug interactions**: the data compiled for this report lists 100 potential interactions. Only cimetidine is graded (Minor). The rest, such as phentermine, metformin, morphine, simvastatin, prednisone and epinephrine, have no severity grade and need review.

For full warnings and contraindications, please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No trials exist, and the single linked paper is a cardiac safety case report. Varenicline's EU authorization is cancelled, and the knowledge graph flags psychiatric and cardiovascular cautions, so there is no basis to advance.

**To proceed, the following is needed:**
- Official EU safety information (warnings and contraindications from the SmPC), which is currently missing and blocks safety screening
- Detailed mechanism of action data
- Preclinical or early clinical evidence that varenicline reduces migraine, given that headache is a known adverse effect
- A cardiovascular and neuropsychiatric risk assessment for a migraine population
- Clarification of why the EU authorization was cancelled and of the regulatory pathway for any new use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

