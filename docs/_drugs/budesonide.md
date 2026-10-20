---
layout: default
title: Budesonide
parent: Medium Evidence (L3-L4)
nav_order: 111
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-15
description: "Budesonide: predicted new indication Atopic eczema (evidence level L4). Approved use: Eosinophilic esophagitis (EoE) in adults (older than 18 years of age)"
monitor_inn: "Budesonide"
predicted_indications: ["atopic eczema", "bronchitis", "dermatitis, atopic", "polyp of vocal cord", "polyp of middle ear", "epulis", "fibroepithelial polyp", "uterine polyp", "polyp of frontal sinus", "polyp of external auditory canal"]
---

# Budesonide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Budesonide: From Eosinophilic Esophagitis to Atopic Eczema

## One-Sentence Summary

Budesonide is a glucocorticoid that was originally authorized in the EU (as Jorveza) for eosinophilic esophagitis in adults.
The TxGNN model predicts it may be effective for **atopic eczema**, but **no clinical trials** are registered for this indication, and the **20 publications** retrieved are mostly indirect (reviews, contact-allergy studies, and a preclinical formulation study).
The evidence is essentially model-prediction level, so this direction is not yet ready for advancement.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Eosinophilic esophagitis (EoE) in adults (older than 18 years of age) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| EU Market Status | Cancelled only (no currently valid authorization) |
| Number of Authorizations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, budesonide is a potent glucocorticoid with broad anti-inflammatory and immunosuppressive effects. Its efficacy in eosinophilic esophagitis, a type 2 inflammatory condition, has been demonstrated, and mechanistically it may be applicable to atopic eczema.

Eosinophilic esophagitis and atopic eczema both belong to the atopic/type 2 inflammatory disease spectrum, so a steroid-responsive mechanism is plausible. However, the supporting literature is largely indirect: reviews of EoE therapy, corticosteroid contact allergy and adrenal suppression papers, and a preclinical budesonide nanoparticle-hydrogel formulation study. Established topical corticosteroids already exist for atopic eczema, so the incremental value of budesonide is unclear.

Note that the same underlying disease also appears in the prediction list as "dermatitis, atopic" (score 99.81%). The two entries should be merged in downstream review to avoid double counting.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31705907](https://pubmed.ncbi.nlm.nih.gov/31705907/) | 2020 | Review | J Allergy Clin Immunol | Emerging EoE therapies, including swallowed topical steroid formulations optimized for mucosal deposition |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Intranasal corticosteroids and adrenal suppression (HPA axis effects) |
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Preclinical formulation study | Gels (Basel) | Budesonide-loaded pH-sensitive nanoparticles in hydrogels for local therapy of atopic dermatitis |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Review | Allergy | Corticosteroid contact and immediate allergy in asthma patients |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | Open longitudinal trial (n=14) | Pediatr Dermatol | Knemometry to assess short-term growth effects of topical budesonide in children with atopic dermatitis |
| [16428071](https://pubmed.ncbi.nlm.nih.gov/16428071/) | 2006 | In vitro study | Int Immunopharmacol | Budesonide, unlike tacrolimus, affects immune functions of normal human keratinocytes |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Patch-test study | Contact Dermatitis | Budesonide as a marker of corticosteroid hypersensitivity; decreasing allergy trend in Italy |
| [37927648](https://pubmed.ncbi.nlm.nih.gov/37927648/) | 2023 | Case report | Cureus | Steroid-induced angioedema and urticaria in a patient with a history of atopic dermatitis |
| [36713411](https://pubmed.ncbi.nlm.nih.gov/36713411/) | 2022 | Case report | Front Immunol | Dupilumab in IPEX syndrome (not a budesonide study) |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | Cross-sectional/cohort | Contact Dermatitis | Contact sensitization patterns in patients with and without atopic dermatitis |

---

## EU Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| EMEA/H/C/004655 | Jorveza | Not specified | Treatment of eosinophilic esophagitis (EoE) in adults (older than 18 years of age). (Status: cancelled) |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified. Selected higher-severity examples:
  - **Major**: adalimumab, fosamprenavir
  - **Moderate**: zidovudine, isotretinoin, acebutolol, ketorolac, nifedipine, ibuprofen, ethinylestradiol, fluvoxamine, aldesleukin, alemtuzumab, among others
  - **Minor**: formoterol, salbutamol
- **Knowledge-graph contraindication signals** (from a computational drug-disease knowledge graph, not from label text): hypertension, epilepsy, liver disease, gallbladder disease, hyperglycemia, congestive heart failure, herpes simplex virus keratitis, measles, several urea-cycle disorders, and various pituitary/growth hormone deficiency conditions. These need verification against the SmPC.
- **Literature-derived concerns for the predicted use**: adrenal suppression, growth effects in children, and corticosteroid contact allergy.

Please refer to the SmPC for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no clinical trials and the literature is indirect or preclinical. Established topical corticosteroids already treat atopic eczema, and the only EU authorization for budesonide in this data has been cancelled.

**To proceed, the following is needed:**
- Mechanism of action data to support the mechanistic-link analysis
- SmPC warnings and contraindications to complete safety screening
- Direct clinical evidence of budesonide in atopic eczema, such as controlled trials with a topical formulation
- Comparative evidence against existing topical corticosteroids
- A route and formulation compatibility assessment (not yet available)
- Merging of the "atopic eczema" and "dermatitis, atopic" entries in downstream review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

