---
layout: default
title: Mexiletine
parent: AI Predictions (L5)
nav_order: 404
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Mexiletine: predicted new indication hypertrichosis (disease) (evidence level L5). Approved use: Symptomatic treatment of myotonia in adult patients with non-dystroph…"
monitor_inn: "Mexiletine"
predicted_indications: ["hypertrichosis (disease)", "nephrogenic syndrome of inappropriate antidiuresis", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "migraine disorder", "isolated genetic hair shaft abnormality", "pulmonary hypertension", "migraine with brainstem aura", "headache disorder"]
---

# Mexiletine
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

## Mexiletine: From Non-Dystrophic Myotonia to hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Mexiletine is a sodium channel blocker, originally authorised in the EU for the symptomatic treatment of myotonia in adults with non-dystrophic myotonic disorders.
The TxGNN model predicts it may be effective for **hypertrichosis**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Symptomatic treatment of myotonia in adult patients with non-dystrophic myotonic disorders |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for mexiletine: "Mexiletine hydrochloride is a local anesthetic, antiarrhythmic agent, structurally similar to lidocaine, but orally active. In animal studies, mexiletine has been shown to be effective in the suppression of induced ventricular arrhythmias, including those induced by glycoside toxicity and coronary artery ligation." ([DailyMed: mexiletine hydrochloride prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c09f68fa-759e-4772-9f6b-11005d8f83d5), label version 2026-03-31; accessed 2026-11-19.) Mexiletine is a class IB sodium channel blocker, and its efficacy in non-dystrophic myotonia is the basis of its EU authorisation.

Nothing in the available data links sodium channel blockade to the regulation of hair growth. The high score (0.9978) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No trials or publications support the prediction. At this stage it should be regarded as a hypothesis with no demonstrated plausibility.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/004584 | Namuscla | Mexiletine hydrochloride | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease contraindication links, not label text): epilepsy, liver disease, gallbladder disease, hypotensive disorder, myocardial infarction, coronary thrombosis, hemoglobinopathy, atrioventricular block, sick sinus syndrome and familial sick sinus syndrome. Most of these are cardiac conduction or ischaemic conditions, consistent with the proarrhythmic concerns of class I antiarrhythmics.
- **Drug Interactions**: 100 interactions were recorded. The main ones listed are:
  - **Major**: bupropion.
  - **Moderate**: alosetron, morphine, lorcaserin, potassium citrate, picosulfuric acid, polyethylene glycol (3350 with electrolytes), eliglustat, obeticholic acid, sodium sulfate, glycerol phenylbutyrate and rolapitant.
  - **Minor**: ascorbic acid.

Please refer to the SmPC for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hypertrichosis rests on a model score alone. Taking on mexiletine's cardiac and interaction risks is not justified for this indication.

<!-- review:begin eu-lic-20261031-mexiletine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The prediction for hypertrichosis rests on a model score alone. There are no clinical trials or literature, no plausible mechanism, and the only EU authorisation is cancelled." Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-10-31). The current number of EU marketing authorisations for this drug is shown in the Quick Overview and in the table under EU Market Information. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261031-mexiletine-1 -->

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological link between sodium channel blockade and hair growth
- Any preclinical or clinical evidence in hypertrichosis
- Label-based warnings and contraindications from the SmPC, and a safety review (cardiac risk, interaction burden)
- Clarification of current EU availability

<!-- review:begin eu-lic-20261106-mexiletine-2 -->

> **Review correction (2026-11-24)**: Originally stated: "Clarification of current EU availability, given the cancelled authorisation" Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-11-06). The current number of EU marketing authorisations for this drug is shown in the Quick Overview and in the table under EU Market Information. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-mexiletine-2 -->

**Note on other predicted indications:** In the same prediction list, **headache disorder** (rank 10, L3) and **migraine disorder** (rank 6, L4) have more support. They rest on small, uncontrolled reports of mexiletine in trigeminal autonomic cephalalgias, refractory chronic daily headache and SUNCT/SUNA. These are better candidates for further research than hypertrichosis, but they still lack controlled trials.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "There are no clinical trials or literature, no plausible mechanism, and the only EU authorisation is cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-24 | Removed: "given the cancelled authorisation" | Corrected (revised 2026-11-24; earlier version kept in the record) | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: mexiletine hydrochloride prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c09f68fa-759e-4772-9f6b-11005d8f83d5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

