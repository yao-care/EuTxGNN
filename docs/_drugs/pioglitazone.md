---
layout: default
title: Pioglitazone
parent: AI Predictions (L5)
nav_order: 487
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Pioglitazone: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus (monotherapy, dual or triple oral therapy…"
---

# Pioglitazone
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

# Pioglitazone: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Pioglitazone is an oral insulin-sensitising drug originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (monotherapy, dual or triple oral therapy, and combination with insulin) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| EU Market Status | Cancelled only (all authorisations cancelled) |
| Number of Authorizations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pioglitazone is known as a thiazolidinedione that activates PPAR-gamma and improves insulin sensitivity. Its efficacy in type 2 diabetes is established, but any link to opsismodysplasia is speculative.

Opsismodysplasia is a rare skeletal dysplasia associated with INPPL1, a gene involved in PI3K/insulin signalling. The only plausible bridge to pioglitazone is this shared insulin-signalling biology. There is no clinical or literature evidence to support benefit. The high score (0.996) is a graph-based prediction only.

Other predictions in the list share the same limitation:

| Rank | Predicted Disease | Score | Evidence Level | Note |
|------|------|------|------|------|
| 2 | Classic stiff person syndrome | 99.50% | L5 | Hypothetical immunomodulatory or diabetes-related link |
| 3 | Focal stiff limb syndrome | 99.50% | L5 | Likely derived from similarity to the classic form |
| 4 | Thiamine-responsive dysfunction syndrome | 99.48% | L5 | Probably a diabetes-overlap association |
| 5–8 | Localised lipodystrophies (drug-induced, centrifugal, pressure-induced, idiopathic) | 99.18–99.30% | L5 | Theoretical PPAR-gamma adipogenesis rationale only |
| 9 | Pancreatic agenesis | 99.18% | L4 | Only indirect literature on type 2 diabetes |
| 10 | Autoimmune oophoritis | 98.06% | L5 | Speculative anti-inflammatory rationale |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for opsismodysplasia.

For reference, seven publications were retrieved for the rank-9 prediction (pancreatic agenesis). They are reviews and a comparator trial on thiazolidinediones or PPAR-gamma agonism in type 2 diabetes, and none address pancreatic agenesis directly:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20859539](https://pubmed.ncbi.nlm.nih.gov/20859539/) | 2010 | Review | Vasc Health Risk Manag | Pioglitazone plus alogliptin as a pathophysiologically sound combination in type 2 diabetes |
| [23680744](https://pubmed.ncbi.nlm.nih.gov/23680744/) | 2013 | Review | Hosp Pract (1995) | Pleiotropic effects of thiazolidinediones, including protection of beta-cell function |
| [15892654](https://pubmed.ncbi.nlm.nih.gov/15892654/) | 2005 | Review | Curr Mol Med | Clinical significance of PPAR-gamma agonism and potential beta-cell benefit |
| [22068250](https://pubmed.ncbi.nlm.nih.gov/22068250/) | 2012 | Review | Endocr Pract | Targeting insulin resistance and beta-cell dysfunction in prediabetes |
| [16644631](https://pubmed.ncbi.nlm.nih.gov/16644631/) | 2006 | Clinical trial | Diabetes Care | Muraglitazar (a different dual PPAR agonist) versus pioglitazone in type 2 diabetes |
| [12149047](https://pubmed.ncbi.nlm.nih.gov/12149047/) | 2002 | Review | Drugs | Rosiglitazone (a different thiazolidinedione) in type 2 diabetes |
| [15832493](https://pubmed.ncbi.nlm.nih.gov/15832493/) | 2002 | Review | Treat Endocrinol | Rosiglitazone profile in type 2 diabetes |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/002277 | Pioglitazone Accord (cancelled) | Not specified | Type 2 diabetes mellitus as monotherapy in adults inadequately controlled by diet and exercise, for whom metformin is inappropriate... |
| EMEA/H/C/002324 | Pioglitazone Actavis (cancelled) | Not specified | Second or third line treatment of type 2 diabetes mellitus as monotherapy, dual or triple oral therapy, or with insulin... |
| EMEA/H/C/000285 | Actos (cancelled) | Not specified | Type 2 diabetes mellitus as monotherapy, dual or triple oral therapy, or with insulin... |

---

## Safety Considerations

- **Disease contraindications flagged in the knowledge graph** (not taken from label text): kidney disease, liver disease, gallbladder disease, congestive heart failure, and a broad group of pituitary and gonadal hormone deficiencies (e.g. hypopituitarism, hypogonadotropic hypogonadism, Kallmann syndrome, Sheehan syndrome), as well as adrenocortical insufficiency/Addison disease, thymus gland disease and infectious disease.
- **Drug Interactions**: 100 interactions were found in the interaction database. Most of those shown are Moderate, for example with abiraterone, acetazolamide, alpelisib, epinephrine, ethanol, formoterol, hydrochlorothiazide, hydrocortisone, phenylephrine, pseudoephedrine and salbutamol. A few are Minor, such as nifedipine, ethinylestradiol and topical corticosteroids.

Label-level warnings and contraindications were not available. Please refer to the SmPC for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for opsismodysplasia is supported only by a graph-based model score. There are no clinical trials or publications, and the mechanistic link is speculative. All EU authorisations for pioglitazone are also cancelled.

**To proceed, the following is needed:**
- Mechanism of action data to assess whether PPAR-gamma activity could plausibly affect INPPL1/PI3K-related bone biology
- Preclinical or case-level evidence in opsismodysplasia (cell or animal models)
- Label-level warnings and contraindications from the SmPC, which are required before any safety screening
- Clarification of current regulatory and supply status in the EU, given that all licences are cancelled
- Re-evaluation of the lower-ranked predictions only if direct evidence emerges, since none currently have supporting trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

