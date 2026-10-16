---
layout: default
title: Glimepiride
parent: AI Predictions (L5)
nav_order: 287
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Glimepiride: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus in patients intolerant to metformin (or for…"
---

# Glimepiride
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

# Glimepiride: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Glimepiride is a sulfonylurea antidiabetic drug, originally used to treat type 2 diabetes mellitus, and in the EU it was authorized as part of the pioglitazone/glimepiride combination Tandemact.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** currently supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus in patients intolerant to metformin (or for whom metformin is contraindicated) who are already treated with pioglitazone plus glimepiride (Tandemact) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Glimepiride is a sulfonylurea that is generally understood to close pancreatic beta-cell KATP channels and so promote insulin secretion. Its efficacy in type 2 diabetes is established, but its mechanism has not been shown to be applicable to focal stiff limb syndrome.

The link between the original and predicted indications is weak. Focal stiff limb syndrome belongs to the stiff-person spectrum, which is mainly autoimmune (often anti-GAD65 antibodies) and involves impaired GABAergic signalling. The high TxGNN score most likely reflects network proximity in the knowledge graph, such as the shared GAD65 autoimmunity seen in type 1 diabetes. It does not reflect a direct pharmacological rationale. No evidence suggests that KATP channel blockade relieves muscle rigidity or spasms.

The same score and the same caveats apply to classic stiff person syndrome, which was ranked immediately after this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/000680 (cancelled) | Tandemact | Not specified | Tandemact is indicated for the treatment of patients with type-2 diabetes mellitus who show intolerance to... |

---

## Safety Considerations

Safety data compiled for this report is limited, and no label-based warnings or contraindications were available. Please refer to the SmPC for authoritative safety information.

- **Knowledge-graph contraindication signals** (derived from the TxGNN knowledge graph, not from label text): kidney disease, liver disease, gallbladder disease, congestive heart failure, osteoporosis (including postmenopausal), thymus gland disease, infectious disease, and a range of pituitary and hypothalamic–gonadal disorders (for example hypopituitarism, growth hormone deficiency, hypogonadotropic hypogonadism, Kallmann syndrome, Sheehan syndrome).
- **Drug Interactions**: 100 interactions were found, and the 20 shown in the data are mostly of moderate severity. Examples include:
  - Phenylephrine, pseudoephedrine, epinephrine, salbutamol and formoterol
  - Acebutolol
  - Acetazolamide
  - Famotidine and ranitidine
  - Ibuprofen and ketorolac
  - Hydrochlorothiazide
  - Ethanol
  - Albiglutide
  - Acitretin
  - Ethinylestradiol
  - Hydrocortisone, systemic (moderate) and topical (minor)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. There are no trials or publications, and no plausible mechanism links a KATP channel blocker to a stiff-person-spectrum disorder. The only EU authorization is cancelled.

**To proceed, the following is needed:**
- Detailed mechanism of action data and a testable mechanistic hypothesis for stiff limb or stiff person syndromes
- Preclinical or case-level evidence of benefit
- Label-based safety data (warnings and contraindications) from the SmPC
- Clarification of why the product's EU authorization was cancelled

**Note on other predictions:** Among the other predicted indications, only type 1 diabetes mellitus has meaningful supporting material (Evidence Level L3). That evidence is mostly indirect: the trials use glimepiride as a comparator in type 2 diabetes, and a small adolescent study and case reports support use in residual beta-cell function or monogenic diabetes. It may be a better candidate for further evaluation than the indication assessed here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

