---
layout: default
title: Empagliflozin
parent: AI Predictions (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Empagliflozin: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus (adults and children aged 10 years and above…"
---

# Empagliflozin
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

# Empagliflozin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Empagliflozin is an SGLT2 inhibitor originally used to treat type 2 diabetes mellitus, and it is also approved for chronic heart failure and chronic kidney disease.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, but the data compiled for this report contain **0 clinical trials** and **0 publications** supporting this prediction. The prediction is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (adults and children aged 10 years and above, insufficiently controlled, as an adjunct to diet and exercise) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (the single EU authorization is recorded as cancelled) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Empagliflozin is known as a renal SGLT2 inhibitor that lowers blood glucose independently of insulin, and its efficacy in type 2 diabetes, heart failure and chronic kidney disease is established.

No mechanistic link to stiff person syndrome has been established. Stiff person syndrome is an autoimmune neurological disorder, typically with anti-GAD65 antibodies and impaired GABAergic signalling. Empagliflozin has no known action on GABAergic or autoimmune pathways. The high score (0.99) is most likely a knowledge-graph artifact, possibly through the shared association of GAD65 autoimmunity with diabetes.

The second-ranked prediction, focal stiff limb syndrome, has an identical score and the same pathophysiology. This suggests both come from the same graph neighbourhood rather than independent evidence.

Other top-ranked predictions are also weakly supported:
- **Opsismodysplasia** (99.03%): rare skeletal dysplasia (INPPL1/SHIP2); any link is speculative.
- **Thiamine-responsive dysfunction syndrome** (98.99%): shares only diabetes as a superficial connection; the underlying defect is thiamine transport.
- **Localized lipodystrophies** (drug-induced, centrifugal, pressure-induced, idiopathic; 98.2–98.5%): likely reflect graph proximity to metabolic terms, with no known role for empagliflozin.
- **Pancreatic agenesis** (98.07%): the only candidate with retrieved literature, but the two papers concern type 2 diabetes and diabetic retinopathy, so they are indirect at best. Empagliflozin cannot replace insulin in patients lacking insulin production and carries a ketoacidosis risk.
- **Autoimmune oophoritis** (92.37%): no data link SGLT2 inhibitor effects to ovarian autoimmunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002677 (cancelled) | Jardiance | Not specified | Type 2 diabetes mellitus in adults and children aged 10 years and above, insufficiently controlled, as an adjunct to diet and exercise... |

The same authorization also covers symptomatic chronic heart failure and chronic kidney disease in adults.

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction database. The first 20 retrieved are mostly Moderate, and a few are Minor. Examples of Moderate interactions: phenylephrine, acebutolol, acetazolamide, formoterol, pseudoephedrine, nifedipine, epinephrine, ethinylestradiol, hydrocortisone, salbutamol, ethanol, furosemide and fosinopril. Minor examples: topical hydrocortisone and topical alclometasone.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications, and no plausible mechanistic link between SGLT2 inhibition and the GABAergic or autoimmune pathophysiology of stiff person syndrome. The identical scores of related predictions suggest a graph artifact. The EU authorization is also recorded as cancelled.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- Warnings and contraindications from the current EU product information
- Preclinical or mechanistic evidence for any link to GABAergic or autoimmune pathways
- Confirmation of the current EU market status of empagliflozin products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

