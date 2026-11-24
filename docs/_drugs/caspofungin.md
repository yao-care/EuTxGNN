---
layout: default
title: Caspofungin
parent: AI Predictions (L5)
nav_order: 133
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Caspofungin: predicted new indication Gastrin secretion abnormality (evidence level L5). Approved use: Invasive candidiasis"
monitor_inn: "Caspofungin"
predicted_indications: ["gastrin secretion abnormality"]
---

# Caspofungin
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

## Caspofungin: From Invasive Fungal Infections to Gastrin Secretion Abnormality
{: .text-alpha }

## One-Sentence Summary

Caspofungin is an intravenous antifungal originally used to treat invasive candidiasis, invasive aspergillosis that has not responded to other treatments, and suspected fungal infections in febrile, neutropaenic patients.
The TxGNN model predicts it may be effective for **gastrin secretion abnormality**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Invasive candidiasis; invasive aspergillosis refractory to or intolerant of other antifungals; empirical therapy for presumed fungal infections in febrile, neutropaenic patients (adults and children) |
| Predicted New Indication | Gastrin secretion abnormality |
| TxGNN Prediction Score | 0.9944 |
| Evidence Level | L5 (model prediction only) |
| EU Market Status | Marketed (valid licences: 1 of 2) |
| Number of Authorizations | 2 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for caspofungin: "Caspofungin is an echinocandin antifungal drug. […] Caspofungin, an echinocandin, inhibits the synthesis of beta (1,3)-D-glucan, an essential component of the cell wall of susceptible Aspergillus species and Candida species. Beta (1,3)-D-glucan is not present in mammalian cells." ([DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c), label version 2024-10-11; accessed 2026-11-19.) Caspofungin belongs to the echinocandin class, which inhibits fungal beta-(1,3)-D-glucan synthase, an enzyme needed to build the fungal cell wall. Its efficacy in invasive fungal infections is established.

This mechanism does not obviously extend to gastrin secretion abnormality. Mammalian cells have no beta-glucan synthase, so the drug has no known target in the pathways that regulate gastrin release. The high TxGNN score (0.9944) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Nothing in the data compiled for this report shows a biological, clinical, or literature link between caspofungin and gastrin regulation, so the prediction is best treated as a hypothesis-generating signal only.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000379 | Cancidas | caspofungin (as acetate) | Valid |
| EMEA/H/C/004134 | Caspofungin Accord | caspofungin acetate | Expired |

<!-- licenses:end -->

## Safety Considerations

- **Contraindications flagged by the knowledge graph** (these come from drug-disease links in the TxGNN knowledge graph, not from the product label): liver disease, gallbladder disease, and potassium deficiency disease.
- **Drug Interactions**: 81 interacting drugs are recorded. Those with a graded severity are:
  - **Major**: dexamethasone
  - **Moderate**: naltrexone
  - Many other recorded interactions have no severity grade. Examples are pantoprazole, omeprazole, lansoprazole, simvastatin, amphotericin B, vancomycin, prednisone, hydrocortisone, and potassium chloride.

Label warnings and contraindications were not available for this report. Please refer to the SmPC for the full safety profile.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone. There are no registered trials and no publications, and no plausible mechanistic link to gastrin regulation.

<!-- review:begin eu-lic-20261106-caspofungin-2 -->

> **Review correction (2026-11-24)**: Originally stated: "There are no registered trials and no publications, and no plausible mechanistic link to gastrin regulation. The EU authorization for the product is also cancelled." Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-11-06). The current number of EU marketing authorisations for this drug is shown in the Quick Overview and in the table under EU Market Information. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-caspofungin-2 -->

**To proceed, the following is needed:**
- A mechanistic hypothesis linking caspofungin to gastrin secretion, supported by preclinical data
- Label-based safety data (warnings and contraindications) and mechanism of action data

<!-- review:begin eu-lic-20261031-caspofungin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Label-based safety data (warnings and contraindications) and mechanism of action data / Verification of the current regulatory and supply status in the EU, since the only authorization is cancelled" Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-10-31). The current number of EU marketing authorisations for this drug is shown in the Quick Overview and in the table under EU Market Information. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261031-caspofungin-1 -->

**Note on other predictions:** This report covers the top-ranked prediction only. Other predictions in the same list have more support. Neonatal candidiasis in particular has two Phase 2 trials, a meta-analysis, and an extension-of-indication rationale that rated it "Proceed with Guardrails". If the goal is to find a repurposing opportunity for caspofungin, that candidate is a better one to evaluate.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "Verification of the current regulatory and supply status in the EU, since the only authorization is cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-24 | Removed: "The EU authorization for the product is also cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cancidas (caspofungin acetate) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3bad23a6-09a6-4194-9182-093ed61bc71c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

