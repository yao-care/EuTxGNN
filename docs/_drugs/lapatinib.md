---
layout: default
title: Lapatinib
parent: AI Predictions (L5)
nav_order: 351
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Lapatinib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L5). Approved use: Breast cancer with HER2 (ErbB2) overexpression…"
monitor_inn: "Lapatinib"
predicted_indications: ["dermatofibrosarcoma protuberans", "fibroblastic neoplasm", "conventional fibrosarcoma", "kidney fibrosarcoma", "cysticercosis", "heart fibrosarcoma", "low grade fibromyxoid sarcoma", "Plasmodium falciparum malaria", "coenurosis", "lymphangiomyoma"]
---

# Lapatinib
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

## Lapatinib: From HER2-Positive Breast Cancer to Dermatofibrosarcoma Protuberans
{: .text-alpha }

## One-Sentence Summary

Lapatinib is an oral EGFR/HER2 tyrosine kinase inhibitor, originally used to treat HER2-overexpressing breast cancer.
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast cancer with HER2 (ErbB2) overexpression, used in combination with capecitabine, trastuzumab, or an aromatase inhibitor in advanced or metastatic disease |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lapatinib is a dual EGFR/HER2 tyrosine kinase inhibitor, its efficacy in HER2-positive breast cancer has been demonstrated, and it may mechanistically be applicable to other tumours driven by receptor tyrosine kinase signalling.

For DFSP, however, the mechanistic link is weak. DFSP is driven by the COL1A1-PDGFB fusion and PDGFR signalling, for which imatinib is the established therapy. Lapatinib has no established PDGFR activity. The high TxGNN score (99.30%) most likely reflects network similarity in the knowledge graph rather than a demonstrated biological rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

For context, among the other predictions the only one with a literature signal is **Plasmodium falciparum malaria** (TxGNN score 98.02%, evidence level L4). Preclinical reports show lapatinib inhibits haemozoin formation in malaria parasites ([PMID 32235391](https://pubmed.ncbi.nlm.nih.gov/32235391/), 2020), and lapatinib-derived 4-anilinoquinolines have antiparasitic activity ([PMID 29301082](https://pubmed.ncbi.nlm.nih.gov/29301082/), 2018). All of this evidence is in vitro or medicinal chemistry, with no clinical trials. The second-ranked prediction, fibroblastic neoplasm, has only an indirect preclinical study on stroma-mediated lapatinib resistance in breast cancer ([PMID 34239043](https://pubmed.ncbi.nlm.nih.gov/34239043/), 2021).

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000795 (cancelled) | Tyverb | Not specified | Tyverb is indicated for the treatment of patients with breast cancer, whose tumours overexpress HER2 (ErbB2): in combination with capecitabine for... |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Liver function, cardiac function (including QT interval), electrolytes (potassium), and respiratory symptoms, based on the knowledge-graph signals below |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text)**: long QT syndrome, familial long QT syndrome, torsades de pointes, liver failure, drug-induced liver injury, potassium deficiency disease, interstitial lung disease, heart failure.
- **Drug Interactions**: 100 interactions were identified. Major interactions include **loperamide** and **clarithromycin**. Moderate interactions include acid-suppressing drugs (famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, dexlansoprazole), corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), aprepitant, pioglitazone, saxagliptin, and several laxatives or bowel-preparation agents (bisacodyl, picosulfuric acid, polyethylene glycol).

Label-based warnings and contraindications were not available for this report. Please refer to the SmPC for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for dermatofibrosarcoma protuberans is supported only by the model score, with no trials or literature. Its mechanistic link is weak because imatinib already targets the PDGFR-driven biology of DFSP. The product's EU authorization is also cancelled, and the knowledge-graph safety signals (QT prolongation, hepatotoxicity) and the large DDI burden add further caution.

**To proceed, the following is needed:**
- Mechanism of action data, and preclinical testing of lapatinib in DFSP models (for example, PDGFR/COL1A1-PDGFB-driven cell lines)
- Label-based warnings and contraindications from the SmPC
- A comparison against imatinib as the established standard therapy
- Clarification of the regulatory and supply status, given the cancelled EU authorization
- Optionally, the malaria direction could be pursued as a separate research question, starting with in vivo preclinical work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

