---
layout: default
title: Ripretinib
parent: AI Predictions (L5)
nav_order: 526
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Ripretinib: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Advanced GIST in adults who have received prior treatment with three…"
monitor_inn: "Ripretinib"
predicted_indications: ["multiple endocrine neoplasia", "HER2 positive breast carcinoma", "infectious bovine rhinotracheitis", "malignant catarrh", "cytomegalovirus infection", "amenorrhea (disease)", "progesterone-receptor negative breast cancer", "progesterone-receptor positive breast cancer", "normal breast-like subtype of breast carcinoma", "breast tumor luminal A or B"]
---

# Ripretinib
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

# Ripretinib: From Gastrointestinal Stromal Tumour to Multiple Endocrine Neoplasia

## One-Sentence Summary

Ripretinib is a kinase inhibitor originally used to treat advanced gastrointestinal stromal tumour (GIST) after failure of three or more prior kinase inhibitors.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting this specific indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced GIST in adults who have received prior treatment with three or more kinase inhibitors, including imatinib |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 98.84% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (the single authorization has been cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ripretinib is known as a broad switch-control inhibitor of KIT and PDGFRA, the kinases that drive most GISTs, and it also inhibits other kinases. Its efficacy in GIST has been studied in the INVICTUS and INTRIGUE trials.

The link to multiple endocrine neoplasia is speculative. This condition is typically associated with drivers such as RET or MEN1, and no data connect ripretinib to these. The high score most likely reflects general oncology and kinase-inhibitor patterns in the knowledge graph rather than disease-specific support. Other top predictions (veterinary herpesvirus diseases, amenorrhea, several breast cancer subtypes) share similarly high scores without supporting evidence, which suggests the score alone is not a reliable signal for this drug.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for multiple endocrine neoplasia.

For context, the data compiled for this report contain publications on ripretinib in its existing GIST indication. These do not support the predicted indication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38182785](https://pubmed.ncbi.nlm.nih.gov/38182785/) | 2024 | RCT (post hoc biomarker analysis) | Nature Medicine | INTRIGUE trial ctDNA analysis: ripretinib vs sunitinib in GIST after imatinib; primary PFS was not superior to sunitinib |
| [34313371](https://pubmed.ncbi.nlm.nih.gov/34313371/) | 2021 | Clinical study | The Oncologist | INVICTUS analysis of dose escalation to 150 mg twice daily after progression in GIST |
| [38473346](https://pubmed.ncbi.nlm.nih.gov/38473346/) | 2024 | Cohort | Cancers | UK expanded access program: efficacy and safety of ripretinib in advanced GIST |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005614 | Qinlock | Not specified | Advanced GIST in adults who have received prior treatment with three or more kinase inhibitors, including imatinib (status: cancelled) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

- **Drug Interactions**: The interaction screening identified 90 potential interactions. The main ones are:
  - **Major**: clarithromycin, cobicistat
  - **Moderate** (examples): aprepitant, dexamethasone, cimetidine, miconazole, clotrimazole, rolapitant, deferasirox, fostamatinib, selexipag, pioglitazone, rosiglitazone, troglitazone, repaglinide, canagliflozin, eliglustat, metreleptin, fidaxomicin, glycerol phenylbutyrate

  Several of these are CYP3A4-related, which is consistent with a pharmacokinetic study showing that a P-gp/CYP3A4 inhibitor altered ripretinib exposure in rats.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (evidence level L5), with no trials, no relevant literature, and no plausible mechanistic link to multiple endocrine neoplasia. In addition, the only EU authorization has been cancelled.

**To proceed, the following is needed:**
- Mechanism of action data (e.g. from DrugBank) and an assessment of whether ripretinib's kinase profile touches drivers of multiple endocrine neoplasia (RET, MEN1)
- Preclinical evidence (cell line or animal models) for this condition
- Warnings and contraindications from the SmPC, which are currently missing and block safety screening
- Clarification of the reason for the EU authorization cancellation and the current regulatory status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

