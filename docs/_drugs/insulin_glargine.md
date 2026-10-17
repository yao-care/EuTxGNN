---
layout: default
title: Insulin Glargine
parent: AI Predictions (L5)
nav_order: 327
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Insulin Glargine: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Treatment of diabetes mellitus in adults…"
monitor_inn: "Insulin glargine"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Insulin Glargine
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

# Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin glargine is a long-acting insulin analogue, originally used to treat diabetes mellitus in adults, adolescents and children.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but **no clinical trials and no publications** currently support this prediction.
It is a graph-based prediction only, and the apparent link is probably explained by the shared association between autoimmune conditions and type 1 diabetes, not by a therapeutic effect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Treatment of diabetes mellitus in adults, adolescents and children aged 2 years and above |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (all authorizations cancelled) |
| Number of Authorizations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin glargine is a long-acting basal insulin analogue, its efficacy in diabetes mellitus is established, and it acts as metabolic replacement therapy by lowering blood glucose.

For autoimmune oophoritis, no direct mechanistic link has been established. The high score is most likely a network association. Autoimmune oophoritis is often part of polyglandular autoimmune syndromes that include type 1 diabetes, so the two conditions sit close together in the knowledge graph. Insulin glargine has no known effect on ovarian autoimmunity.

Other top-ranked predictions follow a similar pattern. Several (thiamine-responsive dysfunction syndrome, classic stiff person syndrome, focal stiff limb syndrome, pancreatic agenesis) are linked through co-existing diabetes. In these cases insulin would treat the diabetic component, not the underlying disease. Drug-induced localized lipodystrophy reflects a known adverse effect of insulin injections, not a benefit, and should be read as a safety signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for autoimmune oophoritis.

For reference, the only literature retrieved among the top ten predictions relates to a lower-ranked prediction, pancreatic agenesis (rank 6), and is indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | J Am Pharm Assoc | Review of insulin therapy in type 2 diabetes and how to start it |
| [19322513](https://pubmed.ncbi.nlm.nih.gov/19322513/) | 2009 | Review | Acta Diabetol | Secondary diabetes associated with endocrine disorders and the effect of new treatments |
| [32871938](https://pubmed.ncbi.nlm.nih.gov/32871938/) | 2020 | Case report | Medicine | MODY5 case treated with a GLP-1 receptor agonist |
| [25818213](https://pubmed.ncbi.nlm.nih.gov/25818213/) | 2015 | Cohort (veterinary) | J Vet Intern Med | Pancreatic enzymes and ultrasound findings in diabetic cats |

None of these studies tests insulin glargine in pancreatic agenesis or in autoimmune oophoritis.

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002835 | Abasaglar (previously Abasria) | Not specified | Treatment of diabetes mellitus in adults, adolescents and children aged 2 years and above. |
| EMEA/H/C/004280 | Semglee | Not specified | Treatment of diabetes mellitus in adults, adolescents and children aged 2 years and above. |
| EMEA/H/C/000284 | Lantus | Not specified | Treatment of diabetes mellitus in adults, adolescents and children aged two years and above |
| EMEA/H/C/000309 | Toujeo (previously Optisulin) | Not specified | Treatment of diabetes mellitus in adults, adolescents and children from the age of 6 years. |

All four authorizations are listed as cancelled.

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction screening. The main ones shown are mostly Moderate severity:
  - Other glucose-lowering drugs (metformin, pioglitazone, alogliptin, albiglutide), which may add to the glucose-lowering effect
  - Sympathomimetics and beta-agonists (epinephrine, phenylephrine, pseudoephedrine, salbutamol, formoterol), which may blunt glucose control
  - Corticosteroids (hydrocortisone), estrogens (estradiol, ethinylestradiol), hydrochlorothiazide, acetazolamide, doxycycline, alcohol, acebutolol and alpelisib
  - Topical corticosteroids (hydrocortisone, alclometasone) are rated Minor
- **Injection-site effects**: Insulin injections are a known cause of localized lipohypertrophy and lipoatrophy. This is relevant to the lipodystrophy predictions.

Please refer to the SmPC for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or publications and no plausible direct mechanism. The market status is also cancelled for all current EU licenses. Insulin glargine would at most manage co-existing diabetes in these conditions.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic rationale for ovarian autoimmunity
- Warnings and contraindications from the SmPC
- Literature or trial evidence in autoimmune oophoritis
- Clarification of the cancelled EU market status and of available routes and formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

