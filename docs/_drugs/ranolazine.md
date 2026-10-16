---
layout: default
title: Ranolazine
parent: AI Predictions (L5)
nav_order: 508
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ranolazine: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Add-on therapy for the symptomatic treatment of patients with stable…"
monitor_inn: "Ranolazine"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "myositis fibrosa", "idiopathic granulomatous myositis", "tendinitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "fibromyalgia", "headache disorder", "conjunctivitis"]
---

# Ranolazine
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

# Ranolazine: From Stable Angina Pectoris to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Ranolazine is an add-on anti-anginal medicine, originally used for the symptomatic treatment of stable angina pectoris.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Add-on therapy for the symptomatic treatment of patients with stable angina pectoris who are inadequately controlled or intolerant to first-line anti-anginal therapies (such as beta-blockers and/or calcium antagonists) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ranolazine is generally known as a late sodium current inhibitor, and its efficacy in stable angina has been established. That mechanism, however, has no established link to nephrogenic syndrome of inappropriate antidiuresis.

This condition is driven by gain-of-function variants of the vasopressin V2 receptor (AVPR2), which is a renal water-handling problem. It differs fundamentally from angina, a cardiac ischaemic condition. The high TxGNN score is a knowledge-graph prediction only. No mechanistic rationale is supported by the available data, and the prediction should be treated as a hypothesis.

Other top-ranked predictions (for example rheumatoid arthritis, fibromyalgia, tendinitis and conjunctivitis) are likewise at the model-prediction level only. The headache disorder prediction has some indirect literature, but it is limited to a case report.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for nephrogenic syndrome of inappropriate antidiuresis.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000805 (status: cancelled) | Ranexa (previously Latixa) | Not specified | Add-on therapy for the symptomatic treatment of patients with stable angina pectoris who are inadequately controlled or intolerant to first-line anti-anginal therapies (such as beta-blockers and / or calcium antagonists). |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: Long QT syndrome, familial long QT syndrome, torsades de pointes, kidney disease, pyoureter, cirrhosis of liver. These relationships come from the TxGNN knowledge graph and should be confirmed against the SmPC. The kidney disease signal is especially relevant, as the predicted indication is a renal condition.
- **Drug Interactions**: 100 interactions were identified in total; the first 20 returned are summarised here.
  - **Major**: aprepitant, dexamethasone, clarithromycin, dolasetron, eliglustat
  - **Moderate**: famotidine, metformin, loperamide, bisacodyl, budesonide (including nasal), canagliflozin, dapagliflozin, empagliflozin, picosulfuric acid, polyethylene glycol (3350 with electrolytes), sodium sulfate
  - **Minor**: bupropion, lorcaserin, cimetidine

Please refer to the SmPC for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (L5), with no clinical trials or literature and no plausible mechanistic link between late sodium current inhibition and AVPR2 gain-of-function. In addition, the only EU authorization has been cancelled, and the knowledge graph flags kidney disease as a contraindication.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a mechanistic analysis relevant to V2 receptor signalling
- Warnings and contraindications from the SmPC, including renal safety
- Preclinical or in vitro evidence showing an effect on renal water handling or the AVPR2 pathway
- A literature and trial search specific to this condition
- If a more evidence-supported direction is preferred, a review of other candidates such as headache disorder, which currently has only case-level evidence (L4)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

