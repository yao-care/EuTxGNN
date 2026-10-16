---
layout: default
title: Metformin
parent: AI Predictions (L5)
nav_order: 396
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Metformin: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus (adjunct to diet and exercise to improve gly…"
monitor_inn: "Metformin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "pancreatic agenesis", "idiopathic localized lipodystrophy", "homozygous familial hypercholesterolemia"]
---

# Metformin
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

# Metformin: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Metformin is a widely used oral glucose-lowering medicine, approved in the EU (mainly in fixed-dose combinations) for type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (adjunct to diet and exercise to improve glycaemic control in adults inadequately controlled on maximal tolerated metformin alone, or in combination with other glucose-lowering medicines) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (all 19 authorizations are cancelled) |
| Number of Authorizations | 19 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, metformin is an insulin-sensitizing glucose-lowering agent. Its efficacy in type 2 diabetes is established, and mechanistically it may be applicable to **focal stiff limb syndrome** only through indirect links.

Focal stiff limb syndrome belongs to the stiff-person spectrum of disorders, which are usually autoimmune. These disorders often co-occur with autoimmune diabetes, which may explain why the knowledge graph associates them with antidiabetic drugs. One speculative link is the anti-inflammatory effect of metformin through AMPK activation. No direct mechanistic evidence was found in the data compiled for this report, and the prediction should be treated as an unvalidated hypothesis.

The same score appears for classic stiff person syndrome (99.45%), which supports the view that the association is driven by the shared diabetes and autoimmunity context rather than by a demonstrated effect on stiffness or spasms.

## Other Predicted Indications (for context)

| Rank | Predicted Disease | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Classic stiff person syndrome | 99.45% | L5 | Association with anti-GAD autoimmunity and type 1 diabetes; not evidence that metformin treats the neurological condition |
| 3 | Opsismodysplasia | 99.40% | L5 | Speculative link through INPPL1/SHIP2 insulin-PI3K signalling |
| 4 | Thiamine-responsive dysfunction syndrome | 99.40% | L5 | Likely driven by the diabetes association; no established role for metformin |
| 5–7, 9 | Localized lipodystrophies (drug-induced, centrifugal, pressure-induced, idiopathic) | 98.90–99.06% | L5 | Insulin-sensitivity link is plausible, but these forms are localized and typically not metabolic |
| 8 | Pancreatic agenesis | 98.91% | L5 | Weak rationale: metformin cannot replace missing insulin, and the retrieved papers do not address this condition |
| 10 | Homozygous familial hypercholesterolemia | 92.30% | L4 | A 1988 in vitro study showed decreased cholesterol metabolism in fibroblasts; classed as a research question only |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for focal stiff limb syndrome.

## EU Market Information

All 19 authorizations are cancelled, and no currently valid single-ingredient or combination product was found. The five main entries are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002279 | Jentadueto | Not specified | Type 2 diabetes mellitus, as an adjunct to diet and exercise (linagliptin + metformin combination)... |
| EMEA/H/C/002672 | Xigduo | Not specified | Type 2 diabetes mellitus in adults, as an adjunct to diet and exercise (dapagliflozin + metformin)... |
| EMEA/H/C/000807 | Eucreas | Not specified | Type 2 diabetes mellitus in adults, as an adjunct to diet and exercise (vildagliptin + metformin)... |
| EMEA/H/C/000862 | Velmetia | Not specified | Type 2 diabetes mellitus, as an adjunct to diet and exercise (sitagliptin + metformin)... |
| EMEA/H/C/003770 | Synjardy | Not specified | Type 2 diabetes mellitus in adults and children aged 10 years and above (empagliflozin + metformin)... |

## Safety Considerations

- **Disease-level cautions from the knowledge graph** (these are graph-based contraindication links, not label text): liver failure and liver disease, kidney disease, congestive heart failure, pancreatitis, gallbladder disease, pyoureter, adrenocortical insufficiency, thymus gland disease, and a group of pituitary hormone deficiency and hypogonadotropic hypogonadism conditions.
- **Drug Interactions** (100 interactions recorded; examples from the data):
  - **Major**: acetazolamide, ethanol
  - **Moderate**: dolutegravir, abemaciclib, phenylephrine, ranitidine, formoterol, pseudoephedrine, ketorolac, nifedipine, epinephrine, ibuprofen, ethinylestradiol, hydrocortisone, salbutamol, hydrochlorothiazide, acetohexamide
  - **Minor**: acarbose, topical hydrocortisone, topical alclometasone

Label-based warnings and contraindications were not available in the data compiled for this report. Please refer to the SmPC for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score of 99.45%, with no clinical trials or publications. The mechanistic link, through shared autoimmune and diabetes associations, is indirect and unproven. In addition, all EU authorizations for metformin-containing products are currently cancelled.

**To proceed, the following is needed:**
- Targeted literature review on metformin or AMPK modulators in stiff-person spectrum disorders and autoimmune neurological conditions
- Mechanism of action data and a clear mechanistic rationale for stiff-limb disorders
- Preclinical or early clinical evidence of any effect on stiffness, spasms, or autoimmunity
- Review of the current EU regulatory status, including whether any metformin-containing product is still marketed
- Label-based safety review (SmPC warnings and contraindications), especially for renal and hepatic impairment, and a comparison with current standard therapy for stiff-person spectrum disorders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

