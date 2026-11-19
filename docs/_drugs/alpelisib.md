---
layout: default
title: Alpelisib
parent: AI Predictions (L5)
nav_order: 40
evidence_level: L5
indication_count: 1
monitor_inn: "Alpelisib"
predicted_indications: ["pulmonary hypertension"]
last_modified_at: 2026-11-20
description: "Alpelisib: predicted new indication pulmonary hypertension (evidence level L5). Approved use: Piqray is indicated in combination with fulvestrant for the treatment…"
---

# Alpelisib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Alpelisib: PI3Kα inhibitor → pulmonary hypertension (pulmonary hypertension)
{: .text-alpha }

## One-Sentence Summary

Alpelisib is a drug authorized in the European Union for a breast cancer indication. The TxGNN model predicts it may be relevant to **pulmonary hypertension**, but the evidence is very thin: **0 clinical trials** and **1 publication** were found, and that publication is a case report of a lung adverse event rather than evidence of benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Piqray is indicated in combination with fulvestrant for the treatment of postmenopausal women, and men, with hormone receptor (HR)-positive, human epidermal growth factor receptor 2 (HER2)-negative, locally advanced or metastatic breast cancer with a PIK3CA mutation after disease progression followi |
| Predicted New Indication | pulmonary hypertension |
| TxGNN Prediction Score | 0.9903 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 2 of 2) |
| Number of Authorizations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for alpelisib: "Alpelisib is an inhibitor of phosphatidylinositol-3-kinase (PI3K) with inhibitory activity predominantly against PI3Kα. Gain-of-function mutations in the gene encoding the catalytic α-subunit of PI3K (PIK3CA) lead to activation of PI3Kα and Akt-signaling, cellular transformation and the generation of tumors in in vitro and in vivo models." ([DailyMed: Piqray (alpelisib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b20b4e18-7a4b-4500-a08f-06c6dab0ee5b), label version 2026-10-28; accessed 2026-11-19.) Alpelisib is known as an inhibitor of the PI3K pathway (specifically the alpha isoform), which is the basis of its use in oncology.

Mechanistically, PI3K/AKT/mTOR signaling has been implicated in pulmonary vascular remodeling, so a theoretical link to pulmonary hypertension exists. However, this is a hypothesis only. No clinical study in the compiled data shows a benefit of alpelisib in pulmonary hypertension.

The only linked publication reports alpelisib-induced interstitial lung disease, which is a safety signal for the lungs rather than a therapeutic one. The high model score (0.9903) should therefore be read as a computational prediction, not as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case report | Journal of Oncology Pharmacy Practice | Alpelisib-induced interstitial lung disease in a patient with advanced breast cancer. This is an adverse event, not evidence of therapeutic benefit. |

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/004804 | Piqray | alpelisib | Valid |
| EMEA/H/C/006539 | Vijoice | alpelisib | Valid |

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3Kα inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction database. The entries listed are all rated Moderate. They are mainly glucose-lowering drugs, including acarbose, albiglutide, alogliptin, metformin, pioglitazone, acetohexamide, canagliflozin, chlorpropamide, dapagliflozin, empagliflozin, ertugliflozin, exenatide, glimepiride and glipizide. Others listed include alosetron, bupropion, dexamethasone, dronabinol, dulaglutide and fidaxomicin.
- **Lung safety signal**: The only linked publication describes interstitial lung disease associated with alpelisib, which calls for caution in any lung-related use.

For other safety information, please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but no clinical trial studies alpelisib in pulmonary hypertension. The only publication reports a lung adverse event, so the evidence level is L5 (model prediction only).

**To proceed, the following is needed:**
- Preclinical or mechanistic studies of PI3Kα inhibition in pulmonary vascular disease
- Mechanism of action data for alpelisib
- A review of the pulmonary toxicity signal (interstitial lung disease) against any potential benefit
- Warnings and contraindications from the SmPC
- A safety plan for the glucose-related interactions

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Piqray (alpelisib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b20b4e18-7a4b-4500-a08f-06c6dab0ee5b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

