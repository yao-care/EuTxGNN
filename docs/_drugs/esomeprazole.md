---
layout: default
title: Esomeprazole
parent: AI Predictions (L5)
nav_order: 243
evidence_level: L5
indication_count: 1
monitor_inn: "Esomeprazole"
predicted_indications: ["duodenal obstruction"]
last_modified_at: 2026-11-20
description: "Esomeprazole: predicted new indication duodenal obstruction (evidence level L5). Approved use: Nexium Control is indicated for the short-term treatment of reflux sy…"
---

# Esomeprazole
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

## Esomeprazole: proton pump inhibitor → duodenal obstruction (duodenal obstruction)
{: .text-alpha }

## One-Sentence Summary

Esomeprazole is a proton pump inhibitor that reduces stomach acid production.
The TxGNN model predicts it may be relevant to **duodenal obstruction**, but **no clinical trials and no publications** were found to support this direction, so it remains a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nexium Control is indicated for the short-term treatment of reflux symptoms (e.g. heartburn and acid regurgitation) in adults. |
| Predicted New Indication | duodenal obstruction |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for esomeprazole: "Esomeprazole belongs to a class of antisecretory compounds, the substituted benzimidazoles, that suppress gastric acid secretion by specific inhibition of the H+/K+ ATPase enzyme system at the secretory surface of the gastric parietal cell. Esomeprazole is protonated and converted in the acidic compartment of the parietal cell forming the active inhibitor, the achiral sulphenamide." ([DailyMed: Nexium (esomeprazole magnesium) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4853677-1622-4037-688b-fdf533a11d96), label version 2025-12-19; accessed 2026-11-19.) Based on general knowledge, esomeprazole belongs to the proton pump inhibitor class, which suppresses gastric acid secretion.

Duodenal obstruction is a mechanical condition, in which the passage through the duodenum is blocked. Acid suppression would not be expected to relieve a blockage itself. At most it could help with associated acid-related disease, such as ulcers in the upper gastrointestinal tract. The high score is therefore a computational signal only, and the mechanistic link is not established. Similarity to the original use has not been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

<!-- review:begin eu-lic-20261106-esomeprazole-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The EU authorization record for this single-ingredient product is marked as cancelled in the compiled licence list, while the overall market status is recorded as marketed." Removed: it described the products as single-ingredient or combination products in a way that did not match the EMA data (the EMA medicines data as of 2026-11-06). Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-esomeprazole-1 -->

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/002618 | Nexium Control | esomeprazole | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction query. Examples of those listed:
  - **Major**: acalabrutinib, atazanavir
  - **Moderate**: abametapir (topical), hydrochlorothiazide, amphotericin B, amikacin, amphetamine, fenofibrate, apalutamide, armodafinil, atorvastatin, bendamustine, bosutinib, bumetanide
  - **Minor**: acetylsalicylic acid, axitinib, bortezomib, brivaracetam, cyanocobalamin

Label warnings and contraindications were not available in the compiled data. Please refer to the SmPC for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (0.9945). No clinical trials or publications address duodenal obstruction, and the mechanism does not obviously fit a mechanical blockage.

**To proceed, the following is needed:**
- Clinical or observational studies that directly examine esomeprazole in duodenal obstruction
- Mechanism of action data and a clear rationale for how acid suppression would help
- Review of the SmPC warnings and contraindications
- Review of the major drug interactions for the intended patient population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The EU authorization record for this single-ingredient product is marked as cancelled in the compiled licence list, while the overall market" | Corrected | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nexium (esomeprazole magnesium) prescribing information, AstraZeneca Pharmaceuticals LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f4853677-1622-4037-688b-fdf533a11d96) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

