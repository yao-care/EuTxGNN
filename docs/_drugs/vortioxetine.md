---
layout: default
title: Vortioxetine
parent: AI Predictions (L5)
nav_order: 678
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "Vortioxetine"
predicted_indications: ["neurotic disorder", "benign paroxysmal torticollis of infancy"]
description: "Vortioxetine: predicted new indication Neurotic disorder (evidence level L5). Approved use: Treatment of major depressive episodes in adults"
---

# Vortioxetine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Vortioxetine: Neurotic disorder
{: .text-alpha }

## One-Sentence Summary

Vortioxetine is an antidepressant originally used to treat major depressive episodes in adults.
The TxGNN model predicts it may be effective for **neurotic disorder**, but **no clinical trials** and only **1 publication** (a narrative article that does not study vortioxetine) currently support this specific prediction.
The prediction mostly reflects overlap with depression and anxiety categories rather than a distinct new indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of major depressive episodes in adults. |
| Predicted New Indication | Neurotic disorder |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Published literature describes vortioxetine as a multimodal serotonergic antidepressant: it inhibits the serotonin transporter (SERT), acts as a 5-HT1A agonist and 5-HT1B partial agonist, and antagonises 5-HT3, 5-HT7 and 5-HT1D receptors.

"Neurotic disorder" is an older, broad diagnostic category that overlaps with today's depressive and anxiety disorders. Because vortioxetine is already approved for depression, the model's high score probably reflects this semantic overlap rather than a distinct, testable indication. The only retrieved paper is a case report and narrative discussion of neurotic depression treated with antidepressants and psychotherapy. It contains no vortioxetine-specific data.

**Other predictions for context** (higher-ranked alternatives that are more actionable than the top-ranked one):
- Evidence concerns the already-approved parent condition. Subgroup analysis of existing trial data would be a reasonable next step.
- This supports a hypothesis only.
- Rare genetic and endocrine predictions (benign paroxysmal torticollis of infancy, Ohdo syndrome and variants, Keppen-Lubinsky syndrome, congenital isolated ACTH deficiency) have no plausible mechanistic link and no evidence, and appear to be TxGNN model (deep learning) artifacts.

## Clinical Trial Evidence

Currently no related clinical trials are registered for neurotic disorder.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Review / case report | Zhurnal nevrologii i psikhiatrii imeni S.S. Korsakova | Case report on neurotic depression, favouring an integrated approach combining antidepressants and cognitive behavioural therapy. Not specific to vortioxetine. |

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002717 | Brintellix | Not specified | Treatment of major depressive episodes in adults. (Status: valid) |

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 interacting drugs in total. The ones listed in the data compiled for this report include:
  - **Major**: bupropion, lorcaserin, diethylpropion, dolasetron, palonosetron, phentermine.
  - **Moderate**: morphine, acetylsalicylic acid, dexamethasone, and several antidiabetic agents (chlorpropamide, glimepiride, and insulins such as aspart, degludec, detemir, glargine and glulisine). Others include picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes, and eliglustat.
- Published reviews also describe class-related adverse effects of second-generation antidepressants, such as gastrointestinal effects, hyperhidrosis and sexual dysfunction.

Please refer to the SmPC for warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, neurotic disorder, is a historical umbrella term with no vortioxetine-specific trials or literature, so it is not a distinct, testable repurposing opportunity. Vortioxetine's EU authorization is also cancelled, which adds a regulatory hurdle.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank.
- Warnings and contraindications from the EMA product information, to allow safety screening.
- Re-mapping of "neurotic disorder" to current diagnoses (depressive, anxiety or dysthymic disorders), and prioritising better-supported candidates such as melancholia (post hoc subgroup analysis of existing MDD trials) and anxiety disorders (controlled trials).
- Clarification of the cancelled EU authorization status and its reasons.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

