---
layout: default
title: Orlistat
parent: AI Predictions (L5)
nav_order: 451
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "Orlistat"
predicted_indications: ["hypervitaminosis"]
description: "Orlistat: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Xenical is indicated in conjunction with a mildly hypocaloric diet fo…"
---

# Orlistat
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

## Orlistat: Hypervitaminosis
{: .text-alpha }

## One-Sentence Summary

Orlistat is a gastrointestinal lipase inhibitor, originally used for weight management in obese and overweight adults.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but **no clinical trials and no publications** currently support this direction.
The prediction rests on model output alone, and the pharmacology points the other way: orlistat is known to *reduce* absorption of fat-soluble vitamins.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Xenical is indicated in conjunction with a mildly hypocaloric diet for the treatment of obese patients with a body mass index (BMI) greater or equal to 30 kg/m2, or overweight patients (BMI &gt; 28 kg/m2) with associated risk factors. Treatment with orlistat should be discontinued after 12 weeks if  |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 2 of 2) |
| Number of Authorizations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for orlistat: "Orlistat is a reversible inhibitor of gastrointestinal lipases. It exerts its therapeutic activity in the lumen of the stomach and small intestine by forming a covalent bond with the active serine residue site of gastric and pancreatic lipases." ([DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e), label version 2026-09-30; accessed 2026-11-19.) Based on known pharmacology, orlistat inhibits gastric and pancreatic lipases, which reduces the absorption of dietary fat. Its efficacy in weight management is established, and the fat malabsorption it causes also lowers absorption of fat-soluble vitamins (A, D, E and K).

This is the only conceivable link to hypervitaminosis, and it is weak. Lowering vitamin absorption is a known **adverse effect** of orlistat, not a documented therapeutic benefit. No study in the compiled data tests orlistat for vitamin excess. The high TxGNN score is therefore best read as a computational association, not as evidence of clinical utility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000154 | Xenical | orlistat | Valid |
| EMEA/H/C/000854 | Alli | orlistat | Valid |

<!-- licenses:end -->

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

**To proceed, the following is needed:**
- Mechanism of action data (MOA), together with a documented rationale for why lipase inhibition would treat vitamin excess.
- Label warnings and contraindications from the SmPC, to complete safety screening.
- Any preclinical or clinical study of orlistat in hypervitaminosis.

Any benefit is likely driven by weight loss rather than a liver-specific effect. This candidate would be a more productive starting point for further evaluation than hypervitaminosis.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

