---
layout: default
title: Trifluridine
parent: AI Predictions (L5)
nav_order: 642
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Trifluridine: predicted new indication Cecum villous adenoma (evidence level L5). Approved use: Metastatic colorectal cancer (with bevacizumab or as monotherapy) and…"
monitor_inn: "Trifluridine"
predicted_indications: ["cecum villous adenoma", "lipoma of colon", "colonic lymphangioma", "cecum neuroendocrine tumor G1", "rectosigmoid junction neoplasm", "colon leiomyoma", "cecal disease", "benign neoplasm of cecum", "cavernous hemangioma of colon", "photosensitivity disease"]
---

# Trifluridine
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

# Trifluridine: From Metastatic Colorectal and Gastric Cancer to Cecum Villous Adenoma

## One-Sentence Summary

Trifluridine (marketed as Lonsurf, combined with tipiracil) was originally approved for metastatic colorectal cancer and metastatic gastric cancer.
The TxGNN model predicts it may be effective for **cecum villous adenoma**, but **0 clinical trials** and **0 publications** currently support this specific use, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer (with bevacizumab or as monotherapy) and metastatic gastric cancer, including gastroesophageal junction adenocarcinoma, after prior therapies |
| Predicted New Indication | Cecum villous adenoma |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, trifluridine is a thymidine-based nucleoside analog that is incorporated into DNA. In the combination product it is paired with tipiracil, which inhibits thymidine phosphorylase and so prevents trifluridine from being broken down. Its efficacy in metastatic colorectal cancer has been established.

A villous adenoma of the cecum is anatomically and biologically related to colorectal neoplasia, because such adenomas are precursor lesions of colorectal cancer. This closeness in the knowledge graph is the most likely source of the high score. However, the prediction is weak as a repurposing hypothesis. A cytotoxic agent with significant myelosuppression has no plausible role in a benign lesion that can usually be removed endoscopically or surgically. The risk-benefit balance is unfavorable.

Other top-ranked predictions show the same pattern: benign colonic lesions (lipoma, lymphangioma, leiomyoma, cavernous hemangioma), a G1 neuroendocrine tumor, and an unrelated photosensitivity disorder. These look like artifacts of graph proximity rather than genuine mechanistic signals. The rectosigmoid junction neoplasm prediction largely restates the existing colorectal cancer label.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for cecum villous adenoma.

Two other predicted indications have indirect literature only. For "cecal disease", the three retrieved papers are case reports in patients with metastatic colorectal cancer. For "benign neoplasm of cecum", the single retrieved paper concerns an irinotecan-loaded bead procedure and is only weakly relevant. Neither provides efficacy evidence for a new use of trifluridine.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/003897 (cancelled) | Lonsurf | Not specified | Colorectal cancer: with bevacizumab or as monotherapy in previously treated adult patients with metastatic disease. Gastric cancer: monotherapy in... |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nucleoside analog, fluoropyrimidine-related class) |
| Myelosuppression Risk | Medium to high. Please refer to the SmPC warnings and precautions for details. |
| Emetogenicity Classification | Low to medium |
| Monitoring Items | Complete blood count with differential, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: 81 interactions were identified. Examples from the data reviewed:
  - **Major**: deferiprone, samarium (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, BCG live vaccine (Tice strain).
  - **Moderate**: strontium chloride Sr-89, roflumilast, chloramphenicol, azathioprine, alemtuzumab, anakinra, canakinumab, and several live or other vaccines.
  - Many of these involve immunosuppressants, biologics, or live vaccines, where added myelosuppression or immunosuppression is the concern.
- **Literature safety signal**: One case report described leukocytoclastic vasculitis with late-onset Henoch-Schönlein purpura after trifluridine/tipiracil treatment.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5), and a myelosuppressive cytotoxic drug is not appropriate for a benign, locally treatable lesion. The product's EU authorization is also cancelled.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank
- Warnings and contraindications from the SmPC (currently a blocking gap for safety screening)
- A biological rationale, and preclinical data, showing why trifluridine would act on villous adenoma
- A comparison with standard endoscopic or surgical management
- Clarification of the cancelled authorization status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

