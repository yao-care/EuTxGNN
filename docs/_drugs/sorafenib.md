---
layout: default
title: Sorafenib
parent: AI Predictions (L5)
nav_order: 572
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-06
monitor_inn: "Sorafenib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "female breast carcinoma", "renal pelvis carcinoma", "vulva sarcoma", "dermatofibrosarcoma protuberans"]
description: "Sorafenib: predicted new indication Liposarcoma (evidence level L5). Approved use: Hepatocellular carcinoma Nexavar is indicated for the treatment of he…"
---

# Sorafenib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Sorafenib: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Sorafenib is an oral multi-kinase inhibitor that is already marketed in the European Union as an anticancer drug. The TxGNN model predicts it may be useful for **liposarcoma**. The evidence level is **L5**, because no clinical trial or publication tests sorafenib in liposarcoma itself. The one related trial enrolled advanced soft tissue sarcoma patients in general.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatocellular carcinoma Nexavar is indicated for the treatment of hepatocellular carcinoma. Renal cell carcinoma Nexavar is indicated for the treatment of patients with advanced renal cell carcinoma who have failed prior interferon-alpha or interleukin-2 based therapy or are considered unsuitable f |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 2 of 2) |
| Number of Authorizations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the data compiled for this report. Sorafenib is a multi-kinase inhibitor acting on the RAF/MEK/ERK pathway and on receptors such as VEGFR, PDGFR and KIT. Blood-vessel growth signalling and PDGFR signalling both contribute to soft tissue sarcoma biology.

Liposarcoma is a subtype of soft tissue sarcoma. In a preclinical study, sorafenib reduced growth and MAPK signalling in nerve sheath tumour cell lines, which included dedifferentiated liposarcoma cell lines (LS141 and DDLS). That study mainly concerns another tumour type, so it is not a direct test of sorafenib in liposarcoma.

The high TxGNN score fits this mechanistic plausibility, but it is a model output and not clinical proof. Whether sorafenib has activity specific to liposarcoma has not been established.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Single-arm trial of sorafenib alone in advanced soft tissue sarcomas. It is a mixed-histology study, not specific to liposarcoma, and the single-arm design limits conclusions about cause and effect. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 trial | Cancer | SWOG S0505 intergroup trial of sorafenib in advanced soft tissue sarcomas. It covers the sarcoma group as a whole, not liposarcoma specifically. |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 trial | Ann Surg Oncol | Neoadjuvant radiotherapy plus sorafenib in locally advanced extremity soft tissue sarcoma. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | Treatment of soft tissue sarcomas is increasingly guided by histological subtype. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magy Onkol | Overview of drug treatment of soft tissue sarcomas by histological subtype. |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Mol Cancer Ther | Sorafenib inhibited growth and MAPK signalling in nerve sheath tumour cells, including dedifferentiated liposarcoma cell lines. |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical | Am J Pathol | Dedifferentiated liposarcoma xenograft models showing a response to PI3K pathway inhibition. This study does not test sorafenib. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | Patient-derived xenograft models in sarcoma, focused on the CDK inhibitor palbociclib. |

---

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000690 | Nexavar | sorafenib | Valid |
| EMEA/H/C/005921 | Sorafenib Accord | sorafenib tosilate | Valid |

<!-- licenses:end -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were found. The main ones listed here are:
  - Major: dolasetron.
  - Moderate: famotidine, loperamide, dexamethasone, clarithromycin, levofloxacin, palonosetron, naltrexone, and several laxatives and bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate, lactulose, lactitol).

Warnings and contraindications from the label were not available in the data compiled for this report. Please refer to the SmPC for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- No study tests sorafenib in liposarcoma itself, so the evidence level is L5. The only clinical signals come from mixed soft tissue sarcoma populations, and the very high score of 0.9982 is not evidence of benefit.

**To proceed, the following is needed:**
- Histology-specific results for liposarcoma patients from the soft tissue sarcoma trials, or a dedicated liposarcoma study.
- Mechanism-of-action data for sorafenib to support the mechanistic link.
- Label warnings and contraindications from the SmPC, to complete the safety review.

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

