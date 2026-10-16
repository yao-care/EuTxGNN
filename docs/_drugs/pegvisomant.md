---
layout: default
title: Pegvisomant
parent: AI Predictions (L5)
nav_order: 476
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pegvisomant: predicted new indication Borderline ovarian serous tumor (evidence level L5). Approved use: Treatment of adult patients with acromegaly who have had an inadequat…"
monitor_inn: "Pegvisomant"
predicted_indications: ["borderline ovarian serous tumor", "rete ovarii cystadenoma", "ovarian papillary cystadenoma", "pyelonephritis", "malignant ovarian Brenner tumor", "aleukemic mast cell leukemia", "ovarian mucinous cystadenofibroma", "ovarian benign neoplasm", "mucinous ovarian cystadenoma", "ovarian surface papilloma"]
---

# Pegvisomant
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

# Pegvisomant: From Acromegaly to Borderline Ovarian Serous Tumor

## One-Sentence Summary

Pegvisomant was originally used to treat acromegaly in adults who did not respond adequately to surgery, radiation, or somatostatin analogues.
The TxGNN model predicts it may be effective for **borderline ovarian serous tumor**,
but there are currently **no clinical trials** and **no publications** supporting this direction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of adult patients with acromegaly who have had an inadequate response to surgery and/or radiation therapy and in whom an appropriate medical treatment with somatostatin analogues did not normalize IGF-I concentrations or was not tolerated |
| Predicted New Indication | Borderline ovarian serous tumor |
| TxGNN Prediction Score | 98.63% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pegvisomant is known as a growth hormone (GH) receptor antagonist. Its efficacy in acromegaly is based on lowering circulating IGF-I, the downstream mediator of GH excess.

A speculative link is that GH/IGF-I signaling can promote the proliferation of epithelial ovarian tissue. Blocking this axis might therefore affect ovarian epithelial tumours. This idea is unvalidated and no data compiled for this report supports it.

Note that the nine other top-ranked predictions have nearly identical scores (about 0.985–0.986). They are mostly benign or borderline ovarian neoplasms, which suggests the scores reflect a shared neighbourhood in the knowledge graph rather than independent evidence. Some predictions, such as pyelonephritis (a bacterial infection) and aleukemic mast cell leukemia, have no plausible mechanistic link and are likely model artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000409 (cancelled) | Somavert | Not specified | Treatment of adult patients with acromegaly who have had an inadequate response to surgery and/or radiation therapy and in whom an appropriate me... |

## Safety Considerations

- **Drug Interactions**: 74 interactions were identified, and the 20 listed in the data compiled for this report are all rated Moderate. They are mainly with glucose-lowering agents, and monitoring of blood glucose may be needed when used together:
  - Insulins: insulin human, insulin aspart
  - Sulfonylureas: chlorpropamide, acetohexamide, glimepiride, glipizide, glyburide
  - Biguanide: metformin
  - Thiazolidinedione: pioglitazone
  - α-Glucosidase inhibitor: acarbose
  - DPP-4 inhibitor: alogliptin
  - GLP-1 agonists: albiglutide, dulaglutide, exenatide
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
  - Others: morphine, pegvaliase

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, and the mechanistic link is speculative. The only EU authorization is cancelled, and warnings and contraindications are not available, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Warnings and contraindications from the EU product information (SmPC)
- Mechanism of action data from DrugBank
- A literature search on GH/IGF-I signaling in ovarian epithelial tumours, and preclinical evidence in relevant models
- Clarification of why the Somavert authorization was cancelled (e.g., commercial or regulatory reasons) and of current EU availability
- Confirmation that the tumour predictions are not a graph-neighbourhood artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

