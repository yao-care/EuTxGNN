---
layout: default
title: Granisetron
parent: AI Predictions (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
monitor_inn: "Granisetron"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
description: "Granisetron: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Prevention of nausea and vomiting in patients receiving moderately or…"
---

# Granisetron
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

## Granisetron: Manic bipolar affective disorder
{: .text-alpha }

## One-Sentence Summary

Granisetron is a 5-HT3 receptor antagonist, originally used to prevent nausea and vomiting in patients receiving moderately or highly emetogenic chemotherapy.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but **no clinical trials and no publications** currently support this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of nausea and vomiting in patients receiving moderately or highly emetogenic chemotherapy, with or without cisplatin, for up to five consecutive days. Sancuso may be used in patients receiving their first chemotherapy regimen or in patients who have previously received chemotherapy. |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for granisetron: "Granisetron is a selective 5-hydroxytryptamine 3 (5-HT 3 ) receptor antagonist with little or no affinity for other serotonin receptors, including 5-HT 1, 5-HT 1A, 5-HT 1B/C, 5-HT 2; for alpha 1-, alpha 2-, or beta-adrenoreceptors; for dopamine-D 2; or for histamine-H 1; benzodiazepine; picrotoxin or opioid receptors. Serotonin receptors of the 5-HT 3 type are located peripherally on vagal nerve terminals and centrally in the chemoreceptor trigger zone of the area postrema." ([DailyMed: Sustol (granisetron) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7c7ffdd-8270-4030-bc1e-a1cb28a6de56), label version 2026-04-30; accessed 2026-11-19.) Granisetron is known to be a selective 5-HT3 receptor antagonist, and its efficacy in chemotherapy-induced nausea and vomiting is established.

A theoretical link to mania exists through serotonergic and dopaminergic modulation in limbic circuits. Other 5-HT3 antagonists, such as ondansetron, have been explored in neuropsychiatric conditions. However, this link is speculative. No granisetron-specific trials or literature were found, and the TxGNN score reflects a computational prediction rather than clinical evidence.

Other top-ranked predictions include Tourette syndrome (0.9952), trichotillomania (0.9923), and several urticaria, conjunctivitis and other conditions. Some of these, such as Tourette syndrome and trichotillomania, have a speculative class-level rationale. Others, such as nephrogenic syndrome of inappropriate antidiuresis, conjunctivitis and bronchitis, appear to be network artifacts without a plausible mechanism. None has clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/002296 | Sancuso | granisetron | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Knowledge-graph contraindication signals** (from a computational knowledge graph, not label text): long QT syndrome, familial long QT syndrome, potassium deficiency disease (hypokalaemia), sudden cardiac arrest, heart conduction disease.
- **Drug Interactions**: 100 interactions were identified; the first 20 retrieved are summarized here.
  - **Major**: fentanyl, dextromethorphan, tramadol, alfentanil, almotriptan, sumatriptan, amiodarone, amisulpride, amitriptyline, anagrelide. These include serotonergic agents (risk of serotonin syndrome) and QT-prolonging agents.
  - **Moderate**: abametapir (topical), abiraterone, dihydrocodeine, codeine, famotidine, formoterol, adenosine, salbutamol, alfuzosin, propofol.

Please refer to the SmPC for label-based warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5). The cardiac contraindication signals and the many QT-related and serotonergic interactions also matter in a psychiatric population that often takes interacting drugs.

<!-- review:begin eu-lic-20261031-granisetron-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The prediction is supported only by the TxGNN model score (L5). There are no registered trials or publications, the mechanistic link is speculative, and the only EU authorization is cancelled." Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-10-31). The EMA data list 1 EU marketing authorisation for this drug, 1 current; the Quick Overview and the table under EU Market Information show the current figures. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261031-granisetron-1 -->

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank)
- Label warnings and contraindications from the EMA package insert, to complete safety screening
- Preclinical or early clinical studies of granisetron (or 5-HT3 antagonists as a class) in mania or bipolar disorder
- A cardiac safety assessment (QT interval, electrolytes) and an interaction review for typical psychiatric co-medications
- Comparison of the higher-plausibility candidates (Tourette syndrome, trichotillomania) before committing resources

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "There are no registered trials or publications, the mechanistic link is speculative, and the only EU authorization is cancelled" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Sustol (granisetron) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7c7ffdd-8270-4030-bc1e-a1cb28a6de56) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

