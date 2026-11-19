---
layout: default
title: Hydroxocobalamin
parent: AI Predictions (L5)
nav_order: 303
evidence_level: L5
indication_count: 2
monitor_inn: "Hydroxocobalamin"
predicted_indications: ["esophageal varices without bleeding", "esophageal varices with bleeding"]
last_modified_at: 2026-11-20
description: "Hydroxocobalamin: predicted new indication Esophageal varices without bleeding (evidence level L5). Approved use: Treatment of known or suspected cyanide poisoning (given together wit…"
---

# Hydroxocobalamin
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

## Hydroxocobalamin: From Cyanide Poisoning to Esophageal Varices Without Bleeding
{: .text-alpha }

## One-Sentence Summary

Hydroxocobalamin is a form of vitamin B12 that is authorized in the EU as Cyanokit for known or suspected cyanide poisoning.
The TxGNN model predicts it may be useful for **esophageal varices without bleeding**,
but **no clinical trials and no publications** were found to support this prediction, so it rests on a model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of known or suspected cyanide poisoning (given together with decontamination and supportive measures) |
| Predicted New Indication | Esophageal varices without bleeding |
| TxGNN Prediction Score | 0.9923 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for hydroxocobalamin: "Cyanide is an extremely toxic poison. In the absence of rapid and adequate treatment, exposure to a high dose of cyanide can result in death within minutes due to the inhibition of cytochrome oxidase resulting in arrest of cellular respiration. […] Each hydroxocobalamin molecule can bind one cyanide ion by substituting it for the hydroxo ligand linked to the trivalent cobalt ion, to form cyanocobalamin, which is then excreted in the urine." ([DailyMed: Cyanokit (hydroxocobalamin) prescribing information, BTG INTERNATIONAL INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d56fcc8d-bd64-46ab-b0c0-2124bd745a6b), label version 2023-04-27; accessed 2026-11-19.) Generally, hydroxocobalamin is a vitamin B12 form that binds cyanide, which is the basis of its use in poisoning. It is also known to scavenge nitric oxide (NO).

A speculative link exists to the predicted use. NO-mediated widening of blood vessels in the gut region contributes to portal hypertension, which drives esophageal varices. In theory, an NO scavenger could affect this process. However, no preclinical or clinical data in the compiled material support this idea, and the link remains unverified.

The cyanide poisoning indication and esophageal varices are unrelated conditions, so the original use does not support the new one. The score for the bleeding form of the same condition is identical (0.9923), which suggests the model is driven by similarity between disease groups rather than evidence specific to either indication. Hydroxocobalamin's NO scavenging is also associated with a temporary rise in blood pressure, and its effect in portal hypertension is unknown.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/000806 | Cyanokit | hydroxocobalamin | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Contraindications recorded in the knowledge graph** (these are graph relations, not label text): hypertensive disorder and hypertension. This fits with the blood pressure rise linked to hydroxocobalamin's NO scavenging.
- **Drug Interactions**: 32 potential interactions were identified in total. The ones rated Moderate are:
  - Arsenic trioxide
  - Chloramphenicol
  - Iodide I-131
  - Iodide I-123

  Others, such as omeprazole, lansoprazole, simvastatin, prednisolone, acetylsalicylic acid, valsartan and ramipril, have an unknown severity level.
- **Theoretical concern**: The pressor effect could raise portal pressure or confound hemodynamic management, especially in variceal bleeding.

Please refer to the SmPC for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications on this disease, no verified mechanism, and a possible safety concern (blood pressure elevation). Established treatments already exist for esophageal varices, so there is no basis to proceed.

**To proceed, the following is needed:**
- Preclinical or mechanistic data showing that NO scavenging by hydroxocobalamin changes portal or splanchnic hemodynamics
- Mechanism of action data from DrugBank
- Warnings and contraindications from the EMA product information, for safety screening
- Assessment of the blood pressure effect in patients with portal hypertension
- Clarification of why the model gives the same score for bleeding and non-bleeding varices
- Route and dosage form compatibility assessment (cyanide poisoning is treated by intravenous administration, but the required route for the new use is not yet defined)

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data for hydroxocobalamin is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cyanokit (hydroxocobalamin) prescribing information, BTG INTERNATIONAL INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d56fcc8d-bd64-46ab-b0c0-2124bd745a6b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

