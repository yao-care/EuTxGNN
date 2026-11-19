---
layout: default
title: Empagliflozin
parent: AI Predictions (L5)
nav_order: 221
evidence_level: L5
indication_count: 3
monitor_inn: "Empagliflozin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia"]
last_modified_at: 2026-11-20
description: "Empagliflozin: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus Jardiance is indicated in adults and childre…"
---

# Empagliflozin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Empagliflozin: Focal stiff limb syndrome
{: .text-alpha }

## One-Sentence Summary

Empagliflozin is an SGLT2 inhibitor originally used to treat type 2 diabetes mellitus, symptomatic chronic heart failure, and chronic kidney disease.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**, but **no clinical trials and no publications** currently support this prediction, so it is a model-based hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus Jardiance is indicated in adults and children aged 10 years and above for the treatment of insufficiently controlled type 2 diabetes mellitus as an adjunct to diet and exercise as monotherapy when metformin is considered inappropriate due to intolerance in addition to other  |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| EU Market Status | Marketed (valid licences: 3 of 3) |
| Number of Authorizations | 3 (valid: 3) |
| Recommended Decision | Hold |

Two other predictions were also generated: classic stiff person syndrome (0.9906) and opsismodysplasia (0.9903). Both likewise have no clinical or literature support (L5, Hold).

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for empagliflozin: "Empagliflozin is an inhibitor of SGLT2, the predominant transporter responsible for reabsorption of glucose from the glomerular filtrate back into the circulation. By inhibiting SGLT2, empagliflozin reduces renal reabsorption of filtered glucose and lowers the renal threshold for glucose, and thereby increases urinary glucose excretion." ([DailyMed: Jardiance (empagliflozin) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=faf3dd6a-9cd0-39c2-0d2e-232cb3f67565), label version 2026-11-10; accessed 2026-11-19.) Empagliflozin is known as an SGLT2 inhibitor that promotes urinary glucose excretion and has metabolic and possibly anti-inflammatory effects. Its efficacy in type 2 diabetes, heart failure, and chronic kidney disease is established, but none of these actions has a documented link to the pathophysiology of focal stiff limb syndrome.

Focal stiff limb syndrome belongs to the stiff person syndrome spectrum. These are autoimmune neurological disorders, often with anti-GAD65 antibodies, involving impaired GABAergic inhibitory signaling. They are usually managed with GABAergic agents and immunotherapy. The only conceivable bridge to empagliflozin is the co-occurrence of anti-GAD autoimmunity with diabetes, which does not provide a therapeutic rationale.

The identical scores for focal stiff limb syndrome and classic stiff person syndrome suggest the model is scoring a shared disease node rather than producing independent evidence. The high score should therefore be read as a computational signal only, not as support for efficacy.

For the third prediction, opsismodysplasia (a rare skeletal dysplasia linked to INPPL1/SHIP2 deficiency), there is a loose conceptual link through insulin signaling. Empagliflozin does not directly target that pathway or bone development, and pediatric use there would raise safety concerns.

---

## EU Market Information

<!-- licenses:begin -->

| Authorization Number | Product Name | Active Substance | Status |
|------|------|------|------|
| EMEA/H/C/002677 | Jardiance | empagliflozin | Valid |
| EMEA/H/C/003770 | Synjardy | empagliflozin; metformin | Valid |
| EMEA/H/C/003833 | Glyxambi | empagliflozin; linagliptin | Valid |

<!-- licenses:end -->

The data compiled for this report list 1 authorization, a single-ingredient product with valid status. The list is not partial.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded in the interaction database. The first 20 listed are mostly of Moderate level, for example:
  - Phenylephrine, acebutolol, acetazolamide, formoterol, pseudoephedrine, nifedipine, epinephrine, ethinylestradiol, hydrocortisone, salbutamol, ethanol, fosamprenavir, fosinopril, fosphenytoin, fostamatinib, fostemsavir, furosemide, gemifloxacin (Moderate)
  - Topical hydrocortisone and topical alclometasone (Minor)

Warnings and contraindications from the product label were not available in the data compiled for this report. Please refer to the SmPC for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN score, with no clinical trials or publications studying empagliflozin in focal stiff limb syndrome, so the evidence level is L5. No plausible mechanistic link to the disease can be established from the available data.

**To proceed, the following is needed:**
- Mechanism of action data for empagliflozin to enable a proper mechanistic-link analysis
- Label warnings and contraindications from the SmPC (currently missing, a blocking gap for safety screening)
- Any preclinical or clinical studies directly addressing empagliflozin in stiff person syndrome spectrum disorders
- A check of why the model gives identical scores to focal stiff limb syndrome and classic stiff person syndrome

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Jardiance (empagliflozin) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=faf3dd6a-9cd0-39c2-0d2e-232cb3f67565) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

