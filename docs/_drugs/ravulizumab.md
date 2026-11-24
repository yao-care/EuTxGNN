---
layout: default
title: Ravulizumab
parent: AI Predictions (L5)
nav_order: 511
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Ravulizumab: predicted new indication Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency (evidence level L5). Approved use: Paroxysmal nocturnal haemoglobinuria (PNH) in adult and…"
monitor_inn: "Ravulizumab"
predicted_indications: ["autosomal recessive severe congenital neutropenia due to G6PC3 deficiency", "cyclic hematopoiesis", "primary hyperoxaluria", "severe congenital neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "pseudo-von Willebrand disease", "X-linked severe congenital neutropenia", "primary release disorder of platelets", "megaloblastic anemia (disease)"]
---

# Ravulizumab
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

## Ravulizumab: From Paroxysmal Nocturnal Haemoglobinuria to Autosomal Recessive Severe Congenital Neutropenia due to G6PC3 Deficiency
{: .text-alpha }

## One-Sentence Summary

Ravulizumab (Ultomiris) is a long-acting C5 complement inhibitor, originally used to treat paroxysmal nocturnal haemoglobinuria (PNH), atypical haemolytic uraemic syndrome (aHUS), generalized myasthenia gravis and neuromyelitis optica spectrum disorder.
The TxGNN model predicts it may be effective for **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**,
but **no clinical trials and no publications** currently support this prediction. It is a model-only signal (Evidence Level L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Paroxysmal nocturnal haemoglobinuria (PNH) in adult and paediatric patients with a body weight of 10 kg or above (also aHUS, gMG and NMOSD) |
| Predicted New Indication | Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 1 of 1) |
| Number of Authorizations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for ravulizumab: "Ravulizumab-cwvz is a terminal complement inhibitor that specifically binds to the complement protein C5 with high affinity, thereby inhibiting its cleavage to C5a (the proinflammatory anaphylatoxin) and C5b (the initiating subunit of the membrane attack complex [MAC or C5b-9]) thus preventing MAC formation. ULTOMIRIS inhibits terminal complement-mediated intravascular hemolysis in patients with PNH and complement-mediated thrombotic microangiopathy (TMA) in patients with aHUS." ([DailyMed: Ultomiris (ravulizumab) prescribing information, Alexion Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a9a590d9-0217-43c7-908d-e62a71279791), label version 2026-10-29; accessed 2026-11-19.) Based on known information, ravulizumab is a monoclonal antibody that inhibits complement component C5. Its efficacy in complement-mediated diseases such as PNH and aHUS has been established.

For the predicted indication, no mechanistic link is established. G6PC3 deficiency is a metabolic defect in neutrophil glucose-6-phosphatase activity that leads to neutrophil apoptosis and endoplasmic reticulum stress. Complement-mediated pathology is not a recognized driver of this disease. The high TxGNN score (0.9996) is a computational prediction, probably reflecting shared network features among related blood disorders rather than a pharmacological basis.

Other highly ranked predictions show the same pattern. They include cyclic haematopoiesis, primary hyperoxaluria, severe congenital neutropenia (several subtypes), pseudo-von Willebrand disease, primary release disorder of platelets and megaloblastic anaemia. None has trial or literature support, and none has a recognized complement-driven mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/004954 | Ultomiris | ravulizumab | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Contraindication signal (knowledge graph)**: The TxGNN knowledge graph lists a contraindication with **meningococcal infection**. This comes from graph data, not from label text.
- **Drug Interactions**: Four interactions were identified, all rated Minor. They involve human immunoglobulin G in its intravenous, subcutaneous, intramuscular, and combined intravenous and subcutaneous forms.
- **Additional concern for the predicted populations**: Complement inhibition increases the risk of infection with encapsulated bacteria. Using it in patients who are already immunodeficient or neutropenic (for example, p14 deficiency or congenital neutropenia) raises a particular safety concern. C5 blockade could also further impair innate immune defence in CXCR2 deficiency through reduced C5a signalling.

Please also refer to the SmPC for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No trials or publications support it, no mechanistic link to complement is known, and the infection risk of complement inhibition is a safety concern in neutropenic patients.

<!-- review:begin eu-lic-20261106-ravulizumab-1 -->

> **Review correction (2026-11-24)**: Originally stated: "No trials or publications support it, no mechanistic link to complement is known, and the infection risk of complement inhibition is a safety concern in neutropenic patients. The EU authorization is also recorded as cancelled." Removed: it said the EU marketing authorisations were cancelled, discontinued, or not current, which did not match the EMA data (the EMA medicines data as of 2026-11-06). The current number of EU marketing authorisations for this drug is shown in the Quick Overview and in the table under EU Market Information. Source: [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines).

<!-- review:end eu-lic-20261106-ravulizumab-1 -->

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and a plausible biological link between C5 inhibition and G6PC3-deficiency neutropenia
- Preclinical or mechanistic studies supporting the hypothesis
- Warnings and contraindications from the SmPC, to allow safety screening
- Confirmation of the current EU authorization status of Ultomiris
- A risk assessment of meningococcal and other encapsulated-bacteria infections in neutropenic patients

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official European Medicines Agency data (centrally authorised medicines). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "The EU authorization is also recorded as cancelled" | Corrected (revised 2026-11-24; earlier version kept in the record) | [EMA – Medicines (centrally authorised)](https://www.ema.europa.eu/en/medicines) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Ultomiris (ravulizumab) prescribing information, Alexion Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a9a590d9-0217-43c7-908d-e62a71279791) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

