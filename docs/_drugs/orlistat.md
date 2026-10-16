---
layout: default
title: Orlistat
parent: AI Predictions (L5)
nav_order: 451
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Orlistat: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Treatment of obese patients (BMI ≥ 30 kg/m²) or overweight patients (…"
---

# Orlistat
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

# Orlistat: From Obesity and Overweight to Hypervitaminosis

## One-Sentence Summary

Orlistat is a gastrointestinal lipase inhibitor, originally used for weight management in obese and overweight adults.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but **no clinical trials and no publications** currently support this direction.
The prediction rests on model output alone, and the pharmacology points the other way: orlistat is known to *reduce* absorption of fat-soluble vitamins.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of obese patients (BMI ≥ 30 kg/m²) or overweight patients (BMI > 28 kg/m²) with associated risk factors, alongside a mildly hypocaloric diet |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 2 (both cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, orlistat inhibits gastric and pancreatic lipases, which reduces the absorption of dietary fat. Its efficacy in weight management is established, and the fat malabsorption it causes also lowers absorption of fat-soluble vitamins (A, D, E and K).

This is the only conceivable link to hypervitaminosis, and it is weak. Lowering vitamin absorption is a known **adverse effect** of orlistat, not a documented therapeutic benefit. No study in the compiled data tests orlistat for vitamin excess. The high TxGNN score is therefore best read as a computational association, not as evidence of clinical utility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

Both EU authorizations have been cancelled, so orlistat has no currently valid EU marketing authorization in the compiled data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000154 | Xenical | Not specified | Treatment of obese patients with BMI ≥ 30 kg/m², or overweight patients (BMI > 28 kg/m²) with associated risk fact... |
| EMEA/H/C/000854 | Alli (previously Orlistat GSK) | Not specified | Weight loss in adults who are overweight (BMI 28 kg/m²), taken with a mildly hypocaloric, lower-fat diet. |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these come from drug-disease links in the model's knowledge graph, not from label text): liver failure, primary hyperoxaluria, anorexia nervosa, bulimia nervosa, vitamin deficiency disorder, cholestasis, benign recurrent intrahepatic cholestasis, familial intrahepatic cholestasis, and drug-induced liver injury.
  - The flag for **vitamin deficiency disorder** is consistent with orlistat's effect on fat-soluble vitamin absorption. That effect runs opposite to any benefit in hypervitaminosis.
- **Drug Interactions**: The query returned 100 interactions, most rated Moderate. The main ones in the data reviewed include:
  - Antidiabetic agents: acarbose, albiglutide, alogliptin, canagliflozin, chlorpropamide, metformin.
  - Antiretrovirals: abacavir, lamivudine, emtricitabine, atazanavir.
  - Other: amiodarone, cannabidiol, clofarabine, brentuximab vedotin, and the asparaginase products (*E. coli*, *Erwinia chrysanthemi*, calaspargase pegol).
  - Minor interactions are listed with the fat-soluble vitamin analogues cholecalciferol, calcifediol and calcitriol.

Please refer to the SmPC for label warnings and contraindications, which were not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has no clinical or literature support (L5, model prediction only).
- The known pharmacology, reduced absorption of fat-soluble vitamins, is an adverse effect rather than a therapeutic rationale.
- Orlistat currently has no valid EU marketing authorization.

**To proceed, the following is needed:**
- Mechanism of action data (MOA), together with a documented rationale for why lipase inhibition would treat vitamin excess.
- Label warnings and contraindications from the SmPC, to complete safety screening.
- Any preclinical or clinical study of orlistat in hypervitaminosis.

**Note on other candidates:** Among the other model predictions for orlistat, **fatty liver disease** is the best supported. It has two completed Phase 4 trials (NCT00160407, n=50; NCT00207311, n=30), a 2023 randomized controlled trial of orlistat versus diet in obesity with metabolic-associated fatty liver disease (PMID 36781126), and a 2024 meta-analysis of randomized trials (PMID 38910819). Any benefit is likely driven by weight loss rather than a liver-specific effect. This candidate would be a more productive starting point for further evaluation than hypervitaminosis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

