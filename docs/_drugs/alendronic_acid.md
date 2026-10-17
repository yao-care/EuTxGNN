---
layout: default
title: Alendronic Acid
parent: AI Predictions (L5)
nav_order: 34
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Alendronic Acid: predicted new indication HIV infectious disease (evidence level L5). Approved use: Treatment of postmenopausal osteoporosis in patients at risk of vitam…"
monitor_inn: "Alendronic acid"
predicted_indications: ["HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "deficiency anemia", "vitamin B12- and folate-independent constitutional megaloblastic anemia", "Plummer-Vinson syndrome", "osteomesopyknosis", "obsolete familial combined hyperlipidemia", "biotin metabolic disease"]
---

# Alendronic Acid
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

# Alendronic Acid: From Postmenopausal Osteoporosis to HIV Infectious Disease

## One-Sentence Summary

Alendronic acid is a bisphosphonate originally authorised in the EU (in combination products) for postmenopausal osteoporosis, where it reduces the risk of vertebral and hip fractures.
The TxGNN model predicts it may be effective for **HIV infectious disease**, but this is a knowledge-graph prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of postmenopausal osteoporosis in patients at risk of vitamin-D insufficiency (reduces the risk of vertebral and hip fractures) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 96.78% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorisations) |
| Number of Authorizations | 3 (all cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Alendronate is a nitrogen-containing bisphosphonate. Drugs of this class are generally understood to inhibit farnesyl pyrophosphate synthase in the mevalonate pathway, which could in theory affect protein prenylation and immune cell function. Nitrogen-containing bisphosphonates have also been studied for gamma-delta T cell activation.

The link to HIV is weak. Osteoporosis and HIV infection are pathologically distinct, and no direct connection to HIV pathology is established. HIV-associated bone loss is a related question, but it would be an osteoporosis indication rather than an antiviral one. The high score (0.968) should therefore be read as a graph-derived signal, not biological confirmation.

Other top-ranked predictions look like artefacts of the same graph signal or are biologically implausible:
- Feline AIDS and simian immunodeficiency virus infection (score 0.948 each) mirror the HIV result and are veterinary or animal-model conditions, not independent human indications.
- Deficiency anemia, megaloblastic anemia, and biotin metabolic disease have no plausible mechanistic link.
- Plummer-Vinson syndrome and osteomesopyknosis argue against use, because of oesophageal adverse events and further suppression of bone resorption respectively.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/001180 (cancelled) | Vantavo (previously Alendronate sodium and colecalciferol, MSD) | Not specified | Treatment of postmenopausal osteoporosis in patients at risk of vitamin-D insufficiency. Vantavo reduces the risk of ve... |
| EMEA/H/C/000759 (cancelled) | Adrovance | Not specified | Treatment of postmenopausal osteoporosis in patients at risk of vitamin-D insufficiency. Adrovance reduces the risk of ... |
| EMEA/H/C/000619 (cancelled) | Fosavance | Not specified | Treatment of postmenopausal osteoporosis in patients at risk of vitamin-D insufficiency. Fosavance reduces the risk of ... |

## Safety Considerations

**Contraindications suggested by the knowledge graph (not label text):** The following conditions are linked to alendronate through drug-disease contraindication edges and should be verified against the SmPC:
- Oesophageal and upper gastrointestinal disorders: achalasia, megaesophagus, oesophageal dyskinesia, oesophageal ulcer, oesophagitis (including eosinophilic and peptic), gastroesophageal reflux disease, gastritis, duodenitis
- Renal conditions: kidney disease, nephrolithiasis, nephrocalcinosis, acute urate nephropathy
- Mineral and vitamin disorders: hypercalcaemia, hyperphosphataemia, phosphorus metabolism disease, vitamin D deficiency, hypervitaminosis, osteomalacia, rickets
- Other: osteonecrosis of the jaw, atrial fibrillation, sarcoidosis, arteriosclerosis obliterans, pyoureter

**Drug Interactions:** 100 interactions were recorded, and the first 20 are summarised here.
- Moderate: calcium salts (acetate, carbonate, citrate, glubionate, gluconate, lactate, phosphate), magnesium salts (carbonate, chloride, citrate), aluminium hydroxide, magaldrate, attapulgite, kaolin, iron, acetylsalicylic acid, kanamycin. Several of these (minerals, antacids) are likely to reduce oral absorption of alendronate.
- Minor: famotidine, ranitidine, cimetidine.

For label-level warnings and contraindications, please refer to the SmPC.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV prediction rests solely on a knowledge-graph score, with no registered trials, no literature, and no established mechanism. All three EU authorisations for the original indication are cancelled, and the safety profile includes oesophageal and renal concerns.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological rationale linking bisphosphonate activity to HIV, such as in vitro or preclinical studies
- A literature and trial search specific to alendronate and HIV, distinguishing antiviral effects from HIV-associated bone loss
- Current SmPC warnings and contraindications, which are not available in the data compiled for this report
- Clarification of route and formulation compatibility
- Review of whether the current regulatory status (all authorisations cancelled) affects feasibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

