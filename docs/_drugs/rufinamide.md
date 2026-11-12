---
layout: default
title: Rufinamide
parent: AI Predictions (L5)
nav_order: 541
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "Rufinamide"
predicted_indications: ["perioral myoclonia with absences"]
description: "Rufinamide: predicted new indication Perioral myoclonia with absences (evidence level L5). Approved use: Inovelon is indicated as adjunctive therapy in the treatment of seizu…"
---

# Rufinamide
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

## Rufinamide: Perioral myoclonia with absences
{: .text-alpha }

## One-Sentence Summary

Rufinamide is an antiseizure medicine, originally authorised in the EU as add-on therapy for seizures associated with Lennox-Gastaut syndrome in patients aged 4 years and older.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inovelon is indicated as adjunctive therapy in the treatment of seizures associated with Lennox Gastaut syndrome in patients 4 years of age and older. |
| Predicted New Indication | Perioral myoclonia with absences |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Rufinamide is generally described as a sodium channel modulator that prolongs the inactive state of voltage-gated sodium channels. This stabilises neuronal membranes and limits repetitive firing. It is structurally unrelated to other antiseizure drugs and is established for seizures in Lennox-Gastaut syndrome.

Both Lennox-Gastaut syndrome and FIRES are severe, drug-resistant epilepsies that begin in childhood. This gives the prediction some indirect plausibility for seizure control. FIRES, however, is thought to be driven largely by neuroinflammation, and a sodium channel blocker would not address that component. Any benefit would probably be symptomatic only.

No trials or publications specific to FIRES were found.

For context, other predictions in the same analysis have more indirect support. The broader category "childhood onset epileptic encephalopathy" has substantial literature, but it is largely Lennox-Gastaut syndrome (the approved use), so it is essentially on-label. Several other epilepsy-related predictions have no supporting data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000660 | Inovelon | rufinamide | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links in the TxGNN knowledge graph, not from label text): liver failure, liver disease, gallbladder disease, leukopenia, anxiety disorder, neurotic disorder, dysthymic disorder.
- **Drug Interactions**: 100 interactions were identified. The ones reviewed are all rated **Moderate**. Examples include:
  - Corticosteroids: hydrocortisone, prednisone, triamcinolone, betamethasone.
  - Vitamin D analogues: cholecalciferol, calcifediol, calcitriol.
  - CNS-active or opioid-type drugs: morphine, bupropion, difenoxin, diphenoxylate, dronabinol, nabilone.
  - Others: pioglitazone, metoclopramide, ondansetron, eliglustat, nitisinone, naloxegol, rolapitant.

Please refer to the SmPC for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5), with no trials or literature for FIRES. The mechanism is only partly aligned, because it addresses seizures but not neuroinflammation.

<!-- review:begin eu-lic-20261031-rufinamide-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The mechanism is only partly aligned, because it addresses seizures but not neuroinflammation. The only EU authorisation is also cancelled, which may limit practical availability." Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-10-31). The EMA data list 1 EU marketing authorisation for this drug, 1 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261031-rufinamide-1 -->

**To proceed, the following is needed:**
- Clinical or observational data on rufinamide in FIRES, such as case series or registry data.
- Mechanism of action data, to assess fit with the inflammatory drivers of FIRES.
- The SmPC warnings and contraindications, as well as the current availability of rufinamide in the EU.
- An assessment of dosage forms and routes suitable for the target population, since route compatibility has not been evaluated.
- A review of the more evidence-supported alternatives from the same analysis, as a possible redirect.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The only EU authorisation is also cancelled, which may limit practical availability" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

