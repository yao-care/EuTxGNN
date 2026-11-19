---
layout: default
title: Dantrolene
parent: AI Predictions (L5)
nav_order: 168
evidence_level: L5
indication_count: 7
monitor_inn: "dantrolene"
predicted_indications: ["moderate multiminicore disease with hand involvement", "King-Denborough syndrome", "congenital multicore myopathy with external ophthalmoplegia", "central core myopathy", "hypokalemic periodic paralysis", "thyrotoxic periodic paralysis", "myopathy, centronuclear"]
last_modified_at: 2026-11-20
description: "Dantrolene: predicted new indication moderate multiminicore disease with hand involvement (evidence level L5). Approved use: In combination with adequate support measures…"
---

# Dantrolene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Dantrolene: ryanodine receptor (RyR1) antagonist → moderate multiminicore disease with hand involvement
{: .text-alpha }

## One-Sentence Summary

Dantrolene is a muscle relaxant that acts on the skeletal muscle ryanodine receptor (RyR1) and is marketed in the European Union.
The TxGNN model predicts it may be relevant to **moderate multiminicore disease with hand involvement**, with a score of **0.9990**.
The data compiled for this report contain **no clinical trials and no publications** for this disease, so the prediction rests on the model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | In combination with adequate support measures, Agilus is indicated for the treatment of malignant hyperthermia in adults and children of all ages. |
| Predicted New Indication | moderate multiminicore disease with hand involvement |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dantrolene: "In isolated nerve-muscle preparation, dantrolene has been shown to produce relaxation by affecting the contractile response of the muscle at a site beyond the myoneural junction. In skeletal muscle, dantrolene dissociates the excitation-contraction coupling, probably by interfering with the release of Ca ++ from the sarcoplasmic reticulum." ([DailyMed: Ryanodex Dantrolene Sodium (dantrolene sodium) prescribing information, Eagle Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f7b3ac0-604d-4c78-b545-5e0f8ea3d698), label version 2024-10-30; accessed 2026-11-19.) Dantrolene is nonetheless known to antagonise RyR1, the calcium release channel of skeletal muscle.

Multiminicore disease can be caused by mutations in *RYR1*, the gene encoding this channel. That gives a plausible but unverified link between dantrolene's mechanism and the disease. The high TxGNN score is a computational prediction only. No study in the supplied data tests dantrolene in this condition, and no evidence shows that blocking RyR1 would change the course of the myopathy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

Dantrolene currently has a marketed status in the European Union, based on the local regulatory records. The authorization details are provided separately by the site program.

## Safety Considerations

- **Drug Interactions**: 72 interaction records were found. The main ones are:
  - **Major**: morphine, liposomal morphine
  - **Moderate**: dronabinol, metoclopramide, nabilone, naltrexone, opium, sibutramine, ethanol, promethazine

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, and a link through RYR1 is biologically plausible. However, there are no clinical trials, no literature and no mechanism data for this disease, which places it at evidence level L5. It is a hypothesis only.

**To proceed, the following is needed:**
- Literature and preclinical evidence on RyR1 modulation in multiminicore disease, particularly the form with hand involvement
- Detailed mechanism-of-action data for dantrolene
- Review of the SmPC warnings and contraindications, which were not available for this report
- A safety assessment for patients with neuromuscular disease

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Ryanodex Dantrolene Sodium (dantrolene sodium) prescribing information, Eagle Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f7b3ac0-604d-4c78-b545-5e0f8ea3d698) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

