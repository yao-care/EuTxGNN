---
layout: default
title: Granisetron
parent: AI Predictions (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Granisetron: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Prevention of nausea and vomiting in patients receiving moderately or…"
monitor_inn: "Granisetron"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
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

## Granisetron: From Chemotherapy-Induced Nausea and Vomiting to Manic Bipolar Affective Disorder
{: .text-alpha }

## One-Sentence Summary

Granisetron is a 5-HT3 receptor antagonist, originally used to prevent nausea and vomiting in patients receiving moderately or highly emetogenic chemotherapy.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but **no clinical trials and no publications** currently support this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of nausea and vomiting in patients receiving moderately or highly emetogenic chemotherapy, with or without cisplatin, for up to five consecutive days |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Granisetron is known to be a selective 5-HT3 receptor antagonist, and its efficacy in chemotherapy-induced nausea and vomiting is established.

A theoretical link to mania exists through serotonergic and dopaminergic modulation in limbic circuits. Other 5-HT3 antagonists, such as ondansetron, have been explored in neuropsychiatric conditions. However, this link is speculative. No granisetron-specific trials or literature were found, and the TxGNN score reflects a computational prediction rather than clinical evidence.

Other top-ranked predictions include Tourette syndrome (99.52%), trichotillomania (99.23%), and several urticaria, conjunctivitis and other conditions. Some of these, such as Tourette syndrome and trichotillomania, have a speculative class-level rationale. Others, such as nephrogenic syndrome of inappropriate antidiuresis, conjunctivitis and bronchitis, appear to be network artifacts without a plausible mechanism. None has clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002296 (cancelled) | Sancuso | Not specified | Prevention of nausea and vomiting in patients receiving moderately or highly emetogenic chemotherapy, with or without cisplatin, for up to five consecutive days. Sancuso may be used in patients rece... |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from a computational knowledge graph, not label text): long QT syndrome, familial long QT syndrome, potassium deficiency disease (hypokalaemia), sudden cardiac arrest, heart conduction disease.
- **Drug Interactions**: 100 interactions were identified; the first 20 retrieved are summarized here.
  - **Major**: fentanyl, dextromethorphan, tramadol, alfentanil, almotriptan, sumatriptan, amiodarone, amisulpride, amitriptyline, anagrelide. These include serotonergic agents (risk of serotonin syndrome) and QT-prolonging agents.
  - **Moderate**: abametapir (topical), abiraterone, dihydrocodeine, codeine, famotidine, formoterol, adenosine, salbutamol, alfuzosin, propofol.

Please refer to the SmPC for label-based warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (L5). There are no registered trials or publications, the mechanistic link is speculative, and the only EU authorization is cancelled. The cardiac contraindication signals and the many QT-related and serotonergic interactions also matter in a psychiatric population that often takes interacting drugs.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank)
- Label warnings and contraindications from the EMA package insert, to complete safety screening
- Preclinical or early clinical studies of granisetron (or 5-HT3 antagonists as a class) in mania or bipolar disorder
- A cardiac safety assessment (QT interval, electrolytes) and an interaction review for typical psychiatric co-medications
- Comparison of the higher-plausibility candidates (Tourette syndrome, trichotillomania) before committing resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

