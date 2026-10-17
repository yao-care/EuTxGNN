---
layout: default
title: Sorafenib
parent: High Evidence (L1-L2)
nav_order: 572
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-15
description: "Sorafenib: predicted new indication Liposarcoma (evidence level L2). Approved use: Hepatocellular carcinoma"
monitor_inn: "Sorafenib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "female breast carcinoma", "renal pelvis carcinoma", "vulva sarcoma", "dermatofibrosarcoma protuberans"]
---

# Sorafenib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Sorafenib: From Hepatocellular Carcinoma to Liposarcoma

## One-Sentence Summary

Sorafenib is a multi-kinase inhibitor originally used to treat hepatocellular carcinoma, advanced renal cell carcinoma, and differentiated thyroid carcinoma.
The TxGNN model predicts it may be effective for **liposarcoma**, with **1 clinical trial** (a mixed soft tissue sarcoma study) and **8 publications** currently related to this direction.
The evidence is indirect: no study has been specific to liposarcoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatocellular carcinoma; advanced renal cell carcinoma (after failure of interferon-alpha or interleukin-2 therapy, or when unsuitable for it); progressive differentiated thyroid carcinoma refractory to radioactive iodine |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| EU Market Status | Cancelled only (the single Nexavar authorization is cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally recorded in the data compiled for this report. Based on known information, sorafenib is a multi-kinase inhibitor acting on the RAF/MEK/ERK pathway and on VEGFR, PDGFR, and KIT. Its efficacy in hepatocellular and renal cell carcinoma has been established.

Angiogenic and PDGFR signalling contribute to soft tissue sarcoma biology, and preclinical work shows that MAPK pathway inhibition by sorafenib suppresses growth in sarcoma models. These include a dedifferentiated liposarcoma cell line in a malignant peripheral nerve sheath tumour study. Liposarcoma is one subtype within the broader soft tissue sarcoma population studied clinically.

The very high TxGNN score is consistent with this mechanistic plausibility, but it is not clinical proof. Activity specific to liposarcoma has not been established.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Single-agent sorafenib in advanced soft tissue sarcomas. Mixed histologies including liposarcoma, single-arm design, so causal inference is limited |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 trial (SWOG S0505) | Cancer | Sorafenib, a multi-targeted tyrosine kinase inhibitor, studied in advanced soft tissue sarcomas |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 trial | Ann Surg Oncol | Neoadjuvant conformal radiotherapy plus sorafenib in locally advanced extremity soft tissue sarcoma |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | Histology-driven therapy for soft tissue sarcomas; trabectedin has high activity in liposarcoma |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Medical treatment of soft tissue sarcomas by histological subtype |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Mol Cancer Ther | Sorafenib inhibits growth and MAPK signalling in MPNST cells and dedifferentiated liposarcoma lines |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical | Am J Pathol | Dedifferentiated liposarcoma xenograft models and response to PI3K pathway inhibition (not sorafenib-specific) |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Front Oncol | Sarcoma PDOX models and palbociclib combinations (not sorafenib-specific) |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000690 (cancelled) | Nexavar | Not specified | Hepatocellular carcinoma; advanced renal cell carcinoma after failure of interferon-alpha or interleukin-2 based therapy...; differentiated thyroid carcinoma refractory to radioactive iodine... |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions. Haematological parameters and liver and renal function are generally monitored for kinase inhibitors |
| Handling Protection | Please refer to the SmPC warnings and precautions |

---

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: hypertension, liver failure, thrombocytopenia, neutropenia, agranulocytosis, blood coagulation disease, acute coronary syndrome, coronary artery disease, myocardial infarction, myocardial ischemia, anaemia, hypophosphataemia, pancreatitis, and anxiety/neurotic/dysthymic disorders. These come from a computational knowledge graph and need confirmation against the official product information.
- **Drug Interactions**: 100 interactions were identified. Of the 20 shown, one is **Major**: dolasetron. Most others are Moderate, for example famotidine, loperamide, dexamethasone, clarithromycin, levofloxacin, palonosetron, naltrexone, and several laxatives and bowel-preparation agents. Minor interactions include dapagliflozin, naloxegol, and metronidazole.

Label-based warnings and contraindications are not available in the data compiled for this report. Please refer to the SmPC for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only clinical evidence comes from mixed-histology soft tissue sarcoma studies, with no liposarcoma-specific data. Label-based safety information is missing, and the single EU authorization is cancelled. The TxGNN score of 99.82% supports further research but does not justify advancing the candidate.

**To proceed, the following is needed:**
- Liposarcoma-specific subgroup data from the soft tissue sarcoma trials (NCT00217620 and SWOG S0505)
- Official mechanism of action data
- Label-based warnings and contraindications from the SmPC
- A review of the cancelled EU authorization status and its reasons
- Comparison with established liposarcoma treatments such as trabectedin and doxorubicin-based regimens
- A safety monitoring plan covering cardiovascular, haematological, and hepatic risks, and a drug interaction review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

