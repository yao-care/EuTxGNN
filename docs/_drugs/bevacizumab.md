---
layout: default
title: Bevacizumab
parent: AI Predictions (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

# Bevacizumab: From Metastatic Colorectal Cancer to Epiglottis Neoplasm

## One-Sentence Summary

Bevacizumab is an anti-VEGF monoclonal antibody, originally used to treat metastatic colon or rectal cancer and several other cancers.
The TxGNN model predicts it may be effective for **epiglottis neoplasm**, but **no clinical trials and no publications** were found for this indication, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic carcinoma of the colon or rectum (in combination with fluoropyrimidine-based chemotherapy), plus breast, lung, kidney, ovarian and cervical cancers |
| Predicted New Indication | Epiglottis neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorizations in the data compiled for this report) |
| Number of Authorizations | 10 (all cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, bevacizumab neutralizes VEGF-A, a key signal that drives new blood vessel growth in tumors. Its efficacy in colorectal cancer and other solid tumors is established, and mechanistically it could plausibly affect angiogenesis in head and neck tumors such as epiglottis neoplasm.

The link is only plausible, not demonstrated. No trials or publications were retrieved for epiglottis neoplasm, so the high model score is not clinical evidence.

**Other predictions in the same run** (all rated Hold except the cystic neoplasm entry, which the data rate Research Question):
- **Cystic neoplasm (99.89%)**: The data match this term mostly through ovarian tumors. Ovarian cancer is already an approved use, so this is not true repurposing. It has the strongest supporting evidence, including a Phase 3 trial (NCT00565851, n=1052). Subtype-specific questions, such as low-grade serous ovarian cancer, remain open.
- **Benign neoplasm of tongue, benign neoplasm of floor of mouth, cervical neuroblastoma, nasal cavity inverting papilloma**: Only indirect evidence (preclinical, case-level or non-specific trials). Evidence level L4.
- **Tumor of testis and paratestis, benign neoplasm of hypopharynx, mesenchymoma, schwannoma of jugular foramen**: Prediction only (L5). Bevacizumab has known activity in NF2-related vestibular schwannoma, a plausible neighbor, but no evidence was retrieved for jugular foramen schwannoma.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for epiglottis neoplasm.

---

## Literature Evidence

Currently no related literature available for epiglottis neoplasm.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/005286 | Alymsys | Not specified | Alymsys in combination with fluoropyrimidine based chemotherapy is indicated for treatment of adult patients with metastatic carcinoma of the colon or rectum. Alymsys in comb... |
| EMEA/H/C/000582 | Avastin | Not specified | Bevacizumab in combination with fluoropyrimidine-based chemotherapy is indicated for treatment of adult patients with metastatic carcinoma of the colon or rectum. Bevaci... |
| EMEA/H/C/004728 | Mvasi | Not specified | Mvasi in combination with fluoropyrimidine-based chemotherapy is indicated for treatment of adult patients with metastatic carcinoma of the colon or rectum. Mvasi in com... |
| EMEA/H/C/004697 | Zirabev | Not specified | Zirabev in combination with fluoropyrimidine-based chemotherapy is indicated for treatment of adult patients with metastatic carcinoma of the colon or rectum. Zirabev in ... |
| EMEA/H/C/005723 | Lytenava | Not specified | Lytenava is indicated in adults for treatment of neovascular (wet) age-related macular degeneration (nAMD). |

Five more authorizations are listed in the data (Aybintio, Vegzelma, Abevmy, Avzivi, Oyavas). All 10 are recorded as cancelled.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGF monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 22 interactions were recorded in total; 20 are listed in the data. The major-level interactions are:
  - Deferiprone
  - Samarium (153Sm) lexidronam
  - Panitumumab
  - Sunitinib
  - Thalidomide

  Moderate-level interactions include bisphosphonates (alendronic acid, risedronic acid, etidronic acid, ibandronate, pamidronic acid, tiludronic acid), growth factors (filgrastim, pegfilgrastim, sargramostim, palifermin), radiopharmaceuticals (strontium chloride Sr-89, radium Ra 223, sodium phosphate P32), idelalisib and romosozumab.

For warnings and contraindications, please refer to the SmPC.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The epiglottis neoplasm prediction has a very high model score but no trials or literature behind it (L5). Bevacizumab also has no currently valid EU authorization in the data compiled, and safety label data are missing.

**To proceed, the following is needed:**
- EU package insert (SmPC) warnings and contraindications, which block safety screening
- Mechanism of action data, for example from DrugBank
- Disease-specific evidence for epiglottis neoplasm, such as head and neck cancer trials or case series
- Clarification of the current EU authorization status, since all 10 licenses are cancelled
- If a related indication is pursued, the cystic neoplasm (ovarian subtype) question is the best-supported lead, though it overlaps with an approved use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

