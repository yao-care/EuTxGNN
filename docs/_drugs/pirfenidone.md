---
layout: default
title: Pirfenidone
parent: AI Predictions (L5)
nav_order: 488
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pirfenidone: predicted new indication Extracutaneous mastocytoma (evidence level L5). Approved use: Idiopathic pulmonary fibrosis (IPF) in adults (mild to moderate IPF f…"
monitor_inn: "Pirfenidone"
predicted_indications: ["extracutaneous mastocytoma", "dermatofibrosarcoma protuberans", "aggressive systemic mastocytosis", "heart fibrosarcoma", "conventional fibrosarcoma", "autosomal recessive familial Mediterranean fever", "kidney fibrosarcoma", "hepatic infarction", "fibroblastic neoplasm", "low grade fibromyxoid sarcoma"]
---

# Pirfenidone
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

# Pirfenidone: From Idiopathic Pulmonary Fibrosis to Extracutaneous Mastocytoma

## One-Sentence Summary

Pirfenidone is an antifibrotic medicine originally authorised in the EU for idiopathic pulmonary fibrosis (IPF).
The TxGNN model predicts it may be effective for **extracutaneous mastocytoma**, but there are **no clinical trials** and **no publications** supporting this specific prediction.
The only indication in the top 10 with any literature is fibroblastic neoplasm (**6 publications**, mostly preclinical or case reports), so the top prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic pulmonary fibrosis (IPF) in adults (mild to moderate IPF for some products) |
| Predicted New Indication | Extracutaneous mastocytoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorisations) |
| Number of Authorizations | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pirfenidone is an antifibrotic, anti-inflammatory agent. Its efficacy in IPF has been established, and it is reported to modulate TGF-β and TNF-α signalling.

The link to extracutaneous mastocytoma is speculative. Mast cell disease can involve fibrosis and inflammation, so a loose connection to antifibrotic activity is conceivable. However, no data compiled for this report support a direct mechanism, and the very high model score has not been confirmed by any study.

For context, the other top-ranked predictions (for example dermatofibrosarcoma protuberans, other fibrosarcomas, aggressive systemic mastocytosis and familial Mediterranean fever) are also prediction-only. For aggressive systemic mastocytosis, the main driver is KIT mutation, which pirfenidone does not target. Fibroblastic neoplasm is the only top-10 candidate with any related literature, and that literature is indirect (see below).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for extracutaneous mastocytoma. For reference, the table below lists the literature found for the rank-9 prediction, fibroblastic neoplasm, which is the closest indirect evidence in the top 10.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | Pilot study | Am J Gastroenterol | Pilot project testing pirfenidone for desmoid tumours in familial adenomatous polyposis; results cannot be confirmed from the data available |
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | In vitro | BMC Musculoskelet Disord | Pirfenidone inhibits TGF-β1-driven activity in Dupuytren's disease-derived fibroblasts |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | In vitro | BMC Musculoskelet Disord | Effects of pirfenidone on TGF-β1-stimulated non-SMAD signalling in Dupuytren's fibroblasts |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | Preclinical/Review | Pharm Dev Technol | Pirfenidone proposed as a locally injected antifibrotic for Dupuytren's disease |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | Case report | Perm J | Undifferentiated pleomorphic sarcoma reported after pirfenidone use (safety signal) |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | Case report | Rheumatology (Oxford) | Multiple eruptive dermatofibromas aggravated by mycophenolate mofetil and pirfenidone in a patient with systemic sclerosis (safety signal) |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002154 | Esbriet | Not specified | Treatment of idiopathic pulmonary fibrosis in adults (cancelled) |
| EMEA/H/C/005873 | Pirfenidone axunio (previously Pirfenidone AET) | Not specified | Treatment of mild to moderate idiopathic pulmonary fibrosis (IPF) in adults (cancelled) |
| EMEA/H/C/005862 | Pirfenidone Viatris | Not specified | Treatment of mild to moderate idiopathic pulmonary fibrosis (IPF) in adults (cancelled) |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in total. The 20 listed in the data compiled for this report are all rated Moderate, including bupropion, omeprazole, esomeprazole, lansoprazole, cimetidine, eliglustat, obeticholic acid, oxandrolone, naltrexone, miconazole, nitisinone, glycerol phenylbutyrate, rolapitant, deferasirox, ticlopidine, lumefantrine, disulfiram, primaquine, thiabendazole and ivacaftor.
- **Literature safety signals**: Two case reports describe tumour or tumour-like growth (undifferentiated pleomorphic sarcoma; eruptive dermatofibromas) after or during pirfenidone use. These are low-level evidence but deserve attention for any oncology-related repurposing.

For warnings and contraindications, please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The extracutaneous mastocytoma prediction has a very high model score but no trials, no literature and no defined mechanism, so it is Level L5. In addition, all three EU authorisations for pirfenidone are cancelled, and the case reports suggesting possible tumour-promoting signals call for caution.

**To proceed, the following is needed:**
- Mechanism of action data for pirfenidone (e.g., from DrugBank) and a mechanistic analysis linking it to mast cell disease
- Warnings and contraindications from the SmPC or package insert
- A targeted literature and trial search for extracutaneous mastocytoma and mast cell disorders
- Preclinical studies in mast cell models before any clinical consideration
- Clarification of current EU regulatory status, given that all authorisations are cancelled
- Review of the sarcoma and dermatofibroma case reports as a safety question for any oncology-related use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

