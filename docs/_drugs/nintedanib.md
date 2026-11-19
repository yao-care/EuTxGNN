---
layout: default
title: Nintedanib
parent: AI Predictions (L5)
nav_order: 430
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-12
description: "Nintedanib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L5). Approved use: Idiopathic pulmonary fibrosis (IPF) and other chronic fibrosing inter…"
monitor_inn: "Nintedanib"
predicted_indications: ["dermatofibrosarcoma protuberans", "liposarcoma", "ovarian myxoid liposarcoma"]
---

# Nintedanib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Nintedanib: From Idiopathic Pulmonary Fibrosis to Dermatofibrosarcoma Protuberans
{: .text-alpha }

## One-Sentence Summary

Nintedanib is a multi-target tyrosine kinase inhibitor, originally used to treat idiopathic pulmonary fibrosis (IPF), other progressive fibrosing interstitial lung diseases, and non-small cell lung cancer (in combination with docetaxel).
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**.
Support is currently limited to **0 clinical trials** and **1 publication** (an indirect 2018 review).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic pulmonary fibrosis (IPF) and other chronic fibrosing interstitial lung diseases with a progressive phenotype |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 0.9915 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 4 of 4) |
| Number of Authorizations | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Nintedanib is a multi-target tyrosine kinase inhibitor acting on PDGFR alpha/beta, FGFR 1-3 and VEGFR 1-3. According to the Mechanism of Action section of the US FDA-approved prescribing information for nintedanib: "Nintedanib is a small molecule that inhibits multiple receptor tyrosine kinases (RTKs) and non-receptor tyrosine kinases (nRTKs). Nintedanib inhibits the following RTKs: platelet-derived growth factor receptor (PDGFR) α and β, fibroblast growth factor receptor (FGFR) 1-3, vascular endothelial growth factor receptor (VEGFR) 1-3, colony stimulating factor 1 receptor (CSF1R), and Fms-like tyrosine kinase-3 (FLT-3)." ([DailyMed: Nintedanib Capsules, 100 Mg And 150 Mg (nintedanib) prescribing information, EXELAN PHARMACEUTICALS INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=60d8104e-cb6c-4f4f-8159-95ed57346ffa), label version 2026-04-21; accessed 2026-11-19.) The description above is based on the known pharmacology of the drug.

DFSP is driven by the COL1A1-PDGFB fusion, which causes constitutive activation of PDGFRB. Inhibiting PDGFR is therefore mechanistically plausible. Nintedanib's anti-fibrotic activity in lung disease also relies on blocking PDGFR and FGFR signalling in fibroblasts, and DFSP is a fibroblast-lineage tumour. This is the conceptual bridge between the original and the predicted indication.

There are important caveats. The only supporting record is a 2018 review of small-molecule PDGFR inhibitors in neoplastic disorders, which is indirect evidence and not a nintedanib-specific study. Imatinib is the established PDGFR-directed therapy for DFSP, so nintedanib would need to show an advantage (for example, in imatinib-resistant disease) to be of interest.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Review of small-molecule PDGFR inhibitors in neoplastic disorders; indirect support for PDGFR targeting, not specific to nintedanib |

## EU Market Information

All four authorizations are currently valid.

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/002569 | Vargatef | nintedanib | Valid |
| EMEA/H/C/003821 | Ofev | nintedanib | Valid |
| EMEA/H/C/006179 | Nintedanib Accord | nintedanib | Valid |
| EMEA/H/C/006486 | Nintedanib Viatris | nintedanib | Valid |

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction screening. The entries reviewed include:
  - **Major**: Dexamethasone
  - **Moderate**: Acetylsalicylic acid, clarithromycin, naltrexone, rolapitant, cobicistat
  - **Moderate (antithrombotic and anticoagulant agents)**: abciximab, alteplase, antithrombin III, apixaban, dipyridamole, betrixaban, bivalirudin, cangrelor, caplacizumab, cilostazol, clopidogrel, dalteparin, defibrotide, desirudin

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high and the PDGFRB-driven biology of DFSP makes the mechanism plausible. However, there are no clinical trials and only one indirect review, and imatinib is already the established targeted therapy. In addition, nintedanib is currently marketed in this country, with 4 valid licences out of 4.

**To proceed, the following is needed:**
- Nintedanib-specific preclinical data in DFSP models, particularly imatinib-resistant ones
- A comparison with imatinib to define a clear niche
- Confirmation of the current EU regulatory and supply status
- Safety information from the SmPC (warnings and contraindications), which was not available for this report
- Detailed mechanism-of-action data from DrugBank

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data from DrugBank were not available for this report, so t" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nintedanib Capsules, 100 Mg And 150 Mg (nintedanib) prescribing information, EXELAN PHARMACEUTICALS INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=60d8104e-cb6c-4f4f-8159-95ed57346ffa) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

