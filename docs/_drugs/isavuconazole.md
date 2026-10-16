---
layout: default
title: Isavuconazole
parent: AI Predictions (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Isavuconazole: predicted new indication Migraine disorder (evidence level L5). Approved use: Treatment of invasive aspergillosis and mucormycosis in patients for…"
monitor_inn: "Isavuconazole"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "pulmonary hypertension", "kyphoscoliotic heart disease", "rheumatoid arthritis", "atrophoderma vermiculata", "nephrogenic syndrome of inappropriate antidiuresis", "Prinzmetal angina", "ulerythema ophryogenesis"]
---

# Isavuconazole
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

# Isavuconazole: From Invasive Aspergillosis and Mucormycosis to Migraine Disorder

## One-Sentence Summary

Isavuconazole is an azole antifungal originally used to treat invasive aspergillosis and mucormycosis (when amphotericin B is inappropriate).
The TxGNN model predicts it may be effective for **migraine disorder**, but **no clinical trials and no supporting publications** currently back this prediction.
The prediction rests on graph-based modelling alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of invasive aspergillosis and mucormycosis in patients for whom amphotericin B is inappropriate (patients from 1 year of age for the infusion; from 6 years of age for the capsules) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 98.99% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization in the data compiled) |
| Number of Authorizations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Isavuconazole is an azole antifungal that inhibits fungal CYP51 (lanosterol 14-alpha-demethylase), which disrupts fungal cell membrane synthesis. Its efficacy in invasive aspergillosis and mucormycosis is established.

No plausible link to migraine has been identified. Migraine involves CGRP signalling, serotonergic pathways and cortical spreading depression, and none of these is connected to the antifungal mechanism of an azole. The high TxGNN score (0.990) reflects graph proximity only and should not be read as biological support.

The other top predictions (migraine with brainstem aura, migraine susceptibility, pulmonary hypertension, kyphoscoliotic heart disease, rheumatoid arthritis, atrophoderma vermiculata, nephrogenic syndrome of inappropriate antidiuresis, Prinzmetal angina, ulerythema ophryogenesis) are also prediction-only. Several appear to be graph-neighbour effects, and one (migraine susceptibility) is a genetic susceptibility entity rather than a treatable condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (migraine disorder), currently no related literature available.

For reference, the only publication retrieved across the top ten predictions concerns rheumatoid arthritis, rank 6:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37597857](https://pubmed.ncbi.nlm.nih.gov/37597857/) | 2023 | Case report | BMJ Case Reports | Disseminated histoplasmosis in an immunosuppressed patient (methotrexate and infliximab for rheumatoid arthritis) successfully treated with isavuconazole. This is antifungal use; it does not show that isavuconazole treats rheumatoid arthritis. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002734 (cancelled) | Cresemba | Powder for concentrate for solution for infusion; hard capsules | Invasive aspergillosis and mucormycosis in patients for whom amphotericin B is inappropriate... |

## Safety Considerations

Please refer to the SmPC for safety information.

Two points from the compiled data are worth noting for any repurposing discussion. Azoles inhibit CYP3A4, so drug interactions are possible with co-administered therapies, such as pulmonary arterial hypertension drugs. Isavuconazole also shortens the QT interval, which matters for cardiovascular indications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based score, with no clinical trials, no relevant literature and no plausible mechanistic link to migraine. The sole retrieved publication is an antifungal case report that does not support any new indication.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank, and a mechanistic hypothesis connecting isavuconazole to migraine pathophysiology
- Preclinical or observational evidence of any effect on migraine
- Warnings and contraindications from the SmPC, so that safety screening can be carried out
- Clarification of the current EU regulatory status, since the only authorization in the data is recorded as cancelled
- Assessment of route compatibility and of drug interaction and QT-related risks in a migraine population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

