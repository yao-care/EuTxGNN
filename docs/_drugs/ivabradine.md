---
layout: default
title: Ivabradine
parent: AI Predictions (L5)
nav_order: 338
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-20
description: "Ivabradine: predicted new indication hypertrichosis (disease) (evidence level L5). Approved use: Symptomatic treatment of chronic stable angina pectoris"
monitor_inn: "Ivabradine"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ivabradine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Ivabradine: From Chronic Stable Angina Pectoris and Chronic Heart Failure to hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Ivabradine is a heart-rate-lowering drug, originally used for chronic stable angina pectoris and chronic heart failure.
The TxGNN model predicts it may be effective for **hypertrichosis**, but **no clinical trials and no publications** currently support this prediction.
The high score most likely reflects a computational artifact rather than a biological rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Symptomatic treatment of chronic stable angina pectoris; chronic heart failure (NYHA II–IV, systolic dysfunction) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 0.9979 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 5 of 6) |
| Number of Authorizations | 6 (valid: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ivabradine: "Corlanor blocks the hyperpolarization-activated cyclic nucleotide-gated (HCN) channel responsible for the cardiac pacemaker I f current, which regulates heart rate. In clinical electrophysiology studies, the cardiac effects were most pronounced in the sinoatrial (SA) node, but prolongation of the AH interval has occurred as has PR interval prolongation." ([DailyMed: Corlanor (ivabradine) prescribing information, Amgen Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=92018a65-38f6-45f7-91d4-a34921b81d0d), label version 2026-11-09; accessed 2026-11-19.) Ivabradine is known to inhibit the HCN (If, "funny current") channel in the sinoatrial node, which slows the heart rate. This explains its use in angina and heart failure.

No plausible mechanistic link was identified between this action and hair follicle growth regulation. The very high TxGNN score (0.9979) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Several other top-ranked predictions are also hair-related or congenital syndromes, which points to the same effect. Without a mechanistic bridge or supporting studies, this prediction should be treated as a computational output only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

All five authorizations are listed as valid. Dosage form was not specified in the data.

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000597 | Procoralan | ivabradine hydrochloride | Valid |
| EMEA/H/C/000598 | Corlentor | ivabradine hydrochloride | Valid |
| EMEA/H/C/004117 | Ivabradine Zentiva | ivabradine hydrochloride | Valid |
| EMEA/H/C/004187 | Ivabradine Anpharm | ivabradine | Valid |
| EMEA/H/C/004241 | Ivabradine Accord | ivabradine hydrochloride | Valid |
| EMEA/H/C/004217 | Ivabradine JensonR | ivabradine hydrochloride | Withdrawn |

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. The first 20 retrieved included these **Major** interactions: aprepitant, clarithromycin, clotrimazole, cobicistat, cisapride, dolasetron, granisetron, levofloxacin, ondansetron, palonosetron and papaverine.
- **Moderate interactions** included famotidine, ranitidine, cimetidine, nizatidine, dexamethasone, miconazole, metreleptin and troglitazone.

Warnings and contraindications were not available in the compiled data. Please refer to the SmPC for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no publications and no plausible mechanistic link to ivabradine's HCN-channel action. It is supported only by a model score, so the evidence level is L5. In addition, no EU authorization for ivabradine is currently valid.

**Other predictions from the same analysis:**

**To proceed, the following is needed:**
- Any mechanistic or biological evidence linking HCN-channel inhibition to hair growth, or a decision to deprioritize this prediction
- Detailed mechanism-of-action data (MOA) from DrugBank
- Warnings and contraindications from the EMA product information
- Confirmation of the current EU regulatory status, since all five authorizations are listed as valid

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data was not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Corlanor (ivabradine) prescribing information, Amgen Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=92018a65-38f6-45f7-91d4-a34921b81d0d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

