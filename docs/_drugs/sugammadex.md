---
layout: default
title: Sugammadex
parent: AI Predictions (L5)
nav_order: 578
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sugammadex: predicted new indication Breast fibrocystic disease (evidence level L5). Approved use: Reversal of neuromuscular blockade induced by rocuronium or vecuroniu…"
monitor_inn: "Sugammadex"
predicted_indications: ["breast fibrocystic disease", "Prinzmetal angina", "peripheral arterial disease", "blunt duct adenosis of breast", "apocrine adenosis of breast", "thrombotic disease", "tendinitis", "antithrombin deficiency type 2", "benign mammary dysplasia", "female breast carcinoma"]
---

# Sugammadex
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

# Sugammadex: From Reversal of Neuromuscular Blockade to Breast Fibrocystic Disease

## One-Sentence Summary

Sugammadex was originally developed to reverse neuromuscular blockade caused by rocuronium or vecuronium during anaesthesia.
The TxGNN model predicts it may be effective for **breast fibrocystic disease**, but **no clinical trials and no supporting publications** currently exist for this direction.
The prediction rests on model output alone and is best treated as a computational artifact until shown otherwise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Reversal of neuromuscular blockade induced by rocuronium or vecuronium in adults (paediatric use is limited to routine reversal of rocuronium-induced blockade) |
| Predicted New Indication | Breast fibrocystic disease |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorizations) |
| Number of Authorizations | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, sugammadex is a modified gamma-cyclodextrin. It encapsulates steroidal neuromuscular blocking agents (rocuronium and vecuronium), which inactivates them.

This is a highly specific, binding-based action. Fibrocystic breast disease is a benign, hormone-responsive condition. No plausible mechanistic link exists between the two. Sugammadex has no known activity on mammary tissue.

The high score (98.49%) most likely reflects network-based artifacts in the knowledge graph. Several closely related benign breast terms (blunt duct adenosis, apocrine adenosis, benign mammary dysplasia) receive nearly identical scores, which points to clustering of related ontology terms rather than independent evidence. The other top-ranked predictions, such as Prinzmetal angina, peripheral arterial disease, tendinitis and antithrombin deficiency, also lack any mechanistic support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for breast fibrocystic disease.

Publications were found only for other lower-ranked predictions (thrombotic disease and female breast carcinoma). They describe perioperative or anaesthetic use of sugammadex, such as coagulation testing in morbidly obese patients, and case reports in malignant hyperthermia and myasthenia gravis. They do not show a therapeutic effect on those diseases and are not evidence for the predicted indication.

---

## EU Market Information

All six authorizations are cancelled. No valid authorization remains.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000885 | Bridion | Not specified | Reversal of neuromuscular blockade induced by rocuronium or vecuronium. For the peadiatric population: sugammadex is only recomm... |
| EMEA/H/C/005403 | Sugammadex Mylan | Not specified | Reversal of neuromuscular blockade induced by rocuronium or vecuronium in adults. For the paediatric population: sugammadex... |
| EMEA/H/C/005760 | Sugammadex Fresenius Kabi | Not specified | Reversal of neuromuscular blockade induced by rocuronium or vecuronium in adults. For the paediatric population: sugammadex... |
| EMEA/H/C/005935 | Sugammadex Amomed | Not specified | Reversal of neuromuscular blockade induced by rocuronium or vecuronium. For the paediatric population: sugammadex is only reco... |
| EMEA/H/C/006046 | Sugammadex Adroiq | Not specified | Reversal of neuromuscular blockade induced by rocuronium or vecuronium in adults.For the paediatric population: sugammadex is... |

---

## Safety Considerations

- **Drug Interactions**: 31 interactions were identified in total. The main ones listed here are from the first 20 records compiled.
  - **Major**: hormonal contraceptives and progestogens (levonorgestrel, norethisterone, desogestrel, norgestrel, drospirenone, medroxyprogesterone acetate)
  - **Moderate**: anticoagulants and antithrombotics (warfarin, apixaban, rivaroxaban, edoxaban, betrixaban, dalteparin, bivalirudin, argatroban, desirudin, danaparoid, ardeparin, anisindione, antithrombin III human, antithrombin alfa)

Because the predicted indication involves hormone-responsive breast tissue, the major interactions with hormonal agents would be directly relevant in any future use. Interactions with anticoagulants are also relevant, since sugammadex can transiently affect coagulation parameters.

Please refer to the SmPC for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, and no plausible mechanistic link exists. In addition, all EU authorizations are currently cancelled, and sugammadex carries major interactions with hormonal agents that are commonly relevant in breast conditions.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological rationale linking encapsulation of steroidal agents to fibrocystic breast pathology
- Preclinical or observational evidence of any benefit in benign breast disease
- Full SmPC warnings and contraindications, which have not yet been retrieved
- Clarification of the EU regulatory status, including why all six authorizations are cancelled
- Review of whether the high scores for related benign breast terms result from knowledge-graph clustering rather than independent signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

