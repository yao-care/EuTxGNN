---
layout: default
title: Nilotinib
parent: AI Predictions (L5)
nav_order: 429
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "Nilotinib"
predicted_indications: ["dermatofibrosarcoma protuberans"]
description: "Nilotinib: predicted new indication Dermatofibrosarcoma protuberans (evidence level L5). Approved use: Tasigna is indicated for the treatment of: adult and paediatric patie…"
---

# Nilotinib
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

## Nilotinib: Dermatofibrosarcoma protuberans
{: .text-alpha }

## One-Sentence Summary

Nilotinib is a tyrosine kinase inhibitor originally used to treat Philadelphia chromosome-positive chronic myelogenous leukaemia (CML).
The TxGNN model predicts it may be effective for **dermatofibrosarcoma protuberans (DFSP)**,
but so far there are **no registered clinical trials** and only **1 review article** (indirect evidence) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tasigna is indicated for the treatment of: adult and paediatric patients with newly diagnosed Philadelphia chromosome positive chronic myelogenous leukaemia (CML) in the chronic phase, paediatric patients with Philadelphia chromosome positive CML in chronic phase with resistance or intolerance to pr |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 2 of 2) |
| Number of Authorizations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for nilotinib: "Nilotinib is an inhibitor of the BCR-ABL kinase. Nilotinib binds to and stabilizes the inactive conformation of the kinase domain of ABL protein. In vitro, nilotinib inhibited BCR-ABL mediated proliferation of murine leukemic cell lines and human cell lines derived from patients with Ph+ CML." ([DailyMed: Cavhanza (nilotinib) prescribing information, Cycle Pharmaceuticals Ltd](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98b197ea-bca4-427e-8737-97f70a3262bc), label version 2026-07-20; accessed 2026-11-19.) Based on known information, nilotinib is a kinase inhibitor with activity against BCR-ABL, KIT and PDGFR. Its efficacy in Philadelphia chromosome-positive CML has been established, and mechanistically it may be applicable to DFSP.

DFSP is driven by the COL1A1-PDGFB fusion, which produces constitutive activation of PDGFRB signalling. Because nilotinib inhibits PDGFR, the mechanistic rationale is reasonable. Imatinib, a related kinase inhibitor, is an established treatment for DFSP, which further supports the plausibility of the prediction.

However, the supporting evidence is indirect. The only item provided is a review of small-molecule PDGFR inhibitors in neoplastic disorders. No nilotinib-specific study in DFSP is listed.

## Clinical Trial Evidence

Currently no related clinical trials registered for dermatofibrosarcoma protuberans.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews small-molecule PDGFR inhibitors in neoplastic disorders; indirect support for PDGFR-targeted therapy, with no nilotinib-specific DFSP data |

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000798 | Tasigna | nilotinib | Valid |
| EMEA/H/C/006315 | Nilotinib Accord | nilotinib | Valid |

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the SmPC warnings and precautions (the knowledge graph lists neutropenia, thrombocytopenia and anaemia as conditions of concern) |
| Emetogenicity Classification | Please refer to the SmPC warnings and precautions |
| Monitoring Items | Please refer to the SmPC warnings and precautions; based on the conditions of concern listed below, consider blood counts, liver function, glucose, electrolytes and ECG (QT interval) |
| Handling Protection | Please refer to the SmPC warnings and precautions |

## Safety Considerations

**Conditions of concern (from the TxGNN knowledge graph, not label text):**
- Cardiovascular: hypertension, long QT syndrome (including familial), torsades de pointes
- Hepatic and biliary: liver disease, gallbladder disease, hyperbilirubinaemia (including Gilbert syndrome), pancreatitis
- Haematological: thrombocytopenia, neutropenia, agranulocytosis, anaemia
- Metabolic and electrolyte: hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, hypophosphataemia

**Drug Interactions** (100 interactions recorded; main ones shown):
- **Major:** dexamethasone, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes)
- **Moderate:** acid-reducing agents (famotidine, ranitidine, cimetidine, omeprazole, rabeprazole), other corticosteroids (hydrocortisone, betamethasone, budesonide, triamcinolone), pioglitazone, saxagliptin, loperamide, bupropion, aprepitant, bisacodyl

Please also refer to the SmPC for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The PDGFR-driven mechanism of DFSP makes the prediction plausible, but there are no nilotinib trials in DFSP and only one indirect review. The evidence level is L4.

**To proceed, the following is needed:**
- Nilotinib-specific preclinical or clinical data in DFSP, including comparison with imatinib, the established treatment
- Detailed mechanism of action data (MOA)
- Official warnings and contraindications from the SmPC, to allow safety screening
- Clarification of the EU regulatory and market status
- A cardiac safety plan (QT monitoring), given the long QT and torsades de pointes signals and the major interaction with clarithromycin

<!-- review:begin eu-lic-20261106-nilotinib-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of the EU regulatory and market status, since both authorizations are cancelled" Removed: the number or status of EU marketing authorisations stated here did not match the EMA data (the EMA medicines data as of 2026-11-06). The EMA data list 2 EU marketing authorisations for this drug, 2 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-nilotinib-1 -->

---

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "since both authorizations are cancelled" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-19 | "Detailed mechanism of action data is not currently available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cavhanza (nilotinib) prescribing information, Cycle Pharmaceuticals Ltd](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98b197ea-bca4-427e-8737-97f70a3262bc) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

